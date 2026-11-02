"""Lot, public and men: everyday grammatical and historical branches."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
LO=[['古英语 hlot → 中古英语 lot','签、抽签决定；分得的一份、命运'],['英语 lot','份、批、地块；固定短语里表示许多']]
W('lot','英 /lɒt/；美 /lɑːt/','一份、一批；地块；命运；许多',
 '旧时抽签分给谁一份，那一份就是他的 lot；后来还指一批东西、一块地，以及大量的一份。',
 '继承古英语 hlot，旧有抽签、份额、决定等义，经中古英语发展。a lot of 的许多是固定数量表达，不是现代把大量拆成 a + lot 两个新词根。',LO,
 'a lot of books 很多书，lots of time 很多时间；a parking lot 停车场，an auction lot 一批拍卖品。one’s lot in life 是一个人的命运、处境，draw lots 是抽签。',
 'a lot of；lots of；the whole lot；a vacant lot；draw lots；one’s lot in life。',
 'a lot、lots 可修饰可数或不可数名词，但动词跟后面实际名词：a lot of people are，a lot of water is。不要合写 alot。',
 ('A lot of people came to the opening.','很多人参加了开幕活动。'),('They turned the vacant lot into a small garden.','他们把那块空地改成了一座小花园。'),('We drew lots to decide who would go first.','我们抽签决定谁先来。'))
W('sandlot','英 /ˈsændlɒt/；美 /ˈsændlɑːt/','供孩子玩耍的空地；非正式球场',
 '不必有看台和标准设施，一块空地就能让孩子组织自己的比赛。',
 'sand 沙 + lot 地块，形成空地名称；美式常与孩子、业余棒球等非正式活动相联，不要求所有场地都是真正沙地。',C('sand 沙地意象','lot 地块','sandlot','供孩子玩耍、打球的空地'),
 'sandlot baseball 空地上的非正式棒球活动；a sandlot game 常强调自行组织、设施简单的比赛。',
 'sandlot baseball；a sandlot game；play on a sandlot。',
 'sandlot 不是正式体育场 stadium，也不等于儿童沙坑 sandbox；名称已带非正式活动背景。',
 ('The children played baseball on a sandlot behind the houses.','孩子们在房屋后面一块空地上打棒球。'),('He first learned the game through informal sandlot matches.','他最早通过空地上的非正式比赛学会了这项运动。'))
W('feedlot','英 /ˈfiːdlɒt/；美 /ˈfiːdlɑːt/','牲畜集中育肥场',
 '一片专门集中饲养、喂养牲畜的场地，常用于育肥。',
 'feed 喂养、饲料 + lot 场地，形成农业、畜牧业名称。不是只放饲料的一批货。',C('feed 喂养、饲料','lot 场地','feedlot','集中饲养、育肥牲畜的场所'),
 'a cattle feedlot 牛育肥场；feedlot operations 集中育肥经营。常见于北美畜牧报道，但并非所有农场都属于 feedlot。',
 'a cattle feedlot；feedlot management；a large feedlot。',
 'pasture 是放牧草地，feedlot 常强调集中喂养、育肥场地；两者不是随便互换的地貌名词。',
 ('The report compares pasture systems with feedlot systems.','报告比较了放牧体系和集中育肥体系。'),('The farm expanded its cattle feedlot last year.','农场去年扩大了牛育肥场。'))
R('B4061','份额、批；地块；许多与命运的固定用法','LOT：分得的一份，也能是一块地、一批货','抽签、份额和处境提供旧背景；现代 a lot of 先按固定数量表达掌握。',
 'lot 接古英语 hlot，含签、抽签决定、分得份额等义。sandlot、feedlot 取地块、场地一面，不是很多沙、很多食物。',
 'lot → sandlot、feedlot；a lot of、lots of、draw lots 在基础词里对照。',
 [['份、批、命运及数量表达','lot'],['不同用途的场地','sandlot · feedlot']],
 'a lot of people are；a lot of water is。sandlot 是玩耍空地，feedlot 是牲畜集中育肥场。',
 'A lot of children played on the vacant lot after school.\n\n放学后，很多孩子在那块空地上玩。',
 'lot sandlot feedlot')
PU=[['拉丁语 pūblicus → 法语、英语 public','与人民、共同体有关；公共的'],['英语 public 词族','公共、公开；宣传、公众相关职业及否定形式']]
W('publicise','/ˈpʌblɪsaɪz/','宣传；使广为人知',
 '把消息放到更多人面前，让公众知道。',
 'public + 动词后缀 -ise；与 publicize 是同词的拼写变体。英式常见 -ise，美式通常写 -ize，英式也可使用 -ize。',PU+[['public + -ise → publicise','公开、公众相关 → 向公众传播消息']],
 'publicise an event 宣传活动；publicise the results 让结果广为人知。可通过报道、通知等，不只限于付费广告。',
 'publicise an event；widely publicised；publicise the findings。',
 'publicise 让人知道，publish 正式发布、出版；publicise a book 可以是宣传一本已出版的书。',
 ('The library used posters to publicise the reading festival.','图书馆用海报宣传阅读节。'),('The researchers decided to publicise their findings.','研究人员决定让研究结果广为人知。'),sources=['https://en.wiktionary.org/wiki/publicise#English','https://dictionary.cambridge.org/us/dictionary/english/publicize'])
W('publican','/ˈpʌblɪkən/','酒馆经营者；历史语境另可指包税人、税吏',
 '现代英国场景里，常是经营 public house，也就是酒馆的人。',
 '酒馆经营者义通常联系到 public house 或 public + -an，可能起初带幽默色彩；历史税吏义另接拉丁语 pūblicānus，不能把现代酒馆老板一概解释成收税人。',PU+[['public house 相关命名；另有拉丁语 pūblicānus 的历史分支','酒馆经营者；另有古代包税人、税吏用法']],
 'the local publican 当地酒馆老板；现代英式人物报道中常见。读古罗马、宗教旧译文时，publican 可能是税吏，时代与语境决定意思。',
 'a local publican；a retired publican；the publican of the village pub。',
 'publican 不是 politician 政治人物，也不是所有公共部门雇员。pub 是 public house 的缩写，不要与 publisher 出版者混淆。',
 ('The publican knew most of the regular customers by name.','酒馆老板叫得出大多数常客的名字。'),('The novel’s inn is run by a cheerful publican.','小说里的酒馆由一位开朗的老板经营。'))
W('nonpublic','英 /ˌnɒnˈpʌblɪk/；美 /ˌnɑːnˈpʌblɪk/','不公开的；非公共的',
 '范围没有向所有公众敞开，可能只供某群人使用或了解。',
 'non- 非、不 + public 公共、公开的；是否不对外开放，还是不属公共部门，取决于后面的对象。',PU+[['non- + public → nonpublic','非公共、未公开的']],
 'nonpublic information 未公开信息；a nonpublic meeting 不对公众开放的会议。词本身不证明内容违法，也不保证一定属于个人隐私。',
 'nonpublic information；nonpublic records；a nonpublic session。',
 'nonpublic 只是对 public 的否定；private 在不同语境还可有个人的、私人所有等意义，两者不是所有地方完全等同。',
 ('The draft remained nonpublic until the review was complete.','评审完成前，草案一直未公开。'),('The museum stores some nonpublic records in its archive.','博物馆档案室保存着一些不公开的记录。'))
R('B3599','公共、公开；公众相关活动与人物','PUBLIC：公众看得见、能参与，还是共同体所有','public 的公共与公开几种用法分开掌握，再看宣传、职业称呼和否定形式。',
 'public 经法语接拉丁语 pūblicus，与人民、共同体有关。publican 酒馆义与 public house 有关，税吏义另有历史拉丁词背景。',
 'public → publicly、publicity、publicist；publicize / publicise 是拼写变体；publican、nonpublic 各看具体语境。',
 [['公开方式、宣传及职业','public · publicly · publicity · publicist · publicize · publicise'],['人物称呼与否定','publican · nonpublic']],
 'publicise 宣传不等于 publish 出版；publican 常是酒馆老板；nonpublic 不等于违法。',
 'The publican helped publicise the public meeting, while the draft remained nonpublic.\n\n酒馆老板帮助宣传公开会议，而草案当时仍未对外公布。',
 'public publicly publicity publicist publicize publicise publican nonpublic')
ME=[['古英语 mann 的复数 menn → 中古英语 men','人、男子的复数；保留旧元音变化'],['英语 men，单数 man','通常为成年男子的复数；旧材料也可泛称人类']]
W('men','/men/','成年男子们；man 的不规则复数',
 '一个是 man，多个人是 men；变化藏在元音里，而不是靠结尾加 s。',
 '接古英语复数 menn，属于 man 的历史元音变化复数。men 不是独立的前后缀，也不是看到 men 都能任意从单词里拆出来。',ME,
 'two men 两名男子；men and women 男性与女性。旧文学、历史材料可用 men 泛称人类，现代中性表达一般用 people、humanity 等更清楚。',
 'two men；men and women；a group of men；men’s clothing。',
 'men 已是复数，所有格通常 men’s；人的复数不写 mans。man 作动词时的 mans 则是另一种语法情况。',
 ('Two men were waiting outside the museum.','两名男子在博物馆外等候。'),('The course is open to both men and women.','这门课向男性和女性都开放。'))
W('menswear','英 /ˈmenzweə/；美 /ˈmenzwer/','男装',
 '不是指某几个男人正在穿的衣服，而是以男性为主要目标顾客的服装类别。',
 '由 men’s wear 男子穿戴的服装合写成 menswear；中间 /z/ 保留所有关系的读音，词里不再写撇号。',C('men’s 男子的','wear 穿戴物','menswear','男装类别'),
 'a menswear department 男装部；a menswear designer 男装设计师。商业分类说明主要设计、销售对象，不是在规定每个人能穿什么。',
 'a menswear collection；a menswear designer；the menswear department。',
 'menswear 通常不可数；two menswear 不表示两件男装，具体说 two shirts、two items of menswear。',
 ('She designs menswear for a small fashion label.','她为一个小型时装品牌设计男装。'),('The menswear department is on the second floor.','男装部在二楼。'))
W('menfolk','英 /ˈmenfəʊk/；美 /ˈmenfoʊk/','某家庭、社区等中的男人们',
 '把某群体里的男性合在一起说，带一些生活化、乡土或旧式语气。',
 'men 男子们 + folk 人们，形成群体称呼；folk 不只是民歌中的民间。',C('men 男子们','folk 人们','menfolk','某群体中的男人们'),
 'the menfolk of the village 村里的男人们；叙事中常说一个家庭或社区中的男性。这个词比较有语体色彩，不是所有正式统计里的首选。',
 'the village menfolk；the family’s menfolk；among the menfolk。',
 'menfolk 是群体说法，不说明他们天生都承担同一职责；中性统计、通用描述往往直接用 men。',
 ('The novel follows the village’s menfolk through a time of change.','小说讲述村里男性在变革时期的经历。'),('Several of the family’s menfolk arrived together for the reunion.','家里的几位男性成员一起到达团聚现场。'))
R('B2681','men：man 的复数；男装和群体称呼','MEN：复数在元音里，所有关系再看 men’s','先掌握 man → men，再看 men’s wear 如何合写成 menswear，以及 folk 怎样表示群体。',
 'men 接古英语 menn，是保留的历史复数形式。它不是英语中所有 men 字母串的统一词根。',
 'man → men；men’s wear → menswear；men + folk → menfolk。',
 [['不规则复数','men'],['衣物与群体称呼','menswear · menfolk']],
 'men 已经复数；所有格 men’s。menswear 合写后不带撇号，但保留 /z/ 的读音。',
 'The men discussed the new menswear collection in the shop.\n\n几位男子在店里讨论新一季男装。',
 'men menswear menfolk')
for item in WORDS:
 if item['word']=='publican':item['sources'].append('https://www.etymonline.com/word/publican')
if __name__ == '__main__':save('continuation_20261029_cc',ROOTS,WORDS)
