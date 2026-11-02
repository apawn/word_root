"""Stand: upright support, stable positions, and historical extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,name,meaning):return [[f'英语 {a}；{b}','并列组合的两部分'],[f'{a} + {b} → {name}',meaning]]
STAND=[['古英语 standan → 中古英语 standen / stonden','站立；占据一个位置'],['英语 stand','站；立着；坚持；忍受；台架']]
W('stand','/stænd/','站；立；保持某位置；忍受；台架、立场',
 '先想一个人双脚支住、直立不倒；身体稳住，态度也能稳住。',
 '接古英语 standan，经中古英语 standen、stonden 延续；过去式、过去分词 stood /stʊd/ 保留历史元音变化。名词台架、立场等由动作及位置发展。',STAND,
 'stand up 是站起来，stand by a decision 是坚持决定，can’t stand the noise 是受不了噪声；a music stand 是乐谱架，take a stand 是表明坚定立场。',
 'stand up；stand still；can’t stand；take a stand；a display stand。',
 'stand 作不及物可说东西立着，也能及物说把东西竖放：stand the bottle upright。忍受义常接名词或 -ing，如 can’t stand waiting。',
 ('Please stand behind the yellow line.','请站在黄线后面。'),('I can’t stand waiting in a noisy room.','我受不了在吵闹房间里等着。'),('She took a stand against the unfair rule.','她明确反对这项不公平规定。'))
W('standing','/ˈstændɪŋ/','站立的；长期有效的；地位、声誉',
 '人站着不坐下，规则立着没撤掉，人在群体里也有自己的位置。',
 'stand + -ing，接早期英语相应分词和名词形式；standing 不是只有进行时，已能作形容词及地位、持续时间等名词。',STAND[:1]+[['古英语 standende 等 → 中古英语 standing 对应形式','站立着；持续状态'],['英语 standing','站立、长期有效；地位声誉']],
 'a standing ovation 是起立鼓掌，a standing invitation 是长期有效的邀请，professional standing 是职业声望；a problem of long standing 是存在已久的问题。',
 'a standing ovation；a standing invitation；professional standing；of long standing。',
 'standing 形容持续有效，stationary 说不移动；a standing order 还可能是银行常设付款指示等固定术语，不能只译成站立的命令。',
 ('The audience gave the performers a standing ovation.','观众起立为表演者鼓掌。'),('Her professional standing grew over the years.','多年来，她的职业声望不断提高。'))
W('withstand','/wɪðˈstænd/，也 /wɪθˈstænd/','经受住；抵挡住',
 '压力推过来，人或物仍然撑住，没有被冲垮。',
 '接古英语 wiþstandan、中古英语 withstanden；with- 在这里保留 against“对抗”的旧义，不是现代最常见的“和……一起”。',STAND[:1]+[['古英语 wiþ- + standan → wiþstandan','抵住、对抗而立'],['中古英语 withstanden → withstand','承受、抵挡住']],
 'withstand pressure 是经受压力，withstand strong winds 是扛住强风。过去式和过去分词 withstood /wɪðˈstʊd/，跟 stand → stood 的模式走。',
 'withstand pressure；withstand heat；withstand the test of time。',
 'withstand 是经受住作用力，stand with someone 是与某人站在一起或支持某人；拆成两个词就不是同一结构。',
 ('The bridge was designed to withstand strong winds.','这座桥在设计时考虑了抵御强风。'),('The material can withstand repeated washing.','这种材料经得住反复洗涤。'))
W('understand','英 /ˌʌndəˈstænd/；美 /ˌʌndərˈstænd/','理解；懂；体谅；据悉、认为',
 '不是只听见一句话，而是知道对方究竟在说什么、为何这样说。',
 '接古英语 understandan、中古英语 understanden，可辨 under- 与 stand 的历史构成；但从站立怎样发展到理解，具体解释仍有争议。“站在下面所以理解”不是已证实词源。',
 [['古英语 understandan → 中古英语 understanden','已经表示理解、领会；更早语义桥梁有争议'],['英语 understand','懂含义、明白处境、据悉']],
 'understand the instructions 是懂说明，understand how someone feels 是体谅感受；I understand that ... 还可引出据我所知。过去式、过去分词 understood。',
 'understand why；understand how；make oneself understood；as I understand it。',
 'know 可以是知道事实，understand 更强调领会意义、原因或处境。构词联想可以辅助记忆，但对这个词不能把猜测画成确定的历史因果。',
 ('I understand the words, but not the joke.','这些词我都懂，可没听懂笑话。'),('Thank you for understanding why I needed more time.','谢谢你理解我为什么需要更多时间。'),sources=['https://en.wiktionary.org/wiki/understand','https://blog.oup.com/2022/02/the-incomprehensible-word-understand/'])
W('standard','英 /ˈstændəd/；美 /ˈstændərd/','标准；水准；标准的；旗帜〔历史〕',
 '大家需要同一个参照来判断尺寸、质量或做法，而不是各用各的尺。',
 '经古法语 estandart、相关中世纪拉丁语形式借入，早有军旗、集结标志义；更早是否站稳、固定地点等组合有不同分析。不能把现代拼写简单当 stand + ard，然后断言标准就是站得稳。',
 [['古法语 estandart 等 → 中古英语 standard','军旗、显著标志等早期义'],['英语 standard 的度量、规范用法','比较所依据的尺度；标准的']],
 'meet a standard 是达到标准，a high standard 是高水准，standard size 是标准尺寸。历史小说里 a royal standard 可能是王旗；这些义相关，但中间语义转化不全是确定单一路线。',
 'meet standards；set a standard；a high standard；standard practice。',
 'standard 是衡量规范或普通规格，standing 常是地位、长期有效；standard procedure 是标准程序，不写 standing procedure 来表达完全相同的概念。',
 ('The product meets the required safety standard.','产品符合所要求的安全标准。'),('This is standard practice in the workshop.','这是车间的常规做法。'),sources=['https://en.wiktionary.org/wiki/standard','https://www.etymonline.com/word/standard'])
W('nightstand','/ˈnaɪtstænd/','床头柜；床边小桌〔尤美〕',
 '晚上躺下前，眼镜、书和灯需要一个伸手就够得到的地方。',
 'night（夜间、睡眠时段）+ stand（支物的台架），按床边用途命名；不是 night + stand 的“熬夜站着”。',C('night','stand〔台架〕','nightstand','床边放东西的小柜、桌'),
 '美式常见，英式也常说 bedside table。可以有抽屉，也可以是一张简单小桌，重点在床边使用。',
 'a bedside nightstand；on the nightstand；a nightstand drawer。',
 'nightstand 是家具，night shift 是夜班；名字里 night 不意味着有人值夜站岗。',
 ('She left her glasses on the nightstand.','她把眼镜放在床头柜上。'),('A small lamp stood on each nightstand.','两边床头柜上各摆着一盏小灯。'))
W('newsstand','英 /ˈnjuːzstænd/；美 /ˈnuːzstænd/','报刊亭；售报摊',
 '路边摆出一排报纸杂志，过路人停下来买一份。',
 'news（新闻；这里借指报刊）+ stand（摊台），不是让新闻站立起来。news 本来以 s 结尾，不另把这里的 s 误认成连接后缀。',C('news','stand〔摊台〕','newsstand','出售报刊的摊亭'),
 '常在车站、街边、机场看到。on newsstands 可表示刊物正在市面发售，并不是所有刊物一定只通过小亭出售。',
 'a station newsstand；buy a paper at a newsstand；on newsstands。',
 'newsstand 是销售报刊的地点，newsletter 是定期通讯；stand 这一后半先把它定成摊台。',
 ('I bought a magazine at the station newsstand.','我在车站报刊亭买了本杂志。'),('The new issue reaches newsstands next week.','新一期杂志下周上市。'))
W('bandstand','/ˈbændstænd/','露天音乐台；乐队演奏台',
 '公园里搭一个供乐队演奏的高台，人们围在外面听。',
 'band（乐队）+ stand（台），常见亭状有顶结构，但名称重点在演出用途。',C('band','stand〔台〕','bandstand','供乐队演奏的平台'),
 '公园、广场音乐活动叙述常见，也可用于其他小型音乐舞台。a brass band on the bandstand 是铜管乐队在音乐台上演奏。',
 'a park bandstand；play on the bandstand；restore a bandstand。',
 'bandstand 供表演者站台，grandstand 多指观众看台；音乐人和观众所在区域不同。',
 ('A brass band performed on the park bandstand.','铜管乐队在公园音乐台演奏。'),('The town restored its old wooden bandstand.','小镇修复了旧木制音乐台。'))
W('handstand','/ˈhændstænd/','手倒立',
 '正常用脚支撑身体，这次反过来，由双手撑地让身体倒立。',
 'hand（手）+ stand（站立、支撑姿势），按支撑部位命名，不是手放在站台上。',C('hand','stand','handstand','用手支撑身体的倒立姿势'),
 'do a handstand 是做手倒立，hold a handstand 是保持姿势。体操比赛、舞蹈、动作照片的叙述里都可见；也能作动词说做手倒立。',
 'do a handstand；hold a handstand；a handstand position。',
 'handstand 靠手支撑，headstand 常称头倒立；两者不能因为身体都倒过来就当同一个姿势。',
 ('The gymnast held a handstand for several seconds.','体操运动员保持手倒立几秒钟。'),('The photograph captures her in a handstand.','照片拍下了她手倒立的瞬间。'))
W('kickstand','/ˈkɪkstænd/','自行车、摩托车支架；折叠支撑架',
 '停车后放下一根撑杆，车就能靠它立住，不必一直用手扶。',
 'kick（脚踢、脚拨的动作）+ stand（支撑架），按常用脚拨下的自行车部件命名，后扩展为设备的折叠支撑。',C('kick','stand〔支架〕','kickstand','可放下使车辆、设备立住的支撑杆'),
 'a bicycle kickstand 是车撑，a phone kickstand 是手机支架；后者不需要真的用脚去踢。',
 'lower the kickstand；a folding kickstand；a built-in kickstand。',
 'kickstand 说明支撑功能，kickstart 是启动、促使开始的另一词；别把车撑误当启动器。',
 ('He lowered the kickstand before getting off the bike.','他下自行车前放下了车撑。'),('The tablet case has a folding kickstand.','平板保护套带有折叠支架。'))
R('B2545','站立、支住；位置与坚持','STAND：支住身体或事物，留在某个位置','人站着，架子支着东西，面对压力仍站得住，就有坚持和承受的感觉。',
 'stand 接古英语 standan，经中古英语延续；stand → stood。standing、withstand 可辨动作、状态和旧前缀。understand、standard 虽可放在历史关联中学习，意义形成不能只靠现代字面拼出来。',
 '先看 stand、standing、withstand；standpoint、standstill、grandstand 为共享讲解。支架用途再分 nightstand、newsstand、bandstand、handstand、kickstand。understand 的语义桥梁和 standard 的更早分析有争议，单列解释。',
 [['基本状态、承受与位置','stand · standing · withstand · standstill · standpoint'],['台架、场所与支撑','nightstand · newsstand · bandstand · grandstand · handstand · kickstand'],['历史扩展需谨慎拆解','understand · standard']],
 'nightstand 家具、newsstand 摊亭、bandstand 演奏台。understand 早已表示理解，不能说站在下面所以懂了。withstand 的 with- 保留对抗义。',
 'The old bandstand still stands, having withstood years of wind and rain.\n\n旧音乐台经受多年风雨，如今仍然立着。','stand standing withstand standstill standpoint nightstand newsstand bandstand grandstand handstand kickstand understand standard')
if __name__=='__main__':save('continuation_20261028_w',ROOTS,WORDS)
