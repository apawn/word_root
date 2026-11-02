"""Everyday actions: watches, studied, eating, sleeping and common finite verbs."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3373':dict(words=['watch','watches'],label='watch → watches：持续观察；一只只表',note='watch 名词、动词接早期清醒、守望词族，watches 在 /tʃ/ 后增加 /ɪz/。'),
 'C1440':dict(words=['study','studied'],label='study → studied：学过、研究过；经过斟酌的',note='study 变 y 为 i 加 ed，但原词结尾是元音，过去词尾读 /d/，不是多加一个 /ɪd/ 音节。'),
 'B2854':dict(words=['eat','eating'],label='eat → eating：进食、耗用与用餐用途',note='eat 继承古英语 etan，eating 直接加 -ing；过去 ate、分词 eaten 已另讲。'),
 'B2954':dict(words=['sleep','sleeping'],label='sleep → sleeping：睡眠状态与睡觉用途',note='sleeping 直接加 -ing，sleep 本族名词、动词都有古老历史；与过去形式 slept 分开。'),
 'B2882':dict(words=['keep','keeps'],label='keep → keeps：保持、保留与继续',note='keep 接古英语 cēpan 看顾、守护等，keeps 后可接保留的对象或继续做的动作。'),
 'B2591':dict(words=['see','sees'],label='see → sees：看见、理解与见面',note='see 继承古英语 sēon，sees 是现在第三人称，saw／seen 是不同历史屈折形式。'),
 'B2740':dict(words=['hear','hears'],label='hear → hears：听见、听说与审听',note='hear 接古英语 hīeran、hēran 等，hears 与 heard 的元音不相同。'),
 'B3000':dict(words=['tell','tells'],label='tell → tells：告诉、讲述与辨别',note='tell 的早期计数、讲述义相连，tells 后的对象和小词决定告诉内容、区分或显出信息。'),
 'B2539':dict(words=['ask','asks'],label='ask → asks：提问、请求与要求',note='asks 的结尾 /sks/ 是连在一起的辅音，通常不另添元音；ask 的询问、请求语法结构要分开。'),
}
W('watches','英 /ˈwɒtʃɪz/；美 /ˈwɑːtʃɪz/','手表、计时表；值班、守望；观看、留意〔watch 的第三人称单数〕',
 '持续盯着变化看，是 watches 的动词用法；能计时、提醒人的一只只表，则是名词复数。两个分支有清醒、守望的历史联系。',
 'watch + -es，/tʃ/ 后增加 /ɪz/。动词接古英语 wæċċan，名词有 wæċċe 等，计时器义早期关联叫醒睡者的钟，后来扩展到便携表。',
 [['古英语清醒、守望词族 → watch 名词、动词','守望；后来有计时器、表等义'],['watch + -es → watches','多只表；单数主语持续观察等']],
 'watches TV 看电视；watches the children 照看孩子；digital watches 电子表；keeps watches on display 展示一只只表。',
 'watches carefully；watches in the shop。','He watches the clock 中 watches 是动词，The watches are on the shelf 中是复数名词。watch 表和 clock 钟的区分按具体设备、用法看，日常 watch 常说腕表、怀表等便携表。',
 ('She watches the birds from the kitchen window.','她从厨房窗户看鸟。'),('The shop repairs old watches as well as modern ones.','这家店既修老式表，也修现代表。'),sources=['https://en.wiktionary.org/wiki/watches#English','https://en.wiktionary.org/wiki/watch#English'])
W('studied','/ˈstʌdid/','学习、研究过；仔细查看过；经过考虑、刻意作出的；study 的过去式和过去分词等',
 '把精力放进去认真看、学过，是 studied；一个动作经过事先考虑、刻意控制，也可以被形容为 studied。',
 'study 的 y 变 i，再加 -ed，读 /ˈstʌdid/。原词末尾 /i/ 保留，过去词尾只加 /d/，不增加第三个音节。study 经法语接拉丁 studium、studēre 的专注词族。',
 [['拉丁专注词族 → 法语相关形式 → study','用心投入 → 学习、仔细研究'],['study 变 y 为 i + -ed → studied','过去学、研究；刻意斟酌后的']],
 'studied history 学过历史；studied the map 仔细看过地图；a studied response 经过考虑的回应；studied indifference 刻意装出的漠不关心。',
 'carefully studied；has studied the subject。','studied 不必说正式在学校上课，也能说仔细看。studied indifference 中是形容词，重点是看起来不在乎的样子经过控制、安排。',
 ('She studied the photograph before answering.','她仔细看了照片，才回答。'),('He gave a studied response rather than answering immediately.','他没有立即回答，而是经过斟酌后作了回应。'),sources=['https://en.wiktionary.org/wiki/studied#English','https://en.wiktionary.org/wiki/study#English'])
W('eating','/ˈiːtɪŋ/','正在吃；进食；消耗、侵蚀〔引申〕；eat 的 -ing 形式',
 '把食物吃进去，是 eating；时间、费用一点点占掉资源，也可以借吃掉的感觉来理解。',
 'eat + -ing，直接加，保留 /iːt/。eat 继承古英语 etan，现代进行形式规则，过去 ate、分词 eaten 则是不规则形式。',
 [['古英语 etan → eat','吃、进食'],['eat + -ing → eating','进行中的吃；消耗、侵蚀等比喻']],
 'eating dinner 吃晚饭；eating out 在外面吃饭；eating habits 饮食习惯；eating into our time 占用了我们的时间。',
 'enjoy eating；eating with friends。','eating a meal 说吃饭动作，eating habits 用来说明和进食有关的习惯。eat into 常说逐渐消耗、侵占资源，具体看后面的时间、空间等对象。',
 ('We were eating dinner when the lights went out.','停电时，我们正在吃晚饭。'),('The long journey was eating into our time at the museum.','路程太长，挤占了我们参观博物馆的时间。'),sources=['https://en.wiktionary.org/wiki/eating#English','https://en.wiktionary.org/wiki/eat#English'])
W('sleeping','/ˈsliːpɪŋ/','正在睡觉；睡眠；供睡觉用的',
 '人进入睡眠，是 sleeping；放到物品前面，也常表示这个东西是睡觉时用的。',
 'sleep + -ing。sleep 的名词和动词都继承自古英语本族词，sleeping 是常见 -ing 形式；过去式 slept 则保留不规则变化。',
 [['古英语睡眠词族 → sleep','睡觉；睡眠'],['sleep + -ing → sleeping','正在睡；睡眠活动；睡觉用途']],
 'a sleeping child 睡着的孩子；a sleeping bag 睡袋；sleeping well 睡得好。把睡眠状态和用品用途分开理解。',
 'have trouble sleeping；sleeping on the sofa。','asleep 多接在 be、fall 后说明状态，如 is asleep；sleeping 既能参与进行时，也能放在名词前。',
 ('The baby is sleeping in the next room.','婴儿正在隔壁房间睡觉。'),('We packed two sleeping bags for the trip.','我们为旅行装好了两个睡袋。'),sources=['https://en.wiktionary.org/wiki/sleeping#English','https://en.wiktionary.org/wiki/sleep#English'])
W('keeps','/kiːps/','保留；保持；继续；遵守；keep 的第三人称单数',
 '让东西留住、让状态维持下去，是 keeps 的共同画面：留下钥匙、保持温暖、不断提问，都围绕继续保持。',
 'keep + -s，/p/ 后词尾读 /s/。keep 接古英语 cēpan 的看顾、守护等义，后来广泛用于保有、维持；过去形式是 kept。',
 [['古英语 cēpan → keep','看顾、守护 → 保留、维持'],['keep + -s → keeps','单数主语保留、保持或继续']],
 'keeps a diary 记日记；keeps warm 保持暖和；keeps asking 不断问；keeps a promise 信守承诺。',
 'keeps the door open；keeps in touch。','keeps doing 表示继续做或反复做；keeps someone waiting 表示让某人一直等。keeps to a plan 表示遵循计划，小词会改变后面的连接方式。',
 ('She keeps a spare key in her desk.','她在书桌里留了一把备用钥匙。'),('The dog keeps looking at the kitchen door.','那只狗不停地望向厨房门。'),sources=['https://en.wiktionary.org/wiki/keeps#English','https://en.wiktionary.org/wiki/keep#English'])
W('sees','/siːz/','看见；理解；见面；看待；see 的第三人称单数',
 '眼睛接收到画面是 sees；脑子看明白一件事，也沿用这个“看见”的感觉。',
 'see + -s，词尾在元音后读 /z/。see 继承古英语 sēon 的看见义；现在 sees、过去 saw、过去分词 seen 要分别认。',
 [['古英语 sēon → see','看见、察觉'],['see + -s → sees','单数主语看见、明白或会见']],
 'sees the problem 看出了问题；sees a friend 见朋友；sees it differently 对此看法不同；sees a doctor 看医生。',
 'sees clearly；sees someone as a partner。','sees 常侧重看到了、意识到了；looks at 说把目光投过去，watches 常说持续留意。sees someone as ... 是把某人看作……。',
 ('She sees a light at the end of the street.','她看见街道尽头有一盏灯。'),('He sees the delay as a chance to improve the design.','他把这次延误看作改进设计的机会。'),sources=['https://en.wiktionary.org/wiki/sees#English','https://en.wiktionary.org/wiki/see#English'])
W('hears','英 /hɪəz/；美 /hɪrz/','听见；听说；听取、审理；hear 的第三人称单数',
 '声音传到耳朵里是 hears；消息传到自己这里，或者正式听取别人的陈述，也由此展开。',
 'hear + -s，词尾读 /z/。hear 接古英语 hīeran、hēran 等听觉形式；heard 的元音发生变化，不能照 hears 去读过去式。',
 [['古英语 hīeran、hēran 等 → hear','听见、听取'],['hear + -s → hears','单数主语听见、获知、听取']],
 'hears a noise 听见声音；hears from a friend 收到朋友消息；hears about a change 听说变化；hears a case 审理案件。',
 'hears someone singing；hears the news。','hear from 看消息来自谁，hear about 看听说什么。listen to 强调主动听的动作，hears 常说声音或消息已经被接收到。',
 ('She hears music coming from the open window.','她听见音乐从敞开的窗户里传出来。'),('He rarely hears from his old classmates.','他很少收到老同学的消息。'),sources=['https://en.wiktionary.org/wiki/hears#English','https://en.wiktionary.org/wiki/hear#English'])
W('tells','/telz/','告诉；讲述；吩咐；辨别；显露；tell 的第三人称单数',
 '把事情一项项讲出来，是 tells；看出线索、分清差别，也可以用 tell。',
 'tell + -s，/l/ 后读 /z/。tell 接古英语 tellan，早期有数、列举、讲述等义；计数和叙述共享逐项交代的联系。过去式为 told。',
 [['古英语 tellan → tell','数、列举；讲述'],['tell + -s → tells','告诉、讲述；分辨、显示信息']],
 'tells a story 讲故事；tells me the truth 告诉我实情；tells us to wait 叫我们等；tells them apart 分清它们。',
 'tells you something；tells the difference。','tell 常直接接听话的人：tells me。say 通常先接说出的内容；对某人说则常用 says to me。can tell 表示能判断、看得出来。',
 ('My grandfather tells the same story every winter.','我祖父每年冬天都会讲那个故事。'),('The label tells you which side should face up.','标签会告诉你哪一面应该朝上。'),sources=['https://en.wiktionary.org/wiki/tells#English','https://en.wiktionary.org/wiki/tell#English'])
W('asks','英 /ɑːsks/；美 /æsks/','询问；请求；要求；ask 的第三人称单数',
 '把一个问题或一个需要交给别人，希望得到回答或帮助，就是 asks。',
 'ask + -s，形成词尾 /sks/，通常不在中间另添元音。ask 接古英语 āscian，经中古英语 asken 等进入现代形式。',
 [['古英语 āscian → 中古英语 asken 等 → ask','问、请求'],['ask + -s → asks','单数主语提问或提出请求']],
 'asks a question 提问；asks for help 求助；asks me to stay 请我留下；asks about the trip 问起旅行。',
 'asks politely；asks whether it is ready。','ask someone something 是问某人某事；ask someone for something 是向某人要某物；ask someone to do something 是请或要求某人做事。',
 ('She asks a question whenever the instructions are unclear.','只要说明不清楚，她就会提问。'),('He asks everyone to leave their shoes by the door.','他请大家把鞋放在门边。'),sources=['https://en.wiktionary.org/wiki/asks#English','https://en.wiktionary.org/wiki/ask#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xi',ROOTS,WORDS)
 extend_lessons()
