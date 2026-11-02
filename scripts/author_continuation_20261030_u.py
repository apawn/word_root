"""Charge and touch: physical beginnings and everyday abstract meanings."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
CH=[['拉丁 carrus〔车〕→ 晚期拉丁 carricāre','把货装上车、装载'],['法语 chargier／charge → 英语 charge','负担、装入 → 责任、费用、指控、电荷等分支']]
def H(f,m):return CH+[[f,m]]
W('charge','英 /tʃɑːdʒ/；美 /tʃɑːrdʒ/','收费；充电；负责；指控；冲向；费用、电荷',
 '最初是把负担装上去；钱记到你账上、责任交到你身上，都很好理解。充电和冲锋则记各自的固定场景。',
 '经法语接晚期拉丁 carricāre 装车，最终接 carrus 车。费用、责任、指控、电学等义在不同阶段发展；冲锋义的具体连接有讨论，不编成唯一确定画面。',CH,
 'charge a fee 收费，charge a phone 充电，be in charge of 负责，charge someone with an offence 指控某人，charge towards 冲向。free of charge 免费。',
 'charge a fee；charge a phone；in charge of；free of charge。',
 'charge 收费，pay 付款，是交易两边的动作；in charge of 负责，in the charge of 由别人负责，方向相反。',
 ('The museum does not charge an entrance fee.','博物馆不收入场费。'),('Who is in charge of the project?','谁负责这个项目？'),sources=['https://www.etymonline.com/word/charge','https://en.wiktionary.org/wiki/charge#English'])
W('charger','英 /ˈtʃɑːdʒə/；美 /ˈtʃɑːrdʒər/','充电器；另有冲锋战马等用法',
 '把电能送进设备的东西，最熟悉就是手机充电器。',
 'charge + -er，执行某种 charge 功能的主体。不同义项有各自历史；现代设备语境优先理解成充电器。',H('charge + -er → charger','执行充电功能的设备；另有同族旧用法'),
 'a phone charger 手机充电器，a wireless charger 无线充电器，a charger cable 日常常说充电线。',
 'a phone charger；a wireless charger；connect the charger。',
 'charger 充电设备，battery 储能部件；charging cable 是传输连接线，日常有时混称，具体买什么要看对象。',
 ('I left my phone charger at home.','我把手机充电器落在家里了。'),('The charger has two USB ports.','充电器有两个USB接口。'))
W('charging','英 /ˈtʃɑːdʒɪŋ/；美 /ˈtʃɑːrdʒɪŋ/','充电；收费；冲向〔charge 的 -ing 形式〕',
 '同样一个词形，电池在补电，商店在要钱，公牛在冲过来；看动作对象就清楚。',
 'charge 去末尾 e + -ing。可以是活动名词、进行时一部分或修饰语，不等于每次都是充电专名。',H('charge + -ing → charging','充电、收费、冲向等动作的进行或活动'),
 'a charging station 充电站，wireless charging 无线充电；charging extra for delivery 另收配送费。',
 'a charging station；wireless charging；charging extra。',
 'charging 是过程，charger 是设备；The phone is charging 与 The charger is broken 一个讲状态，一个讲物件。',
 ('The phone is charging on the desk.','手机在桌上充电。'),('The hotel is charging extra for late checkout.','酒店对延迟退房额外收费。'))
W('chargeable','英 /ˈtʃɑːdʒəbl/；美 /ˈtʃɑːrdʒəbl/','需收费的；可记账的；可充电的〔较宽泛〕',
 '一项服务要收钱，一笔费用能记到某个项目账上，都可以用 chargeable。',
 'charge + -able，后缀表示可、需按相应方式处理，具体接的是收费、记账等哪一义要看语境。',H('charge + -able → chargeable','可收取、应计入费用；可接受充电'),
 'a chargeable service 收费服务，expenses chargeable to the project 可计入项目的费用。电池可反复充电常用 rechargeable 更清楚。',
 'a chargeable service；chargeable hours；chargeable to an account。',
 'chargeable 不等于有价值的 valuable；它常说费用归属或是否收费。free of charge 与 chargeable 在收费语境相反。',
 ('Technical support is a chargeable service after the first year.','第一年后技术支持是收费服务。'),('These expenses are chargeable to the research project.','这些费用可记入研究项目账下。'))
W('recharge','英 /ˌriːˈtʃɑːdʒ/；美 /ˌriːˈtʃɑːrdʒ/〔动词〕','重新充电；恢复精力；补充',
 '电量用掉了再补上；人累了休息一下，也像给自己重新充电。',
 '借古法语 rechargier，re- 再次 + chargier 装载。电学义和恢复精力义是后来的用法，不把这个词整体当作手机发明后才出现。',CH[:1]+[['古法语 re- + chargier → recharge','再次装载 → 重新充电、恢复精力']],
 'recharge a battery 给电池再充电，recharge your batteries 恢复精力。地下水 recharge 另可指补给，具体看学科。',
 'recharge a battery；recharge your batteries；take time to recharge。',
 'charge 一次充电，recharge 强调再补充；人说 recharge 不表示身体真的插了电源。',
 ('I need to recharge the camera battery.','我得给相机电池再充电。'),('A quiet weekend helped her recharge.','一个安静的周末帮她恢复了精力。'))
W('rechargeable','英 /ˌriːˈtʃɑːdʒəbl/；美 /ˌriːˈtʃɑːrdʒəbl/','可反复充电的',
 '电用完后能补进去再用，这是物品的一项设计能力。',
 'recharge + -able，去末尾 e 接 -able。表示可重新充电，不能只因为此刻有电就叫 rechargeable。',H('recharge + -able → rechargeable','能够再次充电使用的'),
 'rechargeable batteries 充电电池，a rechargeable lamp 可充电灯。常描述设备或储能部件的能力。',
 'rechargeable batteries；a rechargeable lamp；a rechargeable device。',
 'charged 已经有电、充过电，是状态；rechargeable 可以再充，是能力。两者可以同时成立。',
 ('The lamp has a rechargeable battery.','这盏灯装有可充电电池。'),('We use rechargeable batteries in the recorder.','我们在录音机里用充电电池。'))
W('overcharge','英 /ˌəʊvəˈtʃɑːdʒ/；美 /ˌoʊvərˈtʃɑːrdʒ/〔动词〕','多收费；过度充电；过量装入',
 '该收十元收成二十元，是账上的过头；电池补得超过合适限度，是充电上的过头。',
 '中古英语已有相应组合，现代对应 over- 过度 + charge。分别接收费、充电、装载等分支。',H('over- + charge → overcharge','收、充、装得过多'),
 'overcharge a customer 多收顾客钱，be overcharged 被多收费，overcharge a battery 过度充电。名词 an overcharge 可指多收部分，重音常前移。',
 'overcharge a customer；be overcharged；an overcharge on the bill。',
 'overcharge 多收，不一定就是整项商品价格贵；undercharge 少收是反方向。具体是否错误需看约定费用。',
 ('The restaurant accidentally overcharged us.','餐馆不小心多收了我们的钱。'),('The bill included an overcharge of twenty dollars.','账单里有多收的二十美元。'))
R('B3891','装载的旧义与责任、费用、充电','CHARGE：负担交上去；电能补进去','charge 后接 charger、charging、chargeable；recharge → rechargeable 一起，overcharge 看超过哪条限度。',
 '装车词经法语进入英语，责任、费用、电学等多支逐步发展。不把现代各义都编成同一种装货动作。',
 'charge → charger、charging、chargeable；re- + charge → recharge → rechargeable；over- + charge；supercharge 已精讲共享。',
 [['基本动作、主体、过程与收费性质','charge · charger · charging · chargeable'],['再次与可重复能力','recharge · rechargeable'],['超过与加强','overcharge · supercharge']],
 'charge 收、pay 付；charger 设备、charging 过程；rechargeable 能力；in charge of 负责。',
 'The rechargeable lamp is charging, but there is no extra charge.\n\n这盏充电灯正在充电，而且没有额外收费。',
 'charge charger charging chargeable recharge rechargeable overcharge supercharge')
TO=[['古法语 tochier → 中古英语 touchen','触碰、敲击；更早来源有讨论'],['现代 touch','接触 → 影响情感、联系、少量润色']]
def TH(f,m):return TO+[[f,m]]
W('touch','/tʌtʃ/','触碰；打动；联系；一点点、点缀',
 '手碰到物体，话碰到心里；两人保持联系，也像关系还接得上。',
 '经中古英语接古法语 tochier 触碰、敲击，更早来源有拟声等解释。感动义是已固定的情感延伸，名词还能说少量、润色。',TO,
 'touch the screen 触屏，be touched by 被感动，keep in touch 保持联系，a touch of colour 一点色彩，a nice touch 恰到好处的小细节。',
 'touch the screen；keep in touch；a touch of；a nice touch。',
 'touch 只需接触，hold 拿住、握住；keep in touch 说保持联系，不要求身体接触。',
 ('Touch the screen to continue.','触碰屏幕继续。'),('The flowers were a lovely personal touch.','这些花增添了温馨又有心意的细节。'),sources=['https://www.etymonline.com/word/touch','https://en.wiktionary.org/wiki/touch#English'])
W('touched','/tʌtʃt/','被触碰；受到感动的',
 '别人一份心意真的碰到你的心里，让你感到温暖、感激。',
 'touch + -ed，/tʃ/ 后的 -ed 读 /t/。既是过去式、分词，也固定用作感动的形容词。',TH('touch + -ed → touched','已接触；心里受到打动'),
 'be touched by someone’s kindness 被某人的善意感动，deeply touched 深受感动。',
 'be touched by；deeply touched；touched by the gesture。',
 'touched 常描述感受的人，touching 常描述引起感动的事物；a touching letter made me feel touched。',
 ('I was deeply touched by her kindness.','她的善意让我深受感动。'),('He was touched that his old friends had remembered.','老朋友们还记得，他很感动。'))
W('touching','/ˈtʌtʃɪŋ/','感人的；正在接触的',
 '一封信、一个小举动把人的情绪轻轻碰动，就说它很 touching。',
 'touch + -ing，感情影响义固定为形容词感人的；作为普通动词形式也可只是物理接触。',TH('touch + -ing → touching','正在触碰；能够打动情感的'),
 'a touching story 感人故事，a touching gesture 感人举动；The branches are touching 只是树枝碰在一起。',
 'a touching story；a touching gesture；a touching tribute。',
 'touching 形容引起感受的对象，touched 形容感到被打动的人。感动不只悲伤，也可以来自温暖与关爱。',
 ('It was a touching gesture from an old friend.','这是老朋友一个感人的举动。'),('The two branches were touching above the path.','两根树枝在小路上方碰在一起。'))
W('untouched','/ʌnˈtʌtʃt/','未动过的；原状未改的；未受影响的',
 '盘里的饭没人动，林地没被改造，或者某处没受灾害影响：都保留着原来的状态。',
 'un- 不 + touched，否定接触、食用或影响等不同含义。不能把所有情境都理解成手指没碰到。',TH('un- + touched → untouched','没动过、没吃过；未改变、未受影响'),
 'leave food untouched 食物原封没吃，untouched countryside 未受开发的乡野，remain untouched 保持未受影响。',
 'leave untouched；untouched food；remain untouched by。',
 'untouched 不必是全新；老文件原封未动也可说 untouched。untouched by the news 可说情绪未受影响，语境可能带批评。',
 ('She left most of her lunch untouched.','她午饭大部分都没动。'),('The fire left this part of the forest untouched.','火灾没有波及这片森林。'))
W('touchy','/ˈtʌtʃi/','易生气的；敏感、需小心处理的',
 '像一碰就会弹起来：人容易被冒犯，话题稍不注意就引发不快。',
 '可能由 tetchy 易恼怒的变形而来，受 touch 影响；现代看起来像 touch + -y，但不把这种表面分析当唯一确定源头。',
 [['较早 tetchy〔易恼怒〕','来源未完全确定'],['可能受 touch 影响 → touchy','易被冒犯；敏感、难处理']],
 'a touchy subject 敏感话题，be touchy about one’s age 对年龄问题敏感。形容设备也可说一碰就反应、难控制。',
 'a touchy subject；touchy about；a touchy issue。',
 'touching 感人的，touchy 敏感易恼；一句 touching story 通常褒情感，一个 touchy subject 则提醒拿捏方式。',
 ('Money is a touchy subject in their family.','钱在他们家是个敏感话题。'),('He is touchy about criticism of his work.','他对别人批评自己的工作很敏感。'),sources=['https://www.etymonline.com/word/touchy','https://en.wiktionary.org/wiki/touchy#English'])
W('touchstone','英 /ˈtʌtʃstəʊn/；美 /ˈtʌtʃstoʊn/','试金石；检验标准',
 '金属在石上擦出一道痕，用来比较成色；抽象地说，拿来检验好坏的标准。',
 'touch 在旧金属检验用法中有试验义 + stone 石头。真实试金过程留下擦痕，再发展出判断品质的比喻。',TH('touch〔检验〕+ stone → touchstone','试金石 → 衡量、检验的标准'),
 'a touchstone for quality 质量检验标准，a touchstone of good design 好设计的衡量标准。常用于讨论评价依据。',
 'a touchstone for；a touchstone of；a cultural touchstone。',
 'touchstone 是检验参照，milestone 里程碑强调阶段成就；两个石头比喻的作用不同。',
 ('Clarity became the touchstone for every design decision.','清晰易懂成为每项设计决策的检验标准。'),('The jeweller demonstrated how a touchstone was used to test gold.','珠宝匠演示了怎样用试金石检验黄金。'),sources=['https://www.etymonline.com/word/touchstone','https://en.wiktionary.org/wiki/touchstone#English'])
W('touchpad','/ˈtʌtʃpæd/','触控板',
 '手指在面板上滑动、轻点，设备把触碰转成光标或操作。',
 'touch 触碰 + pad 面板，按输入方式命名。trackpad 已精讲，两个词常说同一类装置。',TH('touch + pad → touchpad','靠触碰输入的面板 → 触控板'),
 'a laptop touchpad 笔记本触控板，disable the touchpad 关闭触控板，touchpad gestures 触控板手势。',
 'a laptop touchpad；touchpad gestures；use the touchpad。',
 'touchpad 和 trackpad 常可指同类设备；touchscreen 是显示内容又可触控的屏幕，不都等于独立触控板。',
 ('Use two fingers on the touchpad to scroll.','用两根手指在触控板上滑动来滚动页面。'),('She prefers a mouse to the laptop’s touchpad.','比起笔记本触控板，她更喜欢鼠标。'))
W('touchline','/ˈtʌtʃlaɪn/','球场边线〔尤足球、橄榄球〕',
 '球场长边上的界线，球越过去就出了这一侧的比赛区域。',
 'touch〔球类中场外区域的用法〕+ line 线，固定表示场地侧边界；不是所有被摸到的线。',TH('touch〔场外区域〕+ line → touchline','球场侧边界线'),
 'near the touchline 边线附近，cross the touchline 越过边线，on the touchline 常描述教练在场边。',
 'near the touchline；cross the touchline；stand on the touchline。',
 'touchline 常侧边，goal line 球门线在端部；具体球类规则与边界术语要按项目理解。',
 ('The ball rolled over the touchline.','球滚出了边线。'),('The coach shouted instructions from the touchline.','教练在场边大声指挥。'))
R('B2742','触碰、打动、敏感与联系','TOUCH：接触到物体，也能触动人心','touch → touched、touching、untouched 挨着；touchy 另交代不确定历史，接试金石、触控板、边线。',
 '法语触碰词进入英语，情感和联系义发展很早。touchy 可能受 touch 影响而从 tetchy 改形，不硬说一定由现代 touch 加 -y 新造。',
 'touch → touched → untouched；touch → touching；touchy〔可能重析〕；touch + stone/pad/line；touchdown 已精讲共享。',
 [['基本接触与情感','touch · touched · touching · untouched'],['敏感与检验','touchy · touchstone'],['设备与球场','touchpad · touchline · touchdown']],
 'touched 人被感动，touching 事物感人，touchy 易恼；touchpad 与 trackpad 常同类；touchstone 不等于 milestone。',
 'The touching message left her deeply touched.\n\n这条感人的留言让她深受感动。',
 'touch touched touching untouched touchy touchstone touchpad touchline touchdown')
if __name__=='__main__':save('continuation_20261030_u',ROOTS,WORDS)
