# -*- coding: utf-8 -*-
"""C0285 culin: kitchen vocabulary and the old borrowing kiln."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
def S(w):return 'https://www.etymonline.com/word/'+w
def O(w):return 'https://www.oxfordlearnersdictionaries.com/definition/english/'+w
W=[
E('culinary','英 /ˈkʌlɪnəri/；美 /ˈkʌlɪneri/','烹饪的；与食物制作有关的','把厨房里选料、调味、掌握火候这些本领，放到一个正式的“烹饪”类别下，就是 culinary。','接拉丁 culinarius“厨房的”，由 culina“厨房、炉灶”形成；也有经法语 culinaire 的借入分析。今天可用 culin- 加形容词词尾来认，但它不是英语先有一个独立的 culin 再临时加 -ary。',[['拉丁 culina → culinarius','厨房、炉灶 → 厨房的'],['拉丁 culinarius／法语 culinaire → 英语 culinary','关于厨房，随后常用于烹饪技艺与饮食'],['现代 culinary skills／arts','做菜的技能；烹饪艺术']],'culinary skills 是做菜本领；culinary traditions 是一个地方或群体的烹饪传统。它经常出现在课程、餐饮和旅行介绍里，语气比 cooking 更正式，但不自动意味着昂贵菜肴。','culinary skills；culinary arts；a culinary school；local culinary traditions。常放在名词前。','culinary 说烹饪领域；delicious 评价好吃。a culinary experiment 只是一次做菜尝试，结果未必成功；不能把 culinary 单独翻成美味。',('The course helped him develop basic culinary skills.','这门课帮助他掌握了基本的烹饪技能。'),('The festival celebrates the region’s culinary traditions.','这个节日展示并庆祝当地的烹饪传统。'),sources=[S('culinary'),O('culinary'),'https://en.wiktionary.org/wiki/culinary']),
E('kiln','英美 /kɪln/','窑；用于烧制或干燥材料的炉','想象一个把材料放进去加热的封闭空间：陶土进去后烧成陶器，木材或谷物也可以在相应设备里干燥。','来自中古英语 kilne，更早是古英语 cyln／cylen／cylin，借自拉丁 culina“厨房、炉灶”。这是很早进入英语并改变拼写的借词；不要把现代 kiln 拆成几个假词根，也不要从 culinary 倒推成它的缩写。',[['拉丁 culina','厨房、烹饪炉灶'],['古英语 cyln／cylen → 中古英语 kilne','用于烘、烧、干燥的炉'],['现代英语 kiln','陶窑、砖窑，以及用于干燥等用途的窑炉']],'陶艺里的 fire a pot in a kiln 是把陶坯放入窑中烧制。另一些 kiln 用来干燥木材或谷物，温度和用途与烧陶的设备不同；共同点是控制加热空间。','a pottery kiln；a brick kiln；an electric kiln；fire pottery in a kiln。复数 kilns。','oven 常见于食物烘烤，kiln 常见于材料烧制或干燥。kiln 的常用读音末尾有 /n/，不等于 kill“杀死”。',('The bowls were fired in an electric kiln.','这些碗在电窑里烧制。'),('The company dries its timber in a kiln before shipping it.','这家公司先用干燥窑处理木材，再发货。'),sources=[S('kiln'),O('kiln'),'https://en.wiktionary.org/wiki/kiln']),
]
SH=set();EX={'culinarian':'较少见的厨师、烹饪者称呼；本轮优先保留常用 culinary 与 kiln。'}
ROOT=dict(id='C0285',meaning='厨房；烹饪的炉灶',core='一个是厨房里的技艺，一个是炉子本身：culinary 接着“烹饪”这条意思走，kiln 则保留了加热材料的炉窑画面。',image='拉丁 culina 厨房、炉灶 → culinarius／culinaire → culinary 烹饪的；另一条很早借入古英语 cyln → kiln 窑。',intro='这组只有两个常用入口，但能说明一件重要的事：同一个来源，早借入和晚借入的英语词可能长得很不一样。kiln 看不出 culin-，并不妨碍它们有可靠的历史联系。',forms='拉丁 culina 指厨房或炉灶；culinarius 是相应形容词。culinary 经拉丁或法语形容词路线进入英语；kiln 则在古英语时期已有 cyln 等形式，历经后来的拼写变化。',branches=[['烹饪与饮食技艺','culinary'],['炉窑与材料加热','kiln']],contrasts='culinary 是领域形容词，不保证食物好吃；kiln 是设备，不必用来烤食物。英语 kitchen 与 cook 可在更早的烹饪词族背景下比较，但不是把 culinary 直接删字母就变出来的。',practice='The chef studies culinary history; the potter works with a kiln. 厨师研究烹饪史，陶艺师使用窑炉：同一个古老厨房意象，沿不同借入路线进入了两个现代场景。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w and w not in EX]
 assert set(ROOT['words'])=={e['word'] for e in W}
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_134.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('culin:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
