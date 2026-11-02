"""Magic, award, weather: everyday meanings with distinct historical routes."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
M=[['伊朗语背景的称谓 → 希腊语 magos、magikos','祭司、术士等称谓；相应的术法'],['拉丁语 magicus、magica → 法语 magique → 中古英语 magik → magic','魔法、法术；后来也用于舞台魔术与神奇效果']]
def MH(f,m):return M+[[f,m]]
W('magic','/ˈmædʒɪk/','魔法；魔术；神奇力量、魅力；有魔力的',
 '一挥手，帽子里冒出兔子：故事里可能真有法力，舞台上则是让人看不穿的技巧。好音乐带来的神奇感也能叫 magic。',
 '经法语、拉丁语接希腊语 magikos、magos，较早背景是伊朗地区的祭司等称谓。不能按现代拼写拆成 mag“巨大”加 ic，再编成巨大的力量。',M,
 'do magic 表演魔术，a magic trick 魔术把戏，the magic of music 音乐魅力，a magic wand 魔杖。work your magic 可说施展本领，让事情见效。',
 'a magic trick；a magic wand；the magic of；work your magic。',
 'magic 可名词，也可形容与魔法相关的东西；trick 可指手法、把戏。a magic number 往往是具有特别效果的数值，并不一定是迷信数字。',
 ('The children watched him perform a magic trick.','孩子们看他表演了一个魔术。'),('The old theatre has lost none of its magic.','那座老剧院的魅力丝毫未减。'),
 sources=['https://en.wiktionary.org/wiki/magic#English','https://www.etymonline.com/word/magic'])
W('magical','/ˈmædʒɪkəl/','有魔法的；神奇、美妙得像有魔法的',
 '既可以是能施法的森林，也可以是一次真实而难忘的夜晚。后一种是在说体验像童话般美妙。',
 'magic + -al，形成形容词。magic 自己也能作形容词，不能理解为加 -al 才第一次获得形容词资格。',MH('magic + -al → magical','魔法的；令人感到神奇美妙的'),
 'magical powers 魔力，a magical evening 美妙夜晚，a magical atmosphere 梦幻气氛。',
 'magical powers；a magical moment；a magical atmosphere。',
 'magic trick 是常用搭配；a magical experience 强调神奇体验。二者用法有重叠，不能硬定 magic 全指真的魔法、magical 全指假的。',
 ('In the story, the ring has magical powers.','故事里，那枚戒指有魔力。'),('We spent a magical evening by the lake.','我们在湖边度过了一个美妙的夜晚。'))
W('magically','/ˈmædʒɪkli/','靠魔法；神奇地、仿佛变魔术般',
 '变化发生得太轻巧、太突然，好像有人暗中挥了魔杖；也常用来反驳事情不会自己解决。',
 'magical + -ly；也可从 magic + -ally 认识这个词形。常用读音中间较紧凑，不把拼写中的每个字母都读成一节。',MH('magical + -ly → magically','用魔法；像变魔术一样地'),
 'magically disappear 神奇地消失，magically transform 仿佛施法般改变；will not magically fix itself 不会凭空自己修好。',
 'magically disappear；magically transform；not magically solve。',
 'magically 强调神奇方式或观感，不等于 automatically 自动地；自动完成可以有明确机械过程。',
 ('The rabbit seemed to disappear magically.','兔子仿佛施了魔法般消失了。'),('The problem will not magically solve itself.','这个问题不会凭空自己解决。'))
W('magician','/məˈdʒɪʃən/','魔术师；故事中的术士、法师；妙手人物〔比喻〕',
 '站在台上让硬币消失的人，今天通常是魔术师；奇幻故事里也可能真有法力。',
 '历史接法语 magicien 等形式，与 magique 同族；现代可对照 magic 与人物后缀 -ian 认识。词中 c 对应 /ʃ/，重音也移到后面，不读成 magic 原音直接接人。',M[:1]+[['法语 magicien → 英语 magician','从事魔术、术法的人；后来也比喻技艺神奇者']],
 'a stage magician 舞台魔术师，a skilled magician 技艺高超的魔术师；a magician in the kitchen 比喻很会做菜。',
 'a stage magician；a professional magician；a magician with。',
 'magician 是人，magic 是术法或神奇效果；wizard 在奇幻作品里常是法师，也可比喻高手，具体作品的职业设定不能一概而论。',
 ('The magician asked a volunteer to choose a card.','魔术师请一位志愿者选一张牌。'),('My grandmother was a magician in the kitchen.','我奶奶在厨房里简直有一双巧手。'))
R('B3217','术法、魔术与神奇体验','MAGIC：让人觉得超出平常理解的力量或效果','magic → magical → magically；magician 作为人物名词与前三词相邻。',
 '近源经法语、拉丁语接希腊语，早期伊朗称谓背景不能随意改写成现代英语零件。舞台魔术、奇幻法力、体验魅力分场景讲。',
 'magic + -al → magical；magical + -ly → magically；magician 与法语人物词有关，注意 /məˈdʒɪʃən/。',
 [['基本概念及性质、方式','magic · magical · magically'],['人物','magician']],
 'magic 与 magical 都可作形容词但搭配不同；magically 不等于 automatically；magician 是人物。',
 'The magician created a magical atmosphere with a simple magic trick.\n\n魔术师用一个简单魔术营造了神奇气氛。','magic magical magically magician')
A=[['盎格鲁法语 awarder、award 等 → 中古英语 awarden、award','观察、考虑后作判断；作出的决定'],['英语 award','裁定给予 → 颁发、授予；所授的奖项、款项等']]
W('award','英 /əˈwɔːd/；美 /əˈwɔːrd/','奖项；授予、颁发；裁定给予',
 '先有人审看、评判，再决定把奖、资格或款项给谁。重点在正式决定给予，不只是随手把东西递过去。',
 '经盎格鲁法语 awarder 等进入英语，旧意是考虑后裁定。更早与表示看守、观察的 warder 有关；不是现代 a + ward“一个病房”。',A,
 'win an award 获奖，award someone a prize 授某人奖，award a contract 授予合同。裁定赔偿也可用 award，不一定是表扬某人的奖。',
 'win an award；award a scholarship；award a contract；an award ceremony。',
 'reward 更泛指回报、酬谢，award 常有评选或正式决定。award 与 reward 拼写相近，但不能靠删加一个 r 解释历史。',
 ('Her first novel won a major literary award.','她的第一部小说获得了一项重要文学奖。'),('The committee awarded her a scholarship.','委员会授予了她一项奖学金。'),
 sources=['https://en.wiktionary.org/wiki/award#English','https://www.etymonline.com/word/award'])
W('awardee','英 /əwɔːˈdiː/；美 /əwɔːrˈdiː/','获奖者；获授者',
 'award 是把某物正式授出去，awardee 是接到它的那一方。-ee 在这里把镜头转向接受者。',
 'award + -ee，表示被授予奖项、资助等的人或机构；重音常落在后缀。',A+[['award + -ee → awardee','接受所授奖项、资助等的一方']],
 'an awardee of a prize 某奖获奖者，grant awardees 获得资助者。较正式，日常也常说 winner 或 recipient。',
 'an awardee；the awardees；a grant awardee。',
 'awardee 接受者，awarder 授予者；a winner 通常强调赢得比赛、奖，awardee 更强调被授予。',
 ('Each awardee received a certificate at the ceremony.','每位获奖者都在典礼上拿到一张证书。'),('The grant awardees met to discuss their projects.','获得资助的人聚在一起讨论各自项目。'))
R('B3790','审看后决定授予；奖项和获授方','AWARD：评判之后，正式决定给谁','award → awardee：先讲授予和所授之物，再讲接受者。',
 '近源是法语判断、裁定；不把历史写成英语 a 与 ward 的生硬组合。赔偿、合同、奖项都能接正式决定这条线。',
 'award + -ee；award someone something / award something to someone。',
 [['正式给予与接受者','award · awardee']],
 'award 正式授予，reward 回报；awardee 接受者；award a contract 不等于给合同颁奖。',
 'The committee announced the award and congratulated the awardee.\n\n委员会公布了奖项，并向获奖者表示祝贺。','award awardee')
T=[['古英语 weder → 中古英语 weder → weather','天空、大气、风暴等天气状况'],['名词 weather 派生动词用法','受风雨影响而风化；经受风暴 → 挺过困难']]
def TH(f,m):return T+[[f,m]]
W('weather','英 /ˈweðə/；美 /ˈweðər/','天气；风化、受风雨侵蚀；挺过〔困难〕',
 '抬头看晴雨、感受冷暖是名词；木头在户外被晒旧是动词；人或公司撑过风波，也能借这幅画面来说。',
 '古英语 weder 经中古英语延续，后来词中拼写变为 th。现代动词由天气名词发展：暴露在天气中、经受风雨，再延伸到经受危机。远源与吹风的联系有不同分析，本文不作确定定论。',T,
 'bad weather 坏天气，a weather forecast 天气预报，weather a storm 挺过风暴或风波。weather 通常不可数，谈天气常说 the weather。',
 'the weather forecast；bad weather；weather a crisis；weather the storm。',
 'weather 某时某地的天气，climate 较长期的气候特点；weather 与 whether“是否”常同音，不能互换拼写。',
 ('The weather changed quickly in the mountains.','山里的天气变得很快。'),('The small business managed to weather the crisis.','这家小企业设法挺过了危机。'),
 sources=['https://en.wiktionary.org/wiki/weather#English','https://www.etymonline.com/word/weather'])
W('weathering','英 /ˈweðərɪŋ/；美 /ˈweðərɪŋ/','风化；经受、挺过〔weather 的 -ing 形式〕',
 '石头留在原地，日晒雨淋让它裂开、变碎或发生化学变化，这个变化过程就是地理课里说的风化。',
 'weather + -ing。名词可指风化过程；作分词时也可接挺过困难的动词义，不是每处都说石头。',TH('weather + -ing → weathering','风化过程；正在经受、挺过'),
 'chemical weathering 化学风化，physical weathering 物理风化，weathering a difficult period 正在度过艰难时期。',
 'chemical weathering；physical weathering；signs of weathering。',
 'weathering 强调材料在原处的分解、改变；erosion 侵蚀常涉及搬移。动词 weathering a crisis 则是经受危机，依宾语判断。',
 ('The rock shows clear signs of weathering.','这块岩石呈现明显风化痕迹。'),('The company is weathering a difficult period.','公司正在艰难度过一段困难时期。'))
W('weathered','英 /ˈweðəd/；美 /ˈweðərd/','风化、风吹日晒而旧的；饱经风霜的',
 '木栅栏被晒成灰色，人的脸被风雨刻出痕迹，都能表现为 weathered。',
 'weather + -ed，过去式、过去分词形成的形容词用法。说外表时常是长期暴露的结果；has weathered a crisis 则说已经挺过危机。',TH('weather + -ed → weathered','受风雨作用而改变的；已经经受过'),
 'weathered wood 风化木材，a weathered face 饱经风霜的脸；a weathered surface 久经风雨的表面。',
 'weathered wood；a weathered face；a weathered surface。',
 'weathered 描写经历风雨留下的痕迹，old 只说年龄、年代；新造的仿旧木板也可刻意做出 weathered look。',
 ('The gate was made of weathered wood.','大门用风吹日晒而变旧的木头制成。'),('His weathered face broke into a smile.','他那饱经风霜的脸露出了笑容。'))
W('weatherman','英 /ˈweðəmæn/；美 /ˈweðərmæn/','男性天气预报员',
 '在节目里告诉你明天会不会下雨的人。man 在这里是人物成分，常用于男性预报员。',
 'weather 天气 + man 人，合成职业称呼。泛指不限定性别的工作者时，weather forecaster 或 weather presenter 更方便。',TH('weather + man → weatherman','播报、预报天气的男性人员'),
 'the TV weatherman 电视天气预报员，according to the weatherman 据预报员所说；复数 weathermen。',
 'the TV weatherman；according to the weatherman；a local weatherman。',
 'weatherman 职业称呼，weather 天气；并非天气好的人。meteorologist 气象学家更侧重专业研究、预测背景，不必都在电视上播报。',
 ('The weatherman says it will rain tomorrow.','天气预报员说明天会下雨。'),('She interviewed the local weatherman about the forecast.','她采访了当地的男性天气预报员，询问天气预测情况。'))
W('weatherproof','英 /ˈweðəpruːf/；美 /ˈweðərpruːf/','耐风雨的；使能抵御风雨',
 '放在室外也有办法挡雨、耐晒，经受天气影响。-proof 强调抵御某种影响。',
 'weather + -proof，形成形容词，也能转作使耐风雨的动词。具体保护程度仍看产品和环境，词义不保证任何极端条件都无损。',TH('weather + -proof → weatherproof','能抵御天气影响；使耐风雨'),
 'a weatherproof cover 防风雨罩，weatherproof paint 耐候涂料，weatherproof a shed 给棚屋做耐风雨处理。',
 'a weatherproof cover；weatherproof paint；weatherproof the shed。',
 'weatherproof 防天气影响，waterproof 防水，侧重点不同；weatherproof 里的 proof 不表示证明天气存在。',
 ('Put a weatherproof cover over the outdoor furniture.','给户外家具盖上防风雨罩。'),('They weatherproofed the shed before winter.','他们入冬前给棚屋做了耐风雨处理。'))
R('B2793','天气；受风雨作用；经受风波','WEATHER：外面的晴雨冷暖，也是一场要撑过去的风雨','weather → weathering、weathered；职业 weatherman、防护 weatherproof 随后。',
 '从古英语天气名词讲起。动词风化与挺过风波分开举例，避免只按天气一个中文义硬套。',
 'weather + -ing/-ed；weather + man；weather + -proof。',
 [['天气、风化与经受','weather · weathering · weathered'],['预报与防护','weatherman · weatherproof']],
 'weather/whether 常同音；weather/climate 时间尺度不同；weathering/erosion 改变与搬移侧重不同；weatherproof 不等于任何天气都绝对无损。',
 'The weatherman predicted rain, so we covered the weathered bench with a weatherproof sheet.\n\n预报员说会下雨，于是我们给风吹日晒的长椅盖上一张防风雨罩布。',
 'weather weathering weathered weatherman weatherproof')
if __name__=='__main__':save('continuation_20261030_bw',ROOTS,WORDS)
