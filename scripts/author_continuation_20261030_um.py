"""Useful plural-shaped words whose meanings exceed a mechanical -s rule."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0713':dict(words=['mean','means'],label='means：方法、可用资源与同形动词',note='方法、资源的 means 接法语中间、媒介词族；表示意味着的 means 接古英语 mænan 的动词，不能串成单一词源。'),
 'A1834':dict(words=['custom','customer','customary','customs','costume','customize'],label='custom 词族先看习惯，再分交易、定制与服饰',note='custom 的习惯、光顾和惯常征税分支分别接 customer、customs 等；customize 是定制；costume 经意大利语、法语另一条借入路径形成服饰词，并非现代 custom 加后缀。'),
 'B2504':dict(words=['work','works'],label='works：作品、工厂与进行中的项目',note='works 可说多件作品，也形成工厂、公共设施及 in the works 等固定用法；另可作 work 的第三人称动词形式。'),
 'C0706':dict(words=['manner','manners'],label='manner 与 manners：做法转为待人举止',note='manner 接拉丁 manus 手的操作、处理词族，经法语发展为方式；manners 在社会行为分支常指礼貌、礼仪。'),
 'C0456':dict(words=['fund','funds'],label='fund 与 funds：作为支撑的可用资金',note='fund 接底、基础的拉丁和法语材料；funds 常统称可用资金，也可说多个基金或作资助动词的形式。'),
 'C1395':dict(words=['spirit','spirits'],label='spirits：情绪、精灵与烈酒分支',note='精神、心境与呼吸生命的旧词族相连；烈酒分支经旧炼金术的挥发物、蒸馏物用法发展，现代按心境、精灵、酒类三支分别学习。'),
 'C1487':dict(words=['content','contents'],label='contents：装在里面的东西与目录',note='contents 的名词读音重读第一音节；接拉丁所含之物的旧名词材料，table of contents 说列出内容项目的目录。'),
 'B2424':dict(words=['minute','minutes'],label='minutes：分钟与会议记录同读，路径分开',note='时间名词接小分量；会议记录接摘要、草稿和小字笔记材料。两者常读 /ˈmɪnɪts/；微小的 minute 形容词读 /maɪˈnjuːt/ 或相应变体。'),
 'C1317':dict(words=['second','seconds'],label='seconds：秒、第二份食物与次品',note='秒接第二次六十分割；第二份食物和次品接次序、等级的 second 分支，各有固定名词用法。'),
 'C0751':dict(words=['premise','premises'],label='premises：从前述事项到房屋场地',note='前述事项在契据中常指已描述的房屋土地，后来 premises 形成场所义；论证的 premises 又是多个前提，按上下文分开。'),
}
W('means','/miːnz/','办法、手段；资源、财力；另源：mean 的第三人称动词形式',
 '目标在那头，能把你带过去的途径、工具是 means；能支撑你做到的资源，也叫 means。This means ... 则是在说这意味着什么。',
 '名词接 mean 的法语 meien、中世纪拉丁 medianus 中间、媒介词族，后有方法、可用财富义。动词 means 是 mean + -s，接古英语 mænan 打算、表示，属不同来源。',
 [['法语中间、媒介词族 → 名词 means','达成目标的办法；可用资源'],['古英语 mænan → mean + -s → means','打算、意味着的第三人称形式']],
 'a means of transport 一种交通工具；by means of 借助；live within one’s means 量入为出；This means ... 这意味着……。名词可说 a means、several means，单复数同形。',
 'by all means；by no means；the means to do something。','a means 不是写漏了复数：A bicycle is a means of transport。several means 又是复数。名词财力与动词意味着的词源分支不要混成一个故事。',
 ('A bicycle is an inexpensive means of transport.','自行车是一种便宜的交通工具。'),('They did not have the means to repair the old house.','他们没有修缮旧房子的财力。'),('This means we will need more time.','这意味着我们需要更多时间。'),sources=['https://www.etymonline.com/word/means','https://www.etymonline.com/word/mean','https://en.wiktionary.org/wiki/means#English'])
W('custom','/ˈkʌstəm/','习俗、惯例；光顾；定制的',
 '大家一直这样做，慢慢变成惯例；一个人总来某家店买东西，也成了光顾的习惯。定制义则把目光落到特定顾客的需要。',
 '经古法语 costume、盎格鲁法语 custume 等，接拉丁 consuetudo 习惯及 consuescere 习惯于。现代风俗、经常光顾、惯常税费和按顾客要求制作等义逐渐分开。',
 [['拉丁 consuetudo → 法语／中古英语 custume','习惯、惯常做法'],['现代 custom 的不同分支','风俗；光顾；为特定顾客制作的']],
 'a local custom 当地习俗；as is his custom 按他的习惯；Thank you for your custom 感谢惠顾，尤其英式；custom furniture 定制家具。',
 'follow a custom；custom software；a long-standing custom。','custom 指习惯或定制，costume 指服装；二者同源而分途借入。habit 常说个人习惯，custom 常说群体或长期沿用的做法，也可用于个人。',
 ('It is a local custom to bring a small gift.','带一份小礼物是当地习俗。'),('The workshop makes custom furniture for small apartments.','那间工坊为小公寓制作定制家具。'),sources=['https://www.etymonline.com/word/custom','https://en.wiktionary.org/wiki/custom#English'])
W('customer','英 /ˈkʌstəmə/；美 /ˈkʌstəmər/','顾客、客户；某种难易相处的人',
 '到店里买东西、向服务方下单的人，是 customer。背后的旧线索是惯常交易、光顾，但现代第一次上门的也叫 customer。',
 '现代可对应 custom + -er；历史经盎格鲁法语 custumer、古法语 coustumier 等，接中世纪拉丁惯例、税费词族。英语早期既见税费收取者，也发展出经常购买者、购买者等义。',
 [['拉丁／法语惯例、税费相关材料 → customer','早期税费人员、惯常买卖关系等'],['现代 customer','购买商品、服务的人；引申为要打交道的人']],
 'a regular customer 常客；a new customer 新顾客；customer service 客户服务；a tough customer 难对付的人，不必是真买东西的顾客。',
 'serve a customer；customer needs。','customer 不要求已经来过很多次；consumer 侧重使用、消费产品的人，购买者与最终使用者可能不同。',
 ('The shop assistant helped a customer choose a coat.','店员帮一位顾客挑选外套。'),('He is a tough customer in negotiations.','谈判时他是个难对付的人。'),sources=['https://www.etymonline.com/word/customer','https://en.wiktionary.org/wiki/customer#English'])
W('customary','英 /ˈkʌstəməri/；美 /ˈkʌstəmeri/','惯常的、按惯例的、习俗性的',
 '不必每次重新商量，大家通常就这样做。customary 说的是已经习惯、沿用的做法。',
 '历史经中世纪拉丁 custumarius 等惯例、税费词族发展，接拉丁 consuetudo；现代可对应 custom 与形容词 -ary。早期税费相关义后来退到后面，惯常义成为重点。',
 [['拉丁 consuetudo → 中世纪拉丁相关形容词','惯例；税费相关材料'],['英语 customary','按既有习惯、惯例行事的']],
 'it is customary to do something 惯例是做某事；the customary greeting 惯常问候；his customary seat 他平常坐的位置。',
 'as is customary；the customary practice。','customary 是惯常的，custom 是定制的时含义不同：customary clothes 可指按惯例的衣着，custom clothes 常说按个人要求制作的衣服。',
 ('It is customary to remove your shoes before entering.','进门前脱鞋是惯例。'),('She took her customary seat by the window.','她坐到了窗边那个平常坐的位置。'),sources=['https://www.etymonline.com/word/customary','https://en.wiktionary.org/wiki/customary#English'])
W('customs','/ˈkʌstəmz/','习俗〔复数〕；关税、海关及其检查处',
 'local customs 讲当地习俗；go through customs 却是在机场、口岸过海关。两者都从习惯、惯常做法这一旧词族分支而来。',
 'custom + -s；旧 custom 除习惯外也指惯常征收的通行税费，复数 customs 后来统称相应税费、负责收取检查的机构或区域。机构和场所义沿税费收取这一分支专门化。',
 [['custom 的惯例、惯常税费分支','习惯；按惯例征收的费用'],['customs 的专门化','多种习俗；关税、海关及检查区域']],
 'local customs 当地习俗；customs officers 海关人员；customs duties 关税；go through customs 过海关。普通过海关搭配通常不加 the。',
 'customs checks；respect local customs。','customs 的两类意思看搭配：learn about customs 多为了解习俗，baggage、officers、airport 等常指向海关。不能只凭末尾 s 就当多个风俗。',
 ('We waited at customs after collecting our bags.','取完行李后，我们在海关检查处等候。'),('The guide explained several local customs.','导游介绍了几种当地习俗。'),sources=['https://www.etymonline.com/word/custom','https://en.wiktionary.org/wiki/customs#English'])
W('costume','英 /ˈkɒstjuːm/；美 /ˈkɑːstuːm/','戏服、装扮服装；某时期或群体的服饰',
 '演员一穿上，观众就看出他是古代人物、海盗或舞者。costume 往往突出某个角色、时代、群体的那套装扮。',
 '经法语 costume，接意大利语 costume 风尚、习惯，上溯拉丁 consuetudo。与 custom 同源但不同路径、较晚借入，先有符合时代风俗的艺术表现等用法，后突出衣着。',
 [['拉丁 consuetudo → 意大利语、法语 costume','习俗、风尚；时代相符的表现'],['英语 costume','某种固定衣着、戏服、角色装扮']],
 'a pirate costume 海盗装；costume design 服装设计；traditional costume 传统服饰；a costume party 化装聚会。',
 'wear a costume；the costumes for a play。','clothes 泛指衣服；costume 常突出角色或文化、时代的整套外观。custom 定制与 costume 服饰可以同时出现，但不是一个单词的拼写变体。',
 ('The children wore animal costumes for the school play.','孩子们为学校话剧穿上了动物戏服。'),('The museum displays traditional costumes from the region.','博物馆展出该地区的传统服饰。'),sources=['https://www.etymonline.com/word/costume','https://en.wiktionary.org/wiki/costume#English'])
W('works','英 /wɜːks/；美 /wɝːks/','作品、工程；工厂、设施；全部配套；work 的第三人称形式',
 '做出来的东西可以是 works；把生产活动集中起来的地方也可叫 works。This works 则是在说这个办法管用。',
 'work 接古英语 weorc 等做事、劳动、制成品词族，works 是其复数，较早已说行为、事迹；后来有大型设施和工厂等固定用法。动词 work + -s 又与名词同形。',
 [['古英语 work 词族及复数','做过的事、劳动产品、作品'],['现代 works 的专门义及动词形式','作品、工厂；进行中；管用、工作']],
 'the works of an author 作者作品；a steel works 钢铁厂；in the works 正在筹办、制作；the works 全套；the machine works 机器能运作。',
 'public works；a project in the works。','a works 可指一处工厂，不能仅因 s 就认定一定是多个工厂。通常说有工作 work，不把 I have works 当普通我有工作的表达。',
 ('The library has collected works by local writers.','图书馆收藏了本地作家的作品。'),('The old steel works closed several years ago.','旧钢铁厂几年前关闭了。'),('This method works well for small teams.','这个办法对小团队很管用。'),sources=['https://www.etymonline.com/word/works','https://en.wiktionary.org/wiki/works#English'])
W('manners','英 /ˈmænəz/；美 /ˈmænərz/','礼貌、礼仪；举止；方式、风俗等〔manner 复数〕',
 '说话是否打断别人、吃饭时怎样待人，这一套外在举止是 manners。good manners 就是让相处舒服、合乎礼节的做法。',
 'manner 经法语 maniere 等，接拉丁 manus 手相关的操作、处理材料，发展为做事方式、举止。复数 manners 在社会行为这条分支上固定说礼貌、礼仪。',
 [['拉丁手的操作材料 → 法语／英语 manner','处理方式 → 行为方式、举止'],['manner + -s → manners','各种举止；特指社交礼仪、礼貌']],
 'good manners 有礼貌；bad manners 不礼貌行为；table manners 餐桌礼仪；mind your manners 注意礼貌。',
 'learn manners；polite manners。','manner 单数常说一种做法、姿态，manners 作为礼貌这一整体概念常保留复数。礼貌不等于只是声音小，具体表现依场景和文化。',
 ('She thanked the host and showed good manners.','她感谢了主人，表现得很有礼貌。'),('The children are learning table manners.','孩子们正在学习餐桌礼仪。'),sources=['https://www.etymonline.com/word/manners','https://en.wiktionary.org/wiki/manners#English'])
W('funds','/fʌndz/','资金、经费；基金〔复数〕；fund 的第三人称形式',
 '项目能不能做起来，底下要有一笔可动用的钱来托住。funds 常直接指这些可用资金，不要求分成几个独立基金。',
 'fund 经法语 fond，接拉丁 fundus 底、基础、土地等，由支撑的资本发展为可用钱款。funds 后固定统称财力、资金，也可为规则名词复数或资助动词形式。',
 [['拉丁 fundus → 法语 fond → fund','底、基础 → 可用资本、储备'],['fund + -s → funds','资金；多个基金；某方资助']],
 'raise funds 筹资；lack of funds 缺乏经费；public funds 公共资金；the charity funds the project 慈善机构为项目提供资金。',
 'available funds；funds for the library。','funds 常是钱款统称，a fund 可是一笔专项资金或基金。money 很宽泛，funds 常放在为特定目的提供、安排资金的语境。',
 ('The school raised funds for a new library.','学校为新图书馆筹集了经费。'),('We had to delay the repairs because of a lack of funds.','由于缺少资金，我们只好推迟维修。'),sources=['https://www.etymonline.com/word/fund','https://en.wiktionary.org/wiki/funds#English'])
W('spirits','英 /ˈspɪrɪts/；美 /ˈspɪrɪts/','情绪、心境；精灵、鬼魂〔复数〕；烈酒',
 'in high spirits 是兴高采烈，像整个人提起了气；a story about spirits 则可能讲精灵。菜单上的 spirits 又是烈酒这一固定分支。',
 'spirit 经法语、拉丁 spiritus 呼吸、气息，发展为生命、精神、心境等；精灵义也很早存在。烈酒义另经旧炼金术挥发物、蒸馏物的用法专门化，现代常用复数 spirits。',
 [['拉丁 spiritus → 英语 spirit／spirits','呼吸、生命 → 精神、心境；精灵'],['旧挥发物、蒸馏物用法 → spirits','后来专指烈酒的名词分支']],
 'in high spirits 兴高采烈；in low spirits 情绪低落；raise someone’s spirits 使某人振奋；evil spirits 邪灵；wine and spirits 葡萄酒与烈酒。',
 'lift our spirits；a tale of spirits。','情绪的 spirits 与酒类的 spirits 在现代靠搭配分清。spirits 作为烈酒名不意味着所有含酒精饮品都用这个词。',
 ('The children were in high spirits on the way to the beach.','去海边的路上，孩子们兴高采烈。'),('The old story tells of spirits living in the forest.','那个古老故事讲森林中居住的精灵。'),('The shop has separate shelves for wine and spirits.','商店把葡萄酒和烈酒分开放在不同货架上。'),sources=['https://www.etymonline.com/word/spirit','https://en.wiktionary.org/wiki/spirits#English'])
W('contents','英 /ˈkɒntents/；美 /ˈkɑːntents/','所装物品；内容项目；目录',
 '把盒子打开，里面装的所有东西是 contents；打开书，目录先把里面有什么一项项列给你看。',
 '接拉丁 contentum、复数 contenta 等所含之物的名词材料，上接 continere 把东西容在一起。英语 contents 很早就表示容器、文件所含的东西，后有 table of contents。',
 [['拉丁 continere → contentum／contenta','容纳 → 被容纳的东西'],['英语 contents','所装物品、内容；内容项目列表']],
 'the contents of the box 盒内物品；a table of contents 目录；empty the contents 倒出所装东西；the contents page 目录页。',
 'check the contents；the bag and its contents。','名词 contents 重读第一音节；满意的 content 常重读后面 /kənˈtent/。digital content 常作不可数内容统称，不能只因中文有很多内容就到处加 s。',
 ('She emptied the contents of her bag onto the table.','她把包里的东西都倒在桌上。'),('Use the table of contents to find the chapter.','用目录找到那一章。'),sources=['https://www.etymonline.com/word/contents','https://en.wiktionary.org/wiki/contents#English'])
W('minutes','/ˈmɪnɪts/','分钟〔复数〕；会议记录；minute 的第三人称形式',
 'ten minutes 是十分钟；take the minutes 是把会上讨论、决定的要点记下来。后一个意思要抓短笔记、摘要的旧线索。',
 '时间 minute 接拉丁小分量材料；记录义的 minute 较早指摘要、草稿，可能接 minuta scriptura 小字笔记等表达，后来复数 minutes 固定作会议记录。两支同属小、细的词族，但不是因为会议按分钟计时才产生记录义。',
 [['拉丁小分量材料 → 时间 minute／minutes','细分出来的时间单位'],['摘要、草稿、可能的小字笔记材料 → minutes','会议事项的书面记录']],
 'a few minutes 几分钟；take the minutes 记录会议；approve the minutes 确认会议记录；minutes of the meeting 会议记录。',
 'within ten minutes；send round the minutes。','分钟和会议记录都常读 /ˈmɪnɪts/；微小的 minute 是另一读法的形容词，英常 /maɪˈnjuːt/。句中 take、meeting、approve 常帮助辨认记录义。',
 ('The walk takes about fifteen minutes.','步行大约需要十五分钟。'),('Could you take the minutes at today’s meeting?','你能为今天的会议做记录吗？'),sources=['https://www.etymonline.com/word/minute','https://www.etymonline.com/word/minutes','https://en.wiktionary.org/wiki/minutes#English'])
W('seconds','/ˈsekəndz/','秒〔复数〕；第二份食物；次品；second 的第三人称形式',
 '几秒钟是 seconds；吃完一份又添一份，是 have seconds。它还可指质量第二档的货品，后两支都抓第二这一层。',
 'second 的秒义接中世纪拉丁第二次细分：小时六十分得分钟，再六十分得秒。添饭、次品等则接 second 次序或等级的用法，复数形成固定名词。',
 [['拉丁 second 的第二、接续词族 → 时间单位','第二次六十分割 → 秒'],['second 的次序、等级分支 + -s','再来一份；第二档、未达一等标准的货品']],
 'ten seconds 十秒；go back for seconds 再添一份；factory seconds 工厂次品、瑕疵品；she seconds the proposal 她附议提案。',
 'in seconds；Would you like seconds?。','have seconds 常是再吃一份，不是拥有几秒。seconds 作货品名也不自动等于二手货：次品与用过是两个不同维度。',
 ('The screen went blank for a few seconds.','屏幕黑了几秒钟。'),('The soup was so good that everyone went back for seconds.','汤太好喝，大家都又添了一份。'),('The outlet sells factory seconds with small defects.','那家折扣店销售带小瑕疵的工厂次品。'),sources=['https://www.etymonline.com/word/second','https://en.wiktionary.org/wiki/seconds#English'])
W('premises','/ˈpremɪsɪz/','房屋及其场地、营业场所；另为 premise〔前提〕的复数',
 'Please leave the premises 是请离开这个场所；the premises of an argument 却是论证的前提。场所义有一段文书中前述房产的历史。',
 'premise 接拉丁 praemissa 预先放在前面的事项，来自 prae- 在前与 mittere 送出。文书里前述事项常是已描述的房屋土地，复数 premises 因而发展为房屋及场地；逻辑前提义仍独立使用。',
 [['拉丁 praemissa → premise','前面已经提出、说明的事项；逻辑前提'],['文书中的前述房屋土地 → premises','房屋、场地；现代场所名称']],
 'business premises 营业场所；on the premises 在该场所内；leave the premises 离开场地；false premises 错误的前提。',
 'new premises；the premises are closed。','场所义通常保留复数形式：new premises 可以指一处新场地。单数 a premise 通常更容易被理解为一个论证前提，不能逐字倒推成一间房。',
 ('The company moved to larger premises last year.','公司去年搬到了更大的办公场地。'),('The argument rests on two false premises.','那套论证建立在两个错误前提上。'),sources=['https://www.etymonline.com/word/premises','https://en.wiktionary.org/wiki/premises#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_um',ROOTS,WORDS)
 extend_lessons()
