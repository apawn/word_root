"""Chemical groups, presumably, lime and anchor."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
Y=[['希腊 hylē','材料、物质'],['化学命名采用 -yl','形成许多基团名称；各名称所指结构不同']]
W('ethyl','英 /ˈeθaɪl/、/ˈeθɪl/；美 /ˈeθəl/','乙基，C₂H₅—',
 '把分子当积木搭建，ethyl 是两个碳组成的一块连接件。写成 C₂H₅—，末尾横线标它还能与别的部分连接。',
 '借德语 Ethyl，由 Ether 的截段与 -yl 构成。现代命名中可把 ethane 乙烷少一个氢所得的基团认作 ethyl，但历史命名从 ether 来。',Y+[['德语 Ether + -yl → Ethyl → ethyl','乙基；现代结构写作 C₂H₅—']],
 'an ethyl group 乙基；ethyl alcohol 是乙醇的传统名称，结构为 C₂H₅OH。重点看乙基是其中一部分。',
 'an ethyl group；ethyl alcohol。',
 'ethyl 是基团名称，不独立等于一杯酒；术语中的基团也不自动等于带未成对电子的游离自由基。',
 ('The molecule contains an ethyl group.','这个分子含有一个乙基。'),('Ethyl alcohol is another name for ethanol.','ethyl alcohol 是乙醇的另一名称。'),sources=['https://en.wiktionary.org/wiki/ethyl#English','https://www.etymonline.com/word/ethyl','https://www.affixes.org/-yl.html'])
W('acetyl','英 /əˈsiːtaɪl/；美 /ˈæsətɪl/','乙酰基，CH₃C(=O)—',
 '先看一小块碳氧结构：CH₃ 后接一个碳，这个碳与氧双键相连，还留着和别处连接的位置。整块叫 acetyl。',
 'acet- 联系 acetic acid 乙酸一族，词源通向拉丁 acētum 醋；加 -yl 形成基团名。可从乙酸 CH₃COOH 在形式上去掉羟基来认结构，并非这里只教实际反应步骤。',Y+[['acet- 乙酸词族 + -yl','CH₃C(=O)—，乙酰基']],
 'an acetyl group 乙酰基；描述分子、蛋白质等的结构变化时常见。CH₃CO— 是它的简写。',
 'an acetyl group；carry an acetyl group。',
 'acetyl 与 ethyl 相差一个含氧结构：乙基 C₂H₅—，乙酰基 CH₃CO—。英文相似，结构不能混成一块。',
 ('The diagram highlights the acetyl group.','图中突出标出了乙酰基。'),('The two compounds differ by an acetyl group.','这两种化合物的结构相差一个乙酰基。'),sources=['https://en.wiktionary.org/wiki/acetyl#English','https://www.affixes.org/-yl.html'])
W('carbonyl','英 /ˈkɑːbənɪl/；美 /ˈkɑːrbənɪl/','羰基，C=O；金属羰基化合物',
 '认出碳和氧之间这条双键 C=O，就认出了常说的 carbonyl group。它像一个很醒目的局部结构，出现在许多不同分子里。',
 'carbon 碳 + -yl，形成化学名称。羰基义指 C=O；金属羰基化合物中则是一氧化碳作为配体，需看完整搭配。',Y+[['carbon + -yl → carbonyl','C=O 羰基；另有金属羰基化合物用法']],
 'a carbonyl group 羰基，carbonyl compounds 羰基化合物。醛、酮含羰基，羧酸及其多种衍生物也含这一结构。',
 'a carbonyl group；carbonyl compounds。',
 '羰基 C=O 不等于羟基 —OH；metal carbonyl 也不能只按普通有机羰基结构理解。',
 ('Both aldehydes and ketones contain a carbonyl group.','醛和酮都含有羰基。'),('The carbonyl group is marked in blue in the diagram.','图中的羰基用蓝色标出。'),sources=['https://en.wiktionary.org/wiki/carbonyl#English','https://goldbook.iupac.org/terms/view/C00844'])
W('phenyl','英 /ˈfiːnaɪl/；美 /ˈfenəl/','苯基，C₆H₅—',
 '想象一个苯环，形式上拿掉一个氢，留下一个与其他部分相连的位置，这个环状连接件就是 phenyl。',
 '借法语 phényle，phen- 的历史联系希腊 phaínō 发光及早期相关化学命名，后接材料、基团命名成分 -yl；现代用于苯基。',Y+[['法语 phényle → phenyl','以 C₆H₅— 表示的苯基']],
 'a phenyl group 苯基，two phenyl groups 两个苯基。读名称时先定位这个环状结构，不必把古代发光的词源当成现代化学性质。',
 'a phenyl group；a phenyl ring。',
 'phenyl 苯基 C₆H₅— 与 benzyl 苄基 C₆H₅CH₂— 不同，后者多出 CH₂ 这一段。',
 ('The molecule has two phenyl groups.','这个分子有两个苯基。'),('The drawing shows a phenyl group attached to the main chain.','图中有一个苯基连在主链上。'),sources=['https://en.wiktionary.org/wiki/phenyl#English','https://www.etymonline.com/word/phenyl','https://www.affixes.org/-yl.html'])
R('A2101','化学基团的命名形式，具体结构由整个名称决定','-YL：把分子中的一块结构单独认出来','ethyl、acetyl、carbonyl、phenyl 与 alkyl、hydroxyl、vinyl 对照。',
 '这里先认日常科普、基础化学中较常碰见的名称。基团像分子积木，-yl 提醒你看结构，前面的材料和命名历史帮助区分是哪一块。',
 '-yl 源自希腊 hylē 材料、物质；ethyl 乙基，acetyl 乙酰基，carbonyl 羰基，phenyl 苯基，各有不同结构。',
 [['烃基总称与具体结构','alkyl · ethyl · vinyl · phenyl'],['含氧结构','hydroxyl · carbonyl · acetyl']],
 '传统术语 radical 可能指基团，不能一律理解为游离自由基；羰基 C=O 与羟基 —OH 分清。',
 'The diagram distinguishes an ethyl group from a carbonyl group.\n\n图中区分了乙基和羰基。','alkyl ethyl vinyl phenyl hydroxyl carbonyl acetyl')
Pr=[['presume → presumable','认为大概如此 → 可以合理推测的'],['presumable + -ly → presumably','大概、想必；按目前情况推想']]
W('presumably','英 /prɪˈzjuːməbli/；美 /prɪˈzuːməbli/','想必、大概、据推测',
 '门口鞋子不在，人也没应声：你推想他大概出去了。presumably 给出的就是这种有根据、但尚未直接确认的判断。',
 'presumable + -ly；-able 接 -ly 时变为 -ably。底层 presume 表先作推定，presumable 是可合理推想的。',Pr,
 'Presumably, ... 可以放句首，也能放句中。语气通常是根据情况想必如此，事实仍可能另有解释。',
 'Presumably, ...；will presumably ...。',
 'presumably 与 probably 意思接近，前者更容易突出这是说话者按情况作的推想；两者都不是百分之百保证。',
 ('The lights are off, so presumably everyone has gone home.','灯都关了，想必大家已经回家了。'),('She will presumably contact us when she arrives.','她到了之后大概会联系我们。'),sources=['https://en.wiktionary.org/wiki/presumably#English','https://www.etymonline.com/word/presumably','https://dictionary.cambridge.org/us/dictionary/english/presumably'])
R('A1679','-able 形容词构成副词时常见的 -ably 形式','-ABLY：把某种性质变成做事方式，或对整句话的判断','presumable → presumably；undeniable → undeniably；unquestionable → unquestionably。',
 '看清 -able 与 -ly 的衔接，再学每个整词的实际语气。presumably 只是合理推想，undeniably、unquestionably 则常把肯定程度推高。',
 '-able + -ly → -ably；presume → presumable → presumably。',
 [['合理推测','presumably'],['强调难以否认、没有疑问','undeniably · unquestionably']],
 '不是所有 -ably 都说能够做某事；副词意义取决于底层形容词和整句话。',
 'Presumably the plan will work, but its cost is undeniably high.\n\n这个计划想必行得通，但费用之高无可否认。','presumably undeniably unquestionably')
Li=[['古英语 līm → lime','黏性材料、灰浆 → 石灰'],['波斯、阿拉伯语的柑橘名称，经欧洲语言 → lime','青柠；再扩展到相应颜色'],['古英语 lind → lynde、line → lime','椴树；与青柠树是不同树木']]
W('lime','/laɪm/','青柠；石灰；椴树；青柠绿',
 '杯边那片酸酸的青柠、建筑里说的石灰、英国街道旁的椴树，都可能写 lime。它们来自不同历史，先看场景再选意思。',
 '石灰义承古英语 līm 黏性材料、灰浆；青柠名称经欧洲语言联系阿拉伯、波斯柑橘词，具体借入路线有讨论；椴树义是 lind、line 一族的后起变形。',Li,
 'lime juice 青柠汁，a slice of lime 一片青柠，lime mortar 石灰砂浆，a lime tree 在英国也常指椴树。颜色 lime 联系青柠的鲜绿。',
 'lime juice；lime mortar；a lime tree。',
 'limestone、limelight 的 lime 属石灰这一路；看见 lime tree 不能在所有地区和场景里都认作结青柠的树。',
 ('She squeezed some lime juice into the dressing.','她往调味汁里挤了些青柠汁。'),('The old wall was built with lime mortar.','那堵旧墙使用石灰砂浆砌成。'),('A row of lime trees shaded the avenue.','一排椴树为林荫道遮阴。'),sources=['https://en.wiktionary.org/wiki/lime#English','https://www.etymonline.com/word/lime'])
R('B4596','青柠、石灰、椴树三路同形词','LIME：先认场景，再沿各自词源去理解','lime 的青柠一路；石灰一路连接 limestone、limelight；椴树另有来源。',
 '一个拼写可以容纳不同来源。石灰灯曾用灼热石灰发强光，limelight 因此又能指公众注意；它与青柠汁没有这条演变关系。',
 '石灰承古英语 līm；青柠名经欧洲语言联系阿拉伯、波斯语；椴树名由 lind 一族变形。',
 [['青柠及同形的其他名称','lime'],['石灰材料与灯光比喻','limestone · limelight']],
 'limelight 的名气、关注义从舞台灯光发展；椴树与青柠树分清。',
 'The limestone wall stood beside a row of lime trees.\n\n石灰岩墙立在一排椴树旁。','lime limestone limelight')
An=[['希腊 ánkyra、拉丁 ancora','船锚名称'],['古英语 ancor → 中古英语 anker → anchor','固定船只的器具；现代 ch 受拉丁拼写影响'],['固定船只 → 固定、稳定的比喻','再扩展到新闻主播、锚点等']]
W('anchor','英 /ˈæŋkə/；美 /ˈæŋkər/','锚；固定、使稳住；新闻主播',
 '船不想随水漂走，就让锚抓住底部。能让东西、生活或节目稳住中心的人和物，也可以借用 anchor 这个画面。',
 '名词经古英语 ancor、中古英语 anker 接拉丁 ancora，与希腊 ánkyra 相连；现代拼写 ch 受历史拉丁形式影响，读 /k/。动词沿相关名词、旧动词形式发展。',An,
 'drop anchor 抛锚，anchor a boat 固定船，be anchored in experience 扎根于经验，a news anchor 新闻主播。',
 'drop anchor；be anchored in；a news anchor。',
 'anchor 的 ch 读 /k/；新闻主播义是稳定、主持全局的比喻，并不只指任何在镜头前出现的人。',
 ('The boat dropped anchor in the bay.','船在海湾里抛了锚。'),('Her daily routine helped anchor her during a difficult year.','那一年很艰难，日常规律帮助她稳住了生活。'))
W('anchorage','英 /ˈæŋkərɪdʒ/；美 /ˈæŋkərɪdʒ/','锚地；锚定、固定处；抛锚费',
 'anchor 是锚，anchorage 常是能让船停下来抛锚的水域；讨论结构时，也可以是用来牢牢固定的部位。',
 'anchor + -age，形成地点、状态、费用等相关名词；具体是哪一种，要由航海或工程搭配判断。',An[:2]+[['anchor + -age → anchorage','抛锚处、锚定状态、相关费用']],
 'a sheltered anchorage 避风锚地，a secure anchorage 可靠固定处；地名 Anchorage 另按专名识别。',
 'a sheltered anchorage；a secure anchorage。',
 '-age 在本词里不表示年龄；anchorage 与 harbour 范围有重合，但锚地突出可供抛锚停泊的水域。',
 ('The bay provided a sheltered anchorage for small boats.','海湾为小船提供了避风锚地。'),('The cable requires a secure anchorage.','这根缆索需要可靠的固定处。'))
W('anchoring','英 /ˈæŋkərɪŋ/；美 /ˈæŋkərɪŋ/','抛锚、锚定；锚定效应；anchor 的 -ing 形式',
 '把东西固定住是 anchoring；思考时最先听到的数字，也可能像锚一样拉住后续判断，这就是常说的锚定效应。',
 'anchor + -ing，动作名词、分词。认知用法把判断受初始信息牵引比喻成锚定。',An+[['anchor + -ing → anchoring','固定动作 → 初始信息牵引判断的比喻']],
 'anchoring a boat 给船抛锚，anchoring bias 锚定偏差，an anchoring effect 锚定效应；说的是先入信息影响后续估计。',
 'anchoring a boat；anchoring bias。',
 'anchoring 可能是正常固定动作，也可能是认知术语；不是每次使用最初信息都必然构成偏差。',
 ('Anchoring the boat took longer than expected.','给船抛锚花的时间比预计长。'),('The first estimate influenced later guesses through anchoring.','第一次估计通过锚定效应影响了后面的猜测。'))
R('B3024','锚抓住固定点，再扩展为稳定、主持和判断的锚定','ANCHOR：抓住一个点，就不再任意漂移','anchor → anchorage、anchoring；anchorman 是主持、稳住节目的角色。',
 '从船锚出发理解固定，再看可抛锚的地方、固定动作，以及第一条信息拉住判断的比喻。',
 '古英语 ancor、中古英语 anker 接拉丁 ancora；现代 anchor 的 ch 读 /k/；-age 地点等，-ing 动作。',
 [['固定物、固定处与动作','anchor · anchorage · anchoring'],['主持角色','anchorman']],
 'anchorage 可水域或固定处；anchoring bias 是判断受初始信息过度牵引。',
 'The anchor held the boat securely in the sheltered anchorage.\n\n锚把船稳稳固定在避风锚地里。','anchor anchorage anchoring anchorman')
if __name__=='__main__':save('continuation_20261030_ly',ROOTS,WORDS)
