"""Gas and allow: scientific naming, everyday fuel and permission."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
GA=[['17世纪范·海尔蒙特创造 Dutch gas','通常认为联系希腊 khaos 空阔、虚空'],['英语 gas','气体 → 燃气；另有 gasoline 的美式缩略']]
def GH(f,m):return GA+[[f,m]]
W('gas','/ɡæs/','气体；燃气；汽油〔美式缩略〕',
 '最基本是气态物质；厨房里常指燃气，加油站里美式 gas 却可能是液体汽油。',
 '借荷兰语 gas，是17世纪化学家范·海尔蒙特造的词，通常联系希腊 khaos。汽油义另是 gasoline 的缩略，不表示汽油常温下一定是气体。',GA,
 'natural gas 天然气，a gas cooker 燃气灶；美式 a gas station 加油站，run out of gas 汽油用完。必须看国家用法及场景。',
 'natural gas；gas and electricity；a gas station；run out of gas。',
 'gas 泛指气态物质，air 空气是一种混合物；gas 在美式燃油语境又可指汽油，不能一律译成天然气。',
 ('The house uses gas for heating.','房子用燃气供暖。'),('We stopped at a gas station to fill the tank.','我们在加油站停下加满油箱。'),sources=['https://www.etymonline.com/word/gas','https://en.wiktionary.org/wiki/gas#English'])
W('gasoline','/ˈɡæsəliːn/','汽油〔尤美式〕',
 '给许多汽车发动机使用的一种液体燃料；名字有 gas，东西本身却是液体。',
 '19世纪 gasolene、gasoline 等形式发展而来，通常分析 gas + 表油的 -ol + 化学命名 -ine；早期商品名影响也有不同解释，不把具体品牌故事写死。',GH('gas + -ol + -ine；19世纪 gasolene／gasoline','石油制得的挥发性液体燃料'),
 'unleaded gasoline 无铅汽油，a gasoline engine 汽油发动机。美式常缩 gas，英式多用 petrol。',
 'unleaded gasoline；a gasoline engine；the price of gasoline。',
 'gasoline 汽油、diesel 柴油是不同燃料名称；gasoline 与 gas 的物态含义不能机械等同。',
 ('This engine runs on gasoline.','这台发动机用汽油。'),('The price of gasoline rose during the summer.','夏季汽油价格上涨了。'),sources=['https://www.etymonline.com/word/gasoline','https://en.wiktionary.org/wiki/gasoline#English'])
W('gaseous','/ˈɡæsiəs/；也读 /ˈɡæʃəs/','气态的；气体的',
 '强调物质处于气态，像水蒸气；这是一种物态描述。',
 'gas + -eous，-eous 形成与某物相关、具有某性质的形容词。读音有 /siəs/ 与 /ʃəs/ 等变体。',GH('gas + -eous → gaseous','与气体有关、呈气态'),
 'a gaseous state 气态，gaseous oxygen 气态氧，gaseous emissions 气体排放。',
 'a gaseous state；gaseous oxygen；gaseous emissions。',
 'gaseous oxygen 不等于 air，空气含多种气体；gassy 常描述含气、起泡或胀气，更日常。',
 ('The substance becomes gaseous when heated.','这种物质加热后变为气态。'),('The diagram compares solid, liquid and gaseous states.','图示比较固态、液态与气态。'))
W('gassy','/ˈɡæsi/','含气的；起泡的；胀气的',
 '饮料里气泡多，或者肚子里气多；强调有很多气。',
 'gas + -y，通常双写 s 成 gassy；-y 表带有这种性质。比 gaseous 更常用于日常感受。',GH('gas + -y → gassy','含很多气、起泡；有胀气感'),
 'a gassy drink 气泡多的饮料，feel gassy 感到肚子胀气。这里是日常状态描述。',
 'a gassy drink；feel gassy；too gassy。',
 'gassy drink 是液体含气泡，gaseous state 是物质呈气态；二者并非一个有气就能互换。',
 ('The drink was too gassy for her taste.','这饮料气泡太多，不合她口味。'),('He said he felt gassy after lunch.','他说午饭后觉得肚子胀气。'))
W('gasification','英 /ˌɡæsɪfɪˈkeɪʃən/；美 /ˌɡæsəfɪˈkeɪʃən/','气化；制取可燃气体的转化过程',
 '把煤、生物质等原料经过反应，变成可使用的气体混合物；工业语境常说这种处理。',
 'gas + -ification，后部表示使成为的过程，关联动词 gasify。技术义已固定，不能只按变成气就把所有蒸发都这样叫。',GH('gas + -ification → gasification','转化成气体；工业上将含碳原料转成合成气等'),
 'coal gasification 煤气化，biomass gasification 生物质气化。工业过程常得到含一氧化碳、氢等成分的气体混合物。',
 'coal gasification；biomass gasification；a gasification plant。',
 '工业 gasification 常包含化学反应；vaporization 汽化常强调液体变气体的物理变化。中文都近气化，英文需看过程。',
 ('The report compares coal gasification with other fuel processes.','报告比较煤气化与其他燃料处理过程。'),('The plant uses biomass gasification to produce a fuel gas.','工厂用生物质气化生产燃料气。'))
W('gasworks','英 /ˈɡæswɜːks/；美 /ˈɡæswɜːrks/','煤气厂；燃气生产、供应设施',
 '城市以前造煤气、储气、供气的工业场所，旧厂房改造报道里也常见。',
 'gas + works，works 是工业厂房、工场的固定名词用法，不是这里有人工作的第三人称动词。',GH('gas + works〔工厂设施〕→ gasworks','生产或供应燃气的厂区'),
 'the old gasworks 旧煤气厂，a former gasworks site 原煤气厂地块。以 s 结尾也能指一个工厂。',
 'the old gasworks；a former gasworks site；the local gasworks。',
 'gasworks 工厂与 gas station 加油站不同；works 在这类名称里可单数意义，不能只见 s 就按多家厂处理。',
 ('The old gasworks has been converted into an arts centre.','旧煤气厂已改成艺术中心。'),('The map marks the site of a former gasworks.','地图标出了原煤气厂的位置。'))
R('B2516','气体、燃气、汽油及状态、工业过程','GAS：先分气态总称与美式汽油缩略','gas → gasoline；gaseous 气态与 gassy 含气相邻；再接制气过程和煤气厂。',
 'gas 是科学造词，后来成为气体总称和燃气名；汽油 gas 是 gasoline 缩略。较冷门俚语和设备词先略，biogas 已有精讲共享。',
 'gas → gaseous、gassy；gas + -ol + -ine → gasoline；gas + -ification；gas + works；bio- + gas。',
 [['基本气体与燃油','gas · gasoline'],['性质','gaseous · gassy'],['制气与来源','gasification · gasworks · biogas']],
 'gas station 美式加油站；gaseous 气态、gassy 含气；gasification 工业反应与普通蒸发分清。',
 'The old gasworks is now an exhibition about gas and the city.\n\n旧煤气厂现在是介绍燃气与城市历史的展馆。',
 'gas gasoline gaseous gassy gasification gasworks biogas')
AL=[['拉丁 allocāre〔安排、分配〕；allaudāre〔赞同、称赞〕','两条来源在法语相近形式中汇合'],['法语 alouer 等 → 英语 allow','分配、承认、认可 → 允许；为某事留出条件']]
W('allow','/əˈlaʊ/','允许；给予；留出；考虑到',
 '你可以这样做，是允许；给预算留一笔、给路上留半小时，也是给这件事留出位置。',
 '经法语相近词汇合：一支接 allocāre 分配，一支接 allaudāre 赞同、认可。现代允许与留出等义共同留下这两支影响，不拆成 all + low。',AL,
 'allow someone to do 允许某人做，allow time for 留出时间，allow for delays 考虑可能延误；Smoking is not allowed 禁止吸烟。',
 'allow someone to do；allow time for；allow for；be allowed to。',
 'allow someone to do，let someone do；两者接动词方式不同。allow for 不是允许延误发生，而是把它计入安排。',
 ('The ticket allows visitors to enter the garden twice.','这张票允许游客进入花园两次。'),('Allow extra time for the journey during rush hour.','高峰时段出行要多留些时间。'),sources=['https://www.etymonline.com/word/allow','https://en.wiktionary.org/wiki/allow#English'])
W('allowance','/əˈlaʊəns/','零用钱；津贴；配额、限额；考虑余地',
 '给某人预留的一份钱或额度：孩子每周零用钱、员工出差津贴、行李可带多少。',
 '借古法语 alouance，经中古英语进入；现代可对应 allow + -ance。与 allow 一样涉及分配、批准，不是只讲允许的抽象名词。',AL+[['法语 alouance → 英语 allowance','获分配的钱、额度；考虑调整余地']],
 'a weekly allowance 每周零用钱，a travel allowance 出差津贴，baggage allowance 行李限额；make allowances for 考虑到、体谅某种情况。',
 'a weekly allowance；a travel allowance；baggage allowance；make allowances for。',
 'allowance 不全是 salary 工资；额度可按重量、金额等衡量。make allowances for inexperience 是体谅经验不足，不是给经验发津贴。',
 ('She saves part of her weekly allowance.','她把每周零用钱的一部分存起来。'),('We should make allowances for his lack of experience.','我们应考虑到他经验不足。'))
W('allowable','/əˈlaʊəbl/','允许的；可接受的；在限度内的',
 '规则画出一条界线，界线以内可以接受、可以计入的，就是 allowable。',
 '经中古英语接古法语 alouable，与 allouer 同族；现代可分析 allow + -able。不是每个 -able 都只说物理上做得到。',AL+[['法语 alouable → 英语 allowable','可认可、可允许；符合限度']],
 'the maximum allowable weight 最大允许重量，an allowable error 允许误差，allowable expenses 可计入的费用。具体界线依规则而定。',
 'maximum allowable weight；allowable limits；allowable error。',
 'possible 可能做到，allowable 规则上允许；possible but not allowable 可以发生，却不合规定。',
 ('The bag exceeds the maximum allowable weight.','包的重量超过允许上限。'),('The difference falls within the allowable margin of error.','差异在允许误差范围内。'))
R('B3592','允许、分配、留出与可接受限度','ALLOW：批准可以做，也能给事情留一份','allow 基本动作，allowance 分配的钱、额度，allowable 规则允许的性质。',
 '法语相近形式合并了分配和赞同两支历史，今天的多义因此不能只硬译成允许。',
 'allow → 相关名词 allowance、形容词 allowable；后二者各保留法语借入历史。',
 [['动作、份额与限度','allow · allowance · allowable']],
 'allow someone to do 对照 let someone do；allow for 计入；allowance 不全是工资；allowable 不只是可能。',
 'The allowance must stay within the allowable budget.\n\n津贴必须在允许预算内。',
 'allow allowance allowable')
if __name__=='__main__':save('continuation_20261030_t',ROOTS,WORDS)
