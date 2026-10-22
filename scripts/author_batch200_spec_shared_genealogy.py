# -*- coding: utf-8 -*-
"""Write once: genealogy, shared by Greek gen- and log-."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
W=[E('genealogy','/ˌdʒiːniˈælədʒi/','家谱；世系；家谱研究','沿着父母、祖父母一代代向上找，弄清一个家族的人怎样接起来。','希腊 geneá“世代、血统”+ -logía“叙述、研究”，组成 genealogía，经过晚期拉丁和古法语借入英语。它早于现代 gene“基因”，不是 gene + 一个任意的 alogy。',[['希腊 geneá + -logía → genealogía','世代、血统 + 叙述 → 记述家族世系'],['晚期拉丁 genealogia → 古法语 genealogie → 中古英语 genealogie','家族沿革、家谱'],['现代英语 genealogy','世系及记录；研究家族历史的活动']],'不可数时常指研究活动：an interest in genealogy 是对家谱研究感兴趣。可数时可指某家的世系或家谱记录。它可以利用出生记录、信件等材料，并不等于只做 DNA 检测。','trace a genealogy；research family genealogy；an interest in genealogy。','genetics 研究遗传，genealogy 追查家族世系；family tree 是把关系画成树状的直观记录。拼写是 genealogy，中间接 genea-，不是 geneology。',('Old letters helped her trace the genealogy of her family.','旧信件帮助她追查自己家族的世系。'),('His interest in genealogy began with a photograph of his great-grandparents.','一张曾祖父母的照片，让他开始对家谱研究感兴趣。'),sources=['https://www.etymonline.com/word/genealogy','https://www.oxfordlearnersdictionaries.com/definition/english/genealogy'])]
(OUT/'words_batch200_spec_shared_genealogy.json').write_text(json.dumps(W,ensure_ascii=False,indent=2))
print('genealogy: 1 word / 2 examples')
