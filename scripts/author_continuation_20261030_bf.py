"""Husband, lady and organization: household history and modern roles."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
HU=[['古诺尔斯语 húsbóndi 等 → 古英语 hūsbonda → husband','hús 家 + bóndi 居住者、户主等；借入、仿译关系有不同分析'],['现代 husband','妻子、配偶关系中的丈夫；旧管理者义接节约管理动词']]
W('husband','/ˈhʌzbənd/','丈夫；节约、妥善管理〔动词，正式〕',
 '今天最常见是婚姻关系里的丈夫；动词则像管好一份家业，仔细分配有限资源。',
 '接古英语 hūsbonda，与北欧 húsbóndi 家的居住者、户主有关。后部是旧居住者、户主词，不是现代 band 乐队；管理者旧义留在动词里。',HU,
 'her husband 她丈夫，husband resources 节约使用资源，husband your strength 保存体力。动词较正式、书面。',
 'her husband；husband resources；husband your strength。',
 'husband 名词丈夫，动词管好、节用；不是给东西找丈夫。与 house 有旧来源关系，但不能把 hus 当现代能任意拼词的前缀。',
 ('Her husband works at the local library.','她丈夫在当地图书馆工作。'),('They had to husband their supplies during the long journey.','长途旅程中，他们得节约使用补给。'),sources=['https://www.etymonline.com/word/husband','https://en.wiktionary.org/wiki/husband#English'])
W('husbandry','/ˈhʌzbəndri/','农牧业经营；饲养管理；资源的妥善管理',
 '把土地、牲畜、资源照料好，让它们持续供养生活；不是研究怎样当丈夫的一门学科。',
 '中古英语 husbanderi 等来自当时户主、经营者义的 husband + -ry。家庭、土地经营背景走向农牧管理，也保留审慎使用资源的义。',HU+[['中古英语 husbanderi 等 → husbandry','户、农场经营 → 农牧照料和审慎管理']],
 'animal husbandry 畜牧、动物饲养管理，good husbandry 良好经营管理，careful husbandry of resources 审慎管理资源。',
 'animal husbandry；good husbandry；husbandry of resources。',
 'husbandry 管理、照料活动，husband 常见是丈夫；animal husbandry 的 animal 是饲养对象，不是动物配偶关系称呼。',
 ('The course covers animal husbandry and farm management.','课程介绍动物饲养管理和农场经营。'),('Careful husbandry of resources helped the project continue.','审慎管理资源帮助项目继续进行。'))
R('B2490','家的居住者、户主背景；丈夫与妥善经营','HUSBAND：旧户主、经营者；今天丈夫，动词仍可节用','husband → husbandry；分别看婚姻称呼、节约管理动词与农牧管理名词。',
 '北欧、古英语家庭词的历史比现代 hus+band 的拼字游戏可靠；后部不是乐队，也不从绑住妻子编故事。',
 '旧 hús 家 + bóndi 居住者、户主 → husband；旧 husband 经营者义 + -ry → husbandry。',
 [['家庭角色与管理','husband · husbandry']],
 'husband resources 节约资源，animal husbandry 饲养管理；后部不是现代 band 乐队、带子。',
 'Her husband studies animal husbandry and carefully husbands the farm’s resources.\n\n她丈夫研究饲养管理，也仔细管理农场资源。',
 'husband husbandry')
LA=[['古英语 hlǣfdīġe → 中古英语 lafdi、lavedi 等 → lady','女主人、地位较高的女性；传统拆解联系面包与和面者，但语义动机有争议'],['现代 lady','女士；贵族、特定身份称呼；Our Lady 指圣母玛利亚']]
def L(f,m):return LA+[[f,m]]
W('lady','/ˈleɪdi/','女士；女性；夫人、贵族女性称呼；圣母〔Our Lady〕',
 '可以是礼貌称呼一位女性，也可以在故事、姓名前标出特定身份；语气和场合很关键。',
 '从古英语 hlǣfdīġe 女主人延续，传统常联系 hlāf 面包与和面者成分，但具体语义解释受过质疑。可靠的是旧女主人到女士、身份称呼的发展，不编成所有女人都因做面包得名。',LA,
 'a young lady 年轻女士，Ladies and gentlemen 女士们先生们，Lady + 名字用于特定身份称呼；Our Lady 宗教语境指圣母。',
 'a young lady；Ladies and gentlemen；the lady at the desk；Our Lady。',
 'woman 普通中性的女性类别，lady 常更客气、带身份或风度意味；某些直接称呼语气也可能不客气，不能只靠字面判礼貌程度。',
 ('The lady at the desk helped me find the room.','服务台那位女士帮我找到了房间。'),('Ladies and gentlemen, welcome to the concert.','女士们先生们，欢迎来到音乐会。'),sources=['https://www.etymonline.com/word/lady','https://en.wiktionary.org/wiki/lady#English'])
W('ladylike','/ˈleɪdilaɪk/','淑女般的；举止文雅得体的',
 '按传统想象的淑女样子来评价举止、穿着；这个评价带有时代、文化里的期待。',
 'lady + -like 像……的。不是对女性的客观生物分类，而是对行为风格的社会评价。',L('lady + -like → ladylike','符合淑女形象的举止、风格'),
 'ladylike manners 文雅举止，a ladylike manner 淑女般的举止；小说中也可被用来要求女性守某套规范。',
 'ladylike manners；a ladylike manner；behave in a ladylike way。',
 'ladylike 传统风度评价，female 女性的是类别词；女性并不必然按某时代的 ladylike 标准行动。',
 ('The novel questions what counted as ladylike behaviour.','小说追问什么样的行为才被算作淑女举止。'),('She greeted the guests with ladylike composure.','她以文雅从容的姿态迎接客人。'))
W('ladyship','/ˈleɪdiʃɪp/','夫人身份；夫人阁下〔Your/Her Ladyship〕',
 '在贵族称谓、历史故事中，用一种很正式的方式叫或提到有相应身份的女士。',
 'lady + -ship，中古英语已有对应形式。后缀表身份、地位，不是坐船的 ship。现代常见固定尊称或戏谑仿用。',L('lady + -ship → ladyship','身份、地位；固定正式称呼'),
 'Your Ladyship 对本人说的尊称，Her Ladyship 提到她时的称呼；具体称谓依作品、身份背景。',
 'Your Ladyship；Her Ladyship；addressed as Your Ladyship。',
 'lady 普通女士或身份词，Ladyship 固定正式尊称；Your 是对面说，Her 是谈到第三人。不要把每位顾客都自动这样称呼。',
 ('The servant asked whether Her Ladyship needed anything.','仆人问夫人是否还需要什么。'),('In the play, the visitor says, “Thank you, Your Ladyship.”','剧中，访客说：“谢谢您，夫人阁下。”'))
W('ladybug','/ˈleɪdibʌɡ/','瓢虫〔美式常用〕',
 '常见背上有斑点的小甲虫；名字中的 lady 不是说每只都是雌性。',
 'lady 在此指 Our Lady 圣母玛利亚 + bug 虫。名称来自相关欧洲宗教、民间命名传统，不按现代女士虫逐字翻。',LA+[['Our Lady〔圣母称呼〕+ bug → ladybug','传统命名的瓢虫；美式常用']],
 'a red ladybug 红色瓢虫，a ladybug on a leaf 叶上的瓢虫。不同种类颜色、斑点数量不同。',
 'a ladybug on a leaf；a red ladybug；a spotted ladybug。',
 'ladybug 美式、ladybird 英式常指同类甲虫；两词都不按雌雄分，也不是 bug 与 bird 的现代生物分类较量。',
 ('A ladybug landed on the leaf.','一只瓢虫落在叶子上。'),('The children watched a ladybug crawl across the window.','孩子们看着一只瓢虫爬过窗面。'))
W('ladybird','英 /ˈleɪdibɜːd/；美 /ˈleɪdibɜːrd/','瓢虫〔英式常用〕',
 '和 ladybug 先认作同一种常见小甲虫的两种地区名称；看到 bird 不要直接脑补长羽毛的鸟。',
 'lady 指圣母 + bird。历史民间命名里 bird 出现在这个昆虫名称中，整体已经固定，不能由两个现代分类词重新判定物种。',LA+[['Our Lady〔圣母称呼〕+ bird → ladybird','固定昆虫名称；英式常用']],
 'a ladybird on a flower 花上的瓢虫，ladybird spots 瓢虫斑点。常见英式儿童读物和日常自然描述。',
 'a ladybird on a flower；ladybird spots；a tiny ladybird。',
 'ladybird 是昆虫名称，songbird 鸣禽才是鸟类称呼；ladybug 是常见对应美式名，不是瓢虫的另一性别。',
 ('A tiny ladybird was resting on the flower.','一只小瓢虫停在花上。'),('The picture book shows a ladybird with black spots.','图画书上画着一只有黑斑的瓢虫。'))
R('B3477','女主人到女士；身份、风度与圣母称呼支线','LADY：女性称呼有身份、语气；瓢虫接 Our Lady','lady → ladylike、ladyship；ladybug、ladybird 相邻作为地区对应名称；landlady 已有共享。',
 '传统面包与和面者拆解有语义争议，注明分寸。瓢虫名里的 lady 是宗教称呼，不接普通雌性分类。',
 '古 hlǣfdīġe → lady；lady + -like/-ship；Our Lady + bug/bird；land + lady。',
 [['人物、身份与风度','lady · ladylike · ladyship · landlady'],['同类昆虫的地区名称','ladybug · ladybird']],
 'lady 与 woman 用语场合不同；ladyship 正式尊称；ladybug/ladybird 同类昆虫且不分雌雄；lady 远源拆解有争议。',
 'The lady showed the children a ladybird, also called a ladybug.\n\n那位女士给孩子们看一只瓢虫，也就是美式英语里的 ladybug。',
 'lady ladylike ladyship landlady ladybug ladybird')
OR=[['organize、organization 的组织与有序安排词系','把部分安排成可运作的整体'],['re-/dis- 与相应名词、动词形式结合','重新安排；打乱、缺少有序安排']]
W('reorganization','英 /riːˌɔːɡənaɪˈzeɪʃən/；美 /riːˌɔːrɡənəˈzeɪʃən/','重组；重新安排、整理',
 '已经有一套结构，再把岗位、团队、顺序等重新排过；可以大改，也可以调整。',
 're- 再次 + organization，亦对应 reorganize 的相应名词。这里不把 re- 理解为回到一模一样的旧结构，重点是重新组织。',OR+[['re- + organization → reorganization','组织结构、安排重新调整']],
 'a company reorganization 公司重组，a reorganization of the department 部门重新安排。',
 'a company reorganization；a reorganization of；undergo reorganization。',
 'reorganization 重组，不自动等于裁员、合并或破产；具体变化需看后文。disorganization 则是混乱失序。',
 ('The reorganization brought three small teams together.','重组把三个小团队整合到一起。'),('The library’s reorganization made the books easier to find.','图书馆重新整理后，书更容易找了。'))
W('disorganization','英 /dɪsˌɔːɡənaɪˈzeɪʃən/；美 /dɪsˌɔːrɡənəˈzeɪʃən/','无组织、混乱；安排失序',
 '不是没有注册一个组织，而是该有的次序、协调散掉了，事情接不上。',
 '与法语 désorganiser、英语 disorganize 等词系相关；现代可按 dis- 破坏、缺少 + organization 认形，也对应 disorganize 的行为、状态名词。不要仅凭现代短长词判断借入先后。',OR+[['dis- 与组织词系 → disorganization','有序结构被破坏或缺少安排的状态']],
 'widespread disorganization 大面积安排混乱，disorganization in the office 办公室工作失序。通常不可数。',
 'widespread disorganization；disorganization in；a state of disorganization。',
 'disorganization 缺乏有序安排，reorganization 是重新安排的过程；重组可能有秩序，也可能暂时造成混乱，两者不等同。',
 ('The delay was caused by disorganization rather than a lack of effort.','延误源于安排混乱，并非大家不努力。'),('The office was in a state of complete disorganization.','办公室工作处于完全失序的状态。'),sources=['https://www.etymonline.com/word/disorganization','https://en.wiktionary.org/wiki/disorganization#English'])
R('B3919','有序组织、重新安排与失序','ORGANIZATION：排成可运作整体；re- 重排，dis- 失序','已有 organization、organizational 后，连续比较 reorganization 和 disorganization。',
 '不要从两个都有长后缀就当同义：一个说重排过程，一个说缺协调、次序的状态。具体历史存在法语、英语同族关系，现代拆分不强定先后。',
 're-/dis- + organization；与 reorganize、disorganize 的名词对应；organization + -al。',
 [['组织与性质','organization · organizational'],['重组和失序','reorganization · disorganization']],
 'reorganization 不自动等于裁员；disorganization 不是单纯未注册组织；重新安排也可有秩序地进行。',
 'The reorganization reduced disorganization in the department.\n\n重新安排减少了部门里的混乱。',
 'organization organizational reorganization disorganization')
if __name__=='__main__':save('continuation_20261030_bf',ROOTS,WORDS)
