# -*- coding: utf-8 -*-
"""C0155 cal/call: beauty in writing, images and movement."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('calisthenics','/ˌkælɪsˈθenɪks/','徒手健身；健身操；自重训练','想人用自己的身体完成屈伸、支撑、跳跃等动作，练力量和身体控制。名称把“美”和“力量”放在了一起。','以希腊 kallos“美”／kalos“美的”和 sthenos“力量”为材料，加学科、活动名词词尾 -ics；英语十九世纪的命名参照法语 callisthenie。不是古希腊已有整套现代同名健身项目。',[['希腊 kallos／kalos + sthenos','美／美的 + 力量'],['近代法语 callisthenie 等命名背景 → 英语 calisthenics','十九世纪的体操、健身活动名称'],['现代 calisthenics','常指以身体自重为主的锻炼，也有其他地区性体育用法']],'俯卧撑、深蹲等自重动作常被归入 calisthenics；现代训练也可以借助单杠等设施，所以别把“徒手”误解为绝不能碰任何器械。旧时用法较强调体态与优美动作，今天常把力量、身体控制放在前面。','do calisthenics；a calisthenics routine；bodyweight calisthenics。英式也写 callisthenics；词尾的 s 通常属于活动名称，不是随手去掉的普通复数。','gymnastics 通常让人想到体操项目、动作技术和器械体系；calisthenics 更常指自重锻炼。aerobics 强调有氧运动，两者不是完全重合的类别。',('Their morning routine includes a short session of calisthenics.','他们的晨间安排包括一小段徒手健身。'),('The class uses simple calisthenics rather than heavy weights.','这门课采用简单的自重练习，而不是大重量负重训练。'),sources=['https://www.etymonline.com/word/calisthenics','https://www.oxfordlearnersdictionaries.com/definition/english/calisthenics','https://www.merriam-webster.com/dictionary/calisthenics']),
]
SH=['calligraphy','calligrapher','kaleidoscope','kaleidoscopic']
EX={'Callisto':'神话与木卫专名，本轮按通用词汇范围暂略。','Callista':'人名，按通用词汇范围暂略。','calophyllous':'罕见植物形态形容词，暂略。'}
ROOT=dict(id='C0155',meaning='美、漂亮、优美',core='kalos 是美的，kallos 是美。把“美”放到书写、形状或身体动作前面，就能看出这几个词的命名想法。',image='美 + 写 → calligraphy；美 + 形状 + 观察 → kaleidoscope；美 + 力量 → calisthenics。',intro='这一族不是所有 cal 开头的词。真正有帮助的是三个具体画面：漂亮地写字、观察不断变化的美丽图案、用身体动作表现力量与协调。',forms='希腊 kalos／kallos 在借词和近代构词中表现为 cal-、calli-、kali- 等形式。kaleidoscope 是近代英语造词，calisthenics 也属于近代命名，不能假装整词都从古希腊日常词汇直接沿用。',branches=[['优美书写','calligraphy, calligrapher'],['美丽而变化的形状','kaleidoscope, kaleidoscopic'],['身体动作与力量','calisthenics']],contrasts='这里只认经过证实的“美”这一支；不能看到 call 就把普通英语 call“呼叫”也拉进来。词源的赞美意象也不保证某件实际作品一定美。',practice='写得美是 calligraphy，看到美丽图案变化是 kaleidoscope；calisthenics 则把美与力量放到身体动作里。分别记一个场景，比背同一串中文释义更牢。',words=[e['word'] for e in W]+SH,exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id'])
 assert {w for w in r['family'] if '-' not in w}<=set(ROOT['words'])|set(EX)
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_158.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('cal:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
