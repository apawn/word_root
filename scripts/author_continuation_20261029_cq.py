"""Front and list: coherent subfamilies and false-friend etymology."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
FR=[['拉丁 frōns、front- → 法语 front → 英语 front','额头、正面 → 前部、面对的一面'],['现代 front 词族','最前方、直接面对处；复合词依位置或功能固定']]
W('forefront','英 /ˈfɔːfrʌnt/；美 /ˈfɔːrfrʌnt/','最前沿；突出、领先的位置',
 '不只在前面，而是在一群人、一项技术或大家注意力最靠前的地方。',
 'fore- 在前 + front 前部，中古英语已有对应形式。两个前并不互相抵消，而是强化最前端、最突出位置。',FR+[['fore- + front → forefront','前部 → 最前沿、最突出的位置']],
 'at the forefront of research 在研究前沿，bring an issue to the forefront 让问题受到突出关注；也可指思想中优先考虑的事。',
 'at the forefront of；bring to the forefront；remain at the forefront。',
 'forefront 偏领先、显著位置，frontline 偏直接接触、执行的一线；一线工作者未必是在研究最前沿。',
 ('The team is at the forefront of materials research.','团队处于材料研究前沿。'),('The debate brought transport safety to the forefront.','辩论让交通安全成为突出关注的问题。'))
W('frontline','/ˈfrʌntlaɪn/','前线的；直接服务、执行的一线',
 '离问题、客户或现场最近，直接接触和处理事情的那一层。',
 'front 前方 + line 线、战线，军事最前线的画面扩展到医疗、服务、组织执行等场景；也常分写 front line。',C('front 前方','line 线、战线','frontline','直接面对战事、问题、服务对象的一线'),
 'frontline staff 一线员工，frontline services 一线服务；不是只有军人才能用。',
 'frontline staff；frontline workers；frontline services。',
 'frontline 一线，forefront 最前沿、突出位置；frontline worker 不能一律译成领军研究者。',
 ('Frontline staff answered questions from passengers.','一线员工回答旅客的问题。'),('The report focuses on frontline health services.','报告重点讨论一线医疗卫生服务。'))
W('storefront','英 /ˈstɔːfrʌnt/；美 /ˈstɔːrfrʌnt/','店面；商铺临街正面；网上店铺界面',
 '顾客走过时先看见的门窗和展示面；网上也有迎接顾客浏览、下单的店面。',
 'store 商店 + front 正面，先指商铺临街外观、店面，数字商业再借指网上面向顾客的店铺。',C('store 商店','front 正面','storefront','商店对外展示的一面 → 网上店面'),
 'a glass storefront 玻璃店面，an online storefront 网上店铺页面；某些语境也可指临街商铺空间。',
 'an empty storefront；a glass storefront；an online storefront。',
 'storefront 面向顾客的一面，不是 storeroom 仓库；线上 storefront 也不是网站所有后台功能的统称。',
 ('The bakery has a bright blue storefront.','面包店有一个亮蓝色的店面。'),('The artist opened an online storefront for her prints.','艺术家为版画开了一家网店。'))
W('battlefront','/ˈbætəlfrʌnt/','战线；战事前沿',
 '双方实际对峙、作战的那一片前沿，而不是整个国家所有与战争有关的地方。',
 'battle 战斗 + front 战线、前沿，构成军事地带名称，也可比喻正在激烈争取的领域。',C('battle 战斗','front 战线、前沿','battlefront','实际战斗的前沿地带'),
 'news from the battlefront 前线消息，conditions at the battlefront 战地前沿情况；历史或小说中常见。',
 'at the battlefront；from the battlefront；a distant battlefront。',
 'battlefront 前线地带，battlefield 发生战斗的战场，两者常有交叠；frontline 还广用于非军事一线工作。',
 ('The diary records life near the battlefront.','日记记录了战线附近的生活。'),('News from the battlefront reached the village slowly.','前线消息很慢才传到村里。'))
W('beachfront','/ˈbiːtʃfrʌnt/','海滩边地带；临沙滩的',
 '建筑或地点直接面对、紧邻沙滩，出门就是沙滩这一侧。',
 'beach 海滩 + front 面向的一侧，形成临滩区域、位置修饰语。名字本身不保证有私人沙滩或可直接下水。',C('beach 海滩','front 面向的一侧','beachfront','临海滩的位置、区域'),
 'a beachfront hotel 海滩边酒店，walk along the beachfront 沿海滩一带散步；可名词也可修饰名词。',
 'a beachfront hotel；beachfront property；along the beachfront。',
 'beachfront 特别说海滩边，oceanfront 特别说面海，waterfront 更宽，河边、港边也可算。',
 ('We stayed in a small beachfront hotel.','我们住在一家海滩边的小酒店。'),('Cafés line the beachfront.','海滩边一带排列着咖啡馆。'))
W('seafront','/ˈsiːfrʌnt/','海滨一带；临海的街道、区域',
 '城镇面海的那一条边，常让人想到海滨步道、街道和沿线建筑。',
 'sea 海 + front 面向的一侧，形成临海地带名词。英式旅游、城镇描述里常见，不要求一定有沙滩。',C('sea 海','front 面向的一侧','seafront','城镇临海的地带'),
 'walk along the seafront 沿海滨散步，a seafront café 海滨咖啡馆；与 beachfront 重合时看是否强调沙滩。',
 'along the seafront；a seafront café；the seafront promenade。',
 'seafront 海滨，seaboard 常说较大范围的沿海地区；一个小镇的海边步道常用 seafront。',
 ('We walked along the seafront after dinner.','晚饭后我们沿海滨散步。'),('The café overlooks the seafront.','咖啡馆俯瞰海滨一带。'))
W('oceanfront','英 /ˈəʊʃənfrʌnt/；美 /ˈoʊʃənfrʌnt/','临海的；面向大海的地带',
 '房子或地块朝着大海展开，重点是面海位置，不是强调一定铺着沙子。',
 'ocean 海洋 + front 面向的一侧，作名词或名词前修饰语，北美地产、旅游描述中常见。',C('ocean 海洋','front 面向的一侧','oceanfront','临大海的位置或地带'),
 'an oceanfront room 临海客房，an oceanfront property 临海物业；广告中的实际距离、视野仍要看说明，不能只由词名保证。',
 'an oceanfront hotel；an oceanfront room；oceanfront property。',
 'oceanfront 强调直接临海，ocean view 只说明能看海，未必就在海边；beachfront 另强调临海滩。',
 ('They rented an oceanfront apartment for the summer.','他们为夏天租了一套临海公寓。'),('The hotel has an oceanfront terrace.','酒店有一个临海露台。'))
W('riverfront','英 /ˈrɪvəfrʌnt/；美 /ˈrɪvərfrʌnt/','滨河地带；临河的',
 '城市或建筑面对河流的一面，沿河展开成一条可活动的区域。',
 'river 河 + front 面向的一侧，形成河滨区域和临河位置的名称。不是 river 的源头。',C('river 河','front 面向的一侧','riverfront','滨河区域、临河位置'),
 'the riverfront park 滨河公园，redevelop the riverfront 重新开发滨河地区。可以包含道路、广场、建筑等。',
 'a riverfront park；a riverfront development；along the riverfront。',
 'riverfront 常指沿河开发、活动地带，riverbank 更直接说河岸；二者范围有交叠但侧重点不同。',
 ('The city built a park along the riverfront.','城市沿滨河地带建了一座公园。'),('We found a table at a riverfront café.','我们在临河咖啡馆找到了一张桌子。'))
W('lakefront','/ˈleɪkfrʌnt/','滨湖地带；临湖的',
 '把 riverfront 的河换成湖，就是沿着湖边的一面和地带。',
 'lake 湖 + front 面向的一侧，形成滨湖、临湖的位置表达。不是湖泊向前移动的边缘。',C('lake 湖','front 面向的一侧','lakefront','滨湖区域、临湖位置'),
 'a lakefront cabin 湖边小屋，a lakefront path 滨湖小径；名词也可说 the lakefront 湖滨一带。',
 'a lakefront park；a lakefront cabin；along the lakefront。',
 'lakefront 湖滨，riverfront 滨河，seafront 海滨；共同的 front 是面向某水域的一侧。',
 ('The trail follows the lakefront for several kilometres.','小径沿湖滨延伸了几公里。'),('They stayed in a lakefront cabin.','他们住在一间湖边小屋里。'))
W('wavefront','/ˈweɪvfrʌnt/','波前；波面',
 '把波传播的同一个节拍位置连成一面，就能表示波此刻推进到的形状；它不是整片海浪的最前排。',
 'wave 波 + front 前沿、面，在物理里形成同一相位点构成的面的术语。水波、声波、光波等都有相关描述。',C('wave 波','front 前沿、面','wavefront','波中同一相位点形成的面'),
 'a plane wavefront 平面波前，a spherical wavefront 球面波前；在二维示意里常画成线，真实术语可指面。',
 'a plane wavefront；a spherical wavefront；wavefront distortion。',
 'wavefront 是同相位的面，wavelength 波长是沿传播方向相邻同相位位置之间的距离，二者不是同一量。',
 ('The diagram shows circular wavefronts spreading from a point.','图示显示从一点向外传播的圆形波前。'),('The lens changes the shape of the wavefront.','透镜改变了波前的形状。'))
R('B3407','前部、正面、前沿；面向水域的一侧','FRONT：面对外界或推进方向的那一面','先分最前沿 forefront、执行一线 frontline、店面 storefront，再按水域归拢地理位置词。',
 'front 经法语接拉丁额头、正面词族。现代复合词不都指同一种实体：有些是位置，有些是功能，有些像 wavefront 已成为物理术语。',
 'front → forefront、frontline、storefront；beach、sea、ocean、river、lake + front 看临水位置；wavefront 另学物理含义。',
 [['前沿和正面','front · forefront · frontline · battlefront · storefront · frontal · frontage · frontcourt'],['海滩及海滨','waterfront · beachfront · seafront · oceanfront'],['河湖地带','riverfront · lakefront'],['物理术语','wavefront']],
 'forefront 领先位置，frontline 直接一线；oceanfront 临海与 ocean view 可看海不同；wavefront 不等于 wavelength。',
 'The riverfront project brought the town’s old storefronts to the forefront of local discussion.\n\n滨河项目让镇上的旧店面成为当地讨论的焦点。',
 'front forefront frontline battlefront storefront frontal frontage frontcourt waterfront beachfront seafront oceanfront riverfront lakefront wavefront')
LI=[['古英语 līste、法语 liste 等历史形式','条带、边条；与条状记录相关'],['英语 list 的清单分支','逐项排列的目录、清单；其他同形旧词另分来源']]
W('list','/lɪst/','清单；目录；列出；另有船体倾斜义',
 '把一项项内容排开，让人可以顺着看、逐个查；船侧倾的 list 是另一个固定同形用法。',
 '清单分支联系古英语、法语等条带、边条形式，后来有条状记录、目录等义。船体倾斜义的来源不确定；旧日表示欲望、倾向及听的 list 也不能混成现代清单一支。',LI,
 'make a list 列清单，list the names 把名字列出来；a ship with a list 船体侧倾。listed building 在英式语境是列入保护名录的建筑，而非随便列过名字的房子。',
 'make a list；a shopping list；list the reasons；on the list。',
 'list 名单，enlist 加入或争取支持；listless 没精神却不是清单没写好，来自旧的欲望、兴致分支。',
 ('Make a list of everything we need.','把我们需要的所有东西列一张清单。'),('The report lists three possible causes.','报告列出了三个可能原因。'))
W('enlist','/ɪnˈlɪst/','参军；招募；争取、获得协助',
 '把人拉到某支队伍、某项工作里来；自己进入队伍，也能说 enlist。',
 'en- 使进入 + list 名册，背后是把人记入名册的画面。军事招募和日常争取帮助是不同固定用法。',LI+[['en- + list → enlist','进入名册 → 入伍、招募、争取支持']],
 'enlist in the army 参军，enlist volunteers 招募志愿者，enlist someone’s help 请到某人帮忙。',
 'enlist in；enlist volunteers；enlist support；enlist someone’s help。',
 'enlist 常指入伍或把协助争取过来，list 只是列出、登记；list a name 不必等于那人已经同意参加。',
 ('She enlisted the help of two experienced volunteers.','她请到了两位有经验的志愿者帮忙。'),('The biography describes why he enlisted in the army.','传记描述了他为何参军。'))
W('wishlist','/ˈwɪʃlɪst/','愿望清单；想要物品的收藏列表',
 '现在还没买、还没实现，先把想要的东西或目标存成一张表。',
 'wish 愿望 + list 清单，也常写 wish list。电商界面里是保存想要商品的固定功能名，不等于已经下单。',C('wish 愿望','list 清单','wishlist','想要物品、目标的清单'),
 'add to your wishlist 加入心愿单，a birthday wishlist 生日愿望清单；项目管理里也能说未来想增加的功能清单。',
 'add to a wishlist；a birthday wishlist；a feature wishlist。',
 'wishlist 想要的，shopping cart 购物车通常准备结算；两者都不自动表示交易已经完成。',
 ('I added the book to my wishlist.','我把那本书加入了心愿单。'),('The team shared a wishlist of future features.','团队分享了一份未来希望增加的功能清单。'))
W('tracklist','/ˈtræklɪst/','专辑等的曲目表',
 '一张专辑里有哪些歌、按什么顺序放，把这些条目列出来就是曲目表。',
 'track 音轨、录制曲目 + list 清单，也常分写 track list。track 在这里不是跑道、跟踪，而是录音曲目的固定义。',C('track 录制曲目','list 清单','tracklist','专辑或录音作品的曲目表'),
 'the album’s tracklist 专辑曲目表，reveal the tracklist 公布曲目表；可以包括不带歌词的音乐或其他音轨。',
 'an album tracklist；reveal the tracklist；the full tracklist。',
 'tracklist 通常列某张专辑等的内容，playlist 是组织起来的播放列表；setlist 常指现场演出的曲目安排。',
 ('The band revealed the new album’s tracklist.','乐队公布了新专辑的曲目表。'),('The booklet includes the full tracklist.','小册子包含完整曲目表。'))
W('listless','/ˈlɪstləs/','没精打采的；无兴致的',
 '不是忙得没有清单，而是连想做点什么的劲头都提不起来。',
 '旧 list、liste 欲望、兴致 + -less 没有；联系古英语 lystan 等欲望、喜欢词族，与清单 list 的来路分开。现代不必先认识这个已少用的旧词，也能学会 listless。',
 [['古英语 lystan；中古英语 liste 等','欲望、喜好、兴致的旧词族'],['liste + -less → listless','缺少兴致 → 没精打采的']],
 'feel listless 感到无精打采，a listless afternoon 没精神的一下午；可因疲累、无聊等不同情境使用，不是一个词就能确定原因。',
 'feel listless；look listless；a listless mood。',
 'listless 没精神，careless 粗心，listless 不是不列计划。一个人日程排满，也可能感到 listless。',
 ('The long wait left everyone feeling listless.','漫长等待让大家都没了精神。'),('He gave a listless wave and sat down.','他无精打采地挥了挥手，坐了下来。'),sources=['https://en.wiktionary.org/wiki/listless#English','https://www.etymonline.com/word/listless'])
R('B3067','清单、列出；另一来源的无兴致','LIST：逐项列开；listless 别误认成无清单','购物清单、播放列表、曲目表都按内容用途分；listless 则另看旧词欲望、兴致。',
 '清单 list 接条带、边条的历史形式。enlist 联系进入名册；wishlist、tracklist 是透明复合词。不要用同形 list 给 listless 编出没计划所以懒散的假故事。',
 'list → enlist；按用途 wishlist、checklist、playlist、tracklist、setlist 等；listless 作为另源辨析单列。',
 [['基础、名册与核查','list · enlist · checklist'],['愿望和不同曲目','wishlist · playlist · tracklist · setlist · booklist'],['等待、观察及筛选名单','waitlist · watchlist · longlist · blacklist · whitelist'],['另源辨析','listless']],
 'tracklist 专辑曲目，playlist 播放列表，setlist 演出曲目；listless 不是清单为空。',
 'She checked the tracklist and added the album to her wishlist.\n\n她看过曲目表，把这张专辑加入心愿单。',
 'list enlist checklist wishlist playlist tracklist setlist booklist waitlist watchlist longlist blacklist whitelist listless')
for item in WORDS:
    if item['word']=='wavefront':item['sources'].append('https://www.siyavula.com/read/za/physical-sciences/grade-11/2d-and-3d-wavefronts/06-2d-and-3d-wavefronts-02')
if __name__=='__main__':save('continuation_20261029_cq',ROOTS,WORDS)
