import unittest

from lesson_navigation import LessonNavigation, AFFIX_GROUP


def root(rid, name, group, words, rank=1):
    return dict(id=rid, root=name, group=group, rank=rank,
                file=f'{group}/{rid}.md', family=dict.fromkeys(words, {}),
                word_anchors={word: i for i, word in enumerate(words, 1)})


class NavigationTests(unittest.TestCase):
    def setUp(self):
        self.affix = root('A1', '-less', AFFIX_GROUP, ['harm', 'harmless', 'harmful', 'inferior'])
        self.harm = root('B1', 'harm', '02_英语词基', ['harm'])
        self.fer = root('C1', 'fer-', '01_古典词根', ['infer'])
        self.roots = [self.affix, self.harm, self.fer]
        self.lessons = {r['id']: {} for r in self.roots}
        self.words = dict.fromkeys(['harm', 'harmless', 'harmful', 'infer', 'inferior'], {})

    def nav(self, lexicon=None, overrides=None):
        return LessonNavigation(self.roots, self.lessons, self.words, lexicon or {}, overrides)

    def test_direct_membership_links_to_root_page(self):
        self.assertEqual(self.nav().links('harm', self.affix), ['[harm](../02_英语词基/B1.md)'])

    def test_verified_english_component_reaches_root(self):
        lex = {'harmless': [{'etymology_templates': [
            {'name': 'suffix', 'args': {'1': 'en', '2': 'harm', '3': 'less'}}]}]}
        target = self.nav(lex).targets('harmless')[0]
        self.assertEqual(target['root_id'], 'B1')
        self.assertEqual(target['chain'], ['harmless', 'harm'])

    def test_spelling_and_foreign_operands_do_not_create_roots(self):
        lex = {'inferior': [{'etymology_templates': [
            {'name': 'suffix', 'args': {'1': 'la', '2': 'infer', '3': 'ior'}}]}]}
        self.assertEqual(self.nav(lex).targets('inferior'), [])
        self.assertEqual(self.nav().targets('harmless'), [])

    def test_incomplete_root_is_not_labeled_as_full_lesson(self):
        del self.lessons['B1']
        self.assertEqual(self.nav().targets('harm'), [])

    def test_dictionary_word_form_links_to_its_base(self):
        lex = {'harmful': [{'senses': [{'form_of': [{'word': 'harm'}]}]}]}
        self.assertEqual(self.nav(lex).targets('harmful')[0]['root_id'], 'B1')

    def test_reviewed_component_is_labeled_separately(self):
        override = {'inferior': {'components': ['A1'], 'note': 'Fixture component'}}
        self.assertEqual(self.nav(overrides=override).links('inferior', self.fer),
                         ['[-less（构词成分）](../03_词缀与组合形式/A1.md)'])

    def test_duplicate_base_prefers_focused_lesson(self):
        del self.lessons['B1']
        focused = root('A2', '-itude', AFFIX_GROUP, ['harm'], rank=50)
        self.roots.append(focused)
        self.lessons['A2'] = {}
        nav = self.nav(overrides={'harmless': {'bases': ['harm'], 'note': 'Reviewed'}})
        self.assertEqual(nav.links('harmless', self.affix),
                         ['[harm（基础词讲解）](../03_词缀与组合形式/A2.md#w-1)'])

    def test_base_fallback_uses_stable_anchor_and_handles_cycles(self):
        del self.lessons['B1']
        overrides = {'harmless': {'bases': ['harm'], 'note': 'Reviewed'},
                     'harm': {'bases': ['harmless'], 'note': 'Cycle fixture'}}
        self.assertEqual(self.nav(overrides=overrides).links('harmless', self.affix),
                         ['[harm（基础词讲解）](../03_词缀与组合形式/A1.md#w-1)'])


if __name__ == '__main__':
    unittest.main()
