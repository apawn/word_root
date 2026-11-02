"""Useful independent lemmas and substantial derivatives; qualify disputed relationships."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3812':dict(words=['exploitation'],label='exploit + -ation → exploitation',note='exploitation 从法语利用、开发活动名词借入，现代可联系 exploit 与 -ation。利用资源与不公平剥削分语境。'),
 'C0401':dict(words=['horrific','horrifically'],label='horri- 毛发竖立 + -fic 使 → horrific',note='拉丁 horrere 竖起、战栗配 -ficus 使，接 facere 做、使。horrifically 是 horrific 接 -ally 的副词形式，解释完整词尾。'),
 'B4167':dict(words=['warranty'],label='warrant 保护、保证 → warranty',note='warranty 经法语 warantie 保护、担保词族，现代常见产品保证、保修义；不凭词源指定具体保修范围。'),
 'B3314':dict(words=['vegetable','vegetation','vegetate'],label='veget- 生长、有活力 → vegetable、vegetation、vegetate',note='vegetarian 的植物词基与 vegetable、vegetation、vegetate 都接拉丁 vegetare 使有活力、生长词族。先认植物，再分植物总称与闲散度日的比喻；vegetate 与 vegetation 的直接形成关系有不同可能。'),
 'C1657':dict(words=['revolt','revolting'],label='re- 回转 + volv- 滚动 → revolt',note='revolt 经法语、意大利语接拉丁 revolvere 回滚的相关材料。反抗旧秩序与转身厌恶的语义分支解释 revolting 的两类用法。'),
 'B2841':dict(words=['forthcoming'],label='forth 向前 + come 来 + -ing → forthcoming',note='承古英语 forðcuman 出来、发生的词族；coming 保留完整 -ing。即将发生与乐意提供消息等用法分场景。'),
 'B2942':dict(words=['baggage'],label='bag 包裹词族 → baggage',note='baggage 经法语 bagage、bague 包裹，通常认为与 bag 的北欧来源相关。-age 是集合性名词材料，行李与心理包袱常见。'),
 'C0285':dict(words=['cuisine'],label='厨房、烹饪词族 → cuisine',note='cuisine 经法语接拉丁 coquina、cocina 厨房，连 coquere 烹饪；culinary 的 culina 是同烹饪词族的特殊形式，具体形态演变有未明处。'),
 'B3148':dict(words=['barb','barbed','barber','barbershop'],label='拉丁 barba 胡须词族；与 beard 的更远联系有争议',note='barb、barber 经法语接拉丁 barba 胡须，barbed 为 barb 加完整 -ed，barbershop 为 barber 加 shop。beard 接日耳曼胡须词，常与 barba 比较，但共同远祖分析有争议，不说 barber 是英语 beard 加 -er。'),
 'B3684':dict(words=['battalion'],label='battle 的打、战斗词族 → battalion',note='battalion 经法语、意大利 battaglione 接 battaglia、拉丁 battuere 打的词族。整体借词，现代不是 battle 后随意加 -ion；营的人员规模不固定写死。'),
 'B3206':dict(words=['bulletin'],label='bulla 圆物、印封 → bulletin',note='bullet 与 bulletin 远处同接拉丁 bulla 圆物。bulletin 经法语及意大利单据词族，由印封、文件联系发展为公告，不说公告来自现代子弹。'),
 'C1416':dict(words=['cholesterol'],label='chole- 胆汁 + ster- 固体 + -ol → cholesterol',note='胆固醇名称接胆汁、固体词族与醇类后缀 -ol；因早期从胆结石发现而得名。只讲词义和名称，不将其等同血脂总称或给诊疗建议。'),
 'C0958':dict(words=['apparel'],label='整备、穿衣 → apparel〔更远词源有两说〕',note='apparel 经法语 apareillier 整备、穿衣。拉丁远源一说接 apparare 准备、parare 词族，另一说接 ad-particulare 与 particula 小块，不把一说定成唯一源头。'),
 'A1831':dict(words=['guise','disguise','disguised'],label='日耳曼方式、外观词 → guise → disguise',note='guise 经法语借入，同接 -wise 方式后缀的日耳曼 manner、form 词族。disguise 经法语 des- 加 guise 改变外观，disguised 去 e 加完整 -ed。不是英语 wise 直接改拼而成。'),
 'A1775':dict(words=['splendid','splendour','splendor','splendidly','horrid'],label='另一条 -id：拉丁 -idus 状态形容词',note='本组 -id 接拉丁 -idus 状态形容词材料，如 splendidus、horridus，与 arachnid 的分类后缀分源。splendour、splendor 是同一闪光词族的 -or 名词，不从 splendid 机械去掉 -id 生成；splendidly 加完整 -ly。'),
 'B4610':dict(words=['vodka'],label='水的远古同源词：俄语 voda + -ka → vodka',note='vodka 借俄语 vodka，voda 水配指小词尾 -ka。voda 与英语 water 是远处同源关系，英语不是把 water 改拼加 -ka；小水是名称来历，不是现代饮料成分定义。'),
 'A1904':dict(words=['vigor','vigour','invigorate','invigorating'],label='vigor 精力 + in-、-ate → invigorate',note='vigor、vigour 为同词常见美式、英式拼写，经法语接拉丁 vigor、vigere 有活力。in- 使进入状态配 -ate 动词材料形成 invigorate，去 e 加完整 -ing → invigorating。'),
 'C1609':dict(words=['revulsion'],label='re- 离开 + vuls- 拉 → revulsion',note='revulsion 接拉丁 revulsio 拉离，来自 revellere，含 re- 与 vellere 拉、撕。身体、情感退缩比喻发展出强烈厌恶；与 revolt 的 volvere 滚动要分清。'),
}
W('exploitation','英、美 /ˌeksplɔɪˈteɪʃən/','利用；开发；剥削、压榨',
 '让某种资源、条件为自己产生价值，是 exploitation 的宽泛画面。若靠不公平对待别人来获利，中文就应说剥削、压榨。',
 '现代可联系 exploit 利用 + 完整 -ation 行为名词材料 → exploitation。整个词借法语 exploitation，接 exploiter；远处连拉丁 explicare 展开词族。',
 [['法语 exploiter 利用、开发 → exploitation → 英语','早期英语常用于有产出的开发、利用活动'],['不公平利用他人的利益 → exploitation 的负面分支','现代褒贬依对象、语境；谈人时常突出剥削']],
 'exploitation of resources 是资源利用、开发；labour exploitation 是劳工剥削；commercial exploitation 是商业利用。',
 'exploitation of resources；labour exploitation；commercial exploitation。',
 'exploitation 不总能固定译成剥削，但谈人的处境时常有不公平榨取利益的含义。use 更宽泛，exploitation 更突出把某种条件转为自己的利益。',
 ('The report examines the commercial exploitation of the discovery.','报告考察了这项发现的商业利用。'),('The novel condemns the exploitation of factory workers.','小说谴责了对工厂工人的剥削。'),sources=S('exploitation','exploitation'))
W('horrific','英 /həˈrɪfɪk/；美 /həˈrɪfɪk/','可怕的；令人惊骇的；极糟糕的',
 '事情可怕到让人一缩、汗毛都像要竖起来，就是 horrific 的直观画面。现代常用于严重、令人震惊的事件，也能夸张形容特别糟糕的经历。',
 'horri- 战栗、毛发竖起 + -fic 使 → horrific。经法语或直接接拉丁 horrificus；-ficus 来自 facere 做、使的复合材料，不是把 horror 后随意加 -ic。',
 [['拉丁 horrere 战栗、毛发竖起 + -ficus 使 → horrificus','字面使毛发竖起，描述带来的惊惧效果'],['法语等 → horrific','现代令人惊骇与强调极糟糕的用法并存']],
 'a horrific accident 是可怕的事故；horrific conditions 是极恶劣的条件；a horrific experience 是可怕的经历。',
 'a horrific accident；horrific conditions；a horrific experience。',
 'horrific 强调带来强烈惊骇；horrible 使用范围更宽，从非常讨厌到真正可怕都可用。两者同接 horr- 战栗词族，词尾历史不同。',
 ('The film describes a horrific accident through the survivors’ memories.','影片通过幸存者的回忆描述了一场可怕事故。'),('The workers faced horrific conditions in the abandoned building.','工人们在废弃建筑里面对极其恶劣的条件。'),sources=S('horrific','horrific'))
W('warranty','英 /ˈwɒrənti/；美 /ˈwɔːrənti/','保证；产品保修、质保承诺',
 '卖方对产品作出一份保证：在约定条件下出了问题，会承担相应责任，这种承诺常叫 warranty。具体承诺什么，要看写出的条款。',
 'warranty 经法语 warantie 保护、担保，来自 warant 保护者、担保等词族。现代可联系 warrant 保证与 -y 名词材料；它与 guarantee 的不同开头反映了借入路径差异。',
 [['法语 warant 保护、担保 → warantie → warranty','早期法律语境有权利、交易相关的担保条款'],['保证、保障承诺 → 产品 warranty','现代购物语境常说质保、保修，范围由具体约定说明']],
 'under warranty 是在保修、质保范围内；a warranty period 是保修期；a written warranty 是书面保证。',
 'under warranty；a warranty period；a written warranty。',
 'warranty 是保证、质保承诺；warrant 还有授权文件、正当理由等常见意思。产品 warranty 也不能单凭中文保修二字就判断全部责任。',
 ('The receipt includes details of the warranty.','收据附有质保说明。'),('The camera was still under warranty when it stopped working.','相机出故障时仍在保修期内。'),sources=S('warranty','warranty'))
W('vegetation','英、美 /ˌvedʒəˈteɪʃən/','植被；植物的总称',
 '望向一片地，上面长着草、灌木和树，把这些生长着的植物作为一个整体来看，就是 vegetation。重点不是挑几样蔬菜，而是地表植物这一层。',
 'veget- 生长、有活力 + -ation 行为、状态名词材料 → vegetation。经法语、拉丁 vegetatio，来自 vegetare 生长、使有活力的分词词干 vegetat- 与 -ion。',
 [['拉丁 vegetare 生长、使有活力 → vegetatio → vegetation','早期英语指植物式生长的活动'],['生长活动 → 植物生活、植物总称','现代最常用植被义，把一片地方的植物合起来说']],
 'dense vegetation 是茂密植被；coastal vegetation 是沿海植被；native vegetation 是本地原生植被。',
 'dense vegetation；coastal vegetation；native vegetation。',
 'vegetation 通常不可数，统说植物覆盖；vegetables 是可吃的蔬菜。两词同接生长词族，但现代关注范围不同。',
 ('Dense vegetation covered the hillside.','茂密植被覆盖了山坡。'),('The photographs show changes in coastal vegetation.','这些照片展示了沿海植被的变化。'),sources=S('vegetation','vegetation'))
W('vegetate','英、美 /ˈvedʒɪteɪt/','无所事事地度日；呆着不动脑筋',
 '一天接一天，只是待着，没什么活动、变化或精神投入，口语可以说 vegetate。像只保持生长、没有主动活动的植物，这是旧植物生长义留下的比喻。',
 'veget- 生长、有活力 + -ate 动词形式材料 → vegetate。英语可能由 vegetation 逆构，也可能直接接拉丁 vegetatus、vegetare 的材料；不强定只有一种造词过程。',
 [['拉丁 vegetare 使有活力、生长 → vegetate 的早期植物式生长义','直接借入与从 vegetation 逆构，都是被提出的可能'],['植物式存在 → 闲散、停滞地生活','现代常用这个带评价或自嘲色彩的比喻义']],
 'vegetate at home 是在家无所事事；vegetate in front of the television 是呆在电视前消磨时间；just vegetate 是什么也不想、就待着。',
 'vegetate at home；vegetate in front of the television；just vegetate。',
 'relax 可以中性说放松；vegetate 常更像呆着、没什么积极活动。有时说话人只是在自嘲自己想放空，语气未必严厉。',
 ('I do not want to vegetate in front of the television all weekend.','我不想整个周末都呆在电视前消磨时间。'),('After the busy week, he wanted one evening to vegetate.','忙了一周后，他想有一个晚上什么也不做、放空一下。'),sources=S('vegetate','vegetate'))
W('revolt','英 /rɪˈvəʊlt/；美 /rɪˈvoʊlt/','反抗；叛乱；使厌恶',
 '原来顺着某种权威或安排，现在转身说不、拒绝服从，是 revolt。另一条常见用法是某物令人厌恶，像身体本能地想转开。',
 're- 回、转开 + 拉丁 volvere 滚转的历史词族 → revolt。英语经法语 revolter、révolte，以及相关意大利语材料发展；现代形式不是把英语 revolve 简单去几个字母。',
 [['拉丁 revolvere 回滚 → 通俗拉丁、法语与意大利语翻转、推翻词族 → revolt','英语形成脱离效忠、反抗权威的动词与叛乱名词'],['转开、反感的语义分支 → 使厌恶','后来形成 The smell revolted me 一类用法，也见 revolting 令人作呕的']],
 'a revolt against authority 是反抗权威；revolt against a decision 是反对某项决定；revolt someone 是使某人厌恶。',
 'a revolt against；revolt against；revolt someone。',
 'revolt 可以是反抗动作，也可以是反抗事件名词；revolve 通常说旋转。两者有早期滚转词族联系，现代各有稳定用法。',
 ('The novel describes a revolt against an unjust ruler.','小说描写了对一位不公统治者的反抗。'),('The students threatened to revolt against the new timetable.','学生们表示要反对新的课程时间表。'),sources=S('revolt','revolt'))
W('forthcoming','英 /ˌfɔːθˈkʌmɪŋ/；美 /ˌfɔːrθˈkʌmɪŋ/','即将到来的；即将出版的；乐意提供信息的',
 '一件事快要走到眼前，是 forthcoming；问一个人情况，他愿意把知道的东西拿出来告诉你，也叫 forthcoming。共同感觉是所需的东西愿意、能够来到面前。',
 'forth 向前、出来 + come 来的 -ing 形式 coming → forthcoming。coming 中 come 去 e 加完整 -ing；词承古英语 forðcuman 出来、发生的历史组合。',
 [['古英语 forðcuman 出来、发生 → forthcome 词族 → forthcoming','形容即将出现、发生'],['需要时能拿得出来 → 乐意响应、提供信息','现代形容人很 forthcoming，常表示愿意说明情况、提供帮助']],
 'a forthcoming book 是即将出版的书；the forthcoming event 是即将举行的活动；forthcoming about something 是愿意说明某事。',
 'a forthcoming book；the forthcoming event；forthcoming about。',
 'forthcoming book 里的 forthcoming 讲时间；forthcoming with details 讲愿意提供细节。coming 常说即将到来，但不自动具有乐意说明情况的全部用法。',
 ('Her forthcoming book explores the history of the town.','她即将出版的书探讨了这座城镇的历史。'),('He was forthcoming about the difficulties they had faced.','他很坦率地说出了他们遇到的困难。'),sources=S('forthcoming','forthcoming'))
W('baggage','英 /ˈbæɡɪdʒ/；美 /ˈbæɡɪdʒ/','行李；心理包袱；遗留负担',
 '出门带着的箱包、物品，合起来叫 baggage。人也可能一直背着过去的烦恼、未解开的心结，于是有 emotional baggage 心理包袱的比喻。',
 'baggage 经法语 bagage 行装、装备，接 bague 包裹，通常认为与 bag 的北欧来源相关。-age 在这类借词里提供集合性名词材料，英语不是把末尾读成独立 age 年龄。',
 [['法语包裹、装备词族 → bagage → baggage','早期与军队携带的装备等相连，后常说旅客行李'],['随身负担 → emotional baggage 等比喻','现代把过去留下、难以放下的情绪问题比作背着走的包袱']],
 'checked baggage 是托运行李；a piece of baggage 是一件行李；emotional baggage 是心理包袱。',
 'checked baggage；a piece of baggage；emotional baggage。',
 'baggage 通常不可数，数件数可以说 two pieces of baggage。bag 是单个包；luggage 与行李义 baggage 很接近，但 baggage 另有常见心理包袱用法。',
 ('Please keep your baggage beside you.','请把行李放在身边。'),('The character carries emotional baggage from an unhappy childhood.','这个人物背负着不幸童年留下的心理包袱。'),sources=S('baggage','baggage'))
W('cuisine','英、美 /kwɪˈziːn/','菜系；烹饪风格；某地、某类的料理',
 '一种地方或传统，惯用什么食材、怎样调味和烹调，合起来形成的做菜风格，是 cuisine。它看整套风格，不只看眼前这一盘菜。',
 '整体借法语 cuisine，法语原也指厨房、烹饪，接晚期拉丁 cocina、coquina 厨房，来自 coquere 烹饪。现代不按英语拼写拆成 cu 加某个后缀。',
 [['拉丁 coquere 烹饪 → coquina、cocina 厨房 → 法语 cuisine','做饭动作与做饭场所相连'],['法语 cuisine → 英语 cuisine 烹饪风格','现代常按地域、传统或食材特色来描述菜系']],
 'regional cuisine 是地方菜系；traditional cuisine 是传统料理；French cuisine 是法国菜、法式料理。',
 'regional cuisine；traditional cuisine；French cuisine。',
 'cuisine 常谈烹饪风格、菜系；dish 可以是一道具体菜。culinary 与厨房、烹饪有关，远处同接拉丁烹饪词族，但并不是 cuisine 加 -ary 形成。',
 ('The festival celebrates the region’s traditional cuisine.','节庆展示了该地区的传统料理。'),('Her cooking combines regional cuisine with modern techniques.','她的烹饪把地方菜风格与现代技法融合在一起。'),sources=S('cuisine','cuisine')+['https://www.etymonline.com/word/culinary'])
W('barber','英 /ˈbɑːbə/；美 /ˈbɑːrbɚ/','理发师〔常为男性顾客理发、修须〕',
 '帮人剪头发、修胡须的人，是 barber。这个词的老本义紧贴胡须，现代通常想到理发店里剪短发、修整胡须的师傅。',
 '经法语 barbeor、barbier 等接拉丁 barba 胡须与相关职业者形式。现代词尾看起来像 -er，但整个词是历史借词；不是英语 beard 直接加 -er。',
 [['拉丁 barba 胡须 → 相关职业者词 → 古法语、英法语 → barber','胡须护理扩展、保留为理发修须职业名'],['现代 barber 理发师、修须者','与英语 beard 的更远共同祖先有不同分析，不能把传统同源比较说成定论']],
 'go to the barber 是去理发；a local barber 是当地理发师；the barber’s 是理发店。',
 'go to the barber；a local barber；the barber’s。',
 'barber 常与剪短发、修须的服务相连；hairdresser 更宽泛地说做头发的人。具体服务与从业者身份可以变化，词的历史重点则是胡须护理。',
 ('The barber trimmed his hair and beard.','理发师为他修剪了头发和胡须。'),('A local barber donated old photographs to the exhibition.','当地一位理发师把老照片捐给了展览。'),sources=S('barber','barber')+['https://www.etymonline.com/word/beard'])
W('barbershop','英 /ˈbɑːbəʃɒp/；美 /ˈbɑːrbɚʃɑːp/','理发店；理发店式无伴奏和声唱法',
 'barber 工作的小店，就是 barbershop。它也用来给一种几个人配合唱和声的风格命名，常见于 barbershop quartet 这种搭配。',
 'barber 理发师 + shop 店 → barbershop。barber 借法语并远接拉丁 barba 胡须；shop 是英语商店词。音乐名称是后来另一个领域的扩展。',
 [['barber + shop → barbershop 理发店','现代英语里构成透明的店铺复合词'],['barbershop → 特定人声和声风格名称','现代常见 barbershop quartet，通常指四人无伴奏和声组合']],
 'a neighbourhood barbershop 是街坊理发店；a barbershop quartet 是理发店式四重唱组合；barbershop harmony 是相应和声风格。',
 'a neighbourhood barbershop；a barbershop quartet；barbershop harmony。',
 'barber 指人，barbershop 指场所。音乐用法可以先整体记住 quartet 四人组合与无伴奏人声和声，具体起源不靠“所有人都在店里唱”来推断。',
 ('The barbershop opened early on Saturday.','理发店星期六一早就开门了。'),('A barbershop quartet performed at the community festival.','一个理发店式四重唱组合在社区节庆上表演。'),sources=S('barbershop','barber')+['https://www.barbershop.org/fact-sheet-barbershop-harmony-society'])
W('battalion','英、美 /bəˈtæliən/','营〔军队单位〕；一大队人',
 '一支有组织、能作为一个单位行动的队伍，军事语境里 battalion 通常译作营。日常夸张用法也可以说一大队忙碌的人。',
 '经法语 bataillon、意大利语 battaglione 接 battle 的战斗词族，远连拉丁 battuere 打。词尾来自这些语言的整词发展，现代不能直接把 battle 加 -ion 拼成 battalion。',
 [['拉丁 battuere 打 → 意大利战斗、队伍词族 → battaglione → 法语 bataillon','从战斗词族形成队伍编组名称'],['法语 → battalion','现代多为营，也能比喻数量可观、组织起来的一队人']],
 'an infantry battalion 是步兵营；a battalion commander 是营长；a battalion of volunteers 是一大队志愿者的形象说法。',
 'an infantry battalion；a battalion commander；a battalion of volunteers。',
 'battle 说战斗，battalion 说队伍单位，词源相关而现代所指不同。一个营的人数随国家、年代和编制变化，词本身不规定统一人数。',
 ('The museum displayed the battalion’s old banner.','博物馆展出了这个营的旧旗帜。'),('A battalion of volunteers helped prepare the festival.','一大队志愿者帮助筹备了节庆。'),sources=S('battalion','battalion'))
W('bulletin','英 /ˈbʊlɪtɪn/；美 /ˈbʊlətɪn/','公告；简报；简短新闻播报',
 '把某件事的最新情况整理成一份简短、正式的消息，发给大家看或听，就是 bulletin。可以贴在公告栏，也可以是广播里的新闻简报。',
 '经法语 bulletin、意大利 bulletino 等单据、公告词，远接拉丁 bulla 圆物、印封。意大利语里有多层指小形式；现代不把它拆成英语 bullet 子弹加 -in。',
 [['拉丁 bulla 圆物、印封 → 单据、文件词族 → 意大利、法语 bulletin','印封与正式文件相联系，形成公众通报的名称'],['bulletin → 公告、定期简报、新闻播报','现代纸质、广播、电子消息等都可使用']],
 'a news bulletin 是新闻简报；a bulletin board 是公告栏；a weekly bulletin 是每周简报。',
 'a news bulletin；a bulletin board；a weekly bulletin。',
 'bullet 和 bulletin 远处同接圆物、印封词族，但不是现代子弹变出了新闻公告。report 范围更广，bulletin 常强调简短、面向一群人的信息通报。',
 ('The weekly bulletin lists upcoming events.','每周简报列出了即将举行的活动。'),('A short news bulletin interrupted the programme.','一段简短新闻播报打断了节目。'),sources=S('bulletin','bulletin')+['https://www.etymonline.com/word/bullet'])
W('cholesterol','英 /kəˈlestərɒl/；美 /kəˈlestərɑːl/','胆固醇',
 '身体里一种蜡样、类似脂肪的物质，叫 cholesterol。中文“胆固醇”也藏着它的命名线索：早期从胆结石中发现的固体，后来按化学类别调整了名称。',
 'chole- 胆汁 + ster- 固体、坚实 + 完整 -ol 醇类后缀 → cholesterol。经法语早期 cholestérine 等化学名发展；ster- 与 stere- 坚实词族相连。',
 [['希腊胆汁词与坚实词组合 → 法语早期化学名称','名称联系从胆结石发现的物质'],['名称按醇类改用 -ol → cholesterol','现代为特定物质名称，不是所有脂类的总称']],
 'blood cholesterol 是血液中的胆固醇；cholesterol levels 是胆固醇水平；a cholesterol test 是胆固醇检测。',
 'blood cholesterol；cholesterol levels；a cholesterol test。',
 'cholesterol 是物质名称；cholesterol level 是测得的水平。词源说明为什么这样命名，不代表胆固醇只存在于胆汁或胆结石中。',
 ('The article explains how cholesterol moves through the bloodstream.','文章解释了胆固醇怎样在血液中运输。'),('The chart compares cholesterol levels in the study groups.','图表比较了研究各组的胆固醇水平。'),sources=S('cholesterol','cholesterol')+['https://www.nhlbi.nih.gov/health/blood-cholesterol'])
W('apparel','英 /əˈpærəl/；美 /əˈpærəl/','衣服；服装〔较正式，常见于商业分类〕',
 '商店写 sports apparel，通常就是运动服装。apparel 把衣服作为一类商品、穿着装备来讲，语气比日常 clothes 更正式。',
 '整体经法语 apareil、apareillier 整备、穿衣进入英语。更远来源有两说：一说接拉丁 apparare 准备，另一说接 *ad-particulare 把小部分配在一起；不把现代拼写强拆成固定英语前后缀。',
 [['法语整备、准备、穿衣词族 → apparel','早期英语也说装备、配备，后来服装义突出'],['apparel 衣服、服装总称','现代常见于店铺分类、行业与较正式文字；更早的拉丁构词仍有不同解释']],
 'sports apparel 是运动服装；outdoor apparel 是户外服装；an apparel company 是服装公司。',
 'sports apparel；outdoor apparel；an apparel company。',
 'apparel 通常不可数，clothes 则使用复数形式。a piece of apparel 可数一件服装，日常直接说 a shirt、a coat 往往更具体。',
 ('The shop sells outdoor apparel and equipment.','商店销售户外服装和装备。'),('She designs apparel for children.','她为儿童设计服装。'),sources=S('apparel','apparel'))
W('guise','英、美 /ɡaɪz/','外表；表面身份；假借的名目',
 '事情真实是一回事，给人看到的表面身份却是另一回事，这层外观可以叫 guise。under the guise of help 常是打着帮助的名义。',
 '整体借法语 guise 外观、方式，远接日耳曼 *wisa、*wison 方式、形态。这与英语 -wise 方式后缀的历史名词材料同源，借入法语后起始音经历了不同变化。',
 [['日耳曼方式、形态词 → 法语 guise → 英语 guise','英语早期有穿着样式、外观等用法'],['外观 → 假扮身份、表面名目','现代常用 in the guise of、under the guise of 讲真实与表面之间的关系']],
 'under the guise of 是打着……的幌子；in the guise of 是以……的外表、身份；a familiar guise 是熟悉的外观。',
 'under the guise of；in the guise of；a familiar guise。',
 'guise 常突出呈现出来的样子，尤其是假借身份；appearance 更宽泛。guise 与 -wise 的历史联系是借词和继承词分路，不是把现代 wise 改写一个字母。',
 ('The character enters the house in the guise of a messenger.','这个人物假扮信使进入了房子。'),('He offered criticism under the guise of friendly advice.','他打着友好建议的名义提出批评。'),sources=S('guise','guise'))
W('disguise','英、美 /dɪsˈɡaɪz/','伪装；掩饰；乔装用的外观或装束',
 '把原来的样子改掉，让人认不出真实身份，或看不出真实情绪，就是 disguise。它既说伪装动作，也说用来掩盖身份的装束。',
 'dis- 改开、离开原状 + guise 外观 → disguise，历史经法语 desguiser 进入英语。guise 远接日耳曼方式、形态词族；这里的 dis- 帮助理解改变原来外观。',
 [['法语 des- + guise 外观 → desguiser → disguise 动词','早期重点是改变通常外观、隐藏身份'],['disguise 动词 → 装束、假象名词','现代也用于掩饰声音、情绪、意图等']],
 'wear a disguise 是乔装；in disguise 是经过伪装的；disguise one’s voice 是伪装声音。',
 'wear a disguise；in disguise；disguise one’s voice。',
 'disguise 重点在让真实身份、状态不易被看出；costume 可以只是演出服装，不一定想欺骗。a blessing in disguise 是表面像坏事、后来却有好处。',
 ('In the play, the detective wears a disguise.','剧里，侦探穿着乔装服饰。'),('She could not disguise her surprise.','她掩饰不住自己的惊讶。'),sources=S('disguise','disguise'))
W('splendid','英、美 /ˈsplendɪd/','极好的；壮丽的；华美的',
 '东西亮眼、气派，让人觉得真漂亮、真好，就可以说 splendid。日常还可以直接赞一个想法 splendid，意思是太棒了。',
 'splend- 闪亮 + 拉丁 -idus 状态形容词材料 → splendidus，进入英语后见 splendid；英语形式可能经过较长早期形式缩短。这里 -id 与动物分类的 -id 不同源。',
 [['拉丁 splendere 闪耀 → splendidus 闪亮、华丽的','-idus 与状态动词相配，形成具有某种性质的形容词'],['英语 splendid 的早期相关形式 → splendid','闪亮、壮丽进一步用于赞美极好、出色']],
 'a splendid view 是壮丽景色；a splendid idea 是极好的主意；a splendid performance 是精彩表演。',
 'a splendid view；a splendid idea；a splendid performance。',
 'splendid 可以真说外观华美，也可以只是赞事情很好。splendour、splendor 是同词族名词，在英语里不是临时把 splendid 的 -id 换掉才出现。',
 ('The terrace offers a splendid view of the valley.','露台上可以看到山谷的壮丽景色。'),('That is a splendid idea.','那真是个好主意。'),sources=S('splendid','splendid')+['https://en.wiktionary.org/wiki/splendidus#Latin','https://en.wiktionary.org/wiki/-idus#Latin'])
W('splendour','英 /ˈsplendə/；美 /ˈsplendɚ/','壮丽；华美；辉煌〔常见英式拼写〕',
 '一处建筑、景色或场面，整体亮眼、盛大、华美，这种气象叫 splendour。它把 splendid 那种壮丽感觉当作一个名词来谈。',
 '经法语 splendour、splendor 等及拉丁 splendor 光辉、辉煌，来自 splendere 闪亮。现代常见英式 splendour、美式 splendor；-our、-or 是相应名词拼写材料。',
 [['拉丁 splendere 闪耀 → splendor 光辉 → 法语等 → splendour','名词与形容词有共同词族，但借入时间、路径不同'],['光辉、华美 → 壮丽、盛大气象','现代常说建筑、仪式或自然景观的华美']],
 'in all its splendour 是尽显其壮丽；the splendour of a palace 是宫殿的华美；natural splendour 是自然景色的壮美。',
 'in all its splendour；the splendour of；natural splendour。',
 'splendour 通常是性质名词，splendid 是形容词。splendour 与 splendor 是同一个词的英美拼写，不要另记两套意思。',
 ('The restoration revealed the hall in all its splendour.','修复让大厅重现了全部华美。'),('They admired the natural splendour of the mountains.','他们赞叹群山的自然壮美。'),sources=S('splendour','splendor'))
W('splendor','英 /ˈsplendə/；美 /ˈsplendɚ/','壮丽；华美；辉煌〔常见美式拼写〕',
 '看到宏伟建筑、灿烂装饰或壮丽山景时，可以用 splendor 概括那种令人惊叹的华美气象。它和 splendour 是同一个词的不同拼写。',
 '接法语及拉丁 splendor 光辉，来自 splendere 闪亮。-or 是历史名词词尾，表示这一性质、状态；不能与职业人后缀 -or 混为一谈。',
 [['拉丁 splendere 闪耀 → splendor 光辉、华美 → 法语、英语','以光亮、华丽的画面形成名词'],['英语 splendor、splendour 的拼写分布','现代美式通常写 splendor，英式通常写 splendour']],
 'the splendor of a palace 是宫殿的华美；in all its splendor 是尽显壮丽；historic splendor 是历史上的辉煌气象。',
 'the splendor of；in all its splendor；historic splendor。',
 'splendor 通常不可数，泛说华美、壮丽。复数 splendors 可以突出几种壮丽景象，但学习时先掌握性质名词与 splendid 形容词的区别。',
 ('The photographs capture the splendor of the old theatre.','照片捕捉了老剧院的华美。'),('The city displayed its historic splendor during the festival.','节庆期间，这座城市展现了它历史上的辉煌气象。'),sources=S('splendor','splendor'))
W('vodka','英 /ˈvɒdkə/；美 /ˈvɑːdkə/','伏特加〔一种蒸馏酒〕',
 'vodka 是酒名，中文通常音译伏特加。它的俄语名称原来像在说“小水”，这是词名的历史趣味，今天这个词实际指一种酒。',
 '借俄语 vodka：voda 水 + 指小词尾 -ka。voda 与英语 water 远处同接水的印欧词族；现代英语不是把 water 加 -ka 来构造这个词。',
 [['俄语 voda 水 + -ka 指小 → vodka','水的名称参与酒类命名，是这条语言的命名方式'],['俄语 vodka → 英语 vodka','英语整体借入酒名，与 water 保留远古同源比较关系']],
 'a bottle of vodka 是一瓶伏特加；vodka production 是伏特加生产；the word vodka 是 vodka 这个词。',
 'a bottle of vodka；vodka production；the word vodka。',
 '词源的小水帮助记名字，现代含义则是酒。water 与 vodka 的联系是早期词族分成不同语言后，再有俄语酒名被英语借入。',
 ('The label identifies the drink as vodka.','标签把这种饮品标为伏特加。'),('The exhibition explains the history of vodka production.','展览介绍了伏特加生产的历史。'),sources=S('vodka','vodka'))
W('vigor','英 /ˈvɪɡə/；美 /ˈvɪɡɚ/','活力；精力；有力、旺盛的劲头〔常见美式拼写〕',
 '做事有劲、精神饱满，像一直有力量往前推，这种活力叫 vigor。也可以说一段论证、一次讨论很有力，不只限于身体力气。',
 'vigor 经法语 vigor、vigour 接拉丁 vigor 活跃、力量，来自 vigere 旺盛、有活力。这里 -or 是性质名词材料；常见英式拼写 vigour。',
 [['拉丁 vigere 活跃、旺盛 → vigor 活力 → 法语、英语','从身体活力，也用于语言、思考、植物生长等方面'],['英语 vigor、vigour','同一个词的常见美式、英式拼写分布']],
 'with vigor 是有力地；renewed vigor 是重新恢复的活力；intellectual vigor 是思想活力。',
 'with vigor；renewed vigor；intellectual vigor。',
 'vigor 是力量、活跃的劲头，vigorous 是充满这种劲头的形容词。它与 vigour 同义，不能按有没有 u 分成不同强度。',
 ('She returned to the project with renewed vigor.','她带着恢复的活力重新投入项目。'),('The debate was conducted with vigor and humour.','辩论进行得有力而又幽默。'),sources=S('vigor','vigor'))
W('vigour','英 /ˈvɪɡə/；美 /ˈvɪɡɚ/','活力；精力；旺盛的劲头〔常见英式拼写〕',
 '一个人做事充满精神，或一棵植物长得很旺，可以谈它的 vigour。词的重点是有力量、有生气，而不只是忙得停不下来。',
 '经法语 vigour 等接拉丁 vigor 活力、vigere 旺盛。-our 是这类名词的历史拼写形式；美式通常写 vigor，读音、基本意思相同。',
 [['拉丁 vigere 旺盛 → vigor → 法语 vigour → 英语','英语很早已有力量、活力名词'],['vigour 与 vigor 的现代拼写分布','不因为拼写不同就另造一套词义或来历']],
 'full of vigour 是充满活力；with renewed vigour 是带着恢复的劲头；the vigour of the argument 是论证的有力程度。',
 'full of vigour；with renewed vigour；the vigour of。',
 'vigour 是名词，vigorous 是形容词；invigorate 是使恢复精神。看清这几种词性，就能把同一股活力放进不同句型。',
 ('The young plants grew with remarkable vigour.','幼苗长得格外旺盛。'),('He defended his idea with vigour.','他有力地捍卫了自己的想法。'),sources=S('vigour','vigor'))
W('invigorating','英 /ɪnˈvɪɡəreɪtɪŋ/；美 /ɪnˈvɪɡəreɪtɪŋ/','使人振奋的；使恢复精神的；正在激发活力',
 '原来有点疲、没精神，现在像被重新点亮，这种让人振作的体验可以叫 invigorating。清爽的空气、活跃的讨论，都可以带来这种感觉。',
 'in- 使进入某状态 + vigor 精力 + -ate 动词材料 → invigorate；去末尾 e，加完整 -ing → invigorating。不是把 in- 当成否定来理解。',
 [['vigor 活力 + in-、-ate → invigorate 使充满活力','现代英语用已有名词形成使动意义的动词'],['invigorate + -ing → invigorating','现代常作形容词，描述带来振奋效果的事物']],
 'an invigorating walk 是令人精神一振的散步；an invigorating discussion 是让人振奋的讨论；invigorating the team 是给团队带来活力。',
 'an invigorating walk；an invigorating discussion；invigorating the team。',
 'invigorating 描述带来振奋效果的事物；invigorated 描述已经感到振奋的人或状态。The talk was invigorating 与 I felt invigorated 可以搭配理解。',
 ('The cool morning air felt invigorating.','清晨凉爽的空气让人精神一振。'),('We had an invigorating discussion about the new project.','我们围绕新项目展开了让人振奋的讨论。'),sources=S('invigorating','vigor'))
W('revolting','英 /rɪˈvəʊltɪŋ/；美 /rɪˈvoʊltɪŋ/','令人作呕的；极讨厌的；正在反抗',
 '闻到、看到某物，心里强烈排斥、身体都想转开，可以说 revolting。它也可以只是 revolt 的动作形式，表示人们正在反抗。',
 'revolt + 完整 -ing → revolting，直接加后缀。revolt 接回滚、翻转的拉丁、法语词族；反抗与使人厌恶是不同语义分支。',
 [['revolt 反抗、转开 → revolting 的早期反抗义','动词形式可直接描述正在反抗的人'],['使人因厌恶而转开 → revolting 令人作呕的','现代这个强烈负面形容词义很常见']],
 'a revolting smell 是令人作呕的气味；revolting behaviour 是令人厌恶的行为；revolting against something 是正在反抗某事。',
 'a revolting smell；revolting behaviour；revolting against。',
 'The smell is revolting 中 revolting 是令人厌恶的性质；They are revolting against the ruler 中则是人在反抗的动作。用主语和后面的 against 帮助判断。',
 ('A revolting smell came from the old bin.','旧垃圾桶里飘来一股令人作呕的气味。'),('In the story, the villagers are revolting against the ruler.','故事里，村民们正在反抗统治者。'),sources=S('revolting','revolt'))
W('barb','英 /bɑːb/；美 /bɑːrb/','倒刺；尖刺；尖刻挖苦的话',
 '尖端旁边再长出一个向后钩的小刺，是 barb 的典型画面。说话也会扎人，于是一句尖刻、故意让人难受的话也能叫 barb。',
 '经法语 barbe 胡须、像胡须的突出物，接拉丁 barba 胡须。刺状突出物由相似形状得名；与日耳曼 beard 的远处联系存在争议，不能当作英语 beard 的直接派生。',
 [['拉丁 barba 胡须 → 法语 barbe → barb','胡须状突出物、尖刺等用法发展'],['刺人、钩住的形象 → 话语中的尖刻挖苦','现代可说具体尖刺，也可数一句句伤人的话']],
 'a sharp barb 是尖刺或尖刻挖苦；a barb on a hook 是钩上的倒刺；a verbal barb 是言语中的挖苦。',
 'a sharp barb；a barb on a hook；a verbal barb。',
 'barb 的实体用法强调突出、常带钩的尖刺；话语用法强调刺痛人的那一句。joke 可以只是逗乐，a barb 往往带伤人、挖苦的锋芒。',
 ('The drawing shows a tiny barb at the end of the hook.','图画显示了钩子末端的一枚小倒刺。'),('He ignored the barb hidden in her reply.','他没有理会她回答里藏着的挖苦。'),sources=S('barb','barb'))
W('barbed','英 /bɑːbd/；美 /bɑːrbd/','带倒刺的；带刺的；尖刻的',
 '东西外面有小刺，是 barbed；一句话表面像普通回答，却能扎人，也可以说 barbed。像中文“带刺的话”，画面几乎直接对应。',
 'barb 刺 + 完整 -ed 带有、装有 → barbed，/b/ 后后缀读 /d/。也可作给某物装刺的过去形式；远接法语、拉丁胡须状突出物词族。',
 [['拉丁 barba 胡须 → 法语 barbe → barb 尖刺','现代名词承接相似外形的历史用法'],['barb + -ed → barbed','描述实物有刺，也比喻话语尖刻、带挖苦']],
 'barbed wire 是有刺铁丝网；a barbed remark 是带刺的话；a barbed reply 是尖刻的回答。',
 'barbed wire；a barbed remark；a barbed reply。',
 'barbed 说带刺或言语尖刻；barb 是单个刺、单句挖苦的名词。-ed 在 barbed wire 中常作为带有某物的形容词材料来理解。',
 ('An old fence of barbed wire crossed the field.','一道旧有刺铁丝网围栏横穿田地。'),('She answered with a barbed remark.','她用一句带刺的话作了回答。'),sources=S('barbed','barb'))
W('splendidly','英、美 /ˈsplendɪdli/','极好地；出色地；华美地',
 '事情做得特别好，可以说 it went splendidly；东西装饰得很华美，也可以用 splendidly。它把 splendid 的赞美放到动作、结果上。',
 'splendid + 完整 -ly 副词词尾 → splendidly，原词不改。splendid 远接拉丁 splendere 闪亮与 splendidus 闪亮、壮丽的；其中 -idus 是另一条拉丁形容词材料。',
 [['拉丁闪耀词族 → splendid 壮丽、极好的','外观亮眼进一步发展为一般的高度赞美'],['splendid + -ly → splendidly','现代说明动作、安排或结果出色，也可说外观华美']],
 'went splendidly 是进行得极好；performed splendidly 是表现出色；splendidly decorated 是装饰得华美。',
 'went splendidly；performed splendidly；splendidly decorated。',
 'splendid 是形容词，修饰事物；splendidly 是副词，常修饰动作或另一性质。a splendid performance 与 performed splendidly 表达角度不同。',
 ('The opening night went splendidly.','首演之夜进行得非常顺利。'),('The hall was splendidly decorated for the festival.','大厅为节庆装饰得十分华美。'),sources=S('splendidly','splendid'))
W('horrid','英 /ˈhɒrɪd/；美 /ˈhɔːrɪd/','可怕的；讨厌的；糟糕的',
 '原来的画面是粗糙、带刺、让人起鸡皮疙瘩。今天说 horrid，既可以说可怕，也常只是很讨厌、很糟，让人不舒服。',
 'horri- 竖起、战栗 + 拉丁 -idus 状态形容词材料 → horridus → horrid。这里的 -id 是拉丁性质形容词的一支，与分类名称里的 -id 分源。',
 [['拉丁 horrere 竖起、战栗 → horridus 毛发竖立、粗糙、可怕 → horrid','英语早期也有毛茸、粗糙等描述'],['可怕 → 令人讨厌、糟糕','现代日常语气中可以比真正恐怖轻一些']],
 'a horrid smell 是讨厌的气味；a horrid day 是糟糕的一天；be horrid to someone 是对某人很刻薄、不友善。',
 'a horrid smell；a horrid day；be horrid to someone。',
 'horrid 在日常抱怨里可以只说讨厌、不愉快；horrific 常更强调惊骇、恶劣程度。具体强度仍取决于说话语气和对象。',
 ('A horrid smell filled the kitchen.','厨房里弥漫着一股难闻的气味。'),('Do not be horrid to your brother.','别对你弟弟那么刻薄。'),sources=S('horrid','horrid')+['https://en.wiktionary.org/wiki/horridus#Latin','https://en.wiktionary.org/wiki/-idus#Latin'])
W('horrifically','英、美 /həˈrɪfɪkli/','极其可怕地；令人惊骇地；糟糕透顶地',
 '强调一件事糟糕得令人震惊，可以用 horrifically。它常把后面“出错、受损、遭到虐待”等程度一下推得很高。',
 'horrific + 完整 -ally → horrifically；这类 -ic 形容词常用 -ally 形成副词，形式上含 -al- 与 -ly 材料，不能只写成末尾加 -ly。horrific 自身含 horri- 与 -fic 使。',
 [['拉丁 horrere 战栗 + -ficus 使 → horrific','形成令人惊骇的形容词'],['horrific + -ally → horrifically','现代副词加强动作、结果的可怕、恶劣程度；学习拆分不要求假设英语先造某个中间词']],
 'horrifically wrong 是错得极其糟糕；horrifically mistreated 是遭到极恶劣的对待；horrifically expensive 是夸张说贵得吓人。',
 'horrifically wrong；horrifically mistreated；horrifically expensive。',
 'horrifically 是强烈评价，正式报告和口语中的程度可能不同。horrific 修饰事物，horrifically 通常修饰动作、形容词或结果。',
 ('The plan went horrifically wrong.','计划出了极其严重的岔子。'),('The novel describes people who were horrifically mistreated.','小说描写了一些遭到极恶劣对待的人。'),sources=S('horrifically','horrific'))
W('revulsion','英、美 /rɪˈvʌlʃən/','强烈厌恶；反感得想退开的感觉',
 '某件事让你一下子很反感，像身体都想往后缩、离它远一点，这种强烈排斥感叫 revulsion。',
 're- 离开、往回 + vuls- 拉、撕的分词词干 + -ion 名词词尾 → revulsion。经法语或直接接拉丁 revulsio 拉离，来自 revellere 拉开。',
 [['拉丁 re- + vellere 拉 → revellere、revuls- → revulsio','拉离的动作名词早也曾用于旧医学术语'],['退回、拉开 → 情感突然转开、强烈厌恶','现代常用的是厌恶、反感义，旧医疗做法不作为现代用法解释']],
 'feel revulsion 是感到强烈厌恶；revulsion at something 是对某事的强烈反感；a sense of revulsion 是一股强烈排斥感。',
 'feel revulsion；revulsion at；a sense of revulsion。',
 'revulsion 比普通 dislike 更强烈，常有本能地想退开的感觉。revolt 与它在意义上可相近，但 revulsion 的拉丁词干是 vell-/vuls- 拉，不是 volv- 滚。',
 ('She felt revulsion at the cruelty described in the story.','她对故事中描写的残忍感到强烈厌恶。'),('His expression changed from curiosity to revulsion.','他的神情从好奇变成了强烈反感。'),sources=S('revulsion','revulsion'))
W('disguised','英、美 /dɪsˈɡaɪzd/','伪装了的；掩饰了；假扮成的',
 '真实样子被换成另一套外观，让人不容易认出，就是 disguised。人可以假扮成某种身份，情绪也可以被别的表情掩盖。',
 'disguise 去末尾 e，加完整 -ed → disguised，/z/ 后读 /d/。disguise 经法语 des- 改离原状 + guise 外观；现代以整个动词 disguise 为词基变化。',
 [['法语 desguiser 改变外观 → disguise 伪装','英语也扩展到掩饰情绪、声音、意图'],['disguise + -ed → disguised','现代作过去式、分词，常用 disguised as 假扮成']],
 'disguised as a messenger 是假扮信使；thinly disguised 是掩饰得很浅、明显可辨；disguised her feelings 是掩饰了她的情绪。',
 'disguised as；thinly disguised；disguised one’s feelings。',
 'disguised as 说明呈现出来的假身份；hidden 常只强调藏起来。thinly disguised criticism 是很容易看出来的批评，即使表面用了别的包装。',
 ('In the story, she entered disguised as a traveller.','故事里，她假扮旅人进入了那里。'),('His praise was thinly disguised criticism.','他的赞美其实是很容易识破的批评。'),sources=S('disguised','disguise'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
 # The same written suffix has separate origins; retain existing scientific branches.
 import json
 from pathlib import Path
 folder=Path(__file__).resolve().parents[1]/'content/精讲'
 found=0
 for path in folder.glob('roots*.json'):
  rows=json.loads(path.read_text());changed=False
  for q in rows:
   if q['id']=='A1775':
    found+=1;changed=True
    q['meaning']='分类成员、形似物；拉丁状态形容词〔不同来源〕'
    q['core']='-ID：同样的末尾，分类名称与拉丁状态形容词分开学'
    q['image']='三幅画面分开看：arachnid 属于动物类群，plasmid 是近代遗传学名称；splendid 的闪亮、horrid 的战栗则来自拉丁状态形容词。'
    q['intro']='同写 -id，有多条来源。动物类群名称可接希腊后裔、类群材料，经法语、新拉丁语发展；近代名称也有形似等相关造词材料。另一支接拉丁 -idus，常与状态动词相配，形成具有某种性质的形容词，如 splendidus、horridus。'
    q['contrasts']='arachnid 与 plasmid 要按各自科学命名历史理解；splendid、horrid 的 -id 接拉丁 -idus，不能套成分类成员。splendour、splendor 与 splendid 共享闪亮词族，但名词 -or 与形容词 -idus 是不同材料。'
    q['practice']='Compare arachnid and plasmid with adjectives such as splendid and horrid.\n\n把 arachnid、plasmid 与 splendid、horrid 等形容词分别比较。'
  if changed:path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 assert found==1,found
if __name__=='__main__':
 save('continuation_20261030_zko',ROOTS,WORDS)
 extend_lessons()
