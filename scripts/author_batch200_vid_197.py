# -*- coding: utf-8 -*-
"""C0893 onych: the fingernail comparison behind the gemstone name."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('onyx','英 /ˈɒnɪks/；美 /ˈɑːnɪks/','缟玛瑙〔玉髓类宝石材料〕','想一块可以磨亮、雕刻的石料，其中常见平行色带。古人把某些浅色层纹与指甲的颜色相比，便把“指甲”的名字借给了这种石头。','经古法语 oniche／onix 和拉丁 onyx 接希腊 onyx“指甲、爪；缟玛瑙”。其词干在其他构词中可显为 onych-。石名来自颜色、纹理联想，不是说石头由指甲形成。',[['希腊 onyx','指甲、爪；也用于相似颜色纹理的石料'],['拉丁 onyx → 古法语 oniche／onix','传承宝石名称；英语也有直接拉丁影响'],['中古英语 oneche／onix → onyx','缟玛瑙，常用于首饰与雕刻']],'今天的珠宝描述里，black onyx 很常见；缟玛瑙也不只限于纯黑外观。它属于玉髓一系，条带和颜色可以用于雕刻图案。名称说明历史上的外观联想，不能凭词源判断某件首饰的处理方式或品质。','an onyx ring；black onyx；carved onyx；a piece of onyx。','onyx 是石料名称，onycho- 在医学词里常指指甲或趾甲。黑曜石 obsidian 是另一种材料，不能因为都可能呈黑色就混称。',('The ring is set with polished black onyx.','这枚戒指镶着抛光的黑色缟玛瑙。'),('The carving uses the contrasting bands of the onyx.','这件雕刻利用了缟玛瑙中颜色对比鲜明的条带。'),sources=['https://www.etymonline.com/word/onyx','https://www.oxfordlearnersdictionaries.com/definition/english/onyx'])]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());names=[x['word'] for x in W]
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0893')
EX={w:'冷门指甲疾病、动物分类、占卜或宝石细分类词，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0893',meaning='指甲、趾甲、爪',core='onych- 接希腊 onyx“指甲、爪”。最常见的独立词 onyx 却指石头，因为古人用指甲的颜色去联想某种石料的浅色条纹。',image='onyx 指甲、爪 → 颜色与条纹相似的石料 → 拉丁、法语传承 → 英语 onyx 缟玛瑙。',intro='这组先保留首饰和艺术阅读里的 onyx。抓住“外观命名”就能理解从身体部位到宝石的变化，不必硬记一串冷门疾病名称。',forms='希腊主格 onyx、属格 onychos 显出 onych- 词干；石名经拉丁、古法语传入，英语保留 onyx 拼写。',branches=[['按外观命名的石料','onyx']],contrasts='onyx 不是指甲制品。缟玛瑙与黑曜石并非同一种材料，共同的黑色外观不足以确定类别。',practice='把“指甲的浅色纹理 → 石料的层纹”作为命名联想，再用 onyx ring 记它的现代日常搭配。',words=names,exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_197.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('onych:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
