"""Screen and engine: everyday surfaces and ingenious machines."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
SC=[['中古英语 screne，接法语相应遮挡物名','防火、防风的屏障；更早可能日耳曼来源，路线有讨论'],['现代 screen','屏障、筛网 → 投影幕、显示屏；遮挡、筛选、放映']]
def SH(f,m):return SC+[[f,m]]
W('screen','/skriːn/','屏障；纱网、筛网；屏幕；遮挡、筛选、放映',
 '先是一层挡在中间的东西：挡风、遮视线；有孔就能筛，有平面就能接住投影，后来又成显示屏。',
 '经中古英语接法语遮挡物词，更早可能日耳曼语但具体路线有争论。现代屏幕、筛选与遮挡是不同分支，不都从电脑发明开始。',SC,
 'a phone screen 手机屏幕，a window screen 纱窗网，screen applicants 筛选申请者，screen a film 放映电影，screen out noise 滤掉噪声。',
 'a phone screen；a window screen；screen applicants；screen a film。',
 'screen 既名词又动词；screen a film 是放映，screen a candidate 是审查筛选。宾语决定走哪条义。',
 ('The film will be screened in the main hall.','电影将在主厅放映。'),('The team screened the applications before the interviews.','团队在面试前筛选了申请材料。'),sources=['https://www.etymonline.com/word/screen','https://en.wiktionary.org/wiki/screen#English'])
W('screening','/ˈskriːnɪŋ/','放映；筛选、初步筛查；网筛材料',
 '可以把电影投到幕上让人看，也可以把人或资料过一遍条件，筛出下一步要处理的对象。',
 'screen + -ing，分别承接放映、筛选、网筛等已有义项。词尾 -ing 只把活动或过程提出来，不替你选具体意思。',SH('screen + -ing → screening','放映活动；筛选过程；另有筛网材料名'),
 'a private screening 私人放映，a screening interview 初筛面试，screening applications 筛选申请。健康语境另有初步筛查义。',
 'a private screening；a film screening；a screening interview。',
 'screening 初筛与 final selection 最终选择不同；a screening of the film 则是电影放映，不能只按筛查翻。',
 ('We attended a private screening of the documentary.','我们参加了纪录片的私人放映。'),('Applicants complete a short screening interview first.','申请者先完成简短的初筛面试。'))
W('screenwriter','英 /ˈskriːnraɪtə/；美 /ˈskriːnraɪtər/','电影、电视编剧',
 '把将来要在屏幕上演出来的故事写成剧本的人，不是单纯在屏幕上打字。',
 'screen 银幕、影视 + writer 作者；writer 是 write + -er 的人物词。作品 screenplay 与活动 screenwriting 已有精讲。',SH('screen + writer → screenwriter','为影视作品写剧本的人'),
 'a film screenwriter 电影编剧，a television screenwriter 电视编剧，work with a screenwriter 与编剧合作。',
 'a film screenwriter；a television screenwriter；an experienced screenwriter。',
 'screenwriter 写剧本，director 导演负责影片创作组织、执导等；一个人可以兼任，职位含义仍不同。',
 ('The screenwriter revised the ending after the discussion.','讨论后，编剧修改了结尾。'),('She worked as a television screenwriter before writing novels.','写小说前，她做过电视编剧。'))
W('onscreen','英 /ˌɒnˈskriːn/；美 /ˌɑːnˈskriːn/','在屏幕上的；在镜头画面中的',
 '观众能在屏幕这一面看到的内容、表演或按钮。',
 'on + screen，连写可作形容词或副词；也有 on-screen、on screen 的写法，使用取决于句中位置及编辑习惯。',SH('on + screen → onscreen','显示在屏幕上；呈现在镜头内'),
 'onscreen instructions 屏幕提示，an onscreen character 银幕角色，appear onscreen 出现在画面中。',
 'onscreen instructions；appear onscreen；an onscreen character。',
 'onscreen 画面中，offscreen 画面外或幕后的；onscreen relationship 可角色关系，不一定演员私下关系。',
 ('Follow the onscreen instructions to finish the setup.','按屏幕提示完成设置。'),('The actor appears onscreen for only a few minutes.','这位演员只在画面中出现几分钟。'))
W('screensaver','英 /ˈskriːnseɪvə/；美 /ˈskriːnseɪvər/','屏幕保护程序',
 '电脑暂时没人用，屏幕换成移动图案、照片等显示；早期目的是减少固定画面留下的痕迹。',
 'screen + saver，saver 来自 save + -er。早期技术用途后来扩展成闲置时的图像显示功能。',SH('screen + saver → screensaver','保护显示屏的程序 → 闲置图像显示'),
 'activate the screensaver 启动屏保，a photo screensaver 照片屏保，screensaver settings 屏保设置。',
 'a photo screensaver；screensaver settings；activate the screensaver。',
 'screensaver 屏保通常闲置时出现，wallpaper 壁纸通常是桌面背景。日常有人混用，具体设置里仍要分清。',
 ('The screensaver started after ten minutes of inactivity.','闲置十分钟后屏保启动了。'),('She chose family photos for the screensaver.','她选了家庭照片作屏保。'))
W('smokescreen','英 /ˈsməʊkskriːn/；美 /ˈsmoʊkskriːn/','烟幕；掩人耳目的说法或行动',
 '烟把后面的事挡住；比喻里，一番说法或动作也能把真正的问题遮住、转移注意。',
 'smoke 烟 + screen 屏障，不取显示屏的意思。由烟形成的遮挡扩展到掩饰、干扰视线的借口。',SH('smoke + screen → smokescreen','烟的屏障 → 转移注意、掩盖真相的手段'),
 'a smokescreen for something 为某事打掩护，use something as a smokescreen 用某事转移视线。',
 'a smokescreen for；use as a smokescreen；create a smokescreen。',
 'smokescreen 常带批评，认为表面理由遮盖真因；background 背景信息则不自动意味着掩饰。',
 ('Critics called the announcement a smokescreen for the budget cuts.','批评者称这份公告是在为削减预算打掩护。'),('The novel uses the argument as a smokescreen for a deeper conflict.','小说用这场争吵掩盖了更深层的冲突。'))
W('silkscreen','/ˈsɪlkskriːn/','丝网印版；丝网印刷',
 '一张细网有些地方让墨通过，有些地方挡住，图案就印到布或纸上。',
 'silk 丝 + screen 筛网，名称来自早期丝织网材料。后来网可用其他材料，名称仍保留。',SH('silk + screen → silkscreen','丝制网版 → 丝网印刷用版及相应工艺'),
 'a silkscreen print 丝网版画，silkscreen printing 丝网印刷，a silkscreen poster 丝网印制海报。',
 'silkscreen printing；a silkscreen print；a silkscreen poster。',
 'silkscreen 这里 screen 是网版而非电脑显示屏；silk 的历史命名不保证现代网一定还用真丝。',
 ('The artist produced a series of silkscreen prints.','艺术家创作了一组丝网版画。'),('The poster was made using silkscreen printing.','海报采用丝网印刷制作。'))
W('flatscreen','/ˈflætskriːn/','平板屏幕；平板电视、显示器',
 '跟早期厚厚的显像管设备比，机身前后更薄，成了一块平板。',
 'flat 扁平 + screen 显示屏，合成后也可指整台设备。常见其他写法 flat screen、flat-screen。',SH('flat + screen → flatscreen','扁平显示装置 → 平板屏幕或电视'),
 'a flatscreen television 平板电视，a large flatscreen 大平板电视或显示器。具体液晶、OLED 等属于更细的技术分类。',
 'a flatscreen television；a large flatscreen；a flatscreen monitor。',
 'flatscreen 说明外形类别，不只一种显示技术；widescreen 宽屏说比例较宽，两个标准不同。',
 ('A large flatscreen hangs on the wall.','墙上挂着一台大平板电视。'),('They replaced the old television with a flatscreen.','他们用平板电视换掉了旧电视。'))
R('B4207','屏障、网筛、投影幕与显示屏','SCREEN：从挡在中间的一层，到筛与显示','screen → screening；影视 screenplay → screenwriter → screenwriting 相邻；再分屏幕位置、屏保、烟幕和丝网。',
 '旧词先指防火、防风屏障，经法语进入英语，较远日耳曼路线有讨论。屏幕和筛选都是后来发展的分支。',
 'screen + -ing/writer/saver；on/off + screen；smoke/silk/flat/wide/full/home + screen。',
 [['基本遮挡与筛选、放映','screen · screening'],['影视写作','screenplay · screenwriter · screenwriting'],['屏幕位置与装置','onscreen · offscreen · screensaver · screenshot · widescreen · fullscreen · homescreen · flatscreen'],['其他屏障与网版','smokescreen · silkscreen · sunscreen · windscreen']],
 'screen 电影是放映、申请者是筛选；screensaver 屏保与 wallpaper 壁纸分；flatscreen 外形、widescreen 比例。',
 'The screenwriter attended a screening and saw her characters onscreen.\n\n编剧参加放映，看见自己笔下的角色出现在银幕上。',
 'screen screening screenplay screenwriter screenwriting onscreen offscreen screensaver screenshot widescreen fullscreen homescreen flatscreen smokescreen silkscreen sunscreen windscreen')
EN=[['拉丁 ingenium → 法语 engin','天生能力、巧思 → 巧妙装置、战械'],['中古英语 engyn → engine','机械装置 → 发动机；比喻动力来源、软件核心']]
W('engine','/ˈendʒɪn/','发动机；机车；驱动力；软件引擎',
 '让整套东西运转起来的核心：汽车里是发动机，软件里可以是处理搜索、图形的核心系统。',
 '借法语 engin，接拉丁 ingenium 天赋、巧思，较早也指机械、战械；发动机义后来成为核心。词首 en- 不是现代使成为前缀加独立 gine。',EN,
 'a car engine 汽车发动机，a steam engine 蒸汽机，a search engine 搜索引擎，an engine of growth 增长动力。',
 'a car engine；a steam engine；a search engine；an engine of growth。',
 'engine 常把能量转成有用动力，也可软件比喻；motor 与 engine 用法有交叉，不能只用一条所有发动机都燃油的规则区分。',
 ('The car’s engine would not start.','汽车发动机启动不了。'),('Tourism became an engine of growth for the town.','旅游业成为小镇增长的动力。'),sources=['https://www.etymonline.com/word/engine','https://en.wiktionary.org/wiki/engine#English'])
W('engineer','英 /ˌendʒɪˈnɪə/；美 /ˌendʒɪˈnɪr/','工程师；策划、设计；火车司机〔美式〕',
 '把知识用来设计、建造、维护东西的人；作动词，也可以是有计划地把一件事促成。',
 '名词早经法语 engigneor 等形式进入英语，与 engin 装置、巧思同族；现代可联系 engine + -eer，但不能说只在现代英语临时给发动机添 er。',EN[:1]+[['法语 engigneor 等 → 英语 engineer','设计、建造装置者 → 工程师；后有策划动词']],
 'a civil engineer 土木工程师，a software engineer 软件工程师，engineer a solution 设计促成方案。美式 train engineer 可火车司机。',
 'a civil engineer；a software engineer；engineer a solution。',
 'engineer 不只修发动机的人；engineering 工程范围远宽于 engine。动词 engineer a deal 常策划促成交易，不必画机械图。',
 ('She works as a civil engineer.','她从事土木工程师工作。'),('The team engineered a simple solution to the problem.','团队设计出了一个解决问题的简单方案。'),sources=['https://www.etymonline.com/word/engineer','https://en.wiktionary.org/wiki/engineer#English'])
W('engineering','英 /ˌendʒɪˈnɪərɪŋ/；美 /ˌendʒɪˈnɪrɪŋ/','工程；工程学；设计与建造工作',
 '把想法变成能运作、能建造的方案，算、设计、测试、维护等都可能在里面。',
 'engineer + -ing，把工程师的工作、专业领域作为名词。也可在句中是 engineer 动词的进行形式。',EN[:1]+[['engineer + -ing → engineering','工程设计活动 → 工程专业、学科']],
 'civil engineering 土木工程，mechanical engineering 机械工程，engineering design 工程设计；通常作不可数专业名词。',
 'civil engineering；mechanical engineering；engineering design。',
 'engineering 不只引擎技术；science 常研究规律，engineering 常在约束中应用知识解决设计问题，实际工作可交叉。',
 ('He studied mechanical engineering at university.','他在大学学机械工程。'),('The bridge is an impressive piece of engineering.','这座桥是一项令人赞叹的工程成果。'))
R('B3121','巧思、机械装置与发动机；工程职业','ENGINE：巧思造装置，现代常说提供动力的核心','engine 后接相关职业 engineer、活动 engineering，避免以为工程只修发动机。',
 '法语 engin 来自拉丁 ingenium 天赋、巧思。engineer 有独立法语人物词借入历史，engineering 才是英语常见 -ing 派生。',
 '拉丁 ingenium → 法语 engin → engine；法语 engigneor → engineer → engineering。',
 [['装置、人物与专业','engine · engineer · engineering']],
 'engine 软件可指核心系统；engineer 不只发动机修理员；engine 与 motor 不能简单按燃油、电力绝对分。',
 'The engineer studies how the engine fits into the wider engineering system.\n\n工程师研究发动机怎样融入更大的工程系统。',
 'engine engineer engineering')
R('B4290','工程师、策划与工程专业','ENGINEER：设计解决问题的人，也可说有计划地促成','先相关 engine，再 engineer → engineering，人物和专业相邻。',
 '工程人物词借法语，最终与天赋、巧思词族相连，后来发展到土木、机械、软件等多领域。',
 'engine 相关旧词族；engineer → engineering。',
 [['相关装置、人物与专业','engine · engineer · engineering']],
 'engineering 是专业或活动，不只是引擎；engineer 作动词还可策划促成。',
 'The engineering team engineered a practical solution.\n\n工程团队设计出了一个实用方案。',
 'engine engineer engineering')
if __name__=='__main__':save('continuation_20261030_ag',ROOTS,WORDS)
