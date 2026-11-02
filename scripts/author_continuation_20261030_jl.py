"""Con, rap, loneliness and intentioned."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['confidence trick／confidence man → con 的骗局义','先骗得信任，再骗取利益'],['contra 反对 → con 的反方、不利面义','pros and cons 利弊'],['其他独立来源','convict、convention 等的缩称；旧 con 学习另接古英语知识词源']]
W('con','英 /kɒn/；美 /kɑːn/','骗局、诈骗；欺骗；不利面、反对理由；大会等词的缩称',
 '同一个短词装了几条来源。It’s a con 是骗局，pros and cons 是利弊，a comic con 则是漫画主题大会；不能都套成一个共同词根。',
 '诈骗义缩自 confidence trick、confidence man，抓骗取信任；反方义缩自拉丁 contrā 反对。另有 convict 囚犯、convention 大会等缩称，以及接旧知识词源的学习动词。',C,
 'a con trick 骗局，con someone into doing 骗某人做，the pros and cons 利弊，a fan con 粉丝大会。作为动词，conned、conning 双写 n。',
 'a con trick；con someone into；pros and cons；a comic con。',
 '独立 con 的多条缩词来源，不等于所有单词里的 con- 都是欺骗，也不等于拉丁 con-／com- 一起这个前缀。',
 ('The offer turned out to be a con.','那份优惠原来是骗局。'),('We discussed the pros and cons of moving.','我们讨论了搬家的利弊。'),sources=['https://en.wiktionary.org/wiki/con#English','https://www.etymonline.com/word/con'])
W('conman','英 /ˈkɒnmæn/；美 /ˈkɑːnmæn/','骗子；靠取得信任行骗的人',
 '先装得可靠，让你愿意相信，再利用你的信任骗钱、骗利益，就是 conman 的典型套路。它不仅是偶尔说错话的人。',
 'con 的 confidence 欺诈缩称 + man；也可理解为 confidence man 的缩短形式。不是反对的 con + man，后半主要标人物。',C[:1]+[['con + man → conman','以取得信任来行骗的人']],
 'a clever conman 狡猾骗子，expose a conman 揭穿骗子。也常分写 con man，con artist 则是常见的不带 man 的说法。',
 'a clever conman；expose a conman；con artist。',
 'conman 涉及欺骗意图，不能把一次诚实错误直接当骗局。cunning 狡猾在意义上有关，但它本身不是 conman 的词源。',
 ('The film follows a conman who invents a false identity.','电影讲述一个伪造身份行骗的骗子。'),('The journalist exposed the conman’s scheme.','记者揭穿了骗子的计划。'))
R('B3236','近形短词的多条来源：骗局、反方、缩称与旧学习词','CON：先判断是哪一条来源，再理解整句','con 骗局 → conman；pros and cons 的 con 来自 contra；cunning 只与旧知识词源支线相连。',
 '这个页面把同形词分开。共同拼写不代表每个意思从同一个画面长出来，更不能把所有 con- 前缀都当诈骗。',
 'confidence、contra、convict、convention 等分别缩成 con；旧 con 学习另接古英语 cunnan／cunnian 等知识、尝试相关形式。',
 [['骗局与人物','con · conman'],['旧知识词源的对照','cunning']],
 'cunning 不由骗局 con 直接加 -ing；pros and cons 不说一堆骗子。',
 'The conman’s cunning helped his con appear convincing.\n\n骗子的狡猾让他的骗局显得可信。','con conman cunning')
Q=[['中古英语 rap／rappen 等','短促敲击、敲打，或有北欧语言和拟声联系'],['动作借给说话、责备等','急促说出、谈话；指责、责任'],['现代音乐用法','在节奏上组织语言，形成 rap 的音乐与表演含义']]
W('rap','/ræp/','短促敲击；说唱、说唱音乐；指责、责任〔口语〕',
 '手指短促敲门是 rap；把话说得有力度、节奏鲜明，又发展到说唱。a bad rap 却常是坏名声、不公的负面评价。',
 '接中古英语 rap、rappen 等，可能联系斯堪的纳维亚语或拟声形成。说话、说唱由较早动作、言语用法发展，不是先造 rhythm and poetry 的首字母缩写。',Q,
 'a rap on the door 一下短促敲门声，rap music 说唱音乐，rap lyrics 说唱歌词，get a bad rap 落得不好的名声，take the rap 承担责罚、责任。',
 'a rap on the door；rap music；get a bad rap；take the rap。',
 'rap 与 wrap 包裹同音；音乐 rap 不是 wrap 的省写。hip-hop 是更广的文化、音乐语境，rap 主要说其中的节奏化语言表演，不完全等同。',
 ('We heard a sharp rap on the door.','我们听到门上短促的一记敲击声。'),('The review gave the album an unfairly bad rap.','那篇评论给这张专辑的负面评价并不公允。'),sources=['https://en.wiktionary.org/wiki/rap#English','https://www.etymonline.com/word/rap'])
W('rapper','英 /ˈræpə/；美 /ˈræpər/','说唱歌手、说唱表演者；敲击者或敲击器〔其他语境〕',
 '现代最常想到说唱表演者：用节奏、押韵和语言组织来表演的人。词形更老的含义则可以是敲击的人、器具。',
 'rap + -er，随 rap 的不同动词义形成人物、器具词。音乐人物义接说唱用法，不能拿今天歌手义倒推所有早期 rapper。',Q+[['rap + -er → rapper','执行敲击、说唱等不同动作的人物或器具']],
 'a talented rapper 有才华的说唱表演者，a rapper’s lyrics 说唱歌手的歌词。rapper 不必是职业录音艺人，也可说具体表演者。',
 'a talented rapper；a rapper’s lyrics。',
 'rapper 与 wrapper 包装纸、包裹物同音，但后者来自 wrap。纸包住糖果的那层是 wrapper，不是 rapper。',
 ('The rapper wrote all the lyrics on the album.','这位说唱歌手写了专辑的全部歌词。'),('A local rapper performed at the festival.','一位当地说唱表演者在音乐节上演出。'))
R('B3905','短促敲击、言语与音乐表演，以及责备的固定用法','RAP：从短促、有力的动作到说话和音乐，固定搭配另看','rap → rapper；get a bad rap 负面名声，take the rap 担责。',
 '抓声音和言语的历史联系，同时把固定搭配记成真实用法。音乐词源不需要后来凑出的字母全称。',
 '中古英语 rap、rappen → 动作、言语等分支；rap + -er；rap 音乐并非 rhythm and poetry 的原始缩写。',
 [['动作、音乐与人物','rap · rapper']],
 'rap／wrap、rapper／wrapper 同音不同词；rap 与 hip-hop 关系密切，范围并不全相同。',
 'The rapper turned a simple beat into a memorable rap performance.\n\n说唱表演者把简单节拍组织成了一场令人难忘的说唱演出。','rap rapper')
W('loneliness','英 /ˈləʊnlinəs/；美 /ˈloʊnlinəs/','孤独、寂寞；孤寂状态',
 '身边缺少想要的陪伴、连接，心里空落落，是 loneliness 的常见感受。有时也描写一个地方无人活动的孤寂。',
 'lonely + -ness，y 变 i。lonely 接 lone、alone 一系，alone 的历史联系 all one 单独一人；现代孤独感却不按在场人数机械计算。',
 [['alone → lone → lonely','独自一人 → 孤独、寂寞的性质'],['lonely + -ness → loneliness','孤独感；孤寂状态']],
 'a feeling of loneliness 孤独感，ease loneliness 缓解孤独，the loneliness of the place 那地方的孤寂。通常不可数。',
 'a feeling of loneliness；ease loneliness；the loneliness of。',
 'being alone 说独处事实，loneliness 常说缺少连接的感受。人可以独处却自在，也可能在人群中孤独；它本身不是某种临床诊断的同义词。',
 ('She sometimes felt loneliness even in a crowded room.','她有时即使在人多的房间里也觉得孤独。'),('Regular visits helped ease his loneliness.','定期探望帮助缓解了他的寂寞。'))
R('B3842','孤独的性质，以及把这种感受作为名词来谈','LONELY：觉得缺少连接；LONELINESS：这种感受、状态','lonely → loneliness。',
 '独处是一种情境，孤独可以是一种感受。解释时把事实与感受分开，例句就更容易理解。',
 'alone、lone 相关词族 → lonely；加 -ness 时 y 变 i。',
 [['性质与状态名词','lonely · loneliness']],
 'alone 不自动等于 lonely；loneliness 不是仅按周围有几个人来量。',
 'She was alone that afternoon but did not feel lonely or experience loneliness.\n\n那天下午她独处，却没有感到寂寞。','lonely loneliness')
W('intentioned','/ɪnˈtenʃənd/','怀有某种意图的〔通常带限定词〕',
 '这个词常需要前面交代意图怎样：well intentioned 本意良好，badly intentioned 怀着坏意。它给人或行为的出发点加说明。',
 'intention 意图 + -ed，这里的 -ed 形成具有某种东西的形容词，不是 intention 这个名词自己发生过去动作。词尾常读 /ʃənd/，不多加 /ɪd/。',
 [['拉丁 intentiō 经法语等 → intention','意图、心中指向的目的'],['intention + -ed → intentioned','具有某种意图；通常由 well 等说明性质']],
 'well intentioned 本意良好的，badly intentioned 怀有恶意的。放在名词前常写作 a well-intentioned suggestion，连字符标出整体修饰关系。',
 'well intentioned；badly intentioned；a well-intentioned suggestion。',
 'well intentioned 评价出发点，effective 评价有没有用。好心建议也可能效果差；intentional 则是故意的，不等于出于好意。',
 ('The advice was well intentioned but unhelpful.','建议出于好意，却没有帮助。'),('She appreciated his well-intentioned efforts.','她感激他出于好意所作的努力。'))
R('B4317','意图这一名词，以及怀有某种意图的形容词','INTENTIONED：看出发点怎样，不先断定效果怎样','intention → intentioned，常搭配 well、badly 等限定。',
 '把想达到的目的、出发点与实际结果分开。这样 well intentioned but unhelpful 就不矛盾。',
 'intention + -ed，具有某种意图；这个 -ed 不是普通动词过去时。',
 [['意图与出发点性质','intention · intentioned']],
 'intentioned 通常带限定；intentional 故意的与 well intentioned 出于好意不同。',
 'Her intention was to help, and the suggestion was well intentioned.\n\n她的意图是提供帮助，那条建议也是出于好意。','intention intentioned')
if __name__=='__main__':save('continuation_20261030_jl',ROOTS,WORDS)
