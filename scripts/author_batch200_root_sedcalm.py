# coding: utf-8
import json
from pathlib import Path
ROOT=dict(id='C1296',meaning='使安静；使平稳',core='SED = SETTLE / CALM',image='原先躁动的状态慢慢落下来、安静下来；这是 sedate、sedation、sedative 共同的画面。',intro='拉丁 sedare 表示使安静、平息，通常与 sedere 坐的词族联系起来。这里专看使状态安定的支线，不把它和位置、座位等大量近亲混成一页。',forms='sedare → sedatus 通向 sedate；sedatio 通向 sedation；sedativus 通向 sedative。英语动词 sedate 的现代用药义还涉及从已有名词反构，不能把三个现代词简单排成单向造词链。',branches=[['平静的状态或使平静的动作','sedate'],['镇静过程与作用','sedation；sedative']],contrasts='sedate 可形容生活或活动平静从容，并不总涉及药物。sedation 是镇静过程或状态，sedative 可以是镇静的形容词，也可以指镇静药。',practice='The town has a sedate pace of life.\n\n这座小镇的生活节奏平静从容。',words=['sedate','sedation','sedative'],exclude={})
if __name__=='__main__':
 Path('.cache/batch200/drafts/root/roots_sedcalm.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2));print('1 root, shared words only')
