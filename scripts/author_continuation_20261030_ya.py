"""Frequent present forms: brings, contains, begins, stands and leads."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3560':dict(words=['bring','brings'],label='bring → brings：带来人与物，也带来结果',note='brings 词尾在 ng 音后读 z；继承古英语携带、带来的词族。'),
 'C1487':dict(words=['contain','contains'],label='contain → contains：保持在范围里',note='合在一起持有的拉丁词族，扩展为包含、容纳与控制住。'),
 'C1189':dict(words=['require','requires'],label='require → requires：需要具备、要求做到',note='寻求、请求词族后来突出必要条件、要求。'),
 'B3592':dict(words=['allow','allows'],label='allow → allows：给许可、留余地',note='允许与分配、安排的较早来源汇合，小词决定现代结构。'),
 'B2755':dict(words=['begin','begins'],label='begin → begins：从这里开始发生',note='begin 继承古英语 beginnan；begins 规则，began、begun 不规则。'),
 'B2545':dict(words=['stand','stands'],label='stand → stands：站、立与售卖的小摊',note='站住、占据位置的动作，发展出立场、架台、摊位等名词。'),
 'B2816':dict(words=['lead','leads'],label='lead → leads：带领与线索、连接线',note='本次重点是 /liːd/ 引导词族，leads 可是现在动词或相关复数；金属铅的旧词来源另认。'),
 'B2541':dict(words=['win','wins'],label='win → wins：努力后取得胜利、争取到',note='早期劳作、争取词族，现代突出赢得结果，wins 也可数一次次胜利。'),
 'B3201':dict(words=['help','helps'],label='help → helps：帮人完成与让情况好转',note='本族帮助词族，help 可接人、动作，也可不接宾语说起帮助作用。'),
 'B2518':dict(words=['love','loves'],label='love → loves：爱、喜爱与爱好',note='古英语 lufu、lufian 的名词、动词各自延续，现代 loves 常是第三人称单数。'),
}
W('brings','/brɪŋz/','带来、带到；引起、带来结果；bring 的第三人称单数',
 '某个人或事把东西带到这里、带到谈话中的目的地，是 brings；一项改变带来好处、麻烦，也能这样说。',
 'bring + -s，/ŋ/ 后词尾读 /z/。bring 继承古英语 bringan，经中古英语延续；过去 brought 不规则，现在 brings 直接加 s。',
 [['古英语 bringan → 中古英语 → bring','携带、送来'],['bring + -s → brings','单数主语带来；引起某种结果']],
 'brings a friend 带朋友来；brings good news 带来好消息；brings people together 把人们聚在一起；brings back memories 唤起回忆。',
 'brings a smile；brings the books back。','brings 的带来可以是实物，也可以是感受、影响。bring back 可说带回物品，也可说唤起记忆；参照点与对象一起决定具体意思。',
 ('She brings her lunch to work every day.','她每天都带午饭去上班。'),('The old song brings back memories of school.','那首老歌唤起了学生时代的回忆。'),sources=['https://en.wiktionary.org/wiki/brings#English','https://en.wiktionary.org/wiki/bring#English'])
W('contains','/kənˈteɪnz/','包含、容纳；控制住、遏制；contain 的第三人称单数',
 '把内容留在一个范围之内，是 contains：盒子里有东西，文章里有信息，都属于包含；控制住火势等，也是在限制它继续越界。',
 'contain + -s，/n/ 后读 /z/。contain 经古法语 contenir 接拉丁 continēre，con- 一起与 tenēre 保持、持有形成，早有容纳、约束义。',
 [['拉丁 con- + tenēre → continēre → 法语、英语 contain','保持在一起 → 容纳、约束'],['contain + -s → contains','单数主语包含、装得下；控制住']],
 'contains useful information 包含有用信息；contains three parts 包含三个部分；contains the spread 遏制蔓延。',
 'the box contains ...；contains more than one type。','contains 常说某物内部有什么，includes 常说整体把某些部分也包括进来，两者可重合。contains herself/himself 等表达还可说克制情绪，具体看主语与宾语。',
 ('The box contains all the parts needed for the model.','盒子里有制作模型所需的全部零件。'),('The final chapter contains several practical examples.','最后一章包含几个实际例子。'),sources=['https://en.wiktionary.org/wiki/contains#English','https://en.wiktionary.org/wiki/contain#English'])
W('requires','英 /rɪˈkwaɪəz/；美 /rɪˈkwaɪrz/','需要；要求必须做到；require 的第三人称单数',
 '要把事情办成，有些东西、动作不能缺，这就是 requires 的需要；规章、职责把必须做到的事定下来，也用它。',
 'require + -s，词尾读 /z/。require 经法语及拉丁路线接 requīrere，re- 与 quaerere 寻找、询问相连；由寻求、请求发展到需要、要求。',
 [['拉丁 requīrere → 法语等 → require','寻求、请求 → 需要、要求'],['require + -s → requires','单数主语需要某物；要求某人行动']],
 'requires patience 需要耐心；requires a key 需要钥匙；requires us to wait 要求我们等候；requires attention 需要注意。',
 'requires careful planning；the job requires ...。','requires someone to do 表示要求某人做；requires doing 在一些用法中表示需要被处理，如 requires cleaning。need 通常更日常，require 常更正式或突出条件。',
 ('The job requires patience and careful attention.','这项工作需要耐心和细心。'),('The form requires you to provide a contact address.','这张表要求你提供一个联系地址。'),sources=['https://en.wiktionary.org/wiki/requires#English','https://en.wiktionary.org/wiki/require#English'])
W('allows','/əˈlaʊz/','允许；使能够；留出、考虑到；allow 的第三人称单数',
 '给一个动作放行，或为它留下可行的条件，就是 allows：规则允许、设计让人更方便、计划留出余地都可以用。',
 'allow + -s，元音后读 /z/。allow 的法语来源汇合拉丁 allocāre 分配、安排与 allaudāre 赞同、认可的词族，形成现代许可、留出等用法。',
 [['较早分配、认可词族 → 法语 → allow','安排、同意 → 许可、留出条件'],['allow + -s → allows','单数主语允许、使能够；考虑余量']],
 'allows visitors to enter 允许访客进入；allows time for questions 留出提问时间；allows for changes 考虑到变化。',
 'allows easy access；allows someone to work from home。','allows someone to do 的 to 后接动词原形；allows for 看把什么条件算进去。This design allows easy access 说设计让进入更容易，不必一定存在发许可的人。',
 ('The wide entrance allows people to move through easily.','宽阔的入口让人们容易通行。'),('The schedule allows time for questions after each talk.','日程在每场讲座后都留出了提问时间。'),sources=['https://en.wiktionary.org/wiki/allows#English','https://en.wiktionary.org/wiki/allow#English'])
W('begins','/bɪˈɡɪnz/','开始；开始于；begin 的第三人称单数',
 '一件事从还没进行，跨到开始发生的那一点，就是 begins；也可以把话题、故事的第一个内容交代出来。',
 'begin + -s，/n/ 后读 /z/。begin 继承古英语 beginnan，历史含 be- 与旧动词部分；现在 begins 规则，过去 began、分词 begun 则保留不规则元音变化。',
 [['古英语 beginnan → 中古英语 → begin','开始发生、进行'],['begin + -s → begins','单数主语开始；以某内容开头']],
 'begins at nine 九点开始；begins with a question 以问题开头；begins to understand 开始理解；begins again 重新开始。',
 'the story begins；begins by explaining ...。','begins with 后接开头的内容；begins by doing 后接首先做的动作。begin to do 和 begin doing 都常表示开始做，具体句子中选择自然表达。',
 ('The story begins with a letter found in an old house.','故事从在一栋老房子里发现的一封信开始。'),('She begins each lesson by reviewing the previous topic.','她每节课都先回顾上次的主题。'),sources=['https://en.wiktionary.org/wiki/begins#English','https://en.wiktionary.org/wiki/begin#English'])
W('stands','/stændz/','站着；位于；忍受；代表〔stands for〕；台架、摊位、看台〔复数〕',
 '人、东西稳稳占住一个位置，是 stands；能立住放东西的架台、售货的摊位，也由站立、摆设的画面理解。固定搭配再说明它怎样站、替谁站。',
 'stand + -s，/d/ 后读 /z/。stand 继承古英语 standan，经中古英语延续；台架、摊位、立场等名词由动作、位置发展。过去式、分词是 stood。',
 [['古英语 standan → stand 动词及相关名词','站立、占据位置 → 架台、摊位、立场'],['stand + -s → stands','单数主语站、位于；多个架台、摊位等']],
 'stands by the door 站在门边；stands for something 代表某事；food stands 食品摊位；music stands 乐谱架；the stands 体育场看台。',
 'stands in the centre；stands out from the crowd。','stands for 可以说缩写代表什么，也可说主张、维护的原则。stands out 是显眼、突出，stands by someone 是支持某人。多义搭配按完整短语记。',
 ('A small wooden table stands beside the window.','窗边放着一张小木桌。'),('Several food stands lined the road to the festival.','通往节庆活动的路边排着几个食品摊。'),sources=['https://en.wiktionary.org/wiki/stands#English','https://en.wiktionary.org/wiki/stand#English'])
W('leads','/liːdz/〔引导词族〕','带领、通往、导致；领先；线索、连接线、牵引绳等〔相关复数〕',
 '把人或事情带向一个方向，是 leads；能带调查往前走的信息叫线索，带电流连接两端的线也可叫 leads。',
 'lead /liːd/ + -s，/d/ 后读 /z/。引导词族继承古英语 lǣdan；名词线索、连接线等在相关分支发展。金属 lead /led/ 有另一条古英语来源，本条重点讲引导词族。',
 [['古英语 lǣdan → lead /liːd/','引导、带领；发展出相关名词'],['lead + -s → leads /liːdz/','单数主语带领；多条线索、连接线等']],
 'leads the team 带领团队；leads to the lake 通往湖边；leads to problems 导致问题；new leads 新线索；electrical leads 电连接线。',
 'leads by one point；follow up the leads。','leads to 的 to 后可以是地点，也可以是结果、名词或 -ing。动词 lead 的过去式是 led /led/，与现在 leads /liːdz/ 分开认。',
 ('The narrow path leads to the lake.','那条窄路通向湖边。'),('The old letters gave us several new leads.','那些旧信给我们提供了几条新线索。'),sources=['https://en.wiktionary.org/wiki/leads#English','https://en.wiktionary.org/wiki/lead#English'])
W('wins','/wɪnz/','赢得、取得；获胜；胜利、获胜次数〔复数〕',
 '经过争取后，结果落到自己这边，是 wins；把一次次这样的结果数出来，就是名词的一次次胜利。',
 'win + -s，/n/ 后读 /z/。win 接古英语 winnan、ġewinnan 的劳作、努力、争取、获得词族，经中古英语延续，现代赢得结果义突出。过去式 won 不规则。',
 [['古英语努力、争取词族 → 中古英语 → win','争取、获得 → 赢'],['win + -s → wins','单数主语获胜；多次胜利']],
 'wins the game 赢得比赛；wins a prize 获奖；wins support 赢得支持；three wins 三次胜利。',
 'wins by two points；a record of five wins。','win 常直接接比赛、奖项、支持等；beat 常直接接被击败的人、队伍。wins the match 和 beats the other team 都可以说获胜，关注的对象不同。',
 ('The team with the most points wins the game.','得分最多的队伍赢得比赛。'),('They finished the month with four wins and one draw.','他们以四胜一平的成绩结束了这个月的比赛。'),sources=['https://en.wiktionary.org/wiki/wins#English','https://en.wiktionary.org/wiki/win#English'])
W('helps','/helps/','帮助；使更容易、使好转；help 的第三人称单数',
 '让别人更容易做成一件事，或让情况比原来好一些，就是 helps。提供人手、方法、信息都可能起这样的作用。',
 'help + -s，/p/ 后读 /s/。help 的名词、动词分别继承古英语 help、helpan 等，经中古英语延续；helps 是现代现在时变化。',
 [['古英语 help、helpan → 中古英语 → help','帮助、协助'],['help + -s → helps','单数主语帮助；起改善作用']],
 'helps me understand 帮我理解；helps to explain 有助于解释；helps with the work 帮忙做事；every little helps 一点点帮助也有用。',
 'helps a lot；helps someone to finish。','help someone do 和 help someone to do 都常用；helps with something 把任务作为名词接上。It helps 可以说这起作用、有帮助，不必每次都直接点出某个受帮助的人。',
 ('The diagram helps me understand how the parts fit together.','这张图帮助我理解各部分怎样接在一起。'),('She helps with the cooking on weekends.','她周末会帮忙做饭。'),sources=['https://en.wiktionary.org/wiki/helps#English','https://en.wiktionary.org/wiki/help#English'])
W('loves','/lʌvz/','爱；很喜欢；love 的第三人称单数',
 '把深厚感情放在一个人身上，或对某件活动特别喜欢，就是 loves；对家人的爱与爱做某事，语气、对象不同，但都能表达喜爱。',
 'love + -s，/v/ 后读 /z/。love 动词继承古英语 lufian，名词另接 lufu，经中古英语延续；两者同族，不靠拆现代字母来解释。',
 [['古英语 lufu、lufian → 中古英语、英语 love','爱这一名词；爱、喜爱的动作'],['love + -s → loves','单数主语爱、喜爱']],
 'loves her family 爱她的家人；loves reading 很喜欢阅读；loves to cook 很喜欢做饭；loves the idea 很喜欢这个想法。',
 'really loves；loves spending time outdoors。','loves doing 与 loves to do 都常表示喜爱某活动。loves someone 与 loves a colour、loves a song 的情感强度由对象、语境决定，不必每次都理解成恋爱。',
 ('She loves reading stories aloud to the children.','她很喜欢给孩子们朗读故事。'),('He loves the quiet mornings in the village.','他很喜欢村里宁静的早晨。'),sources=['https://en.wiktionary.org/wiki/loves#English','https://en.wiktionary.org/wiki/love#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ya',ROOTS,WORDS)
 extend_lessons()
