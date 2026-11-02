"""Hole: useful openings, terrain pits, metaphors and common register contrasts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
HO=[['古英语 hol → 中古英语 hol、hole → hole','孔、洞、空腔；与 hollow 相关'],['现代 hole','洞、坑；缺口、漏洞、困境等比喻']]
def H(f,m):return HO+[[f,m]]
W('hole','英 /həʊl/；美 /hoʊl/','洞、孔；坑；缺口、漏洞；困境',
 '本来该实在的地方空了一块；可以穿透一件东西，也可以只是地面凹下去。',
 '继承古英语 hol，与 hollow 空的相关。抽象里的证据缺口、预算缺口、陷入困境等，借缺一块或陷进去的形象。',HO,
 'a hole in the wall 墙洞，a hole in the ground 地坑，a hole in the argument 论证漏洞，in a hole 陷入困境。',
 'a hole in；dig a hole；a hole in the argument；in a hole。',
 'hole 空洞，whole 完整的在许多口音同音；一个说缺了一块，一个说整体。洞不必都穿透，也可凹坑。',
 ('There is a small hole in my sock.','我的袜子上有个小洞。'),('The report reveals a hole in the original argument.','报告揭示了原先论证中的一个漏洞。'))
W('holey','英 /ˈhəʊli/；美 /ˈhoʊli/','有洞、多孔的',
 '衣服破几个洞，奶酪有许多孔，都能按有洞这个特点描述。',
 'hole + -y，现代保留 e，有助与 holy 神圣的区分；中古英语已有同族形容词。不是 hole 变成神圣。',H('hole + -y → holey','有洞的；拼写 e 区分 holy'),
 'holey socks 破洞袜，holey cheese 多孔奶酪。口语也会形容到处漏洞的说法。',
 'holey socks；holey cheese；a holey old sweater。',
 'holey 有洞，holy 神圣，wholly 完全；三词常同音，意义与来源不同。',
 ('He wore an old, holey sweater.','他穿着一件破洞旧毛衣。'),('The cheese was pale and holey.','奶酪颜色浅，里面有许多孔。'))
W('loophole','英 /ˈluːphəʊl/；美 /ˈluːphoʊl/','规则漏洞；可钻的空子；墙上狭小开口〔历史义〕',
 '看似封住的规则还留一条小缝，人能从那里绕过去；这和旧时墙上开口的形象相连。',
 '中古英语 loupe 墙上开口 + hole。前部是旧开口词，不是现代绳圈 loop 的形状加洞；后来的规则空子是比喻。',H('中古英语 loupe〔墙上开口〕+ hole → loophole','狭小开口 → 规则留出的可绕行空隙'),
 'find a loophole 找到漏洞，close a loophole 堵上漏洞，a loophole in the rules 规则空子。',
 'a loophole in；find a loophole；close a loophole。',
 'loophole 常说规则允许绕行的空隙，不等于任意错误 bug；具体利用行为的法律性质不能只由这个词判定。',
 ('The company changed the policy to close a loophole.','公司修改政策，堵上了一个漏洞。'),('They found a loophole in the competition rules.','他们发现竞赛规则里有个可钻的空子。'))
W('pigeonhole','英 /ˈpɪdʒɪnhəʊl/；美 /ˈpɪdʒɪnhoʊl/','鸽巢小格；信件分类格；把……简单归类、贴标签',
 '先把不同东西塞进一个个小格，再把复杂的人硬塞进简单类别；动词常有归类过死的意味。',
 'pigeon 鸽子 + hole，小格、鸽巢位置的名词后来用于分类储物格，再由名词形成动词归类。',H('pigeon + hole → pigeonhole〔名词 → 动词〕','鸽巢格、分类格 → 按格子归类、贴标签'),
 'put a letter in a pigeonhole 把信放分类格，pigeonhole an actor 把演员定型。',
 'a pigeonhole for letters；pigeonhole an actor；avoid pigeonholing。',
 'classify 可中性分类，pigeonhole 常嫌把复杂对象过早、过死地定型；同一个人可能不止一个角色。',
 ('She left the message in his pigeonhole.','她把便条放在他的信件格里。'),('The actor did not want to be pigeonholed as a villain.','演员不想被定型为只演反派。'))
W('wormhole','英 /ˈwɜːmhəʊl/；美 /ˈwɜːrmhoʊl/','虫蛀孔；虫洞〔物理学假设结构〕',
 '木头里虫子钻出的通道很直观；物理里的名字也借通道形象，但那是理论概念。',
 'worm 虫 + hole，先有虫蛀洞用法。20世纪物理借来命名可能连接不同时空区域的理论结构，不是发现了太空里的巨虫。',H('worm + hole → wormhole','虫蛀通道；后借为物理学理论结构名称'),
 'wormholes in old wood 旧木材虫孔，a hypothetical wormhole 假设虫洞。',
 'wormholes in wood；a hypothetical wormhole；a wormhole in fiction。',
 'wormhole 科幻里可作捷径，现实物理仍需区分理论、证据和故事设定；black hole 黑洞是另一概念，不是少一个 worm。',
 ('The old beam was full of wormholes.','旧横梁上满是虫蛀孔。'),('The science fiction novel sends the crew through a wormhole.','科幻小说让船员穿过一条虫洞。'))
W('sinkhole','英 /ˈsɪŋkhəʊl/；美 /ˈsɪŋkhoʊl/','地面塌陷坑；落水洞等凹陷',
 '地下支撑或地层过程出了变化，地面陷下成一个坑；重点是下陷的空缺。',
 'sink 下陷 + hole，有中古英语相关组合。现代常用于自然或地层、地下结构问题造成的地面凹陷，不能直接按厨房水槽的孔理解。',H('sink + hole → sinkhole','下陷形成的坑洞、地貌凹陷'),
 'a sinkhole in the road 路上的塌陷坑，a large sinkhole 大塌陷坑。',
 'a large sinkhole；a sinkhole in the road；a sinkhole opened up。',
 'sinkhole 常接地面下陷，pothole 常是道路磨损坑；仅凭照片外形不能确定地质形成机制。',
 ('A sinkhole opened up near the old building.','旧建筑附近出现了一处地面塌陷坑。'),('The road was closed after a large sinkhole appeared.','大塌陷坑出现后，道路被封闭。'))
W('pothole','英 /ˈpɒthəʊl/；美 /ˈpɑːthoʊl/','路面坑洞；岩石坑、竖穴〔特定用法〕',
 '路面凹下一块，车轮一过就颠一下；日常最常见就是这种坑。',
 'pot 的方言坑、空穴义 + hole，另一些坑穴用法也与 pot 容器形状相联系。不是有人把做饭锅掉地上才形成。',H('pot〔坑、空穴等旧义〕+ hole → pothole','坑穴；现代常见道路坑洞'),
 'hit a pothole 车轮撞上路坑，fill potholes 填补路坑，a road full of potholes 满是坑的路。',
 'hit a pothole；fill potholes；a road full of potholes。',
 'pothole 道路坑与 sinkhole 塌陷坑常见形成背景不同；pothole 不自动表示深到形成洞穴。',
 ('The bus jolted as it hit a pothole.','公交车轧到路坑，猛地颠了一下。'),('Workers filled the potholes before winter.','工人在冬天前填好了路坑。'))
W('borehole','英 /ˈbɔːhəʊl/；美 /ˈbɔːrhoʊl/','钻孔；钻井孔',
 '用钻具向地下或材料里钻出来的长孔，常为了取样、测量或取水。',
 'bore 钻、钻孔 + hole。bore 这里不是无聊、让人厌烦的意思。',H('bore〔钻孔〕+ hole → borehole','钻具钻出的孔洞'),
 'drill a borehole 钻孔，a borehole sample 钻孔样本，a water borehole 取水钻井孔。',
 'drill a borehole；a borehole sample；a deep borehole。',
 'borehole 按人工钻出的过程命名，sinkhole 按下陷命名；两者不能因都在地下就当同一种洞。',
 ('The team drilled a borehole to collect rock samples.','团队钻孔采集岩石样本。'),('The borehole provides water for the village.','钻井孔为村庄供水。'))
W('pinhole','英 /ˈpɪnhəʊl/；美 /ˈpɪnhoʊl/','针孔；极小孔洞',
 '小得像针尖扎出来的孔；实际不必真由针扎。',
 'pin 针 + hole，按小孔大小、形成形象命名。技术里也可用于小孔成像等固定名称。',H('pin + hole → pinhole','针般细小的孔洞'),
 'a pinhole in the fabric 布料针孔，a pinhole camera 针孔相机。',
 'a pinhole in；a pinhole camera；a tiny pinhole。',
 'pinhole 小孔，peephole 为观察而开的孔；一个按大小形象，一个按用途，不是所有针孔都用来窥看。',
 ('Light shone through a pinhole in the curtain.','光从窗帘的针孔里透过来。'),('The class built a simple pinhole camera.','班里做了一台简单针孔相机。'))
W('peephole','英 /ˈpiːphəʊl/；美 /ˈpiːphoʊl/','观察孔；门镜、猫眼',
 '从一个小孔向外看，门上常配镜片，人在屋里先看清外面是谁。',
 'peep 偷看、从小处看 + hole，按用途命名。前部是 peep 的看义，不是鸟叫声义。',H('peep + hole → peephole','用来从小开口观察的孔、门镜'),
 'look through the peephole 从猫眼看，a peephole in the door 门上的观察孔。',
 'look through the peephole；a peephole in the door；a door peephole。',
 'peephole 观察用途，keyhole 钥匙孔；有人可以碰巧从钥匙孔看，但两种结构的主要用途不同。',
 ('She looked through the peephole before opening the door.','开门前，她从猫眼向外看了看。'),('The old door had a small peephole.','旧门上有个小观察孔。'))
W('porthole','英 /ˈpɔːthəʊl/；美 /ˈpɔːrthoʊl/','舷窗；船、飞行器等的小型窗孔',
 '船舱壁上的小窗常是圆的，可以看出去、进光；名字先抓住开口。',
 'port 在此取船壁开口等旧义 + hole，不接港口，也不接计算机端口的现代技术定义来倒推。',H('port〔开口〕+ hole → porthole','船壁孔口、窗孔 → 舷窗'),
 'a cabin porthole 船舱舷窗，look through a porthole 从舷窗看。',
 'a cabin porthole；look through a porthole；a round porthole。',
 'porthole 舷窗与 pothole 路坑仅差 r，读音、用途不同；port 的开口义不等于这里在港口旁挖坑。',
 ('She watched the sea through the cabin porthole.','她透过船舱舷窗望着大海。'),('A round porthole let light into the room.','一扇圆形舷窗让光照进房间。'))
W('foxhole','英 /ˈfɒkshəʊl/；美 /ˈfɑːkshoʊl/','狐狸洞；散兵坑、掩体坑',
 '狐狸钻进地下洞里躲；士兵挖个坑作掩护，也借了这种低伏进洞的形象。',
 'fox 狐狸 + hole，旧英语已有 foxhol。军事掩体坑是后来引申，不表示坑一定由狐狸挖成。',HO[:1]+[['古英语 foxhol → foxhole','狐狸洞；后借指士兵用的掩体坑']],
 'a foxhole in the bank 土坡里的狐狸洞，dig a foxhole 挖散兵坑。',
 'dig a foxhole；shelter in a foxhole；a foxhole in the bank。',
 'foxhole 通常小型掩体坑，trench 战壕常是一条沟式工事；日常军史描写两者形态、用途有侧重。',
 ('The fox disappeared into a foxhole near the trees.','狐狸钻进树旁的狐狸洞不见了。'),('The soldiers sheltered in a foxhole.','士兵们在散兵坑里隐蔽。'))
W('blowhole','英 /ˈbləʊhəʊl/；美 /ˈbloʊhoʊl/','鲸类呼吸孔；喷气、喷水的岩洞孔口',
 '有东西从孔里喷出：鲸从头顶呼吸，海岸岩洞也可能在浪冲来时喷出水、气。',
 'blow 吹、喷 + hole。动物与地貌用法按喷出这个现象分别命名，不表示鲸一定往孔里装水再喷。',H('blow + hole → blowhole','气、水喷出的孔；动物呼吸孔或岩洞孔口'),
 'a whale’s blowhole 鲸的呼吸孔，a coastal blowhole 海岸喷孔。',
 'a whale’s blowhole；a coastal blowhole；air from a blowhole。',
 '鲸的 blowhole 是呼吸相关结构，鱼的 gills 鳃是另一种结构；喷出的可见气雾不能简单当成它的口鼻吐海水。',
 ('The whale surfaced and breathed through its blowhole.','鲸浮出水面，通过呼吸孔呼吸。'),('Waves forced water up through the coastal blowhole.','海浪把水从海岸岩洞喷孔顶了上来。'))
W('asshole','英 /ˈæshəʊl/；美 /ˈæshoʊl/','肛门〔粗俗〕；混蛋〔辱骂〕',
 '字面是粗俗身体部位词，骂人时则贬他自私、恶劣；不是普通正式交流的称呼。',
 'ass 臀部 + hole，现代美式常用形式，与更旧 arsehole 对应。人物辱骂义是后来的贬称，不按身体结构判断人品。',H('ass + hole → asshole','粗俗身体部位 → 辱骂人的称呼'),
 'act like an asshole 表现得像混蛋；文学、影视可见。正式解剖词通常 anus。',
 'act like an asshole；call someone an asshole；the insult asshole。',
 'asshole 粗俗侮辱，rude person 失礼的人较中性；asshole 和 arsehole 常对应美式、英式习惯。',
 ('The character angrily called the driver an asshole.','角色愤怒地骂那个司机是混蛋。'),('She said that acting like an asshole would not solve anything.','她说，表现得像个混蛋解决不了任何问题。'))
W('arsehole','英 /ˈɑːshəʊl/；美 /ˈɑːrshoʊl/','肛门〔粗俗〕；混蛋〔英式常见辱骂〕',
 '和 asshole 对应的常见英式说法，区别主要在 arse 这一形式，侮辱意味仍很强。',
 'arse 臀部 + hole，有中古英语旧形式。不要因为英国拼法不同就当成礼貌词或完全另一概念。',H('arse + hole → arsehole','粗俗身体部位；英式常见人物辱骂'),
 'call someone an arsehole 骂某人混蛋。英式对白中常见，是否直接拼写、引用由场合决定。',
 'call someone an arsehole；act like an arsehole；the word arsehole。',
 'arsehole/asshole 地区拼写及读音不同，语域都粗俗；两者都不是礼貌称呼。',
 ('In the British film, the character uses the insult arsehole.','英国电影里，这个角色用了 arsehole 这个辱骂词。'),('He regretted calling his neighbour an arsehole.','他后悔骂邻居是个混蛋。'))
R('B2687','空了一块的孔、洞、坑；按用途、形态和比喻分组','HOLE：实处缺一块，地面凹下去；复杂词前部说明怎样的洞','hole → holey；loophole/pigeonhole 讲比喻；地面坑、人工孔、动物洞分开；常见粗俗身体词最后注明语域。',
 'hulk 的船、庞大人物等支线和冷门 holing、cornhole 等本轮略过。不是所有名字都按两个现代字面词临时拼出，loophole 的 loop、pothole 的 pot 特别讲旧义。',
 'hole + -y；旧 loupe/pigeon/worm/sink/pot/bore/pin/peep/port/fox/blow/ass/arse + hole；共有 key/man/water + hole。',
 [['基本空洞与比喻','hole · holey · loophole · pigeonhole · wormhole'],['地面凹坑和钻孔','sinkhole · pothole · borehole · manhole · waterhole'],['小孔与观察、船窗','pinhole · peephole · porthole · keyhole'],['动物与呼吸、喷孔','foxhole · blowhole'],['粗俗身体词与辱骂','asshole · arsehole']],
 'hole/whole 同音不同源；holey/holy/wholly 分清；pothole 路坑、porthole 舷窗；wormhole 理论概念与科幻设定区分。',
 'Light passed through a pinhole, while a larger porthole revealed the sea.\n\n光穿过一个针孔，更大的舷窗则能望见海面。',
 'hole holey loophole pigeonhole wormhole sinkhole pothole borehole manhole waterhole pinhole peephole porthole keyhole foxhole blowhole asshole arsehole')
ROOTS[-1]['exclude']['hulk']='船体、庞大人物等支线本轮暂略；更远词源分析有不同说法，不按现代 hole 简单硬拆。'
if __name__=='__main__':save('continuation_20261030_bn',ROOTS,WORDS)
