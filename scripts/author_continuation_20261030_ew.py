"""Escape, identity, cheese and mere: vivid origins and different homograph paths."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
E=[['拉丁 ex- + cappa → 俗拉丁 *excappāre → 法语 escaper、eschaper → escape','从披风里脱出 → 脱身、逃出'],['现代实际与抽象脱离','逃离拘束；避开后果；注意不到；暂时离开现实压力'],['人物、倾向和器件','escapee 逃脱者；escapism/escapist；escapement 每次放过一点的装置']]
W('escape','/ɪˈskeɪp/','逃脱、逃离；避开；被忽略；逃脱机会、解脱',
 '像别人抓住披风，你从衣物里抽身，留下衣物自己走脱；现代也可说逃过处罚、漏过注意，或从忙碌现实里暂时松口气。',
 '经法语 escaper、eschaper 接俗拉丁重建词 *excappāre，ex- 出 + cappa 披风。脱披风是词源画面，不必编成一次有姓名日期的真实追捕事件。',E,
 'escape from prison 越狱，escape punishment 逃过处罚，escape notice 没被注意，a narrow escape 险些出事后逃过一劫。',
 'escape from；escape punishment；escape notice；a narrow escape。',
 'escape from 常接逃离的地方，escape punishment 直接接避开的后果；不把所有场景都塞进 from。',
 ('The bird escaped through an open window.','鸟从一扇开着的窗户逃走了。'),('The spelling error escaped my notice.','那个拼写错误没被我注意到。'),
 sources=['https://en.wiktionary.org/wiki/escape#English','https://www.etymonline.com/word/escape'])
W('escapee','英 /ɪˌskeɪˈpiː/；美 /ˌeskeɪˈpiː/，也有其他重音变体','逃脱者、逃犯；逸出栽培环境的植物〔专门语境〕',
 '成功从拘束里逃出来的人；动物园、监禁等场景靠上下文判断，不能见 -ee 就断定是别人把他逃了。',
 'escape 去 e + -ee，构成人物名；-ee 虽常表示接受方，本词是做出逃脱的人，并不是绝对的被动规则。',E[:1]+[['escape + -ee → escapee','逃出来的人；专门场景也用于逸生植物']],
 'an escaped prisoner and an escapee 逃脱囚犯的两种表达，search for an escapee 搜寻逃脱者，an escapee from captivity 从圈禁中逃出的个体。',
 'search for an escapee；an escapee from captivity；a prison escapee。',
 'escapee 已逃脱的人，escapist 常是想借幻想离开现实的人或作品性质；不等于都在实际越狱。',
 ('The guards searched for the escapee.','看守搜寻逃脱者。'),('The story follows an escapee trying to reach home.','故事跟随一名试图回家的逃脱者。'))
W('escapism','/ɪˈskeɪpɪzəm/','逃避现实；暂离日常压力的娱乐、幻想',
 '人还坐在这里，注意力却借小说、电影去了另一个世界；可只是休息，也可被批评只顾逃开现实，语气看场景。',
 'escape 去 e + -ism，形成倾向、活动名词。精神上逃离的比喻不要求真的离开房间。',E[:2]+[['escape + -ism → escapism','借幻想、娱乐等暂离现实的倾向、活动']],
 'pure escapism 纯粹解压娱乐，a form of escapism 一种逃离日常的方式，escapism through fiction 借小说暂离现实。',
 'pure escapism；a form of escapism；escapism through fiction。',
 'escapism 可中性娱乐或负面逃避，不能看到 -ism 就判成政治主义；escape 实际脱身范围更广。',
 ('For her, adventure novels are a form of escapism.','对她来说，冒险小说是一种暂离日常的方式。'),('The film offers two hours of pure escapism.','电影提供了两小时纯粹的解压娱乐。'))
W('escapist','/ɪˈskeɪpɪst/','逃避现实的人；让人暂离现实的、幻想娱乐性的',
 '人物名词说倾向借幻想躲开现实的人；形容词说作品提供这种暂离日常的体验，不是作品能打开监狱大门。',
 'escape 去 e + -ist，人物、性质用法并存；与 escapism 同基，不必把现代 -ist 每次只解释成职业者。',E[:2]+[['escape + -ist → escapist','逃避现实者；具有暂离现实性质的']],
 'escapist fiction 幻想解压小说，escapist entertainment 让人暂离现实的娱乐，an escapist attitude 逃避现实的态度。',
 'escapist fiction；escapist entertainment；an escapist attitude。',
 'escapist 作品性质或人物，escapee 逃脱者；喜欢幻想小说不自动等于不能面对所有现实问题。',
 ('She enjoys escapist fiction on long journeys.','长途旅行中，她喜欢读让人暂离现实的小说。'),('The critic dismissed the story as escapist entertainment.','评论者把故事贬为逃避现实的娱乐。'))
W('escapement','/ɪˈskeɪpmənt/','擒纵机构〔钟表等〕；控制逐步释放的装置',
 '齿轮本来会往前转，装置每次只放过一点点，再拦住、再释放，使走时按节奏进行；escape 是齿轮一步步获放行的画面。',
 'escape + -ment，装置名义与齿、部件每次从卡住处释放有关。不是一个想逃走的钟，也不只是抽象逃跑行为。',E[:1]+[['escape + -ment → escapement','释放、脱开一点的动作用于机构名'],['钟表常用义','控制轮系逐步前进，并与计时振动部分相互作用']],
 'a watch escapement 手表擒纵机构，an escapement mechanism 擒纵机构，the clock’s escapement 钟的擒纵装置。',
 'a watch escapement；an escapement mechanism；the clock’s escapement。',
 'escapement 装置名，escapism 心理娱乐倾向；同个 escape 词基走不同具体用途，不靠结尾长度猜意思。',
 ('The watchmaker examined the escapement.','钟表师检查了擒纵机构。'),('The model showed how the escapement releases the wheel step by step.','模型展示了擒纵机构如何让轮子逐步放行。'))
R('B3577','从衣物中抽身到实际、精神上的脱离','ESCAPE：从原来的束缚里脱出来','escape → escapee；escapism → escapist 是现实压力分支；escapement 是机械逐步放行分支。',
 '同一个脱身画面可以进监禁、注意力、娱乐、机械场景；escapee 与 escapist 别混人物角色。',
 'ex- + cappa → *excappāre，经法语 → escape；escape + -ee/-ism/-ist/-ment。',
 [['脱身动作与逃脱者','escape · escapee'],['现实、幻想和娱乐','escapism · escapist'],['机械控制释放','escapement']],
 'escape from 与 escape punishment 句型；escapee/escapist 实际逃脱者与精神娱乐；escapement 装置非逃避主义。',
 'The escapist novel offered an escape from the routine.\n\n这本幻想小说让人暂时离开日常的单调。','escape escapee escapism escapist escapement')
W('identity','/aɪˈdentəti/，也有 /aɪˈdentɪti/','身份、认同；同一性；确定某物是什么的特征',
 '怎么确定这个人就是那个人、这个东西还是同一个东西？这是同一性的底子。转到生活，就是“我是谁、我属于哪里、什么特征让我成为我”。',
 '经法语 identité 接拉丁 identitās 等，源自 idem 同一个与抽象名词词尾；不是 identify 简单截尾，也不是 ID 缩写先长出完整单词。',
 [['拉丁 idem〔同一个〕→ identitās 等 → 法语 identité → identity','同一性、是同一个'],['现代个人、群体与识别场景','身份；文化认同；对象的独特特征']],
 'confirm someone’s identity 确认身份，a sense of identity 身份认同感，cultural identity 文化认同，an identity card 身份证件。',
 'confirm someone’s identity；a sense of identity；cultural identity；an identity card。',
 'identity 身份与认同不只姓名、证件号；personality 人格性格是另一侧面，ID 可以是 identity 或 identification 的简称依场景。',
 ('The officer asked her to confirm her identity.','工作人员请她确认身份。'),('Language plays a part in cultural identity.','语言在文化认同中发挥作用。'),
 sources=['https://en.wiktionary.org/wiki/identity#English','https://www.etymonline.com/word/identity'])
R('B3659','是同一个，到我是谁的身份认同','IDENTITY：同一性和独特身份，其实都在问怎么认出这个对象','从 idem 同一个到身份识别、文化认同；本页把基础词几个核心场景讲清。',
 '身份不只证件号码，也包括自我、群体认同；数学等领域的同一性、恒等关系有更专门用法。',
 'idem + 抽象词尾 → identitās 等，经法语 identité → identity。',
 [['同一性、身份与认同','identity']],
 'identity/personality 身份认同与性格；ID 缩写需场景；姓名只是身份信息的一部分。',
 'The book explores the link between language and identity.\n\n这本书探讨语言与身份认同之间的联系。','identity')
C=[['拉丁 cāseus 早期借入日耳曼语 → 古英语 ċēse → cheese','奶酪'],['现代性质与组合','cheesy 含奶酪、俗套煽情；cheesecake、cheeseburger、cheesesteak'],['同形口语需另看','say cheese 拍照口令；big cheese 重要人物的来源不直接从奶酪硬推']]
W('cheese','/tʃiːz/','奶酪、干酪；拍照时说的“茄子”一类口令',
 '食品是由乳凝成、加工的一类奶酪；拍照说 cheese 常是借读这个音让表情像微笑，不是让大家去拿吃的。',
 '奶酪名接古英语 ċēse，更早为拉丁 cāseus 早期借词。拍照口令、the big cheese 重要人物等另有口语历史，不能全画成奶酪越大职位越高。',C,
 'a piece of cheese 一块奶酪，grated cheese 奶酪碎，say cheese 拍照时说笑脸口令，the big cheese 大人物〔口语〕。',
 'a piece of cheese；grated cheese；say cheese；the big cheese。',
 'cheese 食品常不可数，different cheeses 指不同品种可数；cheese 和 butter 奶酪黄油是不同制品。',
 ('She grated cheese over the pasta.','她在意面上撒了奶酪碎。'),('Everyone said cheese for the photo.','拍照时，大家一起喊了 cheese。'))
W('cheesy','/ˈtʃiːzi/','有奶酪的、奶酪味的；俗套煽情的、土气做作的',
 '酱汁浓浓奶酪味是字面；台词甜得过分、剧情套路得让人尴尬，也常被嫌 cheesy。',
 'cheese + -y，末尾 e 去掉接 y，中古英语已有 chesy。负面俗套、廉价感等口语义有自己的发展，不必给它编一个确定的变质奶酪故事。',C[:1]+[['cheese + -y → cheesy','含奶酪、像奶酪'],['口语评价扩展','俗套、过度煽情、做作']],
 'a cheesy sauce 奶酪酱，a cheesy joke 老套笑话，cheesy dialogue 俗套对白，a cheesy grin 夸张做作的咧嘴笑。',
 'a cheesy sauce；a cheesy joke；cheesy dialogue；a cheesy grin。',
 'cheesy 评价作品多偏负面，sweet 可正面甜美；菜品 cheesy 不自动是差评，场景控制语气。',
 ('The sauce was rich and cheesy.','酱汁浓郁，奶酪味十足。'),('The film had some cheesy dialogue.','电影里有些俗套煽情的对白。'))
W('cheesecake','/ˈtʃiːzkeɪk/','芝士蛋糕、奶酪蛋糕',
 '用奶酪等做出浓滑馅层的甜点，具体做法有烘烤和免烤等类型；不要求都是普通海绵蛋糕上撒一层奶酪。',
 'cheese 奶酪 + cake 蛋糕，中古英语已有 chesekake 等相应组合；字面食物名是常用核心。',C[:1]+[['cheese + cake → cheesecake','以奶酪为重要原料的蛋糕甜点']],
 'a slice of cheesecake 一片芝士蛋糕，baked cheesecake 烤芝士蛋糕，lemon cheesecake 柠檬芝士蛋糕。',
 'a slice of cheesecake；baked cheesecake；lemon cheesecake。',
 'cheesecake 蛋糕，cheesesteak 夹肉、奶酪的三明治；cake 与 steak 形近读音不同，点餐别只扫开头 cheese。',
 ('We shared a slice of lemon cheesecake.','我们分着吃了一片柠檬芝士蛋糕。'),('The café makes its own cheesecake.','咖啡馆自己做芝士蛋糕。'))
W('cheeseburger','英 /ˈtʃiːzbɜːɡə/；美 /ˈtʃiːzbɜːrɡər/','芝士汉堡、加奶酪的汉堡',
 '汉堡里加奶酪；不是把 meat 去掉、只剩一块奶酪就必然叫这个词，肉饼种类看具体菜单。',
 'cheese 与 hamburger 的部分合成，也可现代分析 cheese + burger。burger 由 hamburger 重新分析为可独立使用的词基，非汉堡本来等于 ham 火腿。',C[:1]+[['cheese + hamburger 的词形材料 → cheeseburger','加奶酪的汉堡；现代可拆 cheese + burger']],
 'order a cheeseburger 点芝士汉堡，a double cheeseburger 双层芝士汉堡，a cheeseburger meal 芝士汉堡套餐。',
 'a double cheeseburger；order a cheeseburger；a cheeseburger meal。',
 'cheeseburger 加奶酪，hamburger 基础汉堡；汉堡名称的 ham 不是要求都含火腿，burger 也已能接不同食材名。',
 ('He ordered a cheeseburger and a drink.','他点了一个芝士汉堡和一杯饮料。'),('The menu included a vegetarian cheeseburger.','菜单上有一款素食芝士汉堡。'))
W('cheesesteak','/ˈtʃiːzsteɪk/','奶酪牛肉三明治〔费城风格常见〕',
 '面包里夹切碎、薄切的牛肉和融化奶酪的三明治；不是一块芝士蛋糕，也不是所有撒奶酪的牛排都这样叫。',
 'cheese 奶酪 + steak 牛肉片、牛排，组合后成为有具体做法、地区背景的三明治名称。',C[:1]+[['cheese + steak → cheesesteak','肉与奶酪组合 → 特定夹馅三明治名称']],
 'a Philly cheesesteak 费城奶酪牛肉三明治，a cheesesteak sandwich 奶酪牛肉三明治，order a cheesesteak 点一份。',
 'a Philly cheesesteak；a cheesesteak sandwich；order a cheesesteak。',
 'cheesesteak 的 steak /steɪk/，cheesecake 的 cake /keɪk/；食物类型不同，同一个 cheese 前半不能代替整词。',
 ('She bought a cheesesteak from the sandwich shop.','她在三明治店买了一个奶酪牛肉三明治。'),('The cheesesteak came with onions and melted cheese.','奶酪牛肉三明治里配了洋葱和融化奶酪。'))
R('B2928','奶酪食品与质感、口语评价和组合','CHEESE：看是食物原料，还是口语里的另一用法','cheese → cheesy；cheesecake、cheeseburger、cheesesteak 按食物类型分；cheesecloth 是过滤用途的布名。',
 'cheesy sauce 常中性口味，cheesy dialogue 常负面俗套；say cheese 是口令，big cheese 人物不能只靠食品硬解释。',
 'cāseus 早期借入 → ċēse → cheese；cheese + -y/cake；cheese + hamburger 片段；cheese + steak/cloth。',
 [['食品与性质、语气','cheese · cheesy'],['三种常见食品','cheesecake · cheeseburger · cheesesteak'],['制作过滤用品','cheesecloth']],
 'cheese/butter 奶酪黄油；cheesecake/cheesesteak 蛋糕三明治；cheesy 口味与俗套评价；big cheese 不当食品大小故事。',
 'They ordered cheeseburgers and shared a cheesecake.\n\n他们点了芝士汉堡，又分着吃了一个芝士蛋糕。','cheese cheesy cheesecake cheeseburger cheesesteak cheesecloth')
M=[['拉丁 merus → 法语 mier、meer → mere〔形容词〕','纯、不掺杂 → 仅仅、不外乎；旧纯粹强调义也有保留'],['古英语 mere → mere〔湖水名词〕','海、湖、水体；与形容词分源'],['古英语 merisc、mersc → marsh','沿水体词族的湿地名称；不是 mere 仅仅加后缀']]
W('mere','英 /mɪə/；美 /mɪr/','仅仅的、不过是的；纯粹的；湖、池〔另名词来源，较多见地名〕',
 'a mere ten minutes 是仅仅十分钟，the mere thought 是光想到这一点；湖名中的 mere 却沿水体旧词，和“仅仅”没有直接意思关系。',
 '形容词经法语接拉丁 merus 纯的，后来有不外乎、只有等义；湖水名词继承古英语 mere。另有边界等更旧同形词，本页常用义先分两路。',M,
 'a mere child 不过是个孩子，a mere ten minutes 仅十分钟，the mere thought 光是这个想法，a shallow mere 浅湖〔地理描写〕。',
 'a mere child；a mere ten minutes；the mere thought；a shallow mere。',
 'mere 常放名词前，merely 副词；mere 湖名与形容词不同源，不能把 Windermere 一类地名按仅仅解释。',
 ('The repair took a mere ten minutes.','修理只花了十分钟。'),('The mere thought of the journey excited her.','光想到这趟旅程就让她兴奋。'),
 sources=['https://en.wiktionary.org/wiki/mere#English','https://www.etymonline.com/word/mere'])
W('merely','英 /ˈmɪəli/；美 /ˈmɪrli/','仅仅、只是、不过',
 '把额外的解释拿掉：我只是问问，并没有暗示别的；也可强调某事没达到你期待的更高程度。',
 'mere 仅仅的 + -ly，中古英语已有 mereli 等形式；接形容词的纯粹、仅仅分支，不接湖名词。',M[:1]+[['mere + -ly → merely','仅仅地、不外乎']],
 'merely a suggestion 只是个建议，not merely 不仅仅，merely because 仅因为，merely asking 只是问问。',
 'merely a suggestion；not merely；merely because；merely asking。',
 'merely 较书面对应 only、just 的某些用法；mere 修饰名词，merely 可修饰更宽的表达，不是把 merely 当动词使用。',
 ('I was merely asking a question.','我只是问个问题。'),('The change is not merely cosmetic.','变化不只是表面修饰。'))
W('marsh','英 /mɑːʃ/；美 /mɑːrʃ/','沼泽、草本湿地',
 '地势低湿、经常积水，长着草本湿地植物的一片地；不是任何有点泥的路面都叫 marsh。',
 '继承古英语 mersc、merisc，经中古英语 mersch 等到 marsh；更早在水体 mere 同族词基上构成湿地名称，不是现代 mere 仅仅变了几字母。',M[1:2]+[['水体词族 → 古英语 merisc、mersc → mersch → marsh','水边、湿地性质 → 沼泽名称']],
 'a salt marsh 盐沼，marsh grass 沼泽草，birds in the marsh 沼泽中的鸟，marsh habitat 湿地生境。',
 'a salt marsh；marsh grass；marsh habitat。',
 'marsh 湿地类型，mere 水体名常湖池；swamp、bog 也可湿地，但生态分类、地区习惯不同，不能永远随意互换。',
 ('Birds nested in the marsh.','鸟在沼泽里筑巢。'),('A path crossed the salt marsh.','一条小路穿过盐沼。'))
R('B3998','仅仅、纯粹与另一条水体词源','MERE：常用形容词从纯粹来，湖和沼泽另走水体路','mere → merely 是仅仅分支；marsh 经早期水体同族构词而来。',
 '同形词要按来源分：merely asking 只是问，a mere 湖、marsh 湿地不能靠只有这个意思硬解释。',
 'merus 经法语 → mere 形容词 → merely；古英语 mere 水体；水体词族 merisc、mersc → marsh。',
 [['仅仅与副词','mere · merely'],['水体词族的湿地名称','marsh']],
 'mere/merely 形容副词；mere 两条来源；marsh/mere 湿地与水体；swamp/bog/marsh 不能无差别套用。',
 'The crossing took a mere hour, but the marsh was not merely empty land.\n\n穿越只花一小时，不过沼泽并不只是一片空地。','mere merely marsh')
if __name__=='__main__':save('continuation_20261030_ew',ROOTS,WORDS)
