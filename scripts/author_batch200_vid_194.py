# -*- coding: utf-8 -*-
"""C0920 ornith: birds and the people who study them."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('ornithologist','英 /ˌɔːnɪˈθɒlədʒɪst/；美 /ˌɔːrnɪˈθɑːlədʒɪst/','鸟类学家','不只是在树上发现了一只漂亮的鸟，而是继续研究它怎样迁徙、繁殖、发声，或种群为什么变化的人。','由英语 ornithology“鸟类学”形成 -ist 人员名。ornithology 借自新拉丁 ornithologia，其中 ornith- 接希腊 ornis、属格 ornithos“鸟”；-logy 表研究。',[['希腊 ornis／ornith-；研究构件','鸟；对某类事物的研究'],['新拉丁 ornithologia → 英语 ornithology','鸟类学'],['英语 ornithology → ornithologist','从事鸟类学研究的人']],'ornithologist 可以研究鸟的行为，也可以研究遗传、分布或栖息地。会认鸟是有用技能，但这个人员名强调研究，而不是“喜欢鸟的人”的泛称。','a field ornithologist；a team of ornithologists；an ornithologist studying migration。','birdwatcher 是观鸟者；ornithologist 是鸟类研究者。爱好者也能提供重要记录，但两个称呼关注点不同。',('The ornithologist identified the bird by its call.','鸟类学家根据叫声辨认出了这只鸟。'),('Ornithologists are studying changes in the birds’ migration routes.','鸟类学家正在研究这些鸟迁徙路线的变化。'),sources=['https://www.etymonline.com/word/ornithology','https://www.oxfordlearnersdictionaries.com/definition/english/ornithologist']),
E('ornithological','英 /ˌɔːnɪθəˈlɒdʒɪkl/；美 /ˌɔːrnɪθəˈlɑːdʒɪkl/','鸟类学的；有关鸟类研究的','放在 research、survey、journal 前面，告诉读者这项研究、调查或刊物围绕鸟类展开。','英语 ornithology + -ical 形成相关形容词，词尾按 -logy → -logical 变化。主重音移到 -log-，与 ornithologist 的重音位置不同。',[['希腊 ornith- → 新拉丁 ornithologia → 英语 ornithology','鸟 → 鸟类学'],['英语 ornithology + -ical → ornithological','属于鸟类研究的']],'an ornithological survey 可以调查某地有哪些鸟、数量怎样变化。这个长形容词给活动加上学科标签；不表示活动一定只在野外进行，也不表示被描述的东西长得像鸟。','ornithological research；an ornithological survey；an ornithological society。','ornithology 是学科，ornithologist 是研究者，ornithological 是修饰词。birdlike 才是在描述“像鸟的”。',('The reserve published the results of its annual ornithological survey.','保护区公布了年度鸟类调查的结果。'),('She donated her field notes to an ornithological society.','她把野外笔记捐给了一个鸟类学会。'),sources=['https://www.etymonline.com/word/ornithology','https://www.oxfordlearnersdictionaries.com/definition/english/ornithological']),
]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());names=['ornithology']+[x['word'] for x in W]
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0920')
EX={w:'较冷门的古典地名、动物属名、占卜或疾病细分称呼，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0920',meaning='鸟',core='ornith- 接希腊 ornis 的词干 ornith-，意思是鸟。它在英语中常把“鸟”放进学科名称。',image='ornis／ornith- 鸟 → ornithologia → ornithology 鸟类学 → ornithologist 研究者／ornithological 相关的。',intro='这一组只要把三个位置记清：学科、研究者、修饰词。内容可以从辨认鸟鸣一直延伸到迁徙、遗传和保护研究。',forms='希腊主格 ornis、属格 ornithos 显出词干 ornith-；ornithology 经新拉丁借入，人员名和形容词在英语中派生。',branches=[['研究领域','ornithology'],['研究者','ornithologist'],['研究活动的修饰词','ornithological']],contrasts='birdwatching 是观鸟活动，ornithology 是鸟类学；专业研究可以利用爱好者记录。ornithological 不是描述外形像鸟。',practice='分别用 study ornithology、an ornithologist、ornithological research 说同一个人的学科、身份与工作。',words=names,exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_194.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('ornith:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
