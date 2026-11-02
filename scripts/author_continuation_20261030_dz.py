"""Sand: material, abrasion, play, landforms, bird and sleep figure."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['古英语 sand → 中古英语 sand、sond → sand','沙、砂；本族继承词'],['现代用途、形状比喻','颗粒材料 → 铺撒、磨削；沙地景观、游戏及相关命名']]
def SH(f,m):return S[:1]+[[f,m]]
W('sand','/sænd/','沙、砂；用砂磨平；撒沙',
 '一粒粒很小、抓起来会从指缝漏走的材料；细硬颗粒能磨掉表面不平处，于是 sand 也能作打磨动词。',
 '继承古英语 sand，经中古英语多个形式到现代。由材料名发展出铺撒、打磨等动作，不能从 and 前面多一个 s 来拆义。',S,
 'fine sand 细沙，a grain of sand 一粒沙，sand the wood 打磨木头，sand a road 在路面撒沙。sand 常不可数，sands 可大片沙地、沙滩。',
 'fine sand；a grain of sand；sand the wood；sand a road。',
 'sand 颗粒材料，soil 土壤，dust 灰尘各有侧重；sand 动词打磨未必拿一把松沙直接擦，可用砂纸、相应工具。',
 ('The children played in the sand.','孩子们在沙里玩。'),('Sand the surface before painting it.','涂漆前先打磨表面。'))
W('sandy','/ˈsændi/','多沙的、含沙的；沙色的、浅黄褐色的',
 '海滩、土壤中沙很多；头发是浅黄褐色，也可借沙色叫 sandy，不是说头发里真落满了沙。',
 '古英语 sandiġ → 中古英语 sandi、sondy 等 → sandy，现代对应 sand + -y。颜色义借沙的典型浅黄褐印象。',SH('古英语 sandiġ → sandy；对应 sand + -y','有沙、含沙的；像沙一样的颜色'),
 'a sandy beach 沙滩，sandy soil 沙质土壤，sandy hair 浅黄褐色头发。',
 'a sandy beach；sandy soil；sandy hair。',
 'sandy 含沙或沙色，sand 动词打磨；sandy hair 不保证头发脏，也不是所有沙的颜色都完全相同。',
 ('The plants grow well in sandy soil.','这些植物在沙质土壤里长得很好。'),('He had sandy hair and bright blue eyes.','他头发浅黄褐，眼睛湛蓝。'))
W('sanding','/ˈsændɪŋ/','砂磨、打磨；撒沙；正在进行相应动作',
 '用细硬颗粒把粗表面一点点磨顺；道路作业中也能说在表面撒沙，两个动作都从 sand 的用途来。',
 'sand + -ing，中古英语已有相应动作名词。现代工序名不一定表示动作此刻正在发生，the sanding took an hour 是整个打磨过程。',SH('sand + -ing → sanding','打磨、撒沙的过程；相应分词'),
 'sanding the floor 打磨地板，sanding dust 打磨产生的粉尘，after sanding 打磨后。',
 'sanding the floor；sanding dust；after sanding。',
 'sanding 是磨削工序，painting 涂漆是另一工序；sander 工具，sanding 动作过程。',
 ('The table needs sanding before it is painted.','桌子上漆前需要打磨。'),('The sanding took longer than expected.','打磨所花时间比预期更长。'))
W('sander','英 /ˈsændə/；美 /ˈsændər/','砂磨机、打磨工具；打磨者、撒沙器等',
 '替你让砂纸、磨料持续运动来磨平表面的工具。-er 可以是工具，不必有一个人就叫撒沙人。',
 'sand 打磨、撒沙 + -er，按动作形成执行者、器具名。现代日常先掌握电动打磨工具。',SH('sand + -er → sander','进行打磨、撒沙的人或器具'),
 'an electric sander 电动砂磨机，a belt sander 砂带机，a handheld sander 手持打磨机。',
 'an electric sander；a belt sander；a handheld sander。',
 'sander 机器、sandpaper 砂纸，机器可带动砂纸工作；sandpit 里玩沙的孩子不因此都叫 sander。',
 ('She used an electric sander on the old table.','她用电动砂磨机打磨旧桌子。'),('The sander left the surface much smoother.','砂磨机让表面平滑多了。'))
W('sandcastle','英 /ˈsændkɑːsəl/；美 /ˈsændkæsəl/','沙堡',
 '把沙堆成城墙、塔楼一类形状，castle 的城堡概念接到材料 sand 上。可以很小，也可做得很复杂。',
 'sand + castle 城堡，材料名与造型名并列组合；castle 的 t 不单独读出。',SH('sand + castle → sandcastle','用沙塑成的城堡模型'),
 'build a sandcastle 堆沙堡，a sandcastle on the beach 沙滩上的沙堡，wash away a sandcastle 冲掉沙堡。',
 'build a sandcastle；a sandcastle on the beach；wash away a sandcastle。',
 'sandcastle 是造型作品，不等于 sandhill 自然或一般沙丘；城堡材料松散，不是实际防御建筑。',
 ('The children built a sandcastle near the water.','孩子们在水边堆了个沙堡。'),('A wave washed the sandcastle away.','一个浪把沙堡冲掉了。'))
W('sandpit','/ˈsændpɪt/','沙坑；儿童玩沙池；采沙坑',
 '有沙的一块坑、围出的区域，可以给孩子玩，也可在工程、地理语境中是取沙地点。',
 '古英语 sandpytt → 中古英语 sandpitte 等 → sandpit，现代对应 sand + pit 坑。复合词历史很早，不只现代游乐场才造。',SH('古英语 sandpytt → sandpit；对应 sand + pit','有沙的坑、取沙处 → 儿童玩沙区域等'),
 'play in the sandpit 在沙池里玩，a school sandpit 学校沙池，an old sandpit 旧采沙坑。',
 'play in the sandpit；a school sandpit；an old sandpit。',
 'sandpit 儿童设施英式常见，美式常说 sandbox；sandbox 软件隔离环境是同一沙盒词的后起比喻，不是 sandpit 全部场景都能照搬。',
 ('The children spent the afternoon in the sandpit.','孩子们下午一直在沙池里玩。'),('The path passed an old sandpit.','小路经过一个旧采沙坑。'))
W('sandhill','/ˈsændhɪl/','沙丘、沙质小山',
 '一处主要由沙构成的隆起，hill 指小山、丘；名称让你先看到材料与地形。',
 'sand + hill，合成沙质丘陵、沙丘名。也出现在 sandhill crane 沙丘鹤等名称，不能仅由一个动物名字推断它永远只住沙丘。',SH('sand + hill → sandhill','沙构成的丘、沙质小山'),
 'low sandhills 低矮沙丘，a path over the sandhill 越过沙丘的小路，among the sandhills 沙丘间。',
 'low sandhills；over the sandhill；among the sandhills。',
 'sandhill 沙质地形，sandcastle 人造沙堡；dune 常特指风等塑成的沙丘，不只一座 hill 含沙就能推断同样形成机制。',
 ('The path wound among low sandhills.','小路在低矮沙丘间蜿蜒。'),('We climbed the sandhill to see the sea.','我们爬上沙丘去看海。'))
W('sandpiper','英 /ˈsændpaɪpə/；美 /ˈsændpaɪpər/','鹬类小涉禽〔多种鸟的常用名称〕',
 '常在岸边、浅水边走动觅食的小涉禽；piper 借鸣声像细管发出的尖细音来命名，不是真的带着一根笛子。',
 'sand 沙、沙岸 + piper 吹管者，借栖息环境与鸣声组合成鸟名。它是一组常用鸟名材料，不当所有沙滩鸟的总称。',SH('sand + piper → sandpiper','沙岸活动、发出管音般鸣声的鸟名'),
 'a sandpiper on the shore 岸边的鹬，a flock of sandpipers 一群鹬，sandpipers feeding in shallow water 浅水觅食的鹬类。',
 'a flock of sandpipers；sandpipers on the shore；a small sandpiper。',
 'sandpiper 鹬类涉禽，seagull 海鸥不同；常用名有多种，准确识别看完整种名与外形。',
 ('A small sandpiper ran along the water’s edge.','一只小鹬沿水边跑动。'),('We watched sandpipers feeding in the shallow water.','我们看着鹬类在浅水中觅食。'))
W('sandman','/ˈsændmæn/','睡魔、带来睡意的撒沙人〔民间传说〕',
 '故事说他往眼睛撒沙让人犯困，像眼睛累时有沙粒、想揉眼的感觉；这是民间形象，不是睡眠的实际生理解释。',
 '现代材料为 sand + man，人物形象有欧洲民间传说背景，德语 Sandmann 等也参与传播。不同作品细节不同，不强定一个唯一的最初故事。',SH('sand + man；欧洲民间传说中的相应人物 → sandman','撒沙带来睡意的虚构人物'),
 'the Sandman 睡魔，a story about the Sandman 睡魔故事，the Sandman is coming 睡意来了〔童话式表达〕。',
 'the Sandman；a story about the Sandman；the Sandman is coming。',
 'sandman 传说人物，sander 现代常打磨机；作品同名人物可能另有设定，不能把所有版本都当同一剧情。',
 ('The bedtime story featured the Sandman.','睡前故事里出现了睡魔。'),('“The Sandman is coming,” she said as the child yawned.','孩子打哈欠时，她说：“睡魔要来了。”'),
 sources=['https://en.wiktionary.org/wiki/sandman#English','https://www.etymonline.com/word/sandman'])
R('B3111','颗粒材料、磨削用途与沙地形象','SAND：松散小颗粒，既能塑形、铺撒，也能一点点磨平','sand → sandy；sanding、sander、sandpaper 归打磨；sandcastle、sandpit、sandbox 归玩沙；地形、鸟名、睡魔分开看。',
 'sand 动词可打磨而非只撒沙；sandy hair 是颜色。沙丘、沙堡、鹬和睡魔不是把两段中文机械相加就够，要看命名形象。',
 '古英语 sand → sand；sandiġ → sandy；sand + -ing/-er；sand + castle/pit/hill/piper/man 等；sandpit 保留古英语旧组合。',
 [['基础和打磨','sand · sandy · sanding · sander · sandpaper'],['玩沙与场地','sandcastle · sandpit · sandbox · sandlot'],['地貌、材料与天气','sandhill · sandstone · sandbar · sandbank · sandstorm · quicksand · sandbag'],['鸟与民间人物','sandpiper · sandman']],
 'sanding 工序、sander 工具；sandcastle 沙堡、sandhill 地形；sandpiper 非所有岸鸟；sandman 虚构人物非睡眠机制。',
 'The children built a sandcastle in the sandpit.\n\n孩子们在沙池里堆沙堡。','sand sandy sanding sander sandpaper sandcastle sandpit sandbox sandlot sandhill sandstone sandbar sandbank sandstorm quicksand sandbag sandpiper sandman')
if __name__=='__main__':save('continuation_20261030_dz',ROOTS,WORDS)
