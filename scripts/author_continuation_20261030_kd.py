"""Shade and loop: physical images and modern uses."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['古英语 sceadu 等 → 中古英语 shade／schade','光被挡后的阴影、遮蔽处'],['颜色和细微程度的扩展','颜色深浅、不同色调；微妙区别'],['遮蔽、暗处的比喻与技术用途','shady 可疑；shader 参与图形计算；nightshade 固定植物名']]
W('shade','/ʃeɪd/','阴凉、阴影处；遮光物；色调、细微差别；遮蔽、涂阴影',
 '树挡住太阳，下面就是 shade；颜色因为明暗、深浅变化出现不同 shades。shade an area 也可说给图画局部涂阴影。',
 '承接古英语 sceadu 等形式，经中古英语 shade、schade。与 shadow 有共同历史，后来在遮蔽空间、投影轮廓等常用表达中分工。',S[:2],
 'sit in the shade 坐在阴凉处，a shade of blue 一种蓝色色调，shades of meaning 细微词义差别，shade your eyes 遮眼挡光。throw shade 是含讥讽、贬低的口语表达。',
 'in the shade；a shade of；shades of meaning；shade your eyes。',
 'shade 常看被遮蔽的空间、阴凉，shadow 常看物体投下的具体暗形。两者有关联但搭配不同；sunglasses 的口语 shades 又是复数固定用法。',
 ('We sat in the shade of a large tree.','我们坐在大树的树荫下。'),('The walls were painted in different shades of blue.','墙被涂成不同深浅的蓝色。'))
W('shady','/ˈʃeɪdi/','阴凉、多荫的；可疑、不正当的',
 '小路有树遮光，是 shady；生意像藏在暗处、不让人看清，又可以说 shady。后一义评价透明、可信程度。',
 'shade + -y，去末尾 e。由阴影、遮蔽性质扩到人物、交易等可疑的比喻。',S[:1]+[['shade + -y → shady','有荫、阴凉 → 不光明、可疑的评价']],
 'a shady path 树荫小路，a shady corner 阴凉角落，a shady deal 可疑交易，a shady character 可疑人物。',
 'a shady path；a shady corner；a shady deal。',
 'shady 形容地点常是舒服的阴凉，形容交易常是负面怀疑。一个人坐在树荫里不等于行为可疑。',
 ('The garden has a cool, shady corner.','花园有个凉爽的树荫角落。'),('The detective became suspicious of the shady deal.','侦探对那笔可疑交易起了疑心。'))
W('shader','英 /ˈʃeɪdə/；美 /ˈʃeɪdər/','着色器；进行遮蔽、着色的人或东西',
 '图形处理中，shader 像一套小计算规则，参与算出颜色、光照效果，也可处理位置等。它的工作范围比普通涂阴影更宽。',
 'shade + -er，去末尾 e。由遮蔽、着色的执行者、器具名，形成现代图形技术里的程序名称。',S[:2]+[['shade + -er → shader','着色执行者；图形处理中的程序类别']],
 'a pixel shader 像素着色器，a vertex shader 顶点着色器，a shader effect 着色器效果。不同类型在不同阶段处理数据，不只给表面随手盖一层颜色。',
 'a pixel shader；a vertex shader；a shader effect。',
 'shader 是程序、计算阶段相关名称，shading 是着色等处理过程。纹理 texture、材质 material 与 shader 有联系，但不是完全同一对象。',
 ('The shader makes the surface look like polished metal.','着色器让表面看起来像抛光金属。'),('The lesson compares a vertex shader with a pixel shader.','这课比较顶点着色器与像素着色器。'),sources=['https://en.wiktionary.org/wiki/shader#English','https://learn.microsoft.com/en-us/visualstudio/designers/working-with-shaders?view=visualstudio'])
W('nightshade','/ˈnaɪtʃeɪd/','龙葵、颠茄等植物俗名；茄科植物〔宽泛用法〕',
 '它是一个古老植物名称，后半看得到 shade，命名缘由却没有完全确定。不同完整名称所指不同：black nightshade 常是龙葵，deadly nightshade 是颠茄。',
 '古英语 nihtscada，经中古英语相关形式；对应 night + shade。或许联系深色果实等，但不能把这种猜测说成唯一确定历史。',S[:1]+[['古英语 nihtscada → nightshade','夜与阴影相关组合的固定植物名'],['现代不同范围','具体植物俗名；较宽时说茄科植物']],
 'black nightshade 龙葵，deadly nightshade 颠茄，the nightshade family 茄科。宽泛分类语境还包括番茄、马铃薯等不同成员。',
 'black nightshade；deadly nightshade；the nightshade family。',
 'nightshade 不只指同一个物种，也不是夜里一块树荫。名称、分类相近，不代表所有植物的成分、用途相同。',
 ('The botanist identified the plant as black nightshade.','植物学家认出那株植物是龙葵。'),('The chapter groups tomatoes and potatoes in the nightshade family.','这一章把番茄和马铃薯归入茄科。'),sources=['https://en.wiktionary.org/wiki/nightshade#English','https://www.etymonline.com/word/nightshade'])
R('B3856','光被遮后的空间、色调与细微变化，以及可疑比喻和技术、植物名称','SHADE：挡光后的暗与深浅变化，再分开看固定词义','shade → shady 物理阴凉或可疑评价；shader 图形计算；nightshade 古老植物名。',
 '同一画面能延伸到颜色、遮蔽和可信度，但固定植物名称还需要实际来源说明。',
 'sceadu 等 → shade；-y 性质、-er 执行者和程序；night + shade 的植物名在古英语已存在。',
 [['基础与性质','shade · shady'],['器具、技术与植物名','shader · nightshade · lampshade']],
 'shady 地点可舒服，shady deal 可疑；shader 比涂阴影范围宽；nightshade 不只一种植物。',
 'The shader renders a shady garden with several shades of green.\n\n着色器把阴凉花园渲染成多种深浅的绿色。','shade shady shader nightshade lampshade')
L=[['中古英语 loupe、loop 等','绳、布等弯回形成的圈、套'],['更早来源未定','有凯尔特语弯曲与古诺尔斯语奔跑、活结相关分析'],['现代沿圈返回的扩展','路线绕回；音乐、程序循环；成圈器具、动物形态名称']]
W('loop','/luːp/','环、圈、套；循环；使成圈、循环播放',
 '一根绳弯回来形成圈，是 loop；声音播完回到开头再播，程序做完一轮再回起点，也借同样的返回路线。',
 '中古英语已有 loupe 等圈、套形式。远源有凯尔特语弯曲、古诺尔斯语相关形式等分析，不能把某一条猜定为唯一来历。',L,
 'a loop of string 绳圈，a feedback loop 反馈回路，play on a loop 循环播放，keep someone in the loop 让某人及时知情。动词 loop 可绕圈、循环处理。',
 'a loop of string；a feedback loop；on a loop；in the loop。',
 'loop 看路径回到前面并可重复，circle 更直接说圆形。程序 loop 也不一定永远不停止，可以有结束条件。',
 ('She made a loop in the rope.','她把绳子绕成一个圈。'),('The short video played on a loop.','短视频循环播放。'),sources=['https://en.wiktionary.org/wiki/loop#English','https://www.etymonline.com/word/loop'])
W('loopy','/ˈluːpi/','有环、圈状的；古怪、糊涂、晕乎的〔口语〕',
 'loopy handwriting 是笔画绕圈的字；口语 I feel loopy 则可能说脑子晕乎、状态不清楚。不同用法不必都当真实转圈。',
 'loop + -y。有圈的字面义和古怪、糊涂等俚语用法各自固定；具体抽象路线不宜编成所有人都在脑内打圈的事实。',L[:1]+[['loop + -y → loopy','圈状性质；口语中古怪、糊涂的评价']],
 'loopy handwriting 绕圈的字迹，a loopy idea 古怪想法，feel loopy 觉得晕乎、糊涂。对人的评价可能带戏谑或贬义。',
 'loopy handwriting；a loopy idea；feel loopy。',
 'loopy 不等于 looping：looping animation 是循环动画，loopy animation 可能被理解为古怪、圈状的动画风格。',
 ('Her signature has large, loopy letters.','她签名的字母很大，绕着不少圈。'),('After the sleepless night, he felt a little loopy.','一夜没睡后，他有点晕乎。'))
W('looper','英 /ˈluːpə/；美 /ˈluːpər/','循环录放装置、程序；成圈器具；某些拱身爬行的蛾类幼虫',
 '音乐人录一小段，让它不断循环，再叠新声音，常靠 looper。自然界叫 looper 的幼虫，则因拱起身子、像套成圈那样爬而得名。',
 'loop + -er，可命名形成、执行循环的器具、程序，也可按成圈动作给动物命名。-er 不局限于人。',L+[['loop + -er → looper','成圈、循环的器具或按类似动作命名的动物']],
 'a loop pedal／looper 循环效果器，an audio looper 音频循环录放工具，a looper caterpillar 拱身爬行的蛾类幼虫。',
 'an audio looper；a looper pedal；a looper caterpillar。',
 'looper 的音乐设备与幼虫共享成圈、重复等命名联系，不是同一类物件。loop 是环或循环，looper 是相应执行者、器具等。',
 ('The guitarist used a looper to build several layers of sound.','吉他手用循环效果器叠出几层声音。'),('The looper caterpillar arched its body as it moved.','那条蛾类幼虫前进时拱起身体。'))
R('B4443','弯回成圈，到声音、程序和信息的循环与参与','LOOP：返回前面，形成圈或重复','loop → loopy 看圈状、俚语性质；looper 看循环器具或动物动作。',
 '绳圈是很直观的出发画面。循环播放、程序回路和让人及时知情的 in the loop，再分别看实际关系。',
 '中古英语 loupe 等 → loop；更早来源未定；-y 性质、-er 执行者和器具。',
 [['圈、循环与性质','loop · loopy'],['器具、程序与动物名','looper']],
 'loopy 不等于所有 looping；程序循环可以结束；in the loop 说及时知情。',
 'The musician used a looper to keep the melody playing on a loop.\n\n音乐人用循环效果器，让旋律不断循环播放。','loop loopy looper')
if __name__=='__main__':save('continuation_20261030_kd',ROOTS,WORDS)
