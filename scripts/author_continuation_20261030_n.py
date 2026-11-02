"""Wood: material, woodland and practical compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
WO=[['古英语 wudu、widu → 中古英语 wode','树木、树林；木材'],['英语 wood','木头这种材料；一片树林']]
def H(f,m):return WO+[[f,m]]
W('wood','/wʊd/','木材、木头；树林',
 '站着长成一片是树林，取下来做桌椅、烧火的是木材；wood 可以从两面看同一种东西。',
 '继承古英语 wudu、widu，经中古英语延续。古词就同时涉及树木集合和木材，不必编成现代先有木板再变树林。',WO,
 'made of wood 木制的，a piece of wood 一块木头；a wood 或 the woods 一片树林。wood 作材料通常不可数，woods 作树林很常见。',
 'made of wood；a piece of wood；in the woods；out of the woods。',
 'tree 是单棵树，wood 是材料或林地。out of the woods 还可比喻脱离困境；wood 与 would 常同音，拼写、语法不同。',
 ('The bench is made of solid wood.','长椅由实木制成。'),('We followed a narrow path through the woods.','我们沿着窄路穿过树林。'),sources=['https://www.etymonline.com/word/wood','https://en.wiktionary.org/wiki/wood#English'])
W('wooden','/ˈwʊdən/','木制的；僵硬、不自然的',
 '桌椅真的由木头做；人的动作或表演像木头一样不灵活，就叫 wooden。',
 'wood + -en，-en 在此构成材料形容词。后来从木材性质比喻动作、声音或表情生硬。',H('wood + -en → wooden','由木头制成 → 僵硬、不自然'),
 'a wooden chair 木椅，a wooden spoon 木勺，a wooden performance 生硬表演。',
 'a wooden chair；a wooden spoon；a wooden expression。',
 'wooden 说明木制或僵硬，wooded 说一片地方树多；a wooden house 木屋，a wooded hill 树木覆盖的山。',
 ('She stirred the soup with a wooden spoon.','她用木勺搅汤。'),('His delivery sounded wooden and rehearsed.','他的表达听起来生硬，像排练过一样。'))
W('woody','/ˈwʊdi/','木质的；木质化的；有木香的',
 '植物的茎硬得像木头，或者闻起来带木材气息；强调木头般的性质。',
 'wood + -y，经中古英语同族形式延续；-y 描述性质。这里讲常用形容词，不收较偏的同形俚语名词。',H('wood + -y → woody','有木质结构、质感或木香'),
 'a woody stem 木质茎，a woody plant 木本植物，a woody scent 木质香气。老蔬菜变 woody 可说纤维硬、口感柴。',
 'a woody stem；woody plants；a woody scent。',
 'wooden 多说材料由木头制成，woody 常说结构、质感或香气。woody vegetables 通常是在批评口感老硬。',
 ('Remove the tough, woody ends of the stems.','去掉茎部老硬的末端。'),('The perfume has a warm, woody scent.','这种香水有温暖的木质香气。'))
W('wooded','/ˈwʊdɪd/','树木覆盖的；林木繁茂的',
 '一座山、一片地上长着许多树，绿荫铺满那个地方。',
 'wood + -ed，接中古英语相应形容词；-ed 在这里描述具有树木覆盖的状态，/d/ 后读 /ɪd/。',H('wood + -ed → wooded','长满树林、被树木覆盖的'),
 'a wooded valley 林木覆盖的山谷，a heavily wooded area 树木稠密地区。常描述土地环境。',
 'a wooded valley；wooded hills；a heavily wooded area。',
 'wooded 不是木头做的，wooden 才常说木制；a wooded garden 长树的花园不同于 wooden furniture 木家具。',
 ('The path leads into a wooded valley.','小路通往一个林木覆盖的山谷。'),('The house overlooks a heavily wooded hillside.','房子俯瞰一片树木茂密的山坡。'))
W('plywood','/ˈplaɪwʊd/','胶合板',
 '把多张薄木片叠起来粘牢，常让相邻层纹理换个方向，做成整张板。',
 'ply 层、薄片 + wood 木材；ply 经法语 pli 折层，最终接拉丁 plicare 折叠。不是 plain wood 的缩写。',H('ply〔层〕+ wood → plywood','薄木片胶合成多层板材'),
 'a sheet of plywood 一张胶合板，plywood panels 胶合板板材。它属于工程木材，不等于整块实木。',
 'a sheet of plywood；plywood panels；a plywood box。',
 'plywood 由木薄片分层粘合，particleboard 刨花板用木屑、颗粒等压合；两种材料结构不同。',
 ('They covered the opening with a sheet of plywood.','他们用一张胶合板盖住开口。'),('The shelves are made from plywood.','架子由胶合板制成。'),sources=['https://www.etymonline.com/word/plywood','https://en.wiktionary.org/wiki/plywood#English'])
W('woodworker','英 /ˈwʊdwɜːkə/；美 /ˈwʊdwɜːrkər/','木工；从事木作的人',
 '把木材锯、刨、接起来做成东西的人，重点在加工木头这门手艺。',
 'wood + worker，worker 是 work + -er。woodworking 木作活动已有精讲，woodworker 是做这件事的人。',H('wood + worker → woodworker','加工木材、制作木器的人'),
 'a skilled woodworker 熟练木工，an amateur woodworker 木作爱好者；既可职业，也可爱好。',
 'a skilled woodworker；an amateur woodworker；a local woodworker。',
 'woodworker 范围较宽，carpenter 常侧重建筑木工等实际职业，cabinetmaker 更侧重柜体家具制造。',
 ('A local woodworker made the oak cabinet.','一位本地木工做了这个橡木柜。'),('She is an amateur woodworker who builds toys.','她是一名制作玩具的业余木作爱好者。'))
W('woodcutter','英 /ˈwʊdkʌtə/；美 /ˈwʊdkʌtər/','伐木者；劈柴者；木刻制作者',
 '把木头砍下来或劈开的人；艺术语境也可以是刻木版的人。',
 'wood + cutter，cutter 是 cut + -er，t 双写。这里是从切、砍这个动作给人命名。',H('wood + cutter → woodcutter','砍木、劈柴的人；木刻制作者'),
 'a woodcutter’s axe 伐木者的斧头。童话里常见职业名；木刻艺术中的用法须看上下文。',
 'a woodcutter’s axe；a woodcutter in the forest；a skilled woodcutter。',
 'woodcutter 强调切砍木材，woodworker 强调加工制作，二者可能同一个人做，但词的着眼点不同。',
 ('The woodcutter split the logs before sunset.','劈柴者在日落前劈好了原木。'),('In the story, a woodcutter finds a child in the forest.','故事里，一个樵夫在森林中发现一个孩子。'))
W('woodcraft','英 /ˈwʊdkrɑːft/；美 /ˈwʊdkræft/','林野生活技能；木作、木雕技艺',
 'wood 指树林时，是在林子里辨路、扎营等本领；指木材时，则是动手做木器的手艺。',
 'wood + craft 技艺，两个 wood 义项支撑两种用法。需要从户外活动还是手工制作的语境判断。',H('wood + craft → woodcraft','林中技能；木材加工技艺'),
 'learn woodcraft 学林野生活技能，woodcraft skills 可依语境指户外本领或木作技巧。说明具体活动更清楚。',
 'woodcraft skills；learn woodcraft；a woodcraft course。',
 'woodcraft 不只等于 woodworking；前者在户外教育中也可讲林野技能，后者更明确加工木材。',
 ('The camp teaches woodcraft, including shelter building and navigation.','营地教授搭建庇护处、辨路等林野技能。'),('The workshop introduces woodcraft through simple carving projects.','工坊用简单雕刻项目介绍木作技艺。'))
W('woodshed','/ˈwʊdʃed/','柴棚；储木小屋',
 '把劈好的柴码在有顶的小棚里，避雨并留着取用。',
 'wood 木柴 + shed 棚屋，按储藏用途命名。口语还可比喻独自苦练，尤其音乐练习。',H('wood + shed → woodshed','存放木柴的小棚 → 另有独自练习的动词用法'),
 'stack logs in the woodshed 把原木堆在柴棚里。音乐人说 woodshed a piece，可指关起门来反复练一首曲子。',
 'a small woodshed；stack wood in the woodshed；the door of the woodshed。',
 'shed 可放多种杂物，woodshed 特指柴棚。日常先掌握实物义，不把所有 shed 都译成柴棚。',
 ('He stacked the dry logs in the woodshed.','他把干木柴码在柴棚里。'),('The old woodshed stands behind the kitchen.','旧柴棚位于厨房后面。'))
W('woodblock','/ˈwʊdblɒk/〔英〕；/ˈwʊdblɑːk/〔美〕','木版；木版印刷；木块打击乐器',
 '一块木头刻上图案，涂墨可以印画；做成共鸣木块、敲出声音，也能叫 woodblock。',
 'wood + block 块，印刷用木版和打击乐器是固定专业用法；woodcut 木刻已有精讲可对照。',H('wood + block → woodblock','木块 → 雕刻印版、木块打击乐器'),
 'woodblock printing 木版印刷，a woodblock print 木版画；play the woodblock 演奏木块打击乐器。',
 'woodblock printing；a woodblock print；play the woodblock。',
 'woodblock 与 woodcut 在版画语境常有重合；woodblock 作乐器并不表示这件乐器是一幅版画。',
 ('The artist carved the design into a woodblock.','艺术家把图案刻进木版。'),('The percussionist added a sharp rhythm on the woodblock.','打击乐手用木块乐器敲出清脆节奏。'))
W('woodpecker','英 /ˈwʊdpekə/；美 /ˈwʊdpekər/','啄木鸟',
 '鸟嘴笃笃敲树干，名字直接抓住它啄木头的动作。',
 'wood + pecker，pecker 是 peck 啄 + -er。现代名称按行为命名；不是只要啄过木头的鸟都属于这一类。',H('wood + peck + -er → woodpecker','啄木头的鸟 → 啄木鸟'),
 'a woodpecker on a tree 树上的啄木鸟，the tapping of a woodpecker 啄木鸟的敲击声。',
 'a woodpecker’s beak；a woodpecker on the trunk；hear a woodpecker。',
 'peck 是鸟嘴一下一下啄；pick 是挑选、捡起。woodpecker 的中段是 peck，不是 pick。',
 ('We heard a woodpecker tapping on a dead tree.','我们听见啄木鸟在枯树上笃笃地啄。'),('A woodpecker landed on the trunk outside the window.','一只啄木鸟落在窗外的树干上。'))
W('driftwood','/ˈdrɪftwʊd/','浮木；冲上岸的木头',
 '木头随水流漂，最后可能停在河滩或海滩上；名字里保留了这段漂流经历。',
 'drift 漂流 + wood，指水上漂的木头，也指漂后冲上岸的木头。',H('drift + wood → driftwood','随水漂流或被冲上岸的木头'),
 'pieces of driftwood 几块浮木，driftwood on the beach 海滩上的漂木。通常作为材料、集合名词使用。',
 'pieces of driftwood；collect driftwood；a driftwood sculpture。',
 'firewood 说烧柴用途，driftwood 说随水漂来的来源；两者不是按同一种标准命名。',
 ('The storm left piles of driftwood on the beach.','风暴过后，海滩上留下成堆漂木。'),('She made a small sculpture from driftwood.','她用漂木做了一件小雕塑。'))
W('sandalwood','英 /ˈsændlwʊd/；美 /ˈsændlwʊd/','檀香木；檀香树',
 '一种以木材香气闻名的树及其木材，常见于香料、香水或木制品描述。',
 'sandal〔檀香旧名〕+ wood；前部经中古拉丁、希腊、阿拉伯和波斯等传递，最终接梵语 candana 檀香。这里 sandal 不是凉鞋。',H('梵语 candana 经多种语言 → sandal〔檀香〕；另接 wood','檀香树、檀香木'),
 'a sandalwood scent 檀香气味，sandalwood carvings 檀香木雕。先识别材料与气味，不从名字推任何疗效。',
 'sandalwood oil；a sandalwood scent；sandalwood carvings。',
 'sandal 凉鞋的来源是另一条历史；sandalwood 的 sandal 指檀香，不能拆成做凉鞋的木头。',
 ('The room had a faint scent of sandalwood.','房间里有淡淡的檀香。'),('The box was carved from sandalwood.','盒子由檀香木雕成。'))
R('B2688','木材与树林；材质、覆盖、制作和自然复合词','WOOD：材料是一块木头，环境是一片树林','先 wood → wooden、woody、wooded；接胶合板与木工，再分储柴、印版、鸟类和漂木。',
 '古英语本来就兼有林地和木材义。许多木材名较专门先略；已有常用词条共享。wormwood 是旧植物名受民间词源改写，不作为 worm + wood 的真构词例。',
 'wood + -en/-y/-ed；ply/drift + wood；wood + worker/cutter/craft/shed/block/pecker。sandalwood 的前部是檀香旧名。',
 [['基本材料、材质与林地','wood · wooden · woody · wooded · woodland'],['木材类型','plywood · hardwood · softwood · redwood · heartwood · sandalwood'],['制作、人员与储藏','woodwork · woodworking · woodworker · woodcutter · woodcraft · firewood · woodshed'],['印刷、乐器及自然','woodcut · woodblock · woodwind · woodpecker · driftwood · deadwood']],
 'wooden 木制，wooded 树多，woody 木质或木香；hardwood/softwood 是植物来源分类，不一律按硬度判断。',
 'The woodworker made a wooden bench beside the wooded path.\n\n木工在林间小路旁做了一条木长椅。',
 'wood wooden woody wooded woodland plywood hardwood softwood redwood heartwood sandalwood woodwork woodworking woodworker woodcutter woodcraft firewood woodshed woodcut woodblock woodwind woodpecker driftwood deadwood')
if __name__=='__main__':save('continuation_20261030_n',ROOTS,WORDS)
