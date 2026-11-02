"""Necessary and slow: obligation, speed and their regular extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
N=[['拉丁 necesse、necessarius → 法语 necessaire → 英语 necessary','不可避免、所需；更深组合解释不完全确定'],['现代 necessary','少不了的条件 → 必要的、必需的']]
W('necessary','英 /ˈnesəsəri/；美 /ˈnesəseri/','必要的；必需的',
 '要把这件事做成，这一项少不了；与只是有帮助、最好有，强度不同。',
 '经法语接拉丁 necessarius、necesse 不可避免、需要。更远常解释为否定加退让、避开的相关形式，但不是现代英语 ne- + cess + ary 可逐段随意拼义。',N,
 'necessary equipment 必需设备，if necessary 必要时，It is necessary to... 有必要……。',
 'if necessary；necessary for；necessary to do；where necessary。',
 'necessary 必需，useful 有用；某工具有帮助，不代表少了它任务就完全做不了。',
 ('Bring the necessary documents to the appointment.','赴约时带上必需文件。'),('We can arrange another meeting if necessary.','必要时，我们可以再安排一次会议。'))
W('necessarily','英 /ˌnesəˈserəli/；美 /ˌnesəˈserəli/','必然地；一定',
 '最值得先学 not necessarily：有这种情况，不一定就能推出那个结论。',
 'necessary + -ly，y 改 i，成为 necessarily。副词常从必要关系表达必然结果，而不是永远翻成很有必要地。',N+[['necessary + -ly → necessarily','必要关系 → 必然、一定']],
 'not necessarily 不一定，not necessarily mean 不一定意味着；重音与 necessary 不完全相同。',
 'not necessarily；necessarily mean；necessarily involve。',
 'not necessarily good 是不一定好，未必直接说坏；necessarily not good 才是必定不好，否定位置改变逻辑。',
 ('A higher price does not necessarily mean better quality.','价格更高不一定意味着质量更好。'),('Working longer does not necessarily make you more productive.','工作更久不一定使效率更高。'))
W('unnecessary','英 /ʌnˈnesəsəri/；美 /ʌnˈnesəseri/','不必要的；多余的',
 '拿掉这一步、这笔支出也能达到目的，所以没必要多做。',
 'un- 不 + necessary，否定必要性，不自动否定它是否存在或是否有任何作用。',N+[['un- + necessary → unnecessary','必要的反面 → 不必要']],
 'unnecessary expense 不必要开支，unnecessary detail 多余细节，avoid unnecessary delays 避免无谓延误。',
 'unnecessary expense；unnecessary detail；unnecessary delays。',
 'unnecessary 不必做，impossible 做不到；不必要的问题也可能完全能解决，只是不值得花工夫。',
 ('The new process removes several unnecessary steps.','新流程删去了几个不必要的步骤。'),('Please avoid unnecessary detail in the introduction.','引言里请避免多余细节。'))
R('B3815','必要性与必然推论','NECESSARY：少不了；NECESSARILY：是否一定能推出','必要形容词后接必然副词，not necessarily 的日常逻辑最值得掌握；unnecessary 否定必要性。',
 '借法语接拉丁不可避免、需要词。现代派生透明，但不凭远源猜测替代实际用法。',
 'necessary → necessarily；un- + necessary → unnecessary。',
 [['性质、推论与否定','necessary · necessarily · unnecessary']],
 'not necessarily 不一定，不等于必然相反；useful 有用不自动 necessary 必需。',
 'More equipment is not necessarily necessary.\n\n更多设备未必是必需的。',
 'necessary necessarily unnecessary')
S=[['古英语 slāw → 中古英语 slaw、slow → slow','慢、迟缓；旧有懒惰等相关义'],['现代 slow 词族','速度低 → 放慢；slow + -th 的历史分支 sloth']]
def SH(f,m):return S+[[f,m]]
W('slow','英 /sləʊ/；美 /sloʊ/','慢的；使放慢、放慢；迟缓地',
 '同样一段路、同样一件事，它花的时间更多；也可以主动把节奏放下来。',
 '继承古英语 slāw，现代形容词与动词很常见。副词 slow 也在 go slow、drive slow 等表达中使用，不是一律语法错误。',S,
 'a slow train 慢车，slow progress 缓慢进展，slow down 放慢；a slow clock 是钟走慢了。',
 'slow progress；slow down；go slow；a slow clock。',
 'slow 速度低，late 比约定时间晚；慢车可以准时到，晚点的车也可能跑得快。',
 ('Progress was slow at first.','起初进展缓慢。'),('The driver slowed down near the school.','司机经过学校附近时减速了。'))
W('slower','英 /ˈsləʊə/；美 /ˈsloʊər/','更慢的；更慢地',
 '不是只说慢，而是与另一个速度、原来的节奏比较。',
 'slow + -er，比较级，不双写 w；形容词和相应速度副词比较都可见。',SH('slow + -er → slower','速度更低 → 更慢'),
 'a slower pace 更慢节奏，go slower 慢一点；more slowly 也是常见副词比较形式。',
 'a slower pace；slower than；go slower。',
 'slower 比较程度，slowly 描述方式；write more slowly 或 write slower 可用，语体和搭配决定选择。',
 ('Could we walk at a slower pace?','我们能走慢一点吗？'),('This route is shorter but slower in rush hour.','这条路线更短，但高峰时走起来更慢。'))
W('slowly','英 /ˈsləʊli/；美 /ˈsloʊli/','缓慢地',
 '把慢这一性质加到动作上：慢慢说、慢慢打开、慢慢恢复。',
 'slow + -ly，规则副词。保留 slow 完整拼写，不写成 slowly 之外的变形。',SH('slow + -ly → slowly','慢 → 以慢的方式'),
 'speak slowly 慢慢说，recover slowly 缓慢恢复，slowly but surely 慢而稳地。',
 'speak slowly；move slowly；slowly but surely。',
 'a slow recovery 用形容词修饰名词，recover slowly 用副词修饰动词；slow 也有部分既定副词搭配。',
 ('Please speak slowly so I can take notes.','请慢一点说，方便我做笔记。'),('The door opened slowly.','门缓缓打开了。'))
W('slowness','英 /ˈsləʊnəs/；美 /ˈsloʊnəs/','缓慢；迟缓',
 '把速度慢本身当成问题、特点或感受来讨论。',
 'slow + -ness，状态性质名词；与 slowly 方式副词分工不同。',SH('slow + -ness → slowness','慢的性质 → 缓慢、迟缓'),
 'the slowness of the response 响应迟缓，frustrating slowness 令人烦躁的缓慢。',
 'the slowness of；frustrating slowness；slowness in responding。',
 'slowness 说速度，delay 说延误、等待；系统可能响应慢但尚未超过承诺期限。',
 ('Users complained about the slowness of the website.','用户抱怨网站速度慢。'),('He was frustrated by the slowness of the negotiations.','谈判进展迟缓让他感到沮丧。'))
W('sloth','英 /sləʊθ/；美 /sloʊθ/、/slɔːθ/','懒惰；树懒',
 '抽象先是懒散、迟缓，动物名则借它说动作慢的树懒；这不是动物真的有人的道德过错。',
 'slow + 旧抽象名词后缀 -th 的历史形式，经中古英语 slouthe 等成 sloth。动物因动作缓慢而得英语俗名，现代不按完整 slow 直接拼写。',SH('slow 的旧抽象派生 → sloth','迟缓、懒散 → 树懒的名称'),
 'a three-toed sloth 三趾树懒，sloth and idleness 懒惰闲散；动物名可数，抽象性质通常不可数。',
 'a three-toed sloth；a sloth in a tree；sloth and idleness。',
 'sloth 树懒与 lazy person 懒人不能作生物学等同；人动作慢也可能是谨慎，并非懒惰。',
 ('A sloth hung from a branch above the path.','一只树懒倒挂在小路上方的树枝上。'),('The old story warns against sloth and greed.','古老故事告诫人们远离懒惰与贪婪。'))
W('slowpoke','英 /ˈsləʊpəʊk/；美 /ˈsloʊpoʊk/','慢吞吞的人；慢性子',
 '有人总落在后头、做事慢，你开玩笑叫他慢家伙；也可能惹人不快。',
 'slow + poke，后部人物称呼的确切命名来历不透明，不用 poke 戳的现代常用义硬造戳一下才走的故事。美式口语常见。',SH('slow + poke → slowpoke','慢吞吞的人物称呼'),
 'Come on, slowpoke! 快点，慢家伙！a bit of a slowpoke 有点慢性子。',
 'a slowpoke；Come on, slowpoke；a bit of a slowpoke。',
 'slowpoke 口语人物评价，slower 比较级；称人慢家伙是否亲切，取决于关系和语气。',
 ('Come on, slowpoke, the others are waiting.','快点，慢家伙，其他人都等着呢。'),('He called himself a slowpoke when learning new software.','他说自己学新软件是个慢性子。'))
R('B2488','慢、放慢与迟缓的历史派生','SLOW：完成同一动作需要更久','slow、slower、slowly、slowness 按程度、方式、性质连读；sloth 是旧名词派生，slowpoke 是人物口语称呼。',
 '古英语慢、迟缓词族保留旧抽象形式 sloth。树懒英语名利用动作缓慢命名，不把比喻当动物道德判断。',
 'slow → slower、slowly、slowness；旧 -th 派生 → sloth；slow + poke → slowpoke。',
 [['基本性质、比较与方式','slow · slower · slowly · slowness'],['旧派生与人物称呼','sloth · slowpoke']],
 'slow 慢与 late 晚不同；sloth 动物可数、懒惰抽象义不可数；slowpoke 看语气。',
 'The slower route allowed us to walk slowly and enjoy the view.\n\n那条较慢的路线让我们能慢慢走，欣赏景色。',
 'slow slower slowly slowness sloth slowpoke')
if __name__=='__main__':save('continuation_20261030_b',ROOTS,WORDS)
