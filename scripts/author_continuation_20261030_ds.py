"""Neck: jewelry, clothing and the narrowing bottleneck; user closure."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
N=[['古英语 hnecca → 中古英语 nekke、nakke → neck','颈、脖子等；开头旧辅音群简化'],['现代形状、位置比喻','身体连接头的窄部 → 瓶颈、乐器琴颈等']]
def NH(f,m):return N[:1]+[[f,m]]
W('neck','/nek/','颈、脖子；瓶颈、琴颈等狭长连接部分',
 '头与身体之间这一段，既连接，又常比两头窄。瓶子、吉他也借这个形状叫 neck。',
 '继承古英语 hnecca，经中古英语 nekke 等到现代，开头旧 h 音不再保留；不是 new 和某个 ck 后缀拼起来。器物义按形状延伸。',N,
 'a stiff neck 脖子僵硬，the neck of a bottle 瓶颈，a guitar neck 琴颈，neck and neck 齐头并进，stick your neck out 冒风险表态或帮忙。',
 'a stiff neck；the neck of a bottle；a guitar neck；neck and neck。',
 'neck 外部脖颈，throat 常喉咙；scratch your neck 挠脖子与 a sore throat 喉咙痛不是同一位置说法。',
 ('He turned his head and stretched his neck.','他转了转头，伸展脖子。'),('The two runners were neck and neck near the finish.','临近终点时，两名跑者齐头并进。'))
W('necklace','英 /ˈneklɪs/；美 /ˈnekləs/','项链',
 '一圈挂在脖子周围的饰物。可以是金属链、珠串或绳饰，不是必须用现代蕾丝布做。',
 'neck + lace，lace 在旧义中可以是系带、绳索等；组合成颈部饰物名后，后半读弱，不照单独 lace /leɪs/ 来读。',NH('neck + lace〔系带、绳〕→ necklace','绕颈部的带状饰物 → 项链'),
 'a pearl necklace 珍珠项链，a silver necklace 银项链，wear a necklace 戴项链。',
 'a pearl necklace；a silver necklace；wear a necklace。',
 'necklace /ˈneklɪs, ˈnekləs/ 与 lace /leɪs/ 不同；necklace 饰物，necktie 服饰领带，用途不同。',
 ('She wore a simple silver necklace.','她戴着一条简洁的银项链。'),('The pearl necklace belonged to her grandmother.','那条珍珠项链原是她祖母的。'))
W('neckline','/ˈneklaɪn/','衣服领口的形状、线条、开口位置',
 '不是一根脖子上的皱纹，而是衣服绕颈、胸上方开口的那条边：开得高、低、圆、尖都能说。',
 'neck + line，按靠近颈部的衣物边线组合。line 表轮廓，不保证有一条画上去的墨线。',NH('neck + line → neckline','衣服颈部附近开口的轮廓'),
 'a low neckline 低领口，a high neckline 高领口，a round neckline 圆领口。',
 'a low neckline；a high neckline；a round neckline。',
 'neckline 是衣服开口轮廓，collar 是领子这一结构；有些衣服有 neckline 却没有翻领 collar。',
 ('The dress has a simple round neckline.','这条连衣裙是简单的圆领口。'),('She chose a top with a higher neckline.','她选了一件领口更高的上衣。'))
W('necktie','/ˈnektaɪ/','领带〔通常说长领带〕',
 '在衬衫领口绕颈、打结、垂下来的服饰；tie 是系结或系上的那件东西。',
 'neck + tie，按佩戴位置命名，和 bowtie 的结形命名对看。不是 neck 的动词时态。',NH('neck + tie → necktie','系在颈部的领带'),
 'wear a necktie 打领带，a silk necktie 丝质领带，loosen your necktie 松松领带。',
 'wear a necktie；a silk necktie；loosen your necktie。',
 'necktie 日常常指长领带，与 bowtie 领结对照；necklace 项链主要是饰物，不是一律打结垂下的领带。',
 ('He loosened his necktie after the meeting.','会议后，他松了松领带。'),('She bought him a silk necktie.','她给他买了一条丝质领带。'))
W('turtleneck','英 /ˈtɜːtlnek/；美 /ˈtɜːrtlnek/','高领；高领毛衣、上衣',
 '高高围着颈部的一圈领，头从中伸出来，让人联想到龟的头颈；也用领子的名字代指整件上衣。',
 'turtle 龟 + neck 颈，借形象命名衣领，后可指高领衣物。具体款式可翻折，也可能有其他高领形式，不把词当龟皮材质说明。',NH('turtle + neck → turtleneck','龟颈形象 → 高领及高领衣物'),
 'a black turtleneck 黑色高领上衣，a turtleneck sweater 高领毛衣，wear a turtleneck 穿高领上衣。',
 'a black turtleneck；a turtleneck sweater；wear a turtleneck。',
 'turtleneck 高领，neckline 领口轮廓；英式也常用 polo neck 描述相近款式，名称不代表真用于骑马球。',
 ('She wore a black turtleneck under her jacket.','她在外套里穿了一件黑色高领上衣。'),('The wool turtleneck kept his neck warm.','羊毛高领毛衣让他的脖子很暖和。'))
W('bottleneck','英 /ˈbɒtlnek/；美 /ˈbɑːtlnek/','瓶颈；限制整体进度、流量的环节',
 '瓶身很宽，东西倒出时都得挤过细瓶颈；流程即使别处很快，一个窄环节也能把整体卡住。',
 'bottle 瓶 + neck 颈部，先说瓶的狭窄部分，再借到交通、生产、工作流程等。不是所有小东西都自动是瓶颈，关键是限制整体通过。',NH('bottle + neck → bottleneck','瓶的窄颈 → 限制整体流动的环节'),
 'a traffic bottleneck 交通瓶颈，a production bottleneck 生产瓶颈，identify the bottleneck 找到卡点，remove a bottleneck 消除瓶颈。',
 'a traffic bottleneck；a production bottleneck；identify the bottleneck。',
 'bottleneck 强调卡住整体的环节，delay 泛指延误；一处很忙但不限制总进度，不一定就是主要瓶颈。',
 ('The narrow bridge creates a traffic bottleneck.','窄桥形成了交通瓶颈。'),('The team identified testing as the main bottleneck.','团队发现测试是主要瓶颈。'))
R('B2772','颈部、绕颈服饰与限制流动的窄部','NECK：连接两端的较窄一段，形状能借给器物和流程','neck → necklace、neckline、necktie、turtleneck；bottleneck 接窄部限制；breakneck、redneck 另看固定历史、语气。',
 '从身体位置出发，项链、领带、领口各有用途。bottleneck 不是简单有点窄，而是那个窄环节卡住了整体。',
 'hnecca → nekke → neck；neck + lace/line/tie；turtle + neck；bottle + neck；其他固定词不机械按字面套人。',
 [['基础与服饰','neck · necklace · neckline · necktie · turtleneck'],['窄部、速度与人物固定词','bottleneck · breakneck · redneck']],
 'neck/throat 脖子与喉；necklace 弱读非 lace 原读；neckline 轮廓非必有 collar；bottleneck 卡整体。',
 'She adjusted her necklace above the dress’s neckline.\n\n她在裙子的领口上方整理了项链。','neck necklace neckline necktie turtleneck bottleneck breakneck redneck')
ROOTS[-1]['exclude']['necked']='常见于带颈部特征的组合或规则动词变化，基础词与领口条已说明，本轮不另列重复词头。'
R('B3339','使用者与用户名','USER：使用某工具、服务的人，不一定是付款或管理的人','user 为基础，username 是识别账户的名称；从人物到标识相邻学习。',
 '账户名不等于真实姓名，使用者也不必是设备所有人。看产品说明时先确认系统把谁称作 user。',
 'use + -er → user；user + name → username。',
 [['人物与账户标识','user · username']],
 'user 使用者、customer 客户、owner 所有人角色可能重叠；username 与 password 用户名密码不同。',
 'The user entered a username and password.\n\n使用者输入了用户名和密码。','user username')
if __name__=='__main__':save('continuation_20261030_ds',ROOTS,WORDS)
