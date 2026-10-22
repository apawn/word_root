# -*- coding: utf-8 -*-
"""C0348 dry: an oak/tree nymph, not English dry."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('dryad','/ˈdraɪæd/，也读 /ˈdraɪəd/','树仙；希腊神话中的树木女精灵','把一棵树想象成有自己的女性精灵，或者想象林中出现了一位与树木相伴的女仙，就接近 dryad 的故事形象。','来自希腊 dryas／dryad-，接 drus“橡树、树木”，经拉丁 dryas 与古法语 driade 等进入英语。表面开头像 dry“干燥”，实际不是 dry 加 -ad。',[['希腊 drus／dryos','橡树，亦可泛指树木'],['希腊 dryas／dryad- → 拉丁 dryas','与树木有关的女仙'],['古法语 driade 等 → 英语 dryad','树仙、林中女精灵的名称']],'古典来源以树木、尤其橡树为核心；后来的诗歌、艺术与奇幻故事可以把它扩展为更广的树木精灵。知道这层来源，就不会误以为 dryad 是住在沙漠里、因为“干”而得名的仙女。','a dryad in the forest；a painting of a dryad；dryads and nymphs。通常是可数名词，复数 dryads。','nymph 是更广的自然女神或女精灵名称；dryad 专门把联系落在树木上。不同文学作品会改编设定，不必把某一部小说里的规则当成整个单词的固定词义。',('In the poem, a dryad steps out from behind an ancient oak.','诗中，一位树仙从一棵古老橡树后走了出来。'),('The painting shows dryads dancing among the trees.','画中几位树仙在林木间起舞。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/dryad','https://www.etymonline.com/word/dryad','https://en.wiktionary.org/wiki/dryad'])]
names=['dryad'];cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0348');EX={w:'较少见的神话细分名或派生形容词，当前先保留树仙这个基本名称。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0348',meaning='橡树；树木',core='这一支来自希腊 drus“橡树、树木”。dryad 的画面是与树相连的女精灵，完全不是英语 dry“干燥”。',image='drus／dryos 树、橡树 → dryas／dryad- 树仙 → 拉丁、法语传递 → 英语 dryad。',intro='这是读神话、诗歌和奇幻作品时有用的一小组。一个明确的树木形象，足以把词源与现代角色名称接起来。',forms='dry- 来自希腊树木词，dryad- 是相应名词词干；英语整体借入 dryad，并非自行把 dry 与一个后缀拼接。',branches=[['神话中的树仙','dryad']],contrasts='dryad 与 dry“干的”不同源。dryad 属于自然精灵形象，具体文学作品中的外貌和能力不是这个词唯一的定义。',practice='用一棵橡树旁的树仙记 dryad，不要从干旱或沙漠开始联想。',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_249.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('dry: 1 new; 2 examples')
