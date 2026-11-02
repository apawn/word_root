"""Rot, cartoons, neighbours and ink."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
Ro=[['古英语 rotian → 中古英语 roten → rot','腐烂、败坏'],['北欧相应旧分词 rotinn → rotten','腐烂的状态；与 rot 同源，英语借入路径不同'],['rot + -ing → rotting','正在腐烂、腐烂过程']]
W('rot','英 /rɒt/；美 /rɑːt/','腐烂、腐坏；腐败；〔口语〕胡说',
 '木头慢慢变软、果实腐坏，原来的组织被分解，就是 rot。制度里一点点坏下去，也能借这个画面。',
 '承古英语 rotian，经中古英语 roten 等延续；名词也说腐烂过程、腐物。由实物败坏扩展到道德、制度等败坏。',[['古英语 rotian','腐烂、败坏'],['中古英语 roten → rot','腐坏动作；扩展到腐物、抽象败坏']],
 'wood rot 木材腐朽，rot away 逐渐腐烂，stop the rot 制止恶化；That’s rot! 在口语里是胡说，语气较冲。',
 'rot away；wood rot；stop the rot。',
 'rot 常指组织腐坏的变化，不等于所有金属氧化的 rust；两者都可比喻逐渐损坏，实物机制不同。',
 ('The wooden fence had begun to rot.','木栅栏已经开始腐朽。'),('They hoped the new leadership would stop the rot.','他们希望新领导层能制止局面继续恶化。'))
W('rotten','英 /ˈrɒtən/；美 /ˈrɑːtən/','腐烂的；糟糕、恶劣的；坏透的',
 '苹果里面已经烂了，是 rotten；一天坏事接连不断，也可以 a rotten day。它把物体腐败的坏感推广到生活评价。',
 '中古英语 roten 接北欧语旧分词形式，如古诺斯 rotinn 腐坏的，与 rot 的旧词同族。可用旧分词 -en 辅助认形，但不是今天临时给 rot 加后缀造出。',Ro[:2],
 'a rotten apple 烂苹果，rotten wood 腐木，rotten luck 坏运气，be rotten to someone 对某人很坏；spoil someone rotten 是宠坏某人。',
 'a rotten apple；rotten luck；spoil someone rotten。',
 '现代动词 rot 的普通过去式、过去分词是 rotted；rotten 常作为独立状态形容词，不要把每个过去动作都改成 rotten。',
 ('The builders replaced the rotten wood.','工人换掉了腐朽的木料。'),('I had rotten luck with the weather on that trip.','那次旅行天气很差，我真倒霉。'),sources=['https://en.wiktionary.org/wiki/rotten#English','https://www.etymonline.com/word/rotten'])
W('rotting','英 /ˈrɒtɪŋ/；美 /ˈrɑːtɪŋ/','正在腐烂的；腐烂过程；rot 的 -ing 形式',
 'rotten 常让你看已坏的状态，rotting 更把镜头放在继续腐坏的过程。落叶、木头都可能正在发生这种变化。',
 'rot + -ing，双写 t；也承旧英语、中古英语相应动作名词、分词形式。现代兼有过程名词和分词用法。',Ro[:1]+Ro[2:],
 'rotting leaves 正在腐烂的落叶，rotting wood 腐朽中的木头，the rotting of timber 木材腐烂。',
 'rotting leaves；rotting wood。',
 'rotting 作名词讲腐烂过程，作修饰语讲处于腐烂中；不是 rot 的普通复数。',
 ('Rotting leaves covered the forest floor.','林地上铺满了正在腐烂的落叶。'),('Water trapped beneath the boards accelerated the rotting.','木板下积住的水加快了腐烂。'))
R('B3225','组织渐渐分解、败坏，过程与状态分清','ROT：原本结实的东西，一点点坏下去','rot → rotting；同族北欧旧分词借入形成 rotten。',
 '动作看 rot，正在变化看 rotting，已腐坏、很糟糕的状态看 rotten。制度和人品的坏，也借这种内部败坏画面。',
 'rot 承古英语 rotian；rotten 接北欧同族旧分词；rotting 双写 t。现代 rot 的普通过去、完成形式 rotted。',
 [['腐烂动作、过程与坏的状态','rot · rotting · rotten']],
 'rotten 与 rotted 用法不同；rotten luck 是坏运气，不是运气真的发生生物腐烂。',
 'The wood began to rot, and the rotten boards were eventually replaced.\n\n木头开始腐朽，烂掉的木板最后被换掉。','rot rotting rotten')
C=[['拉丁 carta、意大利 carta 纸 → cartone','较大、厚重纸张；-one 是相关增大形式'],['法语 carton 等 → 英语 cartoon','供壁画、织毯等使用的设计底稿'],['底稿、绘画 → 报刊漫画 → 动画片','媒介与用途不断扩展']]
W('cartoon','英 /kɑːˈtuːn/；美 /kɑːrˈtuːn/','漫画；动画片；〔艺术〕设计底稿',
 '今天可能是报纸上几笔夸张的漫画，也可能是会动的卡通片。更早的 cartoon 则是艺术家画在大纸上的正式底稿。',
 '经法语 carton 或直接接意大利 cartone 厚纸、大纸，底层 carta 纸。先以纸张、底稿命名，再扩展为报刊漫画和动画。',C,
 'a political cartoon 政治漫画，watch cartoons 看动画片，a cartoon character 卡通角色；艺术史语境中的 cartoon 仍可指设计底稿。',
 'a political cartoon；a cartoon character。',
 'cartoon 不等于所有动画技术：animation 可说制作方法、动画领域；cartoon 是作品、风格等具体名称。',
 ('The newspaper published a cartoon about the election.','报纸刊登了一幅关于选举的漫画。'),('The children watched a cartoon after dinner.','孩子们晚饭后看了一部动画片。'),sources=['https://en.wiktionary.org/wiki/cartoon#English','https://www.etymonline.com/word/cartoon'])
W('cartoonist','英 /kɑːˈtuːnɪst/；美 /kɑːrˈtuːnɪst/','漫画家、漫画创作者',
 '用画面、夸张表情和对白讲故事、表达观点的人，可以 cartoonist；常见工作是报刊漫画、连环漫画等。',
 'cartoon + -ist，-ist 标从事相应创作的人。完整保留 cartoon，再加人物后缀。',C+[['cartoon + -ist → cartoonist','创作漫画的人']],
 'a political cartoonist 政治漫画家，a newspaper cartoonist 报刊漫画家，a comic strip cartoonist 连环漫画作者。',
 'a political cartoonist；a newspaper cartoonist。',
 'cartoonist 常以画漫画为角色，animator 常以制作运动画面为工作；同一个人可能兼做，名称观察角度不同。',
 ('The cartoonist drew a new strip every week.','漫画家每周画一篇新的连环漫画。'),('A political cartoonist can express an argument in a single image.','政治漫画家能用一幅画表达一个观点。'))
W('cartoonish','英 /kɑːˈtuːnɪʃ/；美 /kɑːrˈtuːnɪʃ/','卡通般的；夸张、漫画化的',
 '眼睛画得特别大、坏人坏得太单一，都可能 cartoonish。它说像漫画的夸张处理，不要求作品真的用动画制作。',
 'cartoon + -ish，-ish 在此表示像某种风格、具有其特征。',C+[['cartoon + -ish → cartoonish','像卡通、漫画一样夸张']],
 'cartoonish features 漫画式夸张特征，a cartoonish villain 脸谱化反派，a cartoonish style 卡通风格。',
 'a cartoonish style；a cartoonish villain。',
 'cartoonish 可中性描述风格，也可批评过分简单、夸张；不必每处都译幼稚。',
 ('The game uses bright colours and cartoonish characters.','游戏使用鲜亮色彩和卡通式角色。'),('The film’s villain felt too cartoonish to be convincing.','电影反派太脸谱化，显得不可信。'))
R('B4359','厚纸、艺术底稿，到漫画及动画的作品名','CARTOON：先是画在大纸上的稿，后来变成画作和动画名','cartoon → cartoonist、cartoonish。',
 '词的历史从材料走向画作，再走向不同媒介。-ist 说创作者，-ish 说风格，真人电影中的人物也能显得 cartoonish。',
 'carta 纸 → 意大利 cartone 厚纸、大纸 → 法语 carton 等 → cartoon；-ist 人，-ish 相似风格。',
 [['作品及作者','cartoon · cartoonist'],['风格性质','cartoonish']],
 'cartoon 的艺术底稿义仍见于艺术史；cartoonish 不要求本身是动画。',
 'The cartoonist gave the mayor exaggerated, cartoonish features.\n\n漫画家给市长画上了夸张的漫画式特征。','cartoon cartoonist cartoonish')
N=[['古英语 nēah 近 + ġebūr 居住者 → nēahġebūr','住在近处的人'],['中古英语 neighebour 等 → neighbour','邻居、邻近者；英式拼写保留 ou'],['neighbour + -hood、-ly','邻里地区、群体；友好互助的性质']]
W('neighbour','英 /ˈneɪbə/；美 /ˈneɪbər/','邻居；邻近者〔美式常写 neighbor〕',
 '住在你附近的人是 neighbour；坐在旁边的人、相邻国家，也能按位置靠近来称呼。',
 '承古英语 nēahġebūr，内部是近 + 居住者，经中古英语多种拼写发展。现代英式 neighbour、美式 neighbor 是同词拼写。',N[:2],
 'a next door neighbour 隔壁邻居，our neighbours 我们的邻居，neighbouring countries 邻国；字母 gh 在现代常用发音里不单独出声。',
 'a neighbour；our neighbours。',
 'neighbour 是位置、关系称呼，不自动等于朋友；可以互不熟悉，也可能很亲近。',
 ('Our neighbour offered to water the plants.','邻居主动提出帮我们给植物浇水。'),('I introduced myself to my new neighbours.','我向新邻居作了自我介绍。'))
W('neighbourhood','英 /ˈneɪbəhʊd/；美 /ˈneɪbərhʊd/','街区、邻里；附近〔美式常写 neighborhood〕',
 '从一位邻居放大到大家生活的那片地方，就是 neighbourhood；也能说那里的人共同形成的邻里群体。',
 'neighbour + -hood，-hood 形成状态、群体、范围名词；本词常突出邻里地区。',N+[['neighbour + -hood → neighbourhood','附近居民所在的地区、邻里']],
 'a quiet neighbourhood 安静街区，in the neighbourhood 在附近，the neighbourhood school 社区学校；in the neighbourhood of a number 还可说大约某个数。',
 'in the neighbourhood；a quiet neighbourhood。',
 'neighbour 是人或邻近者，neighbourhood 常是地区、群体；-hood 在这里不是衣服帽子。',
 ('There is a small park in our neighbourhood.','我们街区有一座小公园。'),('The whole neighbourhood came to the street party.','街坊们都来参加了街头聚会。'))
W('neighbourly','英 /ˈneɪbəli/；美 /ˈneɪbərli/','像好邻居般友善、乐于互助的〔美式常写 neighborly〕',
 '人就在附近是一回事，主动递把手、相处友好则是 neighbourly。词从邻居身份走到了理想邻里相处的品质。',
 'neighbour + -ly，-ly 在这里造形容词，表示具有友善、互助的好邻居品质。',N+[['neighbour + -ly → neighbourly','像好邻居一样友善互助']],
 'a neighbourly gesture 友好的邻里举动，be neighbourly 友善相处，neighbourly help 邻里互助。',
 'a neighbourly gesture；neighbourly help。',
 'neighbourly 常作形容词，不因 -ly 就一律判为副词；说邻近的位置关系常用 neighbouring。',
 ('Bringing over some soup was a neighbourly gesture.','送来一些汤，是很友好的邻里举动。'),('They appreciated the neighbourly help after the storm.','暴风雨后，他们很感激邻里伸出的援手。'))
R('B3525','住得近的人，扩展为共同地区与互助品质','NEIGHBOUR：近处住着人，再看大家住的那片地方','neighbour → neighbourhood、neighbourly。',
 '一个人、一个地区、一种相处品质，三层连着记。英式 ou 与美式不带 u 的写法对应，读音、核心意思基本相同。',
 '古英语近 + 居住者 → nēahġebūr → neighbour；-hood 地区、群体，-ly 此处为形容词。',
 [['邻居、邻里地区和品质','neighbour · neighbourhood · neighbourly']],
 'neighbourly 不是单纯住得近；neighbourhood 的 -hood 不是帽子。',
 'Neighbourly gestures helped the new neighbours feel welcome in the neighbourhood.\n\n友好的邻里举动让新邻居在街区里感到受欢迎。','neighbour neighbourhood neighbourly')
I=[['希腊 en- 入 + kaiein 烧 → enkauston','烧入的，关联古代用热绘画等工艺'],['拉丁 encaustum → 古法语 enque 等','特种书写墨液的名称逐渐缩短'],['中古英语 ynke → ink','书写、印刷墨液；再到相关动作与形状']]
W('ink','/ɪŋk/','墨水、油墨；着墨；签署；文身',
 '写字、印刷留下颜色的液体是 ink；把合同用墨签下来，可说 ink a deal，皮肤留下墨色图案也能用 ink。',
 '经中古英语 ynke、古法语 enque 等，接拉丁 encaustum 与希腊烧入词形，历史关联用热绘画及特种墨液名称；并非说现代墨水都靠烧制。',I,
 'black ink 黑墨水，printer ink 打印机墨水，ink a contract 签合同，get inked 文身；乌贼等喷出的墨液也叫 ink。',
 'black ink；printer ink；ink a deal。',
 'ink 常不可数，谈种类、颜色可用 inks；文身义是墨液用途的延伸，不是所有 ink 都指文身。',
 ('The pen ran out of ink halfway through the letter.','信写到一半，笔没墨水了。'),('The two companies inked a new agreement.','两家公司签署了一份新协议。'),sources=['https://en.wiktionary.org/wiki/ink#English','https://www.etymonline.com/word/ink'])
W('inked','/ɪŋkt/','着了墨、用墨写过的；有文身的；ink 的过去式、过去分词',
 '纸面印下墨迹、皮肤留下文身，都可以看作 inked。口语 get inked 通常是在说去文身。',
 'ink + -ed，末尾 /k/ 后 -ed 读 /t/；分词从上墨、签署、文身等动词用法分别发展。',I+[['ink + -ed → inked','着墨、签过；带文身的状态']],
 'freshly inked 刚文上的、刚上墨的，an inked design 墨绘图案，get inked 去文身；完整背景决定所指。',
 'get inked；freshly inked。',
 'inked 不全是文身：inked agreement 可指签署过的协议；按宾语区分。',
 ('He showed us the freshly inked design on his arm.','他给我们看手臂上刚文好的图案。'),('The printer checked the inked surface before making a copy.','印刷工在印制前检查了着墨表面。'))
W('inky','/ˈɪŋki/','沾墨的；墨黑、像墨一样的',
 '手指沾了一块墨，可以 inky fingers；夜色黑得像浓墨，则是 inky darkness。一个说真有墨，一个借颜色。',
 'ink + -y，表示含墨、沾墨、像墨的性质，进一步形容深黑颜色。',I[-1:]+[['ink + -y → inky','沾墨；墨一样深黑']],
 'inky fingers 沾墨的手指，inky stains 墨渍，inky darkness 墨黑夜色。',
 'inky fingers；inky darkness。',
 'inky 可以没有实际墨水，只说颜色很深；inked 更容易表示已实施上墨、文身等动作后的状态。',
 ('She wiped her inky fingers on a cloth.','她用布擦了擦沾墨的手指。'),('The boat disappeared into the inky darkness.','船消失在墨黑的夜色中。'))
W('inkjet','/ˈɪŋkdʒet/','喷墨装置、喷墨打印机；喷墨的',
 '不是把整片色块压上纸，而是把细小墨滴喷到指定位置；ink + jet 的名字直接告诉你墨水怎样出去。',
 'ink 墨 + jet 喷射，形成按工作方式命名的复合词；作名词可简称喷墨打印机，也可作名词前修饰语。',I[-1:]+[['ink + jet → inkjet','以细小墨滴喷射成像的装置、方式']],
 'an inkjet printer 喷墨打印机，inkjet printing 喷墨打印；这里按基本成像方式认识名称。',
 'an inkjet printer；inkjet printing。',
 'inkjet 说工作方式，inked 说已着墨状态；jet 在此是喷射，不是一定有喷气飞机。',
 ('The photographs were printed on an inkjet printer.','这些照片用喷墨打印机印了出来。'),('Inkjet printing places tiny drops of ink on the paper.','喷墨打印把微小墨滴喷到纸上。'))
R('B3436','墨液留下色迹，派生上墨状态、颜色和喷墨方式','INK：让颜色留在纸面，也能留在皮肤和签名里','ink → inked、inky；inkjet 按喷射方式命名。',
 '材料、上墨动作、沾墨或墨黑的性质依次展开。墨液的用途能解释签合同、文身等现代义，不必把每次都译作墨水。',
 '希腊烧入词形经拉丁、法语缩短 → ink；-ed 状态，-y 性质；jet 喷射。',
 [['墨液、着墨状态和外观','ink · inked · inky'],['设备工作方式','inkjet']],
 '历史烧入名称不代表现代墨水全靠烧制；inky 可比喻墨黑。',
 'The inkjet printer left an inky mark on the page.\n\n喷墨打印机在纸上留下了一块墨迹。','ink inked inky inkjet')
if __name__=='__main__':save('continuation_20261030_me',ROOTS,WORDS)
