"""Common direction words in -ward and useful -ial/-ent adjectives."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
Wa=[['古英语 -weard、-weardes 等','朝某个方向；日耳曼语方向词尾'],['现代 -ward、-wards','朝……；也用于描述相应方向、趋势']]
W('toward','英 /təˈwɔːd/；美 /tɔːrd/，另有读法','朝、向；对……；有助于、接近某目标',
 '朝车站走，是 toward the station；钱放到实现目标的方向上，是 money toward a goal；态度也可以朝某个人表现出来。',
 '延续古英语 toweard，由 to 与 -weard 朝向的材料构成；现代常作介词，不应每次把它机械拆回不定式 to。',
 [['古英语 to + -weard → toweard','朝向；还曾有其他形容词义'],['现代 toward','朝、对；贡献到某个目标或用途']],
 'walk toward the door 朝门口走；attitude toward someone 对某人的态度；work toward a goal 朝目标努力。',
 'toward the end；toward a goal；attitude toward。',
 'toward 与 towards 通常意义相同，美式较常 toward，英式较常 towards，但不是地区间绝对禁用；go toward 不保证最后已经到达。',
 ('She walked toward the station.','她朝车站走去。'),('The money will go toward repairing the roof.','这笔钱将用于修缮屋顶。'))
W('onward','英 /ˈɒnwəd/；美 /ˈɑːnwərd/','继续向前；往后的、继续前往的',
 '已经走到这一步，接着往前，不倒回去，就是 onward；也能把空间往前换成时间往后。',
 'on 继续、向前的材料 + -ward；现代可作副词，也可作形容词，如 onward journey。',Wa+[['on + -ward → onward','继续前进；往后、下一程']],
 'move onward 继续前进；from Monday onward 从周一起往后；an onward journey 下一程旅途。',
 'from now onward；an onward journey。',
 'onwards 常作副词；作前置形容词通常 onward，如 onward travel，不随意写 onwards travel。',
 ('From that day onward, they kept in touch.','从那天起，他们一直保持联系。'),('We arranged our onward journey to the coast.','我们安排了接下来前往海岸的行程。'))
W('inward','英 /ˈɪnwəd/；美 /ˈɪnwərd/','向内；内在的、内心的',
 '门朝屋里开，是 inward；目光不往外看，而去看自己的感受、动机，也可说 turn inward。',
 '延续古英语 inweard，in 里面 + -ward 朝向；形容词和副词都可用，不只是地点名词内部。',Wa+[['in + -ward → inward','向内；引申为内心、内在']],
 'an inward movement 向内运动；inward feelings 内心感受；inward investment 从外部流入本地区的投资。',
 'turn inward；an inward flow。',
 'inward 强调朝内、内在的方向或感受；inner 更常说内部位置、深处。inwards 常作副词，不直接替换所有 inward 形容词用法。',
 ('The door opens inward.','门向里开。'),('The experience prompted her to turn inward and reflect.','这段经历促使她转向内心、认真反思。'))
W('untoward','英 /ˌʌntəˈwɔːd/；美 /ˌʌntəˈwɔːrd/','不利、意外出问题的；不妥的',
 '原本希望顺顺当当，结果冒出不好的意外，就是 something untoward。常见 nothing untoward happened，表示没出什么不好的岔子。',
 'un- 不 + toward 的旧形容词义；toward 早有温顺、愿意配合等义，untoward 有不愿顺从、难引导的旧义，再走到不利、出问题。不是现代介词 toward 的简单反义介词。',
 [['toward 的旧形容词用法；un- + toward','温顺、愿意；不顺从、难引导'],['现代 untoward','不利、意外不妥、出岔子的']],
 'nothing untoward 没什么不妥；an untoward incident 不好的意外事件；较正式。',
 'anything untoward；an untoward event。',
 'untoward 不是任何 unexpected 意外都适用；意外收到好礼物通常不叫 an untoward event，因为缺少不利、不妥的色彩。',
 ('Nothing untoward happened during the journey.','旅途中没出什么岔子。'),('The inspection found no evidence of anything untoward.','检查没有发现任何不妥之处的证据。'),sources=['https://en.wiktionary.org/wiki/untoward#English','https://www.etymonline.com/word/untoward'])
To=[['拉丁 torrens、torrent- → 法语等相应形式','奔腾、汹涌的水流；词族还关联烘烤、炽烈等材料'],['英语 torrent → torrential','急流、大量涌来；倾泻般的']]
W('torrent','英 /ˈtɒrənt/；美 /ˈtɔːrənt/ 或 /ˈtɑːrənt/','急流；奔流；大量涌来的事物',
 '不是一点点滴，而是一大股水猛冲下来，是 a torrent；骂声、消息一下涌来，也像水流一样。',
 '经法语、意大利语等相应形式接拉丁 torrens、torrent-。历史形容词有汹涌、猛烈等义，不是今天 tor 山丘 + rent 租金的组合。',To,
 'a torrent of water 一股急流；a torrent of criticism 一片猛烈批评；torrents of rain 倾盆大雨。',
 'a torrent of；torrents of rain。',
 'torrent 是猛烈奔流；stream 更一般说流。网络里的 torrent 还有特定文件共享语境，不从普通急流义推定每一种技术细节。',
 ('Rain turned the narrow stream into a torrent.','雨把狭窄溪流变成了急流。'),('The decision drew a torrent of criticism.','这个决定招来了一片猛烈批评。'))
W('torrential','/təˈrenʃl/','倾泻般的；湍急猛烈的',
 '雨下得像一股股水往下倒，最常说 torrential rain；不是任何小雨都配这个强度词。',
 'torrent + -ial → torrential。字形能看见 torrent，整词的重音、末段读音会变，按完整音标记。',To,
 'torrential rain 倾盆大雨；torrential downpours 暴雨。',
 'torrential rain；torrential downpours。',
 'torrential 强调水流、降雨猛烈；frequent rain 只说下雨频繁，频繁也可能每次都很小。',
 ('The match was cancelled because of torrential rain.','比赛因倾盆大雨取消。'),('Torrential downpours flooded the streets.','暴雨淹了街道。'))
W('jovial','英 /ˈdʒəʊviəl/；美 /ˈdʒoʊviəl/','快活友善的；开朗愉快的',
 '一进门就热情说笑，让周围也松快起来，这种开心、好相处的气氛或人可叫 jovial。',
 '经法语、意大利语或晚期拉丁 Iovialis 的材料，原与 Jupiter、Jove 木星、朱庇特相关。旧占星观念认为受木星影响者乐观开朗，因而发展出快活义；这是词义历史，不是性格的科学解释。',
 [['拉丁 Iov- 等 + -alis → Iovialis','与朱庇特、木星有关的'],['欧洲语言 jovial 等 → 英语 jovial','受旧占星性情观念影响，走向快活友善']],
 'a jovial host 快活热情的主人；a jovial mood 欢快心情。',
 'a jovial manner；a jovial laugh。',
 'jovial 是开朗快活，juvenile 是少年、幼稚的；相近开头不代表同一意思。它也不是 joy 后面直接加 vial。',
 ('Our jovial host greeted everyone with a joke.','快活热情的主人用一个笑话迎接大家。'),('The meeting ended in a jovial mood.','会议在轻松愉快的气氛中结束。'),sources=['https://en.wiktionary.org/wiki/jovial#English','https://www.etymonline.com/word/jovial'])
Fl=[['萤石 fluorspar 的命名材料 + -escence → fluorescence','斯托克斯于十九世纪据萤石等现象命名荧光'],['fluor- + -escent → fluorescent；现代也可与 fluoresce + -ent 对照','具有荧光的；相关现代词形不等于较短动词必先出现']]
W('fluorescence','/fləˈresns/，也有较完整首音节读法','荧光；荧光现象',
 '用合适光线照到某些材料，它们吸收能量后又发出光，看起来颜色特别亮。普通荧光的发光通常在激发停止后很快消退。',
 '斯托克斯于 1852 年以 fluorspar 萤石的材料加 -escence 命名，类比 phosphorescence。不能把它讲成普通英语 fluoresce 一定先有，再临时加 ence 的唯一历史。',Fl,
 'fluorescence under ultraviolet light 紫外光照射下的荧光；fluorescence intensity 荧光强度。',
 'fluorescence microscopy；fluorescence intensity。',
 'fluorescence 与 phosphorescence 磷光的持续时间、机制不同；不是所有黑暗中发光都叫荧光，也不表示材料自身一定是元素氟。',
 ('The mineral showed fluorescence under ultraviolet light.','矿物在紫外光下显出荧光。'),('The experiment measured changes in fluorescence intensity.','实验测量了荧光强度的变化。'),sources=['https://en.wiktionary.org/wiki/fluorescence#English','https://www.etymonline.com/word/fluorescence','https://goldbook.iupac.org/terms/view/F02453','https://www.oxfordlearnersdictionaries.com/definition/english/fluorescence'])
W('fluorescent','/fləˈresnt/，也有 /flʊəˈresənt/ 等读法','荧光的；颜色鲜亮显眼的',
 '荧光灯利用这种发光现象；衣服、标记上的 fluorescent yellow 则常说特别醒目的荧光黄。要看是在谈光学性质还是日常颜色。',
 '1853 年已有斯托克斯使用的 fluorescent，以 fluor- 与 -escent 构词；现代也能与 fluoresce 发荧光 + -ent 对照，但不把现代拆法当作历史出现顺序。',Fl,
 'a fluorescent lamp 荧光灯；fluorescent paint 荧光涂料；fluorescent yellow 荧光黄。',
 'fluorescent lighting；fluorescent colours。',
 'fluorescent 荧光与 reflective 反光不同：反光材料主要把入射光反射回去，不能所有亮色、反光条都只凭外观认成同一种材料。',
 ('The room was lit by fluorescent lamps.','房间用荧光灯照明。'),('She marked the route with fluorescent yellow tape.','她用荧光黄胶带标记路线。'),sources=['https://en.wiktionary.org/wiki/fluorescent#English','https://www.etymonline.com/word/fluorescent','https://www.oxfordlearnersdictionaries.com/definition/english/fluorescent','https://goldbook.iupac.org/terms/view/F02453'])
W('resplendent','/rɪˈsplendənt/','灿烂耀眼的；华丽夺目的',
 '礼服、宫殿、金色树叶亮得让人眼前一亮，较文学地赞它华丽灿烂，可以说 resplendent。',
 '接拉丁 resplendere 闪耀、反照与相应分词材料，re- 在这里不能机械限定为又一次，splend- 关联发光。现代末尾 -ent 对应形容词用法，不找一个常用 resplend 来强记。',
 [['拉丁 splendere、resplendere 等','发亮、闪耀、反照'],['英语 resplendent','灿烂、华丽夺目的']],
 'resplendent in gold 身着金色服装、装饰而华丽夺目；resplendent autumn colours 灿烂秋色。',
 'resplendent in；look resplendent。',
 'resplendent 常是较文学的华丽赞美；fluorescent 说荧光性质或鲜亮颜色，不是同一种光学概念。',
 ('The hall was resplendent with flowers and lights.','大厅鲜花与灯光交映，华丽夺目。'),('She arrived resplendent in a deep blue gown.','她穿着深蓝礼服到来，光彩照人。'))
R('A1793','朝某个方向；某种倾向','-WARD：把方向、目标摆在前面','inward 向内；onward 继续向前；homeward 朝家；skyward 朝天空。像给运动或目光安上一支朝向目标的箭头。',
 '不只说走路。an inward movement 是向里移动，an upward trend 是上升趋势；from that day onward 把方向挪到时间线上。toward 已常作介词，untoward、awkward 等则经过旧义发展，不能只按今天字面算意思。',
 '来自古英语 -weard、-weardes 等日耳曼语方向材料，较远与转向的词族相关；现代常见 -ward、-wards 变体。作副词时 forward／forwards、inward／inwards 等可因地区习惯不同；作前置形容词常用无 s 形式，如 an inward movement、an onward journey。医院 ward、guard 守护等词不能仅凭相同拼写就全部当作本后缀来解释。',
 [['朝向与继续前进','toward · towards · onward · onwards'],['向内、向外','inward · inwards · outward'],['上下、前后','forward · backward · downward · upward'],['朝地点、方位','homeward · skyward · eastward · northward · southward · seaward'],['旧义发展出的固定词','untoward · awkward · wayward']],
 'toward 不保证已经到达；toward／towards 通常同义；onward 作形容词时一般不加 s；untoward 常指不好的意外，不是所有惊喜；awkward 不能只硬译为朝 awk。',
 'The group moved onward while the wind pushed the clouds eastward.\n\n队伍继续前进，风把云推向东方。',
 'toward towards onward onwards inward inwards untoward forward awkward backward downward upward outward eastward northward wayward southward windward homeward skyward leeward seaward rearward rightward landward leftward')
R('A2121','与……有关；具有相应性质','-IAL：把相关领域、对象或性质连起来','finance／financial 金融、财务相关；torrent／torrential 像急流倾下；jovial 则有木星与旧占星观念的历史，不能硬拆成 joy。',
 '先看它与哪个词、哪个领域连着。financial plan 是财务计划，presidential election 是总统选举，torrential rain 是倾盆雨；有的很透明，有的必须查借入历史。',
 '与 -al 相联，接拉丁 -ialis，i 有时属于原词干，后来也被当作连接成分。不能每次都给 i 编一个独立词义。financial 等常有法语、拉丁语历史；torrent／torrential 可以作现代词形对应看；jovial 接 Iov-、Jove 的神名材料。整词重音和末段发音会变化，不能总用基础词读音原样相加。',
 [['急流与倾泻','torrent · torrential'],['旧占星命名到性情','jovial'],['财务、政治和地方','financial · presidential · provincial · ministerial'],['管理、学习和写作','managerial · tutorial · editorial · authorial'],['场景、结果和关系','circumstantial · consequential · tangential · referential']],
 'jovial 快活的，不是 juvenile 少年的；torrential 强调降雨猛烈；tutorial 可作教程名词，editorial 可作社论名词，末尾 -ial 不能保证所有整词只有一种词性。',
 'The editorial discussed financial support after the torrential rain.\n\n社论讨论了暴雨后的财务支持。',
 'torrent torrential jovial financial presidential racial editorial provincial tutorial managerial ministerial entrepreneurial exponential microbial gubernatorial circumstantial proverbial consequential dictatorial tangential referential prosecutorial curatorial factorial janitorial sartorial authorial ambassadorial inferential inquisitorial')
R('A1975','处于某状态、有相应作用；也可转指人、物','-ENT：原有动作、状态走成描述词或相应的人、物','excellent 出色的；resident 居住者、居住的；solvent 溶剂、有偿付能力的。它与拉丁分词历史相关，现代词义已经各有发展。',
 '不要只记成正在做。student 是学生，resident 可指居民，repellent 可指驱避用品；还有 innocent 无辜的、convenient 方便的等形容词。后缀提供历史线索，今天用法仍靠完整词。',
 '经法语 -ent 或直接接拉丁 -ens、-ent- 等现在分词材料，与 -ant 有历史联系；英语中的拼写受到多次借入、复古拼写影响，不能只凭发音任选 ant 或 ent。常与 -ence 名词相应：excellent／excellence、resident／residence。fluorescence、fluorescent 属十九世纪科学命名，现代能与 fluoresce 对照，却不能断言动词一定先出现。',
 [['显眼的光','fluorescence · fluorescent · resplendent · luminescent'],['出色、居住与人','excellent · student · resident'],['作用和状态','solvent · repellent · resilient · recurrent'],['判断、性格与程度','lenient · salient · abhorrent · transcendent'],['常见形容词与名词对应','different · patient · present · absent · confident · independent · intelligent · convenient · competent · innocent']],
 'fluorescent 与 reflective 反光不同；resplendent 是较文学的华丽描写；student 等已是人员名词；-ent／-ence 可帮助配对，但不是所有同尾单词都在现代临时拼成。',
 'The student noticed the fluorescent markings under the lamp.\n\n学生在灯下注意到了荧光标记。',
 'fluorescence fluorescent resplendent student excellent resident urgent contingent resilient solvent recurrent lenient salient abhorrent transcendent repellent luminescent referent different patient present absent evident confident dependent independent intelligent convenient competent violent decent innocent')
for x in WORDS:
 if x['word']=='toward':x['sources'].append('https://www.etymonline.com/word/-ward')
 if x['word']=='torrential':x['sources']+=['https://www.etymonline.com/word/-ial','https://www.oxfordlearnersdictionaries.com/definition/english/torrential']
 if x['word']=='resplendent':x['sources'].append('https://www.etymonline.com/word/-ent')
if __name__=='__main__':save('continuation_20261030_qe',ROOTS,WORDS)
