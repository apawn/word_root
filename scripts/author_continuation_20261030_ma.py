"""Arrow, dash, prompt, fisher, availability and binding."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
Ar=[['古英语 earh，变化词干 earw-','弓射出的箭'],['中古英语 arwe → arrow','箭；又用箭形符号表示方向']]
W('arrow','英 /ˈærəʊ/；美 /ˈæroʊ/','箭；箭头符号',
 '一根带尖头、从弓上射出的东西是 arrow。把它简化画成一条线和尖头，就成了路牌、图表里指方向的箭头。',
 '承古英语 earh 的词形及 earw- 变化词干，经中古英语 arwe 发展成 arrow；属于旧日耳曼语箭的词族。',Ar,
 'shoot an arrow 射箭，follow the arrow 沿箭头指示走，an arrow pointing left 向左的箭头；图中箭头的意义还需看图例。',
 'shoot an arrow；follow the arrow。',
 'arrow 可指整支箭，arrowhead 突出箭的尖头；符号箭头也常直接叫 arrow。',
 ('A blue arrow points towards the entrance.','一个蓝色箭头指向入口。'),('The arrow landed close to the centre of the target.','箭落在靶心附近。'))
R('B3294','箭的实体与表示方向的箭形符号','ARROW：尖端指向哪里，视线就跟到哪里','arrow → arrowhead。',
 '整支箭和前端尖头先分清，再把形状迁移到路牌和图表。不同图里的箭头可表示方向、过程或关系，要结合图例。',
 '古英语 earh、earw- → 中古英语 arwe → arrow；head 在 arrowhead 中说尖端、头部。',
 [['整支箭与尖头','arrow · arrowhead']],
 '实体 arrow 是整支箭；图中的 arrow 常直接指箭头符号。',
 'The arrowhead was damaged, so the archer replaced the arrow.\n\n箭头坏了，弓箭手换了一支箭。','arrow arrowhead')
Da=[['中古英语 daschen 等','突然猛击、急冲，可能接北欧相应词，更远未定'],['dash 的扩展','冲刺；少量泼入；希望被打碎；短横符号'],['dash + -ing；slap + dash','潇洒有活力；匆忙草率']]
W('dash','/dæʃ/','急冲、赶去；打碎；一小份；破折号、短横线',
 '赶车时突然冲过去是 dash；希望被猛地打碎是 dash someone’s hopes；往食物里加一点点调料则是 a dash。先抓短促、有劲的动作。',
 '中古英语 daschen 等表示突然打击、急冲，可能借北欧词。名词由动作发展，少量加入、短横符号等成为不同常用分支。',Da[:2],
 'dash for the door 冲向门口，dash off a note 匆匆写张便条，a dash of pepper 少许胡椒，dash someone’s hopes 使希望破灭。',
 'dash for；dash off；a dash of；dash hopes。',
 'a dash 在食谱里通常泛说少量，不总是精确计量单位；标点 dash 与连接词的 hyphen 常有不同长度和用途。',
 ('We dashed across the road to catch the bus.','我们冲过马路去赶公交车。'),('Add a dash of pepper to the soup.','往汤里加少许胡椒。'),('The cancellation dashed their hopes of performing.','活动取消，让他们登台表演的希望破灭了。'),sources=['https://en.wiktionary.org/wiki/dash#English','https://www.etymonline.com/word/dash'])
W('dashing','/ˈdæʃɪŋ/','潇洒、有风度的；富有活力的；dash 的 -ing 形式',
 '一个人精神十足、穿着利落，出场很有风采，可以 dashing；不是必须正在奔跑。',
 'dash + -ing。形容词义与 dash 的气势、引人注目的风采义相连，发展为有活力、潇洒漂亮。',Da[:2]+[['dash 的风采、气势义 + -ing','富有活力 → 潇洒、有风度']],
 'a dashing young man 潇洒的年轻男子，a dashing figure 英姿飒爽的人物；偏带生动、略有文学色彩的赞赏。',
 'a dashing figure；look dashing。',
 'dashing 作分词可以说正在急冲，作形容词却常说气质和风采；看句子结构。',
 ('He looked dashing in his new suit.','他穿上新西装，显得很潇洒。'),('The novel opens with a dashing young officer arriving in town.','小说开篇，一位英姿飒爽的年轻军官来到镇上。'),sources=['https://en.wiktionary.org/wiki/dashing#English','https://www.etymonline.com/word/dash'])
W('slapdash','/ˈslæpdæʃ/','草率、马虎、仓促拼凑的；草率地',
 '赶着交差，随手一拍一抹就算做好了；slapdash 让人看到这种省掉细致检查的做法。',
 'slap 拍、击 + dash 急冲、猛打等组成，形成匆忙、草率的词。这个动作画面帮助记忆，不是特指必须用手拍东西。',Da[:1]+[['slap + dash → slapdash','匆忙粗率地完成 → 草率的']],
 'slapdash work 马虎的工作，a slapdash approach 草率做法；也可作副词说做得草率。',
 'slapdash work；a slapdash approach。',
 'quick 只说快，slapdash 还批评不够仔细；效率高的工作不一定 slapdash。',
 ('The report was full of errors because of slapdash editing.','报告因编辑草率而错误百出。'),('A slapdash repair failed after a few days.','仓促做的修补没过几天就坏了。'))
R('B3301','短促有劲的冲击，扩展为冲刺、少量、风采与草率','DASH：一下冲出去，也能一下打碎、泼入一点','dash → dashing；slapdash 说草率；dashboard 的历史联系挡泥飞溅。',
 '动作的短促、有劲是很好的记忆起点，但不同分支要各配场景：赶路、调味、希望破灭、人物风采。',
 '中古英语 daschen 等可能接北欧词；-ing 形成分词、形容词；slap + dash → slapdash；dash + board → dashboard。',
 [['急冲及风采','dash · dashing'],['草率做法','slapdash'],['历史挡泥板与现代面板','dashboard']],
 'dashing 可潇洒；slapdash 批评马虎；dashboard 最初挡的是飞溅泥水。',
 'He dashed off a note, but the result looked slapdash.\n\n他匆匆写了张便条，结果显得很马虎。','dash dashing slapdash dashboard')
P=[['拉丁 prō- 向前 + emere 拿 → prōmere','拿出、带到眼前'],['过去分词 prōmptus','已拿到手边 → 现成、准备好的'],['法语、拉丁形式 → 英语 prompt','及时的；促使、提示；提示信息']]
W('prompt','英 /prɒmpt/；美 /prɑːmpt/','及时的；促使、提示；提示、提示词',
 '东西已经放在手边，马上就能回应，是 prompt 的及时感；给别人一个线索，带动他说话、行动，则是提示或促使。',
 '经法语及拉丁 prōmptus，源于 prōmere 拿出，其结构是 prō- 向前 + emere 拿。准备就绪、推动行动、给出提示逐步成为英语相关用法。',P,
 'a prompt reply 及时回复，prompt someone to act 促使某人行动，a writing prompt 写作提示，a computer prompt 电脑提示；给 AI 的输入指令也常叫 prompt。',
 'a prompt reply；prompt someone to do；a writing prompt。',
 '形容词 prompt 说及时，动词 prompt 说促使或提醒，名词 prompt 说提示内容。现代 AI 用法是提示、输入义的延伸。',
 ('Thank you for your prompt reply.','谢谢你及时回复。'),('Her question prompted a lively discussion.','她的问题引发了热烈讨论。'),('The teacher gave us a writing prompt about an unexpected journey.','老师给了我们一个关于意外旅程的写作题目。'),sources=['https://en.wiktionary.org/wiki/prompt#English','https://www.etymonline.com/word/prompt','https://dictionary.cambridge.org/dictionary/english/prompt'])
W('promptly','英 /ˈprɒmptli/；美 /ˈprɑːmptli/','及时、迅速地；准时地',
 '该处理就马上处理，是 promptly；说某个钟点时，也可能强调准点、没有拖后。',
 'prompt + -ly，形成副词；由准备好、回应及时的性质，转成行动的方式。',P+[['prompt + -ly → promptly','以及时、无拖延的方式']],
 'reply promptly 及时回复，act promptly 迅速行动，arrive promptly at nine 九点准时到。',
 'reply promptly；act promptly；promptly at nine。',
 'promptly 常突出不耽搁；quickly 也可以只说动作本身速度快。接钟点时注意准时这一层。',
 ('Please report any damage promptly.','发现任何损坏，请及时报告。'),('The meeting began promptly at ten.','会议十点准时开始。'))
W('prompter','英 /ˈprɒmptə/；美 /ˈprɑːmptər/','提词者；提词器；给出提示的人',
 '演员忘词，有人在旁轻声补一句，那个人是 prompter；屏幕把台词送到眼前的装置，也可用这个名称。',
 'prompt + -er，形成执行提示的人或工具名。舞台提词者是典型场景，设备用法常对应 teleprompter 的简称。',P+[['prompt + -er → prompter','帮助提示的人或装置']],
 'a theatre prompter 舞台提词员，read from a prompter 看着提词器读；角色、装置由场景区分。',
 'a theatre prompter；read from a prompter。',
 'prompter 是人或工具，prompt 是一句提示或提示行为；-er 在这里不是更及时的比较级用法。',
 ('The actor waited for a quiet cue from the prompter.','演员等着提词员轻声提示。'),('She glanced at the prompter and continued speaking.','她看了一眼提词器，接着讲了下去。'))
R('B4158','手边准备好，到及时行动、促使和提示','PROMPT：随时拿得出来，回应及时；也拿出线索带动下一步','prompt → promptly、prompter。',
 '一个词有三种常用词性：及时的回复、促使讨论、提供提示。把场景放在一起，便能看懂写作提示、舞台提词及电脑提示之间的联系。',
 'prō- 向前 + emere 拿 → prōmere → prōmptus；经法语、拉丁进入英语；-ly 方式，-er 人物或工具。',
 [['及时与行动方式','prompt · promptly'],['给出提示的角色、工具','prompter']],
 'prompt 的词性先看句法；prompter 可以提词员或提词器。',
 'The prompter supplied a cue promptly when the actor forgot his line.\n\n演员忘词时，提词员及时给了提示。','prompt promptly prompter')
R('B4561','捕鱼者及复合词；动物名有独立命名历史','FISHER：按捕鱼活动叫人，复合词再加限定','fisher → fisherman；kingfisher 是翠鸟名称。',
 'fisher 先抓捕鱼者，fisherman 再加人物后项。翠鸟名称含 fisher，但渔貂的 fisher 常用动物义另有借词来源，不能把所有同形词都当捕鱼的人。',
 '古英语 fisċere → fisher；fisher + man → fisherman；king’s fisher → kingfisher。渔貂义另接法语动物、毛皮词。',
 [['捕鱼者通称','fisher · fisherman'],['捕鱼鸟的名称','kingfisher']],
 'kingfisher 名称不是所有种类只吃鱼的保证；fisher 另有渔貂义。',
 'A fisherman watched a kingfisher dive towards the water.\n\n渔民看见一只翠鸟向水面俯冲。','fisher fisherman kingfisher')
Av=[['available 可获得、可用','能够得到，或时间安排允许'],['availability → unavailability','可用性 → 不可用、无法到场的状态']]
W('unavailability','/ˌʌnəveɪləˈbɪləti/','无法获得、不能使用的状态；无法到场、没有空',
 '东西拿不到、人没空、场地用不了，都可说 unavailability；共同点是这次需要时，相关资源不在可用范围里。',
 'un- + availability；也可按 unavailable + -ity 的对应关系认识，-able 一族形成 -ability 名词形式。',Av,
 'the unavailability of a venue 场地无法使用，staff unavailability 员工无法到场，temporary unavailability 暂时不可用。',
 'the unavailability of；temporary unavailability。',
 'unavailability 不必表示永远不存在：可能只是在所需时间、地区或条件下无法获得。',
 ('The meeting was postponed because of the speaker’s unavailability.','发言人无法到场，会议因此延期。'),('The notice explained the temporary unavailability of the booking service.','通知解释了预订服务暂时无法使用的情况。'))
R('B3794','可用、可获得的状态及其否定','AVAILABILITY：需要的时候，是否拿得到、用得上','availability → unavailability；bioavailability 是专门领域的生物利用度。',
 '日常先看时间、库存和场地条件。bioavailability 已有独立精讲，它有专门的生物、药学含义，不等于货架有没有货。',
 'available → availability；un- 否定可用状态；bio- 连接专门生物学用法。',
 [['可用及不可用','availability · unavailability'],['专门利用度名称','bioavailability']],
 '不可用可能暂时；生物利用度与库存可得性分清。',
 'Check room availability before announcing a date; unavailability could force a change.\n\n公布日期前先查房间能否使用，否则可能不得不改期。','availability unavailability bioavailability')
R('B4188','绑住、结合的动作，进入装订、约束和吸引','BINDING：把东西连住、固定住，或把人吸引住','binding → bookbinding；spellbinding 用魔法束住人的画面说入迷。',
 '书页被固定成册、约定对人有约束力、故事把注意力紧紧抓住，都能沿连接、束住来理解。具体中文随场景走。',
 'bind + -ing → binding；book + binding → bookbinding；spell 咒语 + binding → spellbinding。',
 [['结合与装订','binding · bookbinding'],['吸引注意的比喻','spellbinding']],
 'binding 不都译正在绑；spellbinding 说令人入迷，spellbound 说被迷住的状态。',
 'The book’s binding was plain, but the story was spellbinding.\n\n书的装帧很朴素，故事却扣人心弦。','binding bookbinding spellbinding')
if __name__=='__main__':save('continuation_20261030_ma',ROOTS,WORDS)
