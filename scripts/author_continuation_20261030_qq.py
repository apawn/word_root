"""-ware from goods to software; core contemporary computing and pottery words."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
W('firmware','英 /ˈfɜːmweə/；美 /ˈfɜːrmwer/','固件；设备基础控制程序',
 '路由器、相机等设备里，负责让硬件按设计运转的一层基础程序，常叫 firmware。它属于程序，又比随手安装的普通应用更贴近设备。',
 'firm 稳固的 + 从 software 等借来的 -ware，二十世纪形成，命名上居于 hardware 硬件和 software 软件之间。这里 firm 不是公司。',
 [['hardware、software 的命名对照','硬件与软件的词形材料'],['firm + -ware → firmware','与设备硬件紧密相关的基础控制程序']],
 'a firmware update 固件更新；router firmware 路由器固件。早期常与只读存储器相联，现代许多固件可以更新，不可把“固”误解成永远不能改。',
 'a firmware update；camera firmware。','firmware 是程序，hardware 是实体部件；更换固件通常不是把相机里的电路板换掉，也不是所有应用都叫 firmware。',
 ('The camera received a firmware update.','相机收到了一个固件更新。'),('The new firmware fixed a problem with the display.','新固件修复了显示方面的一个问题。'),sources=['https://www.etymonline.com/word/firmware','https://en.wiktionary.org/wiki/firmware#English'])
W('ransom','/ˈrænsəm/','赎金；付赎金赎回',
 '有人或东西被扣着，对方要求交钱才放回，这笔钱是 ransom；动词就是付出相应代价赎回。',
 '经中古英语 raunsoun 接古法语 raençon，来自拉丁 redemptio 赎回的材料，与 redemption 同源。不是 random 随机少一个字母的近义词。',
 [['拉丁 redemptio → 古法语 raençon','赎回、赎金的词族'],['中古英语 raunsoun → ransom','赎金；赎回']],
 'demand a ransom 索要赎金；hold someone for ransom 绑架索赎；pay a ransom 支付赎金。也可比喻某方拿关键资源要挟别人。',
 'a ransom demand；hold for ransom。','ransom 围绕扣押、勒索的赎回要求，fee 是费用；ransom 不是普通服务的收费。',
 ('The kidnappers demanded a ransom.','绑架者索要赎金。'),('The novel follows a family trying to ransom a captive.','小说讲述一家人试图赎回被扣押者的故事。'))
W('ransomware','英 /ˈrænsəmweə/；美 /ˈrænsəmwer/','勒索软件',
 '恶意程序把文件或系统控制住，让受害者无法正常使用，再要求交钱；这像把数据扣做人质，所以叫 ransomware。',
 'ransom 赎金 + 从 software 延伸的 -ware。这里不是一款帮你管理赎金的正常财务软件，而是以勒索为目的的恶意软件类别。',
 [['ransom','扣押后要求支付的赎金'],['ransom + -ware → ransomware','用控制、加密等手段索要赎金的软件']],
 'a ransomware attack 勒索软件攻击；ransomware can encrypt files 勒索软件可加密文件。也可能涉及窃取信息、威胁公开等，不能把所有案例锁定为一种技术过程。',
 'a ransomware attack；ransomware protection。','malware 恶意软件是大类，ransomware 是其中以勒索为核心的一类；spyware 侧重窃探，不等于一定索取赎金。',
 ('The company reported a ransomware attack.','公司报告遭遇了勒索软件攻击。'),('The training explains how ransomware can disrupt everyday work.','培训说明勒索软件怎样扰乱日常工作。'),sources=['https://www.microsoft.com/en-us/security/business/security-101/what-is-ransomware','https://en.wiktionary.org/wiki/ransomware#English'])
W('adware','英 /ˈædweə/；美 /ˈædwer/','广告软件；显示广告的程序',
 '程序运行时给你显示广告，这个广告相关的软件类别可叫 adware；是否令人讨厌、是否越界，还要看实际行为。',
 'ad 在这里缩自 advertisement 广告 + -ware 软件类词尾。ad 还有别的缩略、拉丁材料，解释这个词时不能拿“朝向”的前缀义来硬套。',
 [['advertisement → ad','广告的缩略形式'],['ad + -ware → adware','与显示广告有关的软件']],
 'adware displays advertisements 广告软件显示广告；unwanted adware 不需要的广告软件。有的与免费软件的广告支持模式有关，有的会带来侵扰，须看软件做了什么。',
 'unwanted adware；remove adware。','adware 以广告为特征，不自动等于所有 spyware 窃探软件；若同时追踪、窃取信息，就还涉及其他行为分类。',
 ('The scan detected unwanted adware.','扫描检测到了不需要的广告软件。'),('The article explains the difference between adware and spyware.','文章解释了广告软件与间谍软件的区别。'),sources=['https://en.wiktionary.org/wiki/adware#English'])
W('earthenware','英 /ˈɜːθənweə/；美 /ˈɜːrθənwer/','陶器；陶制品',
 '泥土做坯、烧成能盛东西的碗罐，是最容易认出的 earthenware 画面。不是把地球当商品卖。',
 'earth 土 → earthen 土制的 + ware 制品；中间 -en 表材料这一层不要漏。英语早已有这种按材料给器物分类的构词。',
 [['earth + -en → earthen','土 → 土制的'],['earthen + ware → earthenware','陶制器物']],
 'an earthenware bowl 陶碗；earthenware pots 陶罐。作为材料、制品类别通常不可数，单件说 a piece of earthenware 或用 bowl、pot。',
 'an earthenware pot；glazed earthenware。','earthenware 陶器与 porcelain 瓷器、stoneware 炻器在专业陶瓷分类里有区别；日常都像碗罐，不能因此视为完全同一材料。',
 ('She served the soup in an earthenware bowl.','她用一个陶碗盛汤。'),('The market sells handmade earthenware.','市场卖手工陶器。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/earthenware'])
R('A1894','器物、制品；现代软件类别命名材料',
 'WARE：一类做出来、拿来用的东西；后来也给软件类别起名',
 'glassware 是玻璃器皿，tableware 是餐具；到了计算机，hardware 是硬件，software 是软件，firmware 又用 firm 命名贴近硬件的一层程序。',
 'ware 本是古英语商品、制品的本族名词，独立常用复数 wares。合词可按材料、用途命名，如 earthenware、cookware；现代软件相关的 -ware 是沿 hardware／software 命名模式扩展，不能每个新词都再按实物商品逐字译。',
 'earth + -en + ware，先有 earthen 土制的；ransom + -ware 是以赎金勒索为特征；ad + -ware 取 advertisement 的缩略。firmware 的 firm 是稳固、较固定的形容材料，不是公司。software、hardware 通常整体不可数，不写 two softwares 表两款软件。',
 [['器物按材料命名','glassware · silverware · stoneware；earth · earthen · earthenware'],['器物按用途命名','tableware · dinnerware · cookware · kitchenware · homeware'],['计算机基础类别','hardware · software · firm · firmware · middleware'],['用途、分发模式与风险类别','freeware · shareware；malware · spyware · ransom · ransomware；ad · adware']],
 'firmware 程序／hardware 实体部件；ransomware 是恶意软件中的勒索类别；adware 与 spyware 特征不同，可能重叠；earthenware 陶器不等于所有陶瓷材料都一样。',
 'The update changes the firmware, while the hardware remains the same.\n\n这次更新改变的是固件，硬件还是原来的硬件。',
 'ware glass glassware silver silverware stone stoneware earth earthen earthenware table tableware dinner dinnerware cook cookware kitchen kitchenware home homeware hard hardware soft software firm firmware middle middleware free freeware share shareware malware spy spyware ransom ransomware ad adware')
if __name__=='__main__':save('continuation_20261030_qq',ROOTS,WORDS)
