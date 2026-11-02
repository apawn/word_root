"""Municipal, graph instruments, ambassadors and drainage."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
M=[['拉丁 mūnus 义务、公共服务 + capere 的相关成分','承担公共责任的居民身份'],['mūniceps、mūnicipium → mūnicipālis → 法语 municipal','城镇、市民、城镇相关的性质'],['英语 municipal','市政的；地方政府相关的']]
W('municipal','/mjuːˈnɪsɪpəl/','市政的；地方自治政府的',
 '路灯、垃圾清运、社区公共设施等由当地政府负责，相关事物常用 municipal。它关注地方公共管理，不只是城市里有的东西。',
 '借法语 municipal，接拉丁 mūnicipālis、mūnicipium。更早的 mūniceps 联系 mūnus 公共义务与承担的成分，帮助理解城镇共同体；不是 music 加后缀。',M,
 'municipal services 市政服务，a municipal council 市政议会，municipal buildings 市政建筑。具体地方政府层级随国家制度不同，不能只按中文某一固定级别套。',
 'municipal services；a municipal council；municipal buildings。',
 'urban 强调城市的环境、性质；municipal 强调地方政府管理、归属。城市里的私人咖啡馆是 urban 场景，不因此就是 municipal 资产。',
 ('The council improved several municipal services.','市政议会改善了几项市政服务。'),('The library is housed in a municipal building.','图书馆设在一座市政建筑里。'))
W('municipality','/mjuːˌnɪsɪˈpæləti/','自治市、地方行政单位；其政府、当局',
 'municipal 说地方政府相关的性质，municipality 则把整块有相应地方政府的行政单位，或管理它的当局，作为一个对象来称呼。',
 '借法语 municipalité，与 municipal + -ity 对应。继承地方共同体的来源，名词重音移到 /pæl/，不只是把形容词原封不动读完再加词尾。',M+[['法语 municipalité → 英语 municipality','地方自治行政单位；该单位的政府']],
 'the local municipality 当地自治市、地方当局，several municipalities 几个地方行政单位。某些地区可含多个居民点，不能一律画成一个连续大城市。',
 'the local municipality；several municipalities。',
 'municipality 可指辖区，也可指当局；city 常指城市。二者在具体制度下可能重叠，含义却不自动完全相同。',
 ('The municipality manages the local parks.','当地政府管理着当地公园。'),('The study compares transport in five municipalities.','研究比较了五个地方行政单位的交通。'))
W('municipally','/mjuːˈnɪsɪpəli/','由地方政府、市政当局；在市政方面',
 'municipally owned 就是地方政府拥有的。这个副词经常告诉你：这件事是谁在管、是谁出资。',
 'municipal + -ly，形容词以 l 结尾，再加 -ly，拼写有 ll；常见读法中末尾音节可压缩。',M+[['municipal + -ly → municipally','与市政管理方式、归属有关的副词']],
 'municipally owned 地方政府所有的，municipally funded 由地方政府资助的，municipally operated 由市政当局运营的。',
 'municipally owned；municipally funded；municipally operated。',
 'municipal facilities 是市政设施；municipally owned facilities 明确说由地方政府拥有。归属、出资和运营并非同一关系。',
 ('The town has a municipally owned swimming pool.','镇上有一个地方政府所有的游泳池。'),('The centre is municipally funded.','这个中心由当地政府资助。'))
R('B4401','城镇共同体、地方公共管理，以及相应行政单位和归属','MUNICIPAL：共同体里的地方公共事务','municipal → municipality 行政单位或当局；municipally 修饰拥有、资助等关系。',
 '先抓地方公共管理，再区分性质、行政对象和句子里的方式、归属。不要只记成城里的。',
 'mūnus 与承担的成分 → mūniceps、mūnicipium → mūnicipālis；经法语形成英语相关词。',
 [['性质、行政对象与副词','municipal · municipality · municipally']],
 'municipal 不等于所有 urban；municipality 的具体层级随制度变化。',
 'The municipality operates several municipally owned facilities and provides municipal services.\n\n当地政府运营几处自有设施，并提供市政服务。','municipal municipality municipally')
W('spectrograph','英 /ˈspektrəɡrɑːf/；美 /ˈspektrəɡræf/','摄谱仪、光谱记录仪',
 '把不同波长的光分开，再把光谱记录下来，好像让光留下自己的指纹。spectrograph 是做这件事的仪器。',
 'spectro- 光谱 + -graph 记录、描记的仪器成分；spectro- 联系 spectrum 光谱，-graph 接希腊写、记录的词源。这里整体不是一张普通统计图。',
 [['拉丁 spectrum 的光谱义 → spectro-','按波长展开的光谱'],['spectro- + -graph → spectrograph','记录光谱的仪器']],
 'a telescope spectrograph 望远镜光谱仪，a high-resolution spectrograph 高分辨率摄谱仪。记录的光谱用于研究光源、物质等，具体性能取决于仪器。',
 'a telescope spectrograph；a high-resolution spectrograph。',
 'spectrograph 侧重记录光谱的仪器；spectrogram 是记录得到的图样。spectrometer 更宽泛说光谱测量仪器，现代设备命名有重叠。',
 ('The telescope’s spectrograph recorded the star’s spectrum.','望远镜的摄谱仪记录了那颗恒星的光谱。'),('The team installed a new spectrograph at the observatory.','团队在天文台安装了一台新摄谱仪。'),sources=['https://en.wiktionary.org/wiki/spectrograph#English','https://science.nasa.gov/asset/hubble/how-a-spectrograph-works/'])
R('A1785','写、描记、记录，以及记录物、设备和动作','-GRAPH：看整词，可能是记录物、仪器，也可能是动词','photograph 照片；spectrograph 记录光谱的仪器；choreograph 编排舞蹈动作。',
 '共同来源指向写、描记，不意味着每个整词都该译成图。随前半对象和词的历史，结果可以是成品、设备或动作。',
 '希腊 gráphein 写、描记，相关 -graphos 等进入学术构词；各词借入、造词路线分别看。',
 [['记录物与记录设备','photograph · autograph · phonograph · polygraph · chronograph · spectrograph'],['记录、编排及相关形式','lithograph · choreograph · orthographic']],
 '-graph 不固定只表示图；spectrograph 仪器与 spectrogram 图样不同。',
 'The spectrograph records a spectrum, while a photograph records a visible scene.\n\n摄谱仪记录光谱，照片则记录可见场景。','photograph autograph phonograph polygraph chronograph spectrograph lithograph choreograph orthographic')
A=[['较早欧洲形式中与任务、差事、服务相关的成分','受派遣、执行使命的人'],['古法语、盎格鲁诺曼语 ambassadeur 等 → 英语 ambassador','正式使节、大使；后来也可说形象代表']]
W('ambassador','英 /æmˈbæsədə/；美 /æmˈbæsədər/','大使；形象代表、推广代表',
 '带着派遣方的身份与使命，到另一方那里代表它，是 ambassador 的主线。国家有大使，品牌、公益活动也会借这个代表形象。',
 '经中古英语 ambassadore、盎格鲁诺曼语 ambassadeur 等借入，较早欧洲词形联系服务、差事、使命。远处路线经历多语言，不按 am + bass + door 拼字硬拆。',A,
 'an ambassador to France 驻法国大使，a brand ambassador 品牌形象代表，a goodwill ambassador 亲善大使。后两者不因名称就自动具备外交职务。',
 'an ambassador to；a brand ambassador；a goodwill ambassador。',
 'ambassador 的外交职位与商业、公益称号要分开。embassy 是大使馆、使团，不是这位代表本人。',
 ('She served as ambassador to several countries.','她曾在几个国家担任大使。'),('The athlete became a goodwill ambassador for the charity.','这位运动员成为该慈善机构的亲善大使。'))
W('ambassadorial','英 /æmˌbæsəˈdɔːriəl/；美 /æmˌbæsəˈdɔːriəl/','大使的；与大使职责有关的',
 '不再说这位大使是谁，而是说某项职责、任命、住所属于大使这个职位，就是 ambassadorial。',
 'ambassador + -ial，形成相关形容词。重音转移到 /dɔː/，不是在 ambassador 原读音后随便附上一个词尾。',A+[['ambassador + -ial → ambassadorial','大使职位、身份或职责相关的']],
 'ambassadorial duties 大使职责，an ambassadorial appointment 大使任命，an ambassadorial residence 大使官邸。正式文体中较常见。',
 'ambassadorial duties；an ambassadorial appointment。',
 'ambassadorial 比 diplomatic 外交的范围窄；一般外交工作、措辞不一定专属大使。',
 ('Her ambassadorial duties included attending official ceremonies.','她的大使职责包括参加正式典礼。'),('The announcement concerned an ambassadorial appointment.','公告涉及一项大使任命。'))
W('ambassadorship','英 /æmˈbæsədəʃɪp/；美 /æmˈbæsədərʃɪp/','大使职务、任期',
 '把担任大使这份职位、任职经历当成一个整体，就是 ambassadorship。不是说一艘载着大使的船。',
 'ambassador + -ship，-ship 在这里表身份、职位、任职状态，与 friendship 等后缀同类，和独立名词 ship 船不同。',A+[['ambassador + -ship → ambassadorship','大使这一职位及任职经历']],
 'an ambassadorship to a country 驻某国大使职务，during her ambassadorship 在她担任大使期间。',
 'an ambassadorship；during her ambassadorship。',
 'ambassador 是人，ambassadorial 是相关性质，ambassadorship 是职位、任职经历；不要只因都能译出大使就互换。',
 ('He accepted an ambassadorship after years in public service.','多年从事公共服务后，他接受了大使职务。'),('The memoir describes her ambassadorship in detail.','回忆录详细讲述了她担任大使的经历。'))
R('B3595','带着使命代表派遣方，以及大使相关职责和职位','AMBASSADOR：受派遣，代表某一方','ambassador 人物 → ambassadorial 相关性质 → ambassadorship 职位、任职。',
 '国家大使是正式外交角色，品牌和公益也借用代表形象的意义。用途扩展不等于职权一样。',
 '经法语、盎格鲁诺曼语等形式借入；现代 ambassador 接 -ial、-ship。',
 [['人物、性质与职位','ambassador · ambassadorial · ambassadorship']],
 'brand ambassador 不自动是外交官；-ship 在此表职位而不是船。',
 'During her ambassadorship, the ambassador carried out many ambassadorial duties.\n\n任大使期间，她履行了许多大使职责。','ambassador ambassadorial ambassadorship')
D=[['古英语 drēahnian → 中古英语 dreinen → drain','逐渐引走液体；联系变干的旧概念'],['实体水流 → 资源、精力的扩展','流走、排走；逐渐耗尽']]
W('drain','/dreɪn/','排水、流走；耗尽；排水口、排水管；消耗资源的事物',
 '水从出口流走，容器逐渐空了；精力、金钱也能像这样不断流失。drain 就连接这两种画面。',
 '承接古英语 drēahnian，经中古英语 dreinen；与 dry、drought 的历史有联系。现代 drain 不能简单按 d + rain 雨拆。',D,
 'drain the sink 排掉水槽里的水，a blocked drain 堵住的排水管，drain resources 消耗资源，go down the drain 白白浪费、付诸东流。',
 'drain away；a blocked drain；a drain on resources；down the drain。',
 'drain 说流出、耗去；flood 说大量涌入、淹没。a drain on time 是不断消耗时间的事，不是字面的时间排水口。',
 ('The water drained slowly from the sink.','水从水槽里慢慢排走。'),('The repeated delays were a drain on our resources.','一再延误不断消耗我们的资源。'))
W('drainage','/ˈdreɪnɪdʒ/','排水；排水系统、排水能力',
 '一块地上的水能不能顺利离开，或靠什么管网离开，都是 drainage 关心的事。它可以说过程，也可以说整套系统。',
 'drain + -age，把排水动作联系到过程、设施等名词。-age 在这里读弱读 /ɪdʒ/，不是独立 age 年龄。',D+[['drain + -age → drainage','排水过程、系统、条件']],
 'good drainage 良好排水，a drainage system 排水系统，poor soil drainage 土壤排水不良。具体强调排水能力还是设施，看搭配。',
 'good drainage；a drainage system；soil drainage。',
 'drain 是单个管道、口，也可作动词；drainage 常把整个排水过程、系统或条件作为一个概念谈。',
 ('These plants need soil with good drainage.','这些植物需要排水良好的土壤。'),('The town upgraded its drainage system.','镇上升级了排水系统。'))
W('drained','/dreɪnd/','排干的、耗尽的；精疲力竭的',
 '像容器里的东西流走了，身体也好像没剩多少劲，便是 feel drained。它强调被耗空后的状态。',
 'drain + -ed，过去分词可作形容词；末尾读 /d/。由液体排走扩到电量、精力耗去。',D+[['drain + -ed → drained','被排走、消耗后的状态']],
 'feel drained 感到精疲力竭，emotionally drained 心力交瘁，a drained battery 电量耗尽的电池。形容人的感受不代表实际生理指标归零。',
 'feel drained；emotionally drained；a drained battery。',
 'drained 是被耗空后的状态；draining 是令人耗力的，an exhausting meeting 可让人 feel drained。',
 ('After the long meeting, she felt completely drained.','开完长会后，她觉得精疲力竭。'),('The drained battery could no longer power the device.','电量耗尽的电池无法再给设备供电。'))
R('B3632','水从容器、土地流走，再借给资源和精力的消耗','DRAIN：从里面流出去，剩下的越来越少','drain → drainage 排水概念、系统；drained 排走、耗尽后的状态；drainpipe 排水管。',
 '名词可以是出口或管道，动词是流走、排走；比喻里则是精力、资源被不断带走。',
 'drēahnian → dreinen → drain；-age 名词，-ed 分词状态；drain + pipe。',
 [['动作、设施与系统','drain · drainpipe · drainage'],['结果状态','drained']],
 'drained 状态与 draining 造成耗力的性质不同；drainage 不只指一根管。',
 'The blocked drainpipe caused poor drainage, and the repair work left everyone drained.\n\n排水管堵塞导致排水不畅，维修工作又让大家疲惫不堪。','drain drainpipe drainage drained')
if __name__=='__main__':save('continuation_20261030_jg',ROOTS,WORDS)
