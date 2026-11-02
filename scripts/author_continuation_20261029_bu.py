"""Red: color changes, established compounds, science and social history."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
RE=[['古英语 rēad → 中古英语 red','红的'],['英语 red','红色；后有警示、财务、政治等约定象征用法']]
W('red','/red/','红的；红色；约定语境中的警示等含义',
 '先把颜色看清楚；红色在标记、脸色、账目和政治里，又被赋予不同约定含义。',
 '继承古英语 rēad，经中古英语发展。它是古老颜色词，现代 red 单独不必再拆。不同象征不是所有英语国家、所有时期都完全一致。',RE,
 'red paint 红油漆，go red 脸红；see red 大发雷霆，in the red 亏损。red hair 通常指橘红、红褐色头发，不必像红油漆那么纯红。',
 'a red light；go red；see red；in the red；red tape。',
 'in the red 是财务亏损，red tape 是官僚繁文缛节，不能只逐字译红色。美国两党颜色与其他国家的政治象征也不能机械互套。',
 ('Her face went red when everyone looked at her.','大家都看着她时，她的脸红了。'),('The theatre stayed in the red for two years.','剧院连续两年处于亏损状态。'),('The room has a bright red door.','房间有一扇鲜红的门。'))
W('reddish','/ˈredɪʃ/','微红的；略带红色的',
 '看得出往红色靠，但没必要说它是纯红、鲜红。',
 'red + -ish，双写 d；-ish 在颜色中常表示略带这种颜色。',RE+[['red + -ish → reddish','红 → 略带红色的']],
 'reddish hair 偏红的头发，a reddish glow 微红的光。也常与 brown 等颜色组合描述混合色。',
 'a reddish glow；reddish hair；a reddish tint。',
 'reddish 不是更红的比较级；redder 才是更红，reddish 是偏红、微红。',
 ('The rocks had a reddish tint in the evening light.','岩石在傍晚光线下略带红色。'),('A reddish glow appeared above the hills.','山丘上方出现了微红的光。'))
W('redness','/ˈrednəs/','发红；红色状态',
 '不只给东西贴红的标签，而是谈它发红这个状态。',
 'red + -ness，把颜色性质名词化。这里不双写 d，因为 red 直接接辅音开头的后缀。',RE+[['red + -ness → redness','红的 → 发红、红色状态']],
 'the redness of the sky 天空的红色；facial redness 面部发红。描述皮肤颜色状态不自动说明原因。',
 'a patch of redness；the redness of the sky；notice some redness。',
 'redness 是状态名词，reddish 是微红的形容词；不能只凭 redness 这个词认定一定是日晒或某一种疾病。',
 ('The redness of the evening sky faded into grey.','傍晚天空的红色渐渐褪成灰色。'),('She noticed some redness where the mask had rubbed her skin.','她注意到口罩摩擦皮肤的地方有些发红。'))
W('redden','/ˈredən/','变红；使变红',
 '颜色正在往红变；既可以自己变，也可以是某种作用让它变红。',
 'red + 动词后缀 -en，双写 d 形成 redden。',RE+[['red + -en → redden','红的 → 变红、使变红']],
 'His face reddened 他的脸红了；the setting sun reddened the clouds 夕阳映红云彩。既有不及物也有及物用法。',
 'redden with embarrassment；redden the sky；a face reddens。',
 'redden 是颜色变化的动词，redness 是状态；redder 是比较级，不是动作。',
 ('His face reddened when he realized his mistake.','发现自己弄错时，他脸红了。'),('The low sun reddened the edges of the clouds.','低垂的太阳把云彩边缘映红了。'))
W('redheaded','/ˈredhedɪd/','红发的',
 '不是整个头是鲜红色，而是头上长着通常称作 red hair 的红褐、橘红头发。',
 'red 红 + headed 有某种头部特征的；headed 中 head + -ed 表示具有。整体以头发特征来描写人。',C('red 红发的颜色','head + -ed 具有相应头部特征','redheaded','长红发的'),
 'a redheaded woman 一位红发女性；a redheaded child 红发孩子。日常描述与 red-haired 同义方向，发色本身不说明性格。',
 'a redheaded actor；a redheaded child；naturally redheaded。',
 'redhead 是红发的人这个名词，redheaded 是红发的形容词；不要把发色与脾气暴躁绑成事实。',
 ('The redheaded actor plays the scientist in the film.','那位红发演员在电影里饰演科学家。'),('She drew a redheaded character with a green coat.','她画了一个穿绿外套的红发人物。'))
W('redwood','/ˈredwʊd/','红杉；红杉木',
 '名称抓住木材的红褐色特征，现代常用来指红杉及其木材。',
 'red 红 + wood 木材，组合为树木、木材名称；这是固定植物名称，不能把所有红色木头都认作同一种树。',C('red 红色、红褐色','wood 木材','redwood','红杉及其木材'),
 'a redwood forest 红杉林；redwood timber 红杉木。常见的 coast redwood 是北美沿海红杉。具体树种仍看完整名称和语境。',
 'a redwood forest；a giant redwood；redwood timber。',
 'redwood 不等于中文家具市场里所有红木类别；wood 也不必每次只译树林，这里还有木材义。',
 ('The path wound through a quiet redwood forest.','小路蜿蜒穿过一片安静的红杉林。'),('The exhibition included a sample of reddish redwood timber.','展览展出了一块偏红的红杉木样本。'),sources=['https://en.wiktionary.org/wiki/redwood#English','https://www.fpl.fs.usda.gov/documnts/usda/amwood/262redwo.pdf'])
W('redline','/ˈredlaɪn/','修订标记；极限线；标示修改、让引擎接近最高转速',
 '红线可以用来指出哪处改过，也可以标出不能随便越过的限值。',
 'red 红 + line 线，来自红色修订标记、仪表红色限值等不同具体场景。它们共享标记画面，不必排成一条先后必然的故事。',C('red 红色','line 标记线','redline','修订标记；限值及其相关动作'),
 'a redline version of a document 是标明修改的版本；an engine’s redline 是转速上限标记。分写 red line 的底线、禁区义也常见。',
 'a redline version；redline a draft；reach the redline；a red line。',
 'redline 在文件里标修改，不必表示不同意所有红字；社会历史中的 redlining 另有特定歧视做法义。',
 ('Please send the clean copy and the redline version.','请发送无修订标记的清稿和标明修改的版本。'),('The diagram marks the engine’s redline in bright red.','图中用鲜红色标出引擎的转速上限。'))
W('redlining','/ˈredlaɪnɪŋ/','标示修订；历史上的地区性歧视信贷、服务做法',
 '一边是给文件画修改标记；另一边是把地图上的某些地区划出去，居民因此被排斥在服务之外。',
 'redline + -ing。美国信贷历史中的专门用法与地图上红色划分、评级区域有关；不能把对文稿的普通修订也读成歧视。',C('red 红色','line 划线 + -ing','redlining','标示修订；另有按地区排斥服务的历史用法'),
 'review the redlining 可说检查修订标记。美国住房、信贷历史中，redlining 常指因地区及居民种族等因素，歧视性地拒绝或限制贷款、保险等服务。',
 'historical redlining maps；the effects of redlining；document redlining。',
 '两种语境都与标记有关，但意义不同。历史地图中的风险标签反映制定者的判断和偏见，不是居民真实价值的客观等级。',
 ('The exhibition displays historical redlining maps.','展览展示了历史上的红线划区地图。'),('The editor checked the document’s redlining before accepting the changes.','编辑在接受修改前检查了文档的修订标记。'),sources=['https://en.wiktionary.org/wiki/redlining#English','https://www.federalreservehistory.org/essays/redlining','https://www.federalreserve.gov/newsevents/speech/bernanke20070330a.htm'])
W('redshift','英 /ˈredʃɪft/；美 /ˈredʃɪft/','红移',
 '光谱中原本熟悉的特征，移到了波长更长、朝红端的方向。',
 'red 红端 + shift 移动，构成物理、天文学术语。名称说波长往哪边变，不是整颗星突然被涂红。',C('red 光谱的红端、较长波长方向','shift 移动','redshift','光的波长向更长方向偏移'),
 'a galaxy’s redshift 星系的红移；measure the redshift 测量红移。宇宙膨胀可以拉长光波造成红移，运动等也可产生相关变化；不把所有情况都简化成同一个原因。',
 'cosmological redshift；measure a redshift；a high redshift。',
 'redshift 不等于物体本来的颜色红；也不必仍落在可见红光内，波长可能移得更远，进入红外等范围。',
 ('Astronomers measured the redshift of the distant galaxy.','天文学家测量了那个遥远星系的红移。'),('The diagram shows spectral lines moving to longer wavelengths because of redshift.','图示显示谱线因红移而移向更长波长。'),sources=['https://en.wiktionary.org/wiki/redshift#English','https://science.nasa.gov/mission/webb/science-overview/science-explainers/spectroscopy-101-beyond-temperature-and-composition/','https://science.nasa.gov/asset/webb/what-is-cosmological-redshift/'])
W('redshirt','英 /ˈredʃɜːt/；美 /ˈredʃɜːrt/','体育语境中暂缓参赛者；影视里容易牺牲的小配角',
 '红衫先是可辨认的服装；不同群体又让它成为一种身份称呼。',
 'red 红 + shirt 衬衫。体育用法与区分球员身份的服装有关；影视迷用法则与《星际迷航》中常遇险的红制服配角相关，两条具体来路分开。',C('red 红色','shirt 衣衫','redshirt','由服装得名的球员身份；另有可牺牲配角的影迷用法'),
 '美国大学体育传统报道中，redshirt 常指暂缓或限制正式参赛、保留后续参赛资格的运动员；词义不要直接当作当前完整赛制。影迷说 a redshirt，常指为了凸显危险而被安排牺牲的小角色。',
 'a redshirt season；a redshirt player；an expendable redshirt character。',
 'redshirt 不只是所有穿红衣服的人；体育身份与影迷配角义都已固定化，不能互相套用。',
 ('The old team profile lists him as a redshirt during his first season.','旧球队资料记载，他首个赛季处于暂缓参赛的红衫身份。'),('The reviewer complained that the new character was treated as a redshirt.','评论者抱怨，新角色被当作一个随时可以牺牲的小配角。'),sources=['https://en.wiktionary.org/wiki/redshirt#English','https://dictionary.cambridge.org/us/dictionary/english/redshirt','https://www.ncaa.org/eligibility-center/division-i-and-division-ii-age-based-eligibility-rules/'])
W('redneck','/ˈrednek/','对美国乡村白人的贬称；有时被自嘲、自称使用',
 '这个词装着说话人对乡村、阶层和生活方式的看法，远比红脖子三个字多。',
 'red 红 + neck 脖子；常见词源解释联系到户外劳作者被晒红的脖颈。后来的社会称呼积累了粗俗、无知、偏执等刻板联想，这些是标签，不是群体本质。',C('red 红的','neck 脖子','redneck','社会标签化的人群称呼'),
 '小说、电影中可见某人被叫 redneck，也可能有人自嘲、自豪地这样自称。是否冒犯要看关系和语气，不能因为有人自称，就推断所有人都接受。',
 'call someone a redneck；a redneck stereotype；describe oneself as a redneck。',
 'redneck 不是所有美国农村居民的中性统称；rural resident 乡村居民更中性。把侮辱性词义解释清楚不代表认同其偏见。',
 ('The film challenges the lazy stereotype of the redneck.','电影挑战了那种把乡村白人简单贴上标签的刻板印象。'),('The character calls himself a redneck with a mixture of humour and pride.','这个人物带着幽默又自豪的语气，自称 redneck。'),sources=['https://en.wiktionary.org/wiki/redneck#English','https://www.collinsdictionary.com/us/dictionary/english/redneck'])
W('redskin','/ˈredskɪn/','对美洲原住民的侮辱性旧称',
 '表面像按肤色描述人，实际使用已经承载了贬低、排斥的历史语气。',
 'red 红 + skin 皮肤，形成按颜色命名的人群标签。早期具体称色背景有争论，不把红色颜料或某个血腥传说强说成唯一确定起源。',C('red 红色标签','skin 皮肤','redskin','带侮辱意味的人群旧称'),
 '主要用于辨认旧材料、旧名称或围绕侮辱性称呼的讨论。现代中性表达可用 Native American、Indigenous person，或更具体的群体名称，按对象与语境选择。',
 'the offensive term “redskin”；the history of the word “redskin”。',
 '不能把 red + skin 的可理解字面义当成中性使用的理由；一个词积累的社会语气也是词义的一部分。',
 ('The museum explains why the term “redskin” is offensive.','博物馆解释了 redskin 这一称呼为何具有侮辱性。'),('The editor added a note about the historical use of the word “redskin.”','编辑加了一条说明，解释 redskin 一词的历史使用背景。'),sources=['https://en.wiktionary.org/wiki/redskin#English','https://dictionary.cambridge.org/us/dictionary/english/redskin'])
R('B2570','红色；颜色变化；固定名称与象征','RED：先看颜色，再看已经约定的用法','红色词很容易组合，但现代意义不能都按字面猜。植物、修订、光谱、服装和人群标签各有具体背景。',
 'red 接古英语 rēad。reddish 是微红，redness 是发红状态，redden 是变红；后面的复合词要逐个看历史与用法。',
 'red → reddish、redness、redden；redhead → redheaded；redwood；redline → redlining；redshift 与 infrared 对照；redshirt、redneck、redskin 放在人群称呼和固定语境中看。',
 [['颜色、变化和发色','red · reddish · redness · redden · redhead · redheaded'],['植物名称','redwood'],['标记与技术术语','redline · redlining · redshift · infrared'],['服装称呼与社会标签','redshirt · redneck · redskin']],
 'redder 更红，reddish 微红，redden 变红；redlining 的修订义与歧视性划区义分开。带贬义的人群标签不是群体的客观性质。',
 'The reddish clouds reddened further as the sun sank behind the redwoods.\n\n太阳落到红杉后方时，微红的云彩变得更红了。',
 'red reddish redness redden redhead redheaded redwood redline redlining redshift infrared redshirt redneck redskin')
if __name__ == '__main__':save('continuation_20261029_bu',ROOTS,WORDS)
