"""Fill high-frequency base-word gaps inside already authored families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0401':dict(words=['difficult','difficulty','office','officer'],label='先补常用基础：困难与职务承担者',note='difficult 在英语中通常解释为从较早 difficulty 逆构，不能把今日教学顺序当历史先后。officer 经法语、拉丁语人物名称借入，现代又与 office + -er 对应。'),
 'B2522':dict(words=['industry','industrial'],label='行业、工业的基础名词',note='industry 与 industrial 同接拉丁语 industria 的勤勉、工作活动词族；industrial 另有法语、拉丁语形容词借入史。先读 industry，便于理解后面的工业、工业化等扩展。'),
 'B3894':dict(words=['matter','material'],label='同源的常用基础词：matter 与 material',note='matter 与 material 同接拉丁语 materia，经不同法语等形式进入英语；是同源借词，不能写成现代 matter 直接加 -ial 就形成 material。'),
 'B2597':dict(words=['reason','rational'],label='理由与理性：先从 reason 进入',note='reason 经法语 raison 等接拉丁语 ratio，rational 接相应拉丁形容词 rationalis 等；现代意义相连，但不是直接由 reason 改拼写加尾。'),
 'B4112':dict(words=['article','articulate'],label='文章、条目与清楚分节的表达',note='article 与 articulate 同接拉丁语 articulus 的关节、部分材料，分别经不同词形借入。文章是完整刊物中的一部分，articulate 的表达义则联系分明的语音、表达。'),
 'C1437':dict(words=['district'],label='由约束、管辖到区域：district',note='district 接拉丁语 distringere、districtus 的约束、管辖材料，经管辖范围再到现代区域；不是 dis- 加现代英语 strict 就能讲完整。'),
}
W('difficult','/ˈdɪfɪkəlt/','困难的、费劲的；难相处、难应付的',
 '事情不是轻轻一推就动，得费力、动脑，叫 difficult。说人 difficult，往往是难沟通、难取悦或不好应付。',
 '英语 difficult 通常解释为从较早 difficulty 逆构；更早名词经法语接拉丁 difficultas，与 dis- 否定、facilis 容易做及 facere 做的词族相连。',
 [['拉丁语 facilis → difficilis、difficultas → 英语 difficulty','容易做 → 不容易做、困难'],['由 difficulty 逆构 difficult','形成英语形容词；后来也形容人难应付']],
 'a difficult question 难题；find it difficult to do 觉得做某事难；be difficult to please 难以取悦；a difficult customer 难应付的顾客。',
 'a difficult decision；a difficult time。','difficult 说做起来有难度，difficulty 说困难这一性质或具体难处。学习先看形容词很方便，但历史上的英语名词更早。',
 ('I found the last question difficult.','我觉得最后一道题很难。'),('He can be difficult to work with.','他有时很难共事。'),sources=['https://www.etymonline.com/word/difficult','https://en.wiktionary.org/wiki/difficult#English'])
W('industry','/ˈɪndəstri/','工业；行业、产业；勤勉〔较正式旧义〕',
 '把一类产品或服务背后成体系的生产经营看成整体，就是一个 industry。工厂制造属于它，旅游、电影等行业也能这样叫。',
 '经法语 industrie、拉丁语 industria 勤勉、活动等借入。工作、勤勉的材料逐渐用于系统经营、特定行业和工业；更远拉丁构成有讨论。',
 [['法语 industrie、拉丁语 industria → 英语 industry','勤勉、技能、工作活动'],['现代经济活动的集合义','工业体系；某类生产或服务行业']],
 'the steel industry 钢铁工业；the tourism industry 旅游业；work in the film industry 在电影行业工作。谈多个行业可用 industries。',
 'heavy industry；a growing industry。','industrial 是工业的；industrious 是勤奋的。industry 的旧勤勉义保存在后者，工业、产业的现代义则帮助理解前者。',
 ('She works in the tourism industry.','她在旅游行业工作。'),('The town was once a centre of heavy industry.','这座镇子曾是重工业中心。'),sources=['https://www.etymonline.com/word/industry','https://en.wiktionary.org/wiki/industry#English'])
W('matter','英 /ˈmætə/；美 /ˈmætər/','事情、问题；物质；要紧、有影响〔动词〕',
 '名词可以说手头这件事，也可以说构成东西的物质；动词 it matters 则问“这会不会影响结果、对人重要”。',
 '经法语 matere、matiere 等接拉丁语 materia 材料、木材、内容等。物质、讨论素材和事情的多条分支在较早词族中发展，英语后又形成要紧的动词。',
 [['拉丁语 materia → 法语相关形式 → 英语 matter','材料、内容、主题等'],['名词分支与动词发展','物质；事情、问题；具有重要性、影响']],
 'an important matter 重要事情；organic matter 有机物；What’s the matter? 怎么了；It doesn’t matter. 没关系、不重要。',
 'a matter of time；your opinion matters。','material 常指制成东西所用材料；matter 可说物质，也很常说事情。It matters 是动词表达“有影响、重要”，不只是名词换了位置。',
 ('We need to discuss an important matter.','我们需要讨论一件重要的事。'),('The soil contains organic matter.','土壤中含有有机物。'),('Your opinion matters to me.','你的看法对我很重要。'),sources=['https://www.etymonline.com/word/matter','https://en.wiktionary.org/wiki/matter#English'])
W('reason','/ˈriːzən/','原因、理由；理性、推理能力；推理、说理',
 '能说清“为什么”，是给出 a reason；能根据证据一步步想，是 use reason；跟某人讲道理，则可以 reason with someone。',
 '经法语 raison、resoun 等接拉丁语 ratio 计算、理解、理由，与 reri 思考、核算同族。名词和动词各有较早借入、发展路径。',
 [['拉丁语 ratio → 法语 raison 等 → 英语 reason','计算、理解、根据、理由'],['名词、动词的现代分支','原因、理由；理性；推理、与人说理']],
 'the reason for the delay 延误原因；give a reason 给出理由；listen to reason 听从道理；reason with someone 跟某人讲道理。',
 'for some reason；reason from the evidence。','cause 更偏造成结果的原因；reason 可以说事发原因，也可以说一个人行动的理由。reason 与 rational 同源，但不能直接按 re- + son 拆。',
 ('What was the reason for the delay?','延误的原因是什么？'),('She tried to reason with him.','她试着跟他讲道理。'),('We should use reason rather than guesswork.','我们应该依据理性判断，而不是瞎猜。'),sources=['https://www.etymonline.com/word/reason','https://en.wiktionary.org/wiki/reason#English'])
W('article','英 /ˈɑːtɪkəl/；美 /ˈɑːrtɪkəl/','文章；条款；一件物品；冠词〔语法〕',
 '把一个整体分开看，其中一节、一项、一篇都能联系 article。报纸里的一篇文章、文件里的一条规定、衣物中的一件，分属不同常用搭配。',
 '经法语 article 接拉丁语 articulus 小关节、部分、成员，是 artus 关节等的小称。文字分节、独立项目和语法术语沿不同分支发展。',
 [['拉丁语 artus → articulus → 法语、英语 article','关节、小部分、项目'],['文字、物品与语法分支','条款、文章；一件物品；冠词']],
 'a newspaper article 报纸文章；an article of clothing 一件衣物；Article 3 第三条；the definite article 定冠词。',
 'read an article；a useful article。','article 的 -icle 有拉丁小称背景，和 particle 中的小称材料可以对照；不是现代 art 艺术直接加 -icle 就变成文章。',
 ('I read an interesting article about birds.','我读了一篇有趣的鸟类文章。'),('Each passenger may bring one extra article of clothing.','每位乘客可以多带一件衣物。'),('In English, “the” is the definite article.','英语中的 the 是定冠词。'),sources=['https://www.etymonline.com/word/article','https://en.wiktionary.org/wiki/article#English'])
W('officer','英 /ˈɒfɪsə/；美 /ˈɑːfɪsər/〔也见 /ˈɔːfɪsər/〕','官员、军官、警员；机构中承担特定职务的人',
 '核心是身上有一项正式职务、职责。究竟是警员、军官，还是公司的某项负责人，由前面的名称和组织语境决定。',
 '经法语 oficier 等接中世纪拉丁语 officiarius，与 officium 职务、职责同族。现代可与 office + -er 对应理解，历史上则有整个人物名称的借入。',
 [['拉丁语 officium → officiarius → 法语人物词','职务、职责 → 承担职务的人'],['英语 officer 的组织分支','官员；军官、警员；机构负责人等']],
 'a police officer 警员；an army officer 陆军军官；a chief financial officer 首席财务官；a safety officer 安全负责人。',
 'a customs officer；the officer in charge。','office 的早期职务义帮助理解 officer；不是凡在办公室工作的人都叫 officer。具体称呼取决于被赋予的职位和职责。',
 ('A police officer helped us find the station.','一名警员帮我们找到了车站。'),('She was appointed chief financial officer.','她被任命为首席财务官。'),sources=['https://www.etymonline.com/word/officer','https://en.wiktionary.org/wiki/officer#English'])
W('district','/ˈdɪstrɪkt/','区域、地区；行政区或特定用途分区',
 '把一片地方按管理、功能或特征圈作一个区。购物区、学区、某个行政区，都可以是 district。',
 '经法语 district 接中世纪拉丁语 districtus 管辖、管辖范围，与拉丁语 distringere 拉紧、约束、强制相连。由管得到的范围，再扩展成区域。',
 [['distringere、districtus 的约束、管辖材料','对某范围行使控制、管辖'],['法语、英语 district','管辖区域；一般行政或功能地区']],
 'a shopping district 购物区；a school district 学区；a rural district 乡村地区；the historic district 历史街区。',
 'a residential district；the business district。','area 是较宽泛的区域；district 常带划区、功能或管理单元的意味。现代 district 与 strict 共享较早拉紧词族，但不能直接按 dis- + 英语 strict 推出全部历史。',
 ('The hotel is in the city’s shopping district.','酒店位于这座城市的购物区。'),('They moved to a quieter residential district.','他们搬到了一个更安静的住宅区。'),sources=['https://www.etymonline.com/word/district','https://en.wiktionary.org/wiki/district#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tt',ROOTS,WORDS)
    extend_lessons()
