"""Short cries, squeaks, piercing voices and two histories of snarl."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3513':dict(words=['bark','barks','barked','barking'],label='bark 的吠叫与喝令变化',note='声音动词承古英语 beorcan；同形树皮另有斯堪的纳维亚来源，不能从狗叫推导树皮。'),
 'B3849':dict(words=['yell','yelp','yelps','yelped','yelping'],label='yell 与 yelp：古老叫喊材料的不同发展',note='yelp 承古英语 gielpan，自夸、欢呼一类旧义后来转向尖短叫声；与 yell 可作较远同源比较，不是现代 yell 加 p。'),
 'A1760':dict(words='barks barked yelp yelps yelped yelping squeak squeaks squeaked squeaking squeal squeals squealed squealing shriek shrieks shrieked shrieking screech screeches screeched screeching bawl bawls bawled bawling snarl snarls snarled snarling scream screams screamed screaming'.split(),label='吠叫、尖叫及缠结动词的现代变化',note='这些基础词供理解 -ed、-ing 等现代变化，并非同一个古代词根；snarl 的露齿低吼与缠结分两条近源，squeaked、shrieked、screeched 的词尾读 /t/。'),
}
BARK=[['古英语 beorcan → 中古英语 berken、barken → bark','狗一声声短促吠叫'],['现代声音动词的扩展','人厉声说、喝令；同形树皮义另有来源']]
W('barks','英 /bɑːks/；美 /bɑːrks/','吠叫、喝令〔第三人称单数〕；一声声吠叫',
 '狗“汪、汪”地叫，用 barks；人把命令短而冲地喊出来，也能这样写。作复数名词时，指一声声叫声。',
 '声音动词或名词 bark + -s；/k/ 后读 /s/。若上下文说不同种树皮，则是同形树皮名词的复数，来源另分。',BARK+[['bark + -s → barks','它吠叫；数声吠叫']],
 'barks at strangers 是朝陌生人叫，barks orders 是厉声下令。a few barks 是几声狗叫，不是几只狗。',
 'barks loudly 大声吠叫；sharp barks 尖厉的吠声。',
 'barks 常是一声声短促的爆发；howls 更容易让人想到拖长的嗥叫。两者都能写狗，但声音不同。',
 ('The dog barks whenever someone rings the bell.','每次有人按门铃，那只狗就叫。'),('Two sharp barks came from the garden.','花园里传来两声尖厉的狗叫。'),sources=S('barks','bark'))
W('barked','英 /bɑːkt/；美 /bɑːrkt/','吠叫了；厉声说了、喝令了',
 '狗刚才猛地叫了几声，或一个人冲口发出命令，叫 barked。说话义带短、硬、冲的声音感觉。',
 'bark + 完整 -ed；/k/ 后读 /t/。树皮语境中的 bark 动词如剥皮，也有同形过去式，不能混成吠叫演化。',BARK+[['bark + -ed → barked','过去吠叫、厉声说']],
 'barked at the visitor 是朝来客叫，barked an order 是喝出一道命令；后者可以接具体说的话。',
 'barked twice 叫了两声；barked a warning 厉声发出警告。',
 'said 只交代说了，barked 还让读者听见说话的冲劲；语气强硬不一定音调很高。',
 ('The dog barked twice and ran to the gate.','狗叫了两声，跑向大门。'),('“Stop there,” the guard barked.','“站住。”守卫厉声喝道。'),sources=S('barked','bark'))
YELP=[['古英语 gielpan、gelpan → 中古英语 yelpen','原有自夸、欢呼一类义，随后发展出大声叫喊'],['后来 yelp 的主要声音义','短而尖的一声叫；动物的尖叫、人吃痛或受惊的叫声']]
W('yelp','/jelp/','尖叫、短促地叫；一声尖叫',
 '像被突然踩到尾巴的小狗，或人碰到烫东西时“呀”一声，叫 yelp。抓住短、尖、猛地冒出来的声音。',
 '承古英语 gielpan，经中古英语 yelpen；更早有自夸、欢呼义，后来集中到尖短叫声。不是现代 yell 加一个 p。',YELP,
 'give a yelp 是尖叫一声，yelp in pain 是吃痛叫起来；也可以是惊喜的短叫，不限于疼痛。',
 'a yelp of surprise 惊叫一声；let out a yelp 发出一声尖叫。',
 'yelp 通常比 howl 短；whimper 偏低弱、呜咽。它们是声音特点的差别，不是三种固定情绪。',
 ('The puppy gave a yelp when the door slammed.','门砰地关上，小狗尖叫了一声。'),('She let out a yelp of surprise when the box moved.','盒子动了一下，她惊叫出声。'),sources=S('yelp','yelp'))
W('yelps','/jelps/','尖叫〔第三人称单数〕；一声声尖叫',
 '说一只狗碰到某件事就短促尖叫，用 yelps；名词复数则把几声尖叫数出来。',
 'yelp + -s，/p/ 后读 /s/；动词三单与名词复数同形。',YELP+[['yelp + -s → yelps','它尖叫；多声尖叫']],
 'yelps in excitement 是兴奋得尖叫，a series of yelps 是接连几声短叫。具体情绪由后面的词交代。',
 'yelps with delight 开心地尖叫；sharp yelps 尖短的叫声。',
 'yells 主要说大喊，yelps 更突出一声声尖短的声音；不是 yells 的另一种拼法。',
 ('The puppy yelps with excitement when we return.','我们回来时，小狗兴奋得尖叫。'),('We heard a few yelps behind the fence.','我们听见栅栏后传来几声尖叫。'),sources=S('yelps','yelp'))
W('yelped','/jelpt/','尖叫了一声、短促地叫了',
 '某个刺激突然来到，声音一下从嘴里蹦出来，叫 yelped。叙事里常写吃惊、吃痛或兴奋那一下。',
 'yelp + 完整 -ed，/p/ 后读 /t/；仍是一个音节，不加读 /ɪd/。',YELP+[['yelp + -ed → yelped','过去发出短促尖叫']],
 'yelped in surprise 是突然惊叫，yelped for help 是用尖短叫声求助。可以接说出的简短话。',
 'yelped suddenly 突然尖叫；yelped with pain 吃痛叫了。',
 'yelped 只说明那一下怎么发声，不能单靠它判断是疼、怕还是开心；上下文才给原因。',
 ('He yelped when the cold water touched his back.','冷水碰到背上时，他尖叫了一声。'),('The puppy yelped and jumped away from the balloon.','小狗尖叫一声，从气球旁跳开。'),sources=S('yelped','yelp'))
W('yelping','/ˈjelpɪŋ/','正在短促尖叫；一阵尖叫声',
 '尖短叫声正一声接一声冒出来，是 yelping。单个 yelp 很短，yelping 可以把持续发生的整段声音写出来。',
 'yelp + 完整 -ing；末尾有 lp 两个辅音字母，直接加词尾，不双写 p。',YELP+[['yelp + -ing → yelping','进行中的尖叫；尖叫活动']],
 'a yelping puppy 是尖叫的小狗，yelping with excitement 是兴奋地叫个不停。',
 'yelping nearby 在附近尖叫；a burst of yelping 突然一阵尖叫。',
 'yelping 不保证一直保持同一个音；重点是接连的尖短叫声。howling 更常给人拖长声调的感觉。',
 ('A yelping puppy followed us across the yard.','一只尖叫着的小狗跟着我们穿过院子。'),('The sudden yelping woke everyone in the house.','突如其来的一阵尖叫吵醒了屋里所有人。'),sources=S('yelping','yelp'))
SQUEAK=[['中古英语 squeken → squeak','短、尖、细的声音；大概来自拟声，可与中古瑞典语相近词比较'],['动词 → 声音名词及比喻','吱声；勉强挤过、险些没成的感觉']]
W('squeak','/skwiːk/','吱吱叫、发出尖细声；勉强通过；一声吱响',
 '想象旧门轴“吱”一下、小老鼠尖细地叫，就是 squeak。声音细而高，不一定很响。',
 '接中古英语 squeken，大概是拟声词。现代 squeak 是完整基础词，不能按外形拆成 squeeze 的缩写。',SQUEAK,
 'the door squeaks 是门轴吱响；squeak through an exam 把“勉强挤过”的画面借给考试，指险险通过。',
 'a faint squeak 微弱的吱声；squeak past 勉强超过、通过。',
 'squeak 偏细小尖声，squeal 常让人想到拖长的尖叫；并非一个只能写物、另一个只能写人。',
 ('The door gave a squeak as I opened it.','我开门时，门吱地响了一声。'),('We managed to squeak through to the next round.','我们总算勉强进入下一轮。'),sources=S('squeak','squeak'))
W('squeaks','/skwiːks/','吱吱响〔第三人称单数〕；一声声吱响',
 '每次动一下就发出“吱”声，用 squeaks；复数名词则是几声尖细声。',
 'squeak + -s，/k/ 后读 /s/；三单与声音名词复数外形相同。',SQUEAK+[['squeak + -s → squeaks','它吱响；数声尖细响声']],
 'squeaks when opened 是打开时吱响，a few squeaks 是几声吱响。主语也能是小动物、鞋子或轮子。',
 'squeaks loudly 吱吱作响；high squeaks 尖细的吱声。',
 'squeaks 描写声音，不直接说明东西坏了；湿鞋底、玩具等也能正常发出这种声音。',
 ('This chair squeaks whenever I lean back.','我每次往后靠，这把椅子就吱响。'),('A few squeaks came from the toy in her hand.','她手里的玩具发出几声吱响。'),sources=S('squeaks','squeak'))
W('squeaked','/skwiːkt/','吱地响了、尖细地说了；勉强通过了',
 '门刚才“吱”了一声，或人紧张得声音变细，叫 squeaked；还可以说刚刚够线、勉强过关。',
 'squeak + 完整 -ed，/k/ 后读 /t/，仍是一个音节。',SQUEAK+[['squeak + -ed → squeaked','过去吱响；后来也比喻险险通过']],
 'squeaked a reply 是细声回答了，squeaked through 是险险通过；后者已经是固定的比喻用法。',
 'squeaked in surprise 惊得尖声叫了；squeaked past the finish 勉强冲过终点。',
 'squeaked through 与 passed 都能说通过，前者额外交代余地很小，差一点就没成。',
 ('The rusty gate squeaked as it swung open.','生锈的大门打开时吱地响了。'),('She squeaked through the test with one point to spare.','她只多出一分，勉强通过考试。'),sources=S('squeaked','squeak'))
W('squeaking','/ˈskwiːkɪŋ/','正在吱响、尖细叫；一阵吱响',
 '尖细的“吱、吱”声正在发生，叫 squeaking。可以把整段响声当名词，也能修饰正在响的东西。',
 'squeak + 完整 -ing，直接加词尾；ea 在基础词里表示 /iː/，不是要拆走的后缀。',SQUEAK+[['squeak + -ing → squeaking','吱响的动作、声音或状态']],
 'a squeaking wheel 是吱响的轮子，the squeaking of shoes 是鞋底摩擦发出的尖细响声。',
 'squeaking hinges 吱响的门铰链；stop squeaking 停止吱响。',
 'squeaking 强调尖细声音；creaking 更常让人想到木板、床架受力时较低、较粗的嘎吱声，实际用法会重合。',
 ('The squeaking wheel made every step of the journey noisy.','轮子一路吱响，让整段路都很吵。'),('We could hear the mice squeaking behind the wall.','我们听见墙后老鼠吱吱叫。'),sources=S('squeaking','squeak'))
SQUEAL=[['中古英语 squelen → squeal','尖叫材料；大概拟声，与古诺尔斯 skvala 等可比较'],['尖叫 → 人、动物、机器的尖声；口语告密义','从发出声音扩展到把别人的事说出去；不是每次尖叫都含告密义']]
W('squeal','/skwiːl/','尖声叫、尖厉地响；〔口语〕告密；一声尖叫',
 '像小猪尖叫、孩子开心得拉长声音叫，或刹车发出刺耳长声，叫 squeal。抓住高、尖、常有拖长感。',
 '承中古英语 squelen；大概拟声，也有联系古诺尔斯 skvala 的分析。整个词作基础，不把 -al 当这里的形容词后缀。',SQUEAL,
 'squeal with delight 是开心尖叫；squeal on someone 在口语里是告某人的密，常带说话者不赞成的语气。',
 'a squeal of excitement 兴奋的尖叫；the squeal of brakes 刹车尖响。',
 'squeal 与 squeak 都尖，squeal 常更响、更长；告密义由搭配和情境决定，听到孩子 squeal 不能往告密上套。',
 ('The children gave a squeal of delight when the puppy arrived.','小狗来了，孩子们开心得尖叫。'),('We heard the squeal of brakes outside.','我们听见外面刹车刺耳地响。'),sources=S('squeal','squeal'))
W('squeals','/skwiːlz/','尖声叫、尖厉响〔第三人称单数〕；一声声尖叫；告密',
 '小孩看到惊喜就尖声叫，或车轮转弯时刺耳地响，用 squeals；复数名词是几声尖叫。',
 'squeal + -s，/l/ 后读 /z/。动词三单、声音名词复数同形。',SQUEAL+[['squeal + -s → squeals','它尖响；他、她尖叫；多声尖叫']],
 'squeals with excitement 是兴奋地叫，squeals on his friends 才是口语里告朋友的密。',
 'squeals in delight 开心尖叫；squeals of laughter 尖声大笑。',
 'squeals 可以是喜悦，也能是害怕、疼痛；声音尖这一点相同，情绪要看后面的词。',
 ('The little girl squeals whenever the swing goes higher.','秋千荡高时，小女孩总会尖叫。'),('Their squeals of laughter echoed down the hall.','他们尖声大笑的声音在走廊里回荡。'),sources=S('squeals','squeal'))
W('squealed','/skwiːld/','尖叫了、尖厉地响了；〔口语〕告密了',
 '刚才声音突然拉高、尖利地冒出来，用 squealed。开心的喊声和受惊的叫声都可以这样写。',
 'squeal + 完整 -ed，/l/ 后读 /d/；字母 l 保留，不双写。',SQUEAL+[['squeal + -ed → squealed','过去尖叫、尖响；另有口语告密义']],
 'squealed with delight 是开心得叫了，brakes squealed 是刹车尖响；squealed on someone 是告了某人的密。',
 'squealed in surprise 惊叫了；squealed around a corner 转弯时尖响。',
 'squealed 不是所有大声说话的通称；低沉的吼声更适合 roar、bellow 等词。',
 ('She squealed with delight when she saw the tickets.','她看到门票，开心得尖叫。'),('The brakes squealed as the bus stopped.','公交车停下时，刹车发出刺耳尖响。'),sources=S('squealed','squeal'))
W('squealing','/ˈskwiːlɪŋ/','正在尖叫、尖厉地响；一阵尖叫声；告密',
 '尖叫声正持续或接连响起，是 squealing。孩子、猪、轮胎都可能成为主语，重点是听见的声音。',
 'squeal + 完整 -ing；现代变化接在整个拟声基础词后，不拆成 sque + 形容词后缀。',SQUEAL+[['squeal + -ing → squealing','进行中的尖叫、尖响；相应声音']],
 'squealing children 是尖叫的孩子，squealing tyres 是尖响的轮胎；告密义常接 on，写谁被出卖。',
 'squealing with joy 开心地尖叫；the squealing of brakes 刹车尖响。',
 'squealing 偏尖厉声；screeching 常更突出摩擦般的刺耳感，边界不是严格的声音测量标准。',
 ('The squealing children ran towards the ice cream van.','尖叫着的孩子们向冰激凌车跑去。'),('The squealing of the brakes made us turn around.','刹车的尖响让我们转过头。'),sources=S('squealing','squeal'))
SHRIEK=[['中古英语 scrycke、skriken 等及北欧叫喊材料 → shriek','尖厉叫声；相关形式最后大概可追到拟声'],['现代 shriek 动词、名词','尖锐叫出声；一声尖叫；也可写鸟鸣、机器尖响']]
W('shriek','/ʃriːk/','尖叫、尖声喊；一声尖叫',
 '声音一下冲到又高又尖的位置，像受惊时“啊”地叫出来，就是 shriek。害怕、疼痛和狂喜都能这样叫。',
 '现代形式接较早 shrick、shreke 一系，联系中古英语 scrycke、skriken 和北欧叫喊词。不是 sh- 加一个可独立解释的 riek。',SHRIEK,
 'let out a shriek 是发出尖叫，shriek with laughter 是尖声大笑；词本身不把原因限定为恐惧。',
 'a shriek of surprise 惊叫；shriek for help 尖声呼救。',
 'shriek 和 scream 都能译尖叫；shriek 常给人更尖、猛然冲出的感觉，实际使用有大量重合。',
 ('She let out a shriek when the spider dropped onto her sleeve.','蜘蛛掉到袖子上时，她尖叫了一声。'),('We heard the children shriek with laughter upstairs.','我们听见楼上孩子们尖声大笑。'),sources=S('shriek','shriek'))
W('shrieks','/ʃriːks/','尖声叫喊〔第三人称单数〕；一声声尖叫',
 '说某个人会突然尖叫，用 shrieks；a few shrieks 则是把几声尖叫当声音事件来数。',
 'shriek + -s，/k/ 后读 /s/。名词复数与动词三单用同一形式。',SHRIEK+[['shriek + -s → shrieks','他、她尖叫；多声尖叫']],
 'shrieks with laughter 是尖声笑，shrieks of delight 是开心的尖叫；不能只按字典的恐惧例子理解。',
 'shrieks loudly 高声尖叫；distant shrieks 远处的尖叫声。',
 'shrieks 主要交代尖利的声音，sobs 则突出抽泣；一个是尖声叫，一个是哭得断续抽气。',
 ('She shrieks with laughter whenever her brother tells that story.','弟弟每次讲那个故事，她都会尖声大笑。'),('We heard excited shrieks from the playground.','我们听见游乐场传来兴奋的尖叫。'),sources=S('shrieks','shriek'))
W('shrieked','/ʃriːkt/','尖叫了、尖声喊了',
 '刚才声音猛地变得尖利、冲口叫出来，叫 shrieked。小说常在一句喊话后用它，让人听见人物的声音。',
 'shriek + 完整 -ed，/k/ 后读 /t/；只有一个音节，不另加 /ɪd/。',SHRIEK+[['shriek + -ed → shrieked','过去尖声叫喊']],
 'shrieked a warning 是尖声警告了，shrieked with joy 是欣喜尖叫。可以直接接人物说的话。',
 'shrieked in terror 惊恐尖叫；shrieked for help 尖声呼救了。',
 'shrieked 描写声音尖，shouted 主要描写声音响；尖叫能兼有两者，但普通大喊不一定尖利。',
 ('“Watch out!” she shrieked as the ball flew towards us.','球朝我们飞来时，她尖声喊：“小心！”'),('The children shrieked with joy as the ride began.','游乐设施启动时，孩子们欣喜地尖叫。'),sources=S('shrieked','shriek'))
W('shrieking','/ˈʃriːkɪŋ/','正在尖叫；尖声的；一阵尖叫',
 '尖叫正在发生，或一群人的尖声接连响起，是 shrieking。也可以用来修饰刺耳的风声、机器声。',
 'shriek + 完整 -ing，直接相接；不是不规则变化。',SHRIEK+[['shriek + -ing → shrieking','尖叫过程；发尖声的状态']],
 'shrieking with laughter 是笑得尖叫，shrieking children 是尖叫的孩子；the shrieking of birds 是鸟儿尖鸣。',
 'shrieking in excitement 兴奋尖叫；a shrieking wind 尖啸的风。',
 'shrieking 可以是欢乐场景；中文译成“惨叫”前，要先看是否真有痛苦或恐惧。',
 ('The children were shrieking with laughter in the next room.','孩子们在隔壁房间笑得尖叫。'),('The shrieking of birds broke the morning silence.','鸟儿尖利的鸣叫打破清晨的寂静。'),sources=S('shrieking','shriek'))
SCREECH=[['中古英语 schrichen、较早 scritch 等 → screech','相关尖叫材料的形式变化；更远大概拟声'],['现代动词、名词','人、鸟的尖叫；轮胎、门轴等刺耳尖响']]
W('screech','/skriːtʃ/','刺耳地尖叫、尖响；刺耳尖声',
 '像急刹车时轮胎那一声刺耳长响，或人扯高嗓子的尖叫，就是 screech。重点是尖得扎耳朵。',
 '现代 screech 是较早 scritch 一类形式的变化，接中古英语尖叫材料；与 shriek 可比较，但不是把现代 shriek 按规则改几个字母。',SCREECH,
 'screech to a halt 是伴着刺耳声停住，a screech of brakes 是刹车尖响。主语可以是人、鸟或机器。',
 'a piercing screech 刺耳尖响；screech at someone 尖声冲某人叫。',
 'screech 常突出声音难听、刺耳；shout 只说喊得响。不能把所有提高音量的说话都叫 screech。',
 ('A sudden screech of brakes made everyone look up.','刹车突然刺耳一响，大家都抬头看。'),('We heard the birds screech in the trees.','我们听见鸟儿在树上尖叫。'),sources=S('screech','screech'))
W('screeches','/ˈskriːtʃɪz/','刺耳尖叫、尖响〔第三人称单数〕；一声声刺耳尖声',
 '说旧机器一动就刺耳地响，用 screeches；复数名词则指接连几声尖响。',
 'screech + -es，/tʃ/ 后读 /ɪz/，因此多一个音节；三单与复数共用这一形式。',SCREECH+[['screech + -es → screeches','它刺耳尖响；多声尖响']],
 'screeches when it starts 是启动时尖响，the screeches of seabirds 是海鸟一声声尖叫。',
 'screeches loudly 刺耳大叫；high screeches 尖高的响声。',
 'screeches 的结尾是 /tʃɪz/，screeching 是 /tʃɪŋ/；前者可以数声音，后者常把声音过程整体说出来。',
 ('The old machine screeches when it starts.','这台旧机器启动时刺耳地响。'),('The screeches of seabirds filled the harbour.','港口里满是海鸟的尖叫声。'),sources=S('screeches','screech'))
W('screeched','/skriːtʃt/','刺耳地尖叫了、尖响了；尖响着停住了',
 '轮胎刚才尖响着急停，或一个人尖厉地喊了一句，用 screeched。这个词让读者听到声音的刺耳感。',
 'screech + 完整 -ed；清音 /tʃ/ 后接 /t/，读 /tʃt/，不是 /tʃɪd/。',SCREECH+[['screech + -ed → screeched','过去刺耳叫喊、尖响']],
 'screeched to a halt 是尖响着停下，screeched a warning 是尖声发出警告；前者不必真指人喊。',
 'screeched around a corner 转角时刺耳尖响；screeched in alarm 惊慌尖叫。',
 'screeched to a halt 把声音和停车放在一起；came to a halt 只说停下，不交代声音。',
 ('The car screeched to a halt beside the crossing.','汽车在路口旁尖响着停住。'),('“Get away from there!” she screeched.','“离那儿远点！”她尖声喊。'),sources=S('screeched','screech'))
W('screeching','/ˈskriːtʃɪŋ/','正在刺耳尖叫、尖响；刺耳的尖声',
 '耳边正响着尖厉、像摩擦出来的声音，叫 screeching。既能写进行中的动作，也能形容吵人的声音。',
 'screech + 完整 -ing，直接加；ch 保持 /tʃ/，没有去字母或双写变化。',SCREECH+[['screech + -ing → screeching','刺耳尖响的过程、状态']],
 'screeching tyres 是尖响的轮胎，screeching birds 是尖叫的鸟；the screeching of metal 是金属摩擦尖响。',
 'screeching brakes 尖响的刹车；stop screeching 别再尖声叫。',
 'screeching 与 squealing 有重合；screeching 往往更突出扎耳的摩擦感，具体选词也受习惯搭配影响。',
 ('The screeching tyres left dark marks on the road.','尖响的轮胎在路上留下黑色印痕。'),('We covered our ears against the screeching of the metal gate.','金属大门尖响，我们捂住了耳朵。'),sources=S('screeching','screech'))
BAWL=[['中古英语 baulen → bawl','与古诺尔斯 baula、或中世纪拉丁 baulare 的动物叫声材料有关；借入路线有不同分析'],['动物叫喊 → 人放声喊、嚎啕哭','声音放开、响而不收着；bawl someone out 又指大声训斥']]
W('bawl','/bɔːl/','放声大喊；嚎啕哭；〔bawl someone out〕大声训斥',
 '不压着嗓子，张口就大声喊或大哭，叫 bawl。比普通 cry 更容易让人听见响亮、放开的哭声。',
 '接中古英语 baulen；有古诺尔斯 baula 与中世纪拉丁 baulare 等来源分析，相关材料模仿动物叫声。不能把不同候选硬排成一条借入链。',BAWL,
 'bawl for his mother 是哭喊着找妈妈，bawl someone out 是大声训斥某人；后者常见于美式口语。',
 'bawl loudly 放声哭喊；bawl your eyes out 嚎啕大哭。',
 'bawl 与 ball 常同音，意思、来源分开。看到 bawl someone out，重点是训斥，不是把某人哭出去。',
 ('The baby began to bawl when the lights went out.','灯灭时，婴儿开始放声大哭。'),('There is no need to bawl at me; I can hear you.','不用冲我大喊，我听得见。'),sources=S('bawl','bawl'))
W('bawls','/bɔːlz/','放声哭喊、大喊〔第三人称单数〕',
 '一个人一不顺心就放声哭，或隔着一段距离大喊，用 bawls。抓住声音完全放开的感觉。',
 'bawl + -s，/l/ 后读 /z/；现代三单直接接在整个基础词后。',BAWL+[['bawl + -s → bawls','他、她放声哭喊']],
 'bawls for food 是哭喊着要吃的，bawls out instructions 是大声喊出指令。bawls someone out 才是训斥某人。',
 'bawls at someone 冲某人大喊；bawls for help 大声呼救。',
 'bawls 不一定在流泪；它也能只表示大声喊。要看是在哄孩子、叫远处的人，还是训话。',
 ('The baby bawls whenever he drops his toy.','婴儿每次掉了玩具就放声哭。'),('The coach bawls instructions from the touchline.','教练在边线旁大声喊指令。'),sources=S('bawls','bawl'))
W('bawled','/bɔːld/','放声哭喊了、大喊了；大声训斥了',
 '刚才一个人不收着声音地哭喊，叫 bawled；接 someone out 时，写的是把某人狠狠训了一顿。',
 'bawl + 完整 -ed，/l/ 后读 /d/。不因与 ball 同音就改用 ball 的拼写。',BAWL+[['bawl + -ed → bawled','过去放声哭喊、训斥']],
 'bawled for her mother 是哭喊着找妈妈；bawled him out 是大声训斥他，out 要与整个搭配一起理解。',
 'bawled all night 整夜放声哭；bawled a warning 大声喊出警告。',
 'bawled 是声音放开的喊或哭，sobbed 更突出一抽一抽、断断续续的哭法，两者有时同时发生。',
 ('The child bawled for her mother until she returned.','孩子一直哭喊着找妈妈，直到她回来。'),('He bawled across the yard to get our attention.','他隔着院子大喊，想引起我们的注意。'),sources=S('bawled','bawl'))
W('bawling','/ˈbɔːlɪŋ/','正在放声哭喊；一阵嚎啕哭声、大喊声',
 '哭声或喊声正放开响着，是 bawling。它把那种又响又不收敛的发声过程直接摆到耳边。',
 'bawl + 完整 -ing，直接加；基础词末尾有 wl，不需要双写 l。',BAWL+[['bawl + -ing → bawling','进行中的放声哭喊']],
 'a bawling baby 是放声大哭的婴儿，bawling out orders 是大声发号施令；bawling someone out 是训斥某人。',
 'bawling loudly 放声哭喊；stop bawling 别再大哭、大喊。',
 'bawling 与 bowling 在许多口音里元音不同：前者 /ɔː/，后者 /əʊ/ 或 /oʊ/；一个哭喊，一个保龄球活动。',
 ('A bawling baby kept the passengers awake.','一个放声大哭的婴儿让乘客们睡不着。'),('He was bawling orders through a loudspeaker.','他正用扩音器大声喊命令。'),sources=S('bawling','bawl'))
SNARL=[['声音支线：较早 snar 等低吼材料 → snarl','或与荷兰语、低地德语相近拟声词有关；露齿低吼，再到人恶声说话'],['缠结支线：中古英语 snarl、snarlen 与 snare 材料相连','套索、缠结 → 线结；使交通、事情堵塞纠缠；不从狗吼推导']]
W('snarl','英 /snɑːl/；美 /snɑːrl/','龇牙低吼、恶声说；缠结、堵塞；低吼声、乱结',
 '看狗时，是龇牙发出带威胁的低吼；看头发、绳子或交通时，是缠在一起、乱成一团。同形的两条线要分开记。',
 '声音支线联系较早 snar 和拟声材料；缠结支线联系中古英语 snarl、snarlen 与 snare 套索材料，有小称或反复动作形式的分析。',SNARL,
 'snarl at someone 是恶声冲某人说，snarl up traffic 是把交通堵住，a snarl in her hair 是头发里的乱结。',
 'a threatening snarl 威胁的低吼；a traffic snarl 交通拥堵。',
 'growl 可以只是低沉吼声；动物 snarl 常带龇牙、威胁的样子。traffic snarl 走缠结线，不是汽车在低吼。',
 ('The dog gave a snarl when the stranger reached towards it.','陌生人伸手过来，狗龇牙低吼。'),('“Leave me alone,” he said with a snarl.','“别烦我。”他恶声恶气地说。'),('There was a stubborn snarl in her hair.','她的头发里有个很难解开的结。'),('The roadworks caused a traffic snarl near the bridge.','道路施工让桥附近堵成一团。'),sources=S('snarl','snarl'))
W('snarls','英 /snɑːlz/；美 /snɑːrlz/','低吼、恶声说〔第三人称单数〕；缠乱、堵塞；低吼声、乱结〔复数〕',
 '狗一边露牙一边低吼，用 snarls；绳子或交通缠乱也能用，但走的是另一条来源。',
 '两条基础词 snarl 都可加 -s，/l/ 后读 /z/；对应三单或名词复数，靠上下文分支。',SNARL+[['snarl + -s → snarls','它低吼、缠结；多声低吼、多个乱结']],
 'snarls at visitors 是冲来客龇牙低吼，snarls up traffic 是堵住交通；tangles、knots 可以帮助理解乱结名词义。',
 'angry snarls 愤怒的低吼；snarls in the rope 绳子里的乱结。',
 'snarls 不把所有义都连成“生气”：绳结没有情绪，乱结义来自套索、缠结材料。',
 ('The dog snarls whenever anyone touches its food.','只要有人碰食物，那只狗就龇牙低吼。'),('She carefully removed the snarls from the fishing line.','她小心地解开鱼线里的乱结。'),sources=S('snarls','snarl'))
W('snarled','英 /snɑːld/；美 /snɑːrld/','龇牙低吼了、恶声说了；缠结的、堵塞的',
 '人刚才带着敌意说话，叫 snarled；线或道路变得纠缠、堵住，也会用这个形式。先看说的是声音还是缠结。',
 'snarl + 完整 -ed，/l/ 后读 /d/。声音、缠结两条动词都按同一现代规则变化。',SNARL+[['snarl + -ed → snarled','过去低吼、恶声说；已缠结、堵塞']],
 'snarled a reply 是恶声回答了，snarled traffic 是堵塞的交通；snarled up in 是缠在、困在某事里。',
 'snarled at him 冲他低吼、恶声说；snarled cables 缠乱的电缆。',
 'snarled traffic 中的 snarled 像 tangled，写堵乱的状态；它不表示交通在发怒。',
 ('“That is none of your business,” he snarled.','“那不关你的事。”他恶声说。'),('The crash left traffic snarled for hours.','事故让交通堵了好几个小时。'),sources=S('snarled','snarl'))
W('snarling','英 /ˈsnɑːlɪŋ/；美 /ˈsnɑːrlɪŋ/','正在低吼、恶声说；正在缠结、造成堵塞的',
 '一只狗露着牙正低吼，是 snarling；某件事正把道路或进展搅成一团，也可用这个词，但属于缠结支线。',
 'snarl + 完整 -ing，直接加；两条动词都能形成这个分词，不能只背一个中文义。',SNARL+[['snarl + -ing → snarling','低吼、恶声说话中；缠乱、堵塞中']],
 'a snarling dog 是龇牙低吼的狗，snarling up traffic 是正在造成交通堵塞；前后走不同的近源。',
 'snarling at each other 相互恶声说话；snarling traffic 堵乱交通。',
 'snarling 可以描述人说话的敌意；在 traffic、cables 等搭配中，要转到套索、乱结的画面。',
 ('A snarling dog blocked the narrow path.','一只龇牙低吼的狗挡住了小路。'),('The broken traffic lights were snarling up traffic.','坏掉的红绿灯正让交通堵成一团。'),sources=S('snarling','snarl'))
SCREAM=[['较早 scræmen、scremen 等 → 中古英语 scremen → scream','尖厉叫声；可与北欧、荷兰语、德语材料比较，具体更远来源不确定'],['动词及声音名词 → 形容强烈传达','人尖叫、机器尖鸣；后来还可说某种迹象特别明显']]
W('scream','/skriːm/','尖叫、惊叫；尖声说；一声尖叫；强烈显出',
 '声音冲得又高又响，像害怕、兴奋或疼痛时放声叫，就是 scream。也能写机器尖鸣，或某种特征明显得像在大声告诉你。',
 '接较早 scræmen、scremen 一系形式；与北欧、荷兰语等叫喊词的借入、同源关系有不同分析。现代 scream 整体作基础词。',SCREAM,
 'scream for help 是尖声呼救，scream with delight 是开心尖叫；the design screams luxury 是设计处处透出奢华感。',
 'let out a scream 发出尖叫；scream at someone 冲某人尖声吼。',
 'scream 不等于总在害怕。cry 还常指流泪哭泣，scream 则先抓声音尖、响；人可以尖叫却不哭。',
 ('The children began to scream with delight as the ride started.','游乐设施启动时，孩子们开心得尖叫。'),('She heard a scream from the house next door.','她听见隔壁房子传来一声尖叫。'),sources=S('scream','scream'))
W('screams','/skriːmz/','尖叫、尖鸣〔第三人称单数〕；一声声尖叫；强烈显出',
 '某人遇到惊喜就尖声叫，用 screams；复数名词指多声尖叫。比喻用法则是某种特征特别显眼。',
 'scream + -s，/m/ 后读 /z/；动词三单、名词复数外形相同。',SCREAM+[['scream + -s → screams','他、她尖叫；多声尖叫；明显表露']],
 'screams with laughter 是笑得尖叫，screams of joy 是欢乐的尖叫；screams success 可比喻处处显出成功的气派。',
 'screams for help 尖声呼救；distant screams 远处的尖叫。',
 'screams 在比喻中不一定真有声音，如 a room that screams luxury 说房间的样子很显奢华。',
 ('She screams with laughter at that part of the film.','看到电影那个片段，她笑得尖叫。'),('Their screams of joy could be heard from the street.','街上都能听见他们欢乐的尖叫。'),sources=S('screams','scream'))
W('screamed','/skriːmd/','尖叫了、尖声喊了；尖鸣了；强烈显出了',
 '刚才情绪一下冲上来、声音又高又响，叫 screamed。它也能把金属、引擎发出的尖厉声写得像叫喊。',
 'scream + 完整 -ed，/m/ 后读 /d/；ea 的 /iː/ 保留，不能照 speak → spoke 那样换元音。',SCREAM+[['scream + -ed → screamed','过去尖叫、尖鸣或强烈传达']],
 'screamed for help 是尖声呼救了，screamed a warning 是尖声喊出警告；可以接引号里的喊话。',
 'screamed with excitement 兴奋尖叫；screamed in pain 痛得尖叫。',
 'screamed 比 said 多了强烈的声音信息；与 shouted 相比，常更突出尖、高或情绪激烈。',
 ('“We won!” she screamed into the phone.','“我们赢了！”她对着电话尖叫。'),('He screamed for help from the upstairs window.','他从楼上的窗口尖声呼救。'),sources=S('screamed','scream'))
W('screaming','/ˈskriːmɪŋ/','正在尖叫、尖鸣；尖厉的；极明显的',
 '尖叫正持续着，叫 screaming；形容标题、颜色或差错时，也可说它醒目得像在大喊。',
 'scream + 完整 -ing，直接加；既能表示进行动作，也能在修饰语里保留“强烈扑面而来”的感觉。',SCREAM+[['scream + -ing → screaming','尖叫过程、尖厉状态；后来的醒目、强烈义']],
 'screaming fans 是尖叫的粉丝，screaming headlines 是耸动、醒目的标题；不是标题真的会发声。',
 'screaming with laughter 尖声大笑；a screaming engine 尖鸣的引擎。',
 'screaming 不能一律译成“惨叫”：欢呼时可译尖叫，标题中可译醒目、耸动，先看具体画面。',
 ('The screaming fans crowded around the entrance.','尖叫着的粉丝挤在入口周围。'),('The story appeared beneath a screaming headline.','这篇报道上面配着一个耸动的大标题。'),sources=S('screaming','scream'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zey',ROOTS,WORDS)
 extend_lessons()
