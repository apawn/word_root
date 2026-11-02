"""Dozing, snoozing and drowsiness, with the older sloth family."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2954':dict(words='doze dozes dozed dozing dozy snooze snoozes snoozed snoozing snoozer snoozers'.split(),label='doze 与 snooze：睡一小会儿',note='这里和 sleep 作近义比较，不把两个词说成从现代 sleep 派生。doze 可能来自北欧日耳曼打盹材料；snooze 来源未定，可能模拟鼾声。'),
 'A1699':dict(words='drowsy drowsier drowsiest drowsily drowse drowses drowsed drowsing'.split(),label='drowsy 与 drowse：昏昏欲睡、半睡着',note='drowsy 可能最终接古英语下沉、变得迟缓材料，但中古有记录空白；现代 drowse 可能由较早 drowsy 逆构。学习动词先后不代表历史记录顺序。'),
 'B2488':dict(words='sloth slothful slothfully slothfulness'.split(),label='slothful：懒散得不愿动',note='sloth 的懒散名词联系 slow 与抽象 -th 材料；动物树懒名称后来才出现。slothful 由懒散义加 -ful，不是说一个人长满了树懒。'),
}
DOZE=[['doze 可能借自北欧日耳曼打盹材料','如古诺尔斯语 dusa；更远关系不能简单按现代英语字母拆'],['英语动词打盹 → 名词一次浅睡','现代 doze off 常说不知不觉打起盹']]
SNOOZE=[['snooze 早为口语、行话中的睡觉动词','来源未定，可能模拟鼾声'],['动词 → 小睡名词；后来用于闹钟延后提醒','词源猜测不是确定的 sn- 加一个有固定义的后缀']]
DROWSE=[['drowsy 较早；可能接古英语下沉、变迟缓材料','中古记录有空白，不能写成已证实无间断传承'],['现代 drowse 可能由 drowsy 逆构','动词说半睡、昏昏欲睡；形容词说这种状态']]
SLOTH=[['中古英语 slow 相关材料 + 抽象 -th → sloth','懒散、怠于做事；动物树懒名称较晚'],['sloth + -ful → slothful','具有懒散性质，再可加 -ly、-ness']]
W('doze','英 /dəʊz/；美 /doʊz/','打盹、浅睡；一次小睡',
 '坐在椅子里眼睛慢慢闭上，稍有动静又醒来，就是 doze。doze off 常说没打算睡，却不知不觉打起盹。',
 '可能来自北欧日耳曼打盹材料，如古诺尔斯语 dusa；英语先有动词，再有一次浅睡的名词。不要按现代字母硬切前后缀。',DOZE,
 'doze in a chair 坐在椅子里打盹；have a doze 打个盹。',
 'doze off 打起盹、睡过去；a short doze。',
 'doze 突出浅睡，sleep 更宽；nap 常指一小段睡眠，可以有意安排，不一定不知不觉。',
 ('I began to doze in the warm afternoon sun.','暖暖的午后阳光让我开始打盹。'),('She had a short doze before the evening concert.','晚间音乐会前，她打了个小盹。'),sources=S('doze','doze'))
W('dozes','英 /ˈdəʊzɪz/；美 /ˈdoʊzɪz/','打盹〔第三人称单数〕；几次小睡',
 '猫一晒太阳就打盹，可以说 dozes；一下午睡睡醒醒的几次浅睡，也可数作 dozes。',
 'doze + -s，拼写只添 -s，/z/ 后读 /ɪz/；动词三单和名词复数同形。',DOZE+[['doze + -s → dozes','他、它打盹，或多次浅睡']],
 'dozes by the fire 在炉火旁打盹；short dozes 几次短浅的睡眠。',
 'dozes off on the sofa；dozes in the sun。',
 'dozes 说浅睡，rests 只说休息；闭眼休息可能还清醒。',
 ('The cat dozes on the sunny windowsill.','猫在阳光下的窗台上打盹。'),('His afternoon was broken into several short dozes.','他一下午断断续续打了几次短盹。'),sources=S('dozes','doze'))
W('dozed','英 /dəʊzd/；美 /doʊzd/','打盹、浅睡了',
 '刚才在车上眯了一会儿，没睡得很沉，可以说 dozed。接 off 时，强调从清醒滑进睡意的那一下。',
 'doze 去 e 加完整 -ed，/z/ 后读 /d/；不是 /ɪd/，与 dozes 的 /ɪz/ 区分。',DOZE+[['doze + -ed → dozed','过去浅睡、打盹']],
 'dozed for ten minutes 打盹十分钟；dozed off 睡过去了。',
 'dozed in an armchair；had dozed during the journey。',
 'dozed 不保证睡得深、睡得久，slept soundly 才突出睡得沉；小盹和沉睡程度不同。',
 ('I dozed for a few minutes on the train.','我在火车上打了几分钟盹。'),('He dozed off before the film ended.','电影还没结束，他就打盹睡过去了。'),sources=S('dozed','doze'))
W('dozing','英 /ˈdəʊzɪŋ/；美 /ˈdoʊzɪŋ/','正在打盹、浅睡',
 '人靠在椅背上，头一点一点，声音稍大又睁眼，是 dozing。它写浅睡的过程，不一定是一整段安稳睡眠。',
 'doze 去 e 加 -ing；/z/ 留在词中，不变成 /s/。',DOZE+[['doze + -ing → dozing','浅睡、打盹的过程']],
 'dozing in a chair 坐着打盹；dozing off 开始打起盹。',
 'caught him dozing 看见他在打盹；half the afternoon dozing。',
 'dozing 是已经进入浅睡，feeling sleepy 是觉得困；困了但还清醒，不必说已在打盹。',
 ('She was dozing in a chair by the window.','她坐在窗边的椅子里打盹。'),('I kept dozing off and waking again.','我不断打起盹，又醒过来。'),sources=S('dozing','doze'))
W('dozy','英 /ˈdəʊzi/；美 /ˈdoʊzi/','困倦、昏昏欲睡的；迷糊迟钝的〔尤英式〕',
 '眼皮沉、脑子没完全清醒，可以说 dozy。英式口语里也可嫌人迷糊、反应慢，语气可能带批评。',
 'doze 去 e 加 -y，表示容易打盹、带睡意的性质；并不是把 dozy 当成过去式。',DOZE+[['doze + -y → dozy','想睡、昏沉，或引申为迷糊迟钝']],
 'feel dozy 觉得困；a dozy mistake 迷迷糊糊犯的错。',
 'a warm, dozy afternoon；look a little dozy。',
 'dozy 可说暂时困倦，也可带嫌人不机灵的语气；sleepy 通常更直接说想睡，评价较少。',
 ('The warm room made me feel dozy.','房间暖暖的，让我昏昏欲睡。'),('That was a dozy mistake to make.','犯这个错可真够迷糊的。'),sources=S('dozy','doze'))
W('snooze','英 /snuːz/；美 /snuz/','小睡、打盹；闹钟的稍后再响功能',
 '窝在沙发上舒服地睡一小会儿，是 snooze。闹钟响了按 Snooze，就是让它过一会儿再叫，给自己再眯几分钟。',
 '来源未定，可能模拟鼾声；英语先有口语动词，后来有小睡名词，再发展出闹钟延后提醒的用法。',SNOOZE,
 'have a snooze 小睡一下；hit snooze 按延后闹钟。',
 'snooze on the sofa；the snooze button 闹钟延后键。',
 'snooze 常轻松口语，nap 也说短睡；snooze button 是稍后再响，turn off the alarm 则是关掉闹钟。',
 ('I had a quick snooze after lunch.','午饭后我小睡了一会儿。'),('She hit snooze and pulled the blanket over her head.','她按了稍后再响，把毯子拉过头顶。'),sources=S('snooze','snooze'))
W('snoozes','英 /ˈsnuːzɪz/；美 /ˈsnuzɪz/','小睡、打盹〔第三人称单数〕；几次小睡',
 '他饭后喜欢眯一会儿，可以说 snoozes；几次短睡也叫 snoozes。这个词常有轻松、日常的感觉。',
 'snooze + -s，/z/ 后读 /ɪz/；动词三单与名词复数同形。',SNOOZE+[['snooze + -s → snoozes','他、它小睡，或多次短睡']],
 'snoozes after lunch 饭后小睡；short snoozes 短短的几次小睡。',
 'snoozes in the sun；takes regular snoozes。',
 'snoozes 常让人想到短睡，sleeps 可以从几分钟到一整夜；长短要由上下文补足。',
 ('He snoozes on the sofa after lunch.','午饭后，他常在沙发上小睡。'),('She takes brief snoozes between long stretches of work.','长时间工作之间，她会短短地眯几次。'),sources=S('snoozes','snooze'))
W('snoozed','英 /snuːzd/；美 /snuzd/','小睡、打盹了；延后提醒了',
 '刚才在沙发上睡了一小会儿，可以说 snoozed。软件里 snoozed a reminder 也可以是把提醒先延后，让它以后再出现。',
 'snooze 去 e 加完整 -ed，读 /d/；现代提醒用法借用稍后再叫醒的画面。',SNOOZE+[['snooze + -ed → snoozed','过去小睡，或把提醒延后']],
 'snoozed for an hour 小睡一小时；snoozed the reminder 延后提醒。',
 'snoozed in the shade；snoozed until noon。',
 'snoozed a reminder 是暂时推后，deleted a reminder 是删掉；稍后再处理和永久移除不同。',
 ('The dog snoozed beside the warm stove.','狗在暖暖的炉子旁打盹。'),('I snoozed the reminder until Monday morning.','我把提醒延后到了周一早晨。'),sources=S('snoozed','snooze'))
W('snoozing','英 /ˈsnuːzɪŋ/；美 /ˈsnuzɪŋ/','正在小睡、打盹；延后提醒',
 '在温暖角落里眯着，是 snoozing；在软件里则可能是让提醒暂时睡一会儿、以后再出现。要看主语和宾语。',
 'snooze 去 e 加 -ing；小睡动词的动作过程，也用于闹钟、提醒的现代延后操作。',SNOOZE+[['snooze + -ing → snoozing','短睡，或让提醒稍后出现的过程']],
 'snoozing on the sofa 在沙发上打盹；snoozing a reminder 延后提醒。',
 'caught someone snoozing；snoozing peacefully。',
 'snoozing 是睡着或延后提醒，ignoring an alarm 是不理闹钟；不理不一定操作了延后功能。',
 ('The cat was snoozing in a cardboard box.','猫正在纸箱里打盹。'),('Snoozing the reminder gives me time to finish the current task.','把提醒延后，能让我先完成手头的任务。'),sources=S('snoozing','snooze'))
W('snoozer','英 /ˈsnuːzə/；美 /ˈsnuzɚ/','打盹的人；无聊得让人想睡的事物〔口语〕',
 '一场片子看得人直想打盹，可以嫌它是 a snoozer。这个词既能说睡的人，也能说让人想睡的电影、比赛、节目。',
 'snooze 去 e 加完整 -er；由睡的动作说做这个动作的人，再可用让人打盹的画面形容无聊事物。',SNOOZE+[['snooze + -er → snoozer','打盹者；也可指无聊到催眠的事物']],
 'a real snoozer 真够无聊的东西；a light snoozer 容易醒的打盹者。',
 'call a film a snoozer；a comfortable snoozer。',
 'a snoozer 说作品、活动无趣，a sleeper hit 是后来才走红的作品；都带睡的字眼，评价完全不同。',
 ('The film looked exciting in the trailer but turned out to be a snoozer.','预告片看着刺激，电影却无聊得让人想睡。'),('He is a light snoozer and wakes at the smallest sound.','他打盹睡得浅，一点声音就醒。'),sources=S('snoozer','snooze'))
W('snoozers','英 /ˈsnuːzəz/；美 /ˈsnuzɚz/','打盹的人〔复数〕；无聊得催眠的事物〔复数，口语〕',
 '几个趴着睡的人是 snoozers；几部无聊得让人犯困的片子，也可被嫌弃为 snoozers。复数没改变这两种观察方向。',
 'snoozer + -s，读 /z/；先从 snooze 去 e 加 -er，再用复数说多人、多件事物。',SNOOZE+[['snooze → snoozer → snoozers','打盹，到打盹者或催眠事物，再到复数']],
 'a few snoozers 几个打盹的人；several snoozers among the films。',
 'the snoozers on the sofa；reviews dismissing films as snoozers。',
 'snoozers 说节目、比赛时是主观嫌无聊，不等于收视率低；热门节目也可能让某位观众犯困。',
 ('Several films in the series were complete snoozers.','这个系列里有几部电影无聊透了。'),('The noise from the kitchen woke the snoozers on the sofa.','厨房的响动叫醒了沙发上那几个打盹的人。'),sources=S('snoozers','snooze'))
W('drowse','/draʊz/','昏昏欲睡；半睡半醒地打盹',
 '眼睛快闭上，又隐约听得见周围的声音，是 drowse。它比日常的 feel sleepy 稍有描写感，常写安静、温暖的场景。',
 '现代动词可能由较早 drowsy 逆构。古英语有相近材料，但中间记录空白很长，不能直接说现代词毫无变化地传下来。',DROWSE,
 'drowse in a chair 在椅子上半睡着；drowse away the afternoon。',
 'drowse by the fire；fall into a drowse 进入半睡状态。',
 'drowse 说半睡、被睡意压着，daydream 是清醒时走神做白日梦；注意力不在现场的原因不同。',
 ('I began to drowse beside the warm fire.','我在暖暖的炉火旁开始昏昏欲睡。'),('They would drowse in the shade after lunch.','午饭后，他们会在阴凉处半睡半醒地打盹。'),sources=S('drowse','drowse'))
W('drowses','/ˈdraʊzɪz/','昏昏欲睡、半睡着〔第三人称单数〕',
 '午后他坐在椅子里，精神慢慢沉下去，是 drowses。句子常有一层安静、昏沉的描写感。',
 'drowse + -s，/z/ 后读 /ɪz/；现代动词可能由 drowsy 逆构，不把较短形式排成确定的最早祖先。',DROWSE+[['drowse + -s → drowses','他或它半睡着、昏昏欲睡']],
 'drowses by the window 在窗边打盹；drowses in the afternoon。',
 'drowses beside the fire；drowses in a chair。',
 'drowses 比 is sleepy 更像写出正在半睡的动作；有睡意和已在打盹仍可区分。',
 ('He drowses in his chair after lunch.','午饭后，他坐在椅子里昏昏欲睡。'),('The cat drowses beside the fire.','猫在炉火旁半睡半醒地打盹。'),sources=S('drowses','drowse'))
W('drowsed','/draʊzd/','昏昏欲睡、半睡着了',
 '刚才没有彻底睡沉，只是在椅子里昏昏沉沉地眯着，是 drowsed。这个词常用于叙述一段慢下来的时间。',
 'drowse 去 e 加完整 -ed，/z/ 后读 /d/；过去式、过去分词。',DROWSE+[['drowse + -ed → drowsed','过去处在半睡、昏沉状态']],
 'drowsed in the sun 晒着太阳打盹；drowsed for a while。',
 'drowsed beside the fire；drowsed through the afternoon。',
 'drowsed 突出半睡，stayed awake 才是保持清醒；隐约听得见声音不保证一直完全清醒。',
 ('We drowsed in the warm afternoon sun.','我们晒着暖暖的午后阳光，昏昏欲睡。'),('She drowsed in an armchair while the rain tapped the window.','雨点敲着窗，她在扶手椅里半睡半醒地眯着。'),sources=S('drowsed','drowse'))
W('drowsing','/ˈdraʊzɪŋ/','正在昏昏欲睡、半睡着',
 '书还摊在膝上，人已经像快沉进睡里，就是 drowsing。它把睡意中的过程写出来，不一定是熟睡。',
 'drowse 去 e 加 -ing；/z/ 保留，词尾 -ing 表示动作过程。',DROWSE+[['drowse + -ing → drowsing','半睡、昏沉的过程']],
 'drowsing in a chair 坐在椅子里打盹；drowsing by the fire。',
 'a drowsing cat；drowsing in the afternoon heat。',
 'drowsing 与 dozing 都可说浅睡，前者常有更浓的半醒、睡意沉沉的描写感；不是精确的睡眠阶段名称。',
 ('He was drowsing with a book open on his knees.','他膝上摊着书，已经昏昏欲睡。'),('The dog lay drowsing in the afternoon warmth.','狗躺在午后的暖意里，半睡半醒。'),sources=S('drowsing','drowse'))
W('drowsier','英 /ˈdraʊziə/；美 /ˈdraʊziɚ/','更困倦、更昏昏欲睡的',
 '一开始还能认真听，越待越觉得眼皮重，就是 getting drowsier。它比较的是睡意更强，不是做事更不愿意。',
 'drowsy 把 y 改 i，加完整比较级 -er → drowsier；不是把原词尾 y 直接删掉只添 r。',DROWSE+[['drowsy + -er → drowsier','睡意比之前或另一个人更重']],
 'feel drowsier 觉得更困；grow drowsier 越来越昏昏欲睡。',
 'drowsier than before；getting drowsier by the minute。',
 'drowsier 比的是想睡，lazier 比的是不愿用力、做事；困倦程度不等于懒惰程度。',
 ('I grew drowsier as the room became warmer.','房间越暖，我越觉得困。'),('She felt drowsier after a long afternoon indoors.','在室内待了漫长的一下午后，她更昏昏欲睡了。'),sources=S('drowsier','drowse'))
W('drowsiest','/ˈdraʊziɪst/','最困倦、最昏昏欲睡的',
 '一天里最容易眼皮打架的那一段，或一群人里最犯困的一个，可以用 drowsiest。要有一个明说或能理解的比较范围。',
 'drowsy 把 y 改 i，加完整最高级 -est → drowsiest；和比较级 drowsier 配着认。',DROWSE+[['drowsy + -est → drowsiest','在某个范围中睡意最重']],
 'the drowsiest part of the day 一天里最犯困的时段；the drowsiest passenger。',
 'at my drowsiest 在我最困的时候；the drowsiest of the group。',
 'drowsiest 不必是已经睡着的人；most deeply asleep 是睡得最沉，状态不同。',
 ('The hour after lunch is often the drowsiest part of my day.','午饭后的一个小时常是我一天里最犯困的时候。'),('Even the drowsiest passenger looked up when the music began.','音乐响起时，连最犯困的乘客都抬头看了。'),sources=S('drowsiest','drowse'))
W('drowsily','/ˈdraʊzɪli/','睡意沉沉地；半醒半睡地',
 '刚被叫醒，眼睛只睁开一点，声音也软绵绵的，是 drowsily。它让读者看见带着睡意做动作的样子。',
 'drowsy 的 y 改 i，加 -ly → drowsily；副词说回答、睁眼、抬头等动作的方式。',DROWSE+[['drowsy + -ly → drowsily','带着困倦、睡意地行动']],
 'answer drowsily 睡意沉沉地回答；blink drowsily 困倦地眨眼。',
 'murmur drowsily；open her eyes drowsily。',
 'drowsily 是带睡意的方式，drowsy 是困倦的性质：answer drowsily；a drowsy answer。',
 ('She opened her eyes drowsily.','她睡意沉沉地睁开眼睛。'),('He murmured drowsily that he wanted five more minutes.','他半梦半醒地嘟囔，说还想再睡五分钟。'),sources=S('drowsily','drowse'))
W('slothful','英 /ˈsləʊθfəl/；美 /ˈsloʊθfəl/','懒散、怠惰的〔较正式〕',
 '该动手却懒得动，责任也拖着不管，可以说 slothful。比 lazy 更书面，常带对懒散的批评，有时出现在道德、宗教语境。',
 'sloth 懒散 + -ful；sloth 联系 slow 与抽象 -th 材料。懒散义比树懒这个动物名称早，不能反过来说先从动物得来。',SLOTH,
 'a slothful habit 懒散习惯；a slothful afternoon 懒懒散散的一下午。',
 'slothful behaviour；a slothful character。',
 'slothful 常批评不愿行动，tired 是疲劳；累得休息和懒得尽责不是同一判断。',
 ('The story contrasts an energetic worker with a slothful neighbour.','故事把勤快的工人与懒散的邻居作了对照。'),('We allowed ourselves a slothful afternoon after the busy week.','忙了一周后，我们允许自己懒懒散散地过一个下午。'),sources=S('slothful','slothful'))
W('slothfully','英 /ˈsləʊθfəli/；美 /ˈsloʊθfəli/','懒散、怠惰地〔较正式〕',
 '能动也不愿动，动作慢吞吞地拖着，是 slothfully。常有旁观者嫌人懒散的评价，也可用来描写一种故意放松的姿态。',
 'slothful + -ly；-ful 与 -ly 各保留一个 l，形成 slothfully。',SLOTH+[['slothful + -ly → slothfully','以懒散的方式行动']],
 'move slothfully 懒懒散散地移动；lie slothfully 懒洋洋地躺着。',
 'slothfully stretch；slothfully postpone a task。',
 'slothfully 带懒散评价，slowly 只说慢；小心走得慢或体力有限，不应自动说成懒。',
 ('He stretched slothfully on the sofa.','他在沙发上懒洋洋地伸了伸身子。'),('The character moves slothfully through a day with no plans.','那个角色没什么安排，懒懒散散地过着一天。'),sources=S('slothfully','slothful'))
W('slothfulness','英 /ˈsləʊθfəlnəs/；美 /ˈsloʊθfəlnəs/','懒散、怠惰这种性质〔较正式〕',
 '讨论一个人长期不肯行动、不尽责任的懒散习惯，可以用 slothfulness。它把 slothful 的性质拿出来当作一件事谈。',
 'slothful + -ness；完整保留 -ful，再加 -ness 表性质、状态。',SLOTH+[['slothful + -ness → slothfulness','懒散、怠惰这种性质']],
 'criticise slothfulness 批评懒散；a reputation for slothfulness。',
 'slothfulness and neglect 懒散与疏忽；accused of slothfulness。',
 'slothfulness 带责备，inactivity 只说没有活动；不活动可能是等待、休息，也可能有别的原因。',
 ('The narrator blames the character’s failures on slothfulness.','叙述者把那个角色的失败归咎于懒散。'),('What looked like slothfulness was actually uncertainty about the next step.','看似懒散不动，实际上是不知道下一步该做什么。'),sources=S('slothfulness','slothful'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhm',ROOTS,WORDS)
 extend_lessons()
