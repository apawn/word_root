"""Buildings, homes and streets, plus rooms and furniture vocabulary."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2834':dict(words=['building','buildings'],label='build → building → buildings：建成的一座座整体',note='-ing 的名词分支可指建成物，buildings 是建筑物复数。'),
 'B3150':dict(words=['home','homes'],label='home → homes：家、居所与归属',note='古英语居住地、村落的词族延续，现代家与住宅的重点按语境看。'),
 'B3082':dict(words=['house','houses'],label='house → houses：房屋与提供容纳处',note='house 名词通常末尾 s，复数 houses 通常 z 加 iz；动词本来常以 z 结尾。'),
 'C1418':dict(words=['street','streets'],label='street → streets：铺好的路与街道',note='拉丁铺路词很早借入日耳曼语，再成为古英语 street 的祖先。'),
 'B2780':dict(words=['road','roads'],label='road → roads：从出行、骑行到通行的路',note='古英语 rad 与 ride 同族，路的意义后来突出。'),
 'B2493':dict(words=['wall','walls'],label='wall → walls：防御墙与隔开空间的墙',note='较早由拉丁 vallum 借入日耳曼语，古英语 weall 延续为 wall。'),
 'B3167':dict(words=['floor','floors'],label='floor → floors：承托的表面、楼层与下限',note='古英语铺地、地面的词族，后发展为楼层与底线。'),
 'C0190':dict(words=['ceiling','ceilings'],label='ceil → ceiling → ceilings：室内上方的覆盖与上限',note='ceiling 接中古英语给房间装板饰的动词，更早词源分析不同；现代天花板与上限义明确。'),
 'B3841':dict(words=['seat','seats'],label='sit／seat → seats：坐的位置与安排入座',note='北欧、较早英语座位词族相互联系，现代 seat 也有给人安排座位的动词。'),
 'B3461':dict(words=['table','tables'],label='table → tables：平面家具与排成行列的信息',note='拉丁 tabula 板、列表，经较早英语借入和法语影响形成现代词。'),
 'C0524':dict(words=['chair','chairs'],label='chair → chairs：椅子与坐在主持席的人',note='希腊座位词经拉丁、法语传入，再由席位联系主席、主持人职务。'),
 'B2739':dict(words=['bed','beds'],label='bed → beds：躺卧处与承托的地层、园地',note='本族床、铺垫词的历史分支，形成花坛、河床等常见用法。'),
 'B2808':dict(words=['desk','desks'],label='desk → desks：书写桌与接待、业务台',note='中世纪拉丁书写桌词，远接盘、平面器物的希腊、拉丁词族。'),
}
W('buildings','/ˈbɪldɪŋz/','建筑物；楼房〔building 的复数〕',
 '把材料搭成可以使用的一座整体，是 a building；一座座这样的建筑就是 buildings。',
 'build + -ing → building，再加 -s，/ŋ/ 后读 /z/。build 接古英语 byldan、bytlan 等建造词；building 在较早英语已有建造过程、建筑物的名词用法。这里 -ing 名词指建成物。',
 [['古英语建造词 → build → building','建造 → 建造过程、建成的建筑物'],['building + -s → buildings','多座建筑物']],
 'old buildings 老建筑；public buildings 公共建筑；office buildings 办公楼；buildings around the square 广场周围的建筑。',
 'a group of buildings；buildings made of stone。','building 可以是住宅、办公楼、学校等建筑，house 通常更偏住宅。building work 则说建筑施工，buildings 这个复数一般数建成的建筑物。',
 ('Several old buildings surround the square.','广场周围有几座老建筑。'),('The map marks all the public buildings in the town.','地图标出了镇上的所有公共建筑。'),sources=['https://en.wiktionary.org/wiki/buildings#English','https://en.wiktionary.org/wiki/building#English'])
W('homes','英 /həʊmz/；美 /hoʊmz/','家；住宅、居所；生活、归属之地〔复数〕',
 '人生活、安定下来、感到有所归属的地方是 home；多个人、家庭各自的家，合起来就是 homes。',
 'home + -s，/m/ 后读 /z/。home 继承古英语 hām，经中古英语 hom 延续，早有家、居住地、村落等义；现代可强调家庭归属，也可指住宅。',
 [['古英语 hām → 中古英语 hom → home','居住地、家、村落'],['home + -s → homes','多个家、居所或住宅']],
 'family homes 家庭住宅；find homes for the animals 为动物寻找安置之家；return to their homes 回到各自家中。',
 'homes near the coast；make people feel at home〔相关表达〕。','home 常带生活、归属的感觉，house 更强调房屋本身；houses can become homes 可以说房子成了安居的家。homes 也可在房产语境直接说住宅。',
 ('The volunteers helped the families return to their homes.','志愿者帮助这些家庭回到各自家中。'),('The shelter finds new homes for abandoned animals.','收容所为被遗弃的动物寻找新的家。'),sources=['https://en.wiktionary.org/wiki/homes#English','https://en.wiktionary.org/wiki/home#English'])
W('houses','通常 /ˈhaʊzɪz/','房屋、住宅；机构、专门场所〔复数〕；容纳、安置〔第三人称单数〕',
 '一栋栋可住人的房子，是 houses；把东西、人安放在一个建筑里，也能用动词 houses。',
 'house + -s。名词 house 常读 /haʊs/，普通复数 houses 通常变为 /ˈhaʊzɪz/；动词 house 常以 /z/ 结尾，第三人称也通常读 /ˈhaʊzɪz/。词族接古英语 hūs 住所及相关形式。',
 [['古英语 hūs → 中古英语 hous → house','房屋、住所；相关容纳动词用法'],['house + -s → houses','多栋房屋；单数主语容纳；常见读音 /ˈhaʊzɪz/']],
 'terraced houses 排屋；old houses 老房子；publishing houses 出版社；houses a collection 收藏、容纳一批藏品。',
 'houses along the river；the building houses ...。','名词 houses 在 These houses are old 中配复数谓语；The building houses a museum 中是动词，表示这栋楼里设有博物馆。publishing houses 是出版社这一机构用法。',
 ('The houses on this street have small front gardens.','这条街上的房子都有小前花园。'),('The old hall houses a collection of local photographs.','旧礼堂里收藏着一批当地照片。'),sources=['https://en.wiktionary.org/wiki/houses#English','https://en.wiktionary.org/wiki/house#English'])
W('streets','/striːts/','街道〔复数〕',
 '两旁常有建筑、店铺，穿过城镇日常生活的一条条路，是 streets；它的较早名称与铺好的道路有关。',
 'street + -s，/t/ 后读 /s/。street 继承古英语 strēt、strǣt，更早是日耳曼语借入的拉丁 (via) strāta 铺好的路，关联 sternere 铺开。',
 [['拉丁 sternere、strāta → 较早日耳曼语借词 → 古英语 street 祖形','铺开、铺好 → 铺成的路'],['street + -s → streets','多条街道']],
 'busy streets 繁忙街道；narrow streets 狭窄街道；streets lined with shops 两旁有商店的街道。',
 'walk through the streets；streets around the square。','street 常带城镇内、两边有建筑的道路感觉；road 的范围更广，也可连接不同地方。实际路名和使用习惯有重合，不把两词硬分成绝对两类。',
 ('We walked through the narrow streets near the harbour.','我们走过港口附近狭窄的街道。'),('The streets were quiet early in the morning.','清晨街道上很安静。'),sources=['https://en.wiktionary.org/wiki/streets#English','https://en.wiktionary.org/wiki/street#English'])
W('roads','英 /rəʊdz/；美 /roʊdz/','道路；通行路线；途径〔复数〕',
 '让人、车辆能从一处走到另一处的路，是 roads；达成目标也可比作沿着某条路前进。',
 'road + -s，/d/ 后读 /z/。road 接古英语 rād 骑行、行程，经中古英语 rode 延续，与 ride 同族；由出行本身发展到出行所走的道路。',
 [['古英语 rād → 中古英语 rode → road','骑行、行程 → 通行的路'],['road + -s → roads','多条道路、路线；比喻途径']],
 'country roads 乡间道路；main roads 主路；roads leading to the town 通往镇上的道路；roads to success 通向成功的途径。',
 'roads through the hills；roads connecting the villages。','roads 说通行道路，routes 常更强调从起点到目的地怎样走的路线。the road to something 也可说通向某目标、结果的过程。',
 ('Heavy rain made the country roads difficult to use.','大雨让乡间道路难以通行。'),('Two roads connect the village with the nearby town.','有两条道路把村庄和附近的镇子连接起来。'),sources=['https://en.wiktionary.org/wiki/roads#English','https://en.wiktionary.org/wiki/road#English'])
W('walls','英 /wɔːlz/；美 /wɔːlz, wɑːlz/','墙、墙壁；障碍〔复数〕；筑墙隔开〔第三人称单数〕',
 '立起来把空间隔开、围住的东西，是 walls；阻挡沟通、行动的障碍，也可以借墙的画面表达。',
 'wall + -s，/l/ 后读 /z/。wall 继承古英语 weall，较早由拉丁 vallum 防御墙、土垒一类词借入日耳曼语；后来广用于室内外的墙。',
 [['拉丁 vallum → 日耳曼借词 → 古英语 weall → wall','防御土垒、墙 → 普通墙壁'],['wall + -s → walls','多面墙；隔开、阻挡的比喻']],
 'stone walls 石墙；walls of the room 房间的墙；walls between people 人与人之间的隔阂；within these walls 在这些墙内、在这里。',
 'pictures on the walls；walls surrounding the garden。','wall 是立着隔开空间的墙；floor 是下面承托的地面，ceiling 是室内上方表面。比喻的 walls 常强调阻碍、隔开，不只说建筑材料。',
 ('Old photographs hung on the walls of the hall.','礼堂的墙上挂着老照片。'),('The garden is surrounded by low stone walls.','花园四周围着低矮的石墙。'),sources=['https://en.wiktionary.org/wiki/walls#English','https://en.wiktionary.org/wiki/wall#English'])
W('floors','英 /flɔːz/；美 /flɔːrz/','地板、地面；楼层；下限〔复数〕',
 '下面托住人、家具的平面是 floor；一栋楼上下分出的每一层，也可以叫 floor。把数量限制在某个最低位置，还有下限的用法。',
 'floor + -s，词尾读 /z/。floor 继承古英语 flōr，经中古英语延续，较早有地面、铺地、甲板等承托表面义；楼层、下限等分别发展。',
 [['古英语 flōr → 中古英语 → floor','地面、铺地等承托表面'],['floor + -s → floors','多个地板、楼层或下限']],
 'wooden floors 木地板；upper floors 楼上各层；three floors 三层；price floors 价格下限。',
 'clean the floors；rooms on different floors。','英式 ground floor 常说地面层，first floor 通常是上面一层；美式 first floor 常说地面层。读具体楼层指示时看当地习惯，floors 的楼层义本身不变。',
 ('The old house has wooden floors in every room.','这栋老房子的每个房间都是木地板。'),('The library occupies three floors of the building.','图书馆占用了这栋建筑的三层。'),sources=['https://en.wiktionary.org/wiki/floors#English','https://en.wiktionary.org/wiki/floor#English'])
W('ceilings','/ˈsiːlɪŋz/','天花板；上限〔ceiling 的复数〕',
 '房间里面抬头能看见的顶部，是 ceiling；数字、费用被划定不能超过的位置，也像头顶的一块板，所以叫上限。',
 'ceiling + -s，/ŋ/ 后读 /z/。ceiling 接中古英语 ceil、celen 给房间装板饰等动词及 -ing 名词；更早来源有隐藏、覆盖或雕饰等不同分析，不强定一条唯一拉丁路线。',
 [['中古英语 ceil、celen → ceiling','给建筑表面装板饰 → 上方覆盖、天花板'],['ceiling + -s → ceilings；比喻扩展','多个天花板；不同上限']],
 'high ceilings 高天花板；painted ceilings 彩绘天花板；spending ceilings 支出上限；ceilings on charges 收费上限。',
 'rooms with low ceilings；set ceilings on spending。','ceiling 是室内看见的上方表面，roof 是建筑外部顶部结构。比喻数值时 ceiling 是上限，floor 是下限。',
 ('The old rooms have unusually high ceilings.','那些老房间的天花板特别高。'),('The plan sets separate spending ceilings for each department.','计划为各部门分别设定了支出上限。'),sources=['https://en.wiktionary.org/wiki/ceilings#English','https://en.wiktionary.org/wiki/ceiling#English','https://www.etymonline.com/word/ceiling'])
W('seats','/siːts/','座位；席位；给……安排座位、可容纳〔第三人称单数〕',
 '能坐下的位置是 seats；组织、议会中的一个正式名额也像席位。动词 seats 则说安排别人坐下，或一个场所有多少座位。',
 'seat + -s，/t/ 后读 /s/。seat 的较早词形涉及古英语 sǣte、古诺尔斯语 sæti 及中古英语 sete，都是坐的位置词族，借入、同源影响细节有不同分析。',
 [['较早英语、北欧座位词族 → 中古英语 sete → seat','坐的位置、所在处'],['seat + -s → seats','多个座位、席位；单数主语安排入座、容纳']],
 'empty seats 空座位；front seats 前排座位；seats on the committee 委员会席位；seats fifty people 可坐五十人。',
 'reserve seats；take your seats。','seat 侧重可坐的位置，chair 侧重椅子这一家具；一排长椅可以有多个 seats。The hall seats fifty 中 seats 是动词，说明容纳人数。',
 ('We reserved two seats near the front.','我们预订了两个靠前的座位。'),('The small hall seats about fifty people.','这间小礼堂能坐大约五十人。'),sources=['https://en.wiktionary.org/wiki/seats#English','https://en.wiktionary.org/wiki/seat#English'])
W('tables','/ˈteɪbəlz/','桌子；表格；提出或搁置议案〔第三人称单数，地区用法不同〕',
 '把东西放在平面上，是桌子；把信息整齐排在平面上，就是表格。把议案放上讨论桌，也发展出了动词，不过英美会议语境的重点可能相反。',
 'table + -s，/l/ 后读 /z/。table 接拉丁 tabula 板、写字板、列表，有较早英语借词及后来法语 table 的共同影响；名词再有把事项摆上桌的动词用法。',
 [['拉丁 tabula → 较早英语及法语 table → 英语 table','板、列表 → 桌子、表格'],['table + -s → tables；动词引申','多个桌子、表格；提出或暂时搁置事项']],
 'dining tables 餐桌；data tables 数据表；multiplication tables 乘法表；tables a proposal 处理一项议案〔看地区语境〕。',
 'tables in the report；tables arranged in a circle。','名词 tables 的桌子、表格靠场景区分。会议动词 table 在英式语境常说正式提出供讨论，在美式语境常说暂时搁置；读具体程序句时看后文。',
 ('The tables in the report summarize the main results.','报告中的表格概括了主要结果。'),('We pushed two tables together for the meal.','我们把两张桌子拼在一起吃饭。'),('The chair tables the proposal because several members are absent.','由于几名成员缺席，主持人暂时搁置提案。〔美式会议用法〕'),sources=['https://en.wiktionary.org/wiki/tables#English','https://en.wiktionary.org/wiki/table#English','https://www.merriam-webster.com/dictionary/table'])
W('chairs','英 /tʃeəz/；美 /tʃerz/','椅子；主席、主持人〔复数〕；主持会议、担任主席〔第三人称单数〕',
 '人坐下的家具是 chairs；坐在主持席上、负责带领会议的人，也用 chair 称呼，动词 chairs 就说主持。',
 'chair + -s，词尾读 /z/。chair 经法语 chaiere、拉丁 cathedra 接希腊 kathédra，较早 katá 与 hédra 座位相连；席位引申权威职务，英语又有主持动词。',
 [['希腊 kathédra → 拉丁 cathedra → 法语 → chair','座位 → 椅子；权威席位、主持人'],['chair + -s → chairs','多把椅子、多个主席；单数主语主持']],
 'wooden chairs 木椅；committee chairs 委员会主席；chairs the meeting 主持会议；pull up chairs 拉来椅子。',
 'chairs around the table；chairs a discussion。','chair 是椅子或主持人的名词，也可以作动词；seat 更强调可坐的位置。She chairs the meeting 说她主持会议，She sits on a chair 才直接说坐在椅子上。',
 ('We arranged the chairs in a circle.','我们把椅子围成了一圈。'),('She chairs the weekly planning meeting.','她主持每周的规划会议。'),sources=['https://en.wiktionary.org/wiki/chairs#English','https://en.wiktionary.org/wiki/chair#English'])
W('beds','/bedz/','床；苗床、花坛；河床、底层〔复数〕',
 '供人躺下休息的地方是 beds；承托花草、河水或材料的一片底部，也常用 bed 的承托、铺垫画面来命名。',
 'bed + -s，/d/ 后读 /z/。bed 继承古英语 bedd，床、铺垫和地块等历史用法相连，更远来源有不同推测；现代花坛、河床等分支各有固定用法。',
 [['古英语 bedd → 中古英语 → bed','躺卧、铺垫之处；床和地块等相关义'],['bed + -s → beds','多张床；多块花坛、多个底层']],
 'single beds 单人床；flower beds 花坛；river beds 河床；beds of gravel 一层层砾石。',
 'make the beds；flowers in raised beds。','make the beds 通常是整理床铺；flower beds 是栽花的地块，river beds 是河流底部。bed 的承托、铺垫感觉能帮你连义，固定搭配仍要看对象。',
 ('The room has two single beds.','房间里有两张单人床。'),('The gardener planted flowers in the beds beside the path.','园丁在小路旁的花坛里种上了花。'),sources=['https://en.wiktionary.org/wiki/beds#English','https://en.wiktionary.org/wiki/bed#English'])
W('desks','/desks/','书桌、办公桌；接待台；业务部门〔复数〕',
 '给人读写、办公用的一张张桌子，是 desks；有人坐在台后负责接待、处理某类业务，desk 也发展出服务台、业务部门的意思。',
 'desk + -s，末尾 /sks/ 连读，通常不另加元音。desk 经中世纪拉丁 desca 写字桌，可能有意大利语 desco 的中介，较早接拉丁 discus、希腊 dískos 盘、平面器物。',
 [['希腊 dískos、拉丁 discus → 中世纪拉丁 desca 等 → desk','盘、平面器物 → 写字桌'],['desk + -s → desks','多个书写、办公桌；多个服务台、业务部门']],
 'school desks 课桌；office desks 办公桌；reception desks 接待台；news desks 新闻编辑部门。',
 'desks by the window；students at their desks。','desk 通常给读写、办公用，table 范围更广。the news desk 说负责某类新闻的部门时，不只是在数一件家具；desks 的具体含义看修饰词。',
 ('The desks were arranged beside the windows.','书桌沿窗摆放。'),('The building has reception desks at both entrances.','这栋楼的两个入口都设有接待台。'),sources=['https://en.wiktionary.org/wiki/desks#English','https://en.wiktionary.org/wiki/desk#English','https://www.etymonline.com/word/desk'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yf',ROOTS,WORDS)
 extend_lessons()
