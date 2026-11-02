"""Linking vowels, bullying, desirability, dwelling and mono-."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
O=[['希腊等组合词的词干、连接元音形式 → 科学英语 -o-','把前后成分接起来，通常没有独立词义'],['近代混合构词、拼合词各自使用连接形式','并不是每个单词里的字母 o 都是连接元音']]
W('testosterone','英 /teˈstɒstərəʊn/；美 /teˈstɑːstəroʊn/','睾酮、睾丸激素',
 '先把长词看成化学命名：test- 联系睾丸，后半联系甾醇、酮。它命名一种甾体激素，名字有发现、研究来源的痕迹。',
 '经德语 Testosteron 借入；test(is) 睾丸的组合形式 + -o- + ster(ol) 甾醇部分 + -one 酮类结尾。也常把后部合看 -sterone 激素命名成分。',O[:1]+[['testis 的组合形式 + sterol 部分 + -one → Testosteron → testosterone','近代化学激素名']],
 'testosterone levels 睾酮水平，testosterone production 睾酮生成；人体不同性别都可有这种激素，主要产生部位、水平不同。',
 'testosterone production；testosterone levels。',
 '激素名不等于一个人的性格判断；日常所谓充满 testosterone 是比喻，不能当作实际测量。',
 ('The study measured testosterone levels in the samples.','研究测量了样品中的睾酮水平。'),('The chapter explains the role of testosterone in human development.','本章解释睾酮在人类发育中的作用。'),sources=['https://en.wiktionary.org/wiki/testosterone#English','https://www.etymonline.com/word/testosterone','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/testosterone'])
W('shambolic','英 /ʃæmˈbɒlɪk/；美 /ʃæmˈbɑːlɪk/','乱七八糟的、组织混乱的',
 '时间表对不上、人不知道去哪、现场没人管，这种失去组织的乱局可以 shambolic。它比只说有点凌乱更像在批评管理。',
 '来自 shambles 一片混乱，可能按 symbolic 等词形改造成 shambolic；也有 shambles + -o- + -ic 的分析。具体构形有不同解释，整体联系混乱义明确。',O[:1]+[['shambles 一片混乱 → shambolic','可能受 symbolic 等词形影响；组织失序的']],
 'a shambolic performance 乱成一团的表现，a shambolic start 混乱开局，shambolic planning 混乱规划，英式常见。',
 'shambolic planning；a shambolic performance。',
 'shambolic 主要说组织、执行混乱；房间略有几本书没放好，不一定需要这么重的评价。',
 ('The event got off to a shambolic start.','活动开场就乱成一团。'),('Shambolic planning left several teams without a schedule.','规划混乱，导致几个团队连日程都没有。'),sources=['https://en.wiktionary.org/wiki/shambolic#English','https://www.oxfordlearnersdictionaries.com/us/definition/english/shambolic'])
R('A1987','组合词中的连接元音，帮助把前后词干接起来','-O-：常是一座连接桥，本身不装一个固定意思','speed-o-meter、sax-o-phone、merit-o-cracy 等帮助看结构，实际借词史逐词核对。',
 '有的 -o- 来自希腊组合词传统，有的在近代混合构词里使用。长化学名称、拼合词又有专门缩短，不能看到 o 就机械切开。',
 '前词干 + -o- + 后成分；词尾、词干字母与连接元音要依实际构词区分。',
 [['测量与记录的组合','speedometer · accelerometer · interferometer · interferometry'],['乐器、网络与社会名称','saxophone · blogosphere · meritocracy · meritocratic'],['有专门命名、拼合背景的词','testosterone · shambolic']],
 '-o- 通常不独立表示物、动作或数量；shambolic 的具体构形有争论，testosterone 含缩短化学成分。',
 'The o in speedometer helps link the parts; the whole word names a speed measuring instrument.\n\nspeedometer 中的 o 连接前后成分，整词才命名测速仪器。','speedometer accelerometer interferometer interferometry saxophone blogosphere meritocracy meritocratic testosterone shambolic')
Bu=[['bully 欺负、威吓 → bullying','反复压迫、欺凌的活动名与分词'],['cyber- + bullying → cyberbullying','通过数字网络进行的欺凌']]
W('bullying','/ˈbʊliɪŋ/','欺凌、霸凌；威吓的、欺凌的',
 '仗着力量、地位、人数或掌握的信息，让别人难以抵抗地反复受欺负，就是 bullying 的核心画面。它可以是动作，也可形容威吓的做派。',
 'bully + -ing，保留 y。由欺负、威吓动词形成活动名词、分词形容词。校园等常用定义强调实际或感知的力量不平衡，以及反复发生或很可能反复发生。',Bu,
 'school bullying 校园欺凌，bullying behaviour 欺凌行为，a bullying manner 威吓人的态度。',
 'bullying behaviour；school bullying。',
 '一次平等争执与典型反复欺凌要分别理解；不符合某一定义的伤害行为，也不因此就变得合理。',
 ('The school investigated reports of bullying.','学校调查了欺凌举报。'),('His bullying manner made the meeting tense.','他咄咄逼人的态度让会议气氛紧张。'),sources=['https://en.wiktionary.org/wiki/bullying#English','https://www.stopbullying.gov/bullying/what-is-bullying'])
W('cyberbullying','英 /ˈsaɪbəbʊliɪŋ/；美 /ˈsaɪbərbʊliɪŋ/','网络欺凌、网络霸凌',
 '欺凌转到群聊、评论、社交平台等地方，网络让伤害内容能反复传播、随时被看见，这就是 cyberbullying 的场景。',
 'cyber- 数字网络 + bullying 欺凌，现代组合词；cyber- 限定发生媒介、环境。',Bu[:1]+[['cyber- + bullying → cyberbullying','利用数字通信媒介的欺凌']],
 'online harassment and cyberbullying 网络骚扰与网络欺凌，reports of cyberbullying 网络欺凌报告。',
 'cyberbullying incidents；cyberbullying prevention。',
 'cyberbullying 不是所有网上不同意见；它关注伤害、威吓、羞辱等欺凌行为及相应关系背景。',
 ('The report describes cyberbullying in group chats.','报告描述了群聊中的网络欺凌。'),('The workshop discussed how cyberbullying differs from an ordinary online disagreement.','研讨会讨论网络欺凌与普通网上争执的区别。'))
R('B4526','欺负、威吓形成持续活动名，网络前项限定媒介','BULLYING：利用优势压人，网络只是其中一种场景','bullying → cyberbullying。',
 '动作名突出行为模式；网络词说明媒介，线下、线上可能相互延续。用事实与关系判断含义，避免把普通争论与反复欺凌混同。',
 'bully + -ing，保留 y；cyber- + bullying。',
 [['欺凌与网络媒介扩展','bullying · cyberbullying']],
 '校园常用定义关注力量不平衡与反复性；具体法律术语范围另按实际制度。',
 'The study compares bullying at school with cyberbullying after school.\n\n研究比较校园内的欺凌与课后的网络欺凌。','bullying cyberbullying')
De=[['desire 想要 → desirable 值得想要、合意的','评价适宜、吸引人的性质'],['un- + desirable → undesirable','不合意、不希望出现的']]
W('undesirable','英 /ˌʌndɪˈzaɪərəbəl/；美 /ˌʌndɪˈzaɪrəbəl/','不希望出现的、不合意的；不受欢迎的',
 '结果、变化或行为不是人们想要的，就是 undesirable。它常说副作用、后果、情况不理想，并不只是外表没有吸引力。',
 'un- 否定 + desirable 合意、值得追求的。原词来自 desire 去 e + -able。',De,
 'undesirable effects 不希望的影响，an undesirable outcome 不理想结果，undesirable behaviour 不受欢迎的行为。',
 'undesirable consequences；undesirable effects。',
 'undesirable 是相对于目标、价值的评价；用来称人还可能带排斥性，不能随手当中性人物类别。',
 ('The change had several undesirable effects.','变化带来了几个不希望出现的影响。'),('The team tried to avoid an undesirable outcome.','团队试图避免不理想的结果。'))
R('B4402','想要、值得想要，再到合意程度与否定性质','DESIRABLE：是否值得追求，评价要放回目标','desirable → desirability；undesirable 是不合意的。',
 '一个方案是否吸引人、值得采用，与看起来好不好看是不同问题。性质名词抽出可取程度，否定前缀撤去合意评价。',
 'desire 去 e + -able → desirable；-able 对应 -ability；un- 否定。',
 [['性质、程度与相反性质','desirable · desirability · undesirable']],
 'undesirable 常说后果不理想；desirability 不只是外貌吸引力。',
 'The review weighed the plan’s desirability against its undesirable effects.\n\n评审权衡了计划的可取之处与不希望出现的影响。','desirable desirability undesirable')
R('B3835','愚傻性质的常用形式，名词、副词各有分工','FOOLISH：判断不明智，别把一次行为扩大成人的全部','foolish → foolishly、foolishness。',
 '一个决定不明智可说 foolish；怎样做用 foolishly；这份愚傻性质或愚行用 foolishness。行为评价常比直接给人贴标签更准确。',
 'fool + -ish → foolish；-ly 方式，-ness 性质、行为。',
 [['性质、方式与愚行概念','foolish · foolishly · foolishness']],
 'a foolish decision 评价决定，不自动说明做决定者一贯缺少能力。',
 'He foolishly ignored the warning and later admitted his foolishness.\n\n他不明智地忽视提醒，后来承认了这份愚行。','foolish foolishly foolishness')
Dw=[['古英语 dwellan 误导、使迷惑；同族有耽搁义','早期各日耳曼语言词义发展不同'],['中古英语 dwellen 耽搁、停留 → 住下 → dwell','现代居住；注意力持续停在某事上'],['-ing、-er 扩展','dwelling 住所；dweller 居住者']]
W('dwell','/dwel/','居住；停留；反复想着、详谈',
 '现代先抓“待在一个地方”：人住在屋里，注意力也能停在旧事上。dwell on a mistake 就是脑子反复停在那个错误上。',
 '承古英语 dwellan 误导等词，与同族耽搁、停留义共同演变；中古英语里由耽搁、留下走到居住。现代停留核心便于串联，但不是古义一开始就只指住房。',Dw[:2],
 'dwell in a place 居住于某地，dwell on the past 老想着过去，dwell on a point 详谈某点。过去式 dwelt，也用 dwelled。',
 'dwell in；dwell on；dwell upon。',
 '居住义 dwell 较书面，日常 live 更常见；dwell on 不只是想起，而常是停留得久、反复或详细讨论。',
 ('The story describes people who dwell in remote valleys.','故事描写住在偏远山谷里的人们。'),('She did not want to dwell on the mistake.','她不想反复纠结那个错误。'),sources=['https://en.wiktionary.org/wiki/dwell#English','https://www.etymonline.com/word/dwell'])
W('dwelling','/ˈdwelɪŋ/','住所、住宅；dwell 的现在分词',
 'dwell 是住，dwelling 就是让人住下的地方。它比较中性、书面，能涵盖各种居住建筑，不只独栋房子。',
 'dwell + -ing；中古英语已有停留、居所名词，逐步定型为住所。现代也仍可作动词分词。',Dw[:2]+[['dwell + -ing → dwelling','停留、居住活动 → 居所、住宅']],
 'a small dwelling 小住所，human dwellings 人类居所，a dwelling place 居住地。',
 'a rural dwelling；a dwelling place。',
 'dwelling 强调住人用途；building 建筑物范围更广，仓库、车站也可以是 building。',
 ('A small dwelling stood beside the river.','河边有一处小住宅。'),('The map marks the old human dwellings.','地图标出了旧时的人类居所。'))
W('dweller','英 /ˈdwelə/；美 /ˈdwelər/','居民、居住者',
 '住在什么地方的人，就是相应 dweller。city dweller 城市居民，cave dweller 洞穴居住者；前面的地点给出身份范围。',
 'dwell + -er，承中古英语 dweller。-er 由居住动作形成相应人物名。',Dw[:2]+[['dwell + -er → dweller','住在某类地方的人']],
 'city dwellers 城市居民，rural dwellers 乡村居民，cave dwellers 洞穴居住者。',
 'city dwellers；urban dwellers。',
 'dweller 通常带地点限定，不像 resident 那样在更多行政、身份语境中独立使用。',
 ('City dwellers often depend on public transport.','城市居民常依赖公共交通。'),('The exhibition reconstructs the homes of early cave dwellers.','展览重建了早期洞穴居民的住处。'))
R('B2853','由耽搁、停留到居住，注意力也能停在某事上','DWELL：人在地方住下，思绪在问题上停留','dwell → dwelling、dweller。',
 '一个是居住动作，一个是住处，一个是居住者。dwell on 让停留从空间转到注意力，通常带反复或详谈意味。',
 'dwellan 的复杂旧义 → dwellen 耽搁、住下 → dwell；-ing 居所，-er 人物；dwelt／dwelled。',
 [['停留、居住、住所与居民','dwell · dwelling · dweller']],
 'dwelling 不限独栋房；dwell on 常比一般 think about 更持续、反复。',
 'The city dweller found a quiet dwelling in the valley.\n\n这位城市居民在山谷找到一处安静住所。','dwell dwelling dweller')
Mo=[['希腊 monos 独一、单个 → mono-','一个、单一；具体数的对象由后部决定'],['mono- + 事物、性质或学科成分','单轨、单神、单一克隆、单不饱和等各数不同对象']]
W('monorail','英 /ˈmɒnəreɪl/；美 /ˈmɑːnəreɪl/','单轨铁路、单轨列车',
 '普通铁路常见两根平行钢轨；monorail 让车沿一条承载、导向轨道结构行走。mono- 数的是轨，不是只有一节车厢。',
 '借自法语 monorail，等于 mono- 单一 + rail 轨道，近代交通名称。',Mo,
 'a monorail system 单轨系统，take the monorail 乘单轨列车。',
 'a monorail system；a monorail train。',
 '单轨列车可以多节；one 在名字里不规定车厢数量或车站数量。',
 ('We took the monorail to the terminal.','我们乘单轨列车去了航站楼。'),('The city built a monorail system above the road.','城市在道路上方建了单轨系统。'))
W('monotheistic','英 /ˌmɒnəʊθiˈɪstɪk/；美 /ˌmɑːnəθiˈɪstɪk/','一神教的、信奉唯一神的',
 'mono- 数一个，theistic 指神的信仰；合在一起说只信奉一个神。它描述信仰结构，不是说宗教里只有一位人物。',
 'mono- + theistic；也与 monotheism 一神教的 -ism／-istic 形式配套，the- 接希腊 theos 神。',Mo[:1]+[['mono- + theistic → monotheistic','信奉唯一神的性质']],
 'a monotheistic religion 一神教，monotheistic belief 一神信仰。',
 'a monotheistic tradition；monotheistic belief。',
 'monotheism 名词说信仰体系，monotheistic 形容词说性质；多神信仰常用 polytheistic。',
 ('The course compares monotheistic and polytheistic traditions.','课程比较一神与多神信仰传统。'),('The text describes a monotheistic belief system.','文本描述了一套一神信仰体系。'))
W('monoclonal','英 /ˌmɒnəˈkləʊnəl/；美 /ˌmɑːnəˈkloʊnəl/','单克隆的',
 '从一个细胞克隆这一条来源出发，便是 monoclonal。单克隆抗体名称里的单，强调来源克隆与相应一致特性。',
 'mono- 单一 + clonal 克隆的。clonal 来自 clone + -al；现代生物学形容词，不必把所有单克隆形成都说成必然经过基因工程。',Mo[:1]+[['mono- + clonal → monoclonal','来自单一细胞克隆的']],
 'a monoclonal antibody 单克隆抗体，a monoclonal cell population 单克隆细胞群。',
 'monoclonal antibodies；a monoclonal cell population。',
 'monoclonal 的单不是只存在一个抗体分子；可以有许多具有相应一致来源、特性的分子。',
 ('The researchers compared monoclonal and polyclonal antibodies.','研究人员比较了单克隆抗体与多克隆抗体。'),('The assay uses a monoclonal antibody.','这项检测使用一种单克隆抗体。'),sources=['https://en.wiktionary.org/wiki/monoclonal#English','https://goldbook.iupac.org/terms/view/09680'])
W('monounsaturated','英 /ˌmɒnəʊʌnˈsætʃəreɪtɪd/；美 /ˌmɑːnoʊʌnˈsætʃəreɪtɪd/','单不饱和的',
 '食品、脂肪酸语境里，mono- 数的是碳链上一处碳碳双键。单不饱和脂肪这长名称，核心就是这一结构提示。',
 'mono- 单一 + unsaturated 不饱和的；unsaturated 为 un- + saturated。营养语境通常指脂肪酸链含一个碳碳双键。',Mo[:1]+[['mono- + unsaturated → monounsaturated','在脂肪酸语境中，碳链有一个碳碳双键']],
 'monounsaturated fatty acids 单不饱和脂肪酸，monounsaturated fats 单不饱和脂肪。',
 'monounsaturated fatty acids；monounsaturated fat content。',
 'mono- 不表示只有一条脂肪分子；它在这里限定不饱和结构的数目。食物可含多种脂肪，不必整瓶油只含这一类。',
 ('The chart compares saturated, monounsaturated and polyunsaturated fatty acids.','图表比较饱和、单不饱和与多不饱和脂肪酸。'),('The label lists the monounsaturated fat content.','标签列出了单不饱和脂肪含量。'),sources=['https://en.wiktionary.org/wiki/monounsaturated#English','https://extension.okstate.edu/fact-sheets/dietary-fat-and-cholesterol'])
R('A1709','单一、一个，关键是找准所数的对象','MONO-：一条轨、一个神、一个克隆，后半决定具体内容','monorail 单轨；monotheistic 一神；monoclonal 单克隆；monounsaturated 单不饱和。',
 '一个成分可以串很多领域，但数量对象各不相同。单轨不等于一节车厢，单克隆不等于一个分子；看清后半就能避免只背一个字的空记。',
 'monos → mono-，有时元音前缩成 mon-；与后续词干组成单一性质、类别名称。',
 [['颜色、文字、语言与形式','monochrome · monochromatic · monogram · monolingual · monosyllabic · monotype'],['结构、表面与交通','monolith · monolayer · monocular · monorail'],['分子与生物来源','monomer · monoxide · monoclonal · monounsaturated'],['信仰、关系与生产方式','monotheism · monotheistic · monogamous · monoculture']],
 'mono- 的一需要后半确定对象；单克隆强调来源，不是分子只有一个。',
 'A monorail has one guiding track structure; a monoclonal population has one clonal origin.\n\n单轨系统以一条轨道结构导向，单克隆群体则有单一克隆来源。',
 'monochrome monochromatic monogram monolingual monosyllabic monotype monolith monolayer monocular monorail monomer monoxide monoclonal monounsaturated monotheism monotheistic monogamous monoculture')
if __name__=='__main__':save('continuation_20261030_nj',ROOTS,WORDS)
