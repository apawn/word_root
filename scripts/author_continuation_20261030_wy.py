"""Common forms in daily reading: programs, records, prices and comments."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0499':dict(words=['program','programs'],label='program → programs：节目、计划、程序；编程',note='program 接希腊 pro- 加 graphein 的公告词族，经拉丁、法语借入；programs 与 programmes 的使用按地区、领域看。'),
 'C0254':dict(words=['record','records'],label='record → records：记录、唱片；记录下来',note='record 接拉丁 recordārī 记住，历史 re- 与 cord- 心相关；records 名词、动词通常靠重音区分。'),
 'B2669':dict(words=['car','cars'],label='car → cars：汽车与轨道车辆车厢',note='car 经法语接拉丁 carrus 运货车，更早与高卢语车辆词有关；现代汽车义只是后来的主要分支。'),
 'C0401':dict(words=['effect','effects'],label='effect → effects：影响、效果；财物；使实现',note='effect 接拉丁 efficere、effectus 的做出结果词族；effects 可数影响，也见 personal effects 随身物品。'),
 'B2797':dict(words=['law','laws'],label='law → laws：法律；规律、定律',note='law 接古诺尔斯语 lǫg 及确立、放置词族，英语法律与科学定律义分场景看；与 legal 的拉丁来源分别讲。'),
 'C1122':dict(words=['price','prices'],label='price → prices：价格；定价',note='price 经法语 pris／preis 接拉丁 pretium，prices 在 /s/ 后加 /ɪz/，也可作定价动词的第三人称。'),
 'B3138':dict(words=['rate','rates'],label='rate → rates：比率、速度、收费标准；评价',note='rate 的数值词族经法语等接拉丁 rata 核定份额；现代不同率、费率和评分用法按语境区分。'),
 'C0726':dict(words=['comment','comments'],label='comment → comments：评论、意见；发表看法',note='comment 名词、动词有相关但不同的法语、拉丁借入路线，更早联系思索、构想词族。'),
}
W('programs','英 /ˈprəʊɡræmz/；美 /ˈproʊɡræmz/','节目；计划、项目、课程安排；程序；编程、安排〔动词形式〕',
 '先把要做的内容排好、写好，是 program 的共同画面：节目有次序，计划有步骤，电脑程序有给机器的指令。',
 'program + -s，/m/ 后读 /z/。经法语 programme、后期拉丁 programma 接希腊 programma 公告，与 pro- 在前和 graphein 写相关。',
 [['希腊 pro- + graphein 词族 → programma → 拉丁、法语相关形式 → program','公开写出的公告 → 安排、节目等'],['program 名词、动词 + -s → programs','多个节目、计划、程序；单数主语编程、安排']],
 'computer programs 计算机程序；TV programs 电视节目〔美式常见〕；training programs 培训项目；programs the device 给设备编程。',
 'several programs；programs on the computer。','英式常以 programmes 写节目、培训安排等，计算机程序通常仍用 programs；美式广泛用 programs。不同拼写习惯本身不表示功能不同。',
 ('The computer can run several programs at the same time.','这台电脑能同时运行几个程序。'),('The centre offers training programs for new volunteers.','中心为新志愿者提供培训项目。'),sources=['https://en.wiktionary.org/wiki/programs#English','https://en.wiktionary.org/wiki/program#English'])
W('records','名词：英 /ˈrekɔːdz/、美 /ˈrekərdz/；动词：英 /rɪˈkɔːdz/、美 /rɪˈkɔːrdz/','记录、档案；纪录、唱片；记录、录制〔动词形式〕',
 '让信息留下来、以后还能查，是 record。留下的档案是 records；成绩中最好的一项也叫纪录；记录声音的载体又形成唱片义。',
 'record + -s。名词通常重读第一音节，动词通常重读第二音节。经法语接拉丁 recordārī 想起、记住，历史 re- 回、再与 cor／cord- 心相关。',
 [['拉丁 re- + cor／cord- 相关材料 → recordārī → 法语 recorder → record','使记起、记住 → 记下、留下记录'],['record 名词、动词 + -s → records','多份记录、唱片、纪录；单数主语记录、录制']],
 'keep records 保存记录；school records 学籍、校方记录；break records 打破纪录；vinyl records 黑胶唱片；records the temperature 记录温度。',
 'check the records；records every meeting。','the records 中常是名词，she records 中常是动词，重音也常随词性变。a record 是一份记录或一个纪录，recording 常指录制过程或录下的内容。',
 ('The archive keeps records of every performance.','档案馆保存每场演出的记录。'),('The small device records the temperature every hour.','这个小设备每小时记录一次温度。'),sources=['https://en.wiktionary.org/wiki/records#English','https://en.wiktionary.org/wiki/record#English'])
W('cars','英 /kɑːz/；美 /kɑːrz/','汽车；车厢、缆车车厢等；car 的复数',
 '日常最常见的是几辆汽车；铁路、缆车语境里，car 还可以指载人、载货的一节车厢。',
 'car + -s，词尾 /z/。经古法语、盎格鲁诺曼 carre 等接拉丁 carrus 运货车，更早与高卢语车辆名称有关，名称早于现代汽车。',
 [['高卢语相关车辆词 → 拉丁 carrus → 法语 carre 等 → car','运货车辆等 → 后来的各种车、车厢'],['car + -s → cars','多辆汽车；若干节车厢等']],
 'parked cars 停着的汽车；electric cars 电动汽车；rental cars 租来的车；railroad cars 铁路车厢〔美式常见〕；cable cars 缆车。',
 'two cars；cars on the road。','cars 在道路语境通常是汽车，在 a train with six cars 中常是六节车厢。carriages 在许多英式铁路场景也能指客运车厢，搭配随地区、用途变化。',
 ('The street was lined with parked cars.','街道两旁停满了汽车。'),('The train has six passenger cars.','这列火车有六节客运车厢。'),sources=['https://en.wiktionary.org/wiki/cars#English','https://en.wiktionary.org/wiki/car#English'])
W('effects','/ɪˈfekts/','影响、效果；特效；个人财物〔personal effects〕；使实现、促成〔动词形式〕',
 '事情做出来以后带来了什么，是 effects；电影里专门制造的画面、声音效果也是 effects。personal effects 则是固定说法，指个人物品。',
 'effect + -s，/t/ 后读 /s/。拉丁 ex- 向外与 facere 做形成 efficere 做成、产生，其分词 effectus 经借入形成英语 effect。',
 [['拉丁 ex- + facere → efficere／effectus → effect','做出来、产生 → 结果、效果'],['effect 名词、动词 + -s → effects','多个效果、影响；部分固定财物义；单数主语促成']],
 'side effects 副作用、附带影响；sound effects 音效；special effects 特效；personal effects 个人财物；effects a change 促成改变。',
 'the effects of a change；effects on the result。','effects 常是名词效果、影响，affects 常是影响的动词第三人称。effect 也能作较正式动词使实现，如 effects a change，不能简单说它永远只作名词。',
 ('The film uses simple sound effects to create tension.','这部电影用简单音效制造紧张感。'),('The small change had noticeable effects on the final result.','这个小改动对最终结果产生了明显影响。'),sources=['https://en.wiktionary.org/wiki/effects#English','https://en.wiktionary.org/wiki/effect#English'])
W('laws','英 /lɔːz/；美 /lɔːz, lɑːz/','法律、法令；规律、定律；law 的复数',
 '社会中确立下来的规则是 laws；描述自然关系的定律，也用 laws。前者说社会规范，后者说被总结出来的自然关系。',
 'law + -s，元音后读 /z/。law 借古诺尔斯语 lǫg，原为 lag 放置、层次等材料的复数，经古英语 lagu 进入英语；现代再有英语复数 laws。',
 [['古诺尔斯语 lag／复数 lǫg → 古英语 lagu → law','确立、放置的旧词族 → 法律、规则'],['英语 law + -s → laws','多项法律；自然规律、定律等']],
 'national laws 国家法律；laws of nature 自然规律；physical laws 物理定律；laws and regulations 法律法规。',
 'the laws of physics；several different laws。','law 与 legal 的意义相近，来路不同：law 主要接北欧词，legal 接拉丁 lex／legis。the law 可概括法律体系，laws 则可数一条条法律、定律。',
 ('The museum display explains several laws of physics.','博物馆展板解释了几条物理定律。'),('The book compares how the laws changed over time.','这本书比较了法律随时间发生的变化。'),sources=['https://en.wiktionary.org/wiki/laws#English','https://en.wiktionary.org/wiki/law#English'])
W('prices','/ˈpraɪsɪz/','价格、价钱〔复数〕；给……定价〔price 的第三人称单数〕',
 '一件件东西标多少钱，是 prices；给东西定下价格，price 又可以作动词。',
 'price 已有 e，加 s；原词 /s/ 后增加 /ɪz/。经古法语 pris、preis 接拉丁 pretium 价值、价格、奖赏等材料。',
 [['拉丁 pretium → 古法语 pris／preis → price','价值、价格；相关奖赏义后来分化'],['price 名词、动词 + -s → prices','多项价格；单数主语定价']],
 'compare prices 比较价格；ticket prices 票价；rising prices 上涨的价格；prices the books individually 给每本书单独定价。',
 'lower prices；prices for the same item。','prices 说商品、服务标多少钱，costs 常说为得到、做出它付出的费用。两者可能是同一笔钱的不同视角，也可能是售价与生产成本的区别。',
 ('The two shops charge different prices for the same notebook.','同样的笔记本，两家店的售价不同。'),('The owner prices each used book separately.','店主给每本旧书分别定价。'),sources=['https://en.wiktionary.org/wiki/prices#English','https://en.wiktionary.org/wiki/price#English'])
W('rates','/reɪts/','比率、速度、频率、收费标准；评定、认为〔rate 的第三人称单数〕',
 '把某种数量放到统一尺度上看，是 rate：每小时做多少、每次收多少钱，都可以有 rates。作动词时，又能把某物放到评价尺度上。',
 'rate 已有 e，加 s，/t/ 后读 /s/。数值词经法语等接拉丁 rata 核定份额，与 reri 计算、判断相关；现代比较、评价等用法沿对应词族发展。',
 [['拉丁 rata／reri 相关词族 → 法语等 → rate','核定份额、计算判断 → 比率、收费等'],['rate 名词、动词 + -s → rates','多个率、收费标准；单数主语评价、认为']],
 'hourly rates 按小时的收费；growth rates 增长率；heart rates 心率；rates the service 评价服务；rates highly 评价很高〔看句式〕。',
 'different rates；rates for weekend bookings。','rates 常按单位时间、次数或比例说明，prices 更直接说要付的价钱。the hotel rates 可说酒店收费标准，rates the hotel 则是给酒店作评价。',
 ('The two machines work at different rates.','这两台机器的工作速度不同。'),('She rates this guide as the most useful of the three.','她认为这份指南是三份中最实用的。'),sources=['https://en.wiktionary.org/wiki/rates#English','https://en.wiktionary.org/wiki/rate#English'])
W('comments','/ˈkɒments/〔英〕；/ˈkɑːments/〔美〕','评论、意见、说明；发表评论〔comment 的第三人称单数〕',
 '看完、听完某事，补上一段看法或解释，就是 comments。它可以是网页留言，也可以是对文章、方案的反馈。',
 'comment + -s，/t/ 后读 /s/。名词经法语 coment 或后期拉丁 commentum，动词另接 commentare、commentari 等相关形式，更早与思索、构想词族相连。',
 [['后期拉丁 commentum、相关动词及法语 coment → comment','思索形成的说明、评论；名词与动词相关借入路线'],['comment 名词、动词 + -s → comments','多条意见、留言；单数主语发表评论']],
 'leave comments 留评论；comments on the draft 对草稿的意见；helpful comments 有帮助的反馈；comments on ... 评论……。',
 'read the comments；comments on the design。','comments 可以是中性的说明、评价，也可以是批评，要看内容。comment on something 是评论某事；a comment about something 也可用来引出评论对象。',
 ('Your comments helped me improve the introduction.','你的意见帮助我改进了开头。'),('She comments on the draft before it is sent to the whole group.','草稿发给全组前，她先提出意见。'),sources=['https://en.wiktionary.org/wiki/comments#English','https://en.wiktionary.org/wiki/comment#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wy',ROOTS,WORDS)
 extend_lessons()
