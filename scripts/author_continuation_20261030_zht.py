"""Scoot, skitter, trot, gallop and zoom: speed with a visible shape."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2975':dict(words='scoot scoots scooted scooting skitter skitters skittered skittering'.split(),label='scoot、skitter：嗖地走、小步快速窜动',note='scoot 来源未定，可能接古诺尔斯 skjota 等快速发出、移动材料；skitter 经 skite 等急窜材料接相近北欧分析。与 shoot 是可能的旧材料联系，不是由现代 shoot 随意换字母。'),
 'B3003':dict(words='trot trots trotted trotting'.split(),label='trot：快而有节奏的小跑',note='经法语 trot、troter，接法兰克语重建 *trotton 与日耳曼踏行材料。和 tread 可作历史同族比较，不是现代 tread 加 -ot。'),
 'B4597':dict(words='gallop gallops galloped galloping'.split(),label='gallop：马飞快奔驰，到做事飞快',note='本组与 horse 作步态场景比较，不是由现代英语 horse 派生。gallop 经古法语 galoper、waloper 等，或接法兰克语善跑的重建组合，不把猜测当确定记录。'),
 'B2964':dict(words='zoom zooms zoomed zooming'.split(),label='zoom：嗡地冲过去，到镜头拉近',note='本组与 run 比较速度、画面，不是现代 run 的后代。zoom 起于低沉嗡声的拟声材料，航空用法带来快速冲向、掠过，再有镜头变焦。'),
 'B4346':dict(words='zip zips'.split(),label='zips：拉链、迅速移动、拉上拉链',note='zip 拟声的快速移动材料与后来拉链名称、动词等关联；现代加 -s 可是动词三单、名词复数。文件压缩用法另看基础词，不把每句都译成拉链。'),
}
SCOOT=[['scoot 来源未定，可能接北欧快速发出、移动材料','如 skjota 的分析，不强定为现代 shoot 直接派生'],['快速离开、挪动 → scoot over 等现代口语搭配','学习像身子很快挪开一点，不要求真的发出声响']]
SKITTER=[['skite 急窜、快跑等材料 → 反复动作 skitter','可能有北欧快速移动材料的更远联系'],['急促小步移动 → 小动物、树叶、念头快速掠动','后来用于许多细碎、急促的移动场景']]
TROT=[['法语 trot、troter → 英语 trot','更远接法兰克语、日耳曼踏行材料'],['马的快而有节奏步态 → 人、动物小跑；比喻快速推进','trot out 后来还可说拿出一套熟话、论点']]
GALLOP=[['古法语 galoper、waloper 等 → gallop','更远可能接法兰克语善跑的重建组合'],['马快速奔驰 → 进程、阅读、时间飞快前进','名词可说这种步态、一次飞奔']]
ZOOM=[['zoom 起于低沉嗡声的拟声材料','航空中发展为快速冲向、飞掠'],['快速接近 → 摄影镜头变焦的用法','现代 zoom in / out 可用于镜头、地图和界面']]
W('scoots','/skuːts/','迅速离开、挪动〔第三人称单数〕',
 '猫听见响声嗖地躲开，或人很快往旁边挪一点，是 scoots。常见 scoots over 给别人腾点位置。',
 'scoot + -s，/t/ 后读 /s/；基础词来源未定，可能接北欧快速移动材料。',SCOOT+[['scoot + -s → scoots','他或它迅速移动、让开']],
 'scoots under the chair；scoots over to make room。',
 'scoots away；scoots along the corridor。',
 'scoots 不要求靠滑板车移动；rides a scooter 才明确说骑滑板车、踏板车。',
 ('The cat scoots under the chair when the doorbell rings.','门铃一响，猫就嗖地钻到椅子下面。'),('She scoots over to make room for her friend.','她很快往旁边挪了挪，给朋友腾出位置。'),sources=S('scoots','scoot'))
W('scooted','/ˈskuːtɪd/','迅速离开、挪动了',
 '刚才迅速往旁边挪，或一下钻走了，可以说 scooted。动作往往短、快，口语感很强。',
 'scoot + 完整 -ed，/t/ 后读 /ɪd/；词干是 oo，不双写 t。',SCOOT+[['scoot + -ed → scooted','过去快速挪动、离开']],
 'scooted over；scooted away；scooted into the kitchen。',
 'scooted along the bench；scooted out of the room。',
 'scooted over 常是坐着挪一挪也能用，不一定站起来跑；ran over 才可能明确说跑过去。',
 ('I scooted over on the bench so she could sit down.','我在长椅上往旁边挪了挪，好让她坐下。'),('The mouse scooted behind the cupboard.','老鼠一下窜到了柜子后面。'),sources=S('scooted','scoot'))
W('scooting','/ˈskuːtɪŋ/','正在迅速移动、挪开；骑滑板车、踏板车前进',
 '身子很快挪过去，是 scooting；现代也能说骑滑板车前进。要由场景看是否真的有车，不是词里天然藏着一辆。',
 'scoot + -ing，保留单 t；从基础动词的快速移动，到与 scooter 相应的现代出行用法。',SCOOT+[['scoot + -ing → scooting','快速挪动的过程，也可说骑滑板车行进']],
 'scooting over on the seat；scooting along the pavement。',
 'scooting away；children scooting in the park。',
 'scooting 强调快挪或骑行，sitting 只说坐；一个人坐着仍可以挪动。',
 ('He kept scooting along the bench to let people sit down.','他不断沿着长椅往旁边挪，让别人坐下。'),('The children were scooting along the park path.','孩子们正骑着滑板车沿公园小路前进。'),sources=S('scooting','scoot'))
W('skitter','英 /ˈskɪtə/；美 /ˈskɪtɚ/','小步急窜；轻快、急促地掠动',
 '蜘蛛脚步很碎，嗖嗖爬过地面；干叶被风吹得跳着滑过，都能 skitter。比 run 多了小、轻、急促的动势。',
 '接 skite 急窜、快跑的反复动作形式，更远可能有北欧来源。这里的 er 是旧动作构词材料，不是在说一个做事者。',SKITTER,
 'skitter across the floor；leaves skitter along the path。',
 'skitter away；thoughts skitter through the mind。',
 'skitter 不限定用脚，叶子、石子也可急促掠动；sprint 通常更直接说用力冲刺跑。',
 ('Dry leaves skitter across the pavement in the wind.','风把干叶吹得在路面上轻快跳滑。'),('Tiny spiders skitter away when the box is opened.','盒子一打开，小蜘蛛就急急地四散爬开。'),sources=S('skitter','skitter'))
W('skitters','英 /ˈskɪtəz/；美 /ˈskɪtɚz/','小步急窜、轻快掠动〔第三人称单数〕',
 '小东西一下爬过，一片叶子被吹得跳着滑走，是 skitters。画面常是动作细碎、快得不太稳。',
 'skitter + -s，读 /z/；基础 skitter 接 skite 的反复动作材料，更远的语言联系仍有不确定性。',SKITTER+[['skitter + -s → skitters','它急促、轻快地掠动']],
 'skitters across the floor；skitters away；skitters along the path。',
 'a leaf skitters；a crab skitters。',
 'skitters 是快速细碎地动，crawls 可以很慢；用小动物作主语也不能把两者一概等同。',
 ('A small crab skitters across the wet sand.','一只小螃蟹在湿沙上急急爬过。'),('A dry leaf skitters along the path.','一片干叶沿小路跳着滑过去。'),sources=S('skitters','skitter'))
W('skittered','英 /ˈskɪtəd/；美 /ˈskɪtɚd/','急促窜过、轻快掠动了',
 '石子沿地面一跳一跳滑过去，或小动物飞快窜开，可以说 skittered。不是一条平稳、缓慢的移动线。',
 'skitter + 完整 -ed，读 /d/；不增加 /ɪd/ 音节。',SKITTER+[['skitter + -ed → skittered','过去急促、细碎地掠动']],
 'skittered across the floor；skittered away；skittered over the stones。',
 'pebbles skittered；a spider skittered。',
 'slid 只说滑动，skittered 常像轻轻跳动、急促掠过；未必一直贴着表面平稳滑。',
 ('The spider skittered behind the cupboard.','蜘蛛急急地窜到柜子后面。'),('Loose stones skittered down the slope.','松动的小石子一跳一跳地滑下坡。'),sources=S('skittered','skitter'))
W('skittering','英 /ˈskɪtərɪŋ/；美 /ˈskɪtərɪŋ/','正在急促窜动、轻快掠过',
 '声音细细碎碎，东西一小下接一小下地急动，是 skittering。可以写动物脚步、被风吹的落叶，也能写散乱掠过的念头。',
 'skitter + -ing；英式在元音后缀前读出 r。原有 er 属于基础动作形式，-ing 才是本层过程后缀。',SKITTER+[['skitter + -ing → skittering','急促、细碎移动的过程']],
 'skittering across the floor；leaves skittering past；skittering footsteps。',
 'thoughts skittering through her mind；skittering away。',
 'skittering 的运动碎、急，gliding 的画面通常更连续、顺滑；都可快，但形状不同。',
 ('We heard something skittering behind the wall.','我们听见墙后有什么东西在细碎急动。'),('Leaves were skittering across the empty square.','落叶在空广场上被风吹得跳滑而过。'),sources=S('skittering','skitter'))
W('trot','英 /trɒt/；美 /trɑt/','小跑、快步走；马的快步步态',
 '狗轻快地小跑着跟来，马比走路快、又没放开奔驰，都能用 trot。它让人看见较短、稳定、有节奏的步子。',
 '经古法语 trot、troter，接法兰克语重建 *trotton 与日耳曼踏行材料。tread 可作历史同族比较，不是现代 tread 直接加一个后缀得到。',TROT,
 'trot along the path；at a trot 小跑着；trot out an excuse 又搬出一套借口。',
 'break into a trot 开始小跑；on the trot 接连、忙个不停〔英式〕。',
 'trot 常是有节奏的小跑，gallop 在马的场景是放开奔驰；速度和步态都不同。',
 ('The dog began to trot beside us.','狗开始在我们身边小跑。'),('We finished three projects on the trot.','我们接连完成了三个项目。'),sources=S('trot','trot'))
W('trots','英 /trɒts/；美 /trɑts/','小跑〔第三人称单数〕；小跑几趟；腹泻〔the trots，口语〕',
 '狗每天小跑着跟主人，是 trots after him。另有 the trots 这个口语说法，指拉肚子，可以用老往厕所跑的画面来记，不据此断定具体造词故事。',
 'trot + -s，/t/ 后读 /s/；可为动词三单、名词复数。the trots 的口语义后来出现，不能每次见复数就只译成多次小跑。',TROT+[['trot + -s → trots','他、它小跑；另有 the trots 拉肚子的固定说法']],
 'trots after someone；trots out an argument；has the trots〔很口语〕。',
 'trots across the yard；trots along beside us。',
 'trots out an excuse 往往嫌人又搬出老借口，不是把借口真的牵来小跑；固定搭配按整句理解。',
 ('The dog trots after its owner.','狗小跑着跟在主人后面。'),('He always trots out the same old excuse.','他总是又搬出那套老借口。'),('In the dialogue, the traveller says he has the trots.','对话里，那位旅人说自己拉肚子了。'),sources=S('trots','trot'))
W('trotted','英 /ˈtrɒtɪd/；美 /ˈtrɑtɪd/','小跑、快步走了；又搬出一套说辞了',
 '刚才轻快小跑到门口，是 trotted；又把老话、老借口拿出来，也能 trotted out。小步向前的画面发展为把东西带出来展示。',
 'trot 双写 t 加完整 -ed，/t/ 后读 /ɪd/；重读短元音单音节的规则变化。',TROT+[['trot + -ed → trotted','双写 t，过去小跑；out 搭配中可说搬出说辞']],
 'trotted across the yard；trotted out an excuse；trotted off。',
 'trotted alongside the horse；trotted down the path。',
 'trotted out 常带又拿出老一套的轻微贬意，introduced 可以中性说介绍；不是所有介绍都显得敷衍。',
 ('She trotted across the yard to meet us.','她小跑着穿过院子来迎我们。'),('He trotted out the usual excuses for being late.','他又搬出那些常见的迟到借口。'),sources=S('trotted','trot'))
W('trotting','英 /ˈtrɒtɪŋ/；美 /ˈtrɑtɪŋ/','正在小跑、快步走；又搬出说辞',
 '马有节奏地快步前进，狗小跑着跟着人，是 trotting。加 out 还可说不断拿出一套旧话、例子。',
 'trot 双写 t 加 -ing；过程分词可形容正在小跑的动物，也用于 trotting out 搭配。',TROT+[['trot + -ing → trotting','双写 t，小跑的过程，或搬出说辞的动作']],
 'trotting beside someone；a trotting horse；trotting out the same excuse。',
 'trotting down the road；came trotting over。',
 'trotting 在马的步态中比 walking 快，但不等于 galloping 全速奔驰；不要只记成笼统的跑。',
 ('The dog came trotting over when it heard its name.','狗听见名字，就小跑着过来了。'),('She was tired of hearing him trotting out the same excuse.','她听腻了他反复搬出同一个借口。'),sources=S('trotting','trot'))
W('gallop','/ˈɡæləp/','马快速奔驰；飞快地推进；一次飞奔',
 '马放开步子飞奔，是 gallop。读书、讲解或时间过得飞快，也能借这个画面，像一阵马蹄冲了过去。',
 '经古法语 galoper、waloper 等进入英语；更远可能接法兰克语善跑的重建组合。用可能来限定远源，现代把 gallop 作为完整基础词，再认它的常见后缀变化。',GALLOP,
 'gallop across the field；at a gallop 飞奔着；gallop through a chapter。',
 'a full gallop；go for a gallop；time seems to gallop。',
 'gallop 在马的场景比 trot 小跑更快、更放开；比喻里强调快，未必在赞扬读得仔细。',
 ('The horse broke into a gallop.','马开始放开步子奔驰。'),('Do not gallop through the explanation; give us time to follow.','解释别讲得那么快，给我们时间跟上。'),sources=S('gallop','gallop'))
W('gallops','/ˈɡæləps/','快速奔驰、飞快推进〔第三人称单数〕；几次飞奔',
 '马一过空地就放开跑，是 gallops；几段快速跑马的活动，也可数成 gallops。人说话飞快推进也能借用。',
 'gallop + -s，/p/ 后读 /s/；动词三单与名词复数同形。',GALLOP+[['gallop + -s → gallops','他、它飞快推进；多次奔驰']],
 'gallops across the field；gallops through the material；short gallops。',
 'gallops towards the gate；morning gallops。',
 'gallops through a topic 可能嫌讲得太快，covers a topic 只说谈到；速度快不保证听者理解。',
 ('The horse gallops towards the open gate.','马飞快奔向敞开的大门。'),('The lecturer gallops through the final slides.','讲师飞快讲过最后几页幻灯片。'),sources=S('gallops','gallop'))
W('galloped','/ˈɡæləpt/','快速奔驰了；飞快地推进、做过了',
 '马一阵飞跑冲过草地，是 galloped；赶时间时飞快念完一段说明，也可 galloped through。',
 'gallop + 完整 -ed，/p/ 后读 /t/；词尾音节不重读，不双写 p。',GALLOP+[['gallop + -ed → galloped','过去快速奔驰，或飞快处理']],
 'galloped across the field；galloped through the chapter；galloped away。',
 'galloped towards the village；had galloped all morning。',
 'galloped through 不保证逐处看懂，studied carefully 才强调仔细研究；快读和细读不是同一过程。',
 ('The riders galloped across the field.','骑手们策马飞奔过田野。'),('He galloped through the final chapter before dinner.','晚饭前，他飞快读完了最后一章。'),sources=S('galloped','gallop'))
W('galloping','/ˈɡæləpɪŋ/','正在奔驰；飞速发展的、失控般快速的',
 '一阵密集马蹄声，是 galloping horses。galloping inflation 则像涨价在放开跑，常嫌增长太快、不容易控制。',
 'gallop + -ing，结尾音节不重读，不双写 p；分词可写奔驰过程，也能形容发展飞快。',GALLOP+[['gallop + -ing → galloping','奔驰的过程，或飞速发展的性质']],
 'galloping horses；galloping inflation；galloping through a speech。',
 'a galloping pace；horses galloping across the plain。',
 'galloping inflation 突出涨价迅猛，stable prices 是价格稳定；这里是形容速度、趋势的比喻，不是具体数值标准。',
 ('We heard galloping horses on the road.','我们听见路上传来马群奔驰的声音。'),('The article described a period of galloping inflation.','文章描述了一段物价飞涨的时期。'),sources=S('galloping','gallop'))
W('zoom','/zuːm/','飞快掠过、猛冲；迅速上升；变焦、缩放',
 '车嗖地开过，数字一下冲高，都能 zoom。相机 zoom in 像快速靠近对象，但画面变大不表示相机一定真的移了位置。',
 '起于低沉嗡声的拟声材料；航空用法发展为快速冲向、掠过，后来摄影镜头借来表示变焦。现代界面也沿用放大、缩小。',ZOOM,
 'zoom past 飞快掠过；zoom in 放大、拉近；zoom out 缩小、拉远。',
 'zoom through a task 飞快做完；a zoom lens 变焦镜头。',
 'zoom in 指视野拉近、细节变大，move closer 才明确说位置靠近；数字界面的缩放更不要求身体移动。',
 ('A motorbike seemed to zoom past the window.','一辆摩托车嗖地从窗外掠过。'),('Zoom in to see the small details on the map.','放大一点，看看地图上的小细节。'),sources=S('zoom','zoom'))
W('zooms','/zuːmz/','飞快移动、猛增、变焦〔第三人称单数〕；几次缩放',
 '相机把远处东西拉近，或孩子骑车嗖地冲过，可以说 zooms。主语不同，快速接近的画面落在运动或视野上。',
 'zoom + -s，读 /z/；可为动词三单，也能作缩放动作名词的复数。',ZOOM+[['zoom + -s → zooms','它飞快移动、放大缩小；多次缩放']],
 'zooms past；zooms in on a face；zooms out to show the street。',
 'zooms up 猛升；quick zooms 快速变焦。',
 'zooms in on a detail 把视野集中到细节，focuses 也可说对焦或集中注意；缩放和是否清晰是不同控制。',
 ('The camera zooms in on her face.','镜头拉近到她的脸部。'),('He zooms past us on his bicycle.','他骑着自行车，嗖地从我们身边冲过。'),sources=S('zooms','zoom'))
W('zoomed','/zuːmd/','飞快掠过了；猛升了；缩放、变焦了',
 '一辆车嗖地过去，或你刚把地图放大，都可以 zoomed。它描述快动或视野变化，不只属于相机。',
 'zoom + 完整 -ed，/m/ 后读 /d/；原词 oo 保留，不双写 m。',ZOOM+[['zoom + -ed → zoomed','过去快速移动、猛增，或完成缩放']],
 'zoomed past；zoomed in on the image；zoomed out。',
 'prices zoomed up；zoomed through the work。',
 'zoomed in 可以是数字放大，walked closer 是身体靠近；看起来更近并不能单凭一个词判断用了哪种设备技术。',
 ('A red car zoomed past the café.','一辆红车嗖地从咖啡馆前开过。'),('I zoomed in on the photograph to read the sign.','我放大照片，想看清牌子上的字。'),sources=S('zoomed','zoom'))
W('zooming','/ˈzuːmɪŋ/','正在飞快移动、猛增；变焦、缩放',
 '东西嗖嗖移动，是 zooming；手指把地图拉近拉远，也是 zooming。一个词把快动的感觉延伸到视野快速接近、远离。',
 'zoom + -ing，保留单 m；过程形式用于速度、数量变化，也用于镜头和界面的缩放。',ZOOM+[['zoom + -ing → zooming','快速移动，或缩放视野的过程']],
 'zooming past；zooming in and out；zooming around the room。',
 'zooming in on the details；zooming through the streets。',
 'zooming 常说缩放比例，scrolling 是滚动内容位置；在地图上放大和拖到另一块地方不是同一种动作。',
 ('Children were zooming around the room with toy cars.','孩子们拿着玩具车，在房间里嗖嗖地跑来跑去。'),('Zooming out reveals the whole coastline.','缩小视野后，就能看见整段海岸线。'),sources=S('zooming','zoom'))
W('zips','/zɪps/','拉链〔复数〕；迅速移动、拉上拉链〔第三人称单数〕',
 '包上两条拉链，是 two zips；他很快拉上外套，是 zips up his jacket；快车嗖地经过，也能 zips past。句子决定动作落在哪里。',
 'zip + -s，/p/ 后读 /s/；快动支有拟声背景，拉链名词与 zipper 等名称相接，拉上拉链的动词后来发展。',
 [['zip 的拟声材料 → 快速移动','zipper、zip 的装置名称再与拉链动作相接'],['zip + -s → zips','多条拉链，或它快动、他把拉链拉上']],
 'zips on a bag；zips up a coat；zips past the window。',
 'the bag has two zips；zips along the road。',
 'zips 是名词时可为英式常见的拉链，zippers 在美式常见；动词 zips up 两种英语都可使用。',
 ('The bag has two sturdy zips.','那个包有两条结实的拉链。'),('He zips up his coat before leaving.','出门前，他把外套拉链拉上。'),('A small train zips past the platform.','一列小火车嗖地掠过站台。'),sources=S('zips','zip'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zht',ROOTS,WORDS)
 extend_lessons()
