"""Height, names in grids, lots, blankness and floor coverings."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1696':dict(words=['tall','taller','tallest'],label='tall → taller → tallest：向上长的高度',note='tall 说人、树、建筑等自身从底到顶的高度；比较形式按规则加 er、est，不双写已有的双 l。'),
 'B3714':dict(words=['roast','roster'],label='roast 与 roster：烤架、格子、名单',note='roster 经荷兰语 rooster 借入，其表格义常解释为烤架的格子转喻；与 roast 经法语接日耳曼语烤制词是不同借入路线。'),
 'B4061':dict(words=['lot','lottery'],label='lot → lottery：抽签与机会分配',note='lottery 经罗曼语形式接日耳曼语 lot 签、份额词族，现代既说彩票抽奖，也比喻结果很看运气。'),
 'A1740':dict(words=['blank','blankly'],label='blank → blankly：表面空白与茫然表情',note='blank 经法语 blanc 白，发展为留白、无内容；blankly 常说表情没有反应、茫然地。'),
 'A1698':dict(words=['blank','blanket'],label='blank 与 blanket：同一白色词的不同发展',note='blank 接法语 blanc 白，blanket 接其小称、白色毛织物名称；现代 blanket 不必是白色，也不是空白加通用 et。'),
 'A1741':dict(words=['carpet','carpeting'],label='carpet → carpeting：铺地毯、地毯材料',note='carpet 经法语、拉丁相关厚织物名称，通常联系拉丁 carpere 拔取、梳理材料；不接希腊 carp- 果实或手腕。carpeting 是规则 ing 形式及材料集合名。'),
}
W('tall','英 /tɔːl/；美常 /tɔːl/、/tɑːl/','高的；有……身高的；夸大的〔如 tall tale〕',
 '一个人从脚到头、一棵树从根边到树梢，往上长得高，可以说 tall。它常看物体自身的底到顶。',
 '中古英语 tal 曾有俊美、英勇、大等义，现代高度义较晚突出，通常与古英语相关词联系；意义变化并非每一步都能直译。今天把 tall 当完整词，不强拆 ta + ll。',
 [['古英语相关材料 → 中古英语 tal','较早有活跃、英勇、俊美等意思'],['早期现代英语 tall','人、物自身高度大；也用于夸张故事']],
 'a tall person 高个子；a tall tree 高树；two metres tall 两米高；a tall tale 夸张、不大可信的故事。比较 taller，最高 tallest。',
 'stand tall；grow tall。','tall 常说自身高度；high 也可说离地位置、水平或程度。a tall building 是高楼，a high window 是位置较高的窗户。',
 ('A tall tree stands beside the gate.','门旁立着一棵高树。'),('The shelf is almost two metres tall.','这个架子差不多有两米高。'),sources=['https://www.etymonline.com/word/tall','https://en.wiktionary.org/wiki/tall#English'])
W('taller','英 /ˈtɔːlə/；美 /ˈtɔːlər/、/ˈtɑːlər/','更高的；tall 的比较级',
 '把两个人站在一起，或比较同一棵树去年和今年的高度，高出一些的一方就是 taller。',
 'tall + 比较级 -er。tall 已有 ll，直接接 er，写 taller；不是再加一个 l。现代形式表示高度比较。',
 [['tall','自身从底到顶较高'],['tall + -er → taller','与另一人、物或先前状态相比更高']],
 'taller than ... 比……高；a little taller 高一点；much taller 高得多；ten centimetres taller 高十厘米。',
 'grow taller；look taller。','比较级通常不再叠加 more：taller 已经有更高的意思。说高出多少，可以直接在前面放差值：five centimetres taller。',
 ('My sister is a little taller than me.','我姐姐比我高一点。'),('The plant is much taller than it was last month.','这株植物比上个月高多了。'),sources=['https://www.etymonline.com/word/tall','https://en.wiktionary.org/wiki/taller#English'])
W('tallest','英 /ˈtɔːlɪst/；美 /ˈtɔːlɪst/、/ˈtɑːlɪst/','最高的〔身高、物体自身高度〕；tall 的最高级',
 '把一组人或建筑排着比较，从底到顶最高的那一个，就是 the tallest。比较范围要从后面的说明或上下文找。',
 'tall + 最高级 -est，直接接在已有 ll 后。与 taller 一起记：tall 高、taller 更高、tallest 其中最高。',
 [['tall → taller','高度性质 → 与另一对象相比更高'],['tall + -est → tallest','在限定范围内高度最大']],
 'the tallest building in the town 镇上最高的建筑；the tallest person in the class 班里个子最高的人；one of the tallest trees 最高的树之一。',
 'the tallest of the three；our tallest player。','最高级的范围很重要：镇上最高不等于全国最高。one of the tallest 后面的可数名词要用复数，如 buildings。',
 ('This is the tallest tree in our garden.','这是我们花园里最高的一棵树。'),('She is one of the tallest players on the team.','她是队里个子最高的队员之一。'),sources=['https://www.etymonline.com/word/tall','https://en.wiktionary.org/wiki/tallest#English'])
W('roster','英 /ˈrɒstə/；美 /ˈrɑːstər/','人员名单；值班表、轮值表；队员名单',
 '谁今天值班、谁明天接替，或者谁在这支队伍里，把名字列成表，就是 roster 的常见用途。',
 '借荷兰语 rooster 表格、名单，较早是烤架；通常解释为烤架的格子让人联想到纸上划出的表格。它与 roast 的烤制词族相关，但不是英语 roast 加 -er 表示烤东西的人。',
 [['荷兰语烤制、烤架词族 → rooster','烤架的条格 → 表格、名单〔常见解释〕'],['荷兰 rooster → 英语 roster','先常见轮值名单，后扩大为人员名单']],
 'a duty roster 值班表；a team roster 队员名单；the staff roster 员工名单、排班表；add someone to the roster 把某人列入名单。',
 'on the roster；check the roster。','roster 的人名单不一定按班次轮换，体育里常是队员名单。rooster 多一个 o，通常是公鸡，来源是 roost 栖息的动词线，不能混写。',
 ('Check the roster to see who is working tonight.','查一下排班表，看看今晚谁上班。'),('Her name was added to the team roster.','她的名字被加进了队员名单。'),sources=['https://www.etymonline.com/word/roster','https://en.wiktionary.org/wiki/roster#English'])
W('lottery','英 /ˈlɒtəri/；美 /ˈlɑːtəri/','彩票抽奖、博彩抽奖；很看运气的事',
 '把机会按抽签、抽号码分出去，谁拿到奖并不靠先后顺序，这是一种 lottery。比喻时常说结果主要看运气。',
 '经罗曼语彩票名称联系日耳曼语 lot 签、份额词族；意大利 lotteria、法语 loterie 与相关荷兰语形式有各自传入关系。与英语 lot 同族，现代把 lottery 整体记住，再与 lot 的抽签义对照。',
 [['日耳曼语 lot 签、份额词族','用签决定分给谁'],['欧洲相关彩票名 → 英语 lottery','机会抽奖；比喻结果难预测、看运气']],
 'a lottery ticket 彩票；win the lottery 彩票中奖；a lottery draw 彩票开奖；allocation by lottery 通过抽签分配。',
 'enter a lottery；a complete lottery。','lottery 可以是具体抽奖，也能比喻结果全凭运气。This process is a lottery 不一定真有人卖彩票，而是说过程缺乏可预测性。',
 ('The story begins with a man who wins the lottery.','故事从一个彩票中奖的人讲起。'),('Getting a seat on the crowded bus felt like a lottery.','在拥挤公交车上找到座位，感觉全凭运气。'),sources=['https://www.etymonline.com/word/lottery','https://en.wiktionary.org/wiki/lottery#English'])
W('blank','/blæŋk/','空白的、未填写的；茫然的；空白处；一时想不起来〔动词〕',
 '纸上本该有内容的地方还空着，是 blank；别人问你问题，脑子里一时什么也抓不到，也可说 your mind went blank。',
 '经古法语 blanc 白、发亮，较早接日耳曼语白亮词。英语先有白、无色义，后来突出未写内容的空白，再用于无表情、想不起来的状态。',
 [['日耳曼语白亮词 → 法语 blanc → blank','白、浅色、无色'],['未写内容的白面 → 空白及比喻','未填、未记录；表情或头脑一时无内容']],
 'a blank page 空白页；leave it blank 留空；a blank expression 茫然表情；fill in the blanks 填空；draw a blank 一无所获、想不起来。',
 'go blank；a blank screen。','blank 强调预期内容缺失，empty 更广地说里面没有东西。a blank page 可以有纸张颜色，关键是还没有相应内容。',
 ('Please leave this section blank.','这一栏请留空。'),('My mind went blank when I stood up to speak.','我站起来发言时，脑子突然一片空白。'),sources=['https://www.etymonline.com/word/blank','https://en.wiktionary.org/wiki/blank#English'])
W('blankly','/ˈblæŋkli/','茫然地、毫无表情地',
 '你说了一句话，对方脸上没有理解后的反应，只是直直看着你。这种空着似的神情，可以用 blankly。',
 'blank + 副词词尾 -ly。blank 的无内容、无表情义转成动作方式，常与 stare、look 等描述目光的动词连用。',
 [['blank 的空白、无表情义','没有显出理解、反应'],['blank + -ly → blankly','以茫然、无表情的方式看、回答']],
 'stare blankly 茫然盯着；look blankly at someone 茫然看着某人；gaze blankly 茫然凝视。',
 'stare blankly at the screen；look back blankly。','blankly 不等于所有情况下都表示发呆；可能是不理解、惊讶后失去反应，也可能刻意面无表情，具体原因要看上下文。',
 ('He stared blankly at the question on the screen.','他茫然地盯着屏幕上的问题。'),('She looked at me blankly, as if she had never heard the name.','她茫然地看着我，好像从没听过这个名字。'),sources=['https://www.etymonline.com/word/blank','https://en.wiktionary.org/wiki/blankly#English'])
W('carpet','英 /ˈkɑːpɪt/；美 /ˈkɑːrpɪt/','地毯；给……铺地毯；像地毯一样覆盖',
 '先想地上铺着一层厚织物。再把这个整片盖住地面的画面用到落叶、花朵等，就能理解 a carpet of leaves。',
 '经古法语 carpite 与中古拉丁等厚织物名称，通常联系拉丁 carpere 拔取、梳理材料。英语较早还能说桌布、床罩等，后来地面覆盖物成为主要意思。',
 [['拉丁相关厚织物名 → 法语 carpite → carpet','较早为厚布，可覆盖桌、床等'],['现代 carpet','地毯；转作动词铺毯、整片覆盖']],
 'a thick carpet 厚地毯；lay a carpet 铺地毯；a carpet of flowers 一片如毯的花；sweep something under the carpet 掩盖问题。',
 'carpet the room；a red carpet。','rug 通常是较小、可移动的铺地毯，carpet 可说整间房铺设的地毯，也能指一块毯。来源里的 carpere 与希腊 carp- 果实、手腕不是同一个词根。',
 ('The room has a thick blue carpet.','房间里铺着厚厚的蓝色地毯。'),('A carpet of leaves covered the path.','落叶像地毯一样铺满小路。'),sources=['https://www.etymonline.com/word/carpet','https://en.wiktionary.org/wiki/carpet#English'])
W('carpeting','英 /ˈkɑːpɪtɪŋ/；美 /ˈkɑːrpɪtɪŋ/','地毯材料、地毯铺装；铺地毯；carpet 的 -ing 形式',
 '选装修材料时，把整片地毯材料统称为 carpeting；说工人正在铺地毯，也可用同一个形式。',
 'carpet + -ing，常见标准写法不双写 t，因为最后一节不重读。动词名词发展为铺毯动作和地毯材料的集合表达。',
 [['carpet 名词 → carpet 动词','地毯 → 用地毯覆盖'],['carpet + -ing → carpeting','铺地毯动作；铺装用的地毯材料']],
 'new carpeting 新地毯铺装、材料；replace the carpeting 更换地毯；soft carpeting 柔软的地毯材料；carpeting the stairs 给楼梯铺地毯。',
 'office carpeting；install new carpeting。','carpeting 说材料通常不可数；carpets 能数一块块地毯。They are carpeting ... 中则是动词进行形式，看后面是否接铺设对象。',
 ('We chose soft carpeting for the bedroom.','我们为卧室选了柔软的地毯材料。'),('They are carpeting the stairs this afternoon.','他们今天下午要给楼梯铺地毯。'),sources=['https://www.etymonline.com/word/carpet','https://en.wiktionary.org/wiki/carpeting#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vn',ROOTS,WORDS)
 extend_lessons()
