"""Field: physical land, activity areas, sports and redevelopment."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
FI=[['古英语 feld → 中古英语 feld、feeld','开阔地、田野'],['英语 field','田地、场地 → 专门活动范围、领域、场等']]
W('field','/fiːld/','田野；场地；领域；场；字段；处理、接应',
 '先是一块展开的地面，再把活动、知识或作用展开的范围也叫 field。',
 '接古英语 feld，是本族继承词。领域、物理场、表单字段和体育动词等是不同专门发展，不是凡有 field 都能只译田地。',FI,
 'a field of wheat 麦田，a football field 足球场，a field of study 学习领域；a magnetic field 磁场，a form field 表单字段。field questions 作动词是接住、应对问题。',
 'in the field；a field of study；field questions；a text field。',
 'field 与 farm 农场不同，一座 farm 可有几块 fields；field questions 不是去田里问问题。',
 ('Her main field of research is language learning.','她主要研究语言学习领域。'),('He fielded questions from the audience.','他应对了观众提出的问题。'))
W('afield','/əˈfiːld/','在远处；离开原处、原题地',
 '从原来那块熟悉范围往外走，距离更远；讨论也可能越走越偏离主题。',
 '古英语 on felde 在田野中，经中古英语 afeld 等延续，现代可认作 a- 在 + field。如今常配 far、further、farther，保留向外扩展的感觉。',FI[:1]+[['on felde → afield','在野外 → 远离原处、原来范围']],
 'further afield 更远处，visitors from far afield 从远方来的游客；go too far afield 也可说离题太远。',
 'further afield；far afield；look afield；go too far afield。',
 'afield 是副词，a field 两词是一个田地或场地；We searched further afield 不是又搜了一块田。',
 ('We had to look further afield for a suitable venue.','我们只好到更远的地方寻找合适场地。'),('The festival attracted visitors from far afield.','节庆吸引了远道而来的游客。'))
W('cornfield','英 /ˈkɔːnfiːld/；美 /ˈkɔːrnfiːld/','玉米田；谷物田〔依地区〕',
 '种着 corn 的那块田；先确认当地 corn 指玉米还是谷物，别只凭中文习惯。',
 'corn 谷物、玉米 + field 田。美国英语 corn 通常是玉米，英国等历史用法还能泛指当地主要谷物。',C('corn 谷物、常指玉米','field 田','cornfield','种 corn 的田地'),
 'a vast cornfield 一大片玉米田或谷物田；现代国际农业、美国场景常是玉米，英国历史文本需看作物。',
 'a vast cornfield；walk past a cornfield；rows in a cornfield。',
 'cornfield 不必每个年代、地区都译玉米田；wheat field 明确是麦田，corn 的地区差异才是关键。',
 ('The American farm had a cornfield beside the house.','这座美国农场的房子旁有一片玉米田。'),('A narrow path ran through the cornfield.','一条窄路穿过谷物田。'))
W('hayfield','/ˈheɪfiːld/','割草晒干草的草地',
 '这块草地的用途，是把草割下来做干草饲料，而不只是让它一直长着好看。',
 'hay 干草 + field 田地，按收获用途命名。草在地里生长时还没晒干，也仍可叫 hayfield。',C('hay 干草','field 田地','hayfield','供收割草制作干草的地'),
 'mow a hayfield 收割干草地的草；a hayfield in summer 夏季割草地。',
 'a hayfield；mow a hayfield；across the hayfield。',
 'hayfield 侧重供干草收获，pasture 牧场草地侧重让牲畜吃草；同一地块在不同管理下用途可能变化。',
 ('The farmer was mowing the hayfield.','农夫正在割干草地上的草。'),('Swallows flew low over the hayfield.','燕子低低掠过干草地。'))
W('coalfield','英 /ˈkəʊlfiːld/；美 /ˈkoʊlfiːld/','煤田；产煤区',
 '这一区域地下分布着煤层，可能有多座煤矿；不是把挖出的煤摊在一块地上。',
 'coal 煤 + field 区域，field 从田地扩展为某种资源分布区。',C('coal 煤','field 资源分布区','coalfield','具有煤层、煤资源的区域'),
 'a coalfield region 煤田地区，a former coalfield 旧产煤区；地质资源存在不保证当前仍开采。',
 'a coalfield；a coalfield community；the history of the coalfield。',
 'coalfield 资源分布区，coal mine 具体煤矿；一个 coalfield 可以包含多处 mines。',
 ('The town developed beside a major coalfield.','这座城镇在一片大煤田附近发展起来。'),('The museum tells the story of the local coalfield.','博物馆讲述当地煤田的历史。'))
W('goldfield','英 /ˈɡəʊldfiːld/；美 /ˈɡoʊldfiːld/','金矿区；产金地区',
 '人们在这个地区找到金、开采金；不必是田地表面金灿灿。',
 'gold 金 + field 资源分布区域。常见复数 goldfields 指较广的产金区，单个矿坑则是更具体设施。',C('gold 黄金','field 资源分布区','goldfield','发现或开采黄金的地区'),
 'the Australian goldfields 澳大利亚金矿区，a historic goldfield 历史金矿区；命名可能保留历史，不能凭词名断言现在仍产金。',
 'a historic goldfield；the goldfields；a goldfield settlement。',
 'goldfield 矿区，gold mine 金矿；golden field 金色田野只是颜色描述，未必有金矿。',
 ('Families travelled to the goldfields in search of work.','许多家庭前往金矿区找工作。'),('The old goldfield is now a heritage site.','这片旧金矿区如今是一处遗产地。'))
W('battlefield','/ˈbætəlfiːld/','战场；激烈冲突的领域',
 '战斗实际发生的场所；争论和竞争激烈时，也把讨论空间比成战场。',
 'battle 战斗 + field 场地，形成战场名称，再引申为冲突激烈的范围。不是所有田野都曾发生战争。',C('battle 战斗','field 场地','battlefield','战斗发生地 → 激烈冲突领域'),
 'a historic battlefield 历史战场，a political battlefield 政治争夺的领域；后者不必真实发生军事战斗。',
 'on the battlefield；a historic battlefield；a political battlefield。',
 'battlefield 战斗发生地，battlefront 战事前沿；历史战场即便今天安静，也仍可叫 battlefield。',
 ('The battlefield is now covered with grass.','昔日战场如今长满了草。'),('Education became a political battlefield in the novel.','小说中，教育成了政治争夺的战场。'))
W('minefield','/ˈmaɪnfiːld/','雷区；问题重重、容易触雷的领域',
 '走错一步可能碰到危险；复杂话题里一句说错就引发问题，也借雷区来比。',
 'mine 地雷 + field 布设区域；这里 mine 不是我的，也不是 coal mine 的采矿设施义。比喻义保留处处潜藏麻烦的感觉。',C('mine 地雷','field 区域','minefield','地雷布设区 → 潜在问题重重的领域'),
 'a legal minefield 法律问题复杂棘手的领域，a social minefield 人际、礼仪上容易出问题的情境；这是词义比喻，不是在给法律结论。',
 'a minefield of problems；a legal minefield；navigate a minefield。',
 'minefield 雷区或复杂风险领域，mining field 采矿领域；不能看到 mine 都译成矿区。',
 ('The history book includes a map of former minefields.','历史书中有一幅昔日雷区的地图。'),('The seating plan became a minefield of family tensions.','座位安排成了家人关系矛盾重重的一块雷区。'))
W('fielder','英 /ˈfiːldə/；美 /ˈfiːldər/','棒球、板球等的守场员',
 '球打出去后，在场上接球、拦球、回传的人，不是只要站在草地上的人都叫 fielder。',
 '现代体育义由 field 守场、处理来球 + -er 人形成。更早还有田野居住者等相应形式，不能把现代守场员一律译成农民。',FI+[['field 的体育动词义 + -er → fielder','守场、处理球 → 守场员']],
 'an outfielder 外野守场员，an infielder 内野守场员；fielder 在不同击球运动里担任相应守备工作。',
 'a good fielder；a close fielder；the fielders on the team。',
 'fielder 守场员，batter 击球员；不是一切运动的后卫都统称 fielder。',
 ('The fielder caught the ball near the boundary.','守场员在边界附近接住了球。'),('She is one of the team’s best fielders.','她是队里最好的守场员之一。'))
W('infield','/ˈɪnfiːld/','内场；棒球内野；某些场地中心区域',
 '把整个场地分里外，靠内的一块叫 infield；具体内到哪里由运动、场地的定义决定。',
 'in 内部 + field 场地，形成内部区域名称。棒球里有固定内野范围，赛道等还会用它指环形场地内侧。',C('in 内部','field 场地','infield','某场地的内部区域，尤其棒球内野'),
 'the baseball infield 棒球内野，the track infield 跑道内场；作为集合也可能说内野守备阵容。',
 'the baseball infield；the track infield；an infield hit。',
 'infield 与 outfield 是相对位置词，边界随项目；不能把足球中场无条件叫棒球式 infield。',
 ('The ball rolled across the infield.','球滚过内野。'),('Athletes gathered on the track’s infield.','运动员在跑道内场集合。'))
W('outfield','/ˈaʊtfiːld/','外场；棒球、板球等的外野',
 '比内场更靠外围、离击球中心较远的场区；在那里守备的人也可被合称为 outfield。',
 'out 外部 + field 场地，形成体育外场等名称。不是所有不在球场里的地方，而是场地内部划出的外区。',C('out 外部','field 场地','outfield','球场较外围的区域；相关守备阵容'),
 'a ball into the outfield 打向外野的球；an outfield player 在足球等语境通常指非门将球员，不能硬套成棒球外野手。',
 'in the outfield；a ball to the outfield；an outfield player。',
 'outfield 外场仍在比赛场地内，不是 out of bounds 出界；足球 outfield player 另有排除门将的固定用法。',
 ('The ball landed deep in the outfield.','球落在外野深处。'),('Three players were positioned across the outfield.','三名球员分布在外野守备。'))
W('midfield','/ˈmɪdfiːld/','中场；中场球员群体',
 '球场中间这片区域，连接后场防守与前场进攻；也可用来说在这里承担职责的球员。',
 'mid- 中间 + field 场地，形成球场中部及相应位置名称。具体职责与范围随运动项目和战术。',C('mid- 中间','field 场地','midfield','场地中部及相应球员位置'),
 'control midfield 控制中场，play in midfield 踢中场；a midfield role 中场角色。并非只能站在中心点不动。',
 'control midfield；play in midfield；a midfield player。',
 'midfield 中场，infield 内场；两者不是中文里都在里面就能互换，尤其项目不同。',
 ('The team struggled to control midfield.','球队很难控制住中场。'),('She moved from defence into midfield.','她从防守位置改踢中场。'))
W('backfield','/ˈbækfiːld/','后场；美式橄榄球等的后场球员',
 '相对队伍阵线或规定位置更靠后的场区，也可以合称站在那里的一组球员。',
 'back 后面 + field 场区，形成体育后场及后场阵容名称；美式橄榄球中常见，不能从 back 一字推出全部是防守队员。',C('back 后面','field 场区','backfield','按项目定义的后场及相关球员'),
 'the offensive backfield 进攻后场阵容，a strong backfield 强劲的后场配置；具体哪些位置被包含，要看项目、队形。',
 'the offensive backfield；the defensive backfield；a backfield player。',
 'backfield 是相对位置，不自动等于 defence 防守；进攻方也有 backfield。',
 ('The coach praised the speed of the offensive backfield.','教练称赞了进攻后场球员的速度。'),('The article compares the two teams’ backfields.','文章比较了两队的后场阵容。'))
W('greenfield','/ˈɡriːnfiːld/','未开发土地上的；从头新建的',
 '原来没有那套建筑或系统，现在从一个比较空白的基础开始做。',
 'green 绿色、未建用土地的联想 + field 地块，形成开发选址术语；软件、投资等再借指新建项目。不能把所有绿色田野都等同一个政策类别。',C('green 绿色、未建用土地的联想','field 地块','greenfield','未开发地块 → 从头新建项目的'),
 'a greenfield site 待首次开发的地块，a greenfield software project 新建软件项目；技术上通常强调较少旧系统包袱，不保证没有任何外部约束。',
 'a greenfield site；greenfield development；a greenfield project。',
 'greenfield 从较空白基础新建，brownfield 常从已有开发、设施基础改造；不同国家对土地类别的细节规定不同。',
 ('The factory was built on a greenfield site.','工厂建在一块此前未开发的地块上。'),('The team preferred a greenfield project to modifying the old system.','团队更想从头新建项目，而不是修改旧系统。'))
W('brownfield','/ˈbraʊnfiːld/','已开发土地；旧工业等地块的再开发；沿用既有系统改造的',
 '这地方或系统已经用过，再动手时要面对留下来的设施、限制，有时还包括污染等历史问题。',
 'brown 褐色 + field 地块，与 greenfield 形成开发语汇对照。它是固定类别名，不是看地面实际是不是棕色；软件等再借用已有系统上改造的意义。',C('brown 褐色的命名对照','field 地块','brownfield','已有开发地块 → 既有设施、系统基础上的改造'),
 'brownfield redevelopment 旧开发地块再开发；美国环境政策语境尤其关注实际或潜在污染造成的再利用困难，其他地区类别范围可能不同。技术里 a brownfield project 则面临既有系统。',
 'a brownfield site；brownfield redevelopment；a brownfield project。',
 'brownfield 不在所有国家都等于已确认污染地；也不是 greenfield 的颜色反义词就足够解释。',
 ('The city plans to turn the brownfield site into a park.','城市计划把这块旧开发地改成公园。'),('A brownfield software project must work with existing systems.','在既有基础上改造的软件项目，必须与现有系统配合。'))
R('B3122','田野、场区、领域；资源区与再开发','FIELD：一块展开的区域，按活动和作用细分','麦田是一块土地，研究领域是一块知识范围；球场、矿区、物理场等已经各有固定定义。',
 'field 继承古英语 feld。先读基础及 afield 向外，再把作物、矿产、战事、运动区分组；greenfield、brownfield 在开发语境里不能只按颜色判断。',
 'field → afield、fielder；cornfield、hayfield 按用途，coalfield、goldfield 按资源；infield、outfield、midfield、backfield 按项目位置。',
 [['基础与专门范围','field · afield · subfield · fieldwork · airfield'],['作物和资源区域','cornfield · hayfield · coalfield · goldfield'],['战场及危险比喻','battlefield · minefield'],['守场与分区','fielder · infield · outfield · midfield · backfield'],['新建与既有基础改造','greenfield · brownfield']],
 'infield 不等于 midfield；outfield 仍可能在场内；minefield 的 mine 是地雷；brownfield 不必各地都等于已确认污染地。',
 'The team’s fieldwork focused on a brownfield site near the old coalfield.\n\n团队的实地工作，聚焦旧煤田附近一块已开发地。',
 'field afield subfield fieldwork airfield cornfield hayfield coalfield goldfield battlefield minefield fielder infield outfield midfield backfield greenfield brownfield')
for item in WORDS:
    if item['word']=='brownfield':item['sources'].append('https://www.epa.gov/brownfields/environmental-contamination-brownfield-sites')
    if item['word']=='greenfield':item['sources'].append('https://www.oxfordlearnersdictionaries.com/definition/english/greenfield')
    if item['word']=='field':item['sources'].append('https://www.etymonline.com/word/field')
if __name__=='__main__':save('continuation_20261029_ct',ROOTS,WORDS)
