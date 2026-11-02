"""Media, people, working practices and service organisations."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C1635':dict(words=['video','videos'],label='video → videos：我看与现代视频',note='近代仿 audio 的命名，取拉丁 video 我看；名词、动词用途后来扩展。'),
 'B3611':dict(words=['film','films'],label='film → films：薄膜、胶片与电影',note='本族薄膜词的现代技术扩展，数字时代继续保留旧名称。'),
 'B2932':dict(words=['card','cards'],label='card → cards：纸张、卡片与身份、支付工具',note='法语、拉丁纸张词族借入，实体卡与虚拟卡沿凭证功能扩展。'),
 'B2485':dict(words=['tax','taxes'],label='tax → taxes：评定、征收与负担',note='法语借词接拉丁评定词，现代具体征税与比喻负担按语境解释。'),
 'C1526':dict(words=['return','returns','returning'],label='return → returns → returning：转回、归还与交回的信息',note='法语名动词及相关拉丁形式共同参与历史，现代名词有退货、回报、报表等用途。'),
 'C0564':dict(words=['human','humans'],label='human → humans：人的与人类个体',note='拉丁人类词族经法语借入，形容词也作可数名词。'),
 'B4278':dict(words=['folk','folks'],label='folk → folks：人群、家人和亲切称呼',note='本族人群词延续，现代有集合的 folk 与加 s 的常用 folks。'),
 'C1111':dict(words=['practice','practices'],label='practice → practices：练习、做法与美式动词形式',note='希腊行动材料经拉丁、法语进入英语；英美 practise、practice 的词性拼写习惯分开。'),
 'C0023':dict(words=['agency','agencies'],label='agency → agencies：起作用与替人办事的机构',note='拉丁行动者材料形成抽象名词，现代机构义随后发展。'),
 'C0499':dict(words=['program','programs','programme','programmes'],label='program／programme：公告、节目与一套安排',note='同一历史词的拼写变体，计算机程序常用 program，其他英式语境常用 programme。'),
}
W('videos','英 /ˈvɪdiəʊz/；美 /ˈvɪdioʊz/','视频、录像〔复数〕；录下影像〔第三人称单数〕',
 '把能看的活动画面保存、传给别人，是 videos 的视频义；与 audio 声音相对，video 的近代名字就是借我看这个拉丁形式。',
 'video + -s，元音后读 /z/，结尾是 o 的名词在这里直接加 s。video 近代仿 audio，借拉丁 videō 我看，属于 vidēre 看词族，后有录制品与录影动词。',
 [['拉丁 videō 我看；近代仿 audio → video','视觉部分、图像信号的技术命名'],['video + -s → videos；录制用途','多段视频、录像；单数主语录影']],
 'short videos 短视频；instructional videos 教学视频；watch videos 看视频。',
 'videos stored on the device；videos explaining the steps。','videos 的复数没有 e；potatoes 的复数有 es，o 结尾名词要按具体词记。video 表示影像，audio 更侧重声音。',
 ('The course includes short videos explaining each step.','课程配有短视频，讲解每个步骤。'),('She saved the videos in a separate folder.','她把视频存进单独的文件夹。'),sources=['https://en.wiktionary.org/wiki/videos#English','https://www.etymonline.com/word/video'])
W('films','/fɪlmz/','电影；薄膜、薄层〔复数〕；拍摄〔第三人称单数〕',
 'film 最早的画面是一层薄皮、薄膜；摄影把影像留在感光薄层上，后来便用 films 数电影。拍摄也直接用 film 作动词。',
 'film + -s，/m/ 后读 /z/。继承古英语 filmen 薄皮、膜；感光层、胶片再引出电影和拍摄用法，数字电影沿用这个名称。',
 [['古英语 filmen → film','薄皮、膜 → 摄影感光薄层、胶片'],['电影与动词用途；film + -s → films','多部电影、多层薄膜；单数主语拍摄']],
 'documentary films 纪录片；thin films 薄膜；films interviews 拍摄采访。',
 'films shown at the festival；films covering a surface。','films 不保证今天仍用实体胶片拍，名称会在技术变化后延续。材料科学里的 films 则通常回到薄层、薄膜义。',
 ('The festival shows films from several countries.','电影节放映几个国家的电影。'),('She films interviews for the school website.','她为学校网站拍摄采访。'),sources=['https://en.wiktionary.org/wiki/films#English','https://en.wiktionary.org/wiki/film#English'])
W('cards','英 /kɑːdz/；美 /kɑːrdz/','卡片、纸牌；银行卡、证件卡等〔复数〕',
 '一张张较挺的纸片，是 cards 的具体画面；在上面写信息、印图案，就能用作贺卡、纸牌、身份或支付凭证。',
 'card + -s，/d/ 后读 /z/。经法语 carte 接拉丁 charta、希腊 khártēs 等纸张词，与 chart 有较早同族关系；梳理纤维的同形 card 另有历史。',
 [['希腊、拉丁纸张词 → 法语 carte → card','纸张 → 卡片、凭证'],['card + -s → cards；信息、用途扩展','多张卡；纸牌、证件或支付工具']],
 'playing cards 扑克牌；birthday cards 生日卡片；bank cards 银行卡；a pack of cards 一副纸牌〔英式常见〕。',
 'cards printed on thick paper；cards kept in a wallet。','cards 数单张卡，a pack 或 deck of cards 常数一副纸牌。虚拟卡也沿凭证、信息载体的名称，不要求每张都真是纸片。',
 ('The children made birthday cards for their teacher.','孩子们为老师制作了生日卡片。'),('He put the playing cards back in the box.','他把纸牌放回盒子里。'),sources=['https://en.wiktionary.org/wiki/cards#English','https://en.wiktionary.org/wiki/card#English'])
W('taxes','/ˈtæksɪz/','税、税款〔复数〕；征税；使负担很重〔第三人称单数〕',
 '按一定方式评定后征收的款项，是 taxes 的税款义；给一个人的能力、设备的资源加上重负担，动词也能用 tax。',
 'tax + -es，/ks/ 后增加 /ɪz/。tax 经法语接拉丁 taxāre 评定、估量等词；现代征收义与使承受负担的比喻用途按对象区分。',
 [['拉丁 taxāre → 法语 → tax','评定、估量 → 征收税款'],['tax + -es → taxes；负担比喻','多项税款；单数主语征税或使吃力']],
 'pay taxes 纳税；local taxes 地方税；taxes included 已含税；taxes the system 给系统带来沉重负担。',
 'taxes listed in the statement；taxes the old computer。','taxes 可以泛说多项税款；taxes a person’s patience 这类动词用法则像加上吃力负担。读到税的句子时，具体项目由上下文说明。',
 ('The price includes all taxes.','这个价格包含全部税款。'),('The large file taxes the old computer.','这个大文件让那台旧电脑不堪重负。'),sources=['https://en.wiktionary.org/wiki/taxes#English','https://en.wiktionary.org/wiki/tax#English'])
W('returns','英 /rɪˈtɜːnz/；美 /rɪˈtɜːrnz/','返回、归还〔第三人称单数〕；退货；回报；报表等〔复数〕',
 '人或物转回来，是 returns 的回返画面；商品送回来是退货，付出之后得到的东西可说回报，按要求交回的信息则可以叫 return。',
 'return + -s，/n/ 后读 /z/。动词经古法语 retorner 等及相关中世纪拉丁形式，名词还接法语 retorn 等；现代 re- 回 + turn 的认形不等于名动词只有一条借入路径。',
 [['法语名动词及相关拉丁形式 → return','转回、返回 → 归还、回报等'],['return + -s → returns；按领域专门化','单数主语回来、归还；退货、回报或提交的信息']],
 'returns home 回家；returns the keys 还钥匙；product returns 商品退货；tax returns 纳税申报表。',
 'returns made to the shop；returns from a period of work。','tax returns 通常说提交的申报资料，不等于退税；product returns 则是送回的商品。动词 returns 的对象、方向决定是返回还是归还。',
 ('She returns the keys before leaving the building.','她离开大楼前归还钥匙。'),('The shop keeps a record of product returns.','这家店保留商品退货记录。'),sources=['https://en.wiktionary.org/wiki/returns#English','https://en.wiktionary.org/wiki/return#English'])
W('humans','/ˈhjuːmənz/','人、人类个体〔human 的复数〕',
 '把人作为一种生物、或与机器等对象对照时，常用 humans；它把注意放在人这一类存在，而不是具体身份。',
 'human + -s，/n/ 后读 /z/。古法语 humain 接拉丁 hūmānus 人的，和 homō 人同族；英语形容词也用作可数名词。',
 [['拉丁 homō、hūmānus → 法语 humain → human','人 → 人的、人类的'],['human 名词 + -s → humans','一个个人类个体；合称人类']],
 'humans and animals 人与其他动物；humans and robots 人与机器人；help humans 帮助人。',
 'humans living in the region；designed for humans。','humans 常用于生物、技术等对照；people 说人们更日常。human 与 humane 仁慈的现代意义、重音不同，虽共享较早词族。',
 ('Humans use language to share ideas.','人类用语言交流想法。'),('The machine was designed to work alongside humans.','这台机器被设计为与人协作。'),sources=['https://en.wiktionary.org/wiki/humans#English','https://en.wiktionary.org/wiki/human#English'])
W('folks','英 /fəʊks/；美 /foʊks/','人们、各位〔口语〕；家人、父母〔my folks 等〕',
 '亲切、随意地说一群人，可以用 folks；说 my folks，又常指我的家人，尤其父母。它比正式的 people、parents 更有口语气。',
 'folk + -s，/k/ 后读 /s/，l 在常见读音里不发音。folk 延续古英语 folc 人群、族群，原来就能作集合词；现代 folks 成为常用口语形式。',
 [['古英语 folc → folk','人群、群体'],['folk + -s → folks；亲切称呼与家庭用法','人们、各位；自己的家人、父母']],
 'local folks 当地人；my folks 我的家人、父母；Hi, folks 各位好。',
 'folks living nearby；visiting her folks。','folk music 民间音乐中的 folk 通常用原形修饰；folks 单独作名词常是人们。my folks 的具体家人范围由语境决定。',
 ('The local folks helped us find the old road.','当地人帮我们找到了那条老路。'),('She is visiting her folks this weekend.','她这个周末去看望父母。'),sources=['https://en.wiktionary.org/wiki/folks#English','https://en.wiktionary.org/wiki/folk#English'])
W('practices','/ˈpræktɪsɪz/','做法、惯例；练习、执业机构等〔复数〕；练习〔美式第三人称单数〕',
 '把事情实际做起来、反复做，形成 practices 的练习与做法义；一种经常这样处理事情的方式，也可以数成一项 practice。',
 'practice + -s，/s/ 后增加 /ɪz/。希腊 praktikós 行动相关材料经拉丁 practicāre、法语 pratiser 等进入英语，中古英语有 practisen；名词写法后来形成 practice。',
 [['希腊行动词族 → 拉丁、法语 → 英语 practice 名动词','实际做、反复做 → 练习、做法'],['practice + -s → practices；英美拼写分工','多项做法；美式单数主语练习，英式动词常用 practises']],
 'working practices 工作惯例；good practices 良好做法；practices the piano 练钢琴〔美式〕。',
 'practices used in the classroom；practices speaking each day。','英式名词通常写 practice，动词写 practise，所以名词复数 practices、动词 practises 要分清；美式常都用 practice 及 practices。',
 ('The course compares working practices in different teams.','课程比较不同团队的工作做法。'),('She practices the piano every evening.','她每天晚上练钢琴。'),sources=['https://en.wiktionary.org/wiki/practices#English','https://www.etymonline.com/word/practice'])
W('agencies','/ˈeɪdʒənsiz/','代理机构；机构、部门〔agency 的复数〕',
 '有一群人专门代办、开展某类事务，是 agencies 的机构义；旅行代理、广告机构、公共部门都可按承担的业务命名。',
 'agency 的 y 前是辅音 c，变 y 为 i 加 -es，词尾读 /z/。中世纪拉丁 agentia 来自 agēns、agent- 行动者，英语先有起作用等抽象义，后来发展为代办业务的机构。',
 [['拉丁 agere、agēns → 中世纪拉丁 agentia → agency','行动、起作用 → 办事、施加作用的组织'],['agency → agencies','y 变 i 加 es；多个办事、代理机构']],
 'travel agencies 旅行代理机构；advertising agencies 广告机构；public agencies 公共机构。',
 'agencies sharing information；agencies representing writers。','agency 的机构义不只商业中介，也可用于公共部门。agent 常指执行事务的人或作用物，agency 则可把整个办事组织框起来。',
 ('Local agencies shared information after the storm.','暴风雨后，当地机构共享了信息。'),('The writer contacted several literary agencies.','这位作家联系了几家文学代理机构。'),sources=['https://en.wiktionary.org/wiki/agencies#English','https://www.etymonline.com/word/agency'])
W('programmes','英 /ˈprəʊɡræmz/；美式读音 /ˈproʊɡræmz/','节目；计划、项目；活动安排〔英式复数拼写〕',
 '先把要呈现、要开展的事情排出来，是 programmes 的节目、项目画面。它和 programs 是同一历史词的不同拼写习惯。',
 'programme + -s，/m/ 后读 /z/。法语 programme 经后期拉丁接希腊 prógramma 公告，属于 pro- 在前与写的 gráphein 词族；从公布的内容发展到节目单、安排与项目。',
 [['希腊 prógramma → 拉丁、法语 → programme／program','先公示写出的内容 → 节目、安排'],['programme + -s → programmes','多套节目、项目、计划；英式拼写']],
 'television programmes 电视节目；education programmes 教育项目；training programmes 培训计划。',
 'programmes broadcast each week；programmes offered by the centre。','英式在电视节目、活动安排等语境常写 programme，计算机程序通常也写 program；美式较广地使用 program。programs 与 programmes 的拼写差别不代表两个词根。',
 ('The station broadcasts educational programmes every week.','这家台站每周播出教育节目。'),('The centre offers training programmes for new volunteers.','这个中心为新志愿者开设培训项目。'),sources=['https://en.wiktionary.org/wiki/programmes#English','https://en.wiktionary.org/wiki/programme#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zb',ROOTS,WORDS)
 extend_lessons()
