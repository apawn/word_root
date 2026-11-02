"""Suit: following, matching sets and suitability."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
SU=[['拉丁 sequī、secūtus → 通俗拉丁 *sequita','跟随；跟随、追随相关形式'],['古法语 suite、siute → 英语 suit','随从、追随、成套 → 套服、花色、诉讼；相配、适合']]
def H(f,m):return SU+[[f,m]]
W('suit','/suːt/；英式也读 /sjuːt/','套装；一套衣服；扑克牌花色；诉讼；适合',
 '衣服配成一套，东西彼此配得上，就容易连到适合。诉讼和随从义则要回到跟随、追求的旧历史。',
 '借法语 suite、siute，最终接拉丁 sequī 跟随。早期同族涉及随从、追随、配套衣服、诉讼，后来动词 suit 表相配、合用。',SU,
 'a business suit 正装套服，a suit of cards 一种牌花色，a civil suit 民事诉讼，That suits me 我觉得合适。follow suit 从跟同花色发展为跟着照做。',
 'a business suit；suit someone；suit yourself；follow suit。',
 '衣服 fit 常说尺寸合身，suit 常说颜色、样式等适合这个人；match 常比较两个东西是否相配。三者有交叉但重点不同。',
 ('That colour really suits you.','那个颜色很适合你。'),('Does Friday afternoon suit everyone?','周五下午对大家都方便吗？'),sources=['https://www.etymonline.com/word/suit','https://en.wiktionary.org/wiki/suit#English'])
W('suitable','/ˈsuːtəbl/；英式也 /ˈsjuːtəbl/','合适的；适用的',
 '放到这个人、用途、场合里，条件对得上、用得顺。',
 'suit 动词适合 + -able，形成关系形容词。这里重点是适配某个用途，不是衣服能被穿上的单一意思。',H('suit + -able → suitable','与人、用途或场合相合的'),
 'suitable for children 适合儿童，suitable for the job 适合工作，a suitable time 合适时间。要说明适合什么，不能只空泛说很好。',
 'suitable for；a suitable time；a suitable candidate。',
 'suitable 合用途，available 当前可用；一个候选人合适但可能没空，一个空房可用但可能不适合需求。',
 ('The film is suitable for older children.','影片适合年龄较大的儿童。'),('We need a suitable place for the meeting.','我们需要一个合适的开会地点。'))
W('suited','/ˈsuːtɪd/；英式也 /ˈsjuːtɪd/','适合的；配备某种套服或牌花色的',
 '人和工作、材料和环境之间恰好搭得上，常说 well suited。',
 'suit + -ed，/t/ 后的 -ed 读 /ɪd/。既可过去式、分词，也固定作适配的形容词；其他义项接套服、牌花色。',H('suit + -ed → suited','已适配、合适；具有某套服或花色'),
 'well suited to the role 很适合角色，ideally suited for the task 非常适合任务。根据具体搭配可接 to 或 for。',
 'well suited to；ideally suited for；poorly suited to。',
 'suited 常和程度词、to/for 一起说适配关系；suitable 常直接修饰名词。a suitable candidate 与 a candidate well suited to the role 都自然。',
 ('Her calm manner is well suited to this role.','她沉稳的作风很适合这个角色。'),('The room is poorly suited for large meetings.','这个房间不太适合开大型会议。'))
W('suitability','/ˌsuːtəˈbɪləti/；英式也 /ˌsjuːtəˈbɪləti/','适合程度；适用性',
 '从好不好看的评价，转成问它到底适不适合这个用途、这个人。',
 'suitable + -ity，-able 对应 -ability，重音移到 -bil-。把适合这个性质变成可讨论、可评估的名词。',H('suitable + -ity → suitability','合适这个性质、程度'),
 'assess suitability 评估适用性，suitability for the job 对工作的适合程度，question the suitability 质疑是否合适。',
 'assess suitability；suitability for；question the suitability。',
 'suitability 适合特定要求，quality 一般质量；质量高的材料也可能不适合当前用途。',
 ('The interview assesses each candidate’s suitability for the role.','面试评估每位候选人对岗位的适合程度。'),('We tested the material’s suitability for outdoor use.','我们测试了材料是否适合户外使用。'))
W('suitcase','/ˈsuːtkeɪs/；英式也 /ˈsjuːtkeɪs/','行李箱',
 '旅行时把衣服装进去的箱子，后来也装书、洗漱物品等，不只装正装。',
 'suit 套服 + case 箱，按装衣服的用途命名。这里 case 是容器，不是案件；suit 也不取诉讼义。',H('suit + case → suitcase','装套服、衣物的箱 → 旅行行李箱'),
 'pack a suitcase 收拾行李箱，a wheeled suitcase 拉杆箱，a small suitcase 小行李箱。',
 'pack a suitcase；a wheeled suitcase；carry a suitcase。',
 'suitcase 可数，一只箱子；luggage、baggage 常不可数，说行李总称。不能把 a luggage 当作一只箱子的通常说法。',
 ('She packed her suitcase the night before the trip.','她在出行前一晚收拾好行李箱。'),('The suitcase fits in the overhead compartment.','行李箱能放进头顶行李舱。'))
W('swimsuit','/ˈswɪmsuːt/','泳衣',
 '为了游泳穿的衣服，前部直接告诉用途，后部 suit 说一套或一件活动服装。',
 'swim 游泳 + suit 服装，合成固定衣物名称。词本身不限于某一种性别、剪裁。',H('swim + suit → swimsuit','游泳时穿的服装'),
 'a swimsuit for the pool 泳池用泳衣，a one-piece swimsuit 连体泳衣。具体泳裤、比基尼等也有更细名称。',
 'a one-piece swimsuit；change into a swimsuit；a new swimsuit。',
 'swimsuit 主要游泳衣，wetsuit 是水上水下活动的贴身保温衣；两者不能因都下水就完全混称。',
 ('Remember to pack your swimsuit.','记得把泳衣装好。'),('She changed into a swimsuit before going to the pool.','她去泳池前换上了泳衣。'))
W('jumpsuit','/ˈdʒʌmpsuːt/','连体裤装；连身衣',
 '上衣和裤子连成一件，今天既可工作服，也可日常时装。',
 'jump + suit，最初联系跳伞者穿的连体服，后来扩展到其他运动、工作和时装款式。名字不表示穿上后一定要跳。',H('jump〔跳伞〕+ suit → jumpsuit','跳伞连体服 → 各类连体裤装'),
 'a denim jumpsuit 牛仔连体裤，a work jumpsuit 连体工作服，a black jumpsuit 黑色连体裤装。',
 'a denim jumpsuit；a work jumpsuit；wear a jumpsuit。',
 'jumpsuit 通常上衣与裤腿连成一件，普通 two-piece suit 两件套彼此分开；bodysuit 常贴身、结构又有差别。',
 ('She wore a black jumpsuit to the party.','她穿着黑色连体裤装参加聚会。'),('The workers changed into protective jumpsuits.','工人们换上防护连体服。'))
W('wetsuit','/ˈwetsuːt/','湿式潜水服；水上运动保温衣',
 '水上或水下活动穿的贴身保温衣，衣服可以湿，主要靠材料等减少身体散热。',
 'wet 湿 + suit 活动服装，按允许湿润的工作方式形成名称，常与 drysuit 干式服区分。',H('wet + suit → wetsuit','可以湿润的水上、水下保温服'),
 'a surfing wetsuit 冲浪保温衣，a diving wetsuit 湿式潜水服，a thick wetsuit 厚款保温衣。这里解释服装名称。',
 'a surfing wetsuit；a diving wetsuit；put on a wetsuit。',
 'wetsuit 保温用途不同于普通 swimsuit 泳衣；drysuit 设计上尽量让身体、内层保持干燥，是另一类服装。',
 ('The surfers wore wetsuits in the cold water.','冲浪者在冷水里穿着保温衣。'),('She hung the wetsuit up to dry after the lesson.','课程结束后，她把湿式服挂起来晾干。'))
R('B3166','跟随、配套、相合与衣物名称','SUIT：成套、相配；前部告诉哪种服装','suit → suitable、suited → suitability；接 suitcase 容器，再按游泳、跳伞、湿式保温等场景分服装。',
 '词族最终来自拉丁跟随词。法语、英语早期有随从、追求、成套和诉讼等义，现代服装、合适和诉讼各有固定使用场景。',
 'suit + -able/-ed；suitable + -ity；suit + case；swim/jump/wet/track/body + suit；law + suit。',
 [['基本词与适合程度','suit · suitable · suited · suitability'],['旅行箱与活动服装','suitcase · swimsuit · jumpsuit · wetsuit · tracksuit · bodysuit'],['另支常用词','lawsuit']],
 'suit 适合风格，fit 常合尺寸，match 常两物搭配；suitcase 可数而 luggage 常不可数；swimsuit 与 wetsuit 用途不同。',
 'She packed a suitable swimsuit in her suitcase.\n\n她把一件合适的泳衣装进行李箱。',
 'suit suitable suited suitability suitcase swimsuit jumpsuit wetsuit tracksuit bodysuit lawsuit')
if __name__=='__main__':save('continuation_20261030_ad',ROOTS,WORDS)
