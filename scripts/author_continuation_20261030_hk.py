"""Mum, steal and romantic: homographs, unobtrusive action and story-shaped ideals."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
M=[['亲昵称呼 mummy 等 → mum','妈妈，幼儿、家庭叫法系列'],['另一路中古英语 mum/mom','闭嘴发出的含混声 → 沉默、保密'],['chrysanthemum → mum','菊花名的截短，园艺语境常见']]
W('mum','/mʌm/','妈妈〔英式常见〕；沉默、保密；菊花〔简称〕',
 '叫 Mum 是叫妈妈；keep mum 是嘴闭上、不声张；花店说 mums 却可能是一盆盆菊花。三个场景分开，就不会硬串成一个故事。',
 '妈妈义属 mummy、mam 等亲属昵称系列，mum 常被解释为 mummy 短称。沉默义来自旧的含混闭口声；花名截短自 chrysanthemum，分别有来路。',M,
 'my mum 我妈妈，keep mum 保持沉默，Mum’s the word! 保密！a pot of mums 一盆菊花。称呼妈妈时可按名字大写。',
 'my mum；keep mum；Mum’s the word!；a pot of mums。',
 'mum 英式、mom 美式是常见妈妈叫法；Mum’s the word 是保密的固定话，不是认真声明妈妈是一个词。',
 ('Mum, have you seen my jacket?','妈妈，你看到我的外套了吗？'),('They kept mum about the surprise party.','他们对惊喜聚会的事守口如瓶。'),sources=['https://www.etymonline.com/word/mum'])
W('mummy','/ˈmʌmi/','妈妈〔幼儿、亲昵称呼〕；木乃伊〔另源〕',
 '孩子叫 Mummy 是找妈妈；博物馆的 a mummy 是保存下来的遗体。读音一样，来源却相距很远。',
 '妈妈义属 mam/mammy、mum 等幼儿昵称系列，现代可对照 mum + -y。木乃伊义经法语、拉丁及阿拉伯语等传入，远接波斯语蜡、沥青相关词；旧时物质名后来固定用于保存的遗体。',
 [['mam/mammy 等亲属昵称 → mummy','妈妈、亲昵称呼'],['波斯语 mūm 等 → 阿拉伯语 mūmiyāʔ → 西欧借词','蜡、沥青及遗体相关材料名'],['英语 mummy 的遗体义','经过保存处理的遗体，尤古埃及木乃伊']],
 'Where’s Mummy? 妈妈在哪？an Egyptian mummy 埃及木乃伊，a mummy in a museum 博物馆里的木乃伊。',
 'Mummy〔称呼〕；an Egyptian mummy；a mummy in a museum。',
 'mummy 木乃伊不由母亲义变来；mummify 使成木乃伊走遗体那支，不是给人认个妈妈。',
 ('Mummy, can you read me a story?','妈妈，你能给我读个故事吗？'),('The museum displayed an Egyptian mummy.','博物馆展出了一具埃及木乃伊。'),sources=['https://www.etymonline.com/word/mummy','https://en.wiktionary.org/wiki/mummy#English'])
R('B4250','妈妈、保密的闭口声、菊花简称和木乃伊分源','MUM：先问是家庭、秘密、花店还是博物馆','mum/mummy 妈妈昵称；mum 沉默；mum 菊花简称；mummy 木乃伊又是借词。',
 '这组重点就是不强行统一。同音、同拼写既可能是缩短，也可能是另一语言一路借来的词。',
 'mummy/mam 等亲属昵称 → mum；闭口声 mum → keep mum；chrysanthemum → mum；波斯、阿拉伯等遗体物质词 → mummy。',
 [['同形场景逐个分开','mum · mummy']],
 'keep mum 保密而非照顾妈妈；mummy 妈妈与木乃伊另源；mums 花店里可能指菊花。',
 'Mum kept mum about our surprise visit to see the mummy at the museum.\n\n妈妈对我们要去博物馆看木乃伊的惊喜行程保了密。','mum mummy')
S=[['古英语 stelan → 中古英语 stelen → steal','暗中拿走、偷取'],['英语扩展','偷偷移动、拿走注意；a steal 便宜得像占大便宜的商品']]
W('steal','/stiːl/','偷取、盗用；悄悄移动；抢走注意；极划算的买卖',
 '把别人的东西悄悄拿走是偷；把脚步放轻、不让人注意也能说 steal away。商品便宜得像白拿，口语就叫 a steal。',
 '接古英语 stelan，不规则形式 steal/stole/stolen。暗中取走的核心画面推动悄悄离开、抢走风头等比喻；钢铁 steel 与它常同音但不同源。',S,
 'steal an idea 盗用想法，steal away 悄悄离开，steal the show 抢尽风头，at that price it’s a steal 那价格太划算了。',
 'steal an idea；steal away；steal the show；a steal。',
 'steal 常接被拿走的东西，rob 常接被抢的人、地点；steal a wallet，rob a bank。a steal 的便宜义不表示真是赃物。',
 ('Someone stole my wallet on the train.','有人在火车上偷了我的钱包。'),('At that price, the bicycle was a steal.','那辆自行车按那个价买太划算了。'))
W('stealth','/stelθ/','秘密行动、悄无声息；隐身、低可探测性〔技术义〕',
 '做了事，别人却没注意到；从暗中偷取走到暗中行动，再到让设备较难被探测。不是肉眼绝对看不见。',
 '接中古英语 stelthe，较早的古英语抽象名词 *stælþ 为推定形式，不能当作已找到的记录。词族联系 steal 与旧 -th 抽象名词材料，现代读音 steal /stiːl/、stealth /stelθ/ 不同。',S[:1]+[['推定古英语 *stælþ → 中古英语 stelthe → stealth','偷窃 → 秘密、难被察觉的行动'],['技术定语用法','降低被探测特征的相关性能']],
 'by stealth 暗中，move with stealth 悄悄行动，stealth technology 隐身技术，a stealth tax 暗中增加的税负〔批评性比喻〕。',
 'by stealth；move with stealth；stealth technology。',
 'stealth 低可探测性不等于魔法透明；stealthy 是相应形容词，stealth 名词也能作定语。',
 ('The cat approached with great stealth.','猫悄无声息地靠近。'),('The museum explains the meaning of stealth technology.','博物馆解释了隐身技术这个词的意思。'),sources=['https://www.etymonline.com/word/stealth'])
W('stealer','英 /ˈstiːlə/；美 /ˈstiːlər/','偷取者；抢戏者、夺人注意的人或物',
 '谁在偷取，就能用 -er 标角色；最熟悉的组合 scene stealer 不是盗窃电影胶片，而是抢尽场景风头的人、动物等。',
 'steal + -er，已有中古英语相应人物词。现代独立说小偷更常用 thief，stealer 尤适合和前面的对象、场景组成角色名。',S+[['steal + -er → stealer','偷取、抢走某物的人；夺走注意的比喻']],
 'a scene stealer 抢戏者，a base stealer 棒球盗垒者，a show stealer 抢尽表演风头的人物。',
 'a scene stealer；a base stealer；a show stealer。',
 'stealer 可以是比喻抢注意或体育术语，不保证真犯盗窃；steelworker 炼钢工里的 steel 又是另一词。',
 ('The little dog was the scene stealer in every shot.','那只小狗在每个镜头里都抢戏。'),('The young player became a skilled base stealer.','年轻球员成了一名熟练的盗垒手。'))
R('B4579','暗中拿走，延伸到悄悄行动、抢注意与划算买卖','STEAL：悄悄把东西带走，风头也能被抢走','steal → stealer 角色；stealth 是旧的秘密行动名词，对应元音不同。',
 '具体物品、注意力和行动是否被察觉，是同一个词族的不同观察点。a steal 反而是夸价格好，不要当成供认偷东西。',
 'stelan → steal/stole/stolen；steal + -er；推定古英语 *stælþ → 中古英语 stelthe → stealth，现代对应 -th。',
 [['偷取、比喻及执行者','steal · stealer'],['秘密、低可探测性质','stealth']],
 'steal/rob 宾语习惯不同；steal/steel 同音不同词；stealth /stelθ/ 不照 steal 的长元音读；a steal 可夸划算。',
 'The scene stealer moved with stealth and stole the show.\n\n那个抢戏的小家伙悄悄移动，却抢尽了风头。','steal stealer stealth')
R0=[['拉丁 Rōmānicē 等 → 古法语 romanz/romant','罗曼语、用俗语写的叙事'],['英语 romance / romantic','传奇、富想象叙事 → 爱情、浪漫；理想化'],['艺术与一般评价','Romanticism 特定流派；romanticize 把现实美化成故事']]
W('romance','英 /rəʊˈmæns/；美 /roʊˈmæns/','爱情、恋情；爱情故事、传奇；浪漫情调',
 '先是用通行俗语讲的叙事，常有骑士、冒险、爱情；后来把其中理想化爱情和传奇情调留在 romance 里。',
 '经法语 romanz 等，远接拉丁 Rōmānicē 以罗马式、罗曼语方式。语言名称到叙事类型再到恋情，不能只解释成罗马人天生会谈恋爱。',R0[:2],
 'a holiday romance 假日恋情，a romance novel 爱情小说，the romance of travel 旅行的浪漫情调；Romance languages 大写说罗曼语族。',
 'a holiday romance；a romance novel；the romance of travel；Romance languages。',
 'romance 恋情、情调、文学类型和 Romance languages 语言类名分场景；大写专门名称不能都翻成浪漫语言。',
 ('Their friendship developed into a romance.','他们的友谊发展成了恋情。'),('The book captures the romance of sea travel.','书捕捉了海上旅行的浪漫情调。'))
W('romantic','英 /rəʊˈmæntɪk/；美 /roʊˈmæntɪk/','爱情的、浪漫的；富想象、理想化的；浪漫主义的',
 '烛光晚餐是一种浪漫，想把人生过成壮丽传奇也可 romantic；艺术史的 Romantic 又是一种重情感、想象的流派关系，不只写情侣。',
 '接 romant/romance 叙事词及法语 romantique、拉丁相应形式，现代可认 romant- + -ic。传奇性质先于今天只谈恋爱的狭义联想。',R0,
 'a romantic dinner 浪漫晚餐，a romantic relationship 恋爱关系，a romantic view of the past 对过去的理想化看法，Romantic poetry 浪漫主义诗歌。',
 'a romantic dinner；a romantic relationship；a romantic view；Romantic poetry。',
 'romantic 不总等于爱情：romantic ideas about country life 可能是把乡居想得太美；Roman 罗马的不是同一个形容词。',
 ('They had a romantic dinner by the river.','他们在河边吃了一顿浪漫晚餐。'),('His romantic view of farming ignored the hard work.','他对务农的美好想象忽略了辛苦劳动。'),sources=['https://www.etymonline.com/word/romantic'])
W('romantically','英 /rəʊˈmæntɪkli/；美 /roʊˈmæntɪkli/','在恋爱关系上、以浪漫方式；理想化地',
 '两人 romantically involved 是有恋爱关系；风景被 romantically described，也可能只是被描绘得特别富诗意。',
 'romantic + -ally，-ic 形容词常有这一副词形式。常用读音结尾 /kli/，不必把每个写出的字母都添成独立音节。',R0+[['romantic + -ally → romantically','从爱情、浪漫想象的角度或方式']],
 'romantically involved 有恋爱关系，romantically linked 被传有恋爱关系，romantically describe 以浪漫想象描写。',
 'romantically involved；romantically linked；romantically describe。',
 'romantically linked 在报道里可能只是关系传闻表达，不证明事实；romantically 的理想化支也不一定谈爱情。',
 ('They were romantically involved for several years.','他们谈过几年恋爱。'),('The village was romantically described in the old travel book.','旧旅行书把村子描写得富有诗意。'))
W('romanticism','英 /rəʊˈmæntɪsɪzəm/；美 /roʊˈmæntɪsɪzəm/','浪漫主义；理想化、浪漫情怀',
 '一般用法可说把事物想得充满诗意；艺术史大写 Romanticism 则指特定传统，强调情感、想象、个人体验等，不只是恋爱文学。',
 'romantic + -ism，立场、风格、流派名词。词干末 c 在后续音节环境中读 /s/，不保留 romantic 末尾 /k/ 再加一个 /ɪzəm/。',R0+[['romantic + -ism → romanticism','浪漫情怀、理想化；特定艺术思想流派']],
 'literary Romanticism 文学浪漫主义，Romanticism in music 音乐浪漫主义，the romanticism of youth 青年人的浪漫情怀。',
 'literary Romanticism；Romanticism in music；the romanticism of youth。',
 'Romanticism 不是任何爱情故事的统称；romanticism 一般情怀与具体流派也需按上下文分。',
 ('The course examines Romanticism in poetry and painting.','课程考察诗歌与绘画中的浪漫主义。'),('The memoir balances youthful romanticism with practical detail.','回忆录把青年浪漫情怀和实际细节结合起来。'))
W('romanticize','英 /rəʊˈmæntɪsaɪz/；美 /roʊˈmæntɪsaɪz/','把……理想化、美化得浪漫',
 '只留夕阳、自由、冒险，把泥泞、疲惫、风险剪掉；把现实剪成美好传奇，就是 romanticize。',
 'romantic + -ize，形成使之具有理想化、传奇情调的动词；英式也常写 romanticise。这里 c 后接 i 的部分读 /s/。',R0+[['romantic + -ize → romanticize','把实际的人、生活、历史描绘得理想而浪漫']],
 'romanticize the past 美化过去，romanticize rural life 把乡村生活理想化，romanticize hardship 美化苦难。',
 'romanticize the past；romanticize rural life；romanticize hardship。',
 'romanticize 不只是添加恋爱剧情，更多说滤掉难处后的理想化；describe romantically 有时中性，romanticize 常带批评。',
 ('The film romanticizes life on the road.','电影把漂泊路上的生活美化了。'),('It is easy to romanticize the past and forget its difficulties.','人很容易美化过去，忘掉当年的困难。'))
W('unromantic','英 /ˌʌnrəʊˈmæntɪk/；美 /ˌʌnroʊˈmæntɪk/','不浪漫的；平实、不作美化的',
 '可以是不制造情侣气氛，也可以是老老实实讲日常琐碎、不把现实装成传奇；不一定是缺点。',
 'un- 不 + romantic，否定浪漫、理想化等性质；具体是哪一支由修饰对象决定。',R0+[['un- + romantic → unromantic','缺少爱情情调或传奇美化']],
 'an unromantic task 平淡琐碎的工作，an unromantic view 清醒、朴实的看法，an unromantic setting 没浪漫气氛的环境。',
 'an unromantic task；an unromantic view；an unromantic setting。',
 'unromantic 不自动等于 unloving 缺乏关爱；为人做琐碎家务可能很有爱，只是不像电影场面。',
 ('Washing the dishes is an unromantic but necessary task.','洗碗是一项平淡却必要的工作。'),('The book offers an unromantic account of life at sea.','书平实地讲述海上生活，没有刻意美化。'))
R('B4354','用俗语写的传奇，转到爱情、理想化和艺术流派','ROMANTIC：像传奇故事那样动人，后来才有多种浪漫','romance → romantic → romantically；romanticism 是情怀或流派；romanticize 美化；unromantic 平实或缺少情调。',
 '爱情只是其中一条线。骑士传奇、旅行想象、艺术史流派和把乡居想得过美，分别保留故事、情感、想象的特点。',
 'Rōmānicē → romanz/romant → romance/romantic；romantic + -ally/-ism/-ize；un- + romantic。',
 [['传奇、恋情与相关方式','romance · romantic · romantically'],['情怀流派与美化行为','romanticism · romanticize'],['不带浪漫滤镜','unromantic']],
 'Romance languages 不是浪漫语言；Romanticism 不只情侣文学；romanticize 不只是让人恋爱；unromantic 不等于 unloving。',
 'The unromantic account challenges our tendency to romanticize the past.\n\n这份平实的记述挑战了我们美化过去的倾向。','romance romantic romantically romanticism romanticize unromantic')
if __name__=='__main__':save('continuation_20261030_hk',ROOTS,WORDS)
