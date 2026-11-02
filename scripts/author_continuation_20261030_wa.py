"""Everyday past forms: requests, work, play and changes."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2539':dict(words=['ask','asked'],label='ask → asked：问过、请求过',note='asked 的 -ed 读 /t/；asked someone to do 是请某人做，asked if 是问是否。'),
 'B2504':dict(words=['work','worked'],label='work → worked：工作过；起作用了',note='worked 的 -ed 读 /t/；work 的过去式不只说工作，也常说办法奏效、设备可用。'),
 'B3108':dict(words=['play','played'],label='play → played：玩过、演奏过、扮演过',note='played 的词尾读 /d/，与 paid /peɪd/ 的词首不同；具体动作看宾语和搭配。'),
 'B3174':dict(words=['start','started'],label='start → started：开始、启动了',note='start 原有突然跃起的动作义；started 的词尾增加 /ɪd/ 一个音节。'),
 'B2761':dict(words=['look','looked'],label='look → looked：看过；当时看起来',note='looked 词尾读 /t/；looked tired 是当时显得累，looked at 是把视线投向。'),
 'C1526':dict(words=['turn','turned'],label='turn → turned：转动、转向、变成了',note='turn 的车削、旋转画面扩展到方向与状态变化；turned 的 -ed 读 /d/。'),
 'B3018':dict(words=['change','changed'],label='change → changed：换了；变了',note='change 去末尾 e，加完整 -ed；/dʒ/ 后的过去词尾读 /d/，整词一个音节。'),
 'B3929':dict(words=['consider','considered'],label='consider → considered：考虑过；被认为',note='considered 可说经过思考，也可在 be considered 中引出判断；更深的星辰词源联系有讨论。'),
 'C0168':dict(words=['receive','received'],label='receive → received：收到了；受到',note='received 的 -ed 读 /d/；邮件、帮助、欢迎和信号都能被接收。'),
 'B2502':dict(words=['add','added'],label='add → added：加上了；补充说',note='added 的 -ed 在 /d/ 后读 /ɪd/；英语 add 保留拉丁 addere 加上的词源。'),
}
W('asked','英 /ɑːskt/；美 /æskt/','问了；请求、要求过；ask 的过去式和过去分词',
 '把问题或请求递给对方，事情发生过，就用 asked。问了，不代表对方已经回答；请了，也不代表事情已经做完。',
 'ask + -ed；/k/ 后 -ed 读 /t/，结尾连成 /skt/，标准慢读也不添一个 /ɪd/ 音节。ask 接古英语 āscian 的询问、请求词族。',
 [['古英语 āscian → ask','询问、请求'],['ask + -ed → asked','过去问、请求；也可用于完成时、被动语态']],
 'asked a question 问了个问题；asked for help 请求帮助；asked me to wait 请我等一等；asked whether ... 问是否……。asked for it 还可按语境说自找某个结果。',
 'asked about the schedule；was asked to help。','He asked me to leave 是他叫我离开；He asked if I had left 是问我是否已经离开。to 后是请求的动作，if 后是询问的内容。',
 ('I asked the driver where to get off.','我问司机该在哪儿下车。'),('We were asked to bring our own lunch.','对方请我们自带午饭。'),sources=['https://en.wiktionary.org/wiki/asked#English','https://en.wiktionary.org/wiki/ask#English'])
W('worked','英 /wɜːkt/；美 /wɜːrkt/','工作过；运作过；奏效了；work 的过去式和过去分词',
 '人把活干了，设备运转了，办法产生效果了，都可以说 worked。先看是谁或什么在 work，才能知道是哪种意思。',
 'work + -ed；/k/ 后读 /t/。work 的劳动、制作词族继承古英语 weorc 名词和 wyrcan 等动词，现代动词再按规则变化。',
 [['古英语工作、制作词族 → work','劳动；做出成果；运转、起作用'],['work + -ed → worked','过去的工作、运作或奏效']],
 'worked for a company 为公司工作过；worked on a design 做过某个设计；the key worked 钥匙能用；worked out a solution 想出了解决办法。',
 'worked well；worked together；worked out。','It worked 是办法奏效了；It was worked on 是有人对它做了工作。多一个 on 和被动结构，意思就变了。',
 ('The printer worked yesterday, but it will not start today.','打印机昨天还能用，今天却启动不了。'),('We moved the chair, and the new arrangement worked much better.','我们挪了椅子，新的摆法好用多了。'),sources=['https://en.wiktionary.org/wiki/worked#English','https://en.wiktionary.org/wiki/work#English'])
W('played','/pleɪd/','玩过；比赛过；演奏、扮演、播放过；play 的过去式和过去分词',
 'play 的核心是参与或呈现一场活动：把比赛打起来，把音乐奏出来，把角色演出来。played 把这些动作放到过去或完成的语境里。',
 'play + -ed；元音后词尾读 /d/，字母 y 保留。play 接古英语 plegian、plegan 等形式，较早已有游戏、活动义，更深来源未完全确定。',
 [['古英语 plegian／plegan → play','游戏、参与活动；后来有演奏、扮演等义'],['play + -ed → played','过去参与、演出或播放']],
 'played chess 下过棋；played the violin 拉过小提琴；played a character 扮演过角色；played a part in ... 对……起了作用。played down 常说淡化某事的重要性。',
 'played a game；played an important role。','played 是 /pleɪd/，paid 是 /peɪd/。played football 是参加足球运动，played with a football 是拿着足球玩，后者不一定在比赛。',
 ('She played the same song twice so that we could learn it.','她把同一首歌放了两遍，好让我们学会。'),('Good planning played a large part in the event’s success.','周密的计划对活动成功起了很大作用。'),sources=['https://en.wiktionary.org/wiki/played#English','https://en.wiktionary.org/wiki/play#English'])
W('started','英 /ˈstɑːtɪd/；美 /ˈstɑːrtɪd/','开始了；启动了；惊跳了一下；start 的过去式和过去分词',
 '原来还没动，一下进入了行动：课开讲了，车发动了，人受惊一跳，都能接上 start 原来的动作画面。',
 'start + -ed；原词以 /t/ 收尾，-ed 读 /ɪd/，所以多一个音节。接古英语 styrtan、中古英语 sterten 的突然跃起、冲出词族。',
 [['古英语 styrtan → 中古英语 sterten → start','突然跃起、冲出 → 开始、启动'],['start + -ed → started','过去开始、启动；受惊而动']],
 'started doing／started to do 开始做；started with ... 从……开始；started the engine 启动发动机；got started 开始动手。',
 'started raining；started a new job。','The meeting started 说会议开始；We started the meeting 说我们让会议开始。had started 则把开始放在另一个过去事件之前。',
 ('It started raining just as we reached the station.','我们刚到车站，天就开始下雨了。'),('Once we got started, the task felt much easier.','一旦动起手来，这项任务就感觉容易多了。'),sources=['https://en.wiktionary.org/wiki/started#English','https://en.wiktionary.org/wiki/start#English'])
W('looked','/lʊkt/','看过、找过；看起来曾是；look 的过去式和过去分词',
 '一条线是把目光投过去，另一条线是别人看见你呈现的样子：looked at the clock 看了钟，looked worried 显得担心。',
 'look + -ed；/k/ 后词尾读 /t/，不增加音节。look 继承古英语 lōcian 看、注视，经中古英语形式延续。',
 [['古英语 lōcian → look','看、注视；发展出看起来等用法'],['look + -ed → looked','过去看、寻找或显得某种样子']],
 'looked for 寻找过；looked after 照料过；looked into 调查过；looked up 查过；looked like 看起来像。后面的小词决定视线朝哪类动作走。',
 'looked tired；looked at the map。','looked happy 是看起来高兴，happy 描述主语；looked happily at ... 是高兴地看向……，happily 描述看这个动作的方式。',
 ('He looked tired after the long drive.','长途开车后，他看起来很累。'),('I looked up the word before replying.','回复前，我查了这个词。'),sources=['https://en.wiktionary.org/wiki/looked#English','https://en.wiktionary.org/wiki/look#English'])
W('turned','英 /tɜːnd/；美 /tɜːrnd/','转动、转向了；变成了；turn 的过去式和过去分词',
 '转的不一定是物体：路线可以转，颜色和处境也可以转到另一种状态。turned 后面接什么，就把哪一种变化说具体。',
 'turn + -ed，/n/ 后读 /d/。turn 经早期英语、法语的相关借入路线接拉丁 tornare 车削、旋转加工，和希腊 tornos 工具词相连。',
 [['希腊 tornos → 拉丁 tornare → 早期英语、法语相关形式 → turn','旋转加工 → 转向、改变'],['turn + -ed → turned','过去转动、转向、变成']],
 'turned left 向左转了；turned pale 脸色变白了；turned into ... 变成……；turned down 拒绝、调低；turned up 出现、调高。',
 'turned the handle；turned out well。','turned out to be ... 是结果原来是……；turned into ... 是变成了……。turned down an offer 是拒绝提议，turned down the music 是调小音量。',
 ('The leaves turned red before they fell.','树叶落下前变红了。'),('The old shop was turned into a small library.','那家老店被改成了一间小图书馆。'),sources=['https://en.wiktionary.org/wiki/turned#English','https://en.wiktionary.org/wiki/turn#English'])
W('changed','/tʃeɪndʒd/','改变了；更换了；changed 为 change 的过去式和过去分词',
 '原来的样子、安排或东西被换掉了。changed 只告诉你发生了变化，变好还是变坏，要继续看上下文。',
 'change 已有不发音的 e，只加 d，写 changed；/dʒ/ 后加 /d/，仍是一个音节。change 经古法语接拉丁 cambire／cambiare 的交换、更换词族。',
 [['拉丁交换词族 → 古法语 changier → change','交换、更换 → 改变'],['change 去 e + -ed → changed','过去改变、更换；已经改变的状态']],
 'changed my mind 改了主意；changed clothes 换了衣服；changed trains 换了火车；changed into ... 换成、变成……；a changed person 变化很大的人。',
 'changed the date；things have changed。','I changed the plan 是我改了计划；The plan changed 是计划发生变化。I have changed 说人变了；I have changed clothes 才明确说换过衣服。',
 ('We changed the meeting time to avoid the rush hour.','我们改了开会时间，避开出行高峰。'),('The town has changed a lot since I last visited.','自从我上次来过后，这座镇子变了很多。'),sources=['https://en.wiktionary.org/wiki/changed#English','https://en.wiktionary.org/wiki/change#English'])
W('considered','英 /kənˈsɪdəd/；美 /kənˈsɪdərd/','考虑过；被认为；经过深思的；consider 的过去式和过去分词等',
 '把事情认真放在心里过一遍，是 considered 的考虑义；把人或物放进某种判断里，是 is considered 的被认为义。',
 'consider + -ed，词尾读 /d/。consider 经法语接拉丁 considerare 察看、思量；更深与星辰词的联系有争论，不能把观星故事当成确证。',
 [['拉丁 considerare → 法语 considerer → consider','仔细看、思量'],['consider + -ed → considered','考虑过；被认为；斟酌过的']],
 'considered moving 考虑过搬家；is considered useful 被认为有用；all things considered 综合考虑各方面；a considered response 深思后的回应。',
 'carefully considered；is considered to be ...。','considered doing 是考虑过做某事；was considered to be ... 是被认为是……。这两种结构不同，不能把前者换成 considered to do。',
 ('We considered taking the train, but the times did not suit us.','我们考虑过坐火车，但车次时间不合适。'),('Her proposal was considered practical and affordable.','她的提议被认为切实可行，而且费用可承受。'),sources=['https://en.wiktionary.org/wiki/considered#English','https://en.wiktionary.org/wiki/consider#English'])
W('received','/rɪˈsiːvd/','收到了；接收到、受到；received 为 receive 的过去式和过去分词',
 '东西、消息或反应到你这里来了：收到包裹、得到支持、受到欢迎，都可以用 received。它先说明接到了，再由宾语说明接到了什么。',
 'receive 去末尾 e，加完整 -ed；/v/ 后 -ed 读 /d/。拉丁 re- + capere 形成 recipere 接纳，经古法语 receivre 等形式进入英语 receive。',
 [['拉丁 recipere → 古法语 receivre → receive','接纳、收到'],['receive 去 e + -ed → received','收到过；已被接收']],
 'received an email 收到了邮件；received support 得到支持；was well received 受到欢迎、好评；received wisdom 普遍接受的看法，语境有时含对其质疑。',
 'received from ...；has been received。','received an invitation 是收到了邀请，accepted an invitation 才是接受邀请。was well received 的 well 描述反响好，不只说顺利送达。',
 ('We received the parcel two days after ordering it.','下单两天后，我们收到了包裹。'),('The new design was well received by the team.','团队很认可这个新设计。'),sources=['https://en.wiktionary.org/wiki/received#English','https://en.wiktionary.org/wiki/receive#English'])
W('added','/ˈædɪd/','加上了；相加了；补充说；额外增加的',
 '原来已有一份，再添一份进去：杯里添水，清单添名字，话里添说明，都是 added 的画面。',
 'add + -ed；add 原有双写 dd，直接接 ed，不是这一轮再多添一个 d。/d/ 后 -ed 读 /ɪd/。add 接拉丁 addere 加上，历史构成为 ad- 向 + -dere 放、置。',
 [['拉丁 ad- + dare → addere → add','放上去、加上'],['add + -ed → added','过去加上、补充；额外附加的']],
 'added water 加了水；added that ... 补充说……；added to the cost 增加了费用；an added benefit 额外的好处；no added sugar 未额外添加糖。',
 'added a name to the list；an added advantage。','no added sugar 只说明没有额外添加糖，食物本身仍可能含糖。added to 是给……增加，added ... to ... 是把……加到……。',
 ('I added your name to the list.','我把你的名字加进了名单。'),('She added that there was no need to hurry.','她补充说，不用着急。'),('The quiet location is an added benefit.','位置安静是额外的好处。'),sources=['https://en.wiktionary.org/wiki/added#English','https://en.wiktionary.org/wiki/add#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wa',ROOTS,WORDS)
 extend_lessons()
