"""Paper and issue: materials, media, problems and acts of issuing."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
PA=[['希腊 pápyros → 拉丁 papȳrus → 欧洲语言 paper 形式','纸莎草及其书写材料名称'],['法语等形式 → 中古英语 paper → paper','纸张 → 报纸、论文、文件等按用途发展的名词']]
W('paper','英 /ˈpeɪpə/；美 /ˈpeɪpər/','纸；报纸；论文；试卷；文件',
 '纸是材料，写在上面的报道、论文、试卷又借材料名字成为一种内容、文件。',
 '经法语等中介形式接拉丁 papȳrus、希腊 pápyros，原关联纸莎草书写材料。词名来路不等于现代纸与古纸莎草片采用同一种制造工艺。',PA,
 'some paper 一些纸，a piece of paper 一张纸；a research paper 一篇论文，the morning paper 晨报，exam papers 试卷。paper 作动词也可贴纸、贴墙纸。',
 'a piece of paper；a research paper；exam papers；on paper。',
 '材料 paper 常不可数，一张纸说 a sheet/piece of paper；a paper 可是论文、报纸等可数作品。on paper 还常说理论上、按文件看来。',
 ('Please write your name on a piece of paper.','请在一张纸上写下名字。'),('She presented a paper on language learning.','她提交并介绍了一篇关于语言学习的论文。'))
W('paperboard','英 /ˈpeɪpəbɔːd/；美 /ˈpeɪpərbɔːrd/','纸板',
 '把纸做得更挺、更能保持形状，用来做盒子、包装等；仍然是纸质材料这一类。',
 'paper 纸 + board 板，形成挺括纸板材料名。与 cardboard 有范围交叠，工业细分类要按具体材料，而不是一个词永远厚、另一个永远薄。',C('paper 纸','board 板','paperboard','较挺括、用于包装等的纸板'),
 'paperboard packaging 纸板包装，a paperboard carton 纸板盒；材料通常不可数。',
 'paperboard packaging；a paperboard carton；recycled paperboard。',
 'paperboard 纸板材料，clipboard 夹纸书写板是成品器具；cardboard 与 paperboard 在日常、工业语境有交叠。',
 ('The box is made from recycled paperboard.','盒子由再生纸板制成。'),('The company changed to lighter paperboard packaging.','公司改用了更轻的纸板包装。'))
W('papery','英 /ˈpeɪpəri/；美 /ˈpeɪpəri/','像纸的；薄干、纸质般的',
 '摸着、看着或听着像干纸：薄薄的，干燥，可能会沙沙响。',
 'paper + -y 带……质感，形成形容词。不是 paper 的复数，也不一定表示真正用纸做。',PA+[['paper + -y → papery','纸 → 具有薄、干等纸般质感的']],
 'papery leaves 纸般干薄的叶子，papery skin 纸般薄干的皮肤；a papery rustle 纸张般沙沙声。',
 'papery leaves；papery skin；a papery texture。',
 'papery 像纸的质地，paper 作名词前修饰可能真是纸制；a papery leaf 仍可以是天然植物叶片。',
 ('The dry leaves made a papery sound underfoot.','干叶在脚下发出纸张般的沙沙声。'),('The flower has thin, papery petals.','这朵花的花瓣薄得像纸。'))
W('paperless','英 /ˈpeɪpələs/；美 /ˈpeɪpərləs/','无纸化的；不用纸张记录、传递的',
 '原来印出来、签在纸上、塞进文件夹，现在改用电子记录和流程。',
 'paper 纸 + -less 没有、不用，形成现代无纸化用法；通常是指定业务减少、取消纸张，不必整个场所一张纸也不存在。',PA+[['paper + -less → paperless','纸张 → 不用纸张、无纸化的']],
 'paperless billing 电子账单，a paperless office 无纸化办公；go paperless 转用电子流程。',
 'go paperless；paperless billing；a paperless office。',
 'paperless 不用纸，papery 像纸；电子表单仍可能需要填写、审批，不等于取消所有 paperwork 文书工作。',
 ('The company introduced paperless billing.','公司推出了电子账单。'),('We are trying to make the application process paperless.','我们正在尝试把申请流程改为无纸化。'))
W('wallpaper','英 /ˈwɔːlpeɪpə/；美 /ˈwɔːlpeɪpər/','墙纸；屏幕壁纸；贴墙纸',
 '墙上大面积铺开的装饰层；电脑、手机后面的背景图也像给屏幕贴了一层装饰。',
 'wall 墙 + paper 纸，先是墙面装饰材料，再用于数字背景；也可作动词贴墙纸。现代墙面材料未必只是传统纸质。',C('wall 墙','paper 纸','wallpaper','墙面装饰纸材 → 数字屏幕背景图'),
 'floral wallpaper 花卉墙纸，desktop wallpaper 桌面壁纸；wallpaper a room 给房间贴墙纸。',
 'floral wallpaper；desktop wallpaper；change the wallpaper。',
 'wallpaper 屏幕背景图，screensaver 屏幕保护程序通常在闲置时出现；两者可以用相同图片但用途不同。',
 ('They chose pale green wallpaper for the bedroom.','他们为卧室选了浅绿色墙纸。'),('She changed her phone’s wallpaper to a family photo.','她把手机壁纸换成了一张全家福。'))
W('sandpaper','英 /ˈsændpeɪpə/；美 /ˈsændpeɪpər/','砂纸；用砂纸打磨',
 '纸面上附着粗糙颗粒，来回摩擦就能把木头等表面磨平、磨光。',
 'sand 砂 + paper 纸，按早期材料、功能命名；现代磨料也可用其他材料，不要求都是普通沙粒。',C('sand 砂、磨粒','paper 纸','sandpaper','附磨料的打磨纸材；相应打磨动作'),
 'fine sandpaper 细砂纸，coarse sandpaper 粗砂纸；sandpaper the surface 用砂纸磨表面。',
 'fine sandpaper；coarse sandpaper；smooth with sandpaper。',
 'sandpaper 是打磨材料，wallpaper 是装饰材料；都带 paper，功能却相反，不能拿后者的纸面替代磨料。',
 ('He smoothed the wooden edge with sandpaper.','他用砂纸磨平了木边。'),('The workshop keeps several grades of sandpaper.','工坊备有几种粗细等级的砂纸。'))
W('paperweight','英 /ˈpeɪpəweɪt/；美 /ˈpeɪpərweɪt/','镇纸；压纸重物',
 '桌上纸张容易被风吹散，用个重物压住；那个压纸物就是 paperweight。',
 'paper 纸 + weight 重物，按用途复合成名词。不是纸张每平方米的重量，后者另用 paper weight 等语境描述。',C('paper 纸','weight 重物','paperweight','压住纸张的重物、镇纸'),
 'a glass paperweight 玻璃镇纸，an ornamental paperweight 装饰性镇纸；石头临时拿来压纸，也可起这个作用。',
 'a glass paperweight；an ornamental paperweight；use as a paperweight。',
 'paperweight 是一个物件；weight of the paper 是纸本身重量。还可调侃坏设备成了镇纸，意思是失去原来用途。',
 ('A glass paperweight held the letters in place.','一个玻璃镇纸压住了信件。'),('She used a smooth stone as a paperweight.','她用一块光滑石头作镇纸。'))
R('B3199','纸张；报纸、论文和各种纸相关用品','PAPER：先是材料，再由材料指内容和用途','some paper 是材料，a paper 可以是论文或报纸；纸板、墙纸、砂纸、镇纸按功能分清，无纸化再看流程变化。',
 'paper 经法语等接希腊、拉丁纸莎草名称。词名沿用不代表古今材料工艺相同；papery 像纸、paperless 不用纸是一对很容易混的性质词。',
 'paper → paperboard、papery、paperless；wallpaper 装饰、sandpaper 打磨、paperweight 压纸；报刊、文书和制造词集中作另一组。',
 [['材料及质地','paper · paperboard · papery · papermaking'],['减少纸张及文书','paperless · paperwork'],['墙面、打磨和压纸用品','wallpaper · sandpaper · paperweight'],['出版及投递','newspaper · paperback · paperboy']],
 'paper 材料不可数，a paper 可是论文；paperless 不等于没有文书工作；paperweight 是物件，不是纸重。',
 'The paperless office still had wallpaper and a decorative paperweight.\n\n这间无纸化办公室里，仍有墙纸和装饰镇纸。',
 'paper paperboard papery papermaking paperless paperwork wallpaper sandpaper paperweight newspaper paperback paperboy')
IS=[['拉丁 exīre → 法语 issir、issue → 英语 issue','向外走、流出、出口；后有结果等义'],['英语 issue 的不同分支','发出、签发及发行物；争讼待定点发展成议题、问题']]
W('issue','/ˈɪʃuː/；英式也 /ˈɪsjuː/','议题；问题；一期刊物；签发、发布、发放',
 '会议上是大家要处理的一件事；杂志架上是一期刊物；机构做动作时则是把文件、物品正式发出去。',
 '经法语来自拉丁 exīre，ex- 向外 + īre 走。发出、发行较易连到向外；议题义则有诉讼中待裁定争点等历史，不把今天所有问题都直译出口。',IS,
 'a key issue 关键议题，an issue with the printer 打印机的问题；the latest issue of a magazine 最新一期杂志；issue a warning 发布警告，issue passports 签发护照。',
 'a key issue；the latest issue；issue a statement；take issue with。',
 'issue 可中性说待讨论事项，不一定是故障；take issue with 反对、不认同，不是从对方手里拿走一本杂志。',
 ('We need to discuss the main issue first.','我们得先讨论主要问题。'),('The next issue of the magazine comes out on Monday.','杂志下一期周一出版。'),('The office issued a statement that afternoon.','办公室当天下午发布了一份声明。'),sources=['https://en.wiktionary.org/wiki/issue#English','https://www.etymonline.com/word/issue'])
W('issuance','/ˈɪʃuːəns/；亦 /ˈɪʃjuəns/','签发；发行；正式发放〔书面〕',
 '不讲谁拿到手，而是把文件、证券、许可等正式发出去这一动作。',
 'issue 发出、签发 + -ance 成动作名词，去末尾 e。较正式，常在机构、行政、金融文件出现。',IS+[['issue + -ance → issuance','签发、发行 → 相应动作、过程名词']],
 'the issuance of a permit 许可证签发，bond issuance 债券发行；日常口语许多时候直接用 issuing 更自然。',
 'the issuance of；permit issuance；bond issuance。',
 'issuance 是动作，issuer 是执行者；不是每个 issue 议题都变成 issuance，后者主要取发出、发行分支。',
 ('The office confirmed the issuance of the new permit.','办公室确认了新许可证已经签发。'),('The report describes the process of bond issuance.','报告介绍了债券发行过程。'))
W('issuer','英 /ˈɪʃuːə/；美 /ˈɪʃuːər/','发行者；签发机构、发卡机构',
 '文件、卡、证券是谁正式发出来的，就把那个主体叫 issuer。',
 'issue 发出、发行 + -er 执行者，去 e。主体常是机构，不因 -er 就必须是某个自然人。',IS+[['issue + -er → issuer','发出、签发 → 发行、签发主体']],
 'a card issuer 发卡机构，a bond issuer 债券发行人、发行机构；the issuer of a certificate 证书签发者。',
 'a card issuer；a bond issuer；the issuer of the certificate。',
 'issuer 发出的主体，holder 持有人，recipient 接收者；持卡人不是发卡机构。',
 ('Contact the card issuer if the card is lost.','卡遗失时，请联系发卡机构。'),('The document names the issuer of the certificate.','文件写明了证书签发者。'))
W('reissue','/ˌriːˈɪʃuː/；名词也重读 re-','重新发行；重新签发；再版、重发物',
 '以前已经发过，现在再正式发一回，可能是旧作品再版，也可能是证件替换重发。',
 're- 重新 + issue 发出、发行，兼有动词和名词。重发可能改内容、改格式，也可能仅重新提供，不由前缀保证一定修订。',IS+[['re- + issue → reissue','发行、签发 → 再次发行、签发；重发版本']],
 'reissue an album 重新发行专辑，reissue a ticket 重新出票；a reissue of the book 这本书的再版。',
 'reissue an album；reissue a ticket；a reissue of；a reissued edition。',
 'reissue 重新发行、签发，revise 修订，reprint 重印；一份 reissue 是否改过正文要看具体版本。',
 ('The publisher reissued the novel with a new cover.','出版社换了封面，重新发行了这部小说。'),('The airline reissued the ticket after the name was corrected.','姓名改正后，航空公司重新签发了机票。'))
R('B4208','议题、问题、一期刊物；签发与发布','ISSUE：现代场景先分，词源再接向外发出','a key issue 是议题，the latest issue 是最新一期；issue a warning 是发布，issuer 和 issuance 只从发出这支继续扩展。',
 'issue 经法语接拉丁向外走、流出词族；议题分支由争讼待定点等历史展开。不要为一个中文问题忽略出版、行政这些高频场景。',
 'issue → issuance 动作、issuer 主体；re- 重新 → reissue。',
 [['基础多义及发行派生','issue · issuance · issuer · reissue']],
 'issue 议题不一定故障；issuance 动作、issuer 主体；reissue 重发不保证修订。',
 'The latest issue explains why the issuer decided to reissue the document.\n\n最新一期说明了签发机构为什么决定重新签发文件。',
 'issue issuance issuer reissue')
for item in WORDS:
    if item['word']=='paper':item['sources'].append('https://www.etymonline.com/word/paper')
if __name__=='__main__':save('continuation_20261029_dg',ROOTS,WORDS)
