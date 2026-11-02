"""Holders, berries, polls and deliciousness."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
H=[['hold + -er → holder','持有、保管某物的人；承托某物的装置'],['对象 + holder','按持有对象形成身份名称']]
W('stakeholder','英 /ˈsteɪkhəʊldə/；美 /ˈsteɪkhoʊldər/','利益相关者；赌注保管人〔原有用法〕',
 '一项决定会影响你的工作、生活或利益，你就可能是它的 stakeholder。它不是只数谁手里有公司股票。',
 'stake + holder。旧义是替赌局保管赌注的人；后来常见的利益相关者义，接 stake 在某事中的利益、利害关系。两层都看 stake 的具体意思。',
 H+[['stake + holder → stakeholder','赌注保管者；在某事中有利害关系的个人、机构']],
 'key stakeholders 主要利益相关者，consult local stakeholders 征询当地利益相关者意见。居民、雇员、客户等都可能算，具体范围由项目决定。',
 'key stakeholders；consult stakeholders；stakeholder interests。',
 'shareholder 明确是股东；stakeholder 范围更广。不持股的附近居民，也可能受工厂扩建影响而成为 stakeholder。',
 ('The project team met with local stakeholders before changing the plan.','项目团队改方案前与当地利益相关者开了会。'),('Employees and customers are important stakeholders in the business.','员工和客户是企业重要的利益相关者。'))
W('placeholder','英 /ˈpleɪshəʊldə/；美 /ˈpleɪshoʊldər/','占位内容、占位符；暂时替代物',
 '真正的照片还没来，先放一个灰框；标题还没想好，先写几个字顶着。这些先把位置留住的东西就是 placeholder。',
 'place 位置 + holder 占住、保留位置者。从实体代用品扩到文字、图像、程序等临时内容。',H+[['place + holder → placeholder','暂时占住位置，等待最终内容替换']],
 'placeholder text 占位文字，a placeholder image 占位图片，use a placeholder 先用占位内容。输入框里的浅色提示也常这样称呼，通常输入后消失。',
 'placeholder text；a placeholder image；use a placeholder。',
 'placeholder 暂时顶位置；default 是未另作选择时采用的默认值。输入框提示不一定就是已经填入、可提交的值。',
 ('The designer used a grey box as a placeholder for the photo.','设计师用一个灰框给照片占位。'),('We replaced the placeholder title before publishing the page.','发布页面前，我们换掉了临时标题。'))
W('policyholder','英 /ˈpɒləsihəʊldə/；美 /ˈpɑːləsihoʊldər/','保单持有人、投保人',
 '拿着保险合同里的保单持有人身份，和保险公司建立相应合同关系的人或机构，叫 policyholder。关键是合同身份，不是手里正拿着一张纸。',
 'policy 在这里是保险单、保险合同 + holder 持有者；不取 policy 政策这个意思。',H+[['policy 保险单 + holder → policyholder','保险合同中的保单持有人']],
 'the policyholder’s details 保单持有人资料，notify the policyholder 通知保单持有人。具体权利、缴费与变更规则由合同和相应制度确定。',
 'the policyholder’s details；notify the policyholder。',
 'policyholder 不一定就是被保险人，也不一定就是领取赔款的受益人。例如有人为家人投保，这些角色可能分属不同人。',
 ('The form asks for the policyholder’s name and address.','表格要求填写保单持有人的姓名和地址。'),('The insurer sent the renewal notice to the policyholder.','保险公司把续保通知寄给了保单持有人。'))
R('B4494','持有某种权利、合同、物件，或为内容占住位置','HOLDER：看持有什么，也看是不是承托、占位功能','holder → shareholder、stockholder 看股份；policyholder 看保单；stakeholder 看利害；placeholder 看预留位置。',
 'hold 的持有不只限于手里抓住。身份、权利、位置和实物都能成为持有对象，复合词因此各有专门含义。',
 'hold + -er → holder；stake／place／policy 等对象成分与 holder 组合。',
 [['持有身份','holder · shareholder · stockholder · cardholder · policyholder'],['利益相关与占位','stakeholder · placeholder']],
 'stakeholder 不只指股东；policyholder 不是政策制定者；placeholder 是占位内容。',
 'The placeholder in the form shows where the policyholder’s name belongs.\n\n表格里的占位提示标明了保单持有人姓名该填在哪里。','holder shareholder stockholder cardholder policyholder stakeholder placeholder')
B=[['古英语 berġe 等 → 中古英语 berie → berry','小型多汁果实的古老名称'],['与别的成分组成果名','strawberry、cranberry、gooseberry 等；名称不保证符合植物学浆果分类']]
W('berry','/ˈberi/','浆果；日常所说的小型多汁果实',
 '日常说 berries，常想到一把蓝莓、草莓等小果子。植物学的 berry 则是按果实如何发育来分，不能只看名字。',
 '承接古英语 berġe、berie 等形式，经中古英语 berie 留传。其他表示土丘、洞穴等的旧同形词不拿来解释现代果实义。',B,
 'fresh berries 新鲜浆果类水果，a berry bush 结这类果实的灌木。复数变 berries，去 y 加 -ies。日常果名与专业分类不必完全一致。',
 'fresh berries；a berry bush；pick berries。',
 '名字含 berry，不保证植物学上就是单一子房发育的浆果；学普通英语时先按日常食物、植物名称理解。',
 ('She added fresh berries to her breakfast.','她在早餐里加了新鲜浆果类水果。'),('The children picked berries beside the path.','孩子们在小路旁摘果子。'))
W('strawberry','英 /ˈstrɔːbəri/；美 /ˈstrɔːberi/，也读 /ˈstrɑːberi/','草莓；草莓味的、草莓色的',
 '这个果名很熟悉，但 straw 为什么会和 berry 组合，并没有一个已经证实的简单故事。记构词可以，别把铺稻草种草莓当成确定起源。',
 '古英语 strēawberġe 等形式已存在，接 straw 稻草、茎秆 + berry。命名缘由不确定，细茎、表面小果等解释均有人提出。',B[:1]+[['古英语 strēawberġe → 中古英语 strawberie → strawberry','古老果名；straw 的具体命名缘由未定']],
 'fresh strawberries 鲜草莓，strawberry jam 草莓酱，strawberry ice cream 草莓冰激凌。修饰食物时可指口味，不保证一定用了完整鲜果。',
 'fresh strawberries；strawberry jam；strawberry ice cream。',
 'strawberry 是固定果名，不靠字面判断栽培方式。莓的日常名称也不等于严格植物学分类。',
 ('We bought strawberries at the market.','我们在市场买了草莓。'),('She chose strawberry ice cream.','她选了草莓冰激凌。'),sources=['https://en.wiktionary.org/wiki/strawberry#English','https://www.etymonline.com/word/strawberry'])
W('cranberry','英 /ˈkrænbəri/；美 /ˈkrænberi/','蔓越莓；蔓越莓色的',
 '这种酸味红果子的名字，经借用、改造留着原来鹤加莓的结构。现在 cran- 已不是一个随处能单独使用的现代英语词。',
 '改自低地德语等形式 Kraanbeere，前半与 crane 鹤同源，后半是 berry 的对应词。为何联系鹤仍有疑问，花部像鹤嘴只是解释之一。',B[:1]+[['低地德语 Kraanbeere 等 → 英语 cranberry','鹤相关成分 + 莓；借入后形成固定果名']],
 'cranberry juice 蔓越莓汁，cranberry sauce 蔓越莓酱，dried cranberries 蔓越莓干。常见于食品、配料名称。',
 'cranberry juice；cranberry sauce；dried cranberries。',
 'cran- 是这个固定词里的旧成分，不是可以自由加在任意词前的现代前缀；也不是 cranial 的缩写。',
 ('The recipe calls for dried cranberries.','食谱需要蔓越莓干。'),('They served cranberry sauce with dinner.','他们晚餐配了蔓越莓酱。'),sources=['https://en.wiktionary.org/wiki/cranberry#English','https://www.etymonline.com/word/cranberry'])
W('gooseberry','英常见 /ˈɡʊzbəri/；也读 /ˈɡuːsbəri/；美 /ˈɡuːsberi/','醋栗；鹅莓；电灯泡〔英式口语搭配〕',
 '一种常带酸味、可做甜点的果实。英国口语里 play gooseberry 还可说跟情侣待在一起、显得多余的第三个人。',
 '表面对应 goose 鹅 + berry。前半来源与命名理由未定；有外来果名被改成 goose 的解释，也有按字面组合的分析，不编成鹅最爱吃的果子。',B[:1]+[['goose + berry 的固定果名','前半的真实来源、命名理由仍有争议'],['play gooseberry 的口语扩展','在情侣旁作多余的第三人']],
 'gooseberry jam 醋栗酱，a gooseberry bush 醋栗灌木，play gooseberry 当电灯泡。Chinese gooseberry 是猕猴桃的旧英语名称，不等于普通 gooseberry 同一植物。',
 'gooseberry jam；a gooseberry bush；play gooseberry。',
 'gooseberry 的前半读音有变化，不必强按 goose 的独立读音。也别把所有含 gooseberry 的植物俗名都当同一种果实。',
 ('She made a tart with fresh gooseberries.','她用鲜醋栗做了一个果馅饼。'),('I stayed home because I did not want to play gooseberry.','我留在家里，因为不想去当电灯泡。'),sources=['https://en.wiktionary.org/wiki/gooseberry#English','https://www.etymonline.com/word/gooseberry'])
R('B3354','日常果实名称，以及借入和旧构词留下的差异','BERRY：果名可以直观，也可能保留说不清的古老命名','berry → blackberry、blueberry 可看颜色；strawberry、cranberry、gooseberry 的具体命名不能全靠现代字面猜。',
 '把常吃果名放一起记，同时知道解释的边界：构词成分看得见，不代表命名缘由都已经确定。',
 '古英语 berġe → berry；复数 berries；有些名称直接组合，有些经借词、改造而来。',
 [['基础及常见果名','berry · strawberry · blackberry · blueberry'],['其他果名','cranberry · gooseberry · elderberry']],
 '日常 berry 与植物学分类不同；gooseberry 不必从鹅的食物硬猜，cran- 也不是自由前缀。',
 'The fruit stall sold strawberries, blueberries, cranberries and gooseberries.\n\n水果摊卖草莓、蓝莓、蔓越莓和醋栗。','berry strawberry blackberry blueberry cranberry gooseberry elderberry')
P=[['中古英语 pol／polle；联系低地德语、荷兰语的对应形式','头、头顶'],['按人头计数 → poll','投票、计票；后来也说意见调查']]
W('poll','英 /pəʊl/；美 /poʊl/','民意调查；投票；调查、征询意见',
 '原来是头。数人头，就能数有多少人支持某个选择；再从实际投票扩到询问一批人的意见。',
 '中古英语 pol、polle 的头、头顶义，与中古荷兰语等对应形式有关。由数人头发展投票、意见调查；不是 pole 杆子换了拼写。',P,
 'an opinion poll 民意调查，conduct a poll 开展调查，poll voters 调查选民，go to the polls 去投票。调查结果只反映相应对象、问题和时间，不等于正式投票结果。',
 'an opinion poll；conduct a poll；poll voters；go to the polls。',
 'poll 可指调查或投票；survey 范围更宽，可调查房屋、地形等。polled 是进行调查的词形，不是把 pole 加过去式。',
 ('The poll asked residents about public transport.','这项调查询问居民对公共交通的看法。'),('The newspaper polled five hundred readers.','报纸调查了五百名读者。'))
W('pollster','英 /ˈpəʊlstə/；美 /ˈpoʊlstər/','民意调查人员、机构；民调专家',
 '把设计问题、询问公众、分析回答作为工作的人或机构，就是 pollster。它是做调查的一方，不是被调查的人。',
 'poll 民意调查 + -ster 人物后缀；随着职业化调查形成专门名称。这里 -ster 不限定女性，也不自动含贬义。',P+[['poll + -ster → pollster','从事民意调查、分析的人或机构']],
 'an independent pollster 独立民调人员或机构，pollsters’ estimates 民调机构的估计。常见于政治、社会意见报道。',
 'an independent pollster；pollsters’ estimates。',
 'pollster 组织、分析调查；respondent 回答问题。调查结果也不等于 pollster 本人的政治立场。',
 ('The pollster interviewed voters in several cities.','民调人员在几个城市访问了选民。'),('Several pollsters reported similar findings.','几家民调机构报告了相似的发现。'))
W('tadpole','英 /ˈtædpəʊl/；美 /ˈtædpoʊl/','蝌蚪',
 '看到一个头部显眼、后面拖着尾巴的小生命，这就是 tadpole 的命名画面：蟾蜍的头。名字描述幼体，不是在说一根小杆。',
 '中古英语 tadpolle 等，前半是 toad 蟾蜍的旧形式，后半 poll 头。现代可指蛙、蟾蜍等的水生幼体。',P[:1]+[['toad 的旧形式 + poll 头 → tadpole','头部显眼、带尾巴的两栖动物幼体']],
 'frog tadpoles 蛙的蝌蚪，tadpoles in a pond 池塘里的蝌蚪。发育过程会变化，后期长出腿仍可能称 tadpole，不把没腿当每一阶段的绝对条件。',
 'frog tadpoles；tadpoles in a pond。',
 'tadpole 的 pole 不等于杆子 pole；它保存头的 poll 旧义。名字起于 toad 相关形式，实际用法不限于蟾蜍幼体。',
 ('The children watched tadpoles swimming in the pond.','孩子们看着池塘里的蝌蚪游动。'),('Some of the tadpoles had begun to grow legs.','有些蝌蚪已经开始长腿。'))
R('B4200','从头、人头到计票与意见调查；蝌蚪保存另一条旧义','POLL：先是头，数人头才走到投票和民调','poll → pollster 做民调者；tadpole 的后半保存头的旧义。',
 '同一个旧意思分两路：政治用法数人头，动物名称看头部形状。不要用今天最常见的民调义倒推蝌蚪。',
 '中古英语 pol、polle 头 → 投票、调查；poll + -ster；toad 旧形式 + poll → tadpole。',
 [['调查、投票与职业','poll · pollster'],['保存头的旧义','tadpole']],
 'poll 与 pole 同音，词源不能直接混；tadpole 不是投票小杆。',
 'The teacher used poll and tadpole to show two developments from the older sense of head.\n\n老师用 poll 和 tadpole 展示头这一旧义的两条发展路线。','poll pollster tadpole')
D=[['拉丁 dēliciae 等：乐趣、愉悦 → dēliciōsus','令人愉悦的'],['法语 delicious／delicieux → 英语 delicious','悦人的；常用来夸食物美味']]
W('delicious','/dɪˈlɪʃəs/','美味的；令人愉悦、痛快的',
 '吃一口就觉得真好吃，是 delicious 最常见的画面。它的历史范围更宽，也能形容一种让人享受的感觉。',
 '经古法语、盎格鲁诺曼语接拉丁 dēliciōsus，再联系 dēliciae 乐趣、愉悦。词尾对应 -ous 的性质形容词，但不按现代 delicious 硬拆成 deli 店 + cious。',D,
 'a delicious meal 美味的一餐，a delicious smell 诱人的香味，a delicious irony 令人玩味、痛快的讽刺。非食物用法常带更鲜明的文体色彩。',
 'a delicious meal；a delicious smell；a delicious irony。',
 'delicious 常是积极的感官评价；delicate 是精细、脆弱或清淡等，虽然历史有关，现代不等义。',
 ('The soup was absolutely delicious.','这汤真是太好喝了。'),('A delicious smell drifted from the kitchen.','厨房飘出诱人的香味。'))
W('deliciously','/dɪˈlɪʃəsli/','美味地；令人愉悦地、痛快地',
 '把 delicious 的赞美放到某种味道、效果如何呈现上：酥得好吃，或故事荒诞得让人很享受。',
 'delicious + -ly，形成副词；不仅修饰吃，也可修饰形容词，说明那种性质让人觉得愉悦。',D+[['delicious + -ly → deliciously','以令人愉悦、美味的方式或程度']],
 'deliciously crisp 酥脆可口，deliciously sweet 香甜可口，deliciously absurd 荒诞得令人愉快。',
 'deliciously crisp；deliciously sweet；deliciously absurd。',
 'deliciously 不能机械译成吃得美味；The pastry is deliciously crisp 说糕点酥脆得好吃，不是某个人吃的动作。',
 ('The pastry was deliciously crisp.','糕点酥脆可口。'),('The comedy was deliciously absurd.','这部喜剧荒诞得令人十分愉快。'))
W('deliciousness','/dɪˈlɪʃəsnəs/','美味；令人愉悦的特质',
 '不再直接夸这道菜好吃，而是把它有多好吃当成一件事来谈，这就用 deliciousness。',
 'delicious + -ness，把性质变成名词。现代常说食物的美味，通常不可数。',D+[['delicious + -ness → deliciousness','美味这一性质']],
 'the deliciousness of the sauce 酱汁的美味，sheer deliciousness 纯粹的美味享受。日常直接说 It tastes delicious 往往更轻便。',
 'the deliciousness of；sheer deliciousness。',
 'delicious 形容食物，deliciously 修饰呈现方式或性质，deliciousness 才把美味作为名词谈。',
 ('Everyone commented on the deliciousness of the sauce.','大家都赞叹酱汁的美味。'),('The review praised the simplicity and deliciousness of the dish.','评论称赞这道菜简单又美味。'))
R('B3710','令人愉悦、美味的性质、表现方式和状态名词','DELICIOUS：让人享受，食物是最常见对象','delicious → deliciously / deliciousness。',
 '词源里的愉悦比今天常用的好吃更宽。解释非食物用法时，抓住享受、痛快的感觉就容易理解。',
 '拉丁 dēliciōsus 经法语进入英语；-ly 副词，-ness 性质名词。',
 [['性质、方式与名词','delicious · deliciously · deliciousness']],
 'delicious 不等于 delicate；deliciously crisp 是酥脆可口，别逐字译成美味地脆。',
 'The delicious tart was deliciously crisp, and everyone praised its deliciousness.\n\n果馅饼美味、酥脆，大家都赞叹它好吃。','delicious deliciously deliciousness')
if __name__=='__main__':save('continuation_20261030_jc',ROOTS,WORDS)
