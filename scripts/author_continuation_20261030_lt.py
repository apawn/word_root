"""Surf, rational and rat."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['较早 suff、suffe 等 → surf','岸边涌浪、碎浪；更早来源有声音、借词等不同分析'],['名词 → 动词','在浪上滑行、冲浪'],['现代比喻与后缀','浏览网络；surfing 活动，surfer 人，surfboard 板']]
W('surf','英 /sɜːf/；美 /sɜːrf/','拍岸碎浪；冲浪；浏览网络等',
 '浪到岸边翻白、碎开，是 surf；人借着浪面滑行，就用同一个词作冲浪动词。网上一个页面跳到另一个页面，也借成 surf the web。',
 '可能来自较早 suff、suffe，表示岸边涌浪，更早来源未定。名词成冲浪动词，随后浏览网络等比喻突出，不把它误拆成 surface 的固定缩写。',S,
 'the sound of the surf 拍岸浪声，surf the waves 冲浪，surf the web 浏览网络，surf channels 来回换电视台。',
 'the surf；surf the web。',
 'surf 名词常指一片近岸浪，不只是随便一个 wave；网络 surf 不需要真的有水，也不保证有明确搜索目标。',
 ('We listened to the surf from the balcony.','我们在阳台听拍岸浪声。'),('He spent the evening surfing the web.','他晚上一直在浏览网络。'),sources=['https://en.wiktionary.org/wiki/surf#English','https://www.etymonline.com/word/surf'])
W('surfing','英 /ˈsɜːfɪŋ/；美 /ˈsɜːrfɪŋ/','冲浪运动；网上浏览',
 'surf 是做动作，surfing 是把整项活动拿出来说。go surfing 多指去冲浪；web surfing 看的是网上浏览。',
 'surf + -ing，动作名词、现在分词。物理运动和网络比喻都继承 surf 的相应用法。',S[:2]+[['surf + -ing → surfing','冲浪活动；浏览网络的活动']],
 'go surfing 去冲浪，learn surfing 学冲浪，web surfing 网上浏览，a surfing lesson 冲浪课。',
 'go surfing；a surfing lesson；web surfing。',
 'surfing 不是冲浪者；人用 surfer，板用 surfboard。上下文无网络对象时，运动义更直观。',
 ('They went surfing early in the morning.','他们一大早去冲浪。'),('Web surfing took up most of his break.','他休息时大部分时间都在网上浏览。'))
W('surfer','英 /ˈsɜːfə/；美 /ˈsɜːrfər/','冲浪者；网上浏览的人',
 '做 surf 的人就是 surfer。在海边是踩板乘浪的人，在网络语境则是浏览网页的人。',
 'surf + -er，人物后缀。动词的运动、比喻义都能形成相应参与者名称。',S[:2]+[['surf + -er → surfer','参与冲浪或网上浏览的人']],
 'an experienced surfer 有经验的冲浪者，a web surfer 网上浏览者，a surfer riding a wave 踩着浪前进的冲浪者。',
 'an experienced surfer；a web surfer。',
 'surfer 是人，surfing 是活动；名词 -er 也不表示比赛成绩等级。',
 ('A surfer waited beyond the breaking waves.','一位冲浪者在碎浪外侧等待。'),('The site aims to help web surfers find local events.','网站旨在帮助上网浏览的人找到本地活动。'))
R('B4144','岸边涌浪到乘浪，再借为页面间浏览','SURF：先有岸浪，再有人沿浪滑行','surf → surfing、surfer、surfboard。',
 '浪是环境，surfing 是活动，surfer 是人，surfboard 是所用板。网络用法沿着滑行、跳转的意象另开一支。',
 'suffe 等 → surf，远源未定；-ing 活动，-er 人，board 板。',
 [['浪、活动与参与者','surf · surfing · surfer'],['运动器材','surfboard']],
 'surf 不一定是 surface 缩写；网络浏览不必有明确搜索目标；surfside 等较少用扩展先略过。',
 'The surfer carried her surfboard down to the beach.\n\n冲浪者把冲浪板带到海滩。','surf surfing surfer surfboard')
Ra=[['拉丁 ratiō 计算、推理、道理 → ratiōnālis','与理性、推理相关'],['法语、英语 rational 词族','合理、理性的性质与方式'],['抽象名词与学说','rationality 理性；rationalism 理性主义；rationalist 相应人物']]
W('rationality','/ˌræʃəˈnæləti/','理性、合理性',
 '结论有没有理由支撑，行动能否在目标和证据之间说得通，这种理性、合理的性质就是 rationality。它不只是表面镇定。',
 '联系法语 rationalité、拉丁 ratiōnālitās，现代对应 rational + -ity；重音移到 -nal-，元音也变化。更里层 ratiō 联系计算、推理、道理。',Ra[:2]+[['rational → rationality','理性的性质、合理程度']],
 'the rationality of a decision 决定的合理性，question the rationality of something 质疑其合理性，human rationality 人的理性。',
 'the rationality of；question the rationality。',
 'rationality 不等于没有感情；也不单指算数快。哲学、经济学等领域对它可有具体定义。',
 ('The committee questioned the rationality of the decision.','委员会质疑这个决定是否合理。'),('Her argument appealed to both rationality and compassion.','她的论证同时诉诸理性和同情心。'))
W('rationally','/ˈræʃənəli/','理性地、合乎道理地',
 '把证据、理由摆出来想一想，用 rationally 说明思考、讨论的方式。它说怎样作判断，而不是只看语气冷不冷。',
 'rational + -ly，性质变方式副词；保留 rational 的词干和重音。',Ra[:2]+[['rational + -ly → rationally','以理性、合理方式行动']],
 'think rationally 理性思考，discuss rationally 理性讨论，act rationally 合理行事。',
 'think rationally；discuss rationally。',
 'rationally 是副词，a rational explanation 仍要用形容词；有情绪也可以努力理性分析。',
 ('They tried to discuss the problem rationally.','他们试着理性讨论问题。'),('It was hard to think rationally while everyone was shouting.','人人都在喊时，很难理性思考。'))
W('rationalism','/ˈræʃənəlɪzəm/','理性主义、唯理论；强调理性论证的立场',
 '哲学里会问：有些知识能不能不用感官经验作根据，靠理性推演、先天概念等得到？rationalism 通常重视这条理性知识来源。广义也能说重视理性而非盲从权威的立场。',
 'rational + -ism，形成学说、思想立场名词。哲学认识论与较宽的文化用法有重合，也有不同关注点。',Ra,
 'philosophical rationalism 哲学理性主义，rationalism and empiricism 理性主义与经验主义。具体哲学家不必在所有知识领域都站同一边。',
 'rationalism and empiricism；philosophical rationalism。',
 'rationalism 不只是每次冷静说话，也不等于否认所有经验；它常在讨论知识怎样获得，需和普通 rational 性质分开。',
 ('The seminar compared rationalism and empiricism as accounts of knowledge.','研讨课比较理性主义与经验主义对知识来源的解释。'),('Her essay traces the influence of rationalism on the debate.','她的文章追溯理性主义对这场论争的影响。'),sources=['https://en.wiktionary.org/wiki/rationalism#English','https://plato.stanford.edu/entries/rationalism-empiricism/'])
W('rationalist','/ˈræʃənəlɪst/','理性主义者、唯理论者；主张以理性论证的人',
 'rationalism 是立场、学说，rationalist 是支持、实践相应立场的人。哲学语境多说知识来源，广义语境也可说理性论证的支持者。',
 '联系法语 rationaliste，现代对应 rational + -ist。人物后缀与 -ism 的思想名词相配，但两者不是同一词性。',Ra,
 'a rationalist philosopher 理性主义哲学家，rationalist arguments 理性主义者的论证，a rationalist approach 理性主义取向。',
 'a rationalist philosopher；rationalist arguments。',
 '一个 rational person 不自动就是哲学上的 rationalist；前者评价思考合理，后者常表明具体立场。',
 ('The rationalist argued that some knowledge does not depend on sense experience.','这位理性主义者认为，有些知识不依赖感官经验。'),('The book discusses several rationalist philosophers.','书里讨论了几位理性主义哲学家。'),sources=['https://en.wiktionary.org/wiki/rationalist#English','https://plato.stanford.edu/entries/rationalism-empiricism/'])
R('B2597','计算、推理与道理，分出普通性质和哲学立场','RATIONAL：判断能说出理由，学说还会追问知识从哪来','rational → rationally、rationality；rationalism → rationalist；rationalization 另看合理化、解释等固定义。',
 '理性思考是一般方式，理性主义是知识来源等问题上的立场。这样区分，就不会把每个讲道理的人都自动归入一个哲学流派。',
 'ratiō → ratiōnālis → rational；-ly 方式，-ity 性质，-ism 学说，-ist 人物，-ization 过程名词。',
 [['普通性质、方式与抽象名词','rational · rationally · rationality'],['学说与人物','rationalism · rationalist'],['合理化等过程','rationalization']],
 '理性不要求没有情绪；rationalism 不一律否认经验；rationalization 可中性也可说为行为找借口，须看场景。',
 'The rationalist explained his view rationally.\n\n那位理性主义者用理性论证说明自己的观点。','rational rationally rationality rationalism rationalist rationalization')
Rt=[['古英语 ræt → 中古英语 ratte 等 → rat','鼠类旧名，更远来源与传播方向有争论'],['动物 → 人物、行为比喻','rat 叛徒、告密者；rat on 告发'],['rat + -y → ratty','像鼠、破旧邋遢；烦躁易怒等口语义']]
W('rat','/ræt/','大鼠；〔贬义〕叛徒、告密者；告发',
 '动物里 rat 常说较大的鼠；骂人 a rat 多是在说背叛、出卖。rat on someone 则是把某人的事告出去，带说话人的负面态度。',
 '承古英语 ræt 等形式，更远来源及与拉丁、其他欧洲语言的传播关系有争论。人物贬称、告发动词由旧负面动物联想发展。',Rt[:2],
 'a laboratory rat 实验大鼠，a rat in the cellar 地窖里的鼠，rat on someone 告发某人，smell a rat 觉得有诈。',
 'rat on；smell a rat；a laboratory rat。',
 'rat 与 mouse 日常常按常见较大、较小鼠区分，但不是所有动物都只凭体长分类；人物义是带贬义的评价。',
 ('A rat disappeared behind the boxes.','一只大鼠钻到箱子后面不见了。'),('She smelled a rat when the story changed again.','说法又变时，她觉得其中有诈。'),sources=['https://en.wiktionary.org/wiki/rat#English','https://www.etymonline.com/word/rat'])
W('ratty','/ˈræti/','破旧邋遢的；烦躁易怒的；像鼠的',
 '一件旧外套磨损得乱糟糟，可以 ratty；人因为又累又烦，说话容易发火，也可能 ratty。两者都已是固定口语特点。',
 'rat + -y，双写 t。由像鼠、带鼠的性质发展出破旧、不整洁，以及烦躁等用法；不必真被鼠咬过。',Rt,
 'a ratty old coat 破旧外套，feel ratty 感到烦躁，get ratty with someone 对某人烦躁发火。',
 'a ratty old coat；get ratty with。',
 'ratty 形容物品常说破旧，形容人常说脾气烦；不要一律译为长得像老鼠。',
 ('He wore a ratty old sweater.','他穿着一件破旧毛衣。'),('I get ratty when I have not had enough sleep.','我没睡够时容易烦躁。'))
R('B2698','鼠类名称及负面人物、外观、脾气比喻','RAT：动物义之外，读出人物评价和口语场景','rat → ratty；rat on、smell a rat 各记固定说法。',
 '实验室说动物，故事里说叛徒，衣服说破旧，情绪说烦躁。相同动物词族，具体对象决定中文。',
 'ræt、ratte → rat；-y 性质双写 t；on 引被告发对象。更远来源未定。',
 [['动物、人物及性质','rat · ratty']],
 'rat on 带告发、出卖色彩；smell a rat 是怀疑有诈；ratty 不要求真实鼠患。',
 'He smelled a rat when he saw the suspicious offer.\n\n看到那份可疑报价时，他觉得有诈。','rat ratty')
if __name__=='__main__':save('continuation_20261030_lt',ROOTS,WORDS)
