"""More high-frequency verb forms, including strong verbs and spelling contrasts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3202':dict(words=['link','linked'],label='link → linked：连接与相互关联',note='链环词族发展，现代连接不只实体器件。'),
 'C1097':dict(words=['expose','exposed'],label='expose → exposed：摆在外面与显露、暴露',note='法语词形受 poser 影响而重塑，不把它当拉丁 ponere 的原样延续。'),
 'C0627':dict(words=['injure','injured'],label='injure → injured：受伤、受损与分词状态',note='injure 可能从 injury 反构，也可能经法语动词借入；较早同接不公、侵害的拉丁词族。'),
 'B3365':dict(words=['tie','tied'],label='tie → tied：系住、关联与平局',note='本族绳带和系结动词汇入现代词，分数相同是另一现代用法。'),
 'C1487':dict(words=['contain','contained'],label='contain → contained：装在里面与控制住',note='拉丁保持在一起词族经法语借入，内容、边界、控制各看对象。'),
 'A1741':dict(words=['draw','drew'],label='draw → drew：拉动、画出与得出',note='本族不规则过去式，drew 不是在 draw 后拼一个通用 ew 后缀。'),
 'B3724':dict(words=['try','tries'],label='try → tries：尝试、检验与多次努力',note='法语挑选、检验词借入，现代名动词形式有对应变化。'),
 'B2889':dict(words=['let','lets','letting'],label='let → lets → letting：允许、出租与让事情发生',note='普通允许支接古英语 laetan；阻碍、球类重发等另一支不混入本组。'),
 'C0478':dict(words=['suggest','suggests'],label='suggest → suggests：带到面前与建议、暗示',note='拉丁带来词族的分词材料借入，建议并非每次都是直接命令。'),
 'C1353':dict(words=['exist','exists'],label='exist → exists：出现、站出来与存在',note='拉丁站定词族经法语等借入，现代表示有这样的人或事。'),
 'B3774':dict(words=['represent','represents','represented'],label='represent → represents → represented：呈现与代表',note='相关法语、拉丁呈现词族借入，现代第三人称单数与过去形式相邻。'),
 'B2878':dict(words=['hit','hits','hitting'],label='hit → hits → hitting：击中与双写 t',note='本族借入的击中词，过去仍是 hit，ing 则双写 t。'),
 'C0401':dict(words=['feature','featuring'],label='feature → featuring：特征与作为特色呈现',note='拉丁形成词经法语成为外貌、显著部分名词，英语再有突出展示的动词。'),
}
W('linked','/lɪŋkt/','连接、联系〔过去式、过去分词〕；相连、有关联的',
 '像一环扣住另一环，两件事被接起来，就是 linked；可以连着线，也可以通过证据、意义等建立关联。',
 'link + -ed，/k/ 后读 /t/。link 的中古英语链环词通常联系北欧来源；现代动词、分词沿连接意义扩展。',
 [['中古英语链环词 → link','链环、接合 → 连接与联系'],['link + -ed → linked','连接了；处于有关联、相连的状态']],
 'linked together 连在一起；linked to 与……相连；closely linked 紧密相关。',
 'linked by a bridge；linked through shared information。','linked to 可以是物理连接，也可说统计、叙述或其他关系。读到有关联时，仍要看句子具体说的是怎样一种联系。',
 ('The two buildings are linked by a covered walkway.','两栋建筑由一条有顶走道连接。'),('The report linked the delay to a shortage of materials.','报告把延误与材料短缺联系起来。'),sources=['https://en.wiktionary.org/wiki/linked#English','https://en.wiktionary.org/wiki/link#English'])
W('exposed','英 /ɪkˈspəʊzd/；美 /ɪkˈspoʊzd/','显露、揭露；使暴露于〔过去式、过去分词〕；无遮蔽的',
 '原来遮住、藏住的东西被摆到外面，是 exposed；事实被看见是揭露，东西直接接触风雨等是暴露。',
 'expose 已有 e，加 -d，/z/ 后读 /d/。古法语 exposer 等对应拉丁 expōnere 摆在外面，但法语形式受 poser 放置〔较早接 pausāre〕替换影响，再借入英语。',
 [['拉丁 expōnere 的意义材料；法语 poser 影响 → exposer → expose','放到外面 → 摆开、显露、失去遮蔽'],['expose 去 e + -ed → exposed','揭露过；暴露、无遮蔽的状态']],
 'exposed the error 揭露错误；exposed to rain 暴露在雨中；exposed beams 外露的梁。',
 'exposed by the investigation；left exposed to the weather。','be exposed to something 说明暴露、接触到什么环境或内容；exposed an error 则直接说让错误显出来。两者共享从遮蔽到可接触、可看见的画面。',
 ('The investigation exposed errors in the report.','调查揭露了报告中的错误。'),('The equipment was exposed to the rain.','这些设备无遮蔽地淋在雨中。'),sources=['https://en.wiktionary.org/wiki/exposed#English','https://www.etymonline.com/word/expose'])
W('injured','英 /ˈɪndʒəd/；美 /ˈɪndʒərd/','使受伤、损害〔过去式、过去分词〕；受伤的',
 '身体或某种利益受到了损伤，是 injured；说 an injured player，画面就是已经受伤的队员。',
 'injure 已有 e，加 -d，词尾读 /d/。injure 可能由英语 injury 反构，也可能经古法语 injuriier 等动词借入；较早接拉丁 iniūria 不公、侵害，含 in- 不与 iūs 权利、公道。',
 [['拉丁 iniūria → 法语名词、动词相关形式 → injury、injure','不公、侵害 → 伤害；英语动词路线有不同分析'],['injure 去 e + -ed → injured','受到了伤害；分词作受伤状态形容词']],
 'an injured player 受伤队员；injured in the accident 在事故中受伤；seriously injured 严重受伤的。',
 'injured while moving furniture；helping an injured bird。','injured 常突出已经发生的损伤；hurt 还可直接说疼、感情受伤。injured people 是受伤的人，the injured 也可集合地指受伤者。',
 ('The injured player left the field.','受伤队员离开了赛场。'),('She found an injured bird beside the path.','她在路旁发现一只受伤的鸟。'),sources=['https://en.wiktionary.org/wiki/injured#English','https://www.etymonline.com/word/injure'])
W('tied','/taɪd/','系、捆；关联〔过去式、过去分词〕；分数相同、并列的',
 '绳带把两处固定在一起，是 tied 的具体画面；关系紧连、成绩并列也可用 tied，意思由对象决定。',
 'tie 已有 e，加 -d → tied，/aɪ/ 后读 /d/，整体一个音节。绳带名词与系结动词各有古英语形式，后来汇入 tie；现代关系、平局等用途分别发展。',
 [['古英语绳带名词、系结动词 → tie','把东西接牢、固定'],['tie 去 e + -ed → tied；关系和成绩用途','系好了；受关联限制；比分并列']],
 'tied the rope 系绳；tied to 与……紧连；tied for first 并列第一；the scores are tied 比分相同。',
 'tied to the fence；tied at the end of the game。','tied to something 在抽象语境可说结果与某条件紧连。tied for first 是共同占据第一名，the scores were tied 是比分相同。',
 ('She tied the rope to the wooden post.','她把绳子系在木柱上。'),('The two teams were tied at the end of the game.','比赛结束时，两队打成平局。'),sources=['https://en.wiktionary.org/wiki/tied#English','https://en.wiktionary.org/wiki/tie#English'])
W('contained','/kənˈteɪnd/','含有、容纳；控制住〔过去式、过去分词〕',
 '把东西保持在一个范围里面，是 contained；箱子含有什么、影响被限制到哪里，都可沿边界把握住的画面理解。',
 'contain + -ed，/n/ 后读 /d/。拉丁 con- 与 tenēre 保持形成 continēre，经古法语 contenir 进入英语；范围内保持的意义又发展到控制扩散。',
 [['拉丁 continēre → 古法语 contenir → contain','保持在一起、保持在范围内 → 容纳、限制'],['contain + -ed → contained','含有过；已被控制在范围内']],
 'contained the documents 装着文件；contained in the report 包含在报告里；contained within 限于某范围。',
 'contained in one folder；contained the spread of the problem。','contained something 可以描述原来就装着什么；was contained 也可说问题已控制住。主语和宾语决定是在数内容，还是描述边界控制。',
 ('The box contained old letters and photographs.','箱子里装着旧信和照片。'),('The problem was contained within one small part of the system.','问题被控制在系统的一小部分之内。'),sources=['https://en.wiktionary.org/wiki/contained#English','https://en.wiktionary.org/wiki/contain#English'])
W('drew','/druː/','拉、拖；画；吸引；得出〔draw 的过去式〕',
 '把东西朝某个方向拉，是 drew 的老动作；笔拉出线条能画图，注意力被拉过来是吸引，思路走向结果是得出。',
 'draw 的不规则过去式是 drew，过去分词 drawn，现代不能拆成 draw + ew。draw 接古英语 dragan，经后期古英语、中古英语形式发展，与 drag 有历史亲缘。',
 [['古英语 dragan → draw','拉动 → 拉出线条、画；吸引等意义'],['draw → drew；分词 drawn','旧强变化词族的现代过去式，不是通用后缀']],
 'drew a picture 画画；drew the curtains 拉窗帘；drew attention 引起注意；drew a conclusion 得出结论。',
 'drew a line；drew people to the exhibition。','drew 是过去式，have、had 等结构后通常用 drawn。drew a conclusion 回到把理由推进、带到最后判断的抽象用法。',
 ('She drew a map to show us the route.','她画了一张地图，给我们说明路线。'),('The exhibition drew visitors from nearby towns.','这个展览吸引了附近城镇的访客。'),sources=['https://en.wiktionary.org/wiki/drew#English','https://en.wiktionary.org/wiki/draw#English'])
W('tries','/traɪz/','尝试〔复数〕；尝试、试用〔第三人称单数〕',
 '为了看看能不能成而做一次，是 a try，多次是 tries；他、她反复试着做，也用动词 tries。',
 'try 的 y 前是辅音 r，变 y 为 i 加 -es，但读 /z/，不增加音节。try 经法语 trier 与中古英语 trien 等，较早有挑选、检验义，更远来源未定。',
 [['法语 trier → 中古英语 trien → try','挑选、检验 → 尝试'],['try → tries','y 变 i 加 es；多次尝试或单数主语试着做']],
 'after several tries 尝试几次之后；tries to help 努力帮忙；tries a new method 试用新方法。',
 'tries again；tries different ways of solving it。','tries to do 常强调努力做，tries doing 常可说试用某个办法。tries 作复数名词时，一次次尝试可以数出来。',
 ('The lock opened after several tries.','尝试几次后，锁打开了。'),('She tries to explain each idea with a simple example.','她尽量用一个简单例子解释每个想法。'),sources=['https://en.wiktionary.org/wiki/tries#English','https://en.wiktionary.org/wiki/try#English'])
W('lets','/lets/','让、允许；出租〔let 的第三人称单数〕',
 '留出一个空当、不把事情挡住，让别人去做，是 lets 的允许义；把房间交给别人租用，也用 let。',
 'let + -s，/t/ 后读 /s/。允许、出租的 let 继承古英语 lǣtan；另一个阻碍义旧词 lettan 后有球类 let 等用途，本组先分清普通允许支。',
 [['古英语 lǣtan → let','让去、允许；出租等用途'],['let + -s → lets','单数主语让、允许或出租']],
 'lets us in 让我们进去；lets her use the room 允许她用房间；lets a room 出租房间〔英式常见〕。',
 'lets children choose；lets the light through。','lets somebody do something 中 do 通常不带 to。lets 与 let’s 拼写不同，let’s 是 let us 的缩写，常用来提出一起做某事。',
 ('The teacher lets students choose their own examples.','老师让学生自己选例子。'),('The large window lets more light into the room.','大窗户让更多光线进入房间。'),sources=['https://en.wiktionary.org/wiki/lets#English','https://en.wiktionary.org/wiki/let#English'])
W('suggests','/səˈdʒests/；亦有 /səɡˈdʒests/','建议；暗示、表明〔suggest 的第三人称单数〕',
 '把一个想法递到别人面前，是 suggests 的建议义；证据像把一种解释递过来，也能说 suggests，表示让人推想到。',
 'suggest + -s，/t/ 后读 /s/。拉丁 sub- 在 g 前变为 sug-，与 gerere 带来形成 suggerere，分词 suggestus 借入英语；实际读音可有 /ɡ/ 是否读出的差别。',
 [['拉丁 sub- + gerere → suggerere、suggestus → suggest','从下带上、带来 → 提出想法'],['suggest + -s → suggests','单数主语建议；证据显示某种可能']],
 'suggests a plan 提议方案；suggests doing something 建议做；suggests that... 建议、表明……。',
 'suggests a different approach；the evidence suggests...。','suggests doing 是常用建议结构；suggests that... 要看主语，人物可以提出建议，证据、结果则常表明一种解释。',
 ('She suggests using a larger table.','她建议用一张更大的桌子。'),('The evidence suggests that the building was once a school.','证据表明，这座建筑以前可能是一所学校。'),sources=['https://en.wiktionary.org/wiki/suggests#English','https://en.wiktionary.org/wiki/suggest#English'])
W('exists','/ɪɡˈzɪsts/','存在；存活〔exist 的第三人称单数〕',
 '确实有这样一个人、东西或情况，就是 exists。词源里出现、站出来的画面，可以帮助你从看得见的出现走到抽象的存在。',
 'exist + -s，/t/ 后读 /s/。拉丁 ex- 向外与 sistere 站定形成 exsistere 出现，经法语等路线进入英语，后来存在义成为重点。',
 [['拉丁 ex- + sistere → exsistere → 法语等 → exist','站出来、出现 → 存在'],['exist + -s → exists','单数主语存在、存活']],
 'still exists 仍然存在；exists in several forms 以几种形式存在；a link exists 存在联系。',
 'a copy still exists；exists only in memory。','exists 通常不直接接宾语，说明哪里存在可以接 in 等短语。There exists... 是较正式的有、存在表达。',
 ('A copy of the original map still exists.','原地图的一份副本仍然存在。'),('The problem exists in several parts of the system.','这个问题存在于系统的几个部分。'),sources=['https://en.wiktionary.org/wiki/exists#English','https://en.wiktionary.org/wiki/exist#English'])
W('represents','/ˌreprɪˈzents/','代表；表示、描绘；构成〔represent 的第三人称单数〕',
 '让一个人、图形或数字替另一件事呈现出来，是 represents；代表团队、图上表示地点、数字构成比例，都有各自搭配。',
 'represent + -s，/t/ 后读 /s/。法语 représenter 接拉丁 repraesentāre 展现、使呈现，与 present 的在场、呈现词族相关；现代代表义不能逐次硬译成再呈交。',
 [['拉丁 repraesentāre → 法语 → represent','使呈现 → 代表、表现、表示'],['represent + -s → represents','单数主语代表、表示或构成']],
 'represents the team 代表团队；represents a village 表示村庄；represents a change 构成一种变化。',
 'the symbol represents...；represents the group in meetings。','represents somebody 可以是代理、代表；represents something 也可说图示、数字代表什么。看主语是人、符号还是事件，中文就容易选。',
 ('Each dot represents a village on the map.','地图上每个圆点表示一个村庄。'),('She represents the team at the weekly meeting.','她代表团队参加每周会议。'),sources=['https://en.wiktionary.org/wiki/represents#English','https://en.wiktionary.org/wiki/represent#English'])
W('letting','/ˈletɪŋ/','让、允许；出租〔现在分词、动名词〕；租赁安排〔英式名词用法〕',
 '不拦住、让事情发生，是 letting；房间让别人租用，也叫 letting。它可以说一个正在进行的动作，也能谈出租这项业务。',
 'let 为重读短词，双写 t 加 -ing → letting。允许、出租义继承古英语 lǣtan，英语现在分词再可作动作名词；球类阻碍、重发的另一 let 分开。',
 [['古英语 lǣtan → let','允许、让；出租'],['let → letting','双写 t 加 ing；允许、出租的过程或安排']],
 'letting people choose 让人自己选；letting go 放手；letting a room 出租房间；letting agents 租赁代理〔英式常见〕。',
 'letting the visitors in；letting a room to a student。','letting somebody do 中动词不带 to；letting a room to somebody 的 to 引出承租人。let 的过去式、分词仍是 let，ing 形式才双写 t。',
 ('Letting students explain their ideas helped the discussion.','让学生解释自己的想法，促进了讨论。'),('He is letting a room to a student.','他正在把一间房出租给一名学生。'),sources=['https://en.wiktionary.org/wiki/letting#English','https://en.wiktionary.org/wiki/let#English'])
W('hitting','/ˈhɪtɪŋ/','击打、击中；达到、影响到〔hit 的现在分词、动名词〕',
 '动作碰上目标，是 hitting；撞上某个数字、某个困难，也能借命中的画面表达达到或受到影响。',
 'hit 是重读短词，双写 t 加 -ing → hitting。hit 有古诺尔斯语 hitta 相遇、击中背景；现代过去式、过去分词仍是 hit，ing 的双写不要套到过去式。',
 [['古诺尔斯语 hitta 等 → hit','相遇、碰到 → 击中、达到'],['hit → hitting','双写 t 加 ing；正在击中、达到']],
 'hitting the ball 击球；hitting a target 命中目标；hitting a new high 达到新高。',
 'hitting the wall；hitting the required number。','hitting 可以是实际击打，也可以是数字、水平达到某个点。hit the target 可以是打中实物，也可以是达到工作目标。',
 ('The children practised hitting the ball against a wall.','孩子们练习把球击向墙面。'),('Visitor numbers are hitting a new high this season.','这一季的游客人数正在达到新高。'),sources=['https://en.wiktionary.org/wiki/hitting#English','https://en.wiktionary.org/wiki/hit#English'])
W('featuring','英 /ˈfiːtʃərɪŋ/；美 /ˈfiːtʃərɪŋ/','以……为特色、突出展示；由……特别参与〔feature 的现在分词〕',
 '把最值得注意的人或内容摆到显眼位置，是 featuring；展览突出某类作品，歌曲请某位乐手特别参与，都常这样写。',
 'feature 去末尾 e 加 -ing → featuring。拉丁 factūra 形成、制作经古法语 faiture 发展为外貌、显著特征的 feature；英语由名词形成突出展示的动词。',
 [['拉丁 factūra → 古法语 faiture → feature 名词','形成、样貌 → 显著部分、特色'],['英语动词 feature → featuring','突出作为特色；作品中邀某人参与']],
 'an exhibition featuring local artists 以当地艺术家作品为特色的展览；a song featuring guest musicians 有客座乐手参与的歌曲。',
 'a programme featuring new writers；a film featuring young actors。','featuring 后接被突出呈现的人或内容。音乐作品里的 featuring 常介绍特邀参与者，电影、节目则可介绍主要出现的人物或演员。',
 ('The museum is hosting an exhibition featuring local artists.','博物馆正举办一个突出当地艺术家作品的展览。'),('The album includes a song featuring two guest musicians.','这张专辑收录了一首有两位客座乐手参与的歌。'),sources=['https://en.wiktionary.org/wiki/featuring#English','https://www.etymonline.com/word/feature'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yz',ROOTS,WORDS)
 extend_lessons()
