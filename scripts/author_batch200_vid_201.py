# -*- coding: utf-8 -*-
"""C0715 mei: reduction in chromosome sets, and rhetorical understatement."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('meiosis','英 /maɪˈəʊsɪs/；美 /maɪˈoʊsɪs/','减数分裂；〔修辞〕轻描淡写','先抓住“把数量或分量降下来”：生物学里，染色体由两套减成一套；修辞里，把很严重或很了不起的事说得轻一点。','接希腊 meíōn“较少”→ meióō“使减少”→ meíōsis“减少”，经新拉丁学术用语进入英语。英语早已有修辞义，20 世纪初又把这个希腊词用于减数分裂；不是先有细胞术语，再借来形容说话。',[['希腊 meíōn → meióō → meíōsis','较少 → 使减少 → 减少'],['新拉丁／英语学术用语 meiosis','较早用于轻描淡写的修辞'],['20 世纪初英语生物学 meiosis','用“减少”给染色体套数减半的分裂过程命名']],'在人类的配子形成中，减数分裂使染色体数由 46 减到 23，精卵结合时再凑成 46。核心不是细胞变小，而是染色体套数减少。修辞义也很直观：明明是大麻烦，却只说“一点小波折”。','undergo meiosis；during meiosis；meiosis and mitosis；rhetorical meiosis。复数 meioses，末尾读 /siːz/。','mitosis 通常保持染色体套数；meiosis 会减半。修辞上的 meiosis 是 understatement 一类，与夸张放大的 hyperbole 方向相反。',('Meiosis reduces the chromosome number from 46 to 23 in the formation of human gametes.','在人类配子的形成过程中，减数分裂使染色体数从 46 减到 23。'),('The diagram compares meiosis with mitosis.','这张示意图比较了减数分裂和有丝分裂。'),('Calling the disastrous trip “a slight inconvenience” is an example of meiosis.','把这趟灾难般的旅行说成“一点不便”，就是轻描淡写的修辞。'),sources=['https://www.merriam-webster.com/dictionary/meiosis','https://www.etymonline.com/word/meiosis','https://www.genome.gov/genetics-glossary/Meiosis','https://www.collinsdictionary.com/dictionary/english/meiosis']),
E('meiotic','英 /maɪˈɒtɪk/；美 /maɪˈɑːtɪk/','减数分裂的；与减数分裂有关的','给过程、阶段或变化贴上“发生在减数分裂中”的标签。meiotic division 讲的就是那种把染色体套数减半的分裂。','今天可把它与 meiosis 配对记：-osis 是过程名，-otic 是相应形容词形式。历史上也有希腊 meiōtikos“使减少的”这一形容词基础，接 meioun“使减少”；不能把词形关系当成只在现代英语里机械删加字母。',[['希腊 meioun；meiōtikos','使减少；使减少的'],['现代生物学采用 meiotic','与 meiosis 配套的形容词'],['英语 meiotic division／recombination','减数分裂；减数分裂中的重组']],'meiotic 说的是所属过程，不是“较小的细胞”。meiotic recombination 指减数分裂中的遗传重组：遗传材料可以重新组合，而不只是原封不动分成两堆。','meiotic division；meiotic recombination；meiotic cells；meiotic errors。','meiotic 和 mitotic 只差一个字母，却对应不同分裂过程；不要凭两词长得像就互换。',('The animation shows the two meiotic divisions in sequence.','动画依次展示了减数分裂的两次分裂过程。'),('Meiotic recombination creates new combinations of inherited genetic material.','减数分裂中的重组会形成遗传材料的新组合。'),sources=['https://www.merriam-webster.com/dictionary/meiotic','https://www.collinsdictionary.com/dictionary/english/meiotic','https://en.wiktionary.org/wiki/meiotic#English','https://www.genome.gov/genetics-glossary/Meiosis']),
]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());names=[x['word'] for x in W]
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0715')
EX={w:'冷门细胞分裂细分或小型底栖生物术语，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0715',meaning='较少；使减少',core='mei- 的核心是把分量降下来。meiosis 在生物学里减少染色体套数，在修辞里减少说话表现出的分量。',image='希腊“较少、减少” → meiosis 减数分裂／轻描淡写；meiotic 相关的形容词。',intro='保留最值得认识的名词和形容词。先把“减少的是什么”讲清，就不会把减数分裂误解为细胞变小，也不会把修辞义误当医学隐喻。',forms='meiosis 接希腊名词 meíōsis，经新拉丁学术用语传入；meiotic 有希腊 meiōtikos 的基础，在现代与 meiosis 配套。',branches=[['减少的过程及相关形容词','meiosis, meiotic']],contrasts='meiosis 与 mitosis 不同：前者使染色体套数减半，后者通常保持。meiosis 的修辞义早于现代生物学义。',practice='用一组数字解释生物学的“减少”，再用一句把大事说小的话解释修辞的“减少”。',words=names,exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_201.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('mei:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
