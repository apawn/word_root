"""Trail, rank and ray: paths and rankings without false word histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['古法语 trailler → 中古英语 trailen → trail','拖着走、循迹追踪；更远通常联系拉丁拖拉词族'],['拖行留下的痕迹 → trail 名词','踪迹、路径、小径'],['在后、沿路与开路','trailer 跟在后面；trailhead 起点；trailblazer 标路、开拓者']]
W('trail','/treɪl/','小径、踪迹；拖在后面、跟踪、落后',
 '衣角拖在身后，动物走过留下踪迹，人沿着踪迹走出小路：这些画面都能围绕跟在后面、留下一路痕迹理解。',
 '经中古英语接古法语 trailler，拖、追踪；更远通常联系拉丁拖拉词族，但具体链条保留可能性。名词从拖随物、痕迹扩到小径。',T,
 'a hiking trail 徒步小径，a trail of footprints 一串脚印，trail behind 落在后面，trail off 声音渐弱，an audit trail 可追查的记录链。',
 'a hiking trail；a trail of footprints；trail behind；trail off。',
 'trail 路径、痕迹或跟随，trial 试验、审判，字母顺序不同；trail behind 可说分数落后，不一定真的在跑。',
 ('We followed a narrow trail through the woods.','我们沿一条窄小径穿过树林。'),('Their team trailed by five points at half time.','半场时，他们队落后五分。'),
 sources=['https://en.wiktionary.org/wiki/trail#English','https://www.etymonline.com/word/trail'])
W('trailer','英 /ˈtreɪlə/；美 /ˈtreɪlər/','拖车、挂车；活动房车；影片预告片',
 '车跟在另一辆车后面被拖着走，很好理解；预告片名称也保留跟在正片后面的旧放映背景，今天通常提前放，名称却留下了。',
 'trail + -er，跟随者、拖随物，再指挂车等。电影义与早期附在正片后面的宣传短片有关，不把现代播放位置倒推为词名原意。',T[:2]+[['trail + -er → trailer','跟随、拖在后面的东西 → 挂车'],['电影宣传短片旧放映位置','曾跟在正片之后 → 今天常见预告片']],
 'a movie trailer 电影预告片，a travel trailer 旅行拖挂房车，a trailer attached to a car 汽车挂着的拖车。',
 'a movie trailer；a travel trailer；watch the trailer。',
 'trailer 预告片不是整部电影；拖车 trailer 与能自行行驶的房车 motorhome 不完全相同。',
 ('We watched the trailer before buying tickets.','买票前，我们看了预告片。'),('The car was pulling a small trailer.','汽车拖着一辆小挂车。'))
W('trailhead','/ˈtreɪlhed/','步道起点、小径入口',
 '一条徒步路线从这里进入：可能有路线牌、地图、停车点。head 在这里是路线的头、开始处。',
 'trail 小径 + head 头、起点；不是路上某个人的脑袋，也不是整片山区最高峰。',T[:2]+[['trail + head → trailhead','小径的头 → 步道入口、起点']],
 'meet at the trailhead 在步道入口碰面，a trailhead sign 步道入口标牌，drive to the trailhead 开车到步道起点。',
 'meet at the trailhead；a trailhead sign；drive to the trailhead。',
 'trailhead 通常起点、入口，summit 山顶是另一位置；从入口出发不保证路线一定上山。',
 ('We met at the trailhead at seven.','我们七点在步道入口碰面。'),('A map at the trailhead showed two routes.','步道入口的地图画出了两条路线。'))
W('trailblazer','英 /ˈtreɪlbleɪzə/；美 /ˈtreɪlbleɪzər/','开路者、先驱、开拓者',
 '先有人沿路做标记，后面的人才知道怎么走；比喻到工作、艺术，就是先试出一条新路的人。',
 'trail 路 + blaze 作路标的动作 + -er。这里 blaze 不是生火烧山，而是在树等处留下辨路标记的那支词义。',T[:2]+[['trail + blaze〔作路标〕+ -er → trailblazer','标出路线的人 → 带头开辟新领域的人']],
 'a trailblazer in science 科学领域的先驱，a musical trailblazer 音乐开拓者，be regarded as a trailblazer 被视为先驱。',
 'a trailblazer in；a musical trailblazer；a technological trailblazer。',
 'trailblazer 强调开新路，leader 领导者不一定第一个开路；blaze 此处作标记，不把故事编成点火清路。',
 ('She was a trailblazer in documentary filmmaking.','她是纪录片创作领域的开拓者。'),('The museum honours local trailblazers in science.','博物馆纪念本地科学先驱。'))
W('trailblazing','/ˈtreɪlbleɪzɪŋ/','开创性的、开辟新路的',
 '一项研究、一种做法以前没人这样做，它给后人开了路，就可以说 trailblazing。',
 'trail + blazing，对应 blaze a trail 开路、作标记的 -ing 形式，也作性质形容词；与 trailblazer 的人物名相邻记。',T[:2]+[['trail + blazing → trailblazing','开路的行动 → 开创性的性质']],
 'trailblazing work 开创性工作，a trailblazing researcher 开创道路的研究者，trailblazing research 开创性研究。',
 'trailblazing work；trailblazing research；a trailblazing career。',
 'trailblazer 是先驱人物，trailblazing 形容工作、人物具有开拓性；new 新不一定达到开创的程度。',
 ('The award recognized her trailblazing research.','奖项表彰了她的开创性研究。'),('His trailblazing work inspired younger designers.','他的开创性工作启发了年轻设计师。'))
R('B2781','拖随、留痕，沿痕迹形成路','TRAIL：身后的一道痕迹，可以变成后来人走的路','trail → trailer；trailhead 是路口；trailblazer → trailblazing 是开路人物与性质。',
 '预告片保留旧放映位置的名称；开拓者的 blaze 接做路标，不是点火烧出一条路。',
 'trailler 经中古英语 → trail；trail + -er/head；trail + blaze + -er/-ing。',
 [['路径、拖随物与入口','trail · trailer · trailhead'],['开路人物与开创性质','trailblazer · trailblazing']],
 'trail/trial 拼写不同；trailer 不等于正片；trailhead 非山顶；trailblazer 标路分支非烧路。',
 'A sign at the trailhead described the work of early trailblazers.\n\n步道入口的标牌介绍了早期开路者的工作。','trail trailer trailhead trailblazer trailblazing')
K=[['古法语 ranc、rang 等 → 中古英语 rank','行列 → 地位、等级、排名；较远为日耳曼语背景'],['rank 名词 → 排列、评级的动词','把对象放入次序；处于某名次'],['古英语 ranc → 另一路形容词 rank','旺盛、过度等旧义 → 难闻、十足等现代义；不与排名硬接']]
W('rank','/ræŋk/','等级、军衔、名次、行列；给……排名、处于某名次；难闻的、十足的〔另源形容词〕',
 '把一排人或事物摆出先后，就是 rank 的排名画面；但 rank smell 难闻气味走另一条旧词源，不能理解成高级气味。',
 '行列名词经法语接入英语，再发展等级和排名动词。难闻、过度的形容词接古英语 ranc，历史分开，不都从队伍名次生出来。',K,
 'military rank 军衔，rank first 排第一，rank among the best 名列前茅，the rank and file 普通成员，a rank smell 刺鼻臭味。',
 'military rank；rank first；rank among；the rank and file；a rank smell。',
 'rank 排名可按不同标准，不能自动等于品质；rank 形容难闻与 ranking 评级不在同一条意思链。',
 ('The school ranks among the best in the region.','学校名列当地前茅。'),('A rank smell came from the old drain.','旧排水沟飘出一股刺鼻臭味。'),
 sources=['https://en.wiktionary.org/wiki/rank#English','https://www.etymonline.com/word/rank'])
W('ranked','/ræŋkt/','列入排名的、有评级的；被排在某位的',
 '对象已经被放进一个排名系统；游戏 ranked matches 常说计入等级、排名的对局，不是每一局都有高水平玩家。',
 '排名动词 rank + -ed，过去分词也可作形容词；末尾 -ed 在这里读 /t/，不多加一个 /ɪd/ 音节。',K[:2]+[['rank + -ed → ranked','已被排名、计入评级的']],
 'a highly ranked university 排名靠前的大学，ranked matches 排位对局，ranked second 排名第二。',
 'a highly ranked university；ranked matches；ranked second。',
 'ranked 有排名或评级，highly ranked 才说明排名高；ranked 本身不保证最高或第一。',
 ('She chose a highly ranked university.','她选了一所排名靠前的大学。'),('He prefers ranked matches to casual games.','比起休闲对局，他更喜欢排位赛。'))
W('outrank','/ˌaʊtˈræŋk/','级别高于、排名超过',
 '把两个人、机构放在同一套等级里比，一个在另一个之上；这里 out- 是超过，不是走出队伍。',
 'out- 超过 + rank 等级、排名，形成比较级别高低的动词，后面可直接接比较对象。',K[:2]+[['out- + rank → outrank','在等级、名次等方面高于']],
 'outrank an officer 级别高于某军官，outrank a competitor 排名超过竞争者，outrank someone in seniority 资历级别更高。',
 'outrank someone；outrank a competitor；outrank in seniority。',
 'outrank 侧重等级、名次，outperform 表现更好；职位高不等于每件事做得更好。',
 ('She outranks him in the organization.','她在机构里的级别高于他。'),('The new model outranked its rivals in the survey.','新型号在调查排名中超过了对手。'))
R('B3853','从行列到相对等级、名次','RANK：把对象放进同一套次序里','rank → ranked；outrank 比谁等级、名次更高。难闻义另保留古英语来源。',
 '有排名不等于排得高；等级高不等于实际表现总更好；难闻气味也不是某种排行榜。',
 '法语 ranc、rang → rank 行列、等级 → 排名动词；rank + -ed；out- + rank；古英语 ranc 另形容词路径。',
 [['等级与比较','rank · ranked · outrank']],
 'ranked/highly ranked 是否评级与排名高；outrank/outperform 等级与表现；rank smell 另源。',
 'The highly ranked player outranked most of the competitors.\n\n那位排名靠前的选手名次高于大多数参赛者。','rank ranked outrank')
Y=[['拉丁 radius → 古法语 rai → 中古英语 → ray〔光线〕','杆、辐条、向外伸出的线 → 光线'],['拉丁 raia → 古法语 raie → 英语 ray〔鳐鱼〕','鱼名；较远来源不明，与光线分开'],['复合词分别接两义','sunray 接光线；stingray 接鳐鱼']]
W('ray','/reɪ/','光线、射线；一线希望；鳐鱼〔另来源〕',
 '太阳往外射出一条光，可想成轮辐向外伸；海里扁平的 ray 却是鱼名，不是因为它会发射太阳光。',
 '光线经法语接拉丁 radius，杆、辐条等；鱼名经法语接拉丁 raia，较远来源不明。两条路径不能只因形似就合并。',Y,
 'a ray of sunlight 一缕阳光，a ray of hope 一线希望，gamma rays 伽马射线，a ray swimming near the bottom 靠近水底游动的鳐鱼。',
 'a ray of sunlight；a ray of hope；gamma rays；a ray of light。',
 'ray 鱼与光线同拼写异源；ray of hope 是希望像暗处透来一线光的比喻，不是鱼带来了希望的固定故事。',
 ('A ray of sunlight fell across the desk.','一缕阳光落在桌面上。'),('A ray glided over the sandy seabed.','一条鳐鱼滑游过沙质海底。'),
 sources=['https://en.wiktionary.org/wiki/ray#English','https://www.etymonline.com/word/ray'])
W('sunray','/ˈsʌnreɪ/','太阳光线、一缕阳光',
 '太阳照来的一道光，sun 指来源，ray 指一道光线；不是新的光学单位。',
 'sun 太阳 + ray 光线，组成来源明确的光线名称。也常用分写 sun ray，词义不变。',Y[:1]+[['sun + ray → sunray','太阳发出的光线']],
 'a golden sunray 一道金色阳光，sunrays through the clouds 穿过云层的阳光，the first sunrays 最初照来的阳光。',
 'golden sunrays；sunrays through the clouds；the first sunrays。',
 'sunray 常一道光，sunlight 泛指阳光；ray 的鱼名不是本词的构词基础。',
 ('A sunray slipped through the curtains.','一缕阳光透过窗帘。'),('Golden sunrays lit the clouds.','金色阳光照亮了云层。'))
W('stingray','/ˈstɪŋreɪ/','魟、带尾刺的鳐类',
 'ray 这里是扁平的鱼；sting 提醒这种鳐类有能造成刺伤的尾刺，不是在说一束会蜇人的光。',
 'sting 刺、蜇 + ray 鳐鱼，按尾部刺的特征命名；并不是所有 ray 都能随意换成 stingray。',Y[1:2]+[['sting + ray〔鱼〕→ stingray','具有尾刺特征的鳐类名称']],
 'a stingray gliding over sand 在沙上滑游的魟，a stingray’s tail 魟的尾部，watch a stingray 观察魟。',
 'a stingray’s tail；watch a stingray；a stingray gliding over sand。',
 'stingray 是鳐类中的一类，ray 范围更广；名称的 sting 接刺，不接动词 sing 唱歌。',
 ('A stingray glided past the reef.','一条魟从礁旁滑游而过。'),('The guide pointed out the stingray’s long tail.','向导指给我们看魟的长尾巴。'))
R('B2717','一道光与另一条鱼名路径','RAY：光线向外伸，鳐鱼另有鱼名来源','ray 先分光、鱼；sunray 归光线，stingray 归鱼。',
 'ray 与 radius 同族的线条画面很直观；鳐鱼不能为了同拼写硬解释成海里的光线。',
 'radius 经 rai → ray 光；raia 经 raie → ray 鱼；sun + ray；sting + ray。',
 [['光线与来源','ray · sunray'],['鳐类的具体名称','stingray']],
 'ray 两源；sunray/sunlight 一道光与泛指阳光；stingray 非全部 ray 的无差别替换。',
 'Sunrays lit the water above a passing stingray.\n\n阳光照亮水面下方，一条魟正游过。','ray sunray stingray')
R('B2709','一个环接一个环，形成连续链条','CHAIN：每一节都接着下一节','chain → keychain、blockchain，先实物连接，再借连续、相互衔接的结构。',
 '钥匙链是实际串联；区块链借链式关系命名，不能只靠 chain 一个词推断系统一定可靠或适合某用途。',
 '拉丁 catēna 经法语、英语 → chain；key + chain；block + chain。',
 [['基础链条与钥匙链','chain · keychain'],['信息结构中的链','blockchain']],
 'chain 可锁链、连锁店、事件链；keychain 和 blockchain 的连接对象不同。',
 'The diagram showed the blocks connected in a chain.\n\n图里显示各个区块按链式关系连接。','chain keychain blockchain')
if __name__=='__main__':save('continuation_20261030_ei',ROOTS,WORDS)
