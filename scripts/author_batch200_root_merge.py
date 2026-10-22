# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_merge_a import WA
from author_batch200_root_merge_b import WB
W=WA+WB
ROOT=dict(id='C0729',meaning='浸入、沉下去',core='MERG / MERS = DIP / SINK',image='把一颗石子放入水中：往里是 immerse，往水面下是 submerge，从水下露出来是 emerge；小溪汇入大河、失去自己的边界，则能帮助理解 merge 的合并义。',intro='这一组来自拉丁 mergere“浸入、沉下去”，其分词是 mersus。保留 merg- 的词和采用 mers- 的词，因此常成双出现。词义发展不只是一套换前缀游戏：英语还分别借入过拉丁的动词、分词和名词。',forms='merg- 常见于 merge、emerge、submerge；mers- 常见于 immerse、immersion、submersible。in- 在 m 前同化成 im-；e- 接 ex-“出来”；sub- 是下面。de- 在 demersal 中是向下，在现代商业 demerge 中则表示撤销、反向。',branches=[['边界消失、合成一个整体','merge, merging, merged, merger, demerge, demerger'],['从里面露出来','emerge, emerging, emerged, emergence, emergent, reemerge, reemergence, emersion'],['突然出现并需要及时处理','emergency'],['进入其中、全心投入','immerse, immersed, immersion, immersive, immersible, reimmerse, immerge, immergence'],['处在液面下面','submerge, submersible, submersion, submergence, submerse'],['向下和水底的古典支线','demersal, demerse, demersion'],['以潜水习性命名的鸟','merganser']],contrasts='emergence 是出现，emergency 已固定为紧急情况。immerge 与 emerge 可以同音，但前者往里、后者往外。immersed 说人的状态，immersive 说体验的特点。merger 的 -er 不表示合并人员。',practice='She immersed herself in the records. A pattern soon emerged, and she merged the related notes into one file.\n\n她专心研究那些记录。一个规律很快显现出来，她把相关笔记合并进了一个文件。',words=[w['word'] for w in W]+['submerge'])
if __name__=='__main__':
 for name,v in [('roots_merge',[ROOT]),('words_merge_a',WA),('words_merge_b',WB)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(v,ensure_ascii=False,indent=2))
 print(len(W),'individually authored words')
