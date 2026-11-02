"""Common plural nouns with useful shifts of meaning and carefully separated histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2545':dict(words=['standard','standards'],label='standard → standards：旗帜、参照与标准',note='军旗与标准有历史联系，但中间语义过渡和更远词源保留争议。'),
 'B3790':dict(words=['award','awards'],label='award → awards：裁定与奖项',note='观察、考虑后裁定的借词背景，名动词都有常见形式。'),
 'B3911':dict(words=['relation','relations'],label='relation → relations：联系、关系与亲属',note='拉丁不规则词干 relāt- 与 referre 同族，名词有独立借入路线。'),
 'B4245':dict(words=['communication','communications'],label='communication → communications：沟通、消息与通信业务',note='英语名词有独立借入历史，复数常形成通信、对外沟通等集合用法。'),
 'C0401':dict(words=['affair','affairs'],label='affair → affairs：要做的事与事务',note='法语要做的结构名词化并借入，现代分不同语境解释。'),
 'B2484':dict(words=['bank','banks'],label='bank → banks：银行与河岸的不同借入线',note='金融柜台与地形河岸在英语中分路借入，不把一个现代义直接编成另一个。'),
 'B3433':dict(words=['business','businesses'],label='business → businesses：事务、经营与一家家企业',note='历史 busy + -ness，现代企业可数义与商业总体分开。'),
 'C0659':dict(words=['election','elections'],label='election → elections：选择与选举',note='法语、拉丁名词独立借入，现代与 elect 形成词族对应。'),
 'B2953':dict(words=['cell','cells'],label='cell → cells：小隔间与各类细胞、单元',note='拉丁小房间词扩展到生物、电学等领域的单元名称。'),
 'B3045':dict(words=['end','ends'],label='end → ends：末端、结束与目的',note='本族尽头词延续，目标义与事情所朝向的终点相连。'),
 'C0600':dict(words=['image','images'],label='image → images：图像与形象',note='拉丁形象词经法语借入，不拆成否定前缀 im-。'),
 'B2474':dict(words=['weapon','weapons'],label='weapon → weapons：武器与有力手段',note='古英语武器词延续，现代可有比喻手段义。'),
 'B2554':dict(words=['drug','drugs'],label='drug → drugs：药物与毒品等语境',note='法语借词更远来源不定，不能只凭一个中文义判断句中意思。'),
 'B3178':dict(words=['adult','adults'],label='adult → adults：长成与成年人',note='拉丁成长动词过去分词的借词，现代名词与形容词均常用。'),
}
W('standards','英 /ˈstændədz/；美 /ˈstændərdz/','标准、水平、准则〔standard 的复数〕',
 '拿一把公认的尺来比，要求达到的程度、做事遵循的准则，就是 standards。历史上这个名字先有军旗、集结标志等用法。',
 'standard + -s，/d/ 后读 /z/。standard 接古法语 estandart 等旗帜词及相关中世纪拉丁形式；从军旗到权威参照的过程并不完全清楚，更早还存在不同构词解释。',
 [['古法语 estandart、相关拉丁形式 → standard','军旗、醒目标志；更早来源有争议'],['参照、标准义 → standard + -s → standards','公认参照 → 多项标准、要求或水平']],
 'quality standards 质量标准；high standards 高要求；living standards 生活水平；meet the standards 达到标准。',
 'standards for the work；standards of service。','high standards 可说要求高；living standards 说生活条件、水平。标准义的历史不等于现代简单拆 stand + ard 就能直接推导全部意思。',
 ('The team checks whether the work meets the required standards.','团队检查这项工作是否达到所要求的标准。'),('She has high standards for her own writing.','她对自己的写作要求很高。'),sources=['https://en.wiktionary.org/wiki/standards#English','https://www.etymonline.com/word/standard'])
W('awards','英 /əˈwɔːdz/；美 /əˈwɔːrdz/','奖、奖项〔复数〕；授予、判给〔第三人称单数〕',
 '经过评选，把奖或某项权利给到一个人，是 awards 的动作；评选得来的一个个奖项，也叫 awards。老词里有考虑后作出裁定的背景。',
 'award + -s，/d/ 后读 /z/。award 经盎格鲁法语 awarder 等进入英语，旧义涉及考虑、裁定，较早接看守、观察的 warder 词族；英语名词、动词相互对应。',
 [['盎格鲁法语 awarder 等 → award','考虑后裁定 → 授予、判给'],['award + -s → awards','多个奖项；单数主语授予']],
 'film awards 电影奖项；win awards 获奖；awards prizes 颁奖；awards somebody a prize 给某人颁奖。',
 'awards for design；awards given each year。','win an award 是获奖，award somebody something 是把某物授予某人。The jury awards the prize 的 awards 是动词，The awards are announced 的是复数名词。',
 ('The film won three awards at the festival.','这部电影在电影节上获得了三个奖项。'),('The school awards prizes for creative writing.','学校为创意写作颁发奖项。'),sources=['https://en.wiktionary.org/wiki/awards#English','https://en.wiktionary.org/wiki/award#English'])
W('relations','/rɪˈleɪʃənz/','关系、往来；亲属〔relation 的复数〕',
 '把两个人、群体或事情联系起来的状态，是 relations 的关系义；和你有亲属联系的人，也可以叫 relations。',
 'relation + -s，/n/ 后读 /z/。法语 relation 接拉丁 relātiō，来自 referre 的 relātus 词干；现代可对照 relate 与 -ion，但名词有自己的借入历史。',
 [['拉丁 referre、relātus → relātiō → 法语、英语 relation','带回、报告等旧背景 → 叙述、联系、关系'],['relation + -s → relations','多方面关系；有亲缘联系的人']],
 'international relations 国际关系；relations with neighbours 与邻居的关系；close relations 近亲；public relations 公共关系。',
 'relations between the teams；relations visiting for the weekend。','relations 在 between、with 等结构里常说往来关系；my relations 常说我的亲属，与 relatives 相近。relation 单数还可说事物间的联系。',
 ('Relations between the two teams improved after the meeting.','会后，两个团队之间的关系改善了。'),('Several relations came to stay for the weekend.','几个亲戚周末来住了两天。'),sources=['https://en.wiktionary.org/wiki/relations#English','https://en.wiktionary.org/wiki/relation#English'])
W('communications','/kəˌmjuːnɪˈkeɪʃənz/','通信、通讯；对外沟通业务；消息、往来文件〔复数及集合用法〕',
 'communication 是把信息传过去、让双方知道；communications 可以把一次次消息往来看成多条，也常整体说通信系统或机构的对外沟通工作。',
 'communication + -s，/n/ 后读 /z/。名词经法语与拉丁 commūnicātiōn- 借入，与共享、使共同知道的词族相连；英语名词借入早于 communicate，不能只画成英语动词加后缀。',
 [['拉丁 commūnicātiōn- → 法语 communicacion → communication','共享、传达 → 沟通、信息传递'],['communication + -s → communications','多条消息；通信或沟通业务的集合用法']],
 'communications systems 通信系统；communications team 对外沟通团队；written communications 书面往来；satellite communications 卫星通信。',
 'communications between offices；communications sent to members。','communication 常说沟通过程或能力；communications 常说技术、业务、消息材料。communications team 的 s 是固定领域表达的一部分，不因为后面修饰 team 就机械删掉。',
 ('The storm disrupted communications across the region.','暴风雨使整个地区的通信受到影响。'),('Please keep copies of all written communications.','请保留所有书面往来的副本。'),sources=['https://en.wiktionary.org/wiki/communications#English','https://en.wiktionary.org/wiki/communication#English'])
W('affairs','英 /əˈfeəz/；美 /əˈferz/','事务、事情；私人感情关系〔affair 的复数〕',
 '需要处理、安排的一摊事情，是 affairs 的事务义。国家的事、个人的事，前面的词会告诉你是哪一摊。',
 'affair + -s，/eə/ 或 /er/ 后读 /z/。affair 来自法语 à faire 要做的，faire 接拉丁 facere 做；名词化后指事情，现代还有私情等语境。',
 [['拉丁 facere → 法语 faire；à faire → affaire → affair','做 → 要做的事 → 事情、事务'],['affair + -s → affairs；具体语境分化','多项事务；某些私人感情关系']],
 'current affairs 时事；foreign affairs 外交事务；personal affairs 私人事务；put affairs in order 把事务安排妥当。',
 'discuss current affairs；manage her own affairs。','current affairs 常说公共时事，personal affairs 可泛指私事。affair 还可指婚外等私情，但不能见到 affairs 就把所有事务句子都译成恋情。',
 ('They often discuss current affairs over lunch.','他们常在午饭时讨论时事。'),('She prefers to manage her own affairs.','她更愿意自己处理自己的事务。'),sources=['https://en.wiktionary.org/wiki/affairs#English','https://en.wiktionary.org/wiki/affair#English'])
W('banks','/bæŋks/','银行；河岸、堆积带〔复数，来源分支不同〕；存入、依赖〔第三人称单数〕',
 '金融语境的 banks 是银行；河边两侧隆起的地带，也叫 banks。它们在英语里走了不同借入路线，先分成两个清楚画面。',
 'bank + -s，/k/ 后读 /s/。银行义经法语 banque、意大利语 banca 柜台桌凳，联系钱币兑换台；河岸义经北欧相关地形词，两支有较远日耳曼亲缘背景，不能画成银行直接生出河岸。',
 [['意大利语 banca、法语 banque → 金融 bank','钱币兑换桌、柜台 → 银行'],['北欧地形词 → 河岸 bank；两支各加 -s → banks','河岸、隆起地带；多家银行或多处河岸等']],
 'local banks 当地银行；river banks 河岸；banks on help 指望得到帮助；banks the cash 把现金存入银行。',
 'banks along the street；trees on the banks of the river。','banks on somebody or something 是依赖、指望的动词短语。banks of the river 的 banks 则是河岸；附近名词常能直接区分这两支。',
 ('Several banks have branches near the station.','几家银行在车站附近设有分行。'),('Trees grew along both banks of the river.','河的两岸长着树。'),sources=['https://en.wiktionary.org/wiki/banks#English','https://www.etymonline.com/word/bank'])
W('businesses','/ˈbɪznəsɪz/','企业、商家〔business 的复数〕',
 '把经营活动当作整体，是 business；一家家具体经营的店铺、公司，则可以数成 businesses。',
 'business + -es，/s/ 后增加 /ɪz/。business 接古英语 bisiġnes、中古英语 businesse，历史对应 busy + -ness；现代企业可数义再形成 businesses。',
 [['busy 相关旧形 + -ness → business','忙碌、事务 → 商业、经营'],['business 的可数企业义 + -es → businesses','多家企业、商家']],
 'small businesses 小企业；local businesses 本地商家；family businesses 家族企业；support businesses 支持商家。',
 'businesses in the town centre；businesses owned by local families。','business 的常见读音压缩成 /ˈbɪznəs/，businesses 再加一个音节。泛说生意、商业用 business，数具体企业可用 businesses。',
 ('Local businesses stayed open late for the festival.','节日期间，本地商家营业到很晚。'),('Many small businesses use the shared workspace.','许多小企业使用这个共享办公空间。'),sources=['https://en.wiktionary.org/wiki/businesses#English','https://en.wiktionary.org/wiki/business#English'])
W('elections','/ɪˈlekʃənz/','选举〔election 的复数〕',
 '让有资格的人投票，从候选人中选出担任职务的人，就是 elections 的常见画面；复数可以数不同地区、职位或不同轮次的选举。',
 'election + -s，/n/ 后读 /z/。election 经法语接拉丁 ēlēctiō，联系 ēligere 选出及 ēlēctus；名词有独立借入链，现代与 elect、-ion 对照理解。',
 [['拉丁 ēligere、ēlēctus → ēlēctiō → 法语、英语 election','挑选、选出 → 选择、选举'],['election + -s → elections','多场、不同级别的选举']],
 'local elections 地方选举；hold elections 举行选举；student elections 学生组织选举。',
 'elections for the committee；elections held each year。','election 是选人的过程或事件，vote 可以说投票动作或一票；elections 不能按票数来数。选举结果用 election results，前面 election 常保持单数修饰。',
 ('The club holds elections for its committee each year.','这个俱乐部每年举行委员会选举。'),('Students helped organise the elections.','学生们协助组织了选举。'),sources=['https://en.wiktionary.org/wiki/elections#English','https://en.wiktionary.org/wiki/election#English'])
W('cells','/selz/','细胞；小房间、囚室；电池单元等〔cell 的复数〕',
 '一个个有边界的小隔间，是 cells 最好抓的老画面。生物学把微小结构借称为细胞，电学等领域也各自借用单元、隔室的形象。',
 'cell + -s，/l/ 后读 /z/。cell 接拉丁 cella 小房间、储藏室，英语早期有修道院小室等用法；细胞、电池单元等义在各自领域逐渐固定。',
 [['拉丁 cella → 英语 cell','小房间、隔间；修道院小室等'],['不同领域借用隔室形象；cell + -s → cells','生物细胞、电池单元等；多个隔间或单元']],
 'plant cells 植物细胞；blood cells 血细胞；prison cells 囚室；solar cells 太阳能电池。',
 'cells viewed through a microscope；cells in a battery。','cell 与 sell 发音相同，意义和拼写不同。生物、监狱、电学语境各有自己的 cell，不必把它们编成一个领域里的东西变成另一个。',
 ('The students examined plant cells under a microscope.','学生们用显微镜观察了植物细胞。'),('Solar cells cover part of the roof.','屋顶的一部分铺着太阳能电池。'),sources=['https://en.wiktionary.org/wiki/cells#English','https://www.etymonline.com/word/cell'])
W('ends','/endz/','末端、结尾；目的〔复数〕；结束〔第三人称单数〕',
 '一根绳子到头的地方、一件事做到最后的地方，是 ends；行动想要达到的结果，也可以称为 ends，也就是目的。',
 'end + -s，/d/ 后读 /z/。end 继承古英语 ende，名动词有较老的历史；目标义与所朝向的终点相连，现代仍有多个固定表达。',
 [['古英语 ende → end','端点、尽头、终结'],['end + -s → ends；终点与目标扩展','多个末端、目的；单数主语结束']],
 'both ends 两端；ends at five 五点结束；to achieve certain ends 达到某些目的；make ends meet 收支相抵、维持生计。',
 'ends of the rope；the meeting ends soon。','ends 的具体末端义容易看见；for their own ends 常说为了自己的目的。make ends meet 是收支能接得上的固定表达，作为整组记。',
 ('Hold both ends of the rope firmly.','牢牢抓住绳子的两端。'),('The class ends at half past four.','这节课四点半结束。'),sources=['https://en.wiktionary.org/wiki/ends#English','https://en.wiktionary.org/wiki/end#English'])
W('images','/ˈɪmɪdʒɪz/','图像、影像；形象〔复数〕；成像等〔第三人称单数〕',
 '眼前能看到的画面是 images；脑中想到的画面、公众心里对某人某事的印象，也可以用 image 这个形象词。',
 'image + -s，/dʒ/ 后增加 /ɪz/。image 经法语接拉丁 imāgō、imāginem；英语名词与动词还有相关但不同的借入路线，动词接法语 imagier 等。',
 [['拉丁 imāgō、imāginem → 法语 image → 英语名词','形象、相似形 → 图像、印象'],['相关法语动词等 → 英语动词；image + -s → images','多个画面、形象；单数主语成像等']],
 'digital images 数字图像；satellite images 卫星影像；mental images 脑中的画面；public images 公众形象。',
 'images stored on the computer；images that come to mind。','images 可包含照片、扫描图、绘图等，photos 范围通常较窄。image 的开头 im- 在这里是整个借词的一部分，不能按否定前缀拆。',
 ('The images are stored on a separate drive.','这些图像存储在单独的驱动器上。'),('The poem creates vivid images of the sea.','这首诗让人脑中浮现出生动的海洋画面。'),sources=['https://en.wiktionary.org/wiki/images#English','https://en.wiktionary.org/wiki/image#English'])
W('weapons','/ˈwepənz/','武器；有力的手段〔weapon 的复数〕',
 '用于攻击、防御的器具是 weapons；比喻里，能帮人应对困难、占据优势的能力或办法，也能叫 weapons。',
 'weapon + -s，/n/ 后读 /z/。weapon 继承古英语 wǣpn，日耳曼语言中有相关词，更深来源未定；现代比喻义借用武器发挥作用的形象。',
 [['古英语 wǣpn → weapon','武器；深源不定'],['weapon + -s → weapons；比喻扩展','多件武器；有力办法、能力']],
 'ancient weapons 古代兵器；weapons on display 展出的武器；weapons against doubt 应对怀疑的有力手段〔比喻〕。',
 'weapons in the museum；words used as weapons。','weapons 可以是实物，也能把语言、信息等比作有力或伤人的手段。字母 ea 在这里读 /e/，与 bread 的元音相同。',
 ('The museum displays weapons from several periods.','博物馆展出了几个时期的兵器。'),('Humour and patience were her best weapons against a difficult day.','面对难熬的一天，幽默和耐心是她最有力的办法。'),sources=['https://en.wiktionary.org/wiki/weapons#English','https://en.wiktionary.org/wiki/weapon#English'])
W('drugs','/drʌɡz/','药物；毒品〔复数，视语境〕；使服用药物等〔第三人称单数〕',
 'drugs 是能影响身体或心理作用的物质名称；药房、治疗语境常说药物，illegal drugs 等语境则说毒品。具体是哪一类要靠上下文。',
 'drug + -s，浊音 /ɡ/ 后读 /z/。drug 经中古英语 drogge、法语 drogue 等借入，较早常联系干货、干燥药材，但远源不确定；英语再形成动词。',
 [['法语 drogue 等 → 中古英语 drogge → drug','药材、药物等借词；更早来源未定'],['drug + -s → drugs；现代用途分化','多种药物或毒品；单数主语使服药等']],
 'prescription drugs 处方药；illegal drugs 非法毒品；drug stores 药店〔美式〕。',
 'drugs mentioned in the report；drugs sold by the pharmacy。','drug 不自带非法这层意思；medicine 更常以治病用途为中心。drug stores 的 drug 常用单数作修饰词，drugs 单独出现时按具体语境判断。',
 ('The report lists the drugs used in the study.','报告列出了研究中使用的药物。'),('The documentary examines the trade in illegal drugs.','这部纪录片探讨了非法毒品交易。'),sources=['https://en.wiktionary.org/wiki/drugs#English','https://en.wiktionary.org/wiki/drug#English'])
W('adults','/ˈædʌlts/、/əˈdʌlts/','成年人；成年动物〔adult 的复数〕',
 '已经长到成熟阶段的人，是 adults；说动物时也可以按幼体与成体区分。老词就是长成了的画面。',
 'adult + -s，/t/ 后读 /s/。adult 经法语 adulte、拉丁 adultus 借入，adultus 是 adolēscere 成长的过去分词；现代形容词也用作名词。',
 [['拉丁 adolēscere → adultus → 法语、英语 adult','成长 → 长成的、成年的'],['adult 名词 + -s → adults','多个成年人或成年动物']],
 'children and adults 儿童与成人；young adults 年轻成年人；adult birds 成年鸟类〔前置形容词〕。',
 'activities for adults；adults accompanying children。','adult 有前重音和后重音读法。adults 是可数名词；adult education 成人教育里的 adult 作修饰语，保持单数形式。',
 ('The workshop is open to adults and children.','这个工作坊对成人和儿童开放。'),('Two adults must accompany the group.','必须有两名成人陪同这个小组。'),sources=['https://en.wiktionary.org/wiki/adults#English','https://en.wiktionary.org/wiki/adult#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yl',ROOTS,WORDS)
 extend_lessons()
