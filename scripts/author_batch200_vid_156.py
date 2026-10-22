# -*- coding: utf-8 -*-
"""C0048 amphi: both environments and a surrounding audience."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('amphibian','/æmˈfɪbiən/','两栖动物；两栖类的','从蝌蚪在水里、青蛙能上岸这个画面入手，就能记住“两种生活环境”。但现代 amphibian 是动物分类名称，不是所有会游泳又能上岸的动物。','接近代拉丁 amphibium 和希腊 amphibion／amphibios，后者由 amphi“两种、两边” + bios“生命、生活”构成。英语早期形容词的范围较宽，后来名词用于两栖动物这一类。',[['希腊 amphi + bios → amphibios／amphibion','两种 + 生活 → 在水陆两处生活的'],['近代拉丁 amphibium → 英语 amphibian','早期有两种生活方式等较宽含义'],['现代动物学名词 amphibian','两栖动物：蛙、蟾蜍、蝾螈、蚓螈等所属类群']],'现代两栖动物包括蛙、蟾蜍、蝾螈和蚓螈等。河马、鳄鱼也能在水陆活动，却不因此成为 amphibians。词源画面能帮你入门，真正的分类还取决于生物的亲缘关系和特征，不能只凭“去过两个地方”来判断。','an amphibian；amphibian species；amphibian conservation。作形容词时说两栖动物相关的。','amphibian 常用来给动物分类；amphibious 则强调能在水陆活动，也能形容车辆。动物分类与某一种活动能力是两回事。',('A frog is an amphibian, but a crocodile is a reptile.','青蛙是两栖动物，而鳄鱼是爬行动物。'),('The project protects wetlands used by several amphibian species.','这个项目保护几种两栖动物使用的湿地。'),sources=['https://www.etymonline.com/word/amphibian','https://www.oxfordlearnersdictionaries.com/definition/english/amphibian','https://www.usgs.gov/mission-areas/ecosystems/science/amphibian','https://www.amnh.org/exhibitions/frogs-a-chorus-of-colors/the-amazing-adaptable-frog']),
E('amphibious','/æmˈfɪbiəs/','水陆两栖的；水陆两用的；两栖作战的','一辆车从岸上开进水里，仍能继续前进，这个“两边都能用”的能力就是 amphibious。','来自希腊 amphibios“两种生活的、水陆生活的”的拉丁化词族，常以近代拉丁 amphibium + -ous 说明英语形式。它与 amphibian 共享更早材料，不必画成现代英语名词改几个字母才产生。',[['希腊 amphi + bios → amphibios','两种 + 生活 → 水陆生活的'],['拉丁化 amphibium 等形式 → 英语 amphibious','十七世纪进入英语，形容两种生活方式'],['后来的车辆与军事用法','水陆两用；从海上登陆并向陆地展开的行动']],'an amphibious vehicle 可以在陆地行驶，也可以在水上运行。an amphibious landing 则把水陆两边连成行动：人员从海上登陆。描述动物时它说的是生活或活动能力，不必和严格的动物分类名词 amphibian 完全重合。','an amphibious vehicle；amphibious operations；an amphibious landing；amphibious animals。','waterproof 是防水，amphibious 是能在水陆环境活动或使用。普通防水设备并不因此成为水陆两用交通工具。',('The amphibious vehicle drove down the ramp and entered the lake.','那辆水陆两用车沿坡道驶下，进入了湖中。'),('The documentary describes an amphibious landing on the island.','纪录片介绍了一次在岛上的两栖登陆行动。'),sources=['https://www.etymonline.com/word/amphibious','https://www.oxfordlearnersdictionaries.com/definition/english/amphibious']),
]
SH=['amphitheatre','amphitheater']
EX={w:'矿物、韵律或专业形态术语，按当前常用阅读范围暂略。' for w in ['amphibole','amphibolic','amphimacer','amphoterism','Amphipoda','amphistyly']}
ROOT=dict(id='C0048',meaning='两边、两种；周围',core='amphi- 可以把视线拉到“两边、两种”，也能扩展为“周围”。生物词里是两种生活环境，剧场词里是观众从周围观看。',image='amphi + bios 生活 → amphibian／amphibious；amphi + theatron 观看场所 → amphitheatre。',intro='先想一辆能入水的车，再想观众环绕场地坐下的剧场。两幅画面分别帮助理解“两种”和“周围”，不把 amphi- 机械地只译成数字二。',forms='希腊 amphi 表两边、周围；元音前可见 amph-。amphibian、amphibious 经过拉丁化词形，amphitheatre 经过拉丁语和法语等传播；各词历史分别阅读。',branches=[['动物与水陆能力','amphibian, amphibious'],['环绕场地的观众席','amphitheatre, amphitheater']],contrasts='两栖动物不是“一切水陆都能活动的动物”的统称。amphibian 的现代分类意义比字面联想更精确；amphitheatre 与 amphitheater 只是英美常见拼写差别。',practice='amphibious vehicle 让你看两种环境；amphitheatre 让你看场地周围。再用 amphibian 给动物分类，就不会把所有游泳动物都叫两栖类。',words=[e['word'] for e in W]+SH,exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id'])
 assert {w for w in r['family'] if '-' not in w}<=set(ROOT['words'])|set(EX)
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_156.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('amphi:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
