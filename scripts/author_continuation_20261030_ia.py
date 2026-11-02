"""Layers, soil, a newsroom nickname, sake and ham versus Hamburg."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
L=[['lay 放置 + -er → 铺放者 layer','铺砖的人；产蛋的禽鸟等动作承担者'],['厚度、层次名词 layer','铺在表面的一层；具体早期词源还有其他解释'],['动词和数量组合','分层；园艺压条；单层、双层、多层']]
W('layer','英 /ˈleɪə/；美 /ˈleɪər/','层、层次；分层铺放；铺放者、产蛋禽鸟',
 '蛋糕一层奶油、一层海绵，衣服一件叠一件，是最直观的 layer；电脑图层和问题层次也借这个叠放感觉。',
 '做铺放动作的人可清楚分析 lay + -er；厚度层义常与放在表面的一层相连，但早期也有 lair 等相关形式或烹饪词影响的不同解释，不把一个故事说死。',L,
 'a layer of dust 一层灰，layers of clothing 多层衣物，an image layer 图层，a layer of meaning 一层意义，a good layer 产蛋好的禽鸟。',
 'a layer of；layers of clothing；an image layer；layer the ingredients。',
 'layer 是可分的一层、层次，level 更常说高度、等级。layer 里的 -er 也不保证永远是人；产蛋母鸡可叫 layer。',
 ('A thin layer of dust covered the shelf.','架子上盖着一层薄灰。'),('Each image layer can be edited separately.','每个图层都能单独编辑。'),('This breed of hen is a good layer.','这种母鸡很会产蛋。'),sources=['https://en.wiktionary.org/wiki/layer#English','https://www.etymonline.com/word/layer'])
W('layering','英 /ˈleɪərɪŋ/；美 /ˈleɪərɪŋ/','分层、叠加；多层穿搭；压条繁殖〔园艺〕',
 '日常是把几层叠起来；园艺却常是让仍连着母株的枝条先长根，再成为独立植株，不能当作已经剪下来的扦插。',
 'layer + -ing。名词可指分层过程、分层结构；园艺用法接 layer 压条的动词，并非先把植物叶子像衣服一样层层穿上。',L+[['layer + -ing → layering','叠加、层次安排；压条生根的园艺过程']],
 'layering clothes 多层穿搭，layering colours 叠加颜色，simple layering 普通压条，air layering 高空压条。',
 'layering clothes；layering colours；simple layering；air layering。',
 'layering 园艺义的要点是生根时仍与母株相连；cuttings 扦插通常先取下枝条等部分。不要照层叠字面混淆两种繁殖方式。',
 ('Layering clothes makes it easier to adjust to changing temperatures.','多层穿衣便于应对温度变化。'),('The guide compares layering with propagation from cuttings.','指南比较压条繁殖与扦插繁殖。'),sources=['https://en.wiktionary.org/wiki/layering#English','https://www.rhs.org.uk/propagation/layering'])
W('bricklayer','英 /ˈbrɪkleɪə/；美 /ˈbrɪkleɪər/','砌砖工、砖瓦匠',
 '把砖一块块摆到该放的位置，用来筑墙的人；layer 在这里是铺放者，而不是墙上的一层砖。',
 'brick 砖 + layer 铺放者；layer 这一人物义来自 lay + -er。中古英语已有相关组合。',L[:1]+[['brick + layer → bricklayer','铺砖、砌砖的人']],
 'a skilled bricklayer 熟练砌砖工，work as a bricklayer 当砌砖工，a bricklayer building a wall 正在砌墙的砖匠。',
 'a skilled bricklayer；work as a bricklayer；a bricklayer’s tools。',
 'bricklayer 是人，a layer of bricks 是一层砖；mason 范围可更广，包含石工、砌筑者等，不能只按中文瓦匠全混用。',
 ('The bricklayer checked the wall as each course was added.','每砌上一皮砖，砖匠都会检查墙体。'),('Her father worked as a bricklayer for many years.','她父亲当了很多年砌砖工。'))
W('bilayer','英 /ˈbaɪleɪə/；美 /ˈbaɪleɪər/','双层结构，尤指分子双层',
 '像两排相对的薄层贴在一起；bi- 直接告诉你有两层，具体每层由什么构成再看材料。',
 'bi- 两个 + layer 层。生物、材料语境常说分子级双层，不是两个铺砖工。',L[1:2]+[['bi- + layer → bilayer','由两层组成的结构']],
 'a lipid bilayer 脂质双层，a molecular bilayer 分子双层，a bilayer structure 双层结构。',
 'a lipid bilayer；a molecular bilayer；a bilayer structure。',
 'bilayer 是层数，不说明一定厚或薄到固定数值；bilingual 双语有相同数量前缀，但后半不是一回事。',
 ('The diagram shows a lipid bilayer surrounding the cell.','图中展示了包围细胞的脂质双层。'),('The model compares a monolayer with a bilayer.','模型比较了单层与双层结构。'))
W('monolayer','英 /ˈmɒnəʊleɪə/；美 /ˈmɑːnoʊleɪər/','单分子层、单细胞层等单层结构',
 '不是很多层叠起来，而是只排一层；在材料里可能一分子厚，在培养细胞语境里可能一细胞厚。',
 'mono- 单一 + layer 层。技术语境的一个单位由对象决定，不能一律翻成一种固定厚度。',L[1:2]+[['mono- + layer → monolayer','一个分子、细胞等厚度的单层结构']],
 'a molecular monolayer 单分子层，a cell monolayer 单层细胞，a monolayer film 单层薄膜。',
 'a molecular monolayer；a cell monolayer；a monolayer film。',
 'monolayer 不等于只有一颗分子：平面可有许多分子，厚度方向只有一层。mono- 也不说明平面面积大小。',
 ('The molecules formed a monolayer on the surface.','分子在表面形成了单分子层。'),('The photograph shows a monolayer of cells.','照片展示了一层细胞。'))
R('B3914','铺放者与一层厚度、层次的不同角色','LAYER：一层层叠，或把东西铺下去的角色','layer → layering；bricklayer 砌砖的人；mono-/bi-/multi-layer 看层数。',
 '铺放者是主动角色，铺成的一层是结果形状。园艺压条又有自己的传统用法，不能只套蛋糕叠层的图景。',
 'lay + -er → 铺放者；厚度义的早期来源有其他解释；layer + -ing；brick + layer；mono-/bi-/multi- + layer。',
 [['层次与分层动作','layer · layering'],['铺放角色','bricklayer'],['数量限定的层','monolayer · bilayer · multilayer']],
 'bricklayer 是人；monolayer 可有许多分子但只一层厚；layering 压条不等于剪下扦插；厚度义词源不强定唯一解释。',
 'The bricklayer built one layer at a time, while the diagram showed a molecular bilayer.\n\n砖匠一层层砌筑，旁边图中展示的则是分子双层。','layer layering bricklayer monolayer bilayer multilayer')
O=[['法语 soyl 等与英语旧泥土形式汇合','地面、土壤的名词 soil'],['法语、旧英语弄脏词的相关路线','弄脏、玷污的动词 soil；不能只作现代名词临时转动词']]
W('soil','/sɔɪl/','土壤、土地；国土；弄脏、玷污',
 '花盆里支撑植物生长的是土壤；衣服被弄脏可以说 soiled。概念相近，历史却不是简单先有现代土壤名词再造一切动词。',
 '土壤名词涉及法语 soyl 地面及旧英语泥土词的汇合，远接拉丁 solium/solum 等交错背景。弄脏动词也有法语、旧英语相应路线，不能只凭现代同拼写抹去差别。',O,
 'fertile soil 肥沃土壤，soil quality 土壤质量，on foreign soil 在外国土地上，soiled clothes 脏衣物，soil someone’s reputation 玷污名声。',
 'fertile soil；soil quality；on foreign soil；soiled clothes。',
 'soil 作为土壤并不是需要丢掉的脏东西，dirt 的脏物义更偏相对环境的不洁；土壤含矿物、有机物及生物等，不只一种泥。',
 ('The plants grow well in this soil.','这些植物在这种土壤里长得很好。'),('His shoes soiled the clean floor.','他的鞋把干净地板弄脏了。'))
R('B2734','支撑植物的土壤、土地，以及弄脏动词','SOIL：在花盆里是生长介质，在衣服上可能成污迹','soil → topsoil 表土、subsoil 底土；soil 动词则是弄脏、玷污。',
 '同样的物质在不同位置有不同评价：花盆需要土，干净衬衫不需要。这个画面有助记忆，历史上仍保留多路汇合。',
 '法语与旧英语相关形式 → soil；top/sub- + soil；soil → soiled/soiling。',
 [['土壤及层位','soil · topsoil · subsoil']],
 'soil 不只脏物；on foreign soil 可说在国外；soiled clothes 不必真沾了园土；名词动词历史多路。',
 'The report compares the topsoil with the subsoil beneath it.\n\n报告比较表土与其下的底土。','soil topsoil subsoil')
W('journo','英 /ˈdʒɜːnəʊ/；美 /ˈdʒɜːrnoʊ/','记者〔非正式、略带熟人语气〕',
 '把长职业名 journalist 缩短、再接一个口语尾巴，像聊天时随口叫记者，不是另一种资格证。',
 'journalist 的截短词干 journ- + -o，-o 常见于非正式昵称、人物词。不是 journal 完整名词后直接加一个表示工作的 o。',
 [['journalist → journ-','把职业长词缩短'],['journ- + -o → journo','非正式记者称呼']],
 'a local journo 当地记者，a sports journo 体育记者，a veteran journo 资深记者；在英式、澳大利亚等口语中容易遇见。',
 'a local journo；a sports journo；a veteran journo。',
 'journo 比 journalist 随意，可亲近也可轻蔑，取决于语气；不说明人一定不专业。正式署名通常用 journalist、reporter 等。',
 ('A local journo asked us about the new library.','一位当地记者问我们新图书馆的事。'),('She began as a sports journo before moving into radio.','她先做体育记者，后来转入广播。'))
R('B4337','记者及其学术式派生、口语缩称','JOURNALIST：职业名可长可短，语气不同','journalist → journalistic；journo 是口语缩称；photojournalist 用摄影报道。',
 '缩短名称改变正式程度，不自动改变职责。journalistic 说新闻写作性质，photo- 则指定摄影的表达方式。',
 'journal + -ist → journalist；journalist 与 -ic → journalistic；journ- + -o → journo；photo- + journalist。',
 [['记者、相关性质与口语称呼','journalist · journalistic · journo'],['摄影报道','photojournalist']],
 'journo 不等于不专业；journalistic 是性质，journalist 是人；photojournalist 的工作不只随便拍照。',
 'The local journo interviewed a photojournalist about journalistic standards.\n\n当地记者采访了一位摄影记者，谈新闻专业标准。','journalist journalistic journo photojournalist')
K=[['古英语 sacu → sake','案件、争端、事情 → 原因、目的、利益'],['另源日语 sake → 英语 sake','酒，英语通常指日本米酿酒']]
W('sake','缘故、利益义 /seɪk/；日本清酒义常 /ˈsɑːki/','缘故、目的、利益〔固定搭配〕；日本清酒〔另源〕',
 'for your sake 是为了你好；菜单里的 sake 则是一种日本米酿酒，连读音也不必一样。',
 '缘故义接古英语 sacu 案件、争端、事情，今天主要活在 for ... sake 中。酒名借日语酒的名称，不是目的这个抽象名词变成饮品。',K,
 'for the sake of clarity 为讲清楚，for your sake 为你好，for its own sake 为事情本身，for goodness’ sake 天哪、拜托〔感叹〕；sake 在酒单上另读。',
 'for the sake of；for your sake；for its own sake；for goodness’ sake。',
 'for the sake of 后接名词等；不要把 sake 当 reason 在任何句式里直接替换。酒名的英语读音有变体，通常两音节，与 /seɪk/ 分开。',
 ('For the sake of clarity, I will give one example.','为讲清楚，我举一个例子。'),('She did it for her family’s sake.','她是为了家人才这样做的。'),('The menu lists several kinds of Japanese sake.','菜单列出几种日本清酒。'),sources=['https://en.wiktionary.org/wiki/sake#English','https://www.merriam-webster.com/dictionary/sake'])
R('B3171','缘故、目的和利益；与日本酒名分源','SAKE：for ... sake 看为了什么，酒单另看','sake → namesake 因其得名的同名者，keepsake 留作念想的物品；清酒 sake 则另源。',
 '先按读音和场景分酒名，再看缘故、记念相关组合；不能把所有同形词都往喝酒上拉。',
 'sacu → sake /seɪk/；name/keep + sake；另线日语酒名 → sake 两音节。',
 [['缘故、同名和留念','sake · namesake · keepsake']],
 'sake 常依赖固定介词结构；酒名另源、读音不同；keepsake 不是为保存所有东西而造的任意说法。',
 'She kept a photograph of her namesake as a keepsake.\n\n她留着那位与她同名者的照片作纪念。','sake namesake keepsake')
M=[['古英语 hamm → ham','膝后、后腿部位 → 猪后腿肉、火腿'],['表演俚语 ham → hammy','表演浮夸者；来源有多种解释，不固定为火腿故事'],['另一名称路线 Hamburg → hamburger → burger','地名相关食物名称 → 重新切分出的 burger']]
W('ham','/hæm/','火腿；膝后、后腿〔旧部位义〕；表演浮夸者；业余无线电爱好者',
 '三明治里的 ham 是火腿；He’s a ham 可说他爱夸张表演；ham radio 又是业余无线电。别把所有意思都说成会演戏的火腿。',
 '肉名接古英语 hamm 膝后等部位，后来具体到猪后腿食物。表演俚语常联系 hamfatter 等旧称但细节有争议，业余无线电称呼又与业余者用法有关。',M[:2],
 'a ham sandwich 火腿三明治，sliced ham 火腿片，ham it up 夸张表演，a ham actor 浮夸演员，ham radio 业余无线电。',
 'a ham sandwich；sliced ham；ham it up；ham radio。',
 'hamstring 的 ham 保留膝后旧义；hamburger 前面虽像 ham，食物名却来自 Hamburg，不要求夹火腿。ham it up 可能是故意搞笑。',
 ('She put a slice of ham in the sandwich.','她在三明治里放了一片火腿。'),('He hammed it up for the children.','他故意夸张表演，逗孩子们开心。'),sources=['https://en.wiktionary.org/wiki/ham#English','https://www.etymonline.com/word/ham'])
W('hammy','/ˈhæmi/','表演浮夸、做作的；像火腿的〔另一义〕',
 '感情本来只需一点，演员却把手势、声音和表情全开到最大；看起来过火，就可 hammy。',
 'ham + -y，双写 m；表演义从浮夸演员 ham 派生，不是食品太咸比喻演技。食物相关语境则可按像火腿理解。',M[:2]+[['ham + -y → hammy','浮夸演员般的；另一支具有火腿性质的']],
 'a hammy performance 浮夸表演，hammy acting 做作演技，a hammy villain 演得浮夸的反派。',
 'a hammy performance；hammy acting；a hammy villain。',
 'hammy 不等于 funny 好笑：过火可以产生喜剧效果，也可能让人出戏。serious 表演同样可能 hammy。',
 ('The actor gave a deliberately hammy performance.','那位演员故意演得很夸张。'),('The review praised the scenery but criticized the hammy acting.','评论称赞布景，却批评演技浮夸。'))
W('hamburger','英 /ˈhæmbɜːɡə/；美 /ˈhæmbɜːrɡər/','汉堡包；汉堡肉饼、碎牛肉〔依语境〕',
 '名字记录 Hamburg 汉堡这个地名背景，不是在给 ham 火腿加一个表示包的尾巴；传统肉饼常是牛肉。',
 'German Hamburger 是与 Hamburg 有关的人、物这一形式；英语 Hamburger steak、hamburger sandwich 等后来缩成 hamburger。食物传播细节不能只凭地名认定唯一发明者。',M[2:]+[['Hamburger steak/sandwich → hamburger','地名相关食物称呼缩短 → 肉饼、夹肉饼的面包']],
 'a hamburger 汉堡包，hamburger meat 做肉饼的碎肉，a hamburger bun 汉堡面包。美式不可数 hamburger 还可直接说碎牛肉。',
 'a hamburger；hamburger meat；a hamburger bun。',
 'hamburger 不是 ham + burger 的原始结构，不要求含火腿。cheeseburger 等出现以后，burger 才成为可独立使用、继续组合的部分。',
 ('He ordered a hamburger and a salad.','他点了一个汉堡包和一份沙拉。'),('The recipe calls for a pound of hamburger.','这个食谱需要一磅碎牛肉。'),sources=['https://en.wiktionary.org/wiki/hamburger#English','https://www.etymonline.com/word/burger'])
W('burger','英 /ˈbɜːɡə/；美 /ˈbɜːrɡər/','汉堡包；汉堡肉饼或类似夹饼食品',
 '长词 hamburger 被人重新听成前面是配料、后面是食物类型，burger 于是独立出来；换成鸡肉、豆类也能再组合。',
 'hamburger 的截短，涉及重新切分：原来的 Hamburg + -er 被再分析出 burger。现代 chicken burger、veggie burger 等因此成立，不等于历史真有 ham 火腿作为前缀。',M[2:]+[['hamburger → burger','重新切分并截短，形成独立食物名'],['新配料 + burger','chicken/veggie/cheese 等的新组合']],
 'a beef burger 牛肉汉堡，a veggie burger 素汉堡或素肉饼，a chicken burger 鸡肉汉堡，burger patties 汉堡肉饼。',
 'a beef burger；a veggie burger；a chicken burger；burger patties。',
 'burger 可以是面包夹饼，也可按语境说其中的饼；不是所有 sandwich 都自然叫 burger，具体命名也有地区习惯。',
 ('She chose a veggie burger instead of a beef burger.','她选了素汉堡，没有选牛肉汉堡。'),('The burgers are served in toasted buns.','这些汉堡夹在烤过的面包里上桌。'),sources=['https://en.wiktionary.org/wiki/burger#English','https://www.etymonline.com/word/burger'])
R('B3222','火腿、膝后与表演俚语；把汉堡名称另分','HAM：火腿不是 hamburger 的原始前半','ham → hammy；hamstring 留旧部位义；Hamburg → hamburger → burger 是另一名称和重新切分路线。',
 '同一页放在一起，正好练习识破拼写诱惑。演员俚语保留不确定来源，汉堡名称不靠火腿解释。',
 'hamm → ham；ham + -y/string。另线 Hamburg + -er → 食物称呼 hamburger → burger。',
 [['部位、肉食及表演性质','ham · hamstring · hammy'],['形似却另有来路的食物名','hamburger · burger']],
 'hamstring 不是火腿绑绳；hammy 不一定好笑；hamburger 不要求火腿；burger 是后来重新切出的独立部分。',
 'The hammy actor ordered a hamburger, not a ham sandwich.\n\n那位表演浮夸的演员点了汉堡包，没有点火腿三明治。','ham hamstring hammy hamburger burger')
if __name__=='__main__':save('continuation_20261030_ia',ROOTS,WORDS)
