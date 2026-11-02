"""Color and foreknowledge; organize existing common lessons into complete base pages."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
CL=[['拉丁 color → 法语 colour、colur → 英语 color、colour','颜色；英美常见拼写不同'],['现代 color','颜色；涂色；使判断带上某种倾向']]
W('colored','英 /ˈkʌləd/；美 /ˈkʌlərd/','有颜色的、彩色的；着色的；受某种感情影响的',
 '原本纸、水或判断被带上一层颜色；看得见的颜色和情绪滤镜都能这样理解。',
 'color + -ed；英式常拼 coloured。既可分词说被涂色，也可形容有颜色；修饰判断的用法接 color 影响、使带倾向的动词义。',CL+[['color + -ed → colored','有颜色、经着色；比喻受感情影响']],
 'colored paper 彩纸，colored glass 彩色玻璃，a view colored by anger 被愤怒影响的看法。作英美当代族群称呼时，colored 常有过时、冒犯意味，不能当普通彩色义照搬称人。',
 'colored paper；colored glass；colored by experience。',
 'colored 有颜色或被着色，colorful 常多彩、鲜明；colored paper 可以只有一种颜色，colorful display 往往是很多色彩。',
 ('The children cut shapes from colored paper.','孩子们用彩纸剪出各种形状。'),('His judgment was colored by his earlier experience.','他的判断受到先前经历的影响。'))
W('colorist','英 /ˈkʌlərɪst/；美 /ˈkʌlərɪst/','配色、上色师；擅长用色的画家；染发师〔依行业〕',
 '专门把颜色安排、调配、做出来的人：漫画上色、绘画用色、头发染色都可有这个角色。',
 'color + -ist，按用色、配色工作或专长命名。具体职业范围看行业，不是指某人身体有颜色。',CL+[['color + -ist → colorist','用色专家、上色或染色人员']],
 'a comic-book colorist 漫画上色师，a skilled colorist 擅用色者，a hair colorist 染发师。',
 'a comic-book colorist；a skilled colorist；a hair colorist。',
 'colorist 说用色角色，illustrator 插画师说创作插画；同一人可兼任，但一幅漫画的线稿和上色也可分工。另有肤色歧视语境的用法，需随上下文辨别。',
 ('The colorist gave each scene a different mood.','上色师给每个场景配出了不同氛围。'),('She asked the hair colorist for a softer shade.','她请染发师选一个更柔和的色调。'))
W('colorway','英 /ˈkʌləweɪ/；美 /ˈkʌlərweɪ/','配色；某款产品的一套颜色版本',
 '鞋的款式一样，一双蓝白、一双黑金，是不同 colorways；看的是同一设计怎样配颜色。',
 'color + way 方式，固定用于纺织、时尚、产品等的配色版本。英式也可见 colourway，不是通向颜色的一条真实道路。',CL+[['color + way → colorway','一个设计采用的具体颜色组合、版本']],
 'a new colorway 新配色，available in three colorways 有三套配色可选。',
 'a new colorway；three colorways；a limited colorway。',
 'color 可能单一颜色，colorway 常整套搭配；palette 调色板、色彩体系范围更广，不必对应同款产品版本。',
 ('The shoes are available in three colorways.','这款鞋有三套配色可选。'),('The new colorway combines dark green with cream.','新配色把深绿与奶油色组合在一起。'))
R('B2448','颜色、着色与配色；人物和产品版本分清','COLOR：看到的颜色，也可给判断染上倾向','已有 color 与常见 colorful、colourless 等先读；colored、colorist、colorway 分状态、人员和版本。',
 'color/colour 是常见英美拼写对应，派生中同样有对应。不是每个有颜色的对象都色彩缤纷。',
 'color + -ed/-ful/-ist/way；colour + -less；multi- + color；discolor 有借入历史。',
 [['颜色、状态和否定','color · colored · colorful · colourless · discolor'],['多色、配色人员与版本','multicolor · colorist · colorway']],
 'colored 可以一种颜色，colorful 常多彩；colorist 上色人员，colorway 产品配色；称人 colored 有语域问题。',
 'The colorist chose a colorful new colorway for the design.\n\n配色师为设计选了一套鲜明的新配色。',
 'color colored colorful colourless discolor multicolor colorist colorway')
KN=[['中古英语 knowleche 等 → knowledge','知道、认识形成的名词；结尾不是现代 -edge'],['fore- + knowledge → foreknowledge','事情发生前就已有的知识、了解']]
W('foreknowledge','英 /fɔːˈnɒlɪdʒ/；美 /fɔːrˈnɑːlɪdʒ/','预知；事先知情',
 '事情还没发生，你已经知道会是什么；侧重先前知晓，不只猜测。',
 'fore- 预先、在前 + knowledge 知识。前缀说明知晓发生在事情前面，不能只因自己担心未来就叫 foreknowledge。',KN,
 'foreknowledge of events 对事件的预知，with no foreknowledge 毫不事先知情。可见于小说情节、哲学、日常说明。',
 'foreknowledge of；with no foreknowledge；have foreknowledge。',
 'foreknowledge 强调事先知道，prediction 预测强调判断未来的行为、说法；做过预测不保证已经知道真相。',
 ('She entered the room with no foreknowledge of the surprise.','她走进房间时，事先完全不知道那个惊喜。'),('The novel gives the reader foreknowledge of the ending.','小说让读者预先知道了结局。'))
R('B3080','知道所形成的知识；知情与事先知情','KNOWLEDGE：知道的内容；FOREKNOWLEDGE：事情之前就知道','已有 knowledge、knowledgeable 连读，再 foreknowledge；含连字符形式继续略过。',
 '知识不只书本信息，也可说对具体情况知情。knowledge 的旧名词结尾不拆成 edge 边缘。',
 '中古 knowen + -leche 等 → knowledge；knowledge + -able；fore- + knowledge。',
 [['知识、懂行与提前知道','knowledge · knowledgeable · foreknowledge']],
 'knowledgeable 人懂得多，foreknowledge 事先知情；prediction 做预测不保证知道结果。',
 'The knowledgeable reader had foreknowledge of the historical events.\n\n这位懂行的读者事先了解那些历史事件。',
 'knowledge knowledgeable foreknowledge')
R('B2461','字母与写成的信；通信、抬头、信箱与印刷','LETTER：字母；写成一封寄出去的消息也是信','复用已有 letter、newsletter、letterhead、letterbox、letterpress 精讲，按用途分组；较专门 letterman 暂略。',
 '拉丁 littera 经法语进入英语，单个字母与写成消息的联系保留至今；不是每个带 letter 的词都只接书信。',
 'letter → letters；news + letter；letter + head/box/press。',
 [['基本字母、信和通信','letter · newsletter'],['信纸、收信和印刷','letterhead · letterbox · letterpress']],
 'letter 单个字母或信，newsletter 通讯；letterhead 信纸抬头、letterpress 活版印刷，后者接字模印刷。',
 'The newsletter was printed on paper with the company’s letterhead.\n\n通讯印在带公司抬头的纸上。',
 'letter newsletter letterhead letterbox letterpress')
R('B4248','引起兴趣的性质、相应副词与否定','INTERESTING：它能引起你的兴趣；不是你已感兴趣','复用已有 interesting、interestingly、uninteresting 精讲，集中比较描述对象、评论整句和否定。',
 'interesting 接 interest 的 -ing 形容词，说明引起兴趣；与 interested 的感兴趣者角色不同，基础词页已有对应。',
 'interest + -ing → interesting；interesting + -ly；un- + interesting。',
 [['引起兴趣、评论与否定','interesting · interestingly · uninteresting']],
 'interesting 对象有趣，interested 人感兴趣；interestingly 可评论后面整句话，不只是动作做得有趣。',
 'Interestingly, an apparently uninteresting detail led to an interesting discovery.\n\n有意思的是，一个看似无趣的细节引出了有趣发现。',
 'interesting interestingly uninteresting')
R('B4044','大、壮观、体面；亲属、头衔、看台的固定组合','GRAND：规模、地位或气势大；组合里另有固定传统','复用已有 grand、grandly、granny、grandmaster、grandstand 精讲；亲属和看台不要放成随意混排。',
 'grand 经法语接拉丁 grandis 大，后来家族辈分、尊称、建筑等各有固定用法；granny 是祖母称呼的缩略小称。',
 'grand + -ly；granny 接 gran(nam) + -y；grand + master/stand。',
 [['基本规模和气势','grand · grandly'],['亲属、地位和设施','granny · grandmaster · grandstand']],
 'grand 也可口语一千钱单位；granny 不是 grand 后面简单改 y；grandstand 看台及其炫示动词看具体场景。',
 'The grandmaster watched from the grandstand while her granny cheered.\n\n那位大师在看台观看比赛，她奶奶则在一旁加油。',
 'grand grandly granny grandmaster grandstand')
R('B4198','打开、开端与可进入的机会','OPENING：开出来的口子、事情开头、可进入的机会','复用已有 opening 精讲，把开口、开场、职位空缺连到可以进入的新空间。含连字符词头暂略。',
 'open 的分词、活动名词有旧英语形式。名词 opening 不必只有洞，也可一项工作机会、一次开场。',
 'open + -ing；the opening of 活动，an opening 可具体开口或机会；opening 修饰时可开场的。',
 [['基本活动、开口和机会','opening']],
 'an opening 职位空缺或机会，the opening 开场靠语境；不把所有 -ing 都只译正在打开。',
 'The opening of the new store created a job opening.\n\n新店开业带来了一个职位空缺。',
 'opening')
R('B3910','学习过程、所学知识与学问','LEARNING：学的过程，也可学到的知识积累','复用已有 learning 精讲，先分活动与知识，再看 learning experience、learning process 等常见搭配。含连字符扩展按要求暂略。',
 '学习名词有古英语 leornung 等旧形式，现代对应 learn + -ing；不因为收词表列为独立词基就编出第二个远古词根。',
 'learn + -ing；a learning experience 是能让人学到东西的经历。',
 [['活动和知识','learning']],
 'learning 学习或学问，teaching 教学；a learning experience 不一定是愉快经历，也可从失误学到东西。',
 'The difficult project became a valuable learning experience.\n\n这个困难项目成了一次宝贵的学习经历。',
 'learning')
if __name__=='__main__':save('continuation_20261030_bi',ROOTS,WORDS)
