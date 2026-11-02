"""Party and taking: group membership and useful fixed compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
W('counterparty','英 /ˈkaʊntəpɑːti/；美 /ˈkaʊntərpɑːrti/','交易对方；合同另一方',
 '你站在交易的一边，与你签这笔交易的另一边，就是你的 counterparty。',
 'counter- 相对、另一边 + party 一方。party 在这里用合同、交易参与方的意思，不是聚会，也不一定是政党。',
 [['法语 partie → 英语 party','部分、一方 → 一组人、交易参与方'],['counter- + party → counterparty','相对的一方 → 交易对方']],
 'the counterparty to a contract 合同另一方，counterparty risk 常说交易对方可能不履约的风险；对方可以是人或机构。',
 'a trading counterparty；the counterparty to the agreement；counterparty risk。',
 'counterparty 只指出这笔关系中的对方，不代表敌人；它也不是聚会上站在柜台边的人。',
 ('The bank asked for details of the counterparty to the agreement.','银行要求提供协议另一方的详细资料。'),('Each counterparty received a copy of the signed contract.','合同各方都收到了一份签署后的合同。'))
R('B3155','聚会、政党；一方与多方参与','PARTY：聚在一边的人，或事情的一方','同一个 party，在生日场景是聚会，在选举场景是政党，在合同里是一方。',
 'party 经法语接分开、分成部分的词族，与 part 相关。分出的一方或一群人，形成不同固定用法；现代每个义项仍要看场景。',
 'party → multiparty 多方、多党；counter- 相对一方 → counterparty。连字符的聚会复合词本轮暂略。',
 [['基本词及多方','party · multiparty'],['交易中的对方','counterparty']],
 'a party to the agreement 是协议一方；a party at home 是家里的聚会。counterparty 不是敌对政党。',
 'Each party to the agreement received the counterparty’s contact details.\n\n协议各方都收到了对方的联系方式。',
 'party multiparty counterparty')
T=[['古诺尔斯语 taka → 中古英语 taken → take','拿、取得'],['take + -ing → taking','拿取、接受等过程；部分固定词组形成别的用法']]
W('taking','/ˈteɪkɪŋ/','拿取、接受等的 -ing 形式；取得；营业收入〔复数〕',
 '先想拿到手、带走或接受；放进具体搭配，才知道拿的是东西、行动机会，还是收入。',
 'take 去末尾 e + -ing；take 经中古英语来自古诺尔斯语 taka。taking 可保留动词作用，也可转作名词；takings 的复数形式又有营业收入义。',T,
 'taking notes 记笔记，taking a break 休息；for the taking 可供取用、唾手可得；the day’s takings 当天营业收入。不是所有 taking 都能单译为拿。',
 'taking notes；taking part；for the taking；the day’s takings。',
 'taking 是 -ing 形式，taken 是过去分词：I am taking it 我正拿，It was taken 它被拿走。',
 ('She is taking notes during the lecture.','她正在讲座中记笔记。'),('The shop’s takings were higher than usual.','店里的营业收入比平时高。'))
W('breathtaking','/ˈbreθteɪkɪŋ/','令人惊叹的；惊险、惊人到让人屏息的',
 '看到景色或表演，惊得一瞬间像忘了呼吸；多半是在赞叹，也能强调变化快得惊人。',
 'breath 呼吸 + taking，联系 take someone’s breath away 令人屏息、惊叹。breath 是名词，末尾 /θ/，不是动词 breathe 的 /ð/。',
 [['breath 呼吸；taking 拿走','两部分构成令人仿佛喘不过气的比喻'],['breathtaking','惊叹、惊险到让人屏息的']],
 'a breathtaking view 惊艳的景色，breathtaking speed 惊人的速度；不只形容漂亮，也可形容大胆程度、变化幅度惊人。',
 'a breathtaking view；breathtaking scenery；breathtaking speed。',
 'breathtaking 是事物令人惊叹的效果，breathless 常是人喘不过气或激动的状态；景色 breathtaking，人可能 breathless。',
 ('The train passed through breathtaking mountain scenery.','火车穿过令人惊叹的山景。'),('The city has changed at a breathtaking speed.','这座城市变化快得惊人。'))
R('B4260','取得与接受；令人屏息、费心和照料','TAKING：先看 take，再认固定组合','take 能拿东西、采取行动；与 breath、pains、care 组合后，需要保留各自固定搭配的画面。',
 'taking 是 take 的 -ing 形式。breathtaking 联系拿走呼吸的比喻；painstaking 联系 take pains 费心；caretaking 联系 take care 照料。不要把 painstaking 错拆成 pain + staking。',
 'take → taking；breath + taking → breathtaking；pains + taking → painstaking；care + taking → caretaking。',
 [['基础形式','taking'],['屏息惊叹、认真费心及照料','breathtaking · painstaking · caretaking']],
 'breathtaking 景物等令人惊叹；painstaking 人或工作认真细致。taking 与 taken 的语法形式不同。',
 'The breathtaking exhibition was the result of painstaking work.\n\n令人惊叹的展览，是认真细致工作的成果。',
 'taking breathtaking painstaking caretaking')
if __name__=='__main__':save('continuation_20261029_ck',ROOTS,WORDS)
