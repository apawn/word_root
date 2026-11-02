"""Yell and snake."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
Y=[['古英语 giellan → 中古英语 yellen → yell','发出响亮、尖厉的叫声'],['声音与表达的扩展','喊出内容；因愤怒、兴奋、呼救等大喊'],['yell + -ing → yelling','大喊这一活动、叫喊声']]
W('yell','/jel/','大喊、叫喊；一声大叫',
 '声音突然或持续地放大，用来把话传出去、表达情绪，就是 yell。愤怒会喊，兴奋、呼救也会喊，不能只记成骂人。',
 '古英语 giellan 经中古英语 yellen 传下。现代既作动词，也作一声叫喊的名词。',Y[:2],
 'yell for help 大声呼救，yell at someone 对某人大喊、吼叫，yell out a name 大声喊出名字，give a yell 大叫一声。',
 'yell for help；yell at；yell out。',
 'yell at 常带对人吼叫的感觉；yell to someone 可以强调距离远、为让对方听见而喊。场景、语气共同决定态度。',
 ('She yelled for help from the window.','她从窗口大声呼救。'),('We heard the fans yell as the ball hit the net.','球入网时，我们听见球迷大喊。'))
W('yelling','/ˈjelɪŋ/','大喊、叫喊声',
 '把大喊当成一项正在发生的活动，或整片声音来听，可以 yelling。',
 'yell + -ing；中古英语已有相应形式。这里可作活动名词，也可作正在叫喊的分词。',Y[:2]+[['yell + -ing → yelling','叫喊的活动、声音']],
 'stop yelling 别喊了，a lot of yelling 一片叫喊，yelling and cheering 叫喊与欢呼。',
 'stop yelling；a lot of yelling。',
 'yelling 不保证在吵架；听到比赛中的 yelling，可能是兴奋、加油。a yell 强调一次，yelling 更容易把活动整体来看。',
 ('There was a lot of yelling after the final whistle.','终场哨后响起一片叫喊。'),('They stopped yelling when the room became quiet.','房间安静下来后，他们不再喊了。'))
R('B3849','发出响亮叫声，按场景表达愤怒、兴奋或求助','YELL：先抓声音大，再看为什么喊、对谁喊','yell → yelling。',
 '叫喊的强度与说话意图分开：大声不一定生气，也可能为让远处的人听见。',
 'giellan → yellen → yell；-ing 活动或分词。',
 [['动作、一次叫声与活动','yell · yelling']],
 'yell at 常对人吼，yell to 可为传声；yelling 不自动等于争吵。',
 'We heard yelling from the field, then someone yelled for the coach.\n\n我们听见球场传来叫喊，接着有人大声叫教练。','yell yelling')
S=[['古英语 snaca → 中古英语 snake','蛇；更早联系爬行、滑行词族'],['细长、曲折动作的比喻','路蜿蜒、队列延伸；细长疏通工具'],['动物组合名称与伤害名称','rattlesnake 响尾蛇；snakebite 蛇咬、蛇咬伤']]
W('snake','/sneɪk/','蛇；蜿蜒行进；细长疏通工具；阴险者〔贬义比喻〕',
 '蛇贴地爬行、身体细长弯曲；道路、队列曲折延伸，也可以 snake。疏通管道的长软工具则借外形叫 a drain snake。',
 '承古英语 snaca，经中古英语 snake，联系日耳曼爬行、滑行的旧词族。物件形状、运动方式和文化中的阴险形象，形成不同扩展。',S[:2],
 'a grass snake 草蛇，a drain snake 管道疏通工具，a path snakes through the hills 小路蜿蜒穿山，a snake in the grass 暗藏的阴险者。',
 'a drain snake；snake through；a snake in the grass。',
 '把人称作 snake 是强负面评价；真实蛇的生物行为不由这个文化比喻来定义。serpent 常更文学、庄重。',
 ('A snake slid into the long grass.','一条蛇滑进高草里。'),('The queue snaked around the corner.','队伍弯弯曲曲地延伸过街角。'))
W('rattlesnake','/ˈrætəlsneɪk/','响尾蛇',
 '尾端有能发出响声的结构，所以名称抓住 rattle 响声、响物这一特征。',
 'rattle + snake，由特征加动物名称组成复合词。通常指美洲相应响尾蛇类，不是所有会发声的蛇的随意称呼。',S[:1]+[['rattle + snake → rattlesnake','带尾部响器的蛇类名称']],
 'a rattlesnake’s rattle 响尾蛇的尾部响器，a rattlesnake habitat 响尾蛇栖息地。',
 'a rattlesnake’s rattle；a rattlesnake habitat。',
 'rattle 在这里是响器、发响特征，不能只拿婴儿摇铃这一具体物品义推断名称。',
 ('The documentary showed a rattlesnake moving across the desert.','纪录片展示一条响尾蛇穿过沙地。'),('The exhibit explains how a rattlesnake’s rattle makes sound.','展览解释响尾蛇的尾部响器怎样发声。'),sources=['https://en.wiktionary.org/wiki/rattlesnake#English','https://www.etymonline.com/word/rattlesnake'])
W('snakebite','/ˈsneɪkbaɪt/','蛇咬、蛇咬伤',
 'snake 指来源，bite 指咬：既可说咬这一事件，也常说它造成的咬伤。',
 'snake + bite，按咬的动物来源构成复合名词。复数 snakebites，变化加在完整词末尾。',S[:1]+[['snake + bite → snakebite','蛇的咬、相应咬伤']],
 'a snakebite victim 蛇咬伤者，cases of snakebite 蛇咬伤病例。酒吧中的同名饮品等属于另行固定的名称，不接普通伤害句法。',
 'a snakebite victim；cases of snakebite。',
 'snakebite 命名事件、伤害，不单凭这个词就说明蛇种、是否注入毒液、伤情程度。',
 ('Her grandfather told a story about surviving a snakebite.','她祖父讲过自己被蛇咬后幸存的故事。'),('The report lists cases of snakebite from the region.','报告列出了这个地区的蛇咬伤病例。'),sources=['https://en.wiktionary.org/wiki/snakebite#English','https://www.merriam-webster.com/dictionary/snakebite'])
R('B2645','蛇的爬行、细长形状与特征组合，再到伤害名称','SNAKE：动物名也借出蜿蜒的形状、运动','snake → rattlesnake、snakebite、snakeskin；snake 作动词可说道路、队列蜿蜒。',
 '特征动物名、身体材料、咬伤与形状比喻分别看前后部。对人的贬义比喻也不要拿来代替动物学。',
 'snaca → snake；rattle 响器，bite 咬，skin 皮。',
 [['动物、特征与蜿蜒动作','snake · rattlesnake'],['皮与咬伤','snakeskin · snakebite']],
 'snakebite 不单独决定伤情；snake 可动词说蜿蜒；rattlesnake 是固定动物名。',
 'The film showed a rattlesnake as the camera followed the snaking path.\n\n镜头沿蜿蜒小路移动时，影片展示了一条响尾蛇。','snake rattlesnake snakeskin snakebite')
if __name__=='__main__':save('continuation_20261030_kv',ROOTS,WORDS)
