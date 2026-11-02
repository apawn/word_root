"""Pledges, pay and wagers; a head of ten becomes a dean."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3009':dict(words=['wed','wedding','wage','wages','waged','waging','wager','wagers'],label='wage → wages → waged → waging；wager → wagers：担保、报酬与打赌',note='wed 是本族延续，wage、wager 经法语借回，较早同接日耳曼承诺、担保词族；wager 的 er 不是现代人物后缀。'),
 'C0307':dict(words=['dean','deans'],label='dean → deans：十人之长到院长',note='拉丁 decanus 十人之长经法语演变，现代机构职务不再要求十人。'),
}
W('wage','/weɪdʒ/','工资、工钱；开展、进行〔战争、斗争等〕',
 '为提供劳动、服务而得到的报酬，是 wage 最常见的名词义。它较早和担保、报酬这一组词义相连；动词 wage war 则是另一个必须连搭配记的用途。',
 '名词经盎格鲁法语、古北法语 wage 报酬、担保，接重构法兰克语 *wadja- 或相关日耳曼来源，与本族 wed 的承诺词族同源。动词经法语 wagier 担保，后有开展战争义。',
 [['日耳曼承诺、担保词族 → 法语 wage、wagier','担保、报酬；许诺、担保'],['法语词借入英语 wage → 各支现代用途','劳动报酬；wage war 开展战争或斗争']],
 'an hourly wage 时薪；a weekly wage 周薪；a living wage 维持基本生活的工资；wage a campaign 开展一场运动。',
 'earn a wage 领工资；wage war 发动、进行战争。','wage 常给一种工资标准、某人的工钱，wages 也很常见。wage war 按开展战争理解；它接较早应战、从事战斗的动词发展，具体语义转移有可能性分析。',
 ('The job offers a reasonable hourly wage.','这份工作的时薪还算合理。'),('The group plans to wage a campaign against waste.','这个团体计划开展反对浪费的宣传行动。'),sources=['https://en.wiktionary.org/wiki/wage#English','https://www.etymonline.com/word/wage'])
W('wages','/ˈweɪdʒɪz/','工资、工钱〔复数〕；开展、进行〔第三人称单数〕',
 '持续工作换来的报酬，日常常用 wages 来谈。若后面接 war、campaign，则可能是单数主语正在开展某种斗争的动词。',
 'wage + -s，/dʒ/ 后增加 /ɪz/。名词、动词分别接法语报酬、担保及许诺等相关词，共同远接日耳曼承诺词族，和英语 wed 同源但借入路线不同。',
 [['日耳曼承诺词族 → 法语 → wage','担保、报酬 → 工钱；动词后发展开展义'],['wage + -s → wages','工资、工钱；单数主语开展斗争等']],
 'pay wages 发工资；higher wages 更高工资；weekly wages 每周工钱。',
 'wages for the extra work 额外工作的报酬；wages a campaign 开展行动。','工资义常按复数配谓语：Wages are rising。a wage 指一种工资水平、一个人的工资标准；salary 常指约定的固定薪资，用途有重叠。',
 ('The workers received their wages on Friday.','工人在周五领到了工资。'),('The report compares wages in different industries.','报告比较不同行业的工资。'),sources=['https://en.wiktionary.org/wiki/wages#English','https://www.etymonline.com/word/wage'])
W('waged','/weɪdʒd/','开展了、进行了〔战争或斗争等；过去式、过去分词〕',
 '把一场战争、斗争或持续行动真正展开，是 waged 常见的意思。它常带正式语气，突出持续投入力量。',
 'wage + -d，/dʒ/ 后读 /d/，不添一个 /ɪd/ 音节。动词较早接法语 wagier 担保、许诺，开展战斗义可能与旧时应战承诺用途相连；现代常用 wage war、wage a campaign。',
 [['法语 wagier → 动词 wage','担保、许诺 → 后来开展战争、斗争'],['wage 去 e + -ed → waged','过去开展；某场斗争被持续进行']],
 'waged war 进行了战争；waged a campaign 开展了一场运动；a struggle waged over years 多年开展的斗争。',
 'waged a campaign for cleaner rivers 发起并开展改善河流的运动；war waged on the border 边境上进行的战争。','waged 是动词过去形式；工资复数是 wages。waged a campaign 常说明有组织地持续推动，不只是完成一次单独行动。',
 ('The residents waged a campaign for a safer road.','居民为争取更安全的道路开展了一场行动。'),('The book describes a long struggle waged by local communities.','这本书描述当地社区进行的一场长期斗争。'),sources=['https://en.wiktionary.org/wiki/waged#English','https://www.etymonline.com/word/wage'])
W('waging','/ˈweɪdʒɪŋ/','开展、进行〔战争、斗争等；现在分词、动名词〕',
 '持续把力量投进一场斗争或行动，是 waging。常和 war、campaign、battle 一起出现，读到时先抓开展这件事。',
 'wage 去末尾 e + -ing → waging，g 在 i 前仍读 /dʒ/。底词动词经法语 wagier 担保、许诺，开展战争的用途后来发展，与工资名词有相关而不同的使用史。',
 [['法语 wagier → wage 动词','担保、应诺相关旧义 → 开展斗争'],['wage 去 e + -ing → waging','正在进行；持续投入某场行动']],
 'waging war 进行战争；waging a campaign 开展运动；waging a battle against pollution 与污染作斗争。',
 'waging a campaign for change 为改变而持续开展行动；the cost of waging war 进行战争的代价。','waging 常是正式、强烈的开展，不是所有日常做事都要用它。waging a campaign 与 earning wages 的语法、搭配不同。',
 ('The community is waging a campaign to save the old theatre.','社区正在开展挽救老剧院的行动。'),('The article examines the cost of waging war.','文章分析进行战争的代价。'),sources=['https://en.wiktionary.org/wiki/waging#English','https://www.etymonline.com/word/wage'])
W('wager','英 /ˈweɪdʒə/；美 /ˈweɪdʒər/','赌注、打赌；敢说、确信〔动词〕',
 '拿出一份东西，为一个尚未确定的结果作保证，就是 wager 的打赌画面。口语说 I’d wager...，也常只是带把握地说“我敢说……”。',
 '名词借盎格鲁法语 wageure、古北法语 wagiere 担保、保证，接 wagier 许诺、担保，与 wage 同族。英语动词后来由名词发展；词尾 er 不是表示人的现代英语 -er。',
 [['法语 wageure、wagiere → wager 名词','担保、押上的东西 → 赌注、打赌'],['英语名词 → wager 动词','打赌；引申为有把握地说']],
 'make a wager 打赌；a wager on the result 对结果下的赌注；I’d wager that... 我敢说……。',
 'a friendly wager 朋友间的一次打赌；wager a small amount 押上一小笔钱。','bet 是更常见、口语的打赌词；wager 稍正式。I’d wager 后的判断不一定真押东西，常是表达很有把握的说法。',
 ('They made a friendly wager on who would arrive first.','他们开玩笑地打了个赌，看谁会先到。'),('I’d wager that she has already solved the problem.','我敢说她已经解决这个问题了。'),sources=['https://en.wiktionary.org/wiki/wager#English','https://www.etymonline.com/word/wager'])
W('wagers','英 /ˈweɪdʒəz/；美 /ˈweɪdʒərz/','赌注、打赌〔复数〕；打赌、敢说〔第三人称单数〕',
 '把一次次押下的保证、赌注分别数出来，是名词 wagers；某个人把话说得像敢为它押注，则也能用动词 wagers。',
 'wager + -s，末尾读 /z/。wager 经法语担保名词进入英语，共同远接日耳曼承诺词族；英语后有动词，名词复数与动词单数变化重合。',
 [['法语担保词 → wager 名词 → 动词','押上的保证 → 赌注、打赌、敢说'],['wager + -s → wagers','多个赌注；单数主语打赌或有把握地说']],
 'small wagers 小额赌注；wagers on the result 针对结果的赌注；wagers that... 敢说、打赌说……。',
 'record the wagers 记录赌注；wagers he can finish 他打赌自己能完成。','wagers 是赌注、打赌这一族，wages 才是工资或 wage 动词的单数形式。两者相连的是更早词史，现代拼写、读音都要分清。',
 ('The story records several wagers made by the two friends.','故事记述了这两位朋友打过的几个赌。'),('He wagers that the team will finish before noon.','他打赌说团队能在中午前完成。'),sources=['https://en.wiktionary.org/wiki/wagers#English','https://www.etymonline.com/word/wager'])
W('dean','/diːn/','学院院长；大学某事务负责人；某些教会的主持职务；资深者',
 '一个群体里担任主管、主持事务的人，是 dean 常见的角色。大学里可以管一个学院，也可以管学生事务等，不一定是整所大学的最高负责人。',
 '经中古英语、盎格鲁诺曼语 deen、古法语 deien 接拉丁 decānus 十人之长。这个十的材料有拉丁 decem 构词、希腊 dekanos 联系等不同分析；较后的法语到英语主线清楚。',
 [['古典十的词族 → 拉丁 decānus','十人之长；后有教会群体主持职务'],['法语 deien、deen → 英语 dean','教会职务 → 大学院长、事务主管；资深成员']],
 'dean of the faculty 学院院长；dean of students 学生事务主管；the dean of the diplomatic corps 外交使团团长。',
 'meet the dean 与院长见面；the dean’s office 院长办公室。','dean 的具体职权依机构而定。现代按职务或资历理解，不限定人数；dean of students 常侧重学生事务，不能简单当成一个学科院长。',
 ('The dean welcomed the new students to the faculty.','院长欢迎新生来到学院。'),('She arranged a meeting with the dean of students.','她安排了与学生事务主管的会面。'),sources=['https://en.wiktionary.org/wiki/dean#English','https://en.wiktionary.org/wiki/decanus#Latin','https://www.etymonline.com/word/dean'])
W('deans','/diːnz/','学院院长、大学事务主管；教会主持人员、资深成员〔复数〕',
 '不同学院或不同事务各有一位负责人，把这些 dean 放在一起，就是 deans。它数的是职务承担者，具体管什么仍看后面的说明。',
 'dean + -s，/n/ 后读 /z/。dean 经法语 deien、deen 接拉丁 decānus 十人之长，后来在教会、大学和资深成员称呼中扩展；现代复数只加英语 -s。',
 [['拉丁 decānus → 法语 → dean','十人之长 → 某群体主管或资深成员'],['dean + -s → deans','多位院长或承担相应职务的人']],
 'deans of several faculties 几个学院的院长；a meeting of deans 院长会议；deans and department heads 院长和系负责人。',
 'university deans 大学院长或事务主管；deans attending the event 参加活动的院长们。','一所大学可以有多位 deans，负责不同学院、事务。heads of department 通常是系负责人，与 dean 的组织层级关系看本校安排。',
 ('The deans met to discuss the new teaching programme.','院长们开会讨论新的教学计划。'),('Several deans attended the welcome event.','几位院长参加了欢迎活动。'),sources=['https://en.wiktionary.org/wiki/deans#English','https://en.wiktionary.org/wiki/dean#English','https://www.etymonline.com/word/dean'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
 import json
 from pathlib import Path
 p=Path(__file__).resolve().parents[1]/'content/精讲/roots_continuation_20261030_bz.json'
 rows=json.loads(p.read_text())
 lesson=next(x for x in rows if x['id']=='B3009')
 lesson.update(
  meaning='承诺、担保；结婚、报酬与赌约的同源背景',
  core='先把话或某件东西押在那里，表示会兑现',
  image='同一承诺词族分成三路：wed 以承诺结合；wage 是报酬；wager 是押上的赌约。',
  intro='较早共同背景是日耳曼语的承诺、担保。wed 通过古英语传下，wage、wager 则经过法语进入英语。现代意思已经分开：婚姻承诺、劳动报酬、为不确定结果押下一份保证。它们是同源的不同路线，不能拿一个现代词直接替换成另一个。',
  contrasts='wedding 是婚礼仪式，marriage 是婚姻关系；wages 是工资，wagers 是赌注或打赌。wage a campaign 是开展行动，wager that... 是打赌、敢说某事。',
  practice='用三个场景接住这条词族：新人举办 wedding；工人领 wages；朋友为谁先到打一个 wager。每个现代词的实际搭配分别记。')
 lesson['sources']=list(dict.fromkeys(lesson.get('sources',[])+['https://www.etymonline.com/word/wed','https://www.etymonline.com/word/wage','https://www.etymonline.com/word/wager']))
 p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':
 save('continuation_20261030_zm',ROOTS,WORDS)
 extend_lessons()
