"""Everyday -ing and -ed forms with meanings beyond an unfinished action."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2964':dict(words=['run','running'],label='running：跑动、流动与持续运转',note='run 双写 n 加 -ing；运行、经营、连续等义承接 run 的不同支线，不都翻译成跑步。'),
 'C0728':dict(words=['market','marketing'],label='marketing：把产品带到买家面前',note='market 来自拉丁交易词族；marketing 为动词 -ing 名词，现代营销义覆盖认识需求、定位、推广等市场活动。'),
 'A1741':dict(words=['date','dating'],label='dating：交往与确定年代',note='date 的日期、约会线接拉丁 dare 给出等材料，与椰枣的另一来源分开；date 去 e 加 -ing。'),
 'A1760':dict(words=['date','dated'],label='dated：有日期、显出年代与交往过',note='date 加 -d，末尾读 /ɪd/；dated 形容风格过时，来自显出某个旧时代特征的语义发展。'),
 'C1057':dict(words=['plan','planning','planned'],label='plan：图纸、安排与计划好的状态',note='plan 接拉丁平面词族，经法语入英语；planning、planned 都双写词末 n，分别呈现筹划过程和已安排的状态。'),
 'B2882':dict(words=['keep','keeping'],label='keeping：保管、保持与相称',note='keep 接古英语看顾、守护等材料；keeping 的固定表达 in keeping with 说与某种风格、原则相合。'),
 'C0769':dict(words=['move','moving','moved'],label='move：位置变化与感情受到触动',note='move 经法语接拉丁 movere；moving 可描写引起感情的事物，moved 描写受到触动的人。'),
 'C0232':dict(words=['close','closing'],label='closing：关上、结束与尾声',note='close 经法语接拉丁 clausus、claudere 关闭词族；动词 /z/ 去 e 加 -ing，closing 可作结束部分的名词或修饰语。'),
 'B2968':dict(words=['set','setting'],label='setting：放置、设定与安排好的环境',note='set 双写 t 加 -ing；场景、设置、镶座等名词义抓住某物被安置在何种环境或状态中，不假定每项义都同一天形成。'),
 'C0898':dict(words=['operate','operating'],label='operating：正在运转与业务运作的',note='operate 去 e 加 -ing；operating 的运行、经营、手术等义按所属领域分清。'),
 'B2828':dict(words=['break','breaking'],label='breaking：打破与新闻刚刚传来',note='break + -ing；breaking news 接消息突然传开、出现的用法，不按字面译破碎的新闻。'),
}
W('running','/ˈrʌnɪŋ/','跑步；运行、经营；流动的；连续的',
 '腿不停向前，是 running；水一直流、机器持续转、公司每天运作，也都抓住持续动起来这个画面。',
 'run 双写 n 加 -ing。run 继承古英语 rinnan、irnan 等跑、流材料，现代分词又常用作名词、形容词；名词 running 可直接说跑步或管理运作。',
 [['古英语跑、流词族 → run','移动；流动；后来也说设备运转、经营'],['run + -ing → running','跑步、运转；流动或连续的']],
 'go running 去跑步；running water 流水、自来水；running costs 维持运作的费用；three days running 连续三天；in the running 仍有胜算。',
 'keep the business running；the day-to-day running of a school。','running water 在住宿介绍中常说有管道供水，不能只想成河水。three days running 表连续发生，不是跑了三天步。',
 ('Running helps me clear my head after work.','下班后跑步能让我头脑清醒。'),('The village now has electricity and running water.','村里如今通了电和自来水。'),('It rained for three days running.','雨连续下了三天。'),sources=['https://en.wiktionary.org/wiki/running#English'])
W('marketing','英 /ˈmɑːkɪtɪŋ/；美 /ˈmɑːrkɪtɪŋ/','营销；市场推广；market 的 -ing 形式',
 '做出了东西，还要弄明白谁需要它、怎样让人知道并愿意买。这一整套把产品与买家接起来的工作，是 marketing。',
 'market + -ing，由市场买卖相关动词形成名词。更早 market 经法语等接拉丁 mercatus 交易、市场；现代商业营销义在旧买卖活动义上进一步专门化。',
 [['拉丁 mercatus → market','交易、市场；后来作动词推向市场'],['market + -ing → marketing','市场活动 → 现代营销领域']],
 'a marketing team 营销团队；market research 市场调研；digital marketing 数字营销；a marketing campaign 一轮营销活动。广告是常见手段之一。',
 'work in marketing；a marketing strategy。','marketing 范围通常比 advertising 广，既要考虑对象和产品怎样匹配，也可包括定价、渠道、推广；sales 更直接关心把交易做成。',
 ('She works in marketing for a small food company.','她在一家小食品公司做营销。'),('The marketing team interviewed customers before the launch.','上市前，营销团队采访了顾客。'),sources=['https://www.etymonline.com/word/marketing','https://en.wiktionary.org/wiki/marketing#English'])
W('dating','/ˈdeɪtɪŋ/','约会、恋爱交往；确定年代；date 的 -ing 形式',
 '给见面约定一个时间，发展出约会、交往这一支；给旧物找出它属于哪个时间，发展出测年这一支。',
 'date 去词末 e 加 -ing。这里承接日期、约定时间的 date，近源经法语接拉丁 data 等给出、注明日期的材料；不接椰枣那条同形词源。',
 [['日期 date → date 动词','注明日期、确定年代；安排见面、交往'],['date 去 e + -ing → dating','测年活动；恋爱交往等']],
 'start dating 开始交往；online dating 网络交友、约会；carbon dating 碳年代测定；dating from a period 属于某时期，通常由 date from 接出。',
 'They are dating；a dating app；the dating of an object。','They are dating 常表示正在恋爱交往，不仅是今天碰巧约好见面。dating an old building 则可能是在确定建筑年代，要看对象。',
 ('They started dating after meeting at university.','他们在大学认识后开始交往。'),('The dating of the pottery helped researchers understand the site.','陶器的年代鉴定帮助研究人员了解了遗址。'),sources=['https://www.etymonline.com/word/dating','https://en.wiktionary.org/wiki/dating#English'])
W('dated','/ˈdeɪtɪd/','注明日期的；显得过时的；date 的过去式、过去分词',
 '一封信写着某年某月，是有日期；一件衣服一眼看出是很多年前的流行款，就可能让人觉得 dated，带着旧时代的痕迹。',
 'date + -d；因词干末音 /t/，结尾读 /ɪd/。日期义的分词可说已注明日期；形容词又由显出年代发展为显得陈旧、过时。交往动词也有同形过去式。',
 [['date','日期；注明时间、确定年代；交往'],['date 去 e + -ed → dated','有日期；显出旧年代而过时；过去交往等']],
 'a letter dated 6 May 注明五月六日的信；look dated 看起来过时；a dated design 陈旧设计；They dated for a year 他们交往过一年。',
 'a dated photograph；dated language。','dated 不单等于 old。古老建筑可以仍然好看，dated 常在评价风格或做法跟不上现在；letter dated Monday 则只是中性的日期说明。',
 ('The letter was dated 12 March.','信上注明的日期是三月十二日。'),('The website works well, but its design looks dated.','网站好用，不过设计看起来有些过时。'),sources=['https://en.wiktionary.org/wiki/dated#English'])
W('planning','/ˈplænɪŋ/','筹划、规划；plan 的 -ing 形式',
 '还没动手，先把目标、顺序、时间和需要的东西摆出来。planning 是把准备工作一步步想清楚的过程。',
 'plan 双写 n 加 -ing。plan 先借法语平面、图纸词，上接拉丁 planum 平面；英语再作动词，planning 形成筹划、规划的常用名词。',
 [['拉丁 planum → 法语／英语 plan','平面图 → 行动安排'],['plan + -ing → planning','作安排的过程；规划领域']],
 'careful planning 周密筹划；urban planning 城市规划；planning permission 规划许可，常见英式表达；plan to do，planning to do 都接下一步打算。',
 'the planning stage；planning a trip。','a plan 是一份方案或一个打算，planning 是筹划过程。名词常不可数：good planning；需要数份文件时说 several plans。',
 ('Good planning saved us a lot of time.','妥善筹划给我们省了不少时间。'),('They are planning to visit in spring.','他们打算春天来访。'),sources=['https://www.etymonline.com/word/planning','https://en.wiktionary.org/wiki/planning#English'])
W('planned','/plænd/','计划好的、有安排的；plan 的过去式、过去分词',
 '事情发生前就放进了安排表，不是临时碰上。a planned visit 就是事先安排的拜访。',
 'plan 双写 n 加 -ed；末尾读 /d/。分词可用于被动，也可作形容词说明安排好的性质；如作过去式，说明过去曾作计划，不保证计划后来实现。',
 [['plan','画出、安排行动方案'],['plan + -ed → planned','过去作安排；事先安排好的']],
 'a planned trip 计划中的旅行；as planned 按计划；planned changes 拟定的变更；a planned community 有规划建设的社区。',
 'a carefully planned event；go as planned。','We planned to leave 说原先有离开的打算；We left as planned 才明确说按计划离开了。planned 不自动等于已经完成。',
 ('The repairs took longer than planned.','维修用时比计划长。'),('We planned to walk, but the rain changed our minds.','我们原打算步行，但下雨让我们改了主意。'),sources=['https://en.wiktionary.org/wiki/planned#English'])
W('keeping','/ˈkiːpɪŋ/','保管、照管；保持；keep 的 -ing 形式',
 '把东西留在可靠的人手里，状态也能被保持下去。in her keeping 是交由她保管；in keeping with 则像整体风格被保持一致。',
 'keep + -ing，接古英语 cepan 看顾、守护的动词。保管名词义与保持、维持义并行，固定表达 in keeping with 后来表示相合、协调。',
 [['古英语 cepan → keep','留意、守护；保留、维持'],['keep + -ing → keeping','保管、保持；固定表达中的相称']],
 'in someone’s keeping 由某人保管；in keeping with 与……相称、符合；out of keeping with 与……不协调；keeping a promise 信守承诺。',
 'safe keeping；the keeping of records。','in keeping with the style 说与风格协调，不是把风格收进柜子。作动词时，They are keeping the records safe 表示他们在妥善保管记录。',
 ('The original documents are in her keeping.','原始文件由她保管。'),('The new windows are in keeping with the style of the house.','新窗户与房屋风格很协调。'),sources=['https://en.wiktionary.org/wiki/keeping#English'])
W('moving','/ˈmuːvɪŋ/','移动中的；搬家的；感人的；move 的 -ing 形式',
 '位置在动，是 moving；故事让心里的感受也动起来，就是 moving 感人。',
 'move 去 e 加 -ing。move 经法语接拉丁 movere 移动、使动；感情受触动的用法随动词发展，moving 作形容词说引起情感反应。',
 [['拉丁 movere → move','使位置变化；使感情受到触动'],['move 去 e + -ing → moving','正在动；有感动力的']],
 'a moving car 行驶中的车；moving house 搬家；a moving speech 感人的演讲；moving costs 搬迁费用。',
 'a deeply moving story；a moving target。','moving 说引起感动，moved 说受到感动。The speech was moving；I was moved。描写物体时仍可能只是正在移动。',
 ('She gave a moving account of her childhood.','她讲述了自己的童年，令人动容。'),('We spent the weekend moving house.','我们整个周末都在搬家。'),sources=['https://www.etymonline.com/word/moving','https://en.wiktionary.org/wiki/moving#English'])
W('moved','/muːvd/','移动了、搬迁了；感动的；move 的过去式、过去分词',
 '椅子换了位置，人心里的感受也发生变化。be moved by a letter 是被那封信打动。',
 'move + -d，末尾读 /d/。分词既能表示被移动的结果，也能接感情触动义；与 moving 的作用方向对照理解。',
 [['move','移动；使感情受到触动'],['move 去 e + -ed → moved','发生移动；受到情感触动的状态']],
 'be deeply moved 深受感动；moved by someone’s kindness 被善意打动；moved to tears 感动得流泪；have moved 搬过家、已搬迁。',
 'feel moved；moved from one city to another。','I was moved by the film 说我被打动；I was moving a box 说我当时在搬箱子。先辨词形与结构，中文才不会都挤成移动。',
 ('I was deeply moved by her kindness.','她的善意让我深受感动。'),('They moved to a smaller flat last year.','他们去年搬进了一套更小的公寓。'),sources=['https://en.wiktionary.org/wiki/moved#English'])
W('closing','英 /ˈkləʊzɪŋ/；美 /ˈkloʊzɪŋ/','关闭、结束；收尾的；close 的 -ing 形式',
 '门合上，营业结束；活动走到尾声，最后几句话也是 closing。画面从关上一个空间，扩到结束一段过程。',
 '动词 close 去 e 加 -ing，s 读 /z/。动词经法语接拉丁 clausus 关上的、claudere 关闭；相关分词、名词发展出结束和收尾部分。',
 [['拉丁关闭词族 → close','关闭；结束'],['close 去 e + -ing → closing','关闭过程；结尾部分；收尾的']],
 'closing time 打烊时间；closing remarks 结束语；a closing ceremony 闭幕式；the closing of a shop 商店关闭。',
 'closing date；closing prices。','形容词 close 近的常读 /kləʊs/ 或 /kloʊs/；closing 由动词来，含 /z/。closing date 通常是截止日期，要按活动看具体截止何事。',
 ('We arrived just before closing time.','我们在快打烊时赶到了。'),('Her closing remarks brought the discussion back to its main point.','她的结束语把讨论拉回了重点。'),sources=['https://en.wiktionary.org/wiki/closing#English'])
W('setting','/ˈsetɪŋ/','环境、背景、场景；设置；镶座；set 的 -ing 形式',
 '把故事放在什么地方、把机器调到什么档，都是给东西安置一个位置或状态。setting 可以是周围场景，也可以是设定好的选项。',
 'set 双写 t 加 -ing；动词上接古英语 settan 使就位。名词逐渐用于安置的环境、安排的状态，以及把宝石固定住的镶座等。',
 [['古英语 settan → set','使就位、摆放；设定'],['set + -ing → setting','安置过程；环境、设置、镶嵌结构']],
 'the setting of a story 故事背景；a rural setting 乡村环境；change the settings 更改设置；a low heat setting 低温档；a diamond setting 钻石镶座。',
 'a beautiful setting；privacy settings。','setting 作为背景常看故事发生的时地环境；plot 看情节怎样推进。手机 settings 常用复数，因为里面有多项选项。',
 ('The village provides the setting for the novel.','小说以这个村庄为背景。'),('Check the volume setting before playing the recording.','播放录音前检查一下音量设置。'),('She opened the privacy settings on her phone.','她打开了手机的隐私设置。'),sources=['https://en.wiktionary.org/wiki/setting#English'])
W('operating','英 /ˈɒpəreɪtɪŋ/；美 /ˈɑːpəreɪtɪŋ/','运行中的；经营的、业务运作的；手术的；operate 的 -ing 形式',
 '机器确实转着，机构确实办着事。operating 常把注意力放在实际运作，而不是纸面上拥有设备或公司名称。',
 'operate 去 e 加 -ing；operate 接拉丁 operari 工作、施行，相关词干 oper- 接工作、作品词族。医学手术义是施行操作的一条专业支线。',
 [['拉丁 operari → operate','工作、施行；使运行'],['operate 去 e + -ing → operating','正在操作、运行；运作或手术相关的']],
 'an operating system 操作系统；operating costs 运营费用；operating hours 营业、运行时间；an operating theatre 手术室，常见英式；operating room 常见美式。',
 'operating instructions；an operating company。','operating costs 常指维持日常运作的费用，具体会计范围看语境；operating room 的固定医学义不能直译成任何操作的房间。',
 ('The machine is operating normally again.','机器又恢复正常运行了。'),('The museum reduced its operating hours in winter.','博物馆冬季缩短了开放时间。'),sources=['https://en.wiktionary.org/wiki/operating#English'])
W('breaking','/ˈbreɪkɪŋ/','打破、断裂；刚发生、刚传来的〔尤新闻〕；break 的 -ing 形式',
 '原来连着的东西断开，是 breaking；一条新消息突然进入大家视野，新闻里就说 breaking news。',
 'break + -ing，继承古英语 brecan 打破词族。break 也发展出消息传开、突然出现的用法，breaking news 接这一支，不是新闻物品碎了。',
 [['古英语 brecan → break','打破、断开；后来也说消息传开'],['break + -ing → breaking','打破中；消息刚传来的']],
 'breaking news 突发、最新传来的新闻；breaking a rule 违反规则；breaking the silence 打破沉默；breaking point 忍耐或承受的极限。',
 'a breaking wave；a breaking news alert。','breaking 强调消息刚出现；描述这一类报道时常把 breaking news 当整体记住。broken news 不是这类新闻标签；broken 是另一种分词。',
 ('The radio interrupted the programme with breaking news.','电台中断节目，插播了一条突发新闻。'),('He was fined for breaking the rules.','他因违反规定被罚了款。'),sources=['https://en.wiktionary.org/wiki/breaking#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_us',ROOTS,WORDS)
 extend_lessons()
