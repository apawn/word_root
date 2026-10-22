# -*- coding: utf-8 -*-
"""Individually explained sowing family; no figures; staging only."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
SOW=[['拉丁语 serere，分词 satus','播种、栽种']]
SATIO=SOW+[['拉丁语 satio，宾格 sationem','播种行为 → 播种时节']]
SAISON=SATIO+[['古法语 seison / saison','时节；适当时候']]
SEASON=SAISON+[['中古英语 sesoun → season','季节；某项活动的固定时期']]
SEED=[['拉丁语 semen，属格 seminis','种子；与 serere“播种”同属更早的播种词族']]
NURSERY=SEED+[['拉丁语 seminarius → seminarium','种子的 → 育苗圃；培养来源']]
SEMINARY=NURSERY+[['英语 seminary','苗圃〔旧义〕→ 培养人才的学校，尤指神学院']]
SCATTER=SEED+[['拉丁语 seminare；dis- + seminare → disseminare','播种 → 向四处撒播']]
W=[
E('season','/ˈsiːzən/','季节；赛季、播出季；调味；使熟化',
'最早是适合下种的那段时间，后来变成某件事有固定节奏的一段时期。',
'拉丁 satio“播种”经法语 saison 成为季节。调味动词也接法语 saisonner / assaisonner“使达到适宜状态”，不是“把春夏秋冬放进食物”。',SAISON+[['法语 saisonner / assaisonner；中古英语 sesoun / sesounen','适当时节；使成熟、调到适宜状态'],['英语 season〔名词与动词〕','季节、活动时期；调味；使木材等熟化']],
'a rainy season 是雨季；a season of a show 是一季节目。season the soup 是调味；season timber 则是让木材干燥、适于使用。都不能只用“季节”一义硬译。','in season；the football season；season with salt。','weather 是当下天气，season 是一年中的时段；动词 season 要根据对象读成调味或熟化。',
('The rainy season usually brings cooler afternoons.','雨季通常会带来较凉爽的午后。'),('Season the soup with a little salt and pepper.','给汤加一点盐和胡椒调味。'),('The wood needs time to season before it is used.','这批木材使用前需要时间干燥熟化。'),sources=['https://www.etymonline.com/word/season']),
E('seasonal','/ˈsiːzənəl/','季节性的；随季节变化的；当季的',
'日历转到某一段，它就特别常见、特别需要，或与别的季节不同。',
'season + -al，英语形容词；把季节或固定时段变成性质。',SEASON+[['英语 season + -al → seasonal','与季节有关的']],
'seasonal work 随旺季出现；seasonal vegetables 是当季蔬菜；seasonal variation 是按季节反复出现的变化。','seasonal workers；seasonal produce；seasonal variation。','temporary 只说暂时；seasonal 还指出这种安排或变化与季节有关。',
('The hotel hires seasonal workers during the summer.','这家酒店在夏季雇用季节工。'),('The menu changes to include seasonal vegetables.','菜单会变化，以采用当季蔬菜。')),
E('seminar','英 /ˈsemɪnɑː/；美 /ˈsemɪnɑːr/','研讨课；专题研讨会',
'把一小群人聚起来，围绕一个问题认真讨论，像在苗圃中一起培育想法。',
'借德语 Seminar，接拉丁 seminarium“苗圃、培育之地”。英语 seminar 与 seminary 是不同借入路线，不是把英语 seminary 简单去掉 y。',NURSERY+[['德语 Seminar','大学中由教师指导的研讨学习'],['英语 seminar','研讨课；围绕专题交流的会议']],
'大学 seminar 常需要事先阅读、参与讨论；行业 seminar 可由专家讲解并交流。规模和互动程度随活动安排而变。','attend a seminar；a seminar on history。','lecture 通常以讲授为主；seminar 常更强调专题讨论、交流或研究指导。',
('We read two articles before the seminar.','研讨课前我们读了两篇文章。'),('The library hosted a seminar on preserving family photographs.','图书馆举办了一场保存家庭照片的专题研讨会。'),sources=['https://www.etymonline.com/word/seminar']),
E('preseason','/ˌpriːˈsiːzən/','赛季前阶段；赛季前的；预先调味〔动词〕',
'正式比赛还没开始，球队先练习、试阵容，把状态调到能上场。',
'pre- 在前 + season。体育名词用的是赛季义；动词 preseason food 则是在 season“调味”之前加“预先”。',SEASON+[['英语 pre- + season → preseason','赛季开始前；另可指预先调味']],
'preseason training 是季前训练，preseason games 是正式赛季前的比赛。它不是一定在春季，而是相对于某项运动的赛历。','preseason training；a preseason match。','postseason 是常规赛之后的阶段；preseason 是赛季开始前。',
('The team focused on fitness during the preseason.','球队在季前阶段重点训练体能。'),('Two new players impressed the coach in a preseason match.','两名新球员在一场季前赛中给教练留下了好印象。')),
E('seminary','英 /ˈsemɪnəri/；美 /ˈseməneri/','神学院；宗教人才培养学校；学校〔历史用法〕',
'苗圃培养幼苗，学校培养将来承担宗教或其他职责的人；这里把“培育之地”转到了教育。',
'来自拉丁 seminarium“苗圃”，从 semen“种子”形成。英语早期确有苗圃义，后来广用于学校，现代常指宗教人才培养机构。',SEMINARY,
'可培养牧师、神父、拉比等，具体看宗教传统。旧校名中的 female seminary 可能是女子学校，不一定是女性神职学校。','a theological seminary；enter a seminary。','seminar 通常是一门课或一次研讨；seminary 通常是培养人的学校或机构。',
('He studied theology at a seminary.','他在神学院学习神学。'),('The building once housed a seminary for young women.','这栋楼过去曾是一所女子学校的校舍。'),sources=['https://www.etymonline.com/word/seminary']),
E('postseason','英 /ˌpəʊstˈsiːzən/；美 /ˌpoʊstˈsiːzən/','季后赛阶段；季后赛的',
'常规赛排完次序后，比赛还没有全结束，部分队伍继续争夺更高名次或冠军。',
'post- 在后 + season，英语体育构词；这里通常是常规赛之后，而非所有活动都停止后的休息时间。',SEASON+[['英语 post- + season → postseason','常规赛之后的比赛阶段']],
'常与 playoffs 相连，但具体赛事结构随联赛而不同。make the postseason 是取得进入季后赛阶段的资格。','reach the postseason；postseason games。','offseason 是通常没有正式赛季比赛的休赛期；postseason 往往还有关键比赛。',
('The club reached the postseason for the first time in years.','俱乐部多年来首次进入季后赛阶段。'),('Postseason games attracted larger crowds.','季后赛吸引了更多观众。')),
E('semen','/ˈsiːmən/','精液',
'可以把它理解为携带生殖细胞的液体，但液体整体和其中的精子细胞不是同一样东西。',
'直接接拉丁 semen“种子”，属格 seminis。植物种子与生殖的联想很早就进入词义；不是现代把 seed 翻译一次造出的英语词。',SEED+[['中古英语 semen → 英语 semen','用于生殖液体的拉丁借词']],
'一般是精子与生殖腺分泌液组成的混合物。semen analysis 指精液分析；有没有精子、数量多少，需要具体检查，不能由名称推定每份样本都一样。','a semen sample；semen analysis。','sperm 可以指精子细胞；semen 指包含各种成分的精液整体。',
('The laboratory received a semen sample for analysis.','实验室收到了一份待分析的精液样本。'),('The textbook distinguishes sperm cells from the other components of semen.','教科书区分了精子细胞与精液中的其他成分。'),sources=['https://en.wiktionary.org/wiki/semen','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/semen']),
E('seminal','/ˈsemɪnəl/','开创性的；影响深远的；种子或精液的',
'一个想法像种子一样，后面长出许多研究、作品和新方向，这就叫 seminal。',
'经古法语接拉丁 seminalis，来自 semen 的词干 semin- + 形容词后缀。开创性是从种子、源头义发展出的比喻。',SEED+[['拉丁 seminalis → 古法语 seminal → 英语 seminal','种子的、精液的 → 能引出后续发展的']],
'a seminal paper 不只是写得好，还对后来研究起了奠基作用。解剖语境如 seminal fluid 则保留生殖相关义。','a seminal work；a seminal influence；seminal fluid。','important 泛说重要；seminal 特别强调成为后续发展的起点。',
('Her seminal paper opened a new field of research.','她那篇开创性论文开辟了新的研究领域。'),('The discovery had a seminal influence on later designs.','这项发现对后来的设计产生了奠基性的影响。')),
E('dissemination','/dɪˌsemɪˈneɪʃən/','传播；散布；播散',
'一条信息从少数人手里散到许多地方，像种子被撒到更广的地面。',
'借拉丁 disseminatio，来自 disseminare“向各处撒种”。现代对应 disseminate + -ion，但名词有自己的拉丁借入路线。',SCATTER+[['拉丁 disseminatio → 英语 dissemination','撒播行为 → 信息、思想等传播']],
'常见 dissemination of information 或 research findings，强调让更多人接触到信息。医学里的 dissemination 也可说病变扩散，不能一律译成宣传。','information dissemination；the dissemination of findings。','publication 是发表；dissemination 还包括让成果到达读者和使用者的传播过程。',
('The project includes a plan for the dissemination of its findings.','项目包含一项传播研究结果的计划。'),('Local radio helped with the rapid dissemination of the warning.','地方电台帮助迅速传播了警报。')),
E('seasonally','/ˈsiːzənəli/','按季节；随季节；在当季',
'把一年分段再看，需求、天气或经营方式会随着时段转变。',
'seasonal + -ly，英语副词构词。',SEASON+[['英语 seasonal → seasonally','季节性的 → 随季节地']],
'open seasonally 表示只在特定季节开放；seasonally adjusted data 是按方法调整季节性影响后的数据，不是“把数字改成某个季节”。','vary seasonally；seasonally adjusted；eat seasonally。','annually 只说每年一次或按年；seasonally 特别关注季节之间的规律。',
('Demand for hotel rooms varies seasonally.','酒店客房需求随季节变化。'),('The visitor center operates seasonally.','游客中心只在特定季节开放。')),
E('disseminate','/dɪˈsemɪneɪt/','传播；散布；使广泛流传',
'把一份知识或消息送到许多人的手中，让它不只留在原来的小圈子里。',
'来自拉丁 disseminatus，disseminare 的分词；dis- 向各处 + seminare 播种。这里 dis- 不是把播种取消。',SCATTER+[['拉丁 disseminatus → 英语 disseminate','已撒播的 → 广泛传播']],
'常用于研究成果、消息、观点和知识，语气比 spread 正式。传播本身不保证内容真实，disseminate false information 也说得通。','disseminate information；disseminate research。','distribute 常强调把具体东西分送出去；disseminate 常强调消息或思想广泛到达。',
('The team used workshops to disseminate practical knowledge.','团队通过工作坊传播实用知识。'),('The website was designed to disseminate reliable information.','这个网站旨在传播可靠信息。')),
E('insemination','/ɪnˌsemɪˈneɪʃən/','授精；播种〔旧义〕',
'把生殖材料引入生殖系统，为之后可能发生的受精创造条件；引入这一步与受精结果要分开。',
'inseminate + -ion；动词接拉丁 in- 向内 + seminare 播种，早期英语也有撒种义。生殖专门义后来发展。',SEED+[['拉丁 in- + seminare → inseminare / inseminatus','向内播种、植入'],['英语 inseminate → insemination','播种 → 授精的行为']],
'artificial insemination 是人工授精。insemination 本身不等于卵子已经受精，也不等于已经怀孕；这是几个不同阶段的名称。','artificial insemination；an insemination procedure。','fertilization 是受精、精卵结合；insemination 指引入生殖材料这一步。',
('The textbook distinguishes insemination from fertilization.','教科书区分了授精与受精。'),('The veterinary course includes the history of artificial insemination.','兽医课程包含人工授精的历史。'),sources=['https://www.etymonline.com/word/insemination','https://www.merriam-webster.com/dictionary/insemination']),
E('seasonality','/ˌsiːzəˈnæləti/','季节性；随季节反复变化的规律',
'把每年的曲线叠起来，某些月份总是高、另一些总是低，这种重复节奏就是 seasonality。',
'seasonal + -ity，英语名词；重音转到 -nal- 附近，读作 /næl/。',SEASON+[['英语 seasonal → seasonality','季节性的 → 季节性变化规律']],
'旅游、零售、气温等数据都可能表现出 seasonality。统计里也可广义指按固定周期重复的变化，不只春夏秋冬。','seasonality in demand；account for seasonality。','trend 是较长期的总体方向；seasonality 是反复出现的周期模式。',
('The forecast accounts for seasonality in visitor numbers.','预测考虑了游客人数的季节性变化。'),('Ignoring seasonality made the winter sales decline look unusual.','忽略季节性后，冬季销售下降看起来就显得异常。')),
E('seminarian','英 /ˌsemɪˈneəriən/；美 /ˌseməˈneriən/','神学院学生；宗教人才培养学校的学生',
'他正在那所“培养人的苗圃”里学习，准备将来承担宗教工作。',
'seminary + 表示相关人的 -an / -ian，英语构词。不是 seminar“研讨会”的所有与会者。',SEMINARY+[['英语 seminary → seminarian','神学院 → 神学院学生']],
'常见于宗教教育背景，尤其神职培养。具体学生未来是否成为神职人员，取决于个人与机构，不是词本身保证。','a young seminarian；seminarians studying theology。','student 是所有学生的通称；seminarian 明确指出在神学院或类似机构学习。',
('The seminarian spent the summer working in a local parish.','这位神学院学生暑假在当地教区工作。'),('Several seminarians attended the lecture on church history.','几位神学院学生参加了教会史讲座。'),sources=['https://www.merriam-webster.com/dictionary/seminarian','https://www.etymonline.com/word/seminarian']),
E('seasonable','/ˈsiːzənəbəl/','合乎时令的；适时的',
'事情来得正是时候，或者天气正合这个季节该有的样子。',
'来自古法语 saisonable、盎格鲁法语 seisonnable，与 saison“时节”相关；现代能看成 season + -able，但并非只能解释为英语派生。',SAISON+[['古法语 saisonable / 盎格鲁法语 seisonnable','合时节的、适时的'],['中古英语 → seasonable','合乎时令；来得及时']],
'seasonable weather 是符合时令的天气。旧式表达中的 seasonable advice 指来得正及时的建议，不是关于季节的建议。','seasonable weather；seasonable temperatures；seasonable advice。','seasonal 是与季节有关；seasonable 强调适合这个季节或恰逢其时。',
('Temperatures returned to seasonable levels after the heat wave.','热浪过后，气温恢复到符合时令的水平。'),('A seasonable shower helped the newly planted crops.','一场及时雨帮助了刚种下的作物。'),sources=['https://www.etymonline.com/word/seasonable']),
E('seminiferous','/ˌsemɪˈnɪfərəs/','产种子的；生精的；含有或输送精液的',
'把某个结构看成“生产或承载种子、生殖材料的地方”。',
'拉丁 semin- 种子 + -iferous 承载、产生；也有经后期拉丁 seminifer 的来源分析。fer 接“携带”，不是铁元素符号 Fe。',SEED+[['拉丁 seminifer；英语 semin- + -iferous','承载种子、生殖材料的'],['英语 seminiferous','产生或承载种子、精子的']],
'seminiferous tubules 通常译曲细精管，是睾丸内生成精子的细管。不要因英文词典简写 semen 就把全部精液都说成在这里形成。','seminiferous tubules；seminiferous epithelium。','seminal 泛说种子、精液或开创性；seminiferous 更突出产生、承载的结构作用。',
('Sperm develop within the seminiferous tubules of the testes.','精子在睾丸的曲细精管内发育。'),('The diagram labels the seminiferous epithelium.','示意图标出了生精上皮。'),sources=['https://www.merriam-webster.com/dictionary/seminiferous','https://en.wiktionary.org/wiki/seminiferous']),
E('sative','/ˈseɪtɪv/','栽培的；播种种植的〔旧词〕',
'这株植物不是自己在野外长出来的，而是人有意栽下、培育出来的。',
'借拉丁 sativus，由 serere 的分词 satus 加 -ivus 形成；与 season 的 satio 同属播种分支。',SOW+[['拉丁 satus + -ivus → sativus','已播种的 → 可栽种、栽培的'],['英语 sative〔旧用〕','栽培的，非野生的']],
'现代一般用 cultivated；旧植物学文字中偶见 sative。学名中的 sativa、sativus 是相应拉丁形式，不是英语必须这样变词尾。','sative plants〔旧式〕；a sative variety〔旧式〕。','native 是原生的，与自然分布有关；sative 是栽培的，不能因为只差一个字母就混淆。',
('The old botanical text contrasts sative plants with wild ones.','这本旧植物学著作把栽培植物与野生植物作对比。'),('The author describes the crop as a sative variety.','作者把这种作物描述为一个栽培品种。'),sources=['https://www.merriam-webster.com/dictionary/sative','https://en.wiktionary.org/wiki/sative']),
E('semination','/ˌsemɪˈneɪʃən/','播种；种子散布；授精〔专门用法〕',
'把种子送出去，让它有机会在别处生长；这是比 dissemination 更少见的原始播种说法。',
'接拉丁 seminatio，由 seminare“播种”形成。英语也有 seminate，但名词有独立拉丁来源，不必把它画成英语动词再生出的唯一结果。',SEED+[['拉丁 seminare → seminatio','播种 → 播种行为'],['英语 semination','播种、种子散布；亦有授精用法']],
'现代植物讨论常用 sowing 或 seed dispersal；医学词典也保留授精义。这个词少见，读到时先判断是在讲植物还是生殖。','natural semination；the semination of plants〔较少见〕。','dissemination 常用来讲信息广泛传播；semination 更接近种子与繁殖的原始图景。',
('The old manual discusses the semination of meadow plants.','这本旧手册讨论了草甸植物的播种。'),('The study compared natural semination with deliberate sowing.','研究比较了自然种子散布与有意播种。'),sources=['https://www.etymonline.com/word/semination','https://www.merriam-webster.com/medical/semination']),
]
ROOT=dict(id='C1319',meaning='播种、栽种；同族的种子',core='把种子放到适合的地方和时间，让新的生命或想法从这里长出来。',image='播种的时节成为 season；育苗的地方成为 seminary 与 seminar 的来源；向四周撒播成为 disseminate。',intro='本组的拉丁 serere 是播种，分词 satus 形成 sat-。拉丁 semen“种子”、词干 semin- 与它同属更早的播种词族，可追到重构的原始印欧语 *seh₁-。所以本页不把英语 semen 画成现代 ser- 加字母，也不把每个 semin- 都误拆为 semi-“一半”。',forms='ser- / sat- 见于拉丁 serere、satus、satio、sativus；satio 经法语成为 season。semin- 是 semen 的词干，见 seminal、seminar、disseminate。另一个拉丁 serere“连接、编织”与这里的播种词需分开；英语 series 不能只凭 ser- 搬进来。',branches=[['播种的时节','season, seasonal, seasonally, seasonality, seasonable'],['活动有固定时期','preseason, postseason'],['种子与生殖','semen, seminal, insemination, seminiferous'],['培养人才与想法','seminar, seminary, seminarian'],['撒播与栽培','disseminate, dissemination, semination, sative']],contrasts='seasonal 是季节性的，seasonable 是适时、合时令的。seminar 是研讨活动，seminary 是培养人才的学校，seminarian 是其中学生。semen 是精液整体，sperm 是精子；insemination 是授精，引入之后不等于已经 fertilization 受精。seminal 的开创性来自种子能引出新发展的比喻。',practice='别只背“semin=种子”：先看到播种、培育、扩散三个动作。研讨课培育想法，seminal work 为后人提供起点，disseminate 把成果带到更广的地方；而 season 走的是适合播种的时间这条线。',words=[],exclude={})
if __name__=='__main__':
    manifest=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text())
    original=next(r for r in manifest['roots'] if r['id']==ROOT['id'])
    ROOT['words']=[w for w in original['family'] if '-' not in w]
    expected=set(ROOT['words'])&set(manifest['owned_words']);actual={e['word'] for e in W}
    assert actual==expected,(expected-actual,actual-expected)
    assert len(W)==len(actual)
    assert all(len(e['examples'])>=2 and e['ipa'] and len(e['history'])>=2 for e in W)
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'roots_batch200_vid_06.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2))
    (OUT/'words_batch200_vid_06.json').write_text(json.dumps(W,ensure_ascii=False,indent=2))
    print('ser:',len(W),'new words;',sum(len(e['examples']) for e in W),'bilingual examples')
