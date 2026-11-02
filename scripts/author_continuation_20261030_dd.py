"""Kick and ad: transparent modern compounds with a cautious historical path."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
K=[['中古英语 kyken 等 → kick','伸脚击、踢；更早来源未完全确定'],['现代动作比喻','踢的一下 → 冲击、刺激、兴奋感等']]
def KH(f,m):return K[:1]+[[f,m]]
W('kick','/kɪk/','踢、踢的一下；刺激、兴奋感；〔习惯〕戒掉',
 '脚突然向外一送，把球送走，这是 kick。强烈味道、让人兴奋的体验，也像给感官来一下，于是可说有 a kick。',
 '从中古英语 kyken 等接来，更早与北欧弯膝等动词的联系有不同分析。先抓住可靠的踢义，不把远源猜想写成定论。名词踢、刺激等再由动作扩展。',K,
 'kick a ball 踢球，get a kick out of something 从中得到乐趣，food with a kick 味道很冲的食物，kick a habit 戒掉习惯。kick in 可开始起作用。',
 'kick a ball；get a kick out of；have a kick；kick a habit；kick in。',
 'kick 用脚，hit 范围更宽；a kick 可是乐趣、刺激，不必有实际伤害。kick a habit 是习语，不能对所有完成动作都用 kick。',
 ('He kicked the ball over the fence.','他把球踢过了围栏。'),('I get a real kick out of solving difficult puzzles.','解开难题让我特别有成就感和乐趣。'))
W('kicker','英 /ˈkɪkə/；美 /ˈkɪkər/','踢球者、踢球手；意外转折、关键难点〔口语〕',
 '可以是真正踢球的人；口语 here’s the kicker 则是前面讲了一堆，最后还有一件让你惊讶、改变态度的事。',
 'kick + -er 形成人物、事物名词。抽象 kicker 借突如其来的一下表示额外冲击，不强编成某一项运动唯一传来的故事。',KH('kick + -er → kicker','踢的人；有冲击力的补充、转折'),
 'the team’s kicker 队里的踢球手，here’s the kicker 关键转折来了，the real kicker 真正令人意外之处。',
 'the team’s kicker；here’s the kicker；the real kicker。',
 '口语 kicker 不总是坏事，也可额外好处或惊喜；kicker 是人物、转折，kick 是动作或冲击本身。',
 ('The team signed a new kicker this season.','球队这个赛季签下一名新踢球手。'),('The room was cheap, but here’s the kicker: it had no window.','房间很便宜，可问题来了：它没有窗户。'))
W('kickboxing','英 /ˈkɪkbɒksɪŋ/；美 /ˈkɪkbɑːksɪŋ/','踢拳、自由搏击类运动',
 '既用拳也允许踢的一类搏击运动名称；名称说明拳、腿结合，不代表所有流派规则完全一样。',
 '现代材料为 kick + boxing，boxing 为拳击。资料也把名称传播联系到日语 キックボクシング：英语材料在日本组合使用后回传英语，不能只靠外形断定传播从未绕路。',
 KH('kick + boxing；与日语 kikkubokushingu 的传播有关 → kickboxing','把踢与拳击结合的运动名'),
 'a kickboxing class 踢拳课，take up kickboxing 开始练踢拳，a kickboxing gym 踢拳馆。',
 'a kickboxing class；take up kickboxing；a kickboxing gym。',
 'boxing 主要拳击，kickboxing 名称包含踢；不同项目的完整规则另看具体组织，不从一个复合词推导全部规则。',
 ('She takes a kickboxing class twice a week.','她每周上两次踢拳课。'),('The gym offers boxing and kickboxing lessons.','这家健身馆提供拳击课和踢拳课。'),
 sources=['https://en.wiktionary.org/wiki/kickboxing#English','https://www.etymonline.com/word/kickboxing'])
W('kickball','英 /ˈkɪkbɔːl/；美 /ˈkɪkbɔːl/','踢球跑垒游戏；所用的球',
 '大体像棒球那样跑垒，但用脚踢球来开始进攻，常见于孩子、学校与休闲活动。',
 'kick 踢 + ball 球，按主要动作命名的游戏、用球。两个成分并列组合。',KH('kick + ball → kickball','以踢球结合跑垒的游戏'),
 'play kickball 玩踢球跑垒游戏，a kickball game 一场游戏，a kickball team 踢球跑垒队。',
 'play kickball；a kickball game；a kickball team。',
 'kickball 是一种具体游戏名，不是所有用脚踢球运动的总称；football/soccer 与它不同。',
 ('The children played kickball after lunch.','孩子们午饭后玩踢球跑垒游戏。'),('Our class formed two kickball teams.','我们班组了两支踢球跑垒队。'))
R('B3220','踢的动作与冲击、刺激的扩展','KICK：脚送出去的一下，后来也说感觉受到冲击','kick → kicker；kickboxing、kickball 按动作和运动组合，sidekick、kickstand 是已有常见旁支。',
 '从踢这个可靠动作出发。a kick 的兴奋感、kicker 的转折都借冲击来理解，早期深源不强定。',
 '中古英语 kyken → kick；kick + -er；kick + boxing/ball/stand；sidekick 的人物义按既有历史另看。',
 [['动作、感觉与人物或转折','kick · kicker'],['运动与物品','kickboxing · kickball · kickstand'],['人物旁支','sidekick']],
 'kick 以脚，hit 不限脚；kicker 不保证坏消息；kickball 不是足球总称；kickboxing 保留跨语言命名的可能路径。',
 'I get a kick out of playing kickball with my friends.\n\n和朋友玩踢球跑垒游戏让我很开心。','kick kicker kickboxing kickball kickstand sidekick')
W('adblock','英 /ˈædblɒk/；美 /ˈædblɑːk/','广告拦截；广告拦截功能、工具〔常见于软件语境〕',
 '网页本来要显示广告，工具在加载、显示环节把它挡住。ad 是 advertisement 的缩短，block 是阻挡。',
 '现代材料为 ad + block，普通用法也受 AdBlock、Adblock Plus 等软件名称通用化的影响。功能名与具体软件专名须按大小写、上下文区分，不把所有 adblock 都当同一家产品。',
 [['advertisement → ad','广告的缩略形式'],['ad + block → adblock','阻止广告显示的功能、工具']],
 'enable adblock 启用广告拦截，disable adblock 关闭广告拦截；ad blocker 是更完整的工具称呼。',
 'enable adblock；disable adblock；adblock settings。',
 'adblock 针对广告，popup blocker 针对弹出窗口，两者可能重叠但不相同；ad 在这里不接拉丁朝向前缀 ad-。',
 ('The site asked visitors to disable adblock.','网站请访客关闭广告拦截。'),('She checked the adblock settings in her browser.','她检查了浏览器里的广告拦截设置。'))
R('B2534','广告缩写及广告拦截','AD：advertisement 缩短后，成了现代复合词材料','ad 是基础缩略词，adblock 接阻挡功能。',
 '这个 ad 是独立的广告词，不是把单词开头 ad- 全当成同一种广告意义。an ad 说一则广告，ads 是复数。',
 'advertisement → ad；ad + block → adblock。',
 [['广告与功能','ad · adblock']],
 'ad 广告，add 添加发音相同但拼写和来源不同；adblock 与具体软件专名须分清。',
 'The adblock feature stopped the ad from loading.\n\n广告拦截功能阻止了那则广告加载。','ad adblock')
if __name__=='__main__':save('continuation_20261030_dd',ROOTS,WORDS)
