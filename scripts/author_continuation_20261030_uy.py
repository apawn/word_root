"""Numbers, games, interaction, overcoming and furnishing."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0349':dict(words=['dozen'],label='dozen：两个加十个的一打',note='dozen 经法语 dozaine、doze 接拉丁 duodecim 十二，含 duo 二与 decem 十；现代不能把 dozen 当英语 do 加 zen。'),
 'C0307':dict(words=['dozen'],label='duodecim 的十：十二经法语形成 dozen',note='拉丁 duo 二与 decem 十组成十二，法语数词与集合形式后来借为 dozen，一打固定十二。'),
 'C1487':dict(words=['tennis'],label='tennis：持有、接取动词的法语命令形式',note='tennis 通常联系法语 tenez 接着、接住，为 tenir 持有的命令形式，上接拉丁 tenere；以发球呼声命名的解释常见但并非无争议。'),
 'C0108':dict(words=['base','baseball'],label='baseball：围绕垒位进行的球类运动',note='baseball 是 base 垒位与 ball 球的英语复合；base 这一线接站立处、基础材料，ball 球另来自日耳曼语，不接希腊投掷词根。'),
 'C0609':dict(words=['interact','interaction'],label='interaction：彼此发生作用',note='inter- 之间、相互与 action 行动、作用结合；既可说人交流，也可说物质、系统之间相互影响。'),
 'B2841':dict(words=['come','overcome','overcame'],label='overcome：越过阻力而胜过、克服',note='overcome 承接古英语复合动词 ofercuman；现代过去式 overcame、过去分词 overcome，与 come 的不规则变化对应。'),
 'B2435':dict(words=['odd','odds'],label='odds：差别、不均势与可能性',note='odds 接 odd 的旧名词化、复数用法，发展出差异、优势、机会等分支；at odds、against the odds 按固定结构理解。'),
 'B2475':dict(words=['stock','stocks'],label='stocks：储备、股票与另一个木制刑具分支',note='stock 的储备、资本分支有复数 stocks，旧木块、木架材料也留下 stocks 刑具义；同形动词还可说备货。'),
 'B4201':dict(words=['bond','bonds'],label='bonds：联系、化学键与债券',note='bond 的系住、约束线发展出关系、化学连接和有约束力的债务凭证；复数 bonds 各按领域判断。'),
 'B4383':dict(words=['counter','encounter'],label='encounter：从迎面相对到遇上',note='encounter 经法语接晚期拉丁 incontra 在面前，含 in 与 contra 相对；与表示对抗的 counter 有历史联系，不接计数、柜台的另一来源。'),
 'B3837':dict(words=['frame','furnish','furnished','unfurnished','furnishings'],label='做成、备齐的历史词族：furnish',note='furnish 经法语提供、装备词借入，较早接日耳曼促进、做成材料，与 frame 的动词历史同族；词形已变化，不是英语 frame 直接加后缀。'),
 'A1996':dict(words=['furnish','furniture'],label='furniture：法语供应名词到家具统称',note='furniture 借法语 fourniture 供应、装备等名词，与 fournir 同族；英语后专门化为家具，不是 furnish 去 sh 的现代随意拼写规则。'),
}
W('dozen','/ˈdʌzən/','一打、十二个；dozens of：几十、许多',
 '鸡蛋一盒十二个，就是 a dozen。把十二看作一组来数，two dozen 就是两组、二十四个。',
 '借法语 dozaine 一组十二，来自 doze 十二及集合后缀；更早拉丁 duodecim 含 duo 二与 decem 十。现代 dozen 的日常精确数值仍是十二。',
 [['拉丁 duo + decem → duodecim','二与十 → 十二'],['法语 doze／dozaine → dozen','十二 → 以十二为一组的数量']],
 'a dozen eggs 一打鸡蛋；two dozen chairs 二十四把椅子；half a dozen 六个；dozens of people 几十人、许多人。',
 'a dozen times；several dozen。','确切数词后通常不用复数 s：three dozen eggs。dozens of 是大约数、许多：dozens of eggs；两种结构别混成 three dozens eggs。',
 ('We bought a dozen eggs and half a dozen apples.','我们买了一打鸡蛋和六个苹果。'),('Dozens of people waited outside the hall.','几十个人在大厅外等候。'),sources=['https://www.etymonline.com/word/dozen','https://en.wiktionary.org/wiki/dozen#English'])
W('tennis','/ˈtenɪs/','网球；相关旧式球类运动',
 '今天先记隔网用球拍对打的网球。名字通常被解释为发球时提醒对手的一声接着，老线索是接取、持有。',
 '经中古英语 tennis 等形式，通常联系古法语 tenez、英法语 tenetz，为 tenir 持有、接取的命令形式，上接拉丁 tenere。发球呼声转成运动名的解释常见，但历史上有不同看法；旧运动与现代网球也有变化。',
 [['法语 tenir → tenez 等命令形式〔通常解释〕','持有、接取 → 接着、接住'],['英语 tennis','旧式球类名称 → 现代网球名称']],
 'play tennis 打网球；a tennis court 网球场；a tennis racket 网球拍；a tennis match 网球比赛。',
 'tennis lessons；a tennis player。','运动名称通常直接说 play tennis，不加 the。tennis 与 table tennis 乒乓球不同；词尾 s 是历史拼写的一部分，不是现在给一个 tenni 加复数。',
 ('We play tennis at the park on Sundays.','我们星期天在公园打网球。'),('The tennis court was too wet to use.','网球场太湿，没法使用。'),sources=['https://www.etymonline.com/word/tennis','https://en.wiktionary.org/wiki/tennis#English'])
W('baseball','/ˈbeɪsbɔːl/；美亦 /ˈbeɪsbɑːl/','棒球运动；棒球',
 '击球后沿着几个 base 垒位跑进，这些垒位是运动名称里的线索。baseball 可以指这项运动，也可以数一颗球。',
 'base 垒位 + ball 球，英语复合词。base 的基础、站位线经法语、拉丁语接希腊 basis；ball 球来自日耳曼语，不能因为球会被投出，就改说它来自希腊 ballein。',
 [['英语 base + ball','垒位 + 球'],['复合 baseball','围绕垒位进行的球类运动；所用的球']],
 'play baseball 打棒球；a baseball game 棒球比赛；a baseball bat 棒球棒；catch a baseball 接住一个棒球。',
 'a baseball team；a signed baseball。','play baseball 中通常是运动，不加 a；hold a baseball 中是一个球，可以数。base 在这个运动名中是垒位，不是卑鄙的那个另源形容词。',
 ('He keeps a signed baseball on his desk.','他在桌上放着一个签名棒球。'),('The children played baseball after school.','孩子们放学后打了棒球。'),sources=['https://en.wiktionary.org/wiki/baseball#English'])
W('interaction','/ˌɪntərˈækʃən/','互动、交流；相互作用',
 '不是各做各的，而是你影响我、我也回应你。人之间有交谈互动，药物、物质或系统之间也能有相互作用。',
 'inter- 之间、相互与 action 行动、作用结合；现代也可对照 interact 与名词 -ion。action 较早接拉丁 agere 做、行动的词族。',
 [['inter- + action；与 interact 对应','彼此之间的行动、作用'],['英语 interaction','人际互动；事物之间的相互影响']],
 'interaction between A and B：A 与 B 的互动；interaction with users 与用户互动；social interaction 社交互动；the interaction of light and matter 光与物质的相互作用。',
 'encourage interaction；human interaction。','interaction 不一定是语言交谈。物质、设备之间的 interaction 只需有相互作用；communication 更常突出信息传递。',
 ('The class encourages interaction between students.','这门课鼓励学生之间互动。'),('The study examines the interaction of light and matter.','这项研究考察光与物质的相互作用。'),sources=['https://en.wiktionary.org/wiki/interaction#English'])
W('overcome','/ˌəʊvəˈkʌm/；美 /ˌoʊvərˈkʌm/','克服、战胜；使受不了、使被情绪压倒',
 '前面有道阻力，你跨过去继续走，是 overcome；反过来，情绪强得把你压住，be overcome 则说被压倒。',
 '承接古英语 ofercuman 越过、征服的复合动词，对应 over- 越过与 come 来、达到。现代 overcome—overcame—overcome，过去分词与原形相同。',
 [['古英语 ofer + cuman → ofercuman','越过、来到前面 → 胜过、征服'],['现代 overcome','克服；情绪等使人难以承受']],
 'overcome difficulties 克服困难；overcome a fear 克服恐惧；be overcome with emotion 情绪激动得难以自持；be overcome by smoke 被浓烟熏得受不了。',
 'overcome an obstacle；be overcome with joy。','She overcame her fear 是她克服恐惧；She was overcome with fear 是她被恐惧压倒。被动结构在这里直接改变谁压过谁。',
 ('She overcame her fear of speaking in public.','她克服了公开发言的恐惧。'),('He was overcome with emotion when he saw his family.','看到家人时，他激动得难以自持。'),sources=['https://en.wiktionary.org/wiki/overcome#English'])
W('overcame','英 /ˌəʊvəˈkeɪm/；美 /ˌoʊvərˈkeɪm/','克服了、战胜了；压倒了；overcome 的过去式',
 '那道困难当时挡在眼前，后来被跨过去了。overcame 用在讲述过去事件里，把克服这件事放到过去。',
 'overcome 的过去式，保留 come → came 这一词族的内部元音变化。过去分词回到 overcome，所以说 has overcome，不说 has overcame。',
 [['overcome；承接旧英语复合动词','越过、战胜；也可说情绪压倒'],['过去式 overcame；分词 overcome','过去事件用 came 型，完成结构用 come 型']],
 'overcame the problem 克服了问题；overcame resistance 战胜了阻力；emotion overcame someone 情绪压倒了某人。',
 'finally overcame the difficulty；overcame her doubts。','They overcame it 是一般过去时；They have overcome it 是现在完成时。不要只记克服两字，而漏掉完成结构中的分词形式。',
 ('The team overcame several technical problems.','团队克服了几项技术问题。'),('Relief overcame her when the missing files were found.','丢失的文件找到时，她一下被如释重负的情绪淹没了。'),sources=['https://en.wiktionary.org/wiki/overcame#English'])
W('odds','英 /ɒdz/；美 /ɑːdz/','可能性、胜算；不利条件；分歧〔at odds〕',
 '两边本来就不一定势均力敌，哪一边更可能成事，就有 odds 的胜算线。against the odds 是条件不看好，却还是做成了。',
 '接 odd 零散、不均等的旧名词化、复数用法，发展出差别、优势与机会等义。现代常以复数形式用于胜算、分歧等固定结构，不等于普通 odd numbers 的省略。',
 [['odd 的不均等、差别材料 → odds','差异、优势、不对等'],['现代 odds','胜算、可能性；不利形势；意见不合']],
 'the odds of success 成功的可能性；against all odds 克服重重不利；at odds with someone 与某人意见不合；What are the odds? 真有这么巧，或在问可能性。',
 'improve the odds；the odds are against us。','odds 常按复数搭配：The odds are ...。at odds with 表意见不合，作为固定表达记住；概率语境的具体数值表达另按文本口径理解。',
 ('They completed the project against all odds.','他们克服重重不利，完成了项目。'),('Her account was at odds with the other witnesses’ reports.','她的说法与其他目击者的陈述不一致。'),sources=['https://en.wiktionary.org/wiki/odds#English'])
W('stocks','英 /stɒks/；美 /stɑːks/','库存、储备；股票；旧式木枷；stock 的第三人称单数',
 '仓库里留着的一批批货是 stocks；公司资本分支里的 stocks 常说股票。旧木块词源也保留在另一支 stocks 木制刑具里。',
 'stock + -s。stock 接古英语 stocc 树干、木块、柱等，后有基础、储备、库存和资本等分支；股票、库存与旧木制刑具义须分别看上下文。',
 [['古英语 stocc → stock','树干、木块、基础；后来储备、资本'],['stock + -s → stocks','储备、股票；旧刑具；另为动词形式']],
 'food stocks 食品储备；stocks of medicine 药品库存；stocks and shares 股票；the stocks 旧式夹住脚等的木枷；The shop stocks ... 商店备有……。',
 'replenish stocks；stocks are running low。','stock 在 have it in stock 中通常不加 s，意为有货；stocks of fuel 在说燃料储备。The store stocks fuel 中 stocks 则是动词备货。',
 ('The hospital checked its stocks of essential supplies.','医院检查了基本用品的库存。'),('The museum displayed a set of old wooden stocks.','博物馆展出了一副旧式木枷。'),sources=['https://en.wiktionary.org/wiki/stocks#English'])
W('bonds','英 /bɒndz/；美 /bɑːndz/','联系、纽带；化学键；债券；束缚〔bond 复数〕',
 '把双方系在一起的东西可以是感情、原子间的连接，也可以是有约束力的债务凭据。bonds 在不同领域保留系住、连接这条线。',
 'bond + -s；bond 与 band、bind 的捆绑词族相连，也受北欧语相关形式影响。关系、化学连接和债券各自在历史中专门化，不是所有现代 bond 都是一条实物绳。',
 [['捆绑、带子词族 → bond','系住、约束的东西；联系、承诺'],['bond + -s → bonds','多种纽带；化学键、债券等']],
 'family bonds 家庭纽带；bonds of friendship 友谊纽带；chemical bonds 化学键；government bonds 政府债券。',
 'strengthen bonds；break chemical bonds。','stocks 常说公司所有权相关的股票，bonds 常说债务凭证。这里辨认词义；family bonds 则完全是人与人之间的关系。',
 ('Shared experiences strengthened the bonds between them.','共同经历加深了他们之间的联系。'),('The diagram shows the chemical bonds in the molecule.','示意图显示了分子中的化学键。'),sources=['https://en.wiktionary.org/wiki/bonds#English'])
W('encounter','英 /ɪnˈkaʊntə/；美 /ɪnˈkaʊntər/','遇到、遭遇；一次相遇、交锋',
 '沿路向前，某个人或问题出现在你面前，双方碰上了。encounter 常有实际遇上、面对的感觉，不保证事前约好。',
 '名词、动词经法语 encontre、encontrer 等相对、相遇材料，接晚期拉丁 incontra 在面前，含 in 与 contra 相对。对手迎面相遇的旧义后来放宽为偶遇、遭遇。',
 [['拉丁 incontra → 法语 encontre／encontrer','在面前、相对 → 相遇、交锋'],['英语 encounter','遇上人；面对问题；一次相遇']],
 'encounter a problem 遇到问题；encounter resistance 遭到阻力；a chance encounter 偶遇；an encounter with wildlife 与野生动物的一次相遇。',
 'a brief encounter；problems encountered during the work。','encounter 作动词直接接对象：encounter a problem；作名词则常用 an encounter with someone。它比 meet 更容易突出偶然碰上、实际面对。',
 ('We encountered several problems during the move.','搬迁时我们遇到了几个问题。'),('A chance encounter at the station led to a lasting friendship.','车站的一次偶遇促成了一段长久的友谊。'),sources=['https://www.etymonline.com/word/encounter','https://en.wiktionary.org/wiki/encounter#English'])
W('furnish','英 /ˈfɜːnɪʃ/；美 /ˈfɝːnɪʃ/','为……配家具、装备；提供、供给',
 '空房间里把桌椅床备齐，是 furnish；把别人办事需要的资料也备齐给他，仍然是提供所需的那条线。',
 '经法语 furniss- 等词干接 furnir、fornir 完成、装备、提供，较早接日耳曼促进、做成的材料。与 frame 的动词历史有同族联系，但不是现代从 frame 直接派生。',
 [['较早日耳曼做成、促进材料 → 法语 furnir／fornir','把事情做成；提供、装备'],['法语词干 → 英语 furnish','供给；后来常说给房间配家具']],
 'furnish a room 为房间配家具；furnish someone with information 向某人提供资料；furnish evidence 提供证据；furnish the house simply 简单布置房屋。',
 'furnish an office；furnish someone with the details。','furnish 不只接桌椅。furnish someone with details 里的 details 是提供的信息；谈房间时才通常是配备家具。',
 ('They furnished the flat with second-hand furniture.','他们给公寓配了二手家具。'),('The report furnishes evidence for the claim.','报告为这一说法提供了证据。'),sources=['https://www.etymonline.com/word/furnish','https://en.wiktionary.org/wiki/furnish#English'])
W('furniture','英 /ˈfɜːnɪtʃə/；美 /ˈfɝːnɪtʃər/','家具〔不可数统称〕',
 '桌子、椅子、床等东西放在一起，填充并服务一个生活、工作空间，就是 furniture。英语把它作为一类东西的统称。',
 '借法语 fourniture 供应、装备，接 fournir 提供、装备，与 furnish 同族。英语先有供应、装备等义，后来家具义突出；不能把现代拼写当作 furnish 任意改尾。',
 [['法语 fournir → fourniture','提供、装备 → 所供应、装备的东西'],['英语 furniture','供应、装备等旧义 → 桌椅床柜等家具统称']],
 'a piece of furniture 一件家具；some furniture 一些家具；office furniture 办公家具；wooden furniture 木制家具；move the furniture 搬动家具。',
 'buy furniture；furniture for the living room。','普通家具义不说 a furniture 或 three furnitures。要数件数，用 three pieces of furniture，或直接说 three chairs。',
 ('We need some furniture for the new office.','新办公室需要添些家具。'),('This chair is my favourite piece of furniture.','这把椅子是我最喜欢的一件家具。'),sources=['https://www.etymonline.com/word/furniture','https://en.wiktionary.org/wiki/furniture#English'])
W('furnished','英 /ˈfɜːnɪʃt/；美 /ˈfɝːnɪʃt/','配有家具的；提供了、装备了；furnish 的过去式、过去分词',
 '你走进屋时，基本家具已经在那里：a furnished flat。这里说的是租住空间具备什么，不自动说明每件小用品都齐全。',
 'furnish + -ed，/ʃ/ 后结尾读 /t/。分词形容词先可说装备、供给好的，后来在房屋语境常指配备家具。',
 [['furnish','提供、装备；给房间配家具'],['furnish + -ed → furnished','已供给；配有家具的']],
 'a furnished room 带家具的房间；fully furnished 家具配置齐全的；simply furnished 陈设简朴的；furnished with evidence 获提供证据的，较正式。',
 'a furnished apartment；comfortably furnished。','furnished 在房源介绍里说带家具，unfurnished 说不带或少带家具，具体包含哪些仍按描述。furnished 并不自动等于豪华。',
 ('They rented a small furnished flat near the station.','他们在车站附近租了一套小型带家具公寓。'),('The room was simply furnished with a bed and a desk.','房间陈设简单，只有一张床和一张桌子。'),sources=['https://www.etymonline.com/word/furnish','https://en.wiktionary.org/wiki/furnished#English'])
W('unfurnished','英 /ˌʌnˈfɜːnɪʃt/；美 /ˌʌnˈfɝːnɪʃt/','未配家具的；未装备的',
 '房间可以住，但床、桌椅等要自己安排。unfurnished 把 furnished 的带家具状态否定掉。',
 'un- 不、未 + furnished 配有家具的，furnished 来自 furnish + -ed。这里 un- 否定状态，不保证房子里完全没有任何固定设备。',
 [['furnish → furnished','配备 → 已配家具的'],['un- + furnished → unfurnished','未配家具、尚未装备的']],
 'an unfurnished flat 不带家具公寓；rent unfurnished 以不带家具方式出租、租住；an unfurnished room 未配家具的房间。',
 'an unfurnished apartment；leave the room unfurnished。','unfurnished 不同于 unoccupied 没人住。房子可暂时无人居住却仍带家具，也可不带家具而已经有人租用。',
 ('The flat was unfurnished, so we brought our own bed.','公寓不带家具，所以我们搬来了自己的床。'),('They decided to rent the house unfurnished.','他们决定租下那套不带家具的房子。'),sources=['https://en.wiktionary.org/wiki/unfurnished#English'])
W('furnishings','英 /ˈfɜːnɪʃɪŋz/；美 /ˈfɝːnɪʃɪŋz/','家具及室内陈设；装饰用品',
 '把空间布置成能住、好看的地方，不只要桌椅，也可能要窗帘、地毯、布艺。furnishings 看这些配置、陈设的整体。',
 'furnish + -ing 形成配备、陈设等名词，再以复数 furnishings 指相关物品。与 furniture 同族，但现代范围与语法习惯不完全相同。',
 [['furnish → furnishing','提供、布置 → 配备过程或陈设物'],['furnishing + -s → furnishings','用于室内布置的家具、陈设用品']],
 'home furnishings 家居陈设用品；soft furnishings 窗帘、靠垫等室内布艺；modern furnishings 现代陈设；simple furnishings 简单陈设。',
 'choose the furnishings；bedroom furnishings。','furniture 主要统称桌椅床柜等；furnishings 常范围更广，尤其 soft furnishings 包括窗帘、垫子等。furniture 普通义不可数，furnishings 常以复数出现。',
 ('The room has simple furnishings and plenty of light.','房间陈设简洁，采光充足。'),('She chose blue curtains to match the other soft furnishings.','她选了蓝窗帘来搭配其他室内布艺。'),sources=['https://en.wiktionary.org/wiki/furnishings#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_uy',ROOTS,WORDS)
 extend_lessons()
