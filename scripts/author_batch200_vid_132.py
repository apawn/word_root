# -*- coding: utf-8 -*-
"""C0548 heter: a shared lesson entry point for different kinds and views."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[];SH={'heterosexual','heterosexuality','heterogeneous','heterogeneity','heterodox','heterodoxy','heteronormative','heteronormativity'}
EX={w:'较冷门的专门生物学、物理学或社会术语，本轮按通用阅读优先暂略。' for w in ['heterochromatin','heterosis','heterophobia','heterotic']}
ROOT=dict(id='C0548',meaning='不同的；另一个',core='hetero- 给后面的内容加上“不同、另一类”这一关系。它并没有自带好坏评价：组成不同可以说 heterogeneous，观点不同于正统可以说 heterodox。',image='希腊 heteros 不同、另一个 → heterogeneous 种类有别；heterodox 观点有别；heterosexual 指向异性的性取向；heteronormative 把异性恋当默认规范。',intro='读这一组时，先问“哪一方面不同”：heterogeneous 看内部成员和成分；heterodox 看它与主流观点的关系；heterosexual 看性取向所指向的对象。只背一个“异”字，还不足以理解整个词。',forms='希腊 heteros 意为另一个、不同的，构词时常作 hetero-。heterogeneous 接希腊 genos 种类，经中世纪拉丁借入；heterodox 接 doxa 观点。heterosexual 是近代的希腊、拉丁来源混合构词；heteronormative 和 heteronormativity 是后来社会讨论中的英语构词。',branches=[['组成和性质不同','heterogeneous, heterogeneity'],['与正统观点不同','heterodox, heterodoxy'],['性取向及其社会规范','heterosexual, heterosexuality, heteronormative, heteronormativity']],contrasts='hetero- 与表示相同的 homo- 相对。heterosexual 描述性取向；heteronormative 描述把异性恋当成默认规范的观念或安排，两者不能互换。heterodox 也不等于已经证明错误，只说明偏离正统。',practice='The group was heterogeneous, but its members shared a goal. 这群人的背景各不相同，却有共同目标：heterogeneous 指内部组成不同，不代表彼此不能合作。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w and w not in EX];ROOT['words']+=sorted(SH-set(ROOT['words']))
 assert set(ROOT['words'])==SH
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_132.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('heter:',len(ROOT['words']),'shared references')
