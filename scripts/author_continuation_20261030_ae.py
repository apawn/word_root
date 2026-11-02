"""Drop, clean and kid: everyday words with useful historical contrasts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
DR=[['古英语 dropa〔名词〕及相关动词 → 中古英语 droppe','一滴；落下、滴下'],['英语 drop','滴、下降 → 放下、丢掉、退出、投放']]
def DH(f,m):return DR+[[f,m]]
W('drop','英 /drɒp/；美 /drɑːp/','滴；下降；落下、放下；停止、退出',
 '一滴水往下落，东西从手里掉下，数值也可以掉下；再引申成把某件事放下不做。',
 '继承古英语表示滴的名词与滴落相关动词，经中古英语延续。现代物理下降、数量减少和停止参与等义并存。',DR,
 'a drop of water 一滴水，drop a glass 失手掉落杯子，a drop in price 降价，drop the subject 不再谈这个话题。',
 'a drop of；a drop in；drop the subject；drop out。',
 'drop 可不及物也可及物：Prices dropped 价格下降，They dropped prices 他们降价。fall 通常不这样直接接被降的宾语。',
 ('A drop of water fell onto the page.','一滴水落在书页上。'),('The temperature dropped sharply after sunset.','日落后气温骤降。'))
W('droplet','英 /ˈdrɒplət/；美 /ˈdrɑːplət/','小滴；微滴',
 '比普通说一滴更强调细小，雾气、喷雾或玻璃上细细的水珠都能这样说。',
 'drop + -let，-let 表小，是清楚的小称派生。t 不双写成 dropplet。',DH('drop + -let → droplet','小的一滴 → 微滴'),
 'water droplets 小水滴，tiny droplets 微小液滴，droplets on glass 玻璃上的水珠。',
 'water droplets；tiny droplets；droplets on the glass。',
 'droplet 是具体液滴，mist 雾是许多微小水滴等形成的整体状态；不用因小就把它当水蒸气分子。',
 ('Tiny droplets covered the window.','细小水珠布满窗户。'),('The spray broke the liquid into fine droplets.','喷雾把液体分散成细小液滴。'))
W('dropper','英 /ˈdrɒpə/；美 /ˈdrɑːpər/','滴管；滴液器；放落某物者',
 '吸进一点液体，再一滴一滴放出来的小器具，实验、美术等场景都常见。',
 'drop + -er，双写 p；工具名按能放出液滴的作用命名。别的语境也可说丢下某物的人或投放程序。',DH('drop + -er → dropper','放出液滴的器具；做放落动作的主体'),
 'a glass dropper 玻璃滴管，a bottle with a dropper 带滴管的瓶子。最日常的实物义是按滴放液体的工具。',
 'a glass dropper；a bottle with a dropper；use a dropper。',
 'droplet 是小滴本身，dropper 是放滴的工具；同是 drop 后接不同后缀，物和工具不能混。',
 ('She used a dropper to add colour to the water.','她用滴管往水里加入颜色。'),('The bottle comes with a small glass dropper.','瓶子配有一支小玻璃滴管。'))
W('raindrop','英 /ˈreɪndrɒp/；美 /ˈreɪndrɑːp/','雨滴',
 '从天空落下的雨里，取出一滴来看，就是 raindrop。',
 'rain + drop，古英语已有 reġndropa 等同族组合，经中古英语延续。不是现代天气学才临时新造。',DH('古英语 reġndropa → raindrop','一滴雨水，rain + drop 的旧组合'),
 'raindrops on the window 窗上雨滴，heavy raindrops 大雨点，the first raindrop 第一滴雨。',
 'raindrops on the window；heavy raindrops；falling raindrops。',
 'raindrop 一滴可数，rain 通常作雨的不可数总称；a rain 在其他结构中可能说一场雨，不能拿来总替代雨滴。',
 ('The first raindrops landed on the pavement.','最初几滴雨落在人行道上。'),('She watched raindrops slide down the glass.','她看着雨滴沿玻璃滑下。'))
W('dropbox','英 /ˈdrɒpbɒks/；美 /ˈdrɑːpbɑːks/','投递箱；文件投递文件夹',
 '一个人把东西放进去，另一个人稍后来取；网络里的投递文件夹也借这个交接画面。',
 'drop 放入、投放 + box 箱；由实物投递箱扩展到共享、接收文件的容器。Dropbox 大写另是品牌名。',DH('drop + box → dropbox','投放物品的箱 → 数字文件投递位置'),
 'a book return dropbox 图书归还箱，an assignment dropbox 作业提交文件夹。先分普通词义与具体产品名。',
 'a book return dropbox；an assignment dropbox；a secure dropbox。',
 'dropbox 泛指投递容器，Dropbox 是特定服务品牌；不是每一处写 dropbox 都要求打开某个品牌软件。',
 ('Return the books to the dropbox outside the library.','把书投到图书馆外的归还箱里。'),('The teacher created a dropbox for students’ assignments.','老师建了一个供学生提交作业的文件夹。'))
W('eavesdrop','英 /ˈiːvzdrɒp/；美 /ˈiːvzdrɑːp/','偷听；窃听',
 '老画面是人躲在屋檐滴水的地方，靠近窗墙，听里面不打算让自己听的谈话。',
 '早期 eavesdrop 指屋檐滴水处，eavesdropper 指站在那儿偷听的人；现代动词可能从较早人物名逆构。不能只画成 eaves + drop 当场变偷听。',
 [['古英语、英文旧 eavesdrop〔屋檐滴水处〕→ eavesdropper','站在屋檐近处听别人谈话的人'],['eavesdropper → 动词 eavesdrop〔可能逆构〕','偷听他人非公开谈话']],
 'eavesdrop on a conversation 偷听谈话，eavesdrop on someone 偷听某人。今天不必真站在屋檐下。',
 'eavesdrop on；eavesdrop on a conversation；accidentally overhear。',
 'eavesdrop 常有主动偷听意味，overhear 可只是无意听见。eaves 是屋檐，不是 evenings 夜晚的缩写。',
 ('He realized that someone was eavesdropping on their conversation.','他意识到有人在偷听他们的谈话。'),('She moved away because she did not want to eavesdrop.','她走开了，因为不想偷听。'),sources=['https://www.etymonline.com/word/eavesdrop','https://en.wiktionary.org/wiki/eavesdrop#English'])
R('B3633','液滴、下降、投放与屋檐偷听的历史','DROP：一滴落下；后部和前部改变对象、大小与功能','drop → droplet、dropper；雨滴和投递箱相邻，eavesdrop 则说明旧场所到人物再到动词的历史。',
 '本族滴、滴落词发展出下降和放下等义。eavesdrop 有屋檐滴水处的旧名词背景，不能只用现代词面硬猜。',
 'drop + -let/-er；rain/back/tear/air + drop；drop + box/ship；eavesdrop 旧场所→eavesdropper→动词。',
 [['基本动作、微滴与工具','drop · droplet · dropper'],['自然滴落与投递','raindrop · teardrop · dropbox · airdrop · dropship'],['背景与历史延伸','backdrop · eavesdrop']],
 'drop 可及物或不及物；droplet 液滴、dropper 工具；eavesdrop 主动偷听与 overhear 无意听见。',
 'Raindrops fell from the eaves while someone eavesdropped below.\n\n雨滴从屋檐落下，下面有人正在偷听。',
 'drop droplet dropper raindrop teardrop dropbox airdrop dropship backdrop eavesdrop')
CL=[['古英语 clǣne → 中古英语 clene','干净、纯净、清楚'],['现代 clean','干净；使干净；无杂乱、清楚利落等延伸']]
def CH(f,m):return CL+[[f,m]]
W('clean','/kliːn/','干净的；清洁；利落、无杂乱的；完全〔部分搭配〕',
 '把不该有的污物、杂乱拿走，表面干净，画面和做法也可以清楚利落。',
 '继承古英语 clǣne，较早就有洁净、纯净等义。动词 clean 由使干净发展，不能只因与 clear 相近就说两者同一个现代词。',CL,
 'clean clothes 干净衣服，clean the room 打扫房间，clean design 简洁设计，come clean 坦白说实话。',
 'clean clothes；clean the room；a clean design；come clean。',
 'clean 常说无污物、无杂乱；clear 常说透明、清晰或没有阻挡。a clean window 可干净，但玻璃本身未必透明。',
 ('Please leave the kitchen clean after using it.','用完厨房后请保持干净。'),('We cleaned the room before the guests arrived.','客人到来前，我们打扫了房间。'),sources=['https://www.etymonline.com/word/clean','https://en.wiktionary.org/wiki/clean#English'])
W('cleaner','英 /ˈkliːnə/；美 /ˈkliːnər/','清洁工；清洁器、清洁剂；更干净的',
 '可以是做清洁的人、工具、清洁液；也可能只是两样东西比较，一个更干净。',
 '人物、工具名来自 clean 动词 + -er；形容词比较级另是 clean + 比较级 -er。两个后缀写得一样，功能不同。',CH('clean + 人物工具 -er；clean + 比较级 -er','清洁主体；更干净的性质'),
 'a window cleaner 擦窗工或玻璃清洁剂，a vacuum cleaner 吸尘器；a cleaner room 更干净的房间。',
 'a window cleaner；a vacuum cleaner；a cleaner room。',
 '比较级 cleaner 不是清洁工：The room is cleaner。a cleaner 则通常名词，结合上下文分人、工具、试剂。',
 ('The cleaner arrives before the office opens.','清洁工在办公室开门前到。'),('This cleaner removes marks from glass.','这种清洁剂能去掉玻璃上的污迹。'))
W('unclean','/ʌnˈkliːn/','不干净的；不洁的〔也可宗教礼仪用语〕',
 'un- 把干净否定掉；日常可以说脏，宗教文字有时说不符合礼仪上的洁净要求。',
 '接古英语 unclǣne，经中古英语延续，对应 un- + clean。礼仪、道德等意义是旧用法，不都等于表面灰尘多。',CL[:1]+[['古英语 un- + clǣne → unclean','不洁净；礼仪上的不洁']],
 'unclean water 不洁水，unclean conditions 不洁环境；ritually unclean 礼仪上不洁，需要放在相应传统语境理解。',
 'unclean water；unclean conditions；ritually unclean。',
 'unclean 词义较宽，日常 dirty 更直接说脏；宗教叙述里的 unclean 不应随意推成对现实人群的评价。',
 ('The inspection found unclean conditions in the storeroom.','检查发现储藏室环境不洁。'),('The text explains what the tradition considered ritually unclean.','文本解释了该传统认为哪些情况在礼仪上不洁。'))
W('cleanly','/ˈkliːnli/〔副词〕；/ˈklenli/〔形容词〕','干净利落地；整齐地；爱洁净的〔较少用形容词〕',
 '一刀切得整齐、一次动作没有多余拖带，是 cleanly；较少见的形容词则说爱干净。',
 'clean + -ly，古英语已有相应形容词、副词。现代词性有读音差异：常用副词长 /iː/，较少见形容词短 /e/。',CL+[['clean + -ly → cleanly','干净、利落的方式；另有爱洁净的形容词']],
 'cut cleanly 切得干净利落，break cleanly 断得整齐，play cleanly 比赛动作干净。',
 'cut cleanly；break cleanly；play cleanly。',
 'cleanly 干净利落地，cleaner 可能更干净或清洁工；-ly、-er 要按词性，不能只记中文一个干净。',
 ('The blade cut cleanly through the paper.','刀片干净利落地切开了纸。'),('The branch broke cleanly at the joint.','树枝在连接处整齐地断开了。'))
W('cleantech','/ˈkliːntek/','清洁技术',
 '把减少污染、节约资源或提高能源效率等目标放进技术里，是一个行业总称。',
 'clean + tech，tech 是 technology 的缩略。clean 在此说环境影响取向，不是只研究怎样擦桌子。',CL+[['clean + tech〔technology 缩略〕→ cleantech','减少环境负担、改善资源效率的技术总称']],
 'cleantech companies 清洁技术企业，cleantech investment 清洁技术领域投资。具体是哪种技术仍需另外说明。',
 'cleantech companies；cleantech investment；a cleantech project。',
 'cleantech 是宽泛行业名称，不代表所有项目无任何影响；cleaning technology 清洗技术的范围则不同。',
 ('The exhibition features several cleantech companies.','展览有几家清洁技术企业参展。'),('Her research focuses on cleantech for industrial water use.','她研究工业用水相关的清洁技术。'))
R('B3030','干净、清洁主体与方式；环境技术','CLEAN：去掉污物杂乱；不同后缀说人、工具、程度或方式','clean → cleaner、unclean、cleanly，再接 clean + tech 的现代行业词。品牌词暂略。',
 '古英语洁净词延续至今，人物 -er 与比较级 -er 同形；cleanly 还有词性对应的元音差异。',
 'clean + -er〔工具人物／比较级〕；un- + clean；clean + -ly；clean + tech。',
 [['基本清洁与主体','clean · cleaner'],['否定与方式','unclean · cleanly'],['现代行业','cleantech']],
 'cleaner 可清洁工、剂、器具或比较级；cleanly 副词长元音；cleantech 不是只说擦洗技术。',
 'The cleaner left the windows clean and the room much cleaner.\n\n清洁工把窗户擦干净，也让房间干净了许多。',
 'clean cleaner unclean cleanly cleantech')
KI=[['古诺尔斯语 kið → 中古英语 kide → kid','小山羊'],['现代 kid','小孩的口语称呼；另有开玩笑、逗弄的动词用法']]
W('kid','/kɪd/','小孩；小山羊；开玩笑、逗弄',
 '最早叫小山羊，后来成了叫孩子的日常口语；I’m kidding 则是“我开玩笑的”。',
 '借古诺尔斯语 kið 小山羊。小孩义后来普及，动词开玩笑也在后来的口语中固定下来，不用小羊顽皮的故事充当确定词源。',KI,
 'the kids 孩子们，a young kid 小孩子，a baby goat is a kid，小山羊也叫 kid；You’re kidding! 你开玩笑吧！',
 'the kids；a kid at school；I’m kidding；You’re kidding!。',
 'kid 口语，child 更中性；kid 的动词不是把人变成孩子。开玩笑这个意思通常用进行式 I’m kidding。',
 ('The kids are playing in the garden.','孩子们在花园玩。'),('Do not worry—I am only kidding.','别担心，我只是开玩笑。'))
W('kiddo','英 /ˈkɪdəʊ/；美 /ˈkɪdoʊ/','小家伙；孩子〔亲昵口语称呼〕',
 '像对熟悉的孩子说一声“小家伙”，有亲近、鼓励的味道；也可能同辈打趣。',
 'kid + -o，-o 在这里构成亲昵、口语人物称呼，双写 d。',KI+[['kid + -o → kiddo','孩子、朋友的亲昵称呼']],
 'Hey, kiddo! 嗨，小家伙，Good job, kiddo! 干得好，小家伙。是否亲近或居高临下取决于关系和语气。',
 'Hey, kiddo!；Good job, kiddo!；listen, kiddo。',
 'kiddo 通常直接称呼更自然，正式报告里写 children 更合适；不与 kidnap 的后部混为一谈。',
 ('“Good morning, kiddo,” her grandfather said.','爷爷说：“早上好，小家伙。”'),('You did a great job, kiddo.','小家伙，你做得很棒。'))
W('kiddie','/ˈkɪdi/','小孩〔亲昵口语〕；儿童用的〔作修饰语〕',
 '不仅可以叫孩子，也常给小孩专用的东西贴上一个轻松标签，比如浅浅的儿童戏水池。',
 'kid + 亲昵小称 -ie，双写 d；另有 kiddy 拼写。这里不表示更小的山羊才是唯一意思。',KI+[['kid + -ie → kiddie','小孩；供儿童使用的']],
 'a kiddie pool 儿童戏水池，a kiddie ride 儿童游乐设施；kiddies 可亲昵说孩子们。',
 'a kiddie pool；a kiddie ride；the kiddies。',
 'kiddie 常口语、亲昵或有童趣，children’s 在正式、中性描述里更通用。',
 ('The children splashed in the kiddie pool.','孩子们在儿童戏水池里玩水。'),('The park has a small area of kiddie rides.','公园有一小片儿童游乐设施区。'))
W('kidnap','/ˈkɪdnæp/','绑架；劫持',
 '把人强行带走或藏起来，不限对象是小孩；今天这个词也用于成年人。',
 'kid 小孩 + nap 的旧抓走义，后者与 nab 相近，不是打盹。早期联系拐走儿童充作劳工；动词也可能由更早出现的 kidnapper 逆构。',KI+[['kid〔小孩〕+ nap〔抓走〕；较早 kidnapper 与动词形成相关','拐走儿童的旧称 → 现代绑架任何年龄的人']],
 'be kidnapped 遭绑架，a kidnapped passenger 被劫持乘客。过去式 kidnapped、-ing 为 kidnapping，双写 p。',
 'be kidnapped；a kidnapped passenger；a kidnapping case。',
 'kidnap 不只绑儿童；nap 这里不是让孩子小睡。今天讲绑架，应看强行控制、带走等完整语境。',
 ('The novel begins with a businessman being kidnapped.','小说以一名商人遭绑架开场。'),('The missing passenger had been kidnapped.','失踪乘客遭到了绑架。'),sources=['https://www.etymonline.com/word/kidnap','https://en.wiktionary.org/wiki/kidnap#English'])
R('B3555','小山羊到孩子口语；亲昵称呼与绑架旧称','KID：孩子口语有小山羊历史，后部各有作用','kid 先讲小羊、孩子与玩笑；kiddo、kiddie 亲昵，kidnap 的 nap 必须按旧抓走义。',
 '借古诺尔斯语小山羊名，再发展出小孩口语。kidnap 不是小孩打盹，也不是今天只用于儿童。较冷的 kidder 先略。',
 'kid + -o/-ie → kiddo/kiddie；kid + nap〔抓走〕，kidnapper 与动词逆构关系保留可能性。',
 [['基础与亲昵','kid · kiddo · kiddie'],['旧组合的现代词','kidnap']],
 'I’m kidding 开玩笑；kiddo 与 kiddie 有口语语气；kidnap 的 nap 不打盹，对象不限儿童。',
 'The kid was only kidding when he said the cake had disappeared.\n\n孩子说蛋糕不见了，其实只是在开玩笑。',
 'kid kiddo kiddie kidnap')
if __name__=='__main__':save('continuation_20261030_ae',ROOTS,WORDS)
