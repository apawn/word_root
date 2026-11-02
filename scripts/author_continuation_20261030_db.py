"""Terror and boss: separate fear, organized intimidation and ordinary authority."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['拉丁语 terrēre → terror','使害怕 → 极度恐惧'],['法语 terreur → 中古英语 terrour → terror','强烈恐惧；令人恐惧的人或事物']]
def TH(f,m):return T+[[f,m]]
W('terror','英 /ˈterə/；美 /ˈterər/','极度恐惧；令人害怕的人、事物',
 '害怕强到仿佛身体僵住、脑子只剩危险。也可把制造这种感受的东西叫 a terror，而非只能指心里的感觉。',
 '经法语 terreur 接拉丁语 terror，来自 terrēre 使害怕。英语的 terr- 在这条线上关乎恐惧，不是 terra 土地那条线。',T,
 'in terror 惊恐地，a look of terror 惊恐神情，a reign of terror 恐怖统治；口语 a little terror 还可半开玩笑说闹腾、难管的小孩。',
 'in terror；a look of terror；a reign of terror；strike terror into。',
 'fear 范围宽，terror 往往更强烈；terror 恐惧本身不等于 terrorism 恐怖主义，惊悚片使人害怕并不能因此叫 terrorism。',
 ('The children stared in terror as the huge tree began to fall.','大树开始倒下时，孩子们惊恐地盯着它。'),('There was a look of terror on his face.','他脸上露出了极度恐惧的神情。'))
W('terrorist','英 /ˈterərɪst/；美 /ˈterərɪst/','恐怖主义者；恐怖主义的',
 '用暴力或威胁制造广泛恐惧、借此胁迫他人达到目的的人。这个称呼指向一种做法，不能只因某人令人讨厌、吓人就随便套用。',
 '与法语 terroriste 相接，英语见于十八世纪末法国革命语境，早期还指支持恐怖统治的人。现代可按 terror + -ist 理解人物名，但不是一开始就只有今天常见的组织成员形象。',
 TH('法语 terroriste → 英语 terrorist','早期革命、恐怖统治语境 → 更广的恐怖主义者称呼'),
 'a terrorist attack 恐怖袭击，a terrorist organization 恐怖组织；也作名词 a terrorist。正式报道中的具体认定须看事实与出处。',
 'a terrorist attack；a terrorist organization；the history of the word terrorist。',
 'terrorist 是人物或修饰词，terrorism 是行为体系、手段等抽象概念；terrorize 可说欺凌者恐吓邻居，不自动等于他属于恐怖组织。',
 ('The museum explains how the meaning of terrorist has changed over time.','博物馆解释了 terrorist 一词的意思怎样随时代变化。'),('The novel follows a reporter investigating a terrorist organization.','小说讲一位记者调查一个恐怖组织的故事。'),
 sources=['https://en.wiktionary.org/wiki/terrorist#English','https://www.etymonline.com/word/terrorist'])
W('terrorism','英 /ˈterərɪzəm/；美 /ˈterərɪzəm/','恐怖主义；以制造恐惧实施胁迫的做法',
 '不是有人一时很害怕，而是把让人害怕当作施压手段：通过暴力、威胁等影响更广的人群，迫使人服从、改变行动。',
 '经法语 terrorisme，十八世纪末英语首先接法国革命恐怖统治的语境，后来用于更广的系统性恐吓、恐怖主义。现代可用 terror + -ism 认识抽象名词。',
 TH('法语 terrorisme → 英语 terrorism','恐怖统治的做法 → 更广的恐怖主义称呼'),
 'the history of terrorism 恐怖主义史，the impact of terrorism 恐怖主义的影响，counterterrorism 反恐。不同研究、法律文本可能有不同边界，阅读时留意作者所指。',
 'the history of terrorism；the impact of terrorism；a study of terrorism。',
 'terrorism 不等于所有 violence 暴力，也不等于 terror 恐惧感；要看是否借恐惧实施胁迫及具体语境。',
 ('The course examines the history of terrorism.','这门课研究恐怖主义的历史。'),('The book explores the impact of terrorism on everyday life.','这本书探讨恐怖主义对日常生活的影响。'),
 sources=['https://en.wiktionary.org/wiki/terrorism#English','https://www.etymonline.com/word/terrorism'])
W('terrorize','英 /ˈterəraɪz/；美 /ˈterəraɪz/','恐吓、使长期处于恐惧中',
 '让一个人或一群人怕得不敢正常生活、行动，通常比吓一跳更强，也常带反复威吓的感觉。',
 'terror + -ize，构成使陷入恐惧的动词。英式还见 terrorise，不另设词头。',TH('terror + -ize → terrorize','使陷入极度恐惧；以恐惧控制'),
 'terrorize a neighbourhood 恐吓一个街区的居民，terrorize someone into silence 吓得某人不敢说话。',
 'terrorize someone；terrorize a neighbourhood；terrorize someone into silence。',
 'startle 常突然吓一跳，terrorize 是更强的恐吓、使害怕；日常 bullying 欺凌也能 terrorize，动词不限定政治目的。',
 ('The bullies had terrorized the younger children for months.','那些欺凌者恐吓年幼的孩子已经好几个月。'),('In the story, a dragon terrorizes the village.','故事里，一条龙让全村人惶恐不安。'))
R('B3887','恐惧与通过恐惧控制人','TERROR：怕到压倒日常行动；再分感受、人物、做法和动作','terror → terrorist、terrorism、terrorize，相邻看清恐惧感怎样变成用于控制人的手段。',
 'terror 是感受或恐惧来源；terrorism 有历史上恐怖统治的背景，不把所有惊吓都叫恐怖主义。terr- 在这里不接土地 terra。',
 '拉丁 terrēre → terror，经法语进入英语；terroriste、terrorisme 保留十八世纪末革命语境；terror + -ize。',
 [['恐惧本身','terror'],['人物与做法','terrorist · terrorism'],['使人害怕的动作','terrorize']],
 'terror 恐惧感，terrorism 系统性恐怖手段；terrorist 人物或修饰词，terrorize 动词也适用于日常恐吓。',
 'The book explains how fear and terror can be used to control people.\n\n这本书解释了人们怎样用害怕、恐惧来控制别人。','terror terrorist terrorism terrorize')
B=[['荷兰语 baas，中古荷兰语 baes → 英语 boss','主人、管事者；更远来源不确定'],['英语 boss 的现代扩展','上司、负责人；发号施令；游戏强敌']]
W('boss','英 /bɒs/；美 /bɑːs/ 或 /bɔːs/','上司、负责人；指挥；游戏里的强敌、首领',
 '工作中能给你安排任务、作决定的人。也可说某人老指挥别人；游戏把特别难对付、像头目那样的对手叫 boss。',
 '管事者义借自荷兰语 baas，中古荷兰语 baes，更远来源尚无定论。盾牌中央凸起那种 boss 另接法语 bosse 等，不拿同一个荷兰人物词硬解释所有凸块。',B,
 'my boss 我的上司，be your own boss 自己当老板，boss someone around 对人呼来喝去，the final boss 游戏最终首领。',
 'my boss；be your own boss；boss someone around；the final boss。',
 'boss 不保证是公司 owner 所有人，部门主管也可以是你的 boss；bossy 带爱管人的批评，不只是有管理职位。',
 ('My boss asked me to check the figures again.','我的上司让我再核对一次数字。'),('Stop bossing your little brother around.','别再对你弟弟呼来喝去了。'),
 sources=['https://en.wiktionary.org/wiki/boss#English','https://www.etymonline.com/word/boss'])
W('bossy','英 /ˈbɒsi/；美 /ˈbɑːsi/ 或 /ˈbɔːsi/','爱发号施令的、爱支使人的',
 '好像总觉得自己该作主，动不动就告诉别人必须怎么做，常让听的人觉得被管得过头。',
 '常见形容词由 boss 管事者 + -y，表示带这种作派。与另一种表示凸起的旧 bossy 用法分开。',B+[['boss + -y → bossy','带爱指挥别人特点的']],
 'a bossy attitude 爱支使人的态度，sound bossy 听着像在发号施令，a bossy older sibling 爱管人的哥哥姐姐。',
 'a bossy attitude；sound bossy；stop being bossy。',
 'bossy 常含过度支使的负面评价；confident 自信、decisive 果断不等于 bossy，发出必要指示也不必然是爱管人。',
 ('She disliked his bossy tone.','她不喜欢他那副发号施令的口气。'),('I am trying to be clear without sounding bossy.','我想把话说清楚，又不想听起来像在支使人。'))
R('B2712','上司与爱指使人的作派','BOSS：谁在作主；bossy 则是总要替别人作主','boss → bossy；先分有权安排工作与过度支使别人。',
 '管事者来自荷兰语 baas，深源不确定。凸起、盾心 boss 另有法语来源，常见工作义不必硬接凸块。',
 '荷兰 baas → boss；boss + -y → bossy；boss around 是发号施令的动词搭配。',
 [['人物、角色与动作','boss'],['作派评价','bossy']],
 'boss 可是受雇主管而非公司所有人；bossy 是行为评价，不是所有领导者的同义词。',
 'A good boss can give clear instructions without being bossy.\n\n好上司能把指示说清楚，也不一味支使人。','boss bossy')
if __name__=='__main__':save('continuation_20261030_db',ROOTS,WORDS)
