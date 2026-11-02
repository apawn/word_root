"""Cow, twin, fortune and awkward; keep homographs distinct."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['古英语 cū → 中古英语 cow／cou → cow 名词','母牛；日常也可较宽泛说牛'],['名词与职业、物件组合','cowherd 牧牛人；cowbell 牛铃等'],['cow 动词的另线','通常联系古诺尔斯语 kúga 压迫，不由母牛性格硬推']]
W('cow','/kaʊ/','母牛；牛〔日常泛称〕；吓住、威吓',
 '动物名的核心是成年雌牛；日常指一群 cows 时也可能用得较宽。动词 cow someone 则是把对方吓得不敢反抗，来源要另看。',
 '动物名承接古英语 cū，经中古英语 cow、cou 留传。威吓动词通常联系古诺尔斯语 kúga 压迫，两条直接来源不同，不编成因为母牛胆小。',C,
 'a dairy cow 奶牛，a herd of cows 一群牛，cow someone into silence 威吓得某人不敢说话。名词通常复数 cows /kaʊz/；kine 是古旧形式，先认识不必常用。',
 'a dairy cow；a herd of cows；cow someone into silence。',
 'cow 严格动物用法突出雌性，bull 指成年雄牛，cattle 是牛的集合称呼。动词 cow 不等于把某人变成母牛。',
 ('The farmer keeps a small herd of dairy cows.','农场主养着一小群奶牛。'),('She refused to be cowed by his threats.','她不肯被他的威胁吓住。'))
W('cowherd','英 /ˈkaʊhɜːd/；美 /ˈkaʊhɝːd/','牧牛人',
 '不是那群牛，而是跟着、照管、放牧牛群的人。旧后半 herd 在这里是牧者的身份。',
 '古英语 cūhierde，经中古英语 couherde；对应 cow + herd 牧者。与 shepherd 牧羊人中的后半同类，不把整词译成牛群。',C[:2]+[['cow + 旧 herd 牧者 → cowherd','照管、放牧牛的人']],
 'a young cowherd 年轻牧牛人，the cowherd’s cattle 牧牛人照管的牛。故事、乡村生活和历史叙述中常见。',
 'a young cowherd；the cowherd’s cattle。',
 'a cowherd 是一个人；a herd of cows 才是一群牛。cowboy 也可涉及牧牛工作，但有特定地域、文化形象。',
 ('The cowherd led the cattle back before sunset.','牧牛人在日落前把牛群带了回来。'),('The story begins with a young cowherd in a mountain village.','故事从山村里一个年轻牧牛人讲起。'))
W('cowling','英 /ˈkaʊlɪŋ/；美 /ˈkaʊlɪŋ/','发动机罩、整流罩',
 '飞机、摩托车发动机外面套着一层罩子，用来保护、整理外形，这就是 cowling 的常见机械义。它不在说小母牛。',
 '常用机械名词为 cowl 罩 + -ing。另有罕见 cow + -ling 小牛的同形词，那才接母牛；两条来源不能凭拼写合并。',
 [['cowl 罩、罩形物','像套在外面的覆盖物'],['cowl + -ing → cowling','发动机等外部的防护、整流覆盖结构']],
 'the engine cowling 发动机罩，remove the cowling 拆下发动机罩。航空用法中可与气流、冷却、维护结构有关，具体设计并不全一样。',
 'the engine cowling；remove the cowling。',
 'cowling 的常见来源边界是 cowl + -ing，不是 cow + -ling。cover 范围宽，cowling 更常是机械设备外罩的具体名称。',
 ('The mechanic removed the engine cowling.','机械师拆下了发动机罩。'),('The aircraft’s cowling was inspected for damage.','飞机的发动机罩接受了损伤检查。'))
R('B2543','母牛名称、牧牛相关组合；另辨威吓动词和发动机罩','COW：动物名这一线清楚，近形词还要看真实切分','cow → cowherd、cowbell、cowhide；cowboy、cowgirl 结合牧牛文化；cowling 机械义来自 cowl。',
 '主线是牛，但不是每个开头像 cow 的词都在讲牛。常见威吓动词和机械外罩都需要单独交代。',
 'cū → cow 名词；旧 hierde 牧者 → cowherd；cow 动词通常另接 kúga；cowling 常用义为 cowl + -ing。',
 [['动物、职业与相关物件','cow · cowherd · cowboy · cowgirl · cowbell · cowhide'],['近形词的来源辨认','cowling']],
 'cowherd 是人，a herd of cows 是群；cowling 发动机罩不按小母牛拆。',
 'The cowherd listened for the cowbell while the mechanic inspected an engine cowling nearby.\n\n牧牛人听着牛铃声，附近的机械师则检查发动机罩。','cow cowherd cowboy cowgirl cowbell cowhide cowling')
T=[['古英语 ġetwinn／twinn 等形式','成双、两个一组；孪生者'],['中古英语 twinne → twin','双胞胎之一；成对、结对'],['twin + -ing → twinning','孪生、结对、成对形成的过程或活动']]
W('twin','/twɪn/','双胞胎之一；成对的；结对',
 '两个一起出生的孩子，各自是 a twin，两个人是 twins。这个成双的感觉又借给成对建筑、目标和结成伙伴的城镇。',
 '接古英语 ġetwinn、twinn 等，远源联系 two 的两个概念。现代可作名词、形容词、动词，不是 twi 加一个有独立意义的 n。',T[:2],
 'her twin sister 她的孪生姐妹，twin engines 双发动机，a twin room 双床房，be twinned with 与某地结为友好城镇〔尤见英式〕。',
 'a twin sister；twin engines；a twin room；be twinned with。',
 'twin room 通常是两张分开的床；double room 常是一张双人床的房间，具体仍看住宿说明。双胞胎也不一定外貌完全一样。',
 ('Her twin brother lives in another city.','她的双胞胎兄弟住在另一座城市。'),('The two towns are twinned to promote cultural exchanges.','两个城镇结为友好城镇，以促进文化交流。'))
W('twinning','/ˈtwɪnɪŋ/','孪生；结对；相配、像双胞胎一样〔口语〕；孪晶形成',
 'twin 让两个对象成一对，twinning 就把这个关系的形成或活动拿出来谈。可以是城镇结对，也可以是两个人穿得很像。',
 'twin + -ing，双写 n。动物孪生、城镇结对、晶体孪晶是不同领域用法，共同联系成双、对应的关系，不是两张照片完全相同才算。',T,
 'town twinning 城镇结对，a twinning programme 友好城镇项目；We’re twinning! 口语可笑说我们穿得真像。技术文献中 crystal twinning 是孪晶现象。',
 'town twinning；a twinning programme；crystal twinning。',
 'twinning 强调配对、对应过程，cloning 克隆是另一种机制和概念。把两座城结成伙伴不表示它们规模、制度全相同。',
 ('The schools joined a town-twinning programme.','这些学校参与了友好城镇项目。'),('They laughed about twinning when they arrived in matching jackets.','两人穿着相配的夹克到场，笑称自己像双胞胎。'))
R('B4266','两个成一组，形成孪生、匹配或结对关系','TWIN：两个相连、成对，不等于凡事完全相同','twin → twinning。',
 '从同一次出生的两人，到建筑、城镇等对象的配对，保留的是成双、对应。',
 '古英语 ġetwinn、twinn → twin；加 -ing 双写 n。',
 [['人物、性质与过程','twin · twinning']],
 'twins 不一定同卵、长得一样；twin room 与 double room 通常不同。',
 'The twinning project brought students from the two towns together.\n\n结对项目把两个城镇的学生联系起来。','twin twinning')
R('B2721','命运、机遇与财富，以及遭遇坏运气','FORTUNE：落到人身上的际遇，再联系好运和财富','fortune → misfortune。',
 '说 make a fortune 重点是赚到大笔财富，说 good fortune 则偏好运；misfortune 不只是账上少了点钱。',
 '拉丁 fortūna 命运、机遇，经法语进入英语 fortune；mis- 引入坏、不利。',
 [['际遇与不幸','fortune · misfortune']],
 'fortune 可是财富或运气；misfortune 是不幸，不是财富的普通否定词。',
 'Despite the misfortune, she believed her good fortune would return.\n\n尽管遭遇不幸，她仍相信好运会回来。','fortune misfortune')
A=[['旧 awk：方向不对、倒着、不顺 → awkward','-ward 方向词尾；早期向不合适的方向'],['现代 awkward','笨拙、不便处理；社交尴尬、不自在']]
W('awkward','英 /ˈɔːkwəd/；美 /ˈɔːkwərd/，也读 /ˈɑːkwərd/','笨拙的；难处理的、不方便的；尴尬的',
 '动作不顺手，局面不好处理，两个人待着又不知说什么，都有一种不顺、不自在的 awkward 感。它不只等于社恐。',
 '旧 awk 倒着、方向不对、笨拙 + -ward 方向词尾，中古英语已有 aukeward 向错误方向等用法。这里 ward 不是病房。',A,
 'an awkward movement 笨拙动作，an awkward question 难回答的问题，an awkward silence 尴尬的沉默，an awkward time 不方便的时间。',
 'an awkward movement；an awkward question；an awkward silence。',
 'awkward 可以形容物件难搬、时间不便、问题难答；embarrassed 更直接说某人感到窘迫，不覆盖这些全部语境。',
 ('There was an awkward silence after the joke.','笑话说完后，出现了一阵尴尬的沉默。'),('The box is an awkward shape to carry.','箱子形状别扭，不好搬。'))
W('awkwardly','英 /ˈɔːkwədli/；美 /ˈɔːkwərdli/','笨拙地；尴尬、不自在地；不便地',
 'awkward 说状态、性质，awkwardly 则说动作如何进行、物件怎样摆放：不顺手、不自然或让人不好处理。',
 'awkward + -ly，形成副词；k 发音，w 与后半连起来，不把 awk 当作没有辅音的空白。',A+[['awkward + -ly → awkwardly','以不顺、笨拙、尴尬或不便的方式']],
 'smile awkwardly 尴尬地笑，move awkwardly 动作笨拙，awkwardly placed 摆在不便位置。',
 'smile awkwardly；move awkwardly；awkwardly placed。',
 'awkwardly placed chair 是位置不方便的椅子，不是椅子心里尴尬。方式词仍随所修饰对象改变理解。',
 ('He smiled awkwardly and changed the subject.','他尴尬地笑了笑，换了话题。'),('The desk was awkwardly placed behind the door.','书桌放在门后，位置很不方便。'))
W('awkwardness','英 /ˈɔːkwədnəs/；美 /ˈɔːkwərdnəs/','笨拙；尴尬、不自在；难处理的性质',
 '把场面里的不自然、动作里的不协调当作一种状态来谈，就是 awkwardness。它不是天生给某类人贴的固定标签。',
 'awkward + -ness，性质、状态名词。保留 awkward 多条常用意义，不只剩社交场面这一条。',A+[['awkward + -ness → awkwardness','不协调、尴尬或难处理的状态']],
 'a sense of awkwardness 尴尬感，ease the awkwardness 缓解尴尬，the awkwardness of the shape 形状不便处理的性质。',
 'a sense of awkwardness；ease the awkwardness。',
 'awkwardness 是性质、感受，不是 awkward 的人物名词；clumsiness 更常突出动作笨拙，未必是社交气氛。',
 ('A friendly question eased the awkwardness.','一个友好的问题缓解了尴尬。'),('The awkwardness of the shape made the package difficult to carry.','包裹形状别扭，搬起来很不方便。'))
R('B3793','从方向不顺到动作、物件、时间和社交的不顺或不自在','AWKWARD：不顺手、不自然、不好处理，随对象理解','awkward → awkwardly、awkwardness。',
 '别只背尴尬。搬箱子、安排时间、回答难题，都能触发 awkward 的不同常用含义。',
 'awk 的倒向、不顺概念 + -ward 方向；-ly 副词，-ness 状态名词。',
 [['性质、方式与状态','awkward · awkwardly · awkwardness']],
 'awkward 不只是人害羞；awkwardly placed 可直接说位置不方便。',
 'He smiled awkwardly, but a friendly greeting soon eased the awkwardness.\n\n他尴尬地笑了笑，但友好的招呼很快缓解了不自在。','awkward awkwardly awkwardness')
if __name__=='__main__':save('continuation_20261030_jk',ROOTS,WORDS)
