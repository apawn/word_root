# -*- coding: utf-8 -*-
"""C0912 orch: a tuber-shaped naming history behind a familiar flower."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('orchid','英 /ˈɔːkɪd/；美 /ˈɔːrkɪd/','兰科植物；兰花；淡紫色','现在看到 orchid，通常先想到窗边的一盆兰花。这个优雅花名的古老命名线索却在地下：某些兰科植物成对的块茎让古人联想到睾丸。','来自近代拉丁分类名称 Orchideae、Orchidaceae 的词干形式；上接拉丁 orchis 和希腊 orchis“兰草、睾丸”。字母 d 与分类词干的不规则形成有关，不是英语另加一个表示花的 -id。',[['希腊 orchis','睾丸；因某些植物块茎形状而用于兰草'],['拉丁 orchis → 近代拉丁 Orchideae／Orchidaceae 等分类名','兰科相关的植物命名，形成带 d 的词干'],['十九世纪英语 orchid','兰科植物、兰花；后来也用作淡紫色名称']],'orchid 是一大类植物的常用名称，不只指一种固定花色，也不限于中文园艺里最熟悉的某几种兰花。历史块茎联想针对某些早期命名对象，不意味着每一株现代盆栽兰花都有同样的地下形状。色卡上的 orchid 则常是淡紫色，不是一种新植物。','a potted orchid；orchid flowers；an orchid collection；orchid as a colour name。ch 在这里读 /k/。','orchid 是兰花，orchard 是果园；不能因为开头像就当成同源或把兰花理解为果园里的花。orchid 作色名也不表示所有兰花都开紫花。',('A white orchid stood beside the window.','窗边摆着一盆白色兰花。'),('The conservatory displays orchids from several regions.','这座温室展示了来自多个地区的兰科植物。'),('The fabric sample labelled “orchid” was a pale purple.','标着 orchid 的那块布样是淡紫色。'),sources=['https://www.etymonline.com/word/orchid','https://www.oxfordlearnersdictionaries.com/definition/english/orchid','https://www.merriam-webster.com/dictionary/orchid','https://powo.science.kew.org/taxon/urn%3Alsid%3Aipni.org%3Anames%3A30021702-2/general-information']),
]
EX={w:'专门生殖解剖、手术或植物属名术语；按当前通用阅读范围暂略。' for w in ['orchis','orchiectomy','cryptorchidism','anorchia','monorchism','orchiopexy','polyorchidism']}
ROOT=dict(id='C0912',meaning='睾丸；由块茎外形形成的兰草名',core='orchis 原本是身体部位的名称，也被拿来称呼某些块茎形状相似的兰草。英语 orchid 继承的是这条植物命名路线。',image='身体部位名 orchis → 块茎形状引发的植物名 → 拉丁与近代植物分类名称 → orchid 兰花。',intro='这类词源不必回避，也不必牵强发挥：古人常用熟悉的身体形状给植物命名。现代 orchid 说的就是兰花，并没有附带身体部位的实际含义。',forms='希腊 orchis 经拉丁同形植物名，再通过近代分类名称形成英语 orchid。带 d 的形式来自分类词干历史；它不是现代英语中“orch + 花后缀”的透明拼接。',branches=[['从块茎外形到常见花名','orchid']],contrasts='词源讲的是命名时看到的形状，不是所有兰花共同具有的外观，也不是植物分类的唯一标准。orchard 果园属于另一路线。',practice='先记住日常盆栽 orchid，再补上一句历史说明：古名来自某些地下块茎的形状。这样既记得来源，也不会把现代花名理解歪。',words=[e['word'] for e in W],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id'])
 assert set(ROOT['words'])=={w for w in r['family'] if '-' not in w and w not in EX}
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_165.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('orch:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
