"""Bumbling, waddling, toddling and faltering."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A2238':dict(words='bumble bumbles bumbled bumbling bumbler bumblers toddle toddles toddled toddling toddler toddlers'.split(),label='bumble、toddle：笨拙推进，迈着不稳的小步',note='bumble 笨拙动作义可能拟态，另有嗡嗡声材料，两支具体关系未定；toddle 来源未定，可能与 totter 相接并受 waddle 等影响。不能见到 -le 就给前面的字母编出确定词根。'),
 'B3746':dict(words='waddle waddles waddled waddling'.split(),label='waddle：左右摇摆地走',note='waddle 联系 wade 与旧小幅、反复动作后缀 -le；wade 的旧义更宽，不是现代必须先涉水才能变成摇摆走路。'),
 'A1760':dict(words='falter falters faltered faltering falteringly unfaltering unfalteringly'.split(),label='falter：不稳、迟疑，到坚定不移',note='falter 远源未定，或接北欧迟疑材料，或有中古英语折叠材料等分析；不能直接当成 fault 错误加 -er。unfaltering 的 un- 是否定，表示不失稳、不动摇。'),
}
BUMBLE=[['bumble 笨拙、乱撞的动词，可能为拟态来源','声音支另有嗡嗡材料，具体关系不能一概定死'],['现代笨拙做事 → bumbling / bumbler','笨拙的表现，与笨手笨脚的人']]
WADDLE=[['wade 的旧行进材料 + 小幅、反复动作 -le → waddle','现代不是把完整 wade 原封不动接上 le'],['短步、左右摇摆地走','常见鸭子、企鹅的步态，也可形容人']]
TODDLE=[['toddle 出现于苏格兰、英格兰北部材料','来源未定，可能接 totter 并受 waddle 等影响'],['迈短而不稳的小步 → toddler 学步幼儿','幼儿是典型场景，不按人名 Todd 拆词源']]
FALTER=[['较早 falter：踉跄、摇晃；来源未定','有北欧迟疑、受困材料，或反复折叠材料等分析'],['动作、声音不稳 → 信心、进展动摇','unfaltering 以否定 un- 表不动摇、不中断']]
W('bumbles','/ˈbʌmbəlz/','笨拙地做事、乱闯〔第三人称单数〕',
 '总是忙活，却老出小错、找不着顺畅办法，是 bumbles。常见 bumbles through，像磕磕绊绊总算把事做过去。',
 'bumble + -s，读 /z/；这里用笨拙动作这一义，基础来源可能为拟态。',BUMBLE+[['bumble + -s → bumbles','他或她笨拙地推进']],
 'bumbles through an explanation 解释得乱七八糟；bumbles along。',
 'bumbles into trouble；bumbles around the kitchen。',
 'bumbles 着重笨拙、不利索，rushes 着重匆忙；不着急也可能手忙脚乱。',
 ('He bumbles through the instructions without making them clear.','他磕磕绊绊讲了一遍说明，却没讲清楚。'),('The character bumbles from one mishap to the next.','那个角色笨手笨脚，接连碰上倒霉事。'),sources=S('bumbles','bumble'))
W('bumbled','/ˈbʌmbəld/','笨拙地做了、乱闯了',
 '没想清楚就动手，一路小错不断地做完，可以说 bumbled through。语气常有自嘲或喜剧感。',
 'bumble 去 e 加完整 -ed，读 /d/；过去式、过去分词。',BUMBLE+[['bumble + -ed → bumbled','过去笨拙地推进、误闯']],
 'bumbled through a speech；bumbled into the wrong room。',
 'bumbled around for a while；bumbled along。',
 'bumbled through 可能最终完成了，failed to complete 才明确说没完成；过程不顺与结果失败不同。',
 ('I bumbled through the speech and forgot half my notes.','我磕磕绊绊讲完了发言，忘了一半准备内容。'),('We bumbled into the wrong room and quickly backed out.','我们糊里糊涂进错了房间，赶紧退了出来。'),sources=S('bumbled','bumble'))
W('bumbling','/ˈbʌmbəlɪŋ/','笨手笨脚、糊里糊涂的；正在笨拙地做',
 '喜剧里那个老出错、越帮越忙的助手，就是 a bumbling assistant。动作在继续，办法却不熟练、不灵光。',
 'bumble 去 e 加 -ing；既可写动作过程，也可作形容词说笨拙、糊涂。',BUMBLE+[['bumble + -ing → bumbling','笨拙推进的过程，或经常出错的性质']],
 'a bumbling detective 笨手笨脚的侦探；bumbling through a task。',
 'a bumbling attempt；bumbling around the room。',
 'bumbling 带不熟练、笨拙的评价，beginning 只说刚开始；初学者也可以很认真、有条理。',
 ('The comedy features a well-meaning but bumbling detective.','那部喜剧里有个好心却笨手笨脚的侦探。'),('I was still bumbling through the software when she showed me a shortcut.','我还在笨拙地摸索软件，她就教给我一个快捷办法。'),sources=S('bumbling','bumble'))
W('bumbler','英 /ˈbʌmblə/；美 /ˈbʌmblɚ/','做事笨手笨脚、常出错的人',
 '想帮忙，却老弄错步骤、把事情搞乱的人，可以被叫作 a bumbler。它常含批评，也常见于轻松的喜剧人物描写。',
 'bumble 去 e 加完整 -er，表示做这种动作的人；不是只加一个 r。',BUMBLE+[['bumble + -er → bumbler','笨拙做事的人']],
 'a well-meaning bumbler 好心却笨手笨脚的人；an incompetent bumbler。',
 'portray someone as a bumbler；a lovable bumbler 可爱的糊涂人。',
 'bumbler 是人，blunder 是一次大错；人和错误事件的词性、指代不同。',
 ('The film portrays him as a lovable bumbler.','电影把他塑造成一个可爱的糊涂人。'),('I felt like a complete bumbler while assembling the shelves.','装书架时，我觉得自己笨手笨脚，什么都弄不好。'),sources=S('bumbler','bumble'))
W('bumblers','英 /ˈbʌmbləz/；美 /ˈbʌmblɚz/','笨手笨脚、常出错的人〔复数〕',
 '几个角色互相帮忙，却越弄越乱，可以叫 a group of bumblers。它评价做事方式，不是说几件错误本身。',
 'bumbler + -s，读 /z/；先从 bumble 去 e 加 -er 表人，再用复数。',BUMBLE+[['bumble → bumbler → bumblers','笨拙动作，到做事者，再到多人']],
 'a pair of bumblers 两个糊涂、笨拙的人；well-meaning bumblers。',
 'portrayed as bumblers；a team of bumblers。',
 'bumblers 对人的评价较强，learners 只是学习者；正在学不自动等于总把事搞砸。',
 ('The two thieves are portrayed as harmless bumblers.','那两个小偷被描写成没什么威胁的笨蛋。'),('We looked like a pair of bumblers trying to unfold the tent.','我们试着展开帐篷，看起来像两个笨手笨脚的糊涂人。'),sources=S('bumblers','bumble'))
W('waddles','英 /ˈwɒdəlz/；美 /ˈwɑdəlz/','迈小步、左右摇摆着走〔第三人称单数〕',
 '鸭子一走，身体左一下右一下，就是 waddles。重点是左右摆动的小步态，不是单纯慢。',
 'waddle + -s，读 /z/；waddle 联系 wade 的旧行进材料与反复、小幅动作 -le。',WADDLE+[['waddle + -s → waddles','他或它左右摇摆着迈步']],
 'waddles towards the pond 摇摇摆摆走向池塘；waddles across the yard。',
 'a duck waddles；waddles along the path。',
 'waddles 写左右摇摆，hops 写跳着走；鸭子和兔子常见的移动画面不同。',
 ('The duck waddles towards the pond.','鸭子摇摇摆摆地走向池塘。'),('The penguin waddles across the ice.','企鹅左右摇摆着走过冰面。'),sources=S('waddles','waddle'))
W('waddled','英 /ˈwɒdəld/；美 /ˈwɑdəld/','迈着小步、左右摇摆着走了',
 '看见鸭子从脚边慢慢摇过，可以说 waddled past。它把步态写出来，比 walked 多了左右摆动的形状。',
 'waddle 去 e 加完整 -ed，读 /d/；词干原有双 d 保留。',WADDLE+[['waddle + -ed → waddled','过去左右摇摆着迈步']],
 'waddled away 摇摇摆摆走开；waddled into the water。',
 'waddled past us；waddled along the bank。',
 'waddled 不表示一定跌跌撞撞快摔倒，staggered 更常写失去平衡的踉跄；摇摆可以是正常步态。',
 ('The ducks waddled past us in a line.','鸭子排着队，从我们身边摇摇摆摆地走过。'),('The penguin waddled down to the water.','企鹅摇摇摆摆地走到水边。'),sources=S('waddled','waddle'))
W('waddling','英 /ˈwɒdəlɪŋ/；美 /ˈwɑdəlɪŋ/','正在左右摇摆地走；摇摆的小步态',
 '身体随着小步左右摆动，是 waddling。用来形容步态时，读者能直接看见鸭子一样摇着走的样子。',
 'waddle 去 e 加 -ing；不重复 l。分词写动作，也能修饰 gait 步态。',WADDLE+[['waddle + -ing → waddling','左右摇摆迈步的过程、姿态']],
 'a waddling gait 摇摆的小步态；waddling across the grass。',
 'ducks waddling to the pond；waddling along。',
 'waddling 写步态形状，wandering 写走走逛逛、方向不固定；摇摆着走可以很有明确目的地。',
 ('We watched the ducklings waddling across the grass.','我们看着小鸭在草地上摇摇摆摆地走。'),('The costume gave the actor a waddling gait.','那身服装让演员走起路来左右摇摆。'),sources=S('waddling','waddle'))
W('toddle','英 /ˈtɒdəl/；美 /ˈtɑdəl/','迈着短小、不稳的步子走；慢悠悠地走〔口语〕',
 '小孩刚学会走，步子小，身体晃着往前挪，是 toddle。大人也可轻松说 toddle off，意思近于慢悠悠走开、走一趟。',
 '苏格兰、英格兰北部材料，来源未定；可能与 totter 不稳地走相接，并受 waddle 等影响。不能按人名 Todd 加后缀造历史。',TODDLE,
 'toddle towards someone 摇摇晃晃走向某人；toddle off home。',
 'toddle across the room；toddle down to the shop。',
 'toddle 常有小步、不稳的画面，waddle 更强调左右摆；幼儿迈小步不一定走成鸭子一样。',
 ('The baby began to toddle across the room.','宝宝开始迈着不稳的小步穿过房间。'),('I might toddle down to the shop later.','我待会儿可能慢悠悠去趟商店。'),sources=S('toddle','toddle'))
W('toddles','英 /ˈtɒdəlz/；美 /ˈtɑdəlz/','迈着短小、不稳的步子走〔第三人称单数〕',
 '孩子张着双臂，一小步一小步走向你，是 toddles。动作已经在前进，但平衡还没那么稳。',
 'toddle + -s，读 /z/；词尾 e 保留，基础词来历仍有不同分析。',TODDLE+[['toddle + -s → toddles','他或她迈着不稳的小步走']],
 'toddles towards the door；toddles after her brother 跟在哥哥后面摇摇晃晃走。',
 'toddles across the carpet；toddles into the room。',
 'toddles 是走小步，crawls 是爬；能扶着站起不等于已经能稳定迈步。',
 ('She toddles towards her father with her arms outstretched.','她张着双臂，摇摇晃晃走向爸爸。'),('The little boy toddles after his sister.','小男孩迈着不稳的小步跟在姐姐后面。'),sources=S('toddles','toddle'))
W('toddled','英 /ˈtɒdəld/；美 /ˈtɑdəld/','迈着不稳的小步走了；慢悠悠走去了',
 '刚才孩子晃晃悠悠走到门边，是 toddled。口语里大人说 toddled off，也可只是轻松地走开，不必真走不稳。',
 'toddle 去 e 加完整 -ed，读 /d/；词干已有双 d 保留。',TODDLE+[['toddle + -ed → toddled','过去迈小步、不稳地走，或轻松走开']],
 'toddled across the room；toddled off to bed 慢悠悠去睡觉。',
 'toddled towards the toy；toddled down the path。',
 'toddled 的步态理解要看主语；大人轻松说自己 toddled off，不必据此判断他失去平衡。',
 ('The child toddled across the room to pick up a toy.','孩子摇摇晃晃走过房间，去捡玩具。'),('After tea, we toddled off home.','喝完茶，我们便慢悠悠回家了。'),sources=S('toddled','toddle'))
W('toddling','英 /ˈtɒdəlɪŋ/；美 /ˈtɑdəlɪŋ/','正在迈着不稳的小步走；学步中的',
 '小孩刚能独立走，步子短、身子摇晃，是 toddling。也能在 toddling child 中形容正处在学走路阶段的孩子。',
 'toddle 去 e 加 -ing；动作过程可修饰人，形成正在学步、小步不稳的画面。',TODDLE+[['toddle + -ing → toddling','迈小步的过程，或学步中的性质']],
 'a toddling child 学步中的孩子；toddling around the garden。',
 'toddling towards the door；just started toddling。',
 'toddling 强调小步和不稳，running 是跑；孩子能快走几步，也不表示已经稳定会跑。',
 ('The child was toddling around the garden.','孩子正在花园里摇摇晃晃地走。'),('She held out her hands to the toddling baby.','她向正学着走路的宝宝伸出双手。'),sources=S('toddling','toddle'))
W('toddlers','英 /ˈtɒdləz/；美 /ˈtɑdlɚz/','学步幼儿、小小孩〔复数〕',
 '已经开始迈步、还小小的孩子，日常常叫 toddlers。它联系走路阶段，不是把所有儿童都叫这个词。',
 'toddler + -s，读 /z/；toddle 去 e 加完整 -er，原是迈小步走的人，后来常指学步幼儿。',TODDLE+[['toddle → toddler → toddlers','不稳地走，到学步幼儿，再到多个孩子']],
 'toys for toddlers 适合幼儿的玩具；parents of toddlers。',
 'toddlers and older children；a group of toddlers。',
 'toddlers 常指很小、开始学走路的孩子，teenagers 是青少年；年龄阶段不是同一个范围。',
 ('The play area is designed for toddlers.','这片游乐区是为学步幼儿设计的。'),('The toddlers followed the music with little claps.','几个小小孩跟着音乐轻轻拍手。'),sources=S('toddlers','toddle'))
W('falter','英 /ˈfɔːltə/；美 /ˈfɔltɚ/','开始不稳、迟疑；声音发颤；进展减弱',
 '说到难处声音停顿，信心突然松了一下，或生意增长开始没劲，都能 falter。像原本平稳向前的一步开始晃。',
 '较早指踉跄、摇晃；来源未定，有北欧受困、迟疑材料，或中古英语 falden 折叠的反复动作分析。不能直接当作 fault 加 -er。',FALTER,
 'her voice began to falter 她的声音开始发颤；confidence may falter。',
 'growth starts to falter；never falter 从不动摇。',
 'falter 是开始不稳、迟疑，stop 是停住；声音颤一下、增长放缓，并不一定完全结束。',
 ('Her voice began to falter as she told the story.','讲那个故事时，她的声音开始发颤。'),('Do not let one setback make your confidence falter.','别让一次挫折就动摇了信心。'),sources=S('falter','falter'))
W('falters','英 /ˈfɔːltəz/；美 /ˈfɔltɚz/','开始不稳、迟疑、减弱〔第三人称单数〕',
 '增长原本顺畅，后来明显放慢，是 growth falters；讲到某一处声音颤了，也是 falters。共同点是没能继续稳稳往前。',
 'falter + -s，读 /z/；基础词近源有不同分析，不把它与 fault 错误机械合成。',FALTER+[['falter + -s → falters','它开始不稳、迟缓或减弱']],
 'her voice falters；his confidence falters；growth falters。',
 'never falters 从不动摇；falters at a crucial moment。',
 'falters 不一定是犯错误，makes a mistake 才直接说弄错；犹豫一下可能还答得正确。',
 ('His voice falters when he mentions the old house.','提到老房子时，他的声音有些发颤。'),('The plan needs support when progress falters.','进展不顺时，计划需要支持。'),sources=S('falters','falter'))
W('faltered','英 /ˈfɔːltəd/；美 /ˈfɔltɚd/','曾迟疑、不稳；声音发颤了；进展减弱了',
 '刚才说得好好的，突然卡了一下、声音不稳，可以说 faltered。也可说支持、信心、增长在那一段减弱了。',
 'falter + 完整 -ed，读 /d/；过去式、过去分词，不另加 /ɪd/。',FALTER+[['falter + -ed → faltered','过去一度迟疑、动摇或减弱']],
 'her voice faltered；confidence faltered；growth faltered。',
 'never faltered 从未动摇；faltered for a moment。',
 'faltered for a moment 可以只是不稳片刻，gave up 是放弃；短暂迟疑之后仍能继续。',
 ('She faltered for a moment, then continued speaking.','她迟疑了一下，随后继续说。'),('His confidence never faltered during the difficult weeks.','那几周很艰难，他的信心却从未动摇。'),sources=S('faltered','falter'))
W('faltering','英 /ˈfɔːltərɪŋ/；美 /ˈfɔltərɪŋ/','不稳、迟疑的；断断续续的；正在减弱的',
 '话说得不连贯，是 a faltering voice；经济恢复得慢、还不稳定，是 a faltering recovery。不是已经彻底失败，而是继续得不稳。',
 'falter + -ing；过程形式也可作形容词，写声音、步伐、进展的迟疑不稳。',FALTER+[['falter + -ing → faltering','正在不稳、减弱，或带这种性质']],
 'a faltering voice 迟疑发颤的声音；a faltering economy。',
 'faltering steps 不稳的步子；faltering confidence。',
 'faltering recovery 是恢复不稳，complete recovery 是恢复完全；处于过程不表示已经到达结果。',
 ('He answered in a faltering voice.','他用有些迟疑、发颤的声音回答。'),('The report described a faltering economic recovery.','报告形容经济恢复得迟缓而不稳定。'),sources=S('faltering','falter'))
W('falteringly','英 /ˈfɔːltərɪŋli/；美 /ˈfɔltərɪŋli/','迟疑、不稳、断断续续地',
 '话想说出口，却一句停一下，或脚步还不稳地向前，是 falteringly。它把不稳、迟疑落实到动作方式。',
 'faltering + -ly；先由 falter 加 -ing 成分词、形容词，再加方式副词后缀。',FALTER+[['falter → faltering → falteringly','动作不稳，到迟疑的，再到迟疑地']],
 'speak falteringly 断断续续地说；move falteringly。',
 'begin falteringly 起步不顺；answer falteringly。',
 'quietly 只说声音小，falteringly 说不连贯、迟疑；声音很轻也可以流畅坚定。',
 ('She began falteringly, unsure how to explain.','她不知道怎么解释，开口时有些迟疑。'),('He moved falteringly towards the chair.','他步子不稳地朝椅子走去。'),sources=S('falteringly','falter'))
W('unfaltering','英 /ʌnˈfɔːltərɪŋ/；美 /ʌnˈfɔltərɪŋ/','坚定不移的；稳定而不中断的',
 '困难变多，支持却没有松动；声音从头到尾稳稳的，都能说 unfaltering。像走一条路，步伐没有突然软下来。',
 '否定 un- + faltering；不是撤回某个动作，而是否定迟疑、失稳这类性质。',FALTER+[['un- + faltering → unfaltering','不迟疑、不动摇，保持稳定']],
 'unfaltering support 始终不变的支持；unfaltering determination。',
 'an unfaltering voice；unfaltering commitment。',
 'unfaltering 强调不中断、不动摇，correct 才说正确；一个决定可以很坚定，却仍需要检验是否正确。',
 ('Her unfaltering support helped us through the hardest weeks.','她始终不变的支持帮我们度过了最难的几周。'),('He read the statement in an unfaltering voice.','他用稳定、毫不迟疑的声音读完声明。'),sources=S('unfaltering','unfaltering'))
W('unfalteringly','英 /ʌnˈfɔːltərɪŋli/；美 /ʌnˈfɔltərɪŋli/','坚定不移、毫不迟疑地；始终稳定地',
 '路很难走，却一步步稳稳继续；面对压力仍保持同样的支持，是 unfalteringly。它说明怎样坚持，不保证判断永远无误。',
 'unfaltering + -ly；内部仍可看 un- 否定 + falter + -ing，最外层 -ly 说动作方式。',FALTER+[['unfaltering + -ly → unfalteringly','以不动摇、不间断的方式行动']],
 'support unfalteringly 始终坚定支持；continue unfalteringly。',
 'speak unfalteringly；work unfalteringly towards a goal。',
 'unfalteringly 强调稳定、坚定，unfailingly 常强调每次都如此；频率的可靠与过程中不动摇可以相近但侧重不同。',
 ('She supported the project unfalteringly through every setback.','每遇一次挫折，她都始终坚定地支持这个项目。'),('He continued unfalteringly despite the interruptions.','虽然不断被打断，他仍毫不迟疑地继续下去。'),sources=S('unfalteringly','unfaltering'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhp',ROOTS,WORDS)
 extend_lessons()
