"""Flat with separate flatter history; close root pages for shared shooting and leadership."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
R('B4454','射击活动；枪击事件；摄影拍摄','SHOOTING：按 shoot 的动作分支看正在做哪件事','shooting 已有逐词精讲，本根集中射击运动、新闻事件与拍摄的场景辨析。',
 '这是活动名词、分词形式，可说体育射击，也可摄影拍摄；词形相同不等于新闻、电影都该翻成枪击。',
 'shoot + -ing；shooting star 流星是固定形象表达，不是持枪的星。',
 [['活动和事件','shooting']],
 'a shooting competition 射击比赛；film shooting 拍摄；a shooting incident 枪击事件；按宾语、场景分义。',
 'Shooting for the film begins next week.\n\n这部电影下周开始拍摄。','shooting')
R('B4364','领导能力、行为与领导层','LEADERSHIP：怎样把一群人带向目标，也可说谁在掌舵','leadership 已有逐词精讲，本页把能力、带领行为、领导集体三层意思归在一起。',
 '-ship 构成身份、职能、性质的抽象名词，不是船。领导能力不只来自头衔，没有正式职位也可表现出带领作用。',
 'leader + -ship；leadership skills 能力，under her leadership 带领，the leadership 领导集体。',
 [['能力、行为与集体','leadership']],
 'leader 具体人物，leadership 领导能力或领导层；the leadership 在集合语境不只指一个人。',
 'The team grew stronger under her leadership.\n\n在她带领下，团队变得更强。','leadership')
F=[['古诺尔斯语 flatr → 中古英语 flat → flat','平、摊开、处在一个平面'],['另有本族 flet、苏格兰语 flat 等住房词路径','楼层、住处 → 公寓，与平、楼面词族有关'],['现代 flat 的形状与感受比喻','平、扁；没气、没气泡；平淡、直接等']]
def FH(f,m):return F+[[f,m]]
W('flat','/flæt/','平、扁的；没气、乏味的；公寓〔英式〕；降调的〔音乐〕',
 '表面没明显凸起；气泡饮料不再冒泡、故事没起伏，也借平的感觉。英式一套公寓则有楼层、住处的旧词路径。',
 '形容词经古诺尔斯语 flatr 进入中古英语。公寓名词也接本族 flet、苏格兰语楼层等词的变化，并非所有 modern flat 都是同一次形容词名词化。',F,
 'a flat surface 平面，a flat tyre 没气轮胎，flat soda 没气饮料，rent a flat 租公寓，sing flat 音唱低了。',
 'a flat surface；a flat tyre；rent a flat；fall flat。',
 'flat 平、扁与 smooth 光滑不同，粗糙平面也可 flat；apartment 美式常公寓。fall flat 可失败、没效果，不一定摔倒。',
 ('We need a flat surface for the model.','做模型需要一块平的表面。'),('They rented a small flat near the station.','他们在车站附近租了一套小公寓。'))
W('flatter','英 /ˈflætə/；美 /ˈflætər/','更平的〔比较级〕；奉承、使显得好看〔动词，来源另辨〕',
 '地面更平，是 flat 的比较；话说得让人很受用、衣服衬得人好看，则是另一动词用法，不能只用更平解释。',
 '比较级为 flat + -er，双写 t。奉承动词有中古英语 flatteren 等旧形，法语抚慰、奉承与日耳曼语相近动词的关系有不同分析；不把现代比较级当它确定的直接祖先。',
 [F[0],['flat + -er → flatter〔比较级〕','更平、较扁'],['中古英语 flatteren 等 → flatter〔动词〕','奉承、使有好感；更早路线有不同分析']],
 'a flatter surface 更平表面，flatter someone 奉承某人，That colour flatters you 那颜色很衬你，flatter yourself 自以为、往自己脸上贴金。',
 'a flatter surface；flatter someone；flatter yourself；the colour flatters。',
 'flatter 比较级与奉承动词同形；flattering 可中看、衬人，也可奉承，不是 flatten 压平的进行形式。',
 ('The new path is flatter than the old one.','新小路比旧路更平。'),('Your kind words flatter me, but I still have much to learn.','你的好话让我很受用，但我还有很多要学。'),
 sources=['https://en.wiktionary.org/wiki/flatter#English','https://www.etymonline.com/word/flatter'])
W('flatten','/ˈflætn/','压平、使变平；变平',
 '把凸起压下去，把折皱摊开，让原来不平的东西趋平。也可说曲线趋平、差别被压低。',
 'flat + -en，双写 t，形成使平、变平的动词。',FH('flat + -en → flatten','使变平；变平'),
 'flatten the dough 压平面团，flatten a box 把纸箱压扁，flatten the curve 使曲线趋平。',
 'flatten the dough；flatten the box；flatten the curve。',
 'flatten 压平，flatter 奉承是不同词；the road flattened out 指坡度渐平，不是道路开始夸人。',
 ('Flatten the dough with a rolling pin.','用擀面杖把面团擀平。'),('The road flattened out near the river.','靠近河边时，道路逐渐平坦起来。'))
W('flatness','/ˈflætnəs/','平坦、扁平；平淡、缺少起伏',
 '拿平这个特点来描述地面，也可描述声音、文章缺乏变化。',
 'flat + -ness，中古英语已有 flatnesse。性质名词不限定物理平面，也接乏味、平直表达。',FH('flat + -ness → flatness','平坦性质；比喻缺少变化、生气'),
 'the flatness of the land 地势平坦，flatness of tone 语调平直，check the flatness 检查平整度。',
 'the flatness of；flatness of tone；check the flatness。',
 'flatness 平坦，smoothness 光滑；平而有粗糙纹理的板，两项性质可不同。',
 ('We were surprised by the flatness of the landscape.','地势之平坦让我们意外。'),('The flatness of his delivery made the joke less funny.','他的表达缺乏起伏，让笑话没那么好笑。'))
W('flatly','/ˈflætli/','断然、直截了当地；平淡无起伏地',
 '不绕弯、不给可商量的余地，说一个明确不；也可形容声音平直，没有情绪起伏。',
 'flat + -ly，接平直、完全、明确等旧副词义发展，不是一律平面地。',FH('flat + -ly → flatly','直接、断然；不带起伏地'),
 'flatly refuse 断然拒绝，flatly deny 断然否认，say flatly 平平地、直截了当地说。',
 'flatly refuse；flatly deny；say flatly。',
 'flatly deny 表明确否认，不说明否认本身是真是假；flatly 没有力气地与明确强硬地也须看具体动词、语气。',
 ('She flatly refused to change the schedule.','她断然拒绝更改日程。'),('“There is no spare key,” he said flatly.','“没有备用钥匙。”他平平地说。'))
W('flatmate','/ˈflætmeɪt/','合租公寓的室友〔英式常见〕',
 '住在同一套 flat 里的人，不保证睡同一间卧室。mate 在这里是共同居住的伙伴。',
 'flat 公寓 + mate 伙伴，形成共住者名称。接住房词义，不是平坦的朋友。',F[1:2]+[['flat + mate → flatmate','同住一套公寓的人']],
 'my flatmate 我的合租室友，a new flatmate 新室友，look for a flatmate 找合租者。',
 'a new flatmate；my flatmate；look for a flatmate。',
 'flatmate 同公寓，roommate 美式可同套房也可同卧室，地区习惯不同；housemate 常同一栋房子。',
 ('My flatmate works at the library.','我的合租室友在图书馆工作。'),('We are looking for a third flatmate.','我们在找第三位合租室友。'))
W('flatbread','/ˈflætbred/','扁面包、薄饼类面包',
 '不是高高膨起的一整条，而是较扁、可成薄片或饼状的面包类别。',
 'flat 扁平 + bread 面包，按形状命名。不同品种、发酵做法可不同，不说所有 flatbread 都完全无发酵。',FH('flat + bread → flatbread','扁平形状的面包'),
 'warm flatbread 热扁面包，a piece of flatbread 一块薄面包，flatbread with dips 配蘸酱的扁面包。',
 'warm flatbread；a piece of flatbread；flatbread with dips。',
 'flatbread 形状类别，不是所有地方同一种食谱；slice of bread 面包片是把大面包切片，不必属于 flatbread。',
 ('They served warm flatbread with the soup.','他们给汤配了热扁面包。'),('She tore a piece from the flatbread.','她从扁面包上撕下一块。'))
W('flatware','英 /ˈflætweə/；美 /ˈflætwer/','刀叉匙等餐具〔尤美式〕',
 '桌上那套刀、叉、勺，名字保留扁平用品类别的老分类，不保证勺子每一处都绝对平。',
 'flat + ware 制品，形成餐具集合名。常与 hollowware 壶等较空深器皿的旧分类对照；现代日常先掌握刀叉匙。',FH('flat + ware → flatware','刀叉匙等餐具总称'),
 'stainless steel flatware 不锈钢刀叉匙，a flatware set 一套餐具，polish the flatware 擦亮餐具。通常不可数。',
 'stainless steel flatware；a flatware set；wash the flatware。',
 'flatware 与美式 silverware 常近义，不保证银制；dinnerware 更常说盘碗杯等器皿。',
 ('The drawer holds the stainless steel flatware.','抽屉里放着不锈钢刀叉匙。'),('They bought a flatware set for the new flat.','他们为新公寓买了一套刀叉匙。'))
W('flatline','/ˈflætlaɪn/','平直线；〔指标等〕停滞、不再变化；监测曲线变平〔原用法〕',
 '图线本来上下动，后来拉成一条近直线；比喻增长停住，销量、参与人数长期没变化。',
 'flat 平 + line 线，名词、动词用法。医疗监测曲线是早期常见背景，后来扩展到数据停滞；具体曲线含义不能只凭一个词作诊断。',FH('flat + line → flatline','平直曲线；比喻指标不再增长、变化'),
 'sales flatline 销量停滞，growth flatlines 增长停住，a flatlining market 停滞市场。',
 'sales flatline；growth flatlines；a flatlining trend。',
 'flatline 常比喻变化近乎停止，不等于每次都 drop to zero 跌至零；一条高位水平线也可描述停滞。',
 ('Sales rose in spring and then flatlined.','销量春季上升，随后停滞了。'),('Attendance has flatlined at about fifty people a week.','每周参与人数停在大约五十人，没再变化。'))
W('flatland','/ˈflætlənd/ 或 /ˈflætlænd/','平地、平原地区〔常复数 flatlands〕',
 '不像起伏丘陵，地面延展开来总体较平坦的一片地方。',
 'flat 平坦 + land 土地、地区，合成地形名词。复数 flatlands 常指一大片平坦地区。',FH('flat + land → flatland','平坦的土地、地区'),
 'the coastal flatlands 沿海平原，open flatland 开阔平地，a flatland landscape 平原景观。',
 'the coastal flatlands；open flatland；a flatland landscape。',
 'flatland 平坦不保证 lowland 低海拔；高原上也可有相对平坦地面。',
 ('The road crossed miles of open flatland.','道路穿过数英里的开阔平地。'),('The coastal flatlands were covered in mist.','沿海平原笼罩在雾里。'))
R('B3046','平面、扁平；平淡、没气、直接和住房','FLAT：缺少凸起、起伏；公寓有楼层住处的旧路径','flat → flatter 比较级、flatten、flatness、flatly；flatmate 接公寓；flatbread、flatware、flatland、flatline 按用途与形象；已有 flatbed、flatiron、flatscreen 复用。',
 'flatter 奉承动词历史另辨，不能从现代比较级硬推；平坦与光滑、低海拔、没变化各有侧重点。',
 'flat + -er/-en 双写 t；flat + -ness/-ly/mate/bread/ware/land/line；flat 的公寓义有楼层词历史；flatter 动词细源有争议。',
 [['形状、比较、变化和方式','flat · flatter · flatten · flatness · flatly'],['居住与食品用品','flatmate · flatbread · flatware · flatbed · flatiron · flatscreen'],['地形与数据线','flatland · flatline']],
 'flat/smooth 平与滑不同；flatter 比较与奉承分开；flatmate 未必同卧室；flatbread不保证无发酵；flatline不一定跌到零。',
 'My flatmate flattened the dough to make flatbread.\n\n我的合租室友把面团擀平，做扁面包。','flat flatter flatten flatness flatly flatmate flatbread flatware flatbed flatiron flatscreen flatland flatline')
if __name__=='__main__':save('continuation_20261030_da',ROOTS,WORDS)
