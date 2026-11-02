"""Tubes versus tubers, providing resources and sliding motion."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['拉丁 tubus → 法语 tube → 英语 tube','空心圆管，联系 tuba 号管等词'],['英语具体形状和命名','软管包装、地铁隧道、器材等'],['另源拉丁 tūber → tuber','隆起、肿块 → 膨大的植物贮藏器官']]
W('tube','英 /tjuːb/；美 /tuːb/','管子、管状物；软管包装；伦敦地铁〔the Tube〕',
 '一根中间空、能让东西通过或装进东西的长圆管；牙膏挤压包装和地铁隧道都借这种形状得名。',
 '借法语 tube，接拉丁 tubus 管。伦敦 the Tube 源于管状隧道的称呼，不是所有城市地铁都惯叫同一个专名。',T[:2],
 'a metal tube 金属管，a tube of toothpaste 一管牙膏，a test tube 试管，take the Tube 坐伦敦地铁。英式 tube 也常发 /tʃuːb/。',
 'a metal tube；a tube of toothpaste；a test tube；the Tube。',
 'tube 常强调管形、管状容器，pipe 常突出输送管路，二者有交叠。YouTube 是专名，不能据此把每个视频都叫一个 tube。',
 ('The liquid flows through a narrow tube.','液体流过一根细管。'),('I bought a tube of toothpaste.','我买了一管牙膏。'))
W('tubing','英 /ˈtjuːbɪŋ/；美 /ˈtuːbɪŋ/','管材、管路；乘充气内胎漂流或滑行',
 '供应商卖的是一段段管材；旅游活动里的 tubing 则是人坐在充气圈上，顺水或雪坡滑行，tube 指的物件换了。',
 'tube 去 e + -ing。可形成材料集合名词，也可命名使用充气内胎进行的活动，不一律是正在装管。',T[:2]+[['tube + -ing → tubing','管材、管路；使用充气圈的滑行活动']],
 'plastic tubing 塑料管材，rubber tubing 橡胶管，a length of tubing 一段管子，river tubing 充气圈漂流。',
 'plastic tubing；rubber tubing；a length of tubing；river tubing。',
 'tubing 作管材通常不可数，数一段可用 a length of tubing；活动义不等于乘船 rafting 的每种形式。',
 ('The machine uses flexible plastic tubing.','机器使用柔韧的塑料管路。'),('The brochure lists river tubing as one of the activities.','宣传册把充气圈漂流列为一项活动。'))
W('tubal','英 /ˈtjuːbəl/；美 /ˈtuːbəl/','管的、管道的，尤指身体管状结构',
 'tube 是那根管，tubal 是和那根管有关的性质；在解剖语境，身体也有运送物质、连接部位的管状结构。',
 'tube + -al，去掉末尾 e 再接性质词尾。它常用于解剖名称，具体是哪一管由上下文决定。',T[:2]+[['tube + -al → tubal','管状结构相关的']],
 'tubal anatomy 管道解剖，tubal function 管道功能，tubal pregnancy 输卵管妊娠这一专门医学名词。',
 'tubal anatomy；tubal function；tubal structure。',
 'tubal 不单凭词尾就限定所有场合都是输卵管，也不等于 tuber 块茎的。先找文本正在讨论哪种管。',
 ('The lecture introduced basic tubal anatomy.','讲座介绍了基本的管道解剖。'),('The model shows a tubal structure with an opening at each end.','模型展示了两端都有开口的管状结构。'))
W('tubeless','英 /ˈtjuːbləs/；美 /ˈtuːbləs/','无内胎的；没有管子的',
 '轮胎里省去独立那层充气内胎，靠相应胎体、轮圈等结构保持气密；不是外胎、空气都没了。',
 'tube + -less，无、没有。轮胎用法里的 tube 特指 inner tube 内胎，必须补回省掉的对象。',T[:2]+[['tube + -less → tubeless','无管的；轮胎语境无独立内胎的']],
 'tubeless tyres 无内胎轮胎，a tubeless setup 无内胎配置，tubeless wheels 适配无内胎方案的车轮。',
 'tubeless tyres；a tubeless setup；tubeless wheels。',
 'tubeless 不等于 airless 无气，也不保证永不扎破。构词只告诉你没有独立内胎，不包办全部性能。',
 ('The bicycle is fitted with tubeless tyres.','这辆自行车装了无内胎轮胎。'),('The review compares tubeless tyres with tyres that use inner tubes.','评测比较了无内胎轮胎与使用内胎的轮胎。'))
W('nanotube','英 /ˈnænəʊtjuːb/；美 /ˈnænoʊtuːb/','纳米管',
 '把空心管的形状缩到纳米尺度；常见碳纳米管，但管状微结构不只用碳做。',
 'nano- 纳米尺度 + tube 管。nano- 在单位中表示十亿分之一，名称强调尺度，不要求所有纳米管的直径都恰好一纳米。',T[:2]+[['nano- + tube → nanotube','纳米尺度的管状结构']],
 'a carbon nanotube 碳纳米管，nanotube structures 纳米管结构，a nanotube sample 纳米管样品。',
 'a carbon nanotube；nanotube structures；a nanotube sample。',
 'nanotube 不等于缩小版普通塑料水管；微观材料和结构决定其性质。nano- 说量级，不说明材料、长度或用途都一样。',
 ('The diagram shows a carbon nanotube.','图中展示了一根碳纳米管。'),('Researchers compared nanotubes made from different materials.','研究人员比较了不同材料制成的纳米管。'))
W('tuber','英 /ˈtjuːbə/；美 /ˈtuːbər/','块茎；膨大贮藏器官、结节等',
 '想植物把养分攒进一个鼓起来的地下部分；土豆就是常见块茎。核心是膨大，不是空心管。',
 '植物、解剖名词来自拉丁 tūber 隆起、肿块。这一常用义不是 tube + -er；另有较少见 tube 行为者同形词，需分源。',T[2:]+[['英语植物、解剖用法','膨大的贮藏部位；结节状突出结构']],
 'a potato tuber 土豆块茎，underground tubers 地下块茎，tuber growth 块茎生长。土豆块茎是膨大茎，不能把所有地下贮藏器官都叫根。',
 'a potato tuber；underground tubers；tuber growth。',
 'tuber 与 tube 的常用来源不同；bulb 鳞茎也不是 tuber 的任意同义词。洋葱、土豆长在地下，却有不同结构。',
 ('Each potato plant produced several tubers.','每株马铃薯长出了几个块茎。'),('The class compared a potato tuber with an onion bulb.','课堂比较了马铃薯块茎和洋葱鳞茎。'),sources=['https://en.wiktionary.org/wiki/tuber#English','https://www.etymonline.com/word/tuber'])
R('B3500','空心管路线，与植物块茎的膨大路线分开','TUBE：空心的管；TUBER：膨大的块，别硬接','tube → tubing/tubal/tubeless/nanotube；tuber 植物义来自另一拉丁名词。',
 '管形和膨大形恰好相反，摆在一起更容易识别。无内胎是少了一层特定内胎，纳米管是指定尺度，两者都须补清限定对象。',
 'tubus → tube；tube 去 e 加 -ing/-al，接 -less；nano- + tube。另线 tūber 隆起 → tuber。',
 [['管、材料与相关性质','tube · tubing · tubal'],['没有内胎和微观尺度','tubeless · nanotube'],['形似字母、另源块茎','tuber']],
 'tuber 不由空心管加人物后缀而来；tubing 材料常不可数；tubeless 不等于无气；nano- 不保证直径恰好一纳米。',
 'The display placed a potato tuber beside a model of a nanotube to contrast their shapes.\n\n展台把土豆块茎放在纳米管模型旁，对比两者的形状。','tube tubing tubal tubeless nanotube tuber')
W('resourcing','英 /rɪˈzɔːsɪŋ/；美 /ˈriːsɔːrsɪŋ/','资源配置、提供所需资源',
 '不只说有个好计划，还要给它人手、钱、设备和时间；把这些安排到位，就是 resourcing。',
 'resource 的动词用法去 e + -ing。名词 resource 资源转成提供资源的动词后，再形成过程名词。',
 [['resource 名词 → resource 动词','可利用资源 → 为某事提供资源'],['resource + -ing → resourcing','资源的供给、安排、配置']],
 'project resourcing 项目资源配置，adequate resourcing 充足资源保障，staff resourcing 人手配置。',
 'project resourcing；adequate resourcing；staff resourcing。',
 'resourcing 不只采购实物，也包含人员、经费等；resourceful 足智多谋强调善用办法，不保证资源本来充足。',
 ('The plan failed because of poor resourcing.','计划因资源保障不足而失败。'),('The meeting focused on staffing and resourcing for the project.','会议重点讨论项目的人手和资源配置。'))
R('B4439','可利用的资源、提供资源与善用办法','RESOURCE：有东西可调用，还要安排到位','resource → resourcing 配置；resourceful 善于想办法、利用可用条件。',
 '有资源、给资源和会用资源是三层意思。人手紧缺时仍能足智多谋，但不能拿一句聪明解决所有资源缺口。',
 'resource 名词转动词；resource + -ing → resourcing；resource + -ful → resourceful。',
 [['资源、配置与能力','resource · resourcing · resourceful']],
 'resourcing 不只实物；resourceful 不是资源很多的简单同义词。',
 'The resourceful manager still needed adequate resourcing.\n\n足智多谋的经理仍需要充足资源保障。','resource resourcing resourceful')
S=[['古英语 slīdan → slide','贴着表面滑动'],['名词、器具及展示','滑梯、滑动部件、投影片及演示页'],['相关旧动词与组合','slidrian 等 → slither；mud + slide → mudslide']]
W('slide','/slaɪd/','滑动、悄悄放入；逐渐下滑；滑梯；幻灯片、演示页；载玻片',
 '脚贴着冰面滑，手把纸悄悄推过去，都没有大幅抬起来；数字或状态慢慢滑向更低处，也能 slide。',
 '接古英语 slīdan。名词发展出滑梯、滑动部件与投影片等，现代 slide 也表示演示文稿中的一页；过去式、分词 slid /slɪd/。',S,
 'slide on ice 在冰上滑，slide a note across the desk 把纸条推过桌面，a playground slide 儿童滑梯，a presentation slide 演示页，a microscope slide 显微镜载玻片。',
 'slide on ice；slide a note；a presentation slide；a microscope slide。',
 'slide 是一页，slide deck 是整套页；let it slide 常指暂不追究，不是真让东西滑走。a slide in sales 是销量下滑，不是销售幻灯片。',
 ('She slid the note across the table.','她把纸条沿桌面推过去。'),('The final slide summarizes the main points.','最后一页演示概括了要点。'))
W('slider','英 /ˈslaɪdə/；美 /ˈslaɪdər/','滑块、滑动控件；拉链头；小汉堡；滑球〔依语境〕',
 '音量条上能来回滑的把手是 slider；拉链上滑过去让齿闭合的部件也是。菜单上 sliders 却常是小汉堡。',
 'slide 去 e + -er，给会滑动的部件、角色命名；界面控件从实体滑动控制件抽象而来。小汉堡、体育滑球是固定用法，不逐字硬推。',S+[['slide + -er → slider','滑动部件、控制件等'],['不同场景固定词义','小汉堡；棒球等运动的滑球']],
 'a volume slider 音量滑块，move the slider 拖动滑块，a zip slider 拉链头，mini sliders 小汉堡。',
 'a volume slider；move the slider；a zip slider；sliders on the menu。',
 'slider 不必是滑的人；slide 演示页也不是 slider。菜单叫 slider，不说明汉堡真的会滑来滑去。',
 ('Move the slider to adjust the volume.','移动滑块调节音量。'),('The café serves three small sliders on one plate.','咖啡馆把三个小汉堡装在同一盘上供应。'))
W('slither','英 /ˈslɪðə/；美 /ˈslɪðər/','滑行、蜿蜒爬行；滑着移动',
 '蛇贴着地面，身子左右摆动地往前走；人在泥坡上失去抓地，也可能 slither 下去。',
 '接古英语 slidrian、中古英语 slitheren 等滑行动词，是 slide 相关旧动词一路的变化。后半联系反复动作词尾，不是现代 slider 人物词随意换几个字母。',S[:1]+[['slidrian/slideren → slitheren → slither','连续滑、扭动着滑行；词中辅音、元音历史变化']],
 'slither through the grass 穿草蜿蜒而行，slither down a slope 滑下坡，slither away 滑行离开。',
 'slither through；slither down；slither away。',
 'slither 常强调贴地、左右扭动，slide 更广指滑动；蛇以外的动物、人或物也可按动作使用。',
 ('The snake slithered into the grass.','蛇蜿蜒滑进草丛。'),('We slithered down the muddy bank.','我们沿着泥泞的河岸坡滑了下去。'))
W('mudslide','/ˈmʌdslaɪd/','泥流、泥石流式滑塌；同名鸡尾酒〔菜单义〕',
 '坡上的泥土含水后成片往下滑、流动，名字直接把材料 mud 和运动 slide 合起来。',
 'mud 泥 + slide 滑。地质词指泥质物沿坡下移；酒单的同名饮品是另一场景的名称，不用于判断灾害类型。',S+[['mud + slide → mudslide','含泥物质沿坡下移的事件']],
 'a mudslide after heavy rain 暴雨后的泥流，a road blocked by a mudslide 被泥流堵住的道路。',
 'a mudslide after heavy rain；a road blocked by a mudslide。',
 'landslide 是更广的斜坡物质下移，mudslide 强调泥质、流动性；新闻中文有时笼统译泥石流，精细地质分类仍要看具体材料和过程。',
 ('Heavy rain triggered a mudslide on the hillside.','暴雨引发了山坡上的泥流。'),('The road was closed after a mudslide blocked it.','泥流堵路后，道路被关闭。'))
R('B2980','贴面滑动，及器具、下降和泥流的扩展','SLIDE：贴着表面动，或像那样逐渐往下','slide → slider；slither 是相关旧动词的蜿蜒滑行；mudslide、landslide 看下移材料；slideshow 连续展示演示页。',
 '从动作分名词：滑梯让人滑，控件可滑动，演示页又固定成展示材料。别因词形近就把所有 -er 都看成人。',
 'slīdan → slide/slid；slide + -er；slidrian 等 → slither；mud/land + slide；slide + show。',
 [['动作、部件与蜿蜒滑行','slide · slider · slither'],['材料下移与展示组合','mudslide · landslide · slideshow']],
 'slide 一页、deck 一套；slider 可是控件或小汉堡；slither 后半不是现代人物后缀；mudslide 不涵盖所有山体滑坡。',
 'The final slide shows how the mudslide moved down the slope.\n\n最后一页演示展示了泥流怎样沿坡下移。','slide slider slither mudslide landslide slideshow')
if __name__=='__main__':save('continuation_20261030_ig',ROOTS,WORDS)
