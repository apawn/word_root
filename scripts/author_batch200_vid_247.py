# -*- coding: utf-8 -*-
"""C0143 bront: thunder imagery in Brontosaurus."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[];names=['brontosaurus'];cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0143');EX={w:'较冷门的雷学或恐惧症细分术语，当前先保留通用读物中的雷龙名称。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0143',meaning='雷；雷声',core='希腊 brontē 表示雷。brontosaurus 把“雷”与“蜥蜴”放在一起命名巨大恐龙，让人联想到雷鸣般的声势。',image='brontē 雷 + sauros 蜥蜴 → 近代属名 Brontosaurus → 英语 brontosaurus 雷龙。',intro='把大恐龙的声势与雷联系起来，是命名者的形象表达。词名能帮助记忆，但不能当成我们已经录到了恐龙脚步声的证据。',forms='bronto- 是由希腊 brontē 形成的组合形式；Brontosaurus 是近代科学属名，普通英语动物名称常小写 brontosaurus。',branches=[['借雷的形象命名的恐龙','brontosaurus']],contrasts='bronto- 是雷，sauro- 是蜥蜴。名称不是由现代英语 thunder 一路音变而来；旧书与新书的恐龙属名处理也可能不同。',practice='看到 brontosaurus，先记“雷＋蜥蜴”的命名，再回到长颈、长尾的蜥脚类恐龙这一实际对象。',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_247.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('bront: 0 new; 1 shared')
