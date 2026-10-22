# -*- coding: utf-8 -*-
"""C1612 ven: animal venom and figurative verbal poison."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
def S(w):return 'https://www.etymonline.com/word/'+w
def O(w):return 'https://www.oxfordlearnersdictionaries.com/definition/english/'+w
V=[['拉丁 venenum','药剂、药水；毒药等义'],['古法语、盎格鲁法语 venim／venin','毒物、恶意；常经重构的通俗拉丁 *venimen 解释词形变化'],['中古英语 venim／venym → venom','动物毒液；也比喻带伤害性的恶意']]
W=[
E('venom','英美 /ˈvenəm/','动物毒液；恶意；恶毒言辞','蛇咬或蜂蜇时带入的毒液，是本义的典型画面；把这个画面移到言语上，就是一句话里像含了毒。','经古法语、盎格鲁法语 venim／venin 进入英语，远接拉丁 venenum“药剂、毒药”；中间常拟构 *venimen 说明变化，星号表示重构形式。更早的“爱情药水”解释属于词源推测，不作为确定历史起点。',V,'现代动物学里 venom 通常指动物产生、通过咬、蜇等专门方式传递的毒性分泌物。a voice full of venom 则没有真正的毒液，是说语气带着强烈恶意，想刺伤对方。','snake venom；bee venom；venom glands；speak with venom；venom in someone’s voice。通常不可数。','poison 是毒物的广泛称呼，venom 特别突出动物的毒性分泌物。比喻义的 venom 比普通 anger 更强调恶意和伤人的态度。',('The museum display explains how a snake delivers venom through its fangs.','博物馆展板解释了蛇怎样通过毒牙传递毒液。'),('There was so much venom in his reply that the room fell silent.','他的回答充满恶意，房间里一下安静了下来。'),sources=[S('venom'),O('venom')]),
E('venomous','英美 /ˈvenəməs/','有毒液的；能以毒液伤害的；恶毒的','对动物，是具备毒液这件“武器”；对话语，是带着要刺伤人的敌意。','英语借古法语 venimos、盎格鲁法语 venimeus，来自法语 venim“毒物”加形容词词尾。现代可以按 venom + -ous 理解，但其历史不只是英语名词直接派生形容词。',V[:2]+[['古法语 venimos／盎格鲁法语 venimeus','有毒的、恶意的形容词'],['英语 venomous','恶毒的；有毒液、能以毒液伤害的']],'venomous snake、venomous spider 描述生物特征；venomous remarks 则是恶毒的话。英语早期记录已经有恶意等比喻用法，因此不必假定所有比喻都晚于英语中的字面动物义。','a venomous snake；venomous species；a venomous attack；venomous remarks。','生物描述中，venomous 常说能以咬、蜇等方式输送毒液；poisonous 更常说接触、食用等途径带来毒性。日常会混用，但学习时先记住这种区别。',('The guide identified the snake as a venomous species.','向导辨认出这条蛇属于有毒液的种类。'),('Her review was sharp without becoming venomous.','她的评论很尖锐，但没有变得恶毒。'),sources=[S('venomous'),O('venomous')]),
E('antivenom','英美 /ˌæntiˈvenəm/','抗毒液制剂；抗蛇毒血清等','毒液里的有害成分有特定对手：antivenom 中的抗体可以针对相应毒液成分起作用。','英语 anti-“对抗”+ venom“毒液”组成，属于现代英语构词。另有 antivenin 这一名称；不要把 anti- 理解成“这种动物不产毒”，它说的是针对毒液的制剂。',V+[['英语 anti- + venom → antivenom','对抗毒液的制剂名称']],'常见语境是蛇咬伤治疗及药品供应。它不是适用于一切毒物的万能解毒药；不同制剂针对的毒液范围不同。新闻里的 access to antivenom 说的是能否获得合适的医疗药品。','snake antivenom；effective antivenom；antivenom treatment；a shortage of antivenom。','antidote 是解毒剂、解药的广称；antivenom 专指针对动物毒液的这一类制剂。antibiotic 抗生素针对细菌，两者不是同类概念。',('The regional hospital reported a shortage of antivenom.','这家地区医院报告说，抗毒液制剂供应不足。'),('Researchers tested whether the antivenom could neutralize toxins from several snake species.','研究人员测试了这种抗毒液制剂能否中和几种蛇的毒素。'),sources=['https://dictionary.cambridge.org/dictionary/english/antivenom','https://dictionary.cambridge.org/pronunciation/english/antivenom','https://en.wiktionary.org/wiki/antivenom','https://www.who.int/teams/control-of-neglected-tropical-diseases/snakebite-envenoming/antivenoms']),
]
EX={w:'较罕用的抗毒、带毒形容词，本轮按通用阅读优先暂略。' for w in 'antivenomous veneniferous'.split()};SH=set()
ROOT=dict(id='C1612',meaning='毒物；毒液',core='这一支最清楚的画面是动物的毒液；引申到人说话，就变成带毒般的恶意。不要把它泛化成所有带 ven 字母的词。',image='拉丁 venenum 药剂、毒物 → 法语 venim／venin → venom；法语形容词 venimos → venomous；英语 anti- + venom → antivenom。',intro='保留三词就能覆盖毒液本身、动物或言辞的性质，以及对抗毒液的制剂。掌握比喻义，也能读懂人物冲突和评论文章里的“毒”。',forms='拉丁来源词是 venenum，法语和英语中出现 venim／venin／venom 等变化；部分中间形式依靠重构解释。venomous 有独立的法语形容词借入史，antivenom 才是清楚的现代英语组合。',branches=[['毒液与恶意','venom, venomous'],['针对毒液的制剂','antivenom']],contrasts='venom 常指动物毒液，poison 范围更大。venomous words 是恶毒的话，不是在说文字里有化学毒物；antivenom 也不能泛称所有药物或解毒办法。',practice='The article describes a venomous snake, its venom and the need for antivenom. 文章讲有毒液的蛇、它的毒液，以及抗毒液制剂的需求：性质、物质、对抗物三层分清即可。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w and w not in EX]
 assert set(ROOT['words'])=={e['word'] for e in W}|SH
 assert {e['word'] for e in W}<=set(m['owned_words'])
 assert all(len(e['examples'])>=2 and len(e['history'])>=2 for e in W)
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_129.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('ven:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
