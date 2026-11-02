"""Tech, blame, yellow, fill and connected: useful modern families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['希腊 tékhnē 等技艺词族 → technology、technical 等','技艺、技术'],['英语长词截短 → tech','technology、technician 等的口语简称'],['tech + -ie/-y','懂技术的人；技术味较重的']]
W('techie','/ˈteki/','技术人员、技术爱好者〔口语〕',
 '修电脑、做程序、爱折腾设备的人，口语里可叫 techie；语气随场景，可亲切，也可稍带刻板印象。',
 'tech 技术简称 + 人物后缀 -ie，不是技术学科的正式学位名称。tech 本身由 technology、technician 等长词截短。',T,
 'a computer techie 电脑技术人员，ask a techie 问懂技术的人，a team of techies 一队技术人员。',
 'a computer techie；ask a techie；a team of techies。',
 'techie 人物名词，techy 常形容技术性、懂技术；技术人员的具体职位仍需 technician、engineer 等词说明。',
 ('A techie helped us fix the projector.','一位懂技术的人帮我们修好了投影仪。'),('The event brought artists and techies together.','活动把艺术家和技术人士聚到了一起。'))
W('techy','/ˈteki/','技术性的、技术味重的；懂技术的〔口语〕',
 '一篇说明塞满技术细节，可以说很 techy；一个人很会摆弄设备，也可这样形容。',
 'tech + -y。另有很旧的同拼写形式接 tetchy 易怒，读法也不同；常见科技语境的 techy 按 /ˈteki/ 理解。',T[:2]+[['tech + -y → techy','具有技术性质；懂技术']],
 'techy details 技术细节，a techy person 懂技术的人，too techy for beginners 对初学者太偏技术。',
 'techy details；a techy person；too techy for beginners。',
 'techy 与 techie 常同音，前者常形容性质，后者常指人；正式文体可按意思改用 technical。',
 ('The guide gets rather techy in the final chapter.','指南最后一章变得相当偏技术。'),('My sister is more techy than I am.','我姐姐比我更懂技术。'))
R('B3690','技术长词的口语简称与技术人物','TECH：把长的技术名称缩短，放进日常话里','tech → techie、techy；biotech、cleantech 说明技术所属领域。',
 'tech 是截短，不是把每个含技术的长词都重新拆成 t + ech；techie 和 techy 的人物、性质位置先分清。',
 'tékhnē 等 → technology 等 → tech；tech + -ie/-y；bio-/clean + tech。',
 [['简称、人物和性质','tech · techie · techy'],['技术领域','biotech · cleantech']],
 'techie/techy 人物与形容；biotech 生物技术，cleantech 清洁技术领域。',
 'The techie explained the techy details in simple language.\n\n那位技术人员用简单话解释了技术细节。','tech techie techy biotech cleantech')
B=[['希腊 blasphēmein → 拉丁 blasphemāre 等','恶言、责骂等旧词族'],['古法语 blasmer、blasme → 中古英语 → blame','责备、指责；过错责任'],['现代派生','blaming 归责行为；blameless 无可归咎的']]
W('blame','/bleɪm/','责怪、归咎；责任、过错',
 '坏事发生后，把“是谁造成的”这支箭指向某个人或原因，就是 blame。它在分坏结果的责任，不只是在表达不喜欢。',
 '经古法语 blasmer、blasme 接拉丁、希腊责骂词族。长形式在历史音变里缩短为 blame，不能按现代英语随意拆 bla + me。',B,
 'blame someone for something 因某事责怪某人，blame something on someone 把某事归咎于某人，take the blame 承担责任，be to blame 该负责。',
 'blame someone for；blame something on；take the blame；be to blame。',
 '两个句型换焦点：blame him for the delay / blame the delay on him；be to blame 通常不用被动 blamed。',
 ('Do not blame her for the delay.','别因延误责怪她。'),('The manager took the blame for the mistake.','经理为这次错误承担了责任。'),
 sources=['https://en.wiktionary.org/wiki/blame#English','https://www.etymonline.com/word/blame'])
W('blaming','/ˈbleɪmɪŋ/','责怪、归责的行为；正在责怪',
 '把注意力放在“谁的错”这个动作上；有时反复找人背锅，却还没开始解决问题。',
 'blame 去末尾 e + -ing；中古英语已有对应名词形式。句中既可作过程名词，也可出现在进行时。',B[:2]+[['blame 去 e + -ing → blaming','责怪的行为；责怪动作进行中']],
 'stop blaming 停止责怪，blaming others 责怪别人，a culture of blaming 动辄归责的风气。',
 'stop blaming；blaming others；keep blaming。',
 'blaming 是找过错责任，不等于 explaining an error 分析错误；找原因可以必要，也不必总指责一个人。',
 ('Blaming others will not repair the damage.','责怪别人并不能修复损失。'),('He kept blaming the weather for every problem.','他不断把每个问题都归咎于天气。'))
W('blameless','/ˈbleɪmləs/','无过错的、不该受责备的',
 '在这件事上，责任的箭不该指向他；不等于这个人一辈子从没犯过错。',
 'blame + -less 没有，中古英语已有 blameles 等形式，表示没有应受责备之处。',B[:2]+[['blame + -less → blameless','没有应归咎的过错']],
 'entirely blameless 完全无过错，a blameless person 无过错的人，blameless in this matter 在此事上无过错。',
 'entirely blameless；blameless in this matter；a blameless life。',
 'blameless 无应受责备之处；careless 粗心不是同一后缀结论，-less 要连前面的具体词义理解。',
 ('The investigation found her blameless in the matter.','调查认为她在这件事上没有过错。'),('The driver was not entirely blameless.','司机也并非完全没有责任。'))
R('B3522','把坏结果的责任归给某人、某因','BLAME：责任这支箭指向谁','blame → blaming、blameless，从归责动作到无过错状态。',
 'blame 不只是批评口气，更在说谁该为坏结果负责；blameless 可限于眼前这件事。',
 '希腊责骂词族经拉丁、法语 → blame；blame 去 e + -ing；blame + -less。',
 [['归责及无过错','blame · blaming · blameless']],
 'blame someone for 与 blame something on 换焦点；be to blame 该负责；blameless 不代表一生完美。',
 'Stop blaming her; she was blameless in this matter.\n\n别再责怪她了，她在这件事上没有过错。','blame blaming blameless')
Y=[['古英语 ġeolu、ġeolwe → 中古英语 yelou 等 → yellow','日耳曼语继承的黄色词'],['颜色作动词、构词成分','变黄；略黄；按鳍、尾颜色命名鱼类']]
W('yellow','英 /ˈjeləʊ/；美 /ˈjeloʊ/','黄的、黄色；变黄、使发黄；胆怯的〔贬义口语〕',
 '基础就是黄色；纸放久变黄可作动词。口语说人 yellow 则可能在骂胆小，不能每次都按肤色理解。',
 '接古英语 ġeolu、ġeolwe，经中古英语 yelou 等继承而来。变黄动词也有早期对应形式；不按 yell 大喊 + ow 拆。',Y,
 'yellow flowers 黄花，turn yellow 变黄，yellow with age 年久发黄，yellow journalism 煽情、不负责任的新闻〔固定说法〕。',
 'yellow flowers；turn yellow；yellow with age；yellow journalism。',
 'yellow 颜色，yellowish 略带黄；yellow journalism 不是把报纸印成黄色，yellow 胆怯义带贬意。',
 ('The leaves turned yellow in autumn.','秋天，树叶变黄了。'),('The old pages had yellowed with age.','旧书页随着岁月发黄了。'))
W('yellowish','英 /ˈjeləʊɪʃ/；美 /ˈjeloʊɪʃ/','略黄的、带黄色的',
 '不是很确定、很纯的黄，只是整体透一点黄色；-ish 把颜色说得没那么绝对。',
 'yellow + -ish，表示略带、近似。中古英语已有相应形式，现代构词关系仍清楚。',Y[:1]+[['yellow + -ish → yellowish','略带黄色，不必是纯黄']],
 'a yellowish tint 微黄色调，yellowish light 偏黄的光，yellowish paper 泛黄的纸。',
 'a yellowish tint；yellowish light；yellowish paper。',
 'yellowish 近似黄，不等于黄色之外另一个固定色号；yellowed 常强调已经变黄的结果。',
 ('The lamp gave off a yellowish light.','灯发出微黄的光。'),('The paper had a yellowish tint.','纸带一点黄色。'))
W('yellowfin','英 /ˈjeləʊfɪn/；美 /ˈjeloʊfɪn/','黄鳍金枪鱼〔常见简称〕',
 '菜单、海洋报道里常指黄鳍金枪鱼：名称抓住黄色鳍部这个外观特征，整条鱼并非都黄。',
 'yellow 黄 + fin 鳍；yellowfin tuna 常简称 yellowfin。这里 fin 是鱼鳍，不是词尾 -fine。',Y[:1]+[['yellow + fin → yellowfin〔tuna〕','按黄色鳍部命名的金枪鱼']],
 'yellowfin tuna 黄鳍金枪鱼，a yellowfin steak 黄鳍金枪鱼排，a school of yellowfin 一群黄鳍金枪鱼。',
 'yellowfin tuna；a yellowfin steak；a school of yellowfin。',
 'yellowfin 和 yellowtail 名称都带黄，却不是同一种鱼的两个随意说法；fin 鳍、tail 尾部也不同。',
 ('The menu listed grilled yellowfin tuna.','菜单上有烤黄鳍金枪鱼。'),('The documentary followed a school of yellowfin.','纪录片跟拍了一群黄鳍金枪鱼。'),
 sources=['https://en.wiktionary.org/wiki/yellowfin#English','https://www.fisheries.noaa.gov/species/atlantic-yellowfin-tuna'])
W('yellowtail','英 /ˈjeləʊteɪl/；美 /ˈjeloʊteɪl/','黄尾鱼〔多种鱼的俗名，菜单中常见鰤类〕；黄尾的',
 '抓住黄色尾部来叫动物。菜单里常说鰤类，但这个普通名称在不同地区可指不同鱼，不能只凭单词锁定唯一物种。',
 'yellow 黄 + tail 尾；组合不只说尾巴本身，也可代指长着这种尾巴的整只动物。',Y[:1]+[['yellow + tail → yellowtail','黄尾的 → 有这种特征的鱼等动物名称']],
 'yellowtail sashimi 黄尾鱼刺身，yellowtail snapper 黄尾笛鲷，a yellowtail fillet 黄尾鱼片。',
 'yellowtail sashimi；yellowtail snapper；a yellowtail fillet。',
 'yellowtail 通俗名称可跨多个物种；yellowfin tuna 则是另一种常见鱼名，不把黄尾当黄鳍的缩写。',
 ('The restaurant served yellowtail sashimi.','餐厅供应黄尾鱼刺身。'),('The label gave the full species name after yellowtail.','标签在 yellowtail 后面列出了完整物种名。'))
R('B2573','黄色本身与借颜色命名','YELLOW：先看颜色，再看颜色落在哪个部位','yellow → yellowish；yellowfin、yellowtail 按鳍、尾的外观命名。',
 '鱼名不是把整条鱼涂成黄；通俗名称与严格物种名称也有区别。yellow 的胆怯、新闻固定搭配另看语境。',
 'ġeolu、ġeolwe 经中古英语 → yellow；yellow + -ish；yellow + fin/tail。',
 [['基础颜色与略带黄','yellow · yellowish'],['鱼名的外观特征','yellowfin · yellowtail']],
 'yellow/yellowish 程度不同；yellowfin/yellowtail 不是同鱼随意换名；fin 鳍与 tail 尾部分清。',
 'The yellowish label showed a picture of a yellowfin tuna.\n\n微黄色标签上画着一条黄鳍金枪鱼。','yellow yellowish yellowfin yellowtail')
F=[['日耳曼语 full 词族 → 古英语 fyllan → fill','使满、装满；补足'],['古英语 fyllu → 名词 fill','满的数量、足量；与动词同族并行继承'],['现代扩展','填洞、填表、补位；填充物和再次补充']]
W('fill','/fɪl/','填满、装满；填入、补足、担任；足量、填充材料',
 '空杯子放进水，空格放进信息，空职位安排一个人：共同点是原来有空缺，现在往里面补上东西。',
 '动词接古英语 fyllan，与 full 满同族；常用名词也接古英语 fyllu 的足量、满足词族，并非每个名词义都只由现代动词临时转来。',F,
 'fill a bottle with water 把瓶子装上水，fill in a form / fill out a form 填表，fill a vacancy 填补空缺，eat your fill 吃个够。',
 'fill something with；fill in a form；fill out a form；fill a vacancy；eat your fill。',
 'fill 动作，full 状态：fill the cup / the cup is full；fill in 与 fill out 填表有地区习惯，具体搭配一起学。',
 ('Fill the bottle with clean water.','往瓶子里装入干净的水。'),('The company needs someone to fill the vacancy.','公司需要有人填补这个职位空缺。'))
W('filler','英 /ˈfɪlə/；美 /ˈfɪlər/','填充物；凑数内容；填充词',
 '主要任务是把空的地方占上：修墙的材料、节目之间的过渡内容、说话时的 um，都可能叫 filler。',
 'fill + -er，表示填充的人、工具或材料；常用义多落在材料、内容，不是看见 -er 就只找工人。',F[:1]+[['fill + -er → filler','用来填补空隙、时段等的东西']],
 'wall filler 墙面填料，filler words 填充词，filler material 填充材料，filler content 凑数内容。',
 'wall filler；filler words；filler material；filler content。',
 'filler 可中性材料，也可贬义凑数内容；filling 还常指食物馅料、补牙材料，搭配各有习惯。',
 ('Use filler to repair the small holes in the wall.','用填料修补墙上的小洞。'),('Try to reduce filler words during the presentation.','做演示时尽量减少填充词。'))
W('refill','动词 /ˌriːˈfɪl/；名词 /ˈriːfɪl/','再装满、补充；续杯、补充装',
 '杯子用掉一部分再加，笔芯写完换补充芯，都是把消耗掉的内容补回来。',
 're- 再 + fill；可动词说再填充，也可名词说补充的量、替换装。常见名词与动词重音不同。',F[:1]+[['re- + fill → refill','再装、补充；补充的一份或替换装']],
 'refill a bottle 再装满瓶子，a free refill 免费续杯，a pen refill 替换笔芯，refill the dispenser 给分配器补充。',
 'refill a bottle；a free refill；a pen refill；refill the dispenser。',
 'refill 补充原来的内容，replace 更换对象；refill a bottle 通常不是换一个新瓶子。',
 ('Could you refill my water bottle?','能帮我把水瓶再装满吗？'),('The café offers one free refill.','咖啡馆提供一次免费续杯。'))
W('infill','/ˈɪnfɪl/','填入空隙的材料；填补建设、填充；填入',
 '看一片已有结构里的空档：把墙格填上材料，或在已有城区的空地补建，都可以说 infill。',
 'in 里面 + fill 填；名词、动词都围绕在已有边界、结构之间补进去，不是无限向外扩张。',F[:1]+[['in + fill → infill','已有结构或地区空隙里的填充、补建']],
 'infill development 城区空地补建，infill housing 空地补建住房，infill material 填充材料。',
 'infill development；infill housing；infill material。',
 'infill 强调在已有范围内填空；landfill 常指垃圾填埋或填埋场，backfill 是回填，各看填什么、往哪里填。',
 ('The plan encourages infill housing near the station.','规划鼓励在车站附近的空地补建住房。'),('The frame was strengthened with infill panels.','框架用填充板加固了。'))
R('B3964','把原有空缺补上','FILL：空的地方放进相应的东西','fill → filler；refill 再补，infill 往现有空档补，landfill、backfill 看具体材料和方向。',
 '从杯子、墙洞到信息栏、职位空缺，都保留空处得到补足的画面。full 状态与 fill 动作搭配理解。',
 'full 词族 → 古英语 fyllan/fyllu → fill；fill + -er；re-/in-/back-/land + fill。',
 [['基础与填充物','fill · filler'],['再补、补进与回填','refill · infill · backfill · landfill']],
 'fill/full 动作状态；refill/replace 补内容与换对象；infill、landfill、backfill 场景不同。',
 'Refill the bottle, then use filler to close the gap.\n\n把瓶子再装满，然后用填料封住空隙。','fill filler refill infill backfill landfill')
C=[['拉丁 con- + nectere → connectere → connect','共同 + 系结 → 连接'],['connect + -ed → connected','连着、有关联；也可人脉广'],['un-、-ness 等现代派生','未相连；相连状态、联系感']]
W('unconnected','/ˌʌnkəˈnektɪd/','未连接的；无关的、彼此没有联系的',
 '电缆没接上，是实体不通；两件事只是同时发生却没有关系，也可以是 unconnected。',
 'un- 否定 + connected，后者为 connect + -ed；否定连接状态，不一定说先连上又拆掉。',C,
 'unconnected events 无关事件，unconnected with 与……无关，an unconnected cable 未接上的电缆。',
 'unconnected events；unconnected with；an unconnected cable。',
 'unconnected 可以从来没接过；disconnected 常可强调断开，也有疏离、话不连贯等语境。',
 ('The two complaints were unconnected.','两起投诉互不相关。'),('An unconnected cable lay behind the desk.','一根没接上的电缆放在桌子后面。'))
W('connectedness','/kəˈnektɪdnəs/','相连状态、关联性；联系感、归属联系',
 '不是数一共有几根线，而是看各部分连在一起的状态，或一个人觉得自己与他人有联系。',
 'connected + -ness，把相连的性质、状态名词化。社交、心理语境可说联系感，数学、网络等语境有更具体的定义。',C[:2]+[['connected + -ness → connectedness','相连、有关联的状态；主观联系感']],
 'social connectedness 社会联系感，a sense of connectedness 联系感，the connectedness of a network 网络连通性。',
 'social connectedness；a sense of connectedness；network connectedness。',
 'connectedness 关注相连状态、联系感；connections 可具体一条条联系、人脉，不完全等于连接数量。',
 ('The club gave her a sense of connectedness.','俱乐部让她感到与别人有了联系。'),('The study examined connectedness within the network.','研究考察了网络内部的连通情况。'))
R('B4551','连接完成的状态与联系感','CONNECTED：实体接上，也可事情相关、人与人有联系','connected → unconnected、connectedness；interconnected 彼此交连。',
 '能接通、有关联、有人际联系是不同场景，不是所有 connected 都在说插上电线。',
 'con- + nectere → connect；connect + -ed；un- + connected；connected + -ness；inter- + connected。',
 [['相连及其否定、状态名词','connected · unconnected · connectedness'],['彼此交连','interconnected']],
 'unconnected 不一定曾连过；disconnected 可断开；connectedness 不是简单联系人数量。',
 'The interconnected groups created a sense of connectedness.\n\n彼此往来的小组让成员产生了联系感。','connected unconnected connectedness interconnected')
if __name__=='__main__':save('continuation_20261030_eh',ROOTS,WORDS)
