"""Silk, propagandistic and buck with distinct historical branches."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['希腊、拉丁丝织品词的传播','联系 sērikos、sēricum；向英语借入的具体中间路线仍有讨论'],['古英语 seoloc、seolc → silk','丝、丝线、丝织品'],['材料与相似性质','silken 丝制、丝般；silky 丝般顺滑；silkworm 产丝的蚕']]
W('silk','/sɪlk/','丝、蚕丝；丝线、丝绸',
 '先是细丝纤维，再能捻成线、织成布，所以 silk 可以指丝，也能指丝绸。物品前的 silk 通常在说明材料。',
 '承古英语 seoloc、seolc 等，借入历史联系拉丁 sēricum、希腊丝织品相关词；具体经过哪些中间语言有讨论，与中文丝的更远关系也不宜说成现代直接借入。',S[:2],
 'silk thread 丝线，a silk scarf 丝巾，made of silk 丝制。spider silk 是蜘蛛丝，提醒你英文材料词也不只用于家蚕。',
 'silk thread；a silk scarf；made of silk。',
 'silk 材料义通常不可数；silky 只说像丝的触感时，不保证成分真是丝。',
 ('She bought a blue silk scarf.','她买了一条蓝色丝巾。'),('The fine silk thread caught the light.','细丝线在光下泛着光。'),sources=['https://en.wiktionary.org/wiki/silk#English','https://www.etymonline.com/word/silk'])
W('silky','/ˈsɪlki/','丝般顺滑、柔软的',
 '头发顺得像丝，汤汁入口细滑，也可以 silky。它把丝的顺滑触感借给别的东西，并不要求真由丝织成。',
 'silk + -y，中古英语已有相应形式。-y 在这里突出类似的外观、触感，也能形容柔和声音等。',S[:2]+[['silk + -y → silky','丝的顺滑 → 类似触感、声音']],
 'silky hair 丝般顺滑的头发，a silky texture 细滑质地，a silky voice 柔和悦耳的嗓音。',
 'silky hair；a silky texture。',
 'silky 多突出像丝，silk 常直接说材料；但 silken 也能有丝般比喻义，不能给两种形容词画绝对材料界线。',
 ('The conditioner left her hair soft and silky.','护发素让她的头发柔软顺滑。'),('The soup had a rich, silky texture.','汤的质地浓郁细滑。'))
W('silken','/ˈsɪlkən/','丝制的；丝般柔软、流畅的',
 'silken robe 可以是丝袍；silken voice 则像丝般柔和顺滑，读来常比普通 silky 更有文学感。',
 '承古英语 seolcen 等，对应 silk + 材料、性质后缀 -en。历史材料义和现代相似比喻都可保留。',S,
 'silken robes 丝袍，silken thread 丝线，a silken voice 柔滑嗓音，silken hair 丝般头发。',
 'silken robes；a silken voice。',
 '-en 在这里联系材料、性质，不是过去分词标记；silken 可以真丝制，也可以只是像丝。',
 ('The painting shows a figure in silken robes.','画里的人物穿着丝袍。'),('She answered in a soft, silken voice.','她用柔滑轻柔的嗓音回答。'))
W('silkworm','英 /ˈsɪlkwɜːm/；美 /ˈsɪlkwɜːrm/','蚕、吐丝结茧的蛾类幼虫',
 '生产 silk 的小虫，所以叫 silkworm。日常说家蚕时，指的是蛾的幼虫阶段，并不是蚯蚓这一类动物。',
 'silk + worm，古英语 seolcwyrm 已有组合。worm 在旧动物名称里可以宽泛指蠕动小虫，不能只套今天蚯蚓的窄义。',S[:2]+[['silk + worm → silkworm','产丝的虫，尤其家蚕等蛾类幼虫']],
 'raise silkworms 养蚕，silkworm cocoons 蚕茧，silkworm eggs 蚕卵。通常先认识家蚕的日常用法。',
 'raise silkworms；silkworm cocoons。',
 'silkworm 的 worm 不是严格现代生物分类名；名称里的形象不改变它是蛾类幼虫的事实。',
 ('The children watched a silkworm spin its cocoon.','孩子们看着一条蚕吐丝结茧。'),('The farm raises silkworms for silk production.','农场养蚕用于产丝。'))
R('B3870','丝的纤维、材料及柔滑性质，连接产丝动物与工艺','SILK：细丝织成布，顺滑感觉再借给别的东西','silk → silky、silken；silkworm、silkscreen 按动物、工艺分开。',
 'silk 看材料，silky、silken 可以看丝般触感；worm 是旧小虫名称，screen 是印刷工艺中的网版。',
 'seoloc、seolc → silk；-y、-en 性质或材料；silk + worm、screen。更早借词路线有讨论。',
 [['材料与相似性质','silk · silky · silken'],['产丝动物与工艺名称','silkworm · silkscreen']],
 'silky 不保证成分真丝；silken 也可比喻；silkworm 是蛾类幼虫。',
 'The silken fabric had a smooth, silky feel.\n\n丝织物摸起来柔滑如丝。','silk silky silken silkworm silkscreen')
P=[['拉丁 propagāre 扩展、传播','相关名称用于传播信仰的机构'],['propaganda','由机构、传播活动扩到宣扬立场的材料、信息'],['propagandist + -ic，或 propaganda + -istic','具有宣传鼓动特点的性质']]
W('propagandistic','英 /ˌprɒpəɡænˈdɪstɪk/；美 /ˌprɑːpəɡænˈdɪstɪk/','宣传鼓动性的、带意识形态宣传特点的',
 '作品不是只给你信息，而是有意挑选、安排材料，把你往某种立场上推，这种特点可被说成 propagandistic。',
 'propagandist + -ic，或 propaganda 的相应词干 + -istic。更里层 propaganda 联系拉丁传播词与早期传播信仰机构的名称。',P,
 'a propagandistic film 宣传鼓动性电影，a propagandistic tone 宣传腔调，propagandistic images 带立场宣传特点的图像。常带批评意味。',
 'a propagandistic film；a propagandistic tone。',
 'propaganda 不等于每句话都假；propagandistic 评价的是选材、组织、说服目的等整体特点。是否准确要另看证据。',
 ('Critics found the film overly propagandistic.','评论者认为这部电影宣传鼓动意味过强。'),('The exhibition examines the propagandistic use of heroic images.','展览考察英雄形象在宣传鼓动中的使用。'),sources=['https://en.wiktionary.org/wiki/propagandistic#English','https://www.etymonline.com/word/propaganda'])
R('B3412','传播立场的活动、材料，及参与者、性质','PROPAGANDA：材料怎么安排，想把观点推向哪边','propaganda → propagandist、propagandistic。',
 '信息材料、从事宣传的人、作品的宣传特点分开看。词源传播义帮助理解，现代评价仍需结合立场、方法和事实。',
 'propagāre 传播 → 机构相关名称 propaganda → 广义宣传；-ist 人物，-istic 性质。',
 [['材料、人物与性质','propaganda · propagandist · propagandistic']],
 '宣传不必每句虚假；propagandistic 常带批评；人物和性质后缀不同。',
 'The propagandist designed images with a strongly propagandistic message.\n\n宣传者设计的图像带有强烈的宣传鼓动信息。','propaganda propagandist propagandistic')
B=[['buck 动物名','日耳曼语公鹿、公羊等旧词族；现代按物种限定'],['美元、反抗等分支','buck 美元的来源常联系鹿皮贸易；抗拒动作另有顶撞、butt 等影响分析'],['近形词需分开','buckle 联系拉丁 buccula；buxom 联系弯曲旧动词加 -some']]
W('buck','/bʌk/','雄鹿等雄性动物；〔口语〕美元等；反抗、逆着；〔马〕弓背蹦跳',
 '动物语境里先看是哪种雄兽；ten bucks 在美国口语通常是十美元；buck the trend 则是逆着趋势走。几个常用义要分场景。',
 '动物名来自日耳曼语旧词，英语中由中古英语 bukke 延续。美元义常被解释为鹿皮交易单位的缩略，仍有不确定性；抗拒动词还涉及顶撞、butt 等形式的影响。',B[:2],
 'a deer buck 一只雄鹿，twenty bucks 二十美元，buck the trend 逆势而行，a horse bucks 马弓背蹦跳，pass the buck 推卸责任。',
 'twenty bucks；buck the trend；pass the buck。',
 'buck 的雄兽范围依物种、地区而变；钱义先认语境的货币，不能所有国家一律换成美元。buckle 不直接从动物 buck 加后缀来。',
 ('A buck stood at the edge of the forest.','一只雄鹿站在林缘。'),('The small shop bucked the trend and increased sales.','小店逆势而行，销售额增加了。'),sources=['https://en.wiktionary.org/wiki/buck#English','https://www.etymonline.com/word/buck'])
W('roebuck','英 /ˈrəʊbʌk/；美 /ˈroʊbʌk/','雄狍、雄性狍鹿',
 'roe deer 是狍这一类鹿，buck 加在后面，把性别说清楚：雄性的狍。前面限定物种，后面限定雄性。',
 'roe 狍 + buck 雄鹿，承中古英语相应组合。roe 在这里不是鱼卵，而是同形的动物名称。',B[:1]+[['roe + buck → roebuck','狍类里的雄性']],
 'a roebuck in the woods 林中的雄狍，a roebuck’s antlers 雄狍的角。遇到野生动物描述时能识别。',
 'a roebuck；a roebuck’s antlers。',
 'roebuck 不是所有雄鹿的通名；物种限定在 roe deer，不因 roe 另有鱼卵义就生造鱼卵公羊。',
 ('A roebuck stepped out from between the trees.','一只雄狍从树间走出来。'),('The photographer watched the roebuck from a distance.','摄影师从远处观察那只雄狍。'))
W('buckskin','/ˈbʌkskɪn/','鹿皮、鹿皮革；相应皮衣；黄褐色等',
 'buck 的 skin 是鹿皮，制成柔软皮革也叫 buckskin。后来又能借皮革的色调说颜色、马毛色，先从材料抓起。',
 'buck + skin，承中古英语相应复合。材料名称再指制品、颜色，不代表所有现代黄褐色东西都含鹿皮。',B[:1]+[['buck + skin → buckskin','鹿皮、鹿皮革 → 服饰、颜色等']],
 'buckskin gloves 鹿皮手套，a buckskin jacket 鹿皮夹克，a buckskin horse 特定黄褐色毛色的马。',
 'buckskin gloves；a buckskin jacket。',
 'buckskin 的皮革用法通常不可数；马毛色是固定延伸，不是给马穿上鹿皮。',
 ('The old jacket was made of buckskin.','旧夹克用鹿皮革制成。'),('A pair of buckskin gloves lay on the shelf.','架上放着一副鹿皮手套。'))
K=[['拉丁 buccula 颊带、盾中央凸起 → 法语 bocle、boucle','扣环、凸起等相关形式'],['英语 buckle','扣环、扣紧；另经凸起、拱身发展为弯曲失稳'],['buckle + -ing → buckling','扣紧动作，或受压弯曲的过程']]
W('buckle','/ˈbʌkəl/','扣环；扣紧；受压弯曲、撑不住',
 'belt buckle 是皮带扣，buckle up 是扣好；柱子、膝盖在压力下弯下去，也叫 buckle。后一支抓拱起、变形，不是把柱子扣到皮带上。',
 '借古法语 bocle、boucle，联系拉丁 buccula 颊带、盾面凸起。扣紧由扣具名词成动词，变形义又经凸起、拱身等形式发展；不拆成 buck 动物 + -le。',K[:2],
 'a belt buckle 皮带扣，buckle up 扣好安全带，buckle under pressure 在压力下撑不住，buckle down to work 专心投入工作。',
 'buckle up；buckle under pressure；buckle down to。',
 'buckle under 说被压得撑不住，buckle down 说认真干起来，方向词改变固定短语义；两者都不只说扣安全带。',
 ('She fastened the buckle on her bag.','她扣好包上的扣子。'),('The thin metal sheet buckled under the weight.','薄金属板在重压下弯曲变形。'),sources=['https://en.wiktionary.org/wiki/buckle#English','https://www.etymonline.com/word/buckle'])
W('buckling','/ˈbʌkəlɪŋ/，也读 /ˈbʌklɪŋ/','扣紧；受压屈曲、弯曲失稳；buckle 的现在分词',
 '扣带子时是 buckling the strap；一根细柱受力后突然弯向侧面，则是结构 buckling。相同分词接着 buckle 的两类动作。',
 'buckle + -ing，去 e。名词可说过程、现象，特别是受压、受力后的屈曲，不必是扣具本身坏了。',K,
 'buckling a belt 扣皮带，buckling of a column 柱的屈曲，prevent buckling 防止屈曲。专门工程意义还须按结构条件定义。',
 'buckling of a column；buckling a strap。',
 'buckling 不等于所有 bending 弯曲；工程语境常强调失稳变化。扣紧义则仍是普通动作分词。',
 ('He was buckling the straps on the case.','他正在扣紧箱子上的带子。'),('The test revealed buckling in the thin panel.','试验显示薄板出现了屈曲。'))
U=[['古英语弯曲动词词族 + -sum','可弯、顺从的'],['中古英语 buhsum、buxom','顺从、随和 → 活泼、健康丰满'],['现代身体描述','多说体态丰满，尤指胸部丰满；不再以顺从为常用义']]
W('buxom','/ˈbʌksəm/','体态丰满的，尤指胸部丰满的；健康活泼的〔旧义〕',
 '现代读小说、看人物描写，buxom 常说女性体态丰满，尤其胸部。它和今天的 buck 公鹿没有直接的动物派生关系。',
 '来自弯曲、顺从的旧动词词族加 -some，历史上从可弯、顺从走到随和、活泼，再到健康丰满；旧 -some 的音形与前半融合，现代不再保留完整的 -some 拼写。',U,
 'a buxom figure 丰满体态，a buxom woman 丰满女性。词带对身体外观的具体评价，常见于人物、艺术描述，语体较显眼。',
 'a buxom figure；a buxom woman。',
 'buxom 今天不译成听话、顺从；描述体态也不等于高矮、总体胖瘦的所有指标，尤其胸部含义已很突出。',
 ('The portrait depicts a buxom woman in a red dress.','肖像描绘了一位穿红裙、体态丰满的女性。'),('The actress played a buxom innkeeper in the period drama.','这位女演员在古装剧中饰演一位体态丰满的客栈女店主。'),sources=['https://en.wiktionary.org/wiki/buxom#English','https://www.etymonline.com/word/buxom'])
R('B3506','雄兽、货币与抗拒，近形扣具和丰满词另有来历','BUCK：动物、钱、抗拒先分场景，再比较近形词','buck → roebuck、buckskin、buckshot；buckle → buckling 单列；buxom 单列；humbucker 取抗拒动作分支。',
 '外形相似的词放在一起，不等于统统来自公鹿。扣具来自法语、拉丁颊带词，buxom 从弯曲、顺从的旧词一路换了重点。',
 'buck 动物旧词；skin 皮、roe 狍、shot 弹丸；buckle 联系 buccula；buxom 联系弯曲旧动词 + -some。',
 [['雄兽与皮革、固定复合','buck · roebuck · buckskin · buckshot'],['扣紧与变形','buckle · buckling'],['另源人物性质','buxom'],['抗拒动作的技术复合','humbucker']],
 '美元义来源有推测；buckle 不是 buck + -le；buxom 现代不是顺从；buckling 工程屈曲与普通弯曲有区别。',
 'He spent a few bucks replacing the buckle on his buckskin bag.\n\n他花了几美元，换掉鹿皮包上的扣子。','buck roebuck buckskin buckshot buckle buckling buxom humbucker')
if __name__=='__main__':save('continuation_20261030_lr',ROOTS,WORDS)
