# -*- coding: utf-8 -*-
"""C0441 font: springs and sources, with the two font homographs separated."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
def S(w):return 'https://www.etymonline.com/word/'+w
def O(w):return 'https://www.oxfordlearnersdictionaries.com/definition/english/'+w
FOUNTAIN=[['拉丁 fōns，词干 font-','泉、水源'],['拉丁 fontānus → 后古典拉丁 fontāna','泉的 → 泉、水源这个名词'],['古法语 fontaine → 英语 fountain','天然泉水，后来也指人工喷泉']]
W=[
E('fountain','英 /ˈfaʊntən/；美 /ˈfaʊntn/','喷泉；泉水；喷涌；大量事物的来源','核心画面是某处不断涌出东西：先是泉水，后来可以是人工水柱，也可以是一股火花或源源不断的资源。','经古法语 fontaine 借入，接后古典拉丁 fontana，是 fontanus“泉的”的阴性形式转作名词；再接 fons、词干 font-“泉”。不能把英语 fountain 当作 font 后加一个表示小物的 -ain。',FOUNTAIN,'广场上的 fountain 通常是人工喷泉；a drinking fountain 是供人饮水的设施。a fountain of sparks 把向外喷出的火花比作水柱，a fountain of ideas 则借“不断涌出”说创意很多。','a public fountain；a drinking fountain；a fountain of sparks；a fountain pen。钢笔的 fountain 借储墨器持续供墨的画面命名。','spring 更常直接说自然涌出的泉；fountain 在现代日常场景里常是人工喷泉。两者历史上接近，今天常用场景已有区别。',('We arranged to meet beside the fountain in the square.','我们约好在广场的喷泉旁碰面。'),('A fountain of sparks rose from the firework.','烟花喷出了一股泉水般的火花。'),('The workshop became a fountain of new ideas.','这次工作坊成了新点子不断涌现的源泉。'),sources=[S('fountain'),O('fountain')]),
E('fount','英美 /faʊnt/','源泉；来源〔偏文学或带幽默意味〕','把一个人的知识、经验或热情想成一口泉，总能从那里得到新的东西。','通常解释为英语 fountain 的缩短或逆构，可能受到法语 font 的影响，也常以 mount／mountain 这类词形对应说明其形成。不是先有英语 fount 再加 -ain 才产生 fountain。',FOUNTAIN+[['英语 fount','从 fountain 缩短／逆构；保留泉和来源的比喻']],'最值得掌握的是 a fount of knowledge／wisdom，把某人形容成“知识宝库、智慧源泉”。它可以真心赞许，也可以轻微调侃，不必每次都翻成字面的泉水。','a fount of knowledge；a fount of wisdom；an endless fount of ideas。','source 很中性，fount 更有文采，也容易带夸张。另有印刷术语 fount，作 font“字体”的拼写形式时常读 /fɒnt/ 或美 /fɑːnt/，那一支接铸造词源，不属于这里的泉水义。',('Our librarian is a fount of knowledge about the town’s history.','我们的图书管理员对镇史了如指掌，像一座知识宝库。'),('I am hardly a fount of wisdom when it comes to gardening.','说到园艺，我可远算不上什么智慧源泉。'),sources=[S('fount'),O('fount'),'https://en.wiktionary.org/wiki/fount#English']),
E('fontanelle','英 /ˌfɒntəˈnel/；美 /ˌfɑːntəˈnel/','囟门；婴儿颅骨间尚未闭合的柔软部位','婴儿的头骨不是一整块硬壳；几块骨之间还留有被软组织覆盖的部位，这就是家长常听到的“软点”。','英语借法语 fontanelle；古法语 fontenele 是 fontaine“泉”的小称形式，也见近代拉丁 fontanella 的医学传播。名称常解释为类比泉眼所在的小凹处，并非婴儿头上真的有泉水。',[['拉丁 fons → fontana → 古法语 fontaine','泉、水源'],['古法语小称 fontenele；法语 fontanelle','小泉眼；转用为人体的柔软凹处，近代拉丁亦有 fontanella'],['英语 fontanelle／fontanel','早期用于肌肉间凹处，后来用于婴儿的囟门']],'育儿文章中的 soft spot 常是它的通俗说法。囟门属于婴儿正常生长结构，帮助头颅适应生长；它有组织覆盖，不是一个裸露的洞。美式英语也常拼 fontanel，复数 fontanels 或 fontanelles 随词头拼写。','the anterior fontanelle 前囟；the posterior fontanelle 后囟；fontanelle closure 囟门闭合。','这里与 fountain 的关系发生在法语及更早的拉丁来源中，不是英语先有“喷泉”再新造医学单词。字体 font 的铸造词源也解释不了它。',('The nurse explained that a fontanelle is a normal soft area on a baby’s head.','护士解释说，囟门是婴儿头上正常存在的柔软部位。'),('The parenting guide used the words “soft spot” instead of “fontanelle”.','那本育儿指南用通俗的“软点”来代替“囟门”这个术语。'),sources=[S('fontanelle'),O('fontanelle'),'https://medlineplus.gov/ency/article/002320.htm']),
]
EX={'fontal':'罕用的“泉的、来源的”形容词，本轮暂略。'}
SH={'font'}
ROOT=dict(id='C0441',meaning='泉；水源',core='font- 可以想成水不断涌出的泉眼。从真实的泉，容易借到知识和智慧的来源；与水有关的宗教器物也保留了这条来源。',image='fons／font- 泉 → fontana → fountain 喷泉；fountain → fount 源泉；法语小称 fontanelle → 囟门。',intro='这组不大，但有一个很容易记错的地方：font 的“洗礼盆”和“字体”只是碰巧同形。前者接泉水，后者接金属活字的铸造，不能统一解释成“文字从泉里流出来”。',forms='拉丁主格 fōns，属格 fontis，显出 font- 词干。fountain 经法语借入，fount 通常解释为它的后起缩短／逆构；fontanelle 的小称形成在法语一侧。',branches=[['泉水、喷泉与抽象来源','fountain, fount'],['盛水器与同形词辨认','font'],['借小泉眼形象命名的部位','fontanelle']],contrasts='font 的字体义接法语 fonte“铸造”，不接 fons“泉”。fount 作为“知识源泉”读 /faʊnt/；印刷语境里的 fount 可以只是 font 的另一拼写，词义和读音要看场景。',practice='She is a fount of local knowledge. 她是本地知识的宝库：知识像泉水一样可以不断从她那里得到。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w and w not in EX]
 assert set(ROOT['words'])=={e['word'] for e in W}|SH
 assert {e['word'] for e in W}<=set(m['owned_words'])
 assert all(len(e['examples'])>=2 and len(e['history'])>=2 for e in W)
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_120.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('font:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
