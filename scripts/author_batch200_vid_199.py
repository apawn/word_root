# -*- coding: utf-8 -*-
"""C1037 phyt: growing plants, plankton, and the newcomer metaphor."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('phytoplankton','英 /ˌfaɪtəˈplæŋktən/；美 /ˌfaɪtoʊˈplæŋktən/','浮游植物','水面附近有许多肉眼难以分清的小生命，随水流漂移，并利用阳光制造有机物；它们可以成为水中食物网的起点。','现代科学构词 phyto-“植物” + plankton“浮游生物”。phyto- 接希腊 phyton“植物”，plankton 远接希腊“漂游”的意思；名字保留了把这些光合生物视作植物的一种历史分类方式。',[['希腊 phyton；planktos 一系','植物；漂游'],['现代组合 phyto- + plankton','以“植物型浮游生物”命名'],['英语 phytoplankton','进行光合作用的一类浮游生物']],'浮游植物包括许多藻类，也包括蓝细菌，不能把它们全部归为现代分类中的真正植物。它们可生活在海水或淡水里；“浮游”强调主要随水流运动，不保证每个个体完全没有移动能力。','phytoplankton blooms；phytoplankton growth；feed on phytoplankton。','zooplankton 是浮游动物一系；phytoplankton 强调光合生产者。水里一片漂着的大树叶并不因此就叫 phytoplankton。',('Small aquatic animals feed on phytoplankton near the surface.','小型水生动物以近水面的浮游植物为食。'),('The team measured changes in phytoplankton abundance in the lake.','研究团队测量了湖中浮游植物数量的变化。'),sources=['https://www.merriam-webster.com/dictionary/phytoplankton','https://www.collinsdictionary.com/dictionary/english/phytoplankton','https://oceanservice.noaa.gov/facts/phyto.html']),
E('bryophyte','/ˈbraɪəˌfaɪt/','苔藓植物〔广义可包括苔类、藓类、角苔类〕','石头上、林地里那些低矮的小植物，很多属于苔藓植物。它们没有大树那样的真正木质部输水系统，却有自己的完整生活史。','英语照新拉丁分类名 Bryophyta 形成 bryophyte，后部 -phyte 接希腊 phyton“植物”。bryo- 通常联系 bryon“苔藓”；早期命名者 Braun 自己采用相关动词 bryō“萌发、长出”的解释，不能只当成一个无历史的英语拼词。',[['希腊 bryō／bryon；phyton','萌发／苔藓；植物'],['新拉丁分类名 Bryophyta','19 世纪植物分类命名'],['英语 bryophyte','该类植物的个体名称；广义指苔藓植物']],'普通教材里 bryophytes 常包括苔类、藓类和角苔类；更严格的现代分类里，大写 Bryophyta 可能专指藓类。它们不是“尚未长大的蕨类或树木”，小体型本身就是许多种类的正常状态。','bryophyte species；mosses and other bryophytes；a bryophyte survey。','moss 常指藓；广义 bryophyte 范围更宽。ferns 蕨类有真正的维管组织，因此不属于这一组非维管植物。',('The students found several bryophyte species on the damp rocks.','学生们在潮湿的岩石上发现了几种苔藓植物。'),('The field guide includes mosses, liverworts, and other bryophytes.','这本野外指南收录了藓类、苔类等苔藓植物。'),sources=['https://www.merriam-webster.com/dictionary/bryophyte','https://www.collinsdictionary.com/dictionary/english/bryophyte','https://openstax.org/books/biology-2e/pages/25-3-bryophytes']),
]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());names=['neophyte']+[x['word'] for x in W]
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C1037')
EX={w:'较冷门的真菌病原、植物归化分类或命名术语，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C1037',meaning='生长；植物',core='phyt-／phyto- 接希腊 phyton“植物”，与生长一系相连。字面可以是植物，借喻也可以是刚进入某个领域、像新栽幼苗的人。',image='phyton 植物 → neophyte 新栽者、初学者；phyto- + plankton → 浮游植物；Bryophyta → bryophyte 苔藓植物。',intro='先区分实际植物与人的比喻，再留意科学名称的历史：phytoplankton 里的植物构件，不等于其所有成员都属于现代植物分类。',forms='neophyte 经宗教历史把新栽者用于新入教者、初学者；phytoplankton 是近代组合词；bryophyte 接新拉丁分类名 Bryophyta。',branches=[['新栽幼苗的比喻','neophyte'],['水中的光合浮游生物','phytoplankton'],['苔藓植物','bryophyte']],contrasts='phytoplankton 包括藻类和蓝细菌等，不是漂浮的大植物碎片。bryophyte 的广义范围与大写分类名 Bryophyta 的现代狭义范围要按上下文区分。',practice='把 neophyte 想成刚栽进新领域的幼苗，再分别解释水中光合浮游生物和岩石上的苔藓为什么用 phyt- 命名。',words=names,exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_199.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('phyt:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
