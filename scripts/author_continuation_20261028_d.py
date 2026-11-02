"""Individually authored common word families; 2026-10-28 continuation."""
import json
from pathlib import Path
from lesson_authoring import entry as E, save

WORDS=[];ROOTS=[]
CAT={r['id']:r for r in json.loads((Path(__file__).resolve().parents[1]/'.cache/catalog.json').read_text())}
def W(*args,**kwargs):WORDS.append(E(*args,**kwargs))
def R(rid,meaning,core,image,intro,forms,branches,contrasts,practice,names):
    names=names.split()
    ROOTS.append(dict(id=rid,meaning=meaning,core=core,image=image,intro=intro,forms=forms,branches=branches,contrasts=contrasts,practice=practice,words=names,exclude={w:'本轮先保留常用、构词清楚的学习词；冷门词暂缓。' for w in CAT[rid]['family'] if w not in names}))
REAL=[['拉丁 rēs → 晚期拉丁 reālis','事物 → 实际的'],['古法语 reel → 英语 real','真实的、实际存在的']]
W('real','/ˈrɪəl/','真实的；实际的；真正的',
 '屏幕上是一座画出来的房子，眼前这座能走进去的，才是 a real house。',
 '借古法语 reel，源于晚期拉丁 reālis“实际的”，再接拉丁 rēs“事物”。real 里的 re- 不是表示“再次”的现代前缀。',REAL,
 'real 可以排除假冒，也可以强调实际影响：a real problem 是需要认真处理的问题。real estate 是房地产的固定说法；real income 则常说扣除价格变化影响后的实际收入。',
 'real life；a real problem；the real reason；real estate。',
 'real 强调确实存在或名副其实；true 更常判断说法是否符合事实。a real story 需看语境，a true story 明确说故事确有其事。',
 ('Is this a real diamond?','这是真钻石吗？'),('The real problem is that nobody knows who is responsible.','真正的问题是没人知道谁负责。'))
W('really','/ˈrɪəli/','真的；实际上；很、非常',
 '先确认“这是真的”，再把这个肯定的劲头用来加强语气。',
 'real + -ly，-ly 形成副词；中古英语已有对应形式。这里后缀表示副词用法，不表示“小”或“可爱”。',REAL+[['英语 real + -ly → really','真实地 → 确实、很']],
 'Did it really happen? 询问是否真发生；really useful 是很有用。Really? 单独问可表示惊讶或怀疑，语调决定态度。not really 通常是委婉的“不太是”。',
 'really want；really useful；not really；Really?。',
 'really 修饰形容词时常近似 very，但 really 可以修饰动词：I really like it；不能照搬成 I very like it。',
 ('Do you really want to leave now?','你真的想现在离开吗？'),('The map was really helpful.','这张地图很有帮助。'))
W('reality','英 /riˈæləti/；美 /riˈæləti/','现实；实际情况',
 '脑中设想是一回事，真正过起来、发生出来的那一面是 reality。',
 '现代对应 real + -ity；-ity 表性质、状态。历史经法语 réalité 上接中世纪拉丁 reālitās，早期还有财产相关义，不应只画成英语 real 新加后缀。',REAL[:1]+[['中世纪拉丁 reālitās → 法语 réalité','实际存在、实在性的相应名词'],['英语 reality','现实；实际情况']],
 'in reality 把实际情况与表面印象拉开；face reality 是接受现实。a reality 可数时，常说一种已经存在的事实或情况。virtual reality 是虚拟现实这一技术名称。',
 'in reality；face reality；become a reality；virtual reality。',
 'reality 是实际状态，realism 是正视现实的态度或写实风格；两个名词不能只按中文的“现实”互换。',
 ('The job looked easy, but in reality it required years of practice.','这份工作看着容易，实际上需要多年的练习。'),('Their idea has finally become a reality.','他们的想法终于变成了现实。'))
W('realize','/ˈrɪəlaɪz/','意识到；实现；变现',
 '原来模糊的事忽然在脑中“成了真的”：啊，原来是这样。也可以把计划真正做出来。',
 'real + -ize，-ize 常表示使成为或进入某种状态；形成与法语 réaliser 等相应形式有联系。不能把所有义项都死译为“使真实”。',REAL+[['real + -ize；与法语 réaliser 等对应','使成实际；使头脑清楚认识'],['英语 realize','意识到；实现；把资产变成现金']],
 'realize that 通常是意识到某事；realize a dream 是实现梦想。金融语境 realize a gain 表把账面收益变成已实现收益，realize assets 可指变现。',
 'realize that；realize how；realize a dream；realize a gain。',
 'realize 常有此前没明白、现在明白了的转折；know 只说知道。I realized I was wrong 比 I knew I was wrong 多了认识发生变化的感觉。',
 ('I suddenly realized that I had left my keys at home.','我突然意识到钥匙落在家里了。'),('She worked for years to realize her dream of opening a bakery.','她努力多年，实现了开一家面包店的梦想。'))
W('realise','/ˈrɪəlaɪz/','意识到；实现〔realize 的常见英式拼写〕',
 '看到 s 不必重新猜义，它和 realize 是同一个常用动词的两种拼写。',
 'real + -ise；-ise 与 -ize 是这一类动词的拼写变体。法语 réaliser 也是相关形式；这里不是再接一个独立词 ise。',REAL+[['real + -ise → realise','与 realize 对应的拼写形式']],
 'realise 常用于英式英语，realize 在美式普遍，也用于部分英式编辑规范。两者用法和读音基本相同，一篇文章里保持所选拼写习惯即可。',
 'realise that；realise the importance；realise an ambition。',
 'realise 和 release“释放”拼写相近，但词源和含义不同；意识到错误用 realise a mistake，不能写 release a mistake。',
 ('I did not realise how late it was.','我没意识到已经这么晚了。'),('The project helped her realise a long-held ambition.','这个项目帮助她实现了长久以来的抱负。'))
W('realism','/ˈrɪəlɪzəm/','现实态度；现实主义；写实风格',
 '画人时连皱纹也画出来，做计划时连预算不够也承认：先照着实际情况看。',
 'real + -ism；-ism 常形成立场、思想或风格名词。不同学科对 realism 有专门定义，不能由词尾推成同一种理论。',REAL+[['real + -ism → realism','现实取向；写实或现实主义']],
 '日常说 a sense of realism，是对条件和困难有现实判断。文学、艺术中可说写实；哲学、国际关系中的 realism 要按学科理解。',
 'a sense of realism；literary realism；the realism of the painting。',
 'realism 不自动等于 pessimism 悲观：承认困难后仍可行动。realism 是态度或风格，reality 是实际情况。',
 ('We need a little more realism about the cost.','我们需要更现实地看待费用。'),('The film combines fantasy with moments of striking realism.','影片把幻想与一些非常写实的片段结合起来。'))
W('realist','/ˈrɪəlɪst/','现实的人；现实主义者；写实主义者',
 '讨论计划时，总有人追问“钱从哪来、时间够不够”，这样的人可说 a realist。',
 'real + -ist，-ist 表持某种立场或从事某类活动的人；可与 realism 对照，但不据此断言所有学科名称的借入先后。',REAL+[['real + -ist → realist','按现实判断的人；特定现实主义的主张者']],
 'I am a realist 常用来说明自己重视实际条件。an artistic realist 可说写实派人物；作修饰语时如 realist fiction 是现实主义小说。',
 'a political realist；a realist approach；be a realist。',
 'realist 不等于 real person“真实存在的人”；这里 -ist 说的是立场或风格。',
 ('I am a realist: we cannot finish this with only two people.','我是个讲实际的人：只有两个人做不完这些。'),('The novelist is often described as a social realist.','这位小说家常被称为社会现实主义作家。'))
W('unreal','/ʌnˈrɪəl/','不真实的；恍如梦中的；惊人的〔口语〕',
 '一切发生得太顺、太奇怪，像梦里的一幕，令人难以相信。',
 'un-（不）+ real（真实的）。un- 否定整个形容词，不是把单词拆成 u + nreal。',REAL+[['un- + real → unreal','不真实；像不真实一样令人惊讶']],
 '可用于虚构环境，也可描述真实经历带来的梦幻感。口语 That goal was unreal! 可能在夸进球惊人，并非说根本没进。',
 'an unreal atmosphere；feel unreal；an unreal experience。',
 'unreal 说不真实或难以置信；unrealistic 更直接批评设想不切实际。unreal 的夸赞语气不能套到所有句子。',
 ('After so many years, seeing him again felt unreal.','过了这么多年再次见到他，感觉像做梦一样。'),('The game creates a beautiful but unreal landscape.','游戏创造了美丽却不真实的景观。'))
W('surreal','/səˈrɪəl/','超现实的；梦境般荒诞的',
 '普通房间里站着一只穿西装的大鱼：东西都认得，组合起来却像梦。',
 '由 surrealism 逆构缩短而来，联系法语 surréalisme“超现实主义”；可用 sur- 超出 + real 真实理解材料，但英语较短的 surreal 不是必然先于 surrealism。',
 [['法语 sur- + réalisme → surréalisme','超出通常现实的艺术命名'],['英语 surrealism → surreal','由流派名称逆构，形容梦境般不合常理的感觉']],
 '最初关联艺术流派，后来日常用来形容奇异、不像现实的经历；真实发生的事情也可以 feel surreal。不是每件奇怪的事都属于严格的超现实主义作品。',
 'a surreal scene；a surreal experience；feel completely surreal。',
 'unreal 可泛说不真实或太惊人，surreal 更容易让人想到梦中那种熟悉元素之间不合常理的组合。',
 ('The empty airport at noon was a surreal sight.','中午空无一人的机场景象让人觉得像在梦里。'),('It felt surreal to hear my own name announced on stage.','听到台上宣布自己的名字，感觉很不真实。'))
R('B3269','真实、实际；现实','REAL：把想象与真正存在的东西对上','一张地图上的房子，与眼前真正能住的房子。',
 'real 的近源经法语接拉丁 rēs“事物”。先抓住“真有其物”，再看 reality 现实、really 确实、realize 意识到或实现。艺术里的 surreal 又把日常现实组合成梦境般的画面。',
 '-ly 成副词，-ity 说状态，-ism 说思想或风格，-ist 说相应的人，-ize／-ise 构成动词；这些是帮助认形的对应，不代表所有词都先在现代英语中临时拼成。surreal 的英语形成还有由 surrealism 逆构的过程。',
 [['真实及实际','real · really · reality'],['看明白与做出来','realize · realise'],['态度与风格','realism · realist'],['否定或超出现实','unreal · surreal']],
 'real／true：存在真假／说法真假；reality／realism：实际状态／现实取向；realise／release：意识到／释放。',
 'The plan looked ideal, but a realist asked whether it could become a reality.\n\n计划看着理想，一位讲实际的人却问它能否真正实现。',
 'real really reality realize realise realism realist unreal surreal')

COME=[['古英语 cuman → 中古英语 comen','来到、到达'],['英语 come','来；到达；发生']]
W('come','/kʌm/','来；来到；出现；达到',
 '把位置想在说话者或指定目的地：人和事情正在朝这里靠近。',
 '由古英语 cuman 经中古英语 comen 延续，属于日耳曼语本族词；过去式 came、过去分词 come，不按普通动词一律加 -ed。',COME,
 'Come here 是来到这里；come to an agreement 是达到共识；The answer came to me 是答案浮现在脑中。强调接近的参照点可以是说话者、听话者或约定地点。',
 'come home；come from；come true；come to an agreement。',
 'come 朝语境中的中心走，go 往另一处走。电话里说 I’m coming 可以是朝听话者那里去，不能机械按中文“去”就用 go。',
 ('Can you come to my office after lunch?','午饭后你能来我办公室吗？'),('The two sides finally came to an agreement.','双方终于达成了协议。'))
W('become','/bɪˈkʌm/','变成；成为；适合〔较正式〕',
 '不仅走到一个地点，还进入一种新身份或状态：从学生成为老师。',
 '古英语 becuman 是 be- 与 cuman 的旧组合，原有到达、发生、适合等义，后来发展出现代“成为”。be- 这里不等于现代独立动词 be。',COME[:1]+[['古英语 becuman → 中古英语 becomen','来到、到达；适合'],['英语 become','进入某种状态、成为']],
 'become + 名词或形容词，如 become a doctor、become quiet。That colour becomes you 是较正式的“那个颜色很衬你”，不能按“你变成颜色”理解。',
 'become clear；become aware of；become a member；become ill。',
 'be 表示已经处在状态，become 强调转入状态。He is angry 是他生气；He became angry 是他开始变得生气。',
 ('The reason became clear when we checked the records.','我们查过记录后，原因变清楚了。'),('She became a teacher after working as an engineer.','她当过工程师，后来成为了教师。'))
W('coming','/ˈkʌmɪŋ/','即将到来的；来临；come 的 -ing 形式',
 '日历上一页还没翻过来，但那一天已经在朝你走近。',
 'come 去词末不发音 e 加 -ing；古英语及中古英语已有相应分词形式，现代形容词和名词用法接此发展。',COME+[['come + -ing → coming','正在来；即将到来；来临']],
 'the coming week 是接下来的一周；the coming of spring 是春天的到来；I’m coming 是我来了。并不是看到 -ing 都必须翻成“正在”。',
 'the coming year；in the coming weeks；the coming of spring。',
 'coming 在时间名词前说即将到来；upcoming 也常如此。a coming event 不是某件事情在物理空间里走动。',
 ('We will discuss the budget in the coming weeks.','我们会在接下来的几周讨论预算。'),('The coming of spring brought warmer days.','春天来临，天气暖和起来。'))
W('income','/ˈɪnkʌm/','收入',
 '想象一个家庭的账本：每月不断流进来的钱，就是 income。',
 '由中古英语 income 延续，可能承接古英语 incyme“进入”；对应 in-（向内）+ come。现代收入义从进来的东西、收益发展。',
 [['中古英语 income；可能承接古英语 incyme','进入、进来的事物'],['英语 income','流入的收益 → 收入']],
 '可说工资、租金等收入，通常作不可数名词。income 并不自动等于花完费用后剩下的净利润；谈具体统计需看 gross、net 等限定。',
 'annual income；a source of income；a low income；income tax。',
 'income 是收入，salary 是雇员的固定工资，profit 是收益减去相应成本后的利润；同一笔钱的观察角度不同。',
 ('Rent is her main source of income.','租金是她的主要收入来源。'),('The family spends nearly half its income on housing.','这一家把将近一半的收入花在住房上。'))
W('comer','英 /ˈkʌmə/；美 /ˈkʌmər/','来的人；有发展前景的人',
 '走进门来的人是 comer；在竞争里刚冒出头、很有潜力的人也能这样叫。',
 'come + -er，-er 表执行动作的人；中古英语已有 comere。现代常出现在 all comers、newcomer 等表达中。',COME+[['come + -er → comer','到来的人；后来也说前景看好者']],
 'all comers 是所有前来的人，不论背景。a comer 表有前途者较带口语或体育色彩，普通介绍新同事更常用 newcomer。',
 'all comers；open to all comers；a promising comer。',
 'comer 不等于所有语境的 visitor；访客是按访问身份称呼，comer 主要按“来到”这个动作称呼。',
 ('The race is open to all comers.','这场比赛任何人都可以报名参加。'),('The young player was already being described as a comer.','这名年轻球员已经被视为很有前途的新秀。'))
R('B2841','来、到达；进入一种状态','COME：人或事情朝某个参照点靠近','可以来到门口，也可以让一个状态或结果终于到来。',
 'come 是古英语 cuman 的后代。become 让“到达”走向“进入状态”，income 关注进来的收益；welcome 与 outcome 已有完整精讲，在本页一起复习。',
 'come／came／come 的词形不规则；coming 去末尾 e 加 -ing。become 的 be- 是旧构词材料，不把它等同于今天独立使用的 be。income、outcome 是方向与结果相关名词，不套进“里面来、外面来”的逐字翻译。',
 [['来到与来临','come · coming · comer'],['进入状态','become'],['收入与结果','income · outcome'],['欢迎','welcome']],
 'come／go 取决于参照点；income／outcome 并不是简单的一进一出，后者常是结果。',
 'Come early, and the purpose of the meeting will become clear.\n\n早点来，会议的目的就会清楚了。','come coming comer become income outcome welcome')

NEED=[['古英语 nīed／nēd；nēod','必要、迫切需要；欲求'],['中古英语 nede → 英语 need','需要；有必要']]
W('need','/niːd/','需要；必要；需求',
 '缺了这件东西，事情就办不成；need 指向这个缺口。',
 '中古英语合流了古英语表示必要的 nīed／nēd 与表示欲求的 nēod 等形式。现代 need 可作名词、普通动词，也有情态用法。',NEED,
 'I need help 是需要帮助，You need to rest 是有必要休息。needn’t 表没有必要；名词 in need 是处于困境、需要帮助。',
 'need to do；need help；meet a need；in need。',
 'needn’t go 是不必去，mustn’t go 是禁止去。need 强调必要，want 常只是想要；二者在实际对话里也可重叠。',
 ('You need to save the file before closing it.','关闭文件前你需要先保存。'),('The charity supports families in need.','这家慈善机构帮助有困难的家庭。'))
W('needed','/ˈniːdɪd/','需要的；need 的过去式、过去分词',
 '缺口已经明确，正好能填这个缺口的东西就是 needed。',
 'need + -ed；词末 /d/ 后的 -ed 读 /ɪd/，因此 needed 是两个音节。过去分词可用于被动，也可修饰名词。',NEED+[['need + -ed → needed','过去需要；被需要；所需的']],
 'Help is needed 是现在需要帮助，不因 needed 有 -ed 就成了过去。We needed help 才由过去式说明当时需要。much-needed 常作带连字符修饰语。',
 'the information needed；help is needed；more time was needed。',
 'needed 是否有过去时间，要看整个结构。is needed 是现在时的被动；was needed 才把需要放到过去。',
 ('No special equipment is needed.','不需要特殊设备。'),('We needed more time to check the results.','我们当时需要更多时间检查结果。'))
W('needless','/ˈniːdləs/','不必要的；无谓的',
 '这段麻烦原本可以省掉，做了也没带来必要的好处。',
 'need + -less，-less 表没有；对应“没有必要”。中古英语已有同族形式，不是针 needle 的派生。',NEED+[['need + -less → needless','没有必要的 → 多余、无谓的']],
 'needless worry 是无谓的担心。Needless to say 是不用说、显然；它常用来引出听者大概已能猜到的结果。',
 'needless delay；needless expense；needless to say。',
 'needless 常评价某事本可避免；unneeded 直接说没有被需要。needless 不是“没有针”。',
 ('A clear checklist can prevent needless delays.','清楚的检查清单可以避免不必要的延误。'),('Needless to say, everyone was relieved when the child was found.','不用说，找到孩子后大家都松了口气。'))
W('needy','/ˈniːdi/','贫困的；过分需要关注的',
 '一面是缺少生活必需品，一面是心里总觉得缺关爱，需要别人不断回应。',
 '接中古英语 nedy、古英语 nēdiġ 等形式；现代可对应 need + -y，-y 表带有这种性质。历史并非从现代英语才第一次造出。',NEED[:1]+[['古英语 nēdiġ → 中古英语 nedy','处于需要、匮乏之中'],['英语 needy','贫困的；情感上过度依赖关注的']],
 'needy families 是生活贫困的家庭；a needy partner 可带负面评价，说伴侣不断索取关注。后一个意思并不说明这个人经济贫困。',
 'needy families；the needy；emotionally needy。',
 'needy 描述匮乏或依赖，needed 表别人需要它。a needy person 和 a needed person 的方向正好不同。',
 ('The programme provides meals for needy families.','这个项目给贫困家庭提供餐食。'),('He worried that asking for constant reassurance made him seem needy.','他担心不断要求安慰会显得过度依赖别人。'))
W('needful','/ˈniːdfəl/','必要的；所需的〔较正式或旧式〕',
 '把当下确实该做、该有的那一部分挑出来。',
 '接古英语 nēodful 与中古英语 needeful；可对应 need + -ful。-ful 在此表示与需要有关、必要，不是“需要装得很满”。',NEED[:1]+[['古英语 nēodful → 英语 needful','必要的；需要的']],
 '现代通常用 necessary 或 needed 更自然。do the needful 在部分地区英语、尤其南亚商务英语中表示办理所需事项，跨地区沟通时写清具体动作更明确。',
 'what is needful；needful information；do the needful。',
 'needful 不等于 needy；前者通常说事情必要，后者可说人贫困或过分依赖关注。',
 ('She supplied all that was needful for the journey.','她提供了旅途所需的一切。'),('The older letter asks the clerk to do the needful.','这封旧信请办事员办理必要事项。'))
R('B3918','需要；必要','NEED：缺了它，事情就难办','水杯空了要水，任务太赶要时间，都是一个需要填上的缺口。',
 'need 的本族历史涉及必要与欲求两类古英语形式。先看 need 的需要，再区分 needed 被需要、needless 不必要、needy 匮乏或过分依赖关注。',
 '-ed 在 needed 中读 /ɪd/；-less 否定必要性，-y 描述需要帮助的性质。needful 较正式或旧式，不把它当作 everyday necessary 的唯一替代。原表 needling 有极少见 need 的派生分析，日常常见 needling 实际多来自 needle，本页暂略以免混淆。',
 [['需要与被需要','need · needed'],['没有必要','needless'],['匮乏与必要','needy · needful']],
 'needn’t：不必；mustn’t：不许。needy：需要帮助；needed：被别人需要。',
 'We needed help, but a simple explanation prevented needless worry.\n\n我们需要帮助，但一个简单解释就避免了无谓担忧。','need needed needless needy needful')

LOVE=[['古英语 lufu；lufian','爱；爱、喜爱这一动作'],['中古英语 love → 英语 love','爱；喜爱；亲爱之情']]
W('love','/lʌv/','爱；喜爱；爱好',
 '一个人或一件事让你愿意亲近、关心、反复回去。',
 '名词接古英语 lufu，动词接 lufian，经中古英语延续。是日耳曼语本族词，不需硬拆成更小的现代英语片段。',LOVE,
 'love a person 可以是家人、朋友或恋人之爱；love reading 是非常喜欢阅读。I’d love to 是很愿意。体育计分的 love 有“零分”用法，命名的更远解释存在争论，不借此反推爱情义。',
 'fall in love；love doing something；I’d love to；with love。',
 'love 的分量由关系和语境决定：I love this soup 是夸汤好喝，不是表白；like 通常更轻一些。',
 ('I love the way she tells stories.','我很喜欢她讲故事的方式。'),('He shows his love by making time for his family.','他通过抽时间陪家人表达爱。'))
W('loved','/lʌvd/','被爱的；love 的过去式、过去分词',
 '爱落在这个人身上：他知道自己被关心、被珍惜。',
 'love 加 -d；过去式与分词接续古英语相应动词形式。结尾读 /vd/，-ed 不另外增加一个音节。',LOVE+[['love + -ed → loved','曾喜爱；被爱、受喜爱的']],
 'She loved it 是她当时很喜欢；She felt loved 是她感到自己被爱。a loved one 常指亲人或挚爱之人，复数 loved ones 很常见。',
 'feel loved；a loved one；loved ones。',
 'loved 关注爱已经落在对象身上，lovable 关注这个对象讨人喜欢、值得爱，不保证事实上有谁爱他。',
 ('Every child deserves to feel loved.','每个孩子都值得感受到爱。'),('She called her loved ones as soon as she arrived.','她一到就给亲人打了电话。'))
W('lovely','/ˈlʌvli/','可爱的；美好的；令人愉快的',
 '天气、笑容或一顿饭，让你看见就觉得舒服、喜欢。',
 '接古英语 luflīċ，经中古英语延续；现代对应 love + -ly。这里 -ly 是形容词构词材料，不把 lovely 当成修饰动作的普通副词。',LOVE[:1]+[['古英语 luflīċ → 英语 lovely','惹人喜爱的 → 美好、令人愉快的']],
 'a lovely day 可说天气或一天过得好；That’s lovely 常是温暖的赞许。英式口语尤其常见，也可夸人的态度亲切。',
 'a lovely smile；a lovely day；lovely to meet you。',
 'lovely 是形容词：She has a lovely voice；不能用 She sings lovely 代替标准的 She sings beautifully。',
 ('We had a lovely evening by the river.','我们在河边度过了一个愉快的夜晚。'),('It was lovely to see you again.','再次见到你真高兴。'))
W('lover','英 /ˈlʌvə/；美 /ˈlʌvər/','恋人；情人；爱好者',
 '有人把心放在某个人身上，也有人把热情放在书、音乐或自然上。',
 'love + -er，-er 表做某事的人；中古英语已有相应形式。具体是哪种爱，由前后搭配说明。',LOVE+[['love + -er → lover','爱某人或某事的人']],
 'a music lover 是音乐爱好者；his lover 则通常有恋爱、亲密关系意味，某些语境还暗示婚外情。介绍普通朋友不宜随便叫 my lover。',
 'a book lover；nature lovers；former lovers。',
 'lover 单独谈人与人关系时比 fan 强得多；a coffee lover 却只是咖啡爱好者。',
 ('The town is popular with nature lovers.','这个小镇很受自然爱好者欢迎。'),('The novel follows two lovers separated by war.','小说讲述两个因战争分离的恋人。'))
W('lovable','/ˈlʌvəbəl/','惹人喜爱的；可爱的',
 '也许有点笨拙或淘气，却让人忍不住喜欢、愿意包容。',
 'love + -able；-able 表可被、值得，词末 e 常在此拼写中省去。也见 loveable，不能以为这两种拼写指不同性格。',LOVE+[['love + -able → lovable','值得爱、容易让人喜爱的']],
 '常用于人、动物或角色：a lovable character 不一定完美，可能缺点恰好增加亲切感。比 lovely 更突出对象让人产生喜爱之情。',
 'a lovable child；a lovable character；a lovable rogue。',
 'lovable 是容易让人爱，loving 是主动给予爱。a loving parent 是充满关爱的家长，不只说他可爱。',
 ('The dog is noisy but very lovable.','这只狗虽然吵，却非常讨人喜欢。'),('The actor turned a minor role into a lovable character.','这位演员把一个小角色演得很惹人喜爱。'))
W('loveless','/ˈlʌvləs/','缺乏爱的；没有爱情的',
 '两个人还坐在同一张餐桌旁，关心和亲近却已经不在了。',
 'love + -less；-less 表缺少。中古英语已有相应形式；这里否定的是爱，不是“被爱次数少”。',LOVE+[['love + -less → loveless','缺少爱或爱情的']],
 'a loveless marriage 常说婚姻形式仍在，却缺乏爱情；a loveless childhood 可说缺少关爱的童年。关系是否真实存在，与其中有没有温情是两件事。',
 'a loveless marriage；a loveless relationship；a loveless childhood。',
 'loveless 不必等于 lonely 孤独：可以住在很多人当中，却感受不到爱。',
 ('The novel describes a loveless marriage.','小说描写了一段没有爱情的婚姻。'),('She wanted to give her children the warmth missing from her own loveless childhood.','她想给孩子温暖，弥补自己缺少关爱的童年。'))
W('lovesick','/ˈlʌvsɪk/','苦苦相思的；为情所困的',
 '人没在眼前，心却总围着他转，连饭都不想好好吃。',
 'love（爱）+ sick（不适的）。两个成分并列组合，表示因爱情而苦恼，不是某种可由词名确诊的疾病。',
 [['英语 love；sick','爱情；难受、不适'],['love + sick → lovesick','因相思或爱情不顺而苦恼']],
 '常用于文学或带一点调侃的描述，可能是想念、不被回应或失恋带来的心神不宁，不专指某一种恋爱结局。',
 'a lovesick teenager；a lovesick expression；feel lovesick。',
 'lovesick 强调爱情引起的难受，homesick 是想家；二者都利用 sick 表情绪困扰，不直接等于感染性疾病。',
 ('The lovesick teenager kept checking his phone.','那个苦苦相思的少年不停地看手机。'),('She wrote a song about a lovesick sailor.','她写了一首关于相思水手的歌。'))
W('lovelorn','英 /ˈlʌvlɔːn/；美 /ˈlʌvlɔːrn/','失恋的；为情忧伤的〔文学〕',
 '想要的爱情失去了或得不到，只留下一个人发愁。',
 'love + lorn；lorn 是与 lose 同族的旧“失去、被抛下”的形式。不能把后半截看成普通现代名词，也不按 love + learn 理解。',
 [['英语 love；旧形容词 lorn','爱情；失去、被遗弃的'],['love + lorn → lovelorn','因失去或得不到爱情而忧伤']],
 '比 lovesick 更有文学色彩，常描写失恋者或单相思者。可说 lovelorn poetry，强调作品里为情伤感的情绪。',
 'a lovelorn poet；a lovelorn young man；lovelorn songs。',
 'lovelorn 偏爱情受挫的忧伤；loveless 直接说缺少爱，不必带着一个人思恋另一个人的画面。',
 ('The lovelorn poet filled his notebook with sad verses.','这位失恋的诗人在本子上写满伤感诗句。'),('The film gently mocks its lovelorn hero.','影片温和地调侃着为情所困的男主角。'))
W('lovemaking','/ˈlʌvˌmeɪkɪŋ/','性爱；做爱',
 '这里的 make love 已是固定表达，说的是亲密的性行为。',
 'love + making，联系 make love 这一表达的名词化；早期 make love 有求爱、示爱用法，现代 lovemaking 常指性行为。两个来源成分并列，不把 love 画成 make 的祖先。',
 [['英语 love；make／making','爱；做、进行'],['make love → lovemaking','固定表达的名词形式，现代通常指性爱']],
 '通常作不可数名词，语气相对委婉，见小说、电影评论或关系描述。它不是任何制作爱心礼物、表达关心行为的通称。',
 'a scene of lovemaking；tender lovemaking；an intimate relationship。',
 'showing love 范围很广，包含照料和关心；lovemaking 在现代通常有明确的性意味，不能互换。',
 ('The film suggests intimacy without showing the lovemaking.','影片暗示了亲密关系，没有展示性爱过程。'),('The novel describes their lovemaking in restrained language.','小说用克制的语言描写两人的性爱。'))
R('B2518','爱；喜爱；亲爱之情','LOVE：愿意靠近，也愿意关心','对亲人的牵挂、对食物的喜欢和恋人的爱情，都有不同程度的投入。',
 'love 来自古英语 lufu 等形式。本页先从实际对象和语气理解爱，再分清 lovely 美好、lovable 讨人喜欢、loved 被爱；缺爱与相思又形成 loveless、lovesick 等表达。',
 '-ly 在 lovely 中造形容词，-able 表容易被喜爱，-less 表缺少。lover 单独用于关系时有亲密含义，music lover 则是爱好者。lovelorn 的 lorn 是旧“失去”形式；lovemaking 有现代固定性意味。',
 [['爱与被爱','love · loved'],['让人喜欢','lovely · lovable'],['人及关系','lover · lovemaking'],['缺爱与相思','loveless · lovesick · lovelorn']],
 'lovely：美好；lovable：惹人喜爱；loved：受到爱。loveless：缺爱；lovesick：相思难受。',
 'The lovable dog was clearly loved, and even a short walk made the day feel lovely.\n\n这只讨人喜爱的狗显然很受宠，连一次短短的散步都让这一天变得美好。',
 'love loved lovely lovable lover loveless lovesick lovelorn lovemaking')

HELP=[['古英语 help；helpan','帮助；帮助这一动作'],['中古英语 help／helpen → 英语 help','帮助、协助；使情况好转']]
W('help','/help/','帮助；改善；有帮助',
 '一个人搬不动箱子，另一双手过来分担一点，让事情容易完成。',
 '来自古英语 help、helpan 等名词动词形式，经中古英语延续。现代过去式 helped；旧本族动词形式并不都照现代规则变化。',HELP,
 'help someone do 或 help someone to do 都可说帮助做事。This helps 表示这样有用。can’t help doing 是忍不住做，不能按“不能帮助做”直译。',
 'help with；help someone do；help yourself to；can’t help laughing。',
 'help someone 是帮人，help oneself to food 是自己取食物。helpful 是带来帮助，不只是“愿意提供帮助”的口头态度。',
 ('Could you help me carry this box?','你能帮我搬这个箱子吗？'),('A short break might help you concentrate.','短暂休息可能有助于你集中注意力。'))
W('helping','/ˈhelpɪŋ/','一份食物；帮助；help 的 -ing 形式',
 '盛饭时勺子一次给你盛到盘里的那一份，就是 a helping。',
 'help + -ing；除了帮助的动作名词、分词用法，食物份量义与 help someone to food“给人取食物”相连。',HELP+[['help + -ing → helping','帮助这一动作；由取食物用法发展出一份食物']],
 'a second helping 是再来一份；helping hands 指帮手或伸出的援手。We are helping 中则只是动词形式，不要把所有 helping 都理解成餐点。',
 'a helping of rice；a second helping；a helping hand。',
 'helping 是食物一次分给或取用的量，portion 范围更广，可以强调一部分或一份的大小。',
 ('Would you like a second helping of soup?','你还要再来一份汤吗？'),('Thanks for giving us a helping hand.','谢谢你帮了我们一把。'))
W('helpful','/ˈhelpfəl/','有帮助的；乐于助人的',
 '一句说明正好解开问题，或一个人主动把你卡住的地方处理了。',
 'help + -ful；-ful 在这里造“具有帮助作用”的形容词。中古英语已有同形相关用法，不按字面译成“满是帮助”。',HELP+[['help + -ful → helpful','提供帮助或能派上用场的']],
 'a helpful guide 是能解决问题的指南；helpful staff 是愿意并能给顾客帮助的工作人员。helpful to someone、helpful for doing 常说明对象或用途。',
 'helpful advice；a helpful suggestion；find something helpful。',
 'helpful 评价帮助作用，useful 评价有用途；a useful tool 不一定像 a helpful person 那样带有待人友善的意味。',
 ('The receptionist was friendly and helpful.','接待员亲切又乐于助人。'),('It would be helpful to see a concrete example.','看一个具体例子会有帮助。'))
W('helpless','/ˈhelpləs/','无助的；无能为力的',
 '事情在眼前发生，你却没有办法改变，也没有力量照顾自己。',
 'help + -less，对应缺少帮助或行动能力；中古英语有 helples，相关更早形式属于日耳曼语本族词。',HELP+[['help + -less → helpless','得不到帮助或无力应对的']],
 'feel helpless 是感到无能为力；a helpless baby 强调需要照料，不是责怪婴儿没用。helpless with laughter 还可说笑得无法控制。',
 'feel helpless；a helpless victim；helpless with laughter。',
 'helpless 强调无法应对，hopeless 强调没有希望，或口语里某方面很差；需要帮助的人不一定没有希望。',
 ('I felt helpless as I watched the water rise.','看着水位上涨，我感到无能为力。'),('The newborn puppy was tiny and helpless.','刚出生的小狗又小又需要照料。'))
W('helper','英 /ˈhelpə/；美 /ˈhelpər/','帮手；协助者',
 '不是独自负责全部事情，而是在一旁分担步骤、递东西、完成部分任务的人。',
 'help + -er；-er 表做这个动作的人，接中古英语 helpere 等本族形式。不是把 helper 强制限定为某种职位等级。',HELP+[['help + -er → helper','帮助做事的人']],
 '可说志愿活动中的帮手、课堂助手，也用于某些软件名称里的辅助模块。具体职位须看语境，不能一律翻为秘书。',
 'a volunteer helper；a classroom helper；a willing helper。',
 'helper 是宽泛的协助者；assistant 可是较明确的岗位或职称。两者都不保证对方只做体力劳动。',
 ('We need two helpers to set up the chairs.','我们需要两名帮手摆椅子。'),('The teacher thanked the classroom helpers.','老师感谢了课堂小帮手。'))
W('helpline','/ˈhelplaɪn/','求助热线；咨询热线',
 '遇到问题时，有一条能联系到提供帮助的人的电话线。',
 'help（帮助）+ line（电话线路）。两个现有成分组合成名词，line 在此说联络渠道，不是画在纸上的直线。',
 [['英语 help；line','帮助；电话线路'],['help + line → helpline','提供咨询或帮助的热线']],
 '可用于技术、消费、健康或其他支持服务，不自动表示紧急报警号码；是否全天、免费须看具体服务。',
 'call a helpline；a customer helpline；a confidential helpline。',
 'helpline 重在提供帮助；hotline 更泛指专用快速联络线，也可能是投诉、举报或机构间联络。',
 ('The company lists its customer helpline on the receipt.','公司在收据上印有客服热线。'),('She called the helpline to ask about the application form.','她拨打咨询热线询问申请表的事情。'))
R('B3201','帮助；使事情更容易','HELP：多一双手，让困难轻一点','箱子太重时有人扶一把，说明太难时有人举个例子。',
 'help 接古英语本族形式，既说帮助别人，也说某种方法管用。helpful 有帮助，helper 是帮手，helpless 却说无力应对。helping 还发展出一份食物这个常用意思。',
 '-ful 表具有帮助作用，-less 表缺少帮助或应对能力，-er 指人。helping 的食物义与给人取食物相连；helpline 的 line 是电话联络渠道。',
 [['动作与帮手','help · helper'],['有帮助与无助','helpful · helpless'],['份量及渠道','helping · helpline']],
 'helpless：无力应对；hopeless：没有希望。helpful 是形容词；helping 除了动词形式，也可指一份食物。',
 'A helpful neighbour offered to help, and I no longer felt helpless.\n\n一位热心邻居主动帮忙，我不再感到无助。','help helper helpful helpless helping helpline')

W('great','/ɡreɪt/','很好的；伟大的；程度或规模大的',
 '某件事超出平常水平：可以大在体积、强在程度，也可以好到让人赞叹。',
 '从古英语 grēat“大、粗、厚”等义经中古英语延续，后来发展出重要、出众和很好的评价。不是 grey 灰色加上 t。',
 [['古英语 grēat → 中古英语 greet','大、厚、规模显著'],['英语 great','很大的；重要出众的；很好的']],
 'a great artist 是出色的艺术家；a great deal of time 是大量时间；Great! 是好极了。a great friend 常夸关系或品格，a big friend 更容易被听成身材。',
 'a great idea；a great deal of；great importance；have a great time。',
 'great 常是赞许，也能只说程度：great pain 是剧痛，并不是“很棒的疼痛”。good 与 great 的强度差由语境决定。',
 ('That is a great idea.','那是个很棒的主意。'),('She went to great lengths to make everyone feel welcome.','她花了很大心思，让每个人都觉得受到欢迎。'))
W('greatness','/ˈɡreɪtnəs/','伟大；卓越；巨大',
 '从一次做得好，抬高到这个人或作品整体让人敬佩的品质。',
 'great + -ness；-ness 把形容词变成性质名词，古英语 grēatnes 已有对应形式。词义可接规模大，也可接卓越。',
 [['古英语 grēat + -nes → grēatnes','巨大、重要的性质'],['英语 greatness','伟大、卓越或巨大的程度']],
 'the greatness of a leader 常谈成就与品格，achieve greatness 是取得卓越成就。通常不可数，不能把一个伟人直接叫 a greatness。',
 'achieve greatness；the greatness of the work；true greatness。',
 'greatness 是品质或程度，a great 是某领域的杰出人物，如 one of the greats；词性和数法不同。',
 ('The greatness of the novel lies in its attention to ordinary lives.','这部小说的卓越之处在于它关注普通人的生活。'),('She believed that kindness was part of true greatness.','她相信善良是真正伟大的一部分。'))
R('B3442','大；出众；很好的','GREAT：超过平常的规模、程度或水平','大到显眼，出色到让人赞叹；具体褒贬还看后面的对象。',
 'great 最早的本族词义偏大、粗厚，现代延伸到重要、卓越和很好。greatness 用名词说这种巨大或出众的性质。',
 'great + -ness 对应性质名词。great 与 greatness 的语义不只有夸奖：great danger 是巨大危险，不会因为 great 常表示很棒就变成赞美。',
 [['程度与评价','great'],['性质与卓越','greatness']],
 'great 是形容词，greatness 是名词；one of the greats 则把 great 当作杰出人物的名词。',
 'A great work can make us rethink what greatness means.\n\n一部出色的作品会让我们重新思考何为卓越。','great greatness')

if __name__=='__main__':save('continuation_20261028_d',ROOTS,WORDS)
