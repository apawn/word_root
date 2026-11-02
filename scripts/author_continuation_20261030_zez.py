"""Hoarse cries, bird calls, informal complaints and common -y forms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3527':dict(words=['crack','croak','croaks','croaked','croaking','croaky'],label='croak 与 crack：可比较的拟声材料',note='croak 接中古英语 crouken，或拟声，或与古英语 cracian 一系相关；只作有条件的历史比较，不写成现代 crack 按规则变元音得到 croak。'),
 'B4425':dict(words=['tweet','tweets','tweeted','tweeting'],label='tweet：鸟的短鸣到发短消息',note='tweet 先以鸟鸣名词记录，再有动词；网络发文义是后来的借用，两义都可形成 tweeted、tweeting。'),
 'A1699':dict(words=['squeak','squeaky','croak','croaky','chirp','chirpy','yap','yappy'],label='声音基础词加 -y：吱声、沙哑、活泼与吵闹',note='-y 把声响转成“有这种声音或特征”；chirpy 又可形容人精神活泼，squeaky clean 还发展出清白无污点的比喻。'),
 'A1760':dict(words='howl howls howled howling croak croaks croaked croaking holler hollers hollered hollering whine whinge whinges whinged whinging yap yaps yapped yapping hoot hoots hooted hooting chirp chirps chirped chirping tweet tweets tweeted tweeting'.split(),label='嚎叫、嘶哑声、鸟鸣与抱怨动词的变化',note='这些基础词不是一条共同古代词根；howled、croaked、hooted 等按现代规则变化。whinge 与 whine 的旧北方形式相连，holler 则联系 hollo 一类呼喊形式。'),
}
CROAK=[['中古英语 crouken → croak','嘶哑、喉音重的叫声；或拟声，或联系古英语 cracian 一系'],['鸟叫材料扩到蛙鸣、人沙哑说话','后来口语还可说死了；不同语境选择不同中文义']]
W('croak','英 /krəʊk/；美 /kroʊk/','呱呱叫、哑声叫；沙哑地说；〔口语〕死；一声哑叫',
 '像青蛙“呱”一声，或嗓子哑得话从喉咙里粗粗挤出来，叫 croak。抓住低哑、带喉音的感觉。',
 '接中古英语 crouken，或属拟声，或与古英语 cracian 一系相关；不把现代 croak 当 crack 的规则变体。',CROAK,
 'a frog croaks 是青蛙呱叫，croak out a few words 是哑着嗓子挤出几句话。死的口语义带随便、甚至冷淡的语气。',
 'a hoarse croak 沙哑的叫声；croak a reply 哑声回答。',
 'croak 强调沙哑、喉音，squeak 强调细而尖。青蛙只是常见场景，不是这个词唯一能写的声源。',
 ('We could hear the frogs croak beside the pond.','我们听见池塘边青蛙呱呱叫。'),('Her voice had become a croak by the end of the day.','到一天结束时，她的声音已经沙哑得不成样子。'),sources=S('croak','croak'))
W('croaks','英 /krəʊks/；美 /kroʊks/','呱叫、哑声说〔第三人称单数〕；一声声哑叫',
 '一只青蛙一声声“呱”叫，用 croaks；人嗓子哑、粗声说话也能用这个动词。',
 'croak + -s，/k/ 后读 /s/。作名词复数时，数的是沙哑、喉音重的声音。',CROAK+[['croak + -s → croaks','它呱叫、哑声说；多声哑叫']],
 'croaks from the reeds 是在芦苇里呱叫；a few croaks 是几声哑叫。口语死亡义要由情境另辨。',
 'croaks loudly 大声呱叫；low croaks 低哑的叫声。',
 'croaks 能写鸟、蛙或人，并不自动等于蛙的名字；frog 才是动物名，croak 先是声音词。',
 ('A frog croaks near the garden wall every evening.','每天傍晚，花园墙边都有青蛙呱叫。'),('Low croaks came from the reeds.','芦苇丛里传来几声低哑的叫声。'),sources=S('croaks','croak'))
W('croaked','英 /krəʊkt/；美 /kroʊkt/','呱叫了、哑声说了；〔口语〕死了',
 '嗓子哑得说一句话都粗粗的，叫 croaked；青蛙刚才呱叫也一样用。口语里说人或东西完了、死了，要看情境。',
 'croak + 完整 -ed，/k/ 后读 /t/；仍是一个音节，不读成两节。',CROAK+[['croak + -ed → croaked','过去哑叫、沙哑地说；另有口语死亡义']],
 'croaked a reply 是哑声答了一句，croaked out his name 是沙哑地挤出名字；不必真的模仿青蛙。',
 'croaked weakly 虚弱地哑声说；croaked from the pond 从池塘里呱叫。',
 '“Water,” he croaked 里的 croaked 是说话方式，不是人物死了；后接喊话内容常能直接提示这一点。',
 ('“Some water, please,” she croaked.','“请给我点水。”她沙哑地说。'),('A frog croaked as we walked past the pond.','我们走过池塘时，一只青蛙呱地叫了。'),sources=S('croaked','croak'))
W('croaking','英 /ˈkrəʊkɪŋ/；美 /ˈkroʊkɪŋ/','正在呱叫、哑声说；沙哑的；呱叫声',
 '低哑的叫声或蛙声正响着，是 croaking；修饰 voice 时，把人嗓子粗哑的感觉直接说出来。',
 'croak + 完整 -ing，直接加词尾。动词变化不改变 oa 的元音，也不双写 k。',CROAK+[['croak + -ing → croaking','哑叫、沙哑发声的过程或状态']],
 'croaking frogs 是呱叫的青蛙，a croaking voice 是沙哑的声音；the croaking of frogs 把蛙声整体当名词。',
 'croaking in the pond 在池塘里呱叫；stop croaking 停止哑声叫。',
 'croaking 可以写当前发声，croaky 更常直接描述声音沙哑的特点；两者都能修饰 voice，侧重点略不同。',
 ('The croaking of frogs grew louder after dark.','天黑后，青蛙的呱叫声更响了。'),('He answered in a low, croaking voice.','他用低低的沙哑声音回答。'),sources=S('croaking','croak'))
HOWL=[['中古英语 houlen → howl','大概是拖长叫声的拟声材料'],['现代 howl 的多种声源','动物嚎、人放声哭笑、风呼啸；不从现代 owl 猫头鹰前加 h 构成']]
W('howls','/haʊlz/','嗥叫、放声哭笑、呼啸〔第三人称单数〕；一阵阵嚎叫',
 '声音像“嗷——”一样拖开，用 howls；人笑得放声、风刮得呼啸，也能借用这个画面。',
 'howl + -s，/l/ 后读 /z/。名词复数、动词三单同形，不能据词尾断定词性。',HOWL+[['howl + -s → howls','它嚎叫、呼啸；多声、阵阵嚎叫']],
 'howls with laughter 是放声大笑，howls of protest 是大声抗议；不是所有 howl 都在悲伤。',
 'the wind howls 风呼啸；howls of delight 欢乐的大叫。',
 'howls 比 barks 更有拖长声调的感觉；写人 howls with laughter 时，应译大笑而不是像狼一样嗥叫。',
 ('The wind howls around the house at night.','夜里，风在房子周围呼啸。'),('His joke was met with howls of laughter.','他的笑话引来阵阵大笑。'),sources=S('howls','howl'))
W('howled','/haʊld/','嗥叫了、放声哭笑了；呼啸了',
 '狗或狼刚才拉长声音嚎叫，叫 howled；人放声大哭、大笑，风呼啸，也可以这样写。',
 'howl + 完整 -ed，/l/ 后读 /d/；保留基础词的 /aʊ/。',HOWL+[['howl + -ed → howled','过去嚎叫、放声哭笑、呼啸']],
 'howled with laughter 是放声笑了，howled in pain 是痛得大叫；两个搭配共享响亮、拖开的声音。',
 'howled all night 整夜嚎叫；howled through the trees 在树林间呼啸。',
 'howled 描写声音，不必是哭；with laughter 已明确是笑，不能一见 howl 就译成哀嚎。',
 ('The dogs howled when the siren sounded.','警报响起时，狗儿们嗥叫起来。'),('We howled with laughter at the final scene.','看到最后一幕，我们放声大笑。'),sources=S('howled','howl'))
HOLLER=[['hollo 一类呼喊形式 → 美式 holler','招呼、呼喊的形式变化；与 hello 一系可比较'],['现代 holler 动词及名词','口语里大喊、叫某人；也说一声招呼']]
W('holler','英 /ˈhɒlə/；美 /ˈhɑːlər/','〔口语〕大喊、叫喊；喊一声、招呼一声',
 '隔着院子“喂——”地喊人，或需要帮忙时叫一声，就可以说 holler。是很口语的喊法，尤其常见于美式英语。',
 '由 hollo 一类呼喊形式发展，现代 -er 不是“喊叫的人”这个后缀；不是 hollow 空心的加字母变化。',HOLLER,
 'give me a holler 是有事叫我一声、联系我；holler for help 是大喊求助，不一定在生气。',
 'holler across the yard 隔着院子喊；give us a holler 招呼我们一声。',
 'holler at someone 可能是冲人吼，holler to someone 也可只是喊远处的人；关系、语气和场景一起决定态度。',
 ('Give me a holler if you need a hand.','需要帮忙就叫我一声。'),('We had to holler across the river to be heard.','我们得隔着河大喊，对方才听得见。'),sources=S('holler','holler'))
W('hollers','英 /ˈhɒləz/；美 /ˈhɑːlərz/','〔口语〕大喊、招呼〔第三人称单数〕；喊叫声〔复数〕',
 '某人从远处喊话、招呼人，用 hollers；几声喊叫作为名词也能用同样形式。',
 '声音词 holler + -s，读 /z/；另有方言 holler 表山谷、山坳，走 hollow 的另一条线，不混进这里的发声历史。',HOLLER+[['holler + -s → hollers','他、她喊叫；几声招呼']],
 'hollers from the kitchen 是从厨房喊，hollers for us 是大声叫我们；a few hollers 是几声喊叫。',
 'hollers across the street 隔街喊；hollers for help 大喊求助。',
 '声音义 hollers 不等于山谷义 hollers；相同拼写仍要按“人在喊”或“地形”来分。',
 ('Dad hollers from the kitchen when dinner is ready.','晚饭做好时，爸爸从厨房喊一声。'),('A few hollers from the crowd caught our attention.','人群中几声喊叫引起了我们的注意。'),sources=S('hollers','holler'))
W('hollered','英 /ˈhɒləd/；美 /ˈhɑːlərd/','〔口语〕大喊了、叫了一声',
 '刚才隔远喊了人、冲口喊出一句话，用 hollered。它让叙述带上随意、口语的语感。',
 'holler + 完整 -ed，词尾读 /d/；词内的 -er 是基础词一部分，不是先造一个喊叫者名词。',HOLLER+[['holler + -ed → hollered','过去大声喊、招呼']],
 'hollered her name 是大喊了她的名字，hollered across the yard 是隔院子喊；可以接具体喊话。',
 'hollered for help 大喊求助了；hollered back 大声回应了。',
 'hollered 比 called out 更口语；它可以是友好的招呼，不一定含责骂。',
 ('“We are over here!” he hollered.','“我们在这儿！”他大喊。'),('She hollered my name from the end of the street.','她从街道尽头大声喊我的名字。'),sources=S('hollered','holler'))
W('hollering','英 /ˈhɒlərɪŋ/；美 /ˈhɑːlərɪŋ/','〔口语〕正在大喊；一阵喊叫',
 '远处有人正扯着嗓子喊，或一群人叫成一片，是 hollering。既写动作，也可以把喧闹喊声当一个整体。',
 'holler + 完整 -ing；英式在后接元音时发 /r/。不从一个指人 -er 名词去构词。',HOLLER+[['holler + -ing → hollering','进行中的大喊；喊叫活动']],
 'hollering for help 是大喊求助，all that hollering 是那一大阵喊叫；口语场景常见。',
 'hollering across the room 隔房间喊；cheering and hollering 欢呼叫喊。',
 'hollering 可以来自高兴或急切，不自动等于愤怒；whispering 则把音量压低，正好形成声音对照。',
 ('The fans were cheering and hollering outside the stadium.','球迷们在体育场外欢呼叫喊。'),('I could hear someone hollering for help down the lane.','我听见巷子那边有人大喊求助。'),sources=S('hollering','holler'))
WHINGE=[['古英语 hwinsian 等 → 较早北方形式 → whinge','与 whine 的旧声音材料相连，不是现代 whine 加字母 g'],['现代英国等地口语','不满地嘟囔、发牢骚；常含说话者觉得抱怨过多的语气']]
W('whinge','/wɪndʒ/','〔英等地口语〕发牢骚、嘟囔抱怨；一通牢骚',
 '一点不顺心就“怎么又这样啊”地抱怨个不停，可以叫 whinge。说话者常觉得对方小题大做或抱怨太多。',
 '承较早北方形式，联系古英语 hwinsian 与 whine 的声音材料；g 在现代 /dʒ/ 里发音，不是 whine 的装饰字母。',WHINGE,
 'whinge about the weather 是不停抱怨天气，have a whinge 是发一通牢骚；英国、澳大利亚等地口语常用。',
 'stop whingeing 别再发牢骚；whinge about everything 什么都抱怨。',
 'complain 比较中性，可以是合理投诉；whinge 通常带嫌对方爱抱怨的评价，换词会改变态度。',
 ('There is no point in having a whinge about the rain.','为下雨发一通牢骚也没什么用。'),('They always find something to whinge about.','他们总能找出点事来抱怨。'),sources=S('whinge','whinge'))
W('whinges','/ˈwɪndʒɪz/','〔口语〕发牢骚〔第三人称单数〕；一通通牢骚',
 '说某个人每遇到小事就抱怨，用 whinges；名词复数则是一次次发牢骚。这个词本身常带不耐烦的评价。',
 'whinge + -s，基础词保留 e，词尾 /dʒ/ 后读 /ɪz/。不能读成 whines 的 /waɪnz/。',WHINGE+[['whinge + -s → whinges','他、她发牢骚；几通牢骚']],
 'whinges about the price 是嫌价格而发牢骚；a few whinges 是几句、几通抱怨，不是正式投诉的固定名称。',
 'whinges constantly 不停发牢骚；whinges about work 抱怨工作。',
 'whinges 与 whines 历史有关，现代发音、拼写不同；whine 还能写机器、动物的尖细哀鸣。',
 ('He whinges about the journey every Monday.','他每周一都为这段路程发牢骚。'),('I listened to a few whinges about the new timetable.','我听了几通对新时间表的牢骚。'),sources=S('whinges','whinge'))
W('whinged','/wɪndʒd/','〔口语〕发了牢骚、嘟囔抱怨了',
 '过去有人不停说“太麻烦了、太远了”，而叙述者觉得他是在发牢骚，可以用 whinged。',
 'whinge 去掉末尾 e，再加完整 -ed；/dʒ/ 后词尾读 /d/，不是 /ɪd/。',WHINGE+[['whinge 去 e + -ed → whinged','过去发牢骚']],
 'whinged about the food 是为饭菜发牢骚，whinged all the way 是一路抱怨；带口语和评价色彩。',
 'whinged for hours 抱怨了好几小时；whinged about the cost 抱怨花费。',
 'whinged 描写抱怨的方式和说话者态度；reported a problem 更像陈述、反映问题，不带这种贬意。',
 ('He whinged about the early start all the way to the station.','去车站一路上，他都在抱怨出发太早。'),('They whinged for ten minutes and then got on with the job.','他们发了十分钟牢骚，随后继续干活。'),sources=S('whinged','whinge'))
W('whinging','/ˈwɪndʒɪŋ/','〔口语〕正在发牢骚；爱抱怨的；牢骚',
 '抱怨正一句接一句地冒出来，叫 whinging。既能写正在说，也能把让人厌烦的一阵抱怨整体当名词。',
 'whinge 去 e + 完整 -ing → whinging；另有保留 e 的 whingeing，两种拼法都用。这里解释去 e 的形式。',WHINGE+[['whinge 去 e + -ing → whinging','发牢骚过程；也有 whingeing 拼法']],
 'whinging about the weather 是正为天气抱怨，all this whinging 是这一通通牢骚；形容别人时语气偏负面。',
 'constant whinging 不断的牢骚；stop whinging 别再发牢骚。',
 'whinging 读 /ˈwɪndʒɪŋ/，不是 whining /ˈwaɪnɪŋ/；两者可在抱怨义重合，但不能混读。',
 ('Stop whinging and help me carry the bags.','别发牢骚了，帮我提一下袋子。'),('His constant whinging about the weather was tiring.','他不断为天气发牢骚，听着让人累。'),sources=S('whinging','whinge'))
YAP=[['较早 yap 名词及动词 → 现代 yap','大概模仿小狗短促、尖细的叫声'],['狗不停叫 → 人喋喋不休','后来名词还可在粗鲁口语中指嘴；不是一切用法都客气']]
W('yap','/jæp/','尖声吠叫；喋喋不休；短促吠声；〔粗鲁口语〕嘴',
 '小狗“汪汪汪”地尖声叫个不停，像 yap；借来写人，就是让人嫌烦地说个不停。',
 '大概是拟声词；较早有指叫狗的名词记录，后来动词和声音、嘴的名词义继续发展。不是 yelp 的规则缩写。',YAP,
 'yap at the door 是在门边汪汪叫，yap on about something 是不停唠叨；shut your yap 是粗鲁地叫人闭嘴。',
 'yap away 不停叫、说；a sharp yap 一声尖短狗叫。',
 'chat 可以是轻松聊天，yap 写人说话时常带嫌烦的态度；不用把所有健谈的人都描述成 yapping。',
 ('The little dog began to yap at the gate.','小狗开始在大门边尖声叫。'),('He would yap on about the same story for hours.','他会为同一个故事唠叨好几个小时。'),sources=S('yap','yap'))
W('yaps','/jæps/','尖声吠叫、喋喋不休〔第三人称单数〕；尖短叫声〔复数〕',
 '狗每听见动静就尖声叫，或某人说起来没完，用 yaps；作名词复数时是一声声短叫。',
 'yap + -s，/p/ 后读 /s/；名词、动词都直接加词尾，不双写 p。',YAP+[['yap + -s → yaps','它尖声叫；他、她说个不停；数声短叫']],
 'yaps at passersby 是冲路人尖声叫，yaps about work 是没完没了说工作；描述人时语气通常不耐烦。',
 'yaps constantly 不停叫、说；high yaps 尖高的吠声。',
 'yaps 常给人重复、烦人的感觉；barks 可以只是中性的狗叫描述，是否烦人不一定。',
 ('The tiny dog yaps whenever a car goes past.','每次有车经过，那只小狗就尖声叫。'),('A series of yaps came from behind the gate.','大门后传来一连串尖短狗叫。'),sources=S('yaps','yap'))
W('yapped','/jæpt/','尖声吠叫了；喋喋不休地说了',
 '刚才小狗一阵尖声叫，或有人不停唠叨，用 yapped。写人的用法多带嫌对方话太多的意思。',
 'yap 双写 p + 完整 -ed → yapped；基础词是重读单音节、短元音后一个辅音字母，词尾读 /t/。',YAP+[['yap 双写 p + -ed → yapped','过去尖声叫、说个不停']],
 'yapped at the postman 是冲邮递员尖叫，yapped on about the match 是为比赛唠叨个不停。',
 'yapped all morning 整个上午叫、说个不停；yapped excitedly 兴奋地叫。',
 'yapped 与 yelped 都能写小狗，yapped 常突出接连烦人的叫，yelped 常突出尖短冒出的一声。',
 ('The dog yapped at every cyclist who passed.','每个骑车的人经过，那只狗都尖声叫。'),('He yapped on about the match throughout lunch.','整个午饭时间，他都在唠叨那场比赛。'),sources=S('yapped','yap'))
W('yapping','/ˈjæpɪŋ/','正在尖声吠叫；喋喋不休；一阵尖叫或唠叨',
 '狗正“汪汪汪”叫个不停，或人在耳边不停说，叫 yapping。常带吵闹、让人嫌烦的感觉。',
 'yap 双写 p + 完整 -ing → yapping；双写是现代拼写规则，不是新的词根。',YAP+[['yap 双写 p + -ing → yapping','持续尖声叫、喋喋不休']],
 'a yapping dog 是叫个不停的小狗，stop yapping 是别再唠叨、吵了；对人说通常不客气。',
 'yapping away 一直叫、说；constant yapping 不停的尖叫、唠叨。',
 'yapping 与 chatting 都可写说话，前者常有贬意。句子意思相近，选词却能暴露说话者的态度。',
 ('A yapping dog followed us along the fence.','一只尖叫不休的小狗沿着栅栏跟着我们。'),('I could hear them yapping about the game in the next room.','我听见他们在隔壁没完没了地说那场比赛。'),sources=S('yapping','yap'))
HOOT=[['中古英语 houten、huten 等呼喊材料 → hoot','大概与拟声有关；具体更早北欧联系有不同分析'],['猫头鹰咕叫、人的叫喊 → 嘲笑、大笑等用法','a hoot 后来还能说好笑的人或事；not give a hoot 是一点也不在乎']]
W('hoot','/huːt/','咕咕叫；鸣喇叭；起哄、放声笑；咕声；〔口语〕好笑的人或事',
 '猫头鹰“呼、呼”地圆润叫，是 hoot 的典型声音。人群起哄、放声笑，也能用它；a hoot 又可说某人真逗。',
 '接中古英语 houten、huten 等叫喊材料，大概拟声；鸟鸣、起哄等义逐步发展，不是所有用法都从现代猫头鹰名词派生。',HOOT,
 'hoot with laughter 是放声大笑，he is a hoot 是他很逗；not give a hoot 是一点也不在乎，属口语搭配。',
 'an owl’s hoot 猫头鹰的咕叫；hoot at someone 冲某人起哄。',
 '猫头鹰有多种叫声，并非所有鸟都 hoot。screech 偏刺耳尖叫，hoot 更容易让人想到圆润、较低的咕声。',
 ('We heard an owl hoot in the woods.','我们听见树林里猫头鹰咕地叫。'),('Your uncle is a hoot; he had us laughing all evening.','你叔叔真逗，让我们笑了一晚上。'),sources=S('hoot','hoot'))
W('hoots','/huːts/','咕叫、鸣喇叭、起哄〔第三人称单数〕；咕声、起哄声〔复数〕',
 '猫头鹰定时在树上“呼呼”叫，用 hoots；复数名词则是几声咕叫或一阵阵人群叫声。',
 'hoot + -s，/t/ 后读 /s/。三单和名词复数形式相同。',HOOT+[['hoot + -s → hoots','它咕叫、鸣笛；多声咕叫、起哄声']],
 'hoots from the tree 是从树上传来咕叫，hoots of laughter 是一阵阵大笑；不必逐字译成猫头鹰叫。',
 'soft hoots 轻轻的咕叫；hoots of derision 嘲弄的起哄声。',
 'hoots of laughter 是笑声，hoots of derision 是嘲弄声；后面的词帮助区分同一声音词承载的态度。',
 ('An owl hoots outside our window after dark.','天黑后，一只猫头鹰在窗外咕叫。'),('His impression drew hoots of laughter from the audience.','他的模仿引得观众阵阵大笑。'),sources=S('hoots','hoot'))
W('hooted','/ˈhuːtɪd/','咕叫了、鸣喇叭了；起哄了、放声笑了',
 '猫头鹰叫了几声，车喇叭响了，或人们大笑、起哄，用 hooted。先按场景确定是谁在发声。',
 'hoot + 完整 -ed；/t/ 后读 /ɪd/，因此多一个音节，不与 hoot 读成同样长短。',HOOT+[['hoot + -ed → hooted','过去咕叫、鸣笛、起哄或大笑']],
 'hooted with laughter 是放声大笑了，hooted at the speaker 是冲讲话者起哄；鸣喇叭义常见于英式用法。',
 'hooted twice 咕叫、鸣笛两声；hooted in derision 嘲弄地起哄。',
 'hooted 可以描述欢乐，也可描述嘲讽。不能只见中文“起哄”就默认所有例子带恶意。',
 ('The driver hooted twice to let us know he had arrived.','司机按了两声喇叭，告诉我们他到了。'),('The audience hooted with laughter at the joke.','听到笑话，观众放声大笑。'),sources=S('hooted','hoot'))
W('hooting','/ˈhuːtɪŋ/','正在咕叫、鸣笛、起哄；咕声、喇叭声、起哄声',
 '猫头鹰的咕声、喇叭声或人群起哄声正在响，叫 hooting。它可以是一段活动，也可以是一片声音。',
 'hoot + 完整 -ing，直接加；与 hooted 相比，词尾由 /ɪd/ 换成 /ɪŋ/。',HOOT+[['hoot + -ing → hooting','咕叫、鸣笛或起哄的过程、声音']],
 'the hooting of owls 是猫头鹰咕叫，hooting with laughter 是放声大笑；来源材料相通，场景决定具体理解。',
 'hooting horns 鸣响的喇叭；cheering and hooting 欢呼起哄。',
 'hooting 先描写声音，是否友好看场景：笑话后的大笑、嘲弄讲话者的起哄，态度很不同。',
 ('The hooting of an owl carried across the fields.','猫头鹰的咕叫声传过田野。'),('The crowd was cheering and hooting as the team returned.','球队回来时，人群欢呼叫喊。'),sources=S('hooting','hoot'))
CHIRP=[['中古英语 chirpinge 等分词材料 → chirp 一系','基本动词的早期形式由这些记录推知；或拟声，或与 chirken 等旧词有关'],['现代鸟鸣、虫鸣 → 人轻快地说、电子短响','像“啾”或“唧”一下，短而清楚；不限定每一种动物']]
W('chirp','英 /tʃɜːp/；美 /tʃɜːrp/','啾啾叫、唧唧叫；轻快地说；短促鸣响；一声啾鸣',
 '像小鸟“啾”一下、蟋蟀“唧唧”叫，是 chirp。借来写人时，常像精神很好地冒出一句话。',
 '早期记录见中古英语 chirpinge 等分词，基础动词由此推知；或拟声，或与 chirken 等旧发声词相连。现代 chirp 整体使用。',CHIRP,
 'birds chirp 是鸟儿啾鸣，chirp a greeting 是轻快打招呼；小电子设备的短促提示声也能 chirp。',
 'a cheerful chirp 轻快的一声啾鸣；chirp happily 欢快啾叫、说话。',
 'chirp、tweet 都能写短促鸟鸣；croak 偏低哑，screech 偏刺耳，不必把一种鸟永远绑定一个词。',
 ('We heard the birds chirp outside the kitchen window.','我们听见厨房窗外鸟儿啾鸣。'),('“Good morning!” she said with a cheerful chirp.','“早上好！”她用轻快的声音说。'),sources=S('chirp','chirp'))
W('chirps','英 /tʃɜːps/；美 /tʃɜːrps/','啾叫、唧叫、短促鸣响〔第三人称单数〕；短鸣声〔复数〕',
 '小鸟正一声声“啾”叫，或设备偶尔短促响一下，用 chirps。复数名词就是一声声短鸣。',
 'chirp + -s，/p/ 后读 /s/；名词复数和动词三单同形。',CHIRP+[['chirp + -s → chirps','它啾叫、短响；多声短鸣']],
 'chirps from a branch 是在树枝上啾叫，a few chirps 是几声短鸣；闹钟、探测器等主语也可发出 chirps。',
 'chirps softly 轻轻啾叫；short chirps 短促鸣声。',
 'chirps 不一定是歌唱；sing 更容易把连续、有旋律的鸣唱整体提出来，chirp 常突出短促的一声声。',
 ('A small bird chirps on the branch above us.','一只小鸟在我们头顶的树枝上啾叫。'),('A few electronic chirps came from the device.','设备发出几声短促的电子提示音。'),sources=S('chirps','chirp'))
W('chirped','英 /tʃɜːpt/；美 /tʃɜːrpt/','啾叫了、唧叫了；轻快地说了；短促响了',
 '小鸟刚才“啾”一声，人精神十足地说了一句，或机器短响一下，叫 chirped。',
 'chirp + 完整 -ed，/p/ 后读 /t/；ir 的元音保留，整个词仍是一个音节。',CHIRP+[['chirp + -ed → chirped','过去短鸣、轻快说话或短响']],
 'chirped a greeting 是轻快打招呼，the device chirped 是设备短促响了；叙述人说话常带活泼感。',
 'chirped happily 欢快啾叫、说了；chirped once 短鸣一声。',
 'chirped 写人说话时偏轻快，muttered 偏低声嘟囔；两者都交代声音，却给人物不同的精神状态。',
 ('“Ready to go?” she chirped from the doorway.','“准备好出发了吗？”她在门口轻快地问。'),('The small bird chirped and flew to another branch.','小鸟啾叫一声，飞到另一根树枝上。'),sources=S('chirped','chirp'))
W('chirping','英 /ˈtʃɜːpɪŋ/；美 /ˈtʃɜːrpɪŋ/','正在啾叫、唧叫；短鸣声、虫鸣声；轻快地说',
 '一串串清楚、短促的鸟鸣或虫鸣正响着，是 chirping。它把一声声 chirp 合起来，写成整片背景声音。',
 'chirp + 完整 -ing；早期中古英语已有相应分词记录，现代仍能按这一规则理解，不代表历史上先记录基础词。',CHIRP+[['chirp + -ing → chirping','啾鸣、虫鸣的过程与声音']],
 'chirping birds 是啾叫的鸟，the chirping of crickets 是蟋蟀唧唧叫；轻快说话义也能进入进行式。',
 'birds chirping outside 窗外鸟啾叫；constant chirping 不断的唧唧声。',
 'chirping 写声音怎样响，不是动物分类：鸟能 chirp，一些昆虫也能 chirp。',
 ('We woke to the chirping of birds outside the tent.','我们被帐篷外鸟儿的啾鸣唤醒。'),('Crickets were chirping in the long grass.','蟋蟀在高草里唧唧叫。'),sources=S('chirping','chirp'))
TWEET=[['十九世纪 tweet 鸟鸣名词 → 动词','模仿小鸟短促、尖细的鸣声'],['网络语境借用鸟鸣词','用 tweet 说在 Twitter 上发短帖；是新用途，不是鸟鸣来自网站名']]
W('tweeted','/ˈtwiːtɪd/','啾叫了；发推文了、在 Twitter 上发帖了',
 '鸟刚才“啾”地叫，用 tweeted；读到网络旧帖、新闻时，也常说某人发了一条推文。先看主语和内容。',
 'tweet + 完整 -ed，/t/ 后读 /ɪd/，多一个音节。基础 tweet 先有鸟鸣名词，后来才有动词和网络用途。',TWEET+[['tweet + -ed → tweeted','过去啾鸣或发布推文']],
 'tweeted from the tree 是在树上啾鸣，tweeted a photo 是发了一张图片；网络义不说明一定用手机。',
 'tweeted about the event 发帖谈那件事；tweeted a link 发了一个链接。',
 'tweeted 的两义共用同一读音。网络用法是借鸟的短鸣作名称，不能反过来说鸟在模仿电子消息。',
 ('A bird tweeted from the branch above the window.','窗上方的树枝上传来鸟儿啾鸣。'),('She tweeted a photo of the finished mural.','她发了一张壁画完工后的照片到 Twitter。'),sources=S('tweeted','tweet'))
W('tweeting','/ˈtwiːtɪŋ/','正在啾叫；正在发推文；鸟鸣、发推文活动',
 '鸟一声声短鸣，是 tweeting；网络语境里，则是正在发推文，或把发帖这件事整体说出来。',
 'tweet + 完整 -ing，直接加；tweet 的鸟鸣基础先于网络义，两个义项都按同样规则变化。',TWEET+[['tweet + -ing → tweeting','啾鸣过程；发布推文的过程、活动']],
 'birds tweeting 是鸟儿啾鸣，tweeting about a concert 是发推文谈音乐会；看 about 后的信息常能分清。',
 'tweeting from the garden 在花园里啾鸣；live tweeting 实时发帖记录。',
 'tweeting 不必一律翻成网络行为；自然描写里的 birds tweeting 仍是普通的鸟鸣。',
 ('We could hear the birds tweeting in the garden.','我们听见花园里鸟儿啾鸣。'),('He spent the evening tweeting about the concert.','他那晚一直在发推文谈音乐会。'),sources=S('tweeting','tweet'))
W('squeaky','/ˈskwiːki/','吱吱响的；声音尖细的；〔squeaky clean〕清白无污点的',
 '门一动就“吱”响，或嗓音细高，叫 squeaky。-y 把 squeak 那种声音变成东西或声音的特点。',
 'squeak + 形容词后缀 -y；基础拟声词不变。后来 squeaky clean 从极干净的感觉扩成清白、没有丑闻污点。',[['中古英语 squeken → squeak','尖细、短促的吱声材料'],['squeak + -y → squeaky','有吱声、声音尖细的；squeaky clean 后有清白义']],
 'a squeaky door 是吱响的门，a squeaky voice 是尖细嗓音；squeaky clean 可说东西特别干净，也可说形象清白。',
 'squeaky shoes 吱响的鞋；a squeaky clean image 清白无污点的形象。',
 'squeaky 不等于音量一定大：声音可以又轻又尖细。与 loud 的“响”是两个不同方面。',
 ('The squeaky door needs a little oil.','这扇吱响的门需要上点油。'),('She spoke in a high, squeaky voice.','她说话的声音又高又细。'),sources=S('squeaky','squeaky'))
W('croaky','英 /ˈkrəʊki/；美 /ˈkroʊki/','嗓音沙哑的、低哑的',
 '嗓子像蛙叫那样粗粗哑哑，叫 croaky。主要形容声音的质感，不表示说话内容好不好。',
 'croak + 形容词后缀 -y，把沙哑叫声变成“有这种声音特点”。不是另一个独立的古代词根。',CROAK+[['croak + -y → croaky','有哑声特点；嗓音沙哑']],
 'a croaky voice 是沙哑嗓音，sound croaky 是听起来嗓子哑；它并不单凭声音指定原因。',
 'a low, croaky voice 低而沙哑的声音；feel croaky 觉得嗓子哑。',
 'croaky 偏喉音粗哑，squeaky 偏细高；一个人的嗓音也可能在不同时候有不同特点。',
 ('My voice was croaky after an evening of cheering.','欢呼了一晚上后，我的嗓音哑了。'),('He answered the phone in a croaky voice.','他用沙哑的声音接了电话。'),sources=S('croaky','croak'))
W('chirpy','英 /ˈtʃɜːpi/；美 /ˈtʃɜːrpi/','活泼轻快的、精神十足的；啾啾叫的',
 '像小鸟啾啾叫那样轻快、有精神，叫 chirpy。常形容人兴致好、说话活泼，带口语感。',
 'chirp + 形容词后缀 -y；从有啾鸣的特点，扩到人的活泼、轻快，不要求人真的学鸟叫。',CHIRP+[['chirp + -y → chirpy','有鸟鸣般轻快感；人活泼有精神']],
 'feel chirpy 是觉得精神挺好，a chirpy greeting 是轻快的招呼；语境也能带一点嫌人过分兴奋的意思。',
 'a chirpy voice 轻快的嗓音；look surprisingly chirpy 看起来意外地精神好。',
 'chirpy 比 happy 更具体，常让人听见、看见外露的活泼劲；不是所有安静的开心都适合 chirpy。',
 ('You sound very chirpy this morning.','你今天早上听着挺有精神。'),('She greeted us with a chirpy “Hello!”','她轻快地跟我们说了声“你好！”'),sources=S('chirpy','chirp'))
W('yappy','/ˈjæpi/','爱尖声叫的；喋喋不休、吵闹的',
 '小狗动不动就尖声叫，叫 yappy；形容人则像说“话太多、吵个不停”，常带嫌烦的态度。',
 'yap 双写 p + 形容词后缀 -y → yappy；把短促尖叫的动作变成一种经常表现出的特点。',YAP+[['yap 双写 p + -y → yappy','容易尖声叫；爱吵闹、说个不停']],
 'a yappy little dog 是爱尖声叫的小狗；a yappy person 不是客气地夸健谈，而是嫌对方喋喋不休。',
 'small yappy dogs 爱尖叫的小狗；a yappy neighbour 吵闹话多的邻居。',
 'talkative 较中性地说健谈，yappy 带吵、烦的感觉；描述别人时，这个差别比中文“爱说话”更重要。',
 ('A yappy little dog lives next door.','隔壁住着一只爱尖声叫的小狗。'),('I found the radio host a bit too yappy.','我觉得那个电台主持人有点话多吵闹。'),sources=S('yappy','yap'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zez',ROOTS,WORDS)
 extend_lessons()
