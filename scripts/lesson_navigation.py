"""Cross-page study navigation backed by membership and English morphology.

Reading-order heuristics are deliberately not etymological evidence.
"""
import collections
import hashlib
import json
from pathlib import PurePosixPath

from build_catalog import components

AFFIX_GROUP = '03_词缀与组合形式'


class LessonNavigation:
    def __init__(self, roots, lessons, words, lexicon, overrides=None):
        self.roots = {r['id']: r for r in roots}
        self.lessons = lessons
        self.words = words
        self.members = collections.defaultdict(list)
        self.parents = collections.defaultdict(set)
        self.overrides = overrides or {}
        for root in roots:
            if root['id'] in lessons:
                for word in root['family']:
                    self.members[word].append(root['id'])
        for word in words:
            for entry in lexicon.get(word, []):
                if entry.get('lang_code') not in (None, 'en'):
                    continue
                for sense in entry.get('senses', []):
                    for field in ('form_of', 'alt_of'):
                        for record in sense.get(field, []):
                            parent = record.get('word')
                            if parent in words and parent != word:
                                self.parents[word].add(parent)
                for template in entry.get('etymology_templates', []):
                    if any(k.startswith('lang') and value != 'en'
                           for k, value in template.get('args', {}).items()):
                        continue
                    for parent in components(template):
                        if parent != word and parent in words and not parent.startswith('-') and not parent.endswith('-'):
                            self.parents[word].add(parent)
        for word, config in self.overrides.items():
            assert word in words, ('Unknown navigation word', word)
            for rid in config.get('roots', []):
                assert rid in lessons and self.roots[rid]['group'] != AFFIX_GROUP, rid
            for rid in config.get('components', []):
                assert rid in lessons and self.roots[rid]['group'] == AFFIX_GROUP, rid
            for parent in config.get('bases', []):
                assert parent in words and parent != word, (word, parent)
                self.parents[word].add(parent)
        self.cache = {}

    def is_root(self, rid):
        return self.roots[rid]['group'] != AFFIX_GROUP

    def targets(self, word):
        if word in self.cache:
            return self.cache[word]
        direct = [dict(root_id=rid, via=word, kind='root', chain=[word])
                  for rid in self.members[word] if self.is_root(rid)]
        direct += [dict(root_id=rid, via=word, kind='root', chain=[word],
                        evidence=self.overrides[word]['note'])
                   for rid in self.overrides.get(word, {}).get('roots', [])]
        direct += [dict(root_id=rid, via=word, kind='component', chain=[word],
                        evidence=self.overrides[word]['note'])
                   for rid in self.overrides.get(word, {}).get('components', [])]
        # Follow only explicit dictionary morphology or a reviewed override.
        # Never infer a root from matching letters or learning-order links.
        queue = collections.deque([(word, [word])])
        seen = {word}
        bases = []
        while queue:
            current, chain = queue.popleft()
            for parent in sorted(self.parents[current]):
                if parent in seen:
                    continue
                seen.add(parent)
                path = chain + [parent]
                for rid in self.members[parent]:
                    item = dict(root_id=rid, via=parent, kind='root' if self.is_root(rid) else 'base', chain=path)
                    if self.is_root(rid):
                        direct.append(item)
                    else:
                        bases.append(item)
                queue.append((parent, path))
        # A complete root/base page is the primary destination. If none
        # exists, a verified base's word section can still be useful.
        if direct:
            chosen = direct
        else:
            # The same base may appear in several large suffix lessons.
            # Link once, preferring its most focused lesson over duplicates.
            by_base = {}
            for item in sorted(bases, key=lambda item: (
                    len(item['chain']), len(self.roots[item['root_id']]['family']),
                    self.roots[item['root_id']]['rank'], item['root_id'])):
                by_base.setdefault(item['via'], item)
            chosen = list(by_base.values())
        unique = {}
        for item in chosen:
            key = (item['root_id'], item['via'] if item['kind'] == 'base' else None)
            unique.setdefault(key, item)
        result = sorted(unique.values(), key=lambda item: (
            self.roots[item['root_id']]['group'], len(item['chain']),
            self.roots[item['root_id']]['rank'], item['root_id'], item['via']))
        self.cache[word] = result
        return result

    def links(self, word, source):
        result = []
        for item in self.targets(word):
            dest = self.roots[item['root_id']]
            if item['root_id'] == source['id'] and item['via'] == word:
                continue
            path = str(PurePosixPath('..') / dest['file'])
            if item['kind'] == 'base':
                anchor = dest['word_anchors'][item['via']]
                path += f'#w-{anchor}'
                label = f'{item["via"]}（基础词讲解）'
            else:
                label = dest['root'] + ('（构词成分）' if item['kind'] == 'component' else '')
            result.append(f'[{label}]({path})')
        return result

    def write_audit(self, output):
        rows = []
        counts = collections.Counter()
        unique = set()
        for root in self.roots.values():
            if root['id'] not in self.lessons or root['group'] != AFFIX_GROUP:
                continue
            for word in root['family']:
                targets = self.targets(word)
                links = self.links(word, root)
                status = ('root_lesson' if any(t['kind'] == 'root' for t in targets)
                          else 'component_lesson' if any(t['kind'] == 'component' for t in targets)
                          else 'base_lesson' if links else 'no_verified_destination')
                counts[status] += 1
                unique.add(word)
                rows.append(dict(page_id=root['id'], word=word, status=status, targets=targets, links=links))
        summary = dict(affix_pages=sum(r['group'] == AFFIX_GROUP and r['id'] in self.lessons for r in self.roots.values()),
                       unique_words=len(unique), word_occurrences=len(rows), **counts)
        digest = hashlib.sha256(json.dumps({'roots': self.lessons, 'words': self.words}, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        report = dict(summary=summary, authored_sha256=digest, policy='仅链接已完成精讲页；依据词族收录、词典明确英语构词或人工核对。基础词链接不表示该词是历史祖先；没有可靠目标的情况不猜配。', entries=rows)
        (output / 'data/词缀词根导航检查.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
        lines = ['# 词缀精讲的词根导航检查', '',
                 f'已检查全部 {summary["affix_pages"]} 个词缀精讲页、{len(unique)} 个去重单词（{len(rows)} 处讲解）。', '',
                 f'- {counts["root_lesson"]} 处有对应词根／词基精讲页。',
                 f'- {counts["component_lesson"]} 处跳到经过单独核对的构词成分精讲页。',
                 f'- {counts["base_lesson"]} 处可跳到经过构词核对的基础词讲解。',
                 f'- {counts["no_verified_destination"]} 处没有可靠的独立跳转目标；保留原有词源讲解，不按字母猜配词根。', '',
                 '完整逐词结果保存在 `data/词缀词根导航检查.json`。以下逐页列出没有独立目标的单词，便于继续复核；这不表示它们没有词源或没有精讲。', '']
        missing = collections.defaultdict(list)
        for row in rows:
            if row['status'] == 'no_verified_destination':
                missing[row['page_id']].append(row['word'])
        for rid, names in missing.items():
            root = self.roots[rid]
            lines += [f'## [{root["root"]}](../{root["file"]})', '', '、'.join(names), '']
        (output / '参考资料/词缀词根导航检查.md').write_text('\n'.join(lines))
        return summary
