"""A few common omissions and a genuine historical link to the existing day family."""
import json
from pathlib import Path
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={'B2422':['to','tomorrow']}
W('to','弱读 /tə/、/tu/；强调时 /tuː/','到、向；给、对；不定式标记等',
 'go to the door 朝门走，give it to her 交到她手里。常能先想一个指向；to learn 则是引出要做的事，要跟完整句式一起学。',
 '继承古英语 tō，经中古英语延续，属于旧日耳曼语到、向的材料。它也逐渐固定为动词不定式的标记。today、tomorrow 中保留相应旧时间表达，不是表示分开的另一条古前缀。',
 [['古英语 tō → 中古英语 to','向、到及相应时间、关系用法'],['现代介词与不定式标记','go to；give to；want to learn 等结构']],
 'to the station 到车站；to me 对我、给我；want to learn 想学习。look forward to 后的 to 是介词，接 doing，而不是一见 to 就接动词原形。',
 'go to；give to；to learn；look forward to doing。','to、too、two 强读可以同音；too 常说也、太，two 是二。不是每个 to 都能按空间移动硬译。',
 ('She gave the key to her neighbour.','她把钥匙给了邻居。'),('I want to learn how the machine works.','我想学习这台机器如何运作。'))
W('tomorrow','英 /təˈmɒrəʊ/；美 /təˈmɑːroʊ/，亦见 /təˈmɔːroʊ/','明天；未来、来日〔比喻〕',
 '今天之后的那一天。想象夜里睡下，下一次天亮的新一天到来；较旧的早晨材料就藏在这个词里。',
 '古英语 tō morgne 在明日、到翌晨，经中古英语 tomorwe、tomorwen 等合成现代 tomorrow。morgne 是 morgen 早晨的旧变格形式，与 morrow、morning 同族。',
 [['古英语 tō + morgne','旧时间介词与早晨、次日的变格形式'],['中古英语 tomorwe 等 → tomorrow','明天；未来的比喻']],
 'see you tomorrow 明天见；tomorrow morning 明天早晨；a better tomorrow 更好的未来。直接作时间副词时通常不用再加 on 或 at。',
 'tomorrow afternoon；by tomorrow；tomorrow’s meeting。','today 今天，tomorrow 明天，yesterday 昨天；tomorrow morning 是明天早上，不是把 tomorrow 重复说了两遍。',
 ('I will return the book tomorrow.','我明天还书。'),('Tomorrow’s meeting starts at nine.','明天的会议九点开始。'))
W('as','弱读 /əz/；强调时 /æz/','作为、以……身份；像……一样；同样程度地',
 'work as a teacher 是以教师身份工作；as tall as me 是高度与我一样。先抓身份对应、程度相当两种常见关系。',
 '由古英语 eallswā 就这样、同样，经中古英语 alswa、als、as 等缩短，与 also 有共同历史。现代身份、比较等用法分别固定，不把每个 as 都翻成现代 also 也。',
 [['古英语 eallswā → 中古英语 alswa、als、as','同样、正像这样等材料逐渐缩短'],['现代常见身份与程度关系','作为；像……；同样程度地']],
 'use a box as a table 把箱子当桌子；as heavy as mine 和我的一样重；as a child 在小时候、以儿童身份。读比较时前一个 as 修饰程度。',
 'work as；use as；as ... as。','like 更常说像、有相似处，as a teacher 则常说真的以教师身份；He works as a teacher 不只是他干活像个老师。',
 ('She works as a teacher at the local school.','她在当地学校当老师。'),('Your bag is as heavy as mine.','你的包和我的一样重。'))
W('goddamn','英 /ˈɡɒdæm/；美 /ˈɡɑːdæm/，也可读出两个 /d/ 的衔接','该死的；他妈的〔强烈咒骂、加强语气〕',
 '说话人被东西气到，给名词加很重的一层愤怒、烦躁。常用于情绪爆发，不是在平静描述一种物品类别。',
 'God + damn，本来带愿上帝诅咒、惩罚的咒语关系，后来经常作为加强语气的感叹、修饰语。两个 d 在口语中常合并。',
 [['God + damn 的咒语式表达','愿神降罚的旧宗教措辞'],['固定口语加强形式 goddamn','很强的愤怒、烦躁、强调']],
 'this goddamn lock 这该死的锁；a goddamn mess 一团该死的乱局。语气粗鲁，也可能因宗教措辞引人反感；读小说时留意角色口吻。',
 'a goddamn nuisance；not a goddamn thing。','damn 已有咒骂、强调义，goddamn 进一步加重语气；它不等于字面 God 神与 damaged 损坏的任意组合。',
 ('“This goddamn lock is stuck again,” he muttered.','“这该死的锁又卡住了。”他嘟囔道。'),('The character complains that the room is a goddamn mess.','那个角色抱怨说，房间真是他妈的一团糟。'))
W('dammit','/ˈdæmɪt/，亦见 /ˈdæmət/','该死；真倒霉〔表示恼怒、失望等〕',
 '刚想打印，纸又卡住；一句 Dammit! 就把恼火冲出口了。它是感叹，不需要后面再找一个被骂的人。',
 '把 damn it 按常见读音合写，原本不发音的 n 在 dammit 这一路拼写中省去，m 双写。也常见分写 damn it，网络中另有 damnit 等拼法。',
 [['damn it 的感叹用法','咒骂、恼怒或失望的表达'],['合写 dammit','固定口语感叹词']],
 'Dammit, I forgot! 该死，我忘了！；Oh, dammit! 哎呀，该死。不是正式、客气场合的中性语气词。',
 'Oh, dammit!；Dammit, ...。','dammit 是 damn it 的合写，不是 damn + 一个独立后缀 -mit；damned、damning 则是另一种词形、派生关系。',
 ('“Dammit, I left my keys inside,” she said.','“该死，我把钥匙落在里面了。”她说。'),('“Oh, dammit!” he exclaimed when the paper tore.','纸撕破时，他喊了一声：“哎呀，该死！”'))
R('B2637','作为、以某种身份；相同程度的关系','AS：身份对应与程度相当，是两种常见入口',
 'a box used as a table 是当桌子用；as wide as the door 是与门同样宽。先读完整搭配，再选择中文。',
 'as 与 also 共同接古英语 eallswā 等同样、就这样的材料，经中古英语缩短而来。现代用法已经分工，历史相关不代表能互换。',
 'eallswā → alswa、als → as 是历史缩短；work as 接身份，as ... as 表比较。身份、用途与程度相当要按完整搭配分别掌握。',
 [['身份、用途','as a teacher；use as a table'],['相同程度','as tall as；as heavy as']],
 'work as a teacher 通常真是教师身份，work like a teacher 常说像教师那样；as 与 also 的现代句法也不同。',
 'She used the box as a table because it was as high as her chair.\n\n她把箱子当桌子用，因为箱子和椅子一样高。','as')
R('B3720','谴责、诅咒；咒骂与强烈强调','DAMN：从判罪、诅咒，走向恼火的口语语气',
 'damning evidence 是有力揭露罪责、不利的证据；Dammit! 则可能只是丢了钥匙时冒出的一声恼火。',
 'damn 经古法语 damner 接拉丁 damnare 谴责、判罪、使受损，与 damnum 损失有关。宗教诅咒、一般咒骂和口语强调各自发展。',
 'damn + -ing → damning；God + damn → goddamn；damn it 合写 → dammit。damn 中 n 通常不发音。',
 [['谴责、咒骂与证据性质','damn · damning'],['强烈口语修饰、感叹','goddamn · dammit']],
 'damning evidence 不等于证据在开口骂人；goddamn、dammit 带强烈或粗鲁语气，不是普通礼貌加强词。',
 'The investigator found damning evidence in the old files.\n\n调查者在旧档案里找到了对涉事者极为不利的证据。','damn damning goddamn dammit')

def extend_day_lesson():
    content=Path(__file__).resolve().parents[1]/'content/精讲'
    matches=[]
    for path in sorted(content.glob('roots_*.json')):
        records=json.loads(path.read_text())
        for item in records:
            if item['id']=='B2422':matches.append((path,records,item))
    assert len(matches)==1, 'Expected exactly one existing day lesson'
    path,records,item=matches[0]
    for word in EXISTING_ROOT_ADDITIONS['B2422']:
        if word not in item['words']:item['words'].append(word)
        if isinstance(item.get('exclude'),dict):item['exclude'].pop(word,None)
    branch=['日期表达中的旧时间关系','to · today · tomorrow；yesterday']
    if branch not in item['branches']:item['branches'].append(branch)
    note='tomorrow 接古英语 tō morgne，在明日、到翌晨；to 在这里属于时间表达，与 today 中的旧材料相应。'
    if note not in item['forms']:item['forms']+='\n\n'+note
    path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':
    save('continuation_20261030_rv',ROOTS,WORDS)
    extend_day_lesson()
