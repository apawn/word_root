"""Atory, drum, interfere and wright."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
A=[['拉丁 -ātōrius 等形式 → 英语 -atory','与某动作有关、用于某事、起某作用等性质'],['inflame 联系拉丁 inflammāre 点燃','燃起火；比喻激起怒气，另有炎症术语'],['inflame + -atory → inflammatory','煽动性；炎症相关的性质']]
W('inflammatory','英 /ɪnˈflæmətəri/；美 /ɪnˈflæmətɔːri/','煽动性、容易激起愤怒的；炎症的、引起或伴随炎症的',
 '一句话像往情绪上添火，容易激起怒气、冲突，可以 inflammatory；医学里则与 inflammation 炎症相关。两支共享燃起的历史形象，现代具体对象不同。',
 'inflame + -atory，联系拉丁 inflammāre 点燃及相应形容词构词。现代双写 mm，不能按常见词干原样加尾而漏写。',A[1:],
 'inflammatory remarks 煽动性言论，inflammatory language 容易激起冲突的语言，an inflammatory response 炎症反应。',
 'inflammatory remarks；inflammatory language；an inflammatory response。',
 'inflammatory 与 flammable 易燃的不同。说一段话 inflammatory 是评价其激怒、煽动效果，不自动判断内容真假。',
 ('The editor removed the inflammatory remarks from the article.','编辑删掉了文章里容易激起冲突的话。'),('The study examined the inflammatory response.','研究考察了炎症反应。'),sources=['https://en.wiktionary.org/wiki/inflammatory#English','https://www.merriam-webster.com/dictionary/inflammatory'])
R('A1942','与动作相关、用于某事或起某作用的形容词、固定名词','ATORY：先认整词，再判断关系、用途或作用','exploratory 探索相关，declaratory 宣告相关，respiratory 呼吸相关；inflammatory 看激起情绪或炎症；observatory 是固定场所名。',
 '同样结尾不意味着必须同一词性、同一中文后缀。observatory 名词和其他形容词的具体历史、用法需要分别理解。',
 '拉丁 -atorius 等 → 英语 -atory；常接动作词干，拼写、词性随整词固定。',
 [['动作相关、用途或作用的性质','exploratory · declaratory · respiratory · inflammatory'],['已经固定的场所名词','observatory']],
 'inflammatory 不等于 flammable；observatory 常作名词；-atory 的含义由词干和实际使用确定。',
 'The exploratory study examined an inflammatory response.\n\n这项探索性研究考察了一种炎症反应。','exploratory declaratory respiratory inflammatory observatory')
D=[['中古荷兰语 tromme 等日耳曼相关形式','鼓、鼓击；直接借入还是相关长词逆构有不同分析'],['英语 drum 的声音与形状扩展','敲鼓；圆筒、桶、滚筒；反复敲入、宣传招揽'],['派生与组合','drummer 鼓手；drumline 鼓队、打击乐队列']]
W('drum','/drʌm/','鼓；圆桶、滚筒；敲鼓、连续敲击',
 '鼓有圆筒形外壳，所以大圆桶、机器滚筒也能叫 drum。反复敲打、反复强调一件事，则借敲鼓的节奏来形容。',
 '通常联系中古荷兰语、低地德语鼓词，也有从相关长词逆构的分析，具体借词路径并非完全确定。现代声音、圆筒形状各自发展。',D[:2],
 'play the drums 打鼓，the drum of a washing machine 洗衣机滚筒，drum your fingers 用手指连续敲，drum up support 招揽支持，drum something into someone 反复灌输。',
 'play the drums；drum your fingers；drum up support。',
 'a drum 可以是单只鼓，the drums 常说一套鼓；drum up support 不是必须拿真鼓边敲边找人。',
 ('She learned to play the drums at school.','她在学校学会了打鼓。'),('He drummed his fingers on the table while waiting.','等待时，他用手指不断敲桌子。'))
W('drummer','英 /ˈdrʌmə/；美 /ˈdrʌmər/','鼓手',
 '打鼓、掌握节奏的人是 drummer。名字按动作角色来命名。',
 'drum + -er，双写 m。最常用意义是演奏鼓的人；其他同形旧称不必混进基础鼓手义。',D[:1]+[['drum + -er → drummer','演奏鼓的人']],
 'the band’s drummer 乐队鼓手，a jazz drummer 爵士鼓手。march to a different drummer 比喻按自己的想法行事。',
 'a jazz drummer；the band’s drummer。',
 'drummer 是人，drum 是乐器；percussionist 是打击乐演奏者，范围通常更宽。',
 ('The drummer counted in the rest of the band.','鼓手数拍，带领其他乐手进入演奏。'),('They are looking for a new drummer.','他们在找一位新鼓手。'))
W('drumline','/ˈdrʌmlaɪn/','行进乐队的鼓队、打击乐队列',
 '行进乐队里负责节奏、打击乐编排的一组乐手，可以 drumline。它说的是队伍、演奏分部，不只是一排摆放的鼓。',
 'drum 鼓 + line 队列、分部，形成集体名称。不同编制可包括行进和前场的不同打击乐人员。',D[:1]+[['drum + line → drumline','行进乐队中的打击乐队列、分部']],
 'a marching band drumline 行进乐队鼓队，a drumline rehearsal 鼓队排练。',
 'a drumline rehearsal；join the drumline。',
 'drumline 是一个分部、队伍，drummer 是个体角色；不是每个 drummer 都属于 marching band。',
 ('The drumline rehearsed behind the school.','鼓队在学校后面排练。'),('She joined the drumline as a snare drummer.','她以小军鼓手的身份加入鼓队。'))
R('B4230','鼓的节奏、形状与相应角色、队伍','DRUM：一面是敲击节奏，一面是圆筒外形','drum → drummer；drumline 集体队列；drumbeat、drumstick、eardrum 各看声音、敲击工具和相似结构。',
 '鼓手、鼓队、鼓点、滚筒不必硬背成孤立义项。先找声音、形状、角色中的一层，再接组合。',
 '日耳曼鼓词 → drum；-er 人，line 队列，beat 节奏，stick 敲击工具，ear 耳。',
 [['基础、人物与队伍','drum · drummer · drumline'],['声音、工具与身体结构','drumbeat · drumstick · eardrum']],
 'drumline 是队伍，drummer 是人；drums 可说一套鼓；drum up 是招揽等固定用法。',
 'The drummer led the drumline through a new drumbeat.\n\n鼓手带鼓队练了一种新鼓点。','drum drummer drumline drumbeat drumstick eardrum')
I=[['拉丁 ferīre 击打 → 古法语 ferir；entre- 相互、之间','相互击打、相撞'],['entreferir → 英语 interfere','碰撞、妨碍 → 干预、干扰'],['物理干涉与测量名称','interference 波叠加的效果；interferometer、interferometry']]
W('interfere','英 /ˌɪntəˈfɪə/；美 /ˌɪntərˈfɪr/','干预、插手；妨碍、干扰；产生干涉〔物理〕',
 '两件事碰在一起，一方影响另一方，interfere 的旧撞击画面就容易理解。人插手别人的事、噪声影响信号、波叠加，都各自形成用法。',
 '借古法语 entreferir 等，entre- 之间、相互 + ferir 击打，后者来自拉丁 ferīre。物理术语再用这个词表达波的相互作用。',I,
 'interfere in someone’s affairs 干预某人的事务，interfere with a signal 干扰信号，interfere with work 妨碍工作。in 常看插手领域，with 常看被影响对象。',
 'interfere in；interfere with。',
 'interfere 常带不受欢迎的影响或干预，help 不带同样语气。物理里干涉则是中性现象，可相长、可相消。',
 ('Please do not interfere in their private affairs.','请不要干预他们的私事。'),('The noise interfered with the recording.','噪声干扰了录音。'))
W('interference','英 /ˌɪntəˈfɪərəns/；美 /ˌɪntərˈfɪrəns/','干预、妨碍；信号干扰；干涉〔物理〕',
 '把 interfere 的影响作为现象来谈，就是 interference。电台杂音是干扰；光波叠加出现明暗变化，则是物理干涉的典型画面。',
 'interfere + -ence，去词尾 e。物理义在近代波动研究中固定，不应只按日常妨碍作负面理解。',I[:2]+[['interfere + -ence → interference','干预现象；波叠加的干涉效果']],
 'outside interference 外来干预，radio interference 无线电干扰，an interference pattern 干涉图样，constructive／destructive interference 相长／相消干涉。',
 'radio interference；an interference pattern；constructive interference。',
 '物理干涉不等于波永远互相消灭；相位等关系不同，局部可增强、可减弱。日常干预义与技术术语要分开。',
 ('The radio signal suffered from interference.','无线电信号受到干扰。'),('The experiment produced an interference pattern.','实验产生了干涉图样。'),sources=['https://en.wiktionary.org/wiki/interference#English','https://www.ligo.caltech.edu/LA/page/what-is-interferometer'])
W('interferometer','英 /ˌɪntəfəˈrɒmɪtə/；美 /ˌɪntərfəˈrɑːmɪtər/','干涉仪',
 '把波分开再合起来，路径等条件的细微变化能反映到干涉效果中。干涉仪就利用这种效果，把很小的变化变成可测信号。',
 'interfere 去 e + 连接元音 -o- + -meter 测量仪器。命名的是利用干涉进行测量的仪器，不是专门测有人插手多少次。',I[:2]+[['interfere + -o- + -meter → interferometer','利用波干涉的测量仪器']],
 'an optical interferometer 光学干涉仪，a laser interferometer 激光干涉仪。具体装置的光路、用途有多种。',
 'a laser interferometer；an optical interferometer。',
 'interferometer 是仪器，interferometry 是方法、技术。不同干涉仪不必都有完全相同的布局。',
 ('The interferometer detected a tiny change in distance.','干涉仪检测到距离的一点细微变化。'),('The students adjusted the mirrors in the interferometer.','学生调整了干涉仪中的反射镜。'),sources=['https://en.wiktionary.org/wiki/interferometer#English','https://www.ligo.caltech.edu/LA/page/what-is-interferometer'])
W('interferometry','英 /ˌɪntəfəˈrɒmɪtri/；美 /ˌɪntərfəˈrɑːmɪtri/','干涉测量法、干涉测量技术',
 '把干涉现象当成测量工具，这整套方法叫 interferometry。它可以涉及光，也能涉及无线电波等。',
 'interfere 去 e + -o- + -metry 测量。与 -meter 仪器名相比，-metry 命名测量活动、技术。',I[:2]+[['interfere + -o- + -metry → interferometry','利用波干涉进行测量的方法']],
 'optical interferometry 光学干涉测量，radio interferometry 射电干涉测量，precision interferometry 精密干涉测量。',
 'optical interferometry；radio interferometry。',
 'interferometry 不是一个额外的新干扰源，而是利用干涉进行测量；仪器名用 interferometer。',
 ('The team used interferometry to measure the surface.','团队使用干涉测量法测量表面。'),('Radio interferometry combines observations from multiple antennas.','射电干涉测量结合多个天线的观测。'),sources=['https://en.wiktionary.org/wiki/interferometry#English','https://www.ligo.caltech.edu/LA/page/what-is-interferometer'])
R('B4416','从相互碰撞到干预，再成为中性的波干涉术语','INTERFERE：相互作用可妨碍，也能用来测量','interfere → interference；interferometer 仪器，interferometry 方法；interferon 的名称取干扰病毒复制的相关命名背景。',
 '日常语境常不欢迎干预，技术语境的干涉则可被精密利用。相长、相消都属于干涉，不只看成互相挡住。',
 'entre- + ferir → interfere；-ence 现象；-o- 连接，-meter 仪器、-metry 测量方法。',
 [['动作与现象','interfere · interference'],['仪器与技术','interferometer · interferometry'],['固定生物学名称','interferon']],
 'in、with 搭配看插手领域与影响对象；干涉可相长可相消；-meter 与 -metry 区分仪器和方法。',
 'The interferometer uses interference to make precise measurements.\n\n干涉仪利用干涉现象进行精密测量。','interfere interference interferometer interferometry interferon')
W('wright','/raɪt/','制造者、工匠〔多保留在复合词中〕',
 '看 playwright、millwright 的后半，就像看到制造、建造某物的人。wright 单独用已较旧，但作构词成分仍很有用。',
 '古英语 wyrhta 工作者、制造者，经中古英语 wrighte 等传下，联系 work、wrought 词族。现代 w、gh 静音，和 write、right 同音。',
 [['古英语 wyrhta → 中古英语 wrighte → wright','工作者、制造者、工匠'],['保留在复合词中','playwright 剧作家；millwright 机械安装、维修等工匠']],
 'a village wright 村中工匠〔历史〕；playwright 把剧本创作比作制造，millwright 则来自磨坊、机械建造安装等工作。',
 'a village wright；playwright；millwright。',
 'playwright 的拼写不是 play + write。-wright 来自制造者，虽然实际工作当然包含写作。',
 ('The old contract names the village wright.','旧合同提到了村里的工匠。'),('The wright repaired the wooden wheel.','工匠修好了木轮。'))
R('B3989','工作、制造者的旧名称，仍在职业复合词中使用','WRIGHT：做出、造出某物的人','wright → playwright、millwright。',
 '独立词较旧，复合词却实用。写剧本的人拼 playwright，正因它把作品当成精心做出的东西。',
 'wyrhta 工作者 → wright；play 剧，mill 磨坊、相关机械。',
 [['制造者与职业组合','wright · playwright · millwright']],
 'wright、write、right 同音但来源和拼写不同；playwright 不拼作 playwrite。',
 'The playwright described a village wright in her new play.\n\n剧作家在新剧里描写了一名乡村工匠。','wright playwright millwright')
if __name__=='__main__':save('continuation_20261030_kr',ROOTS,WORDS)
