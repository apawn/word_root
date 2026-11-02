"""Goal and add: targets, sports roles and a rebracketed snake name."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
G=[['中古英语 gol 边界、界限 → goal','赛程终点、目标位置；更远来源不确定'],['现代 goal','球门、进球；想达成的结果']]
def H(f,m):return G+[[f,m]]
W('goal','英 /ɡəʊl/；美 /ɡoʊl/','目标；球门；进球得分',
 '你要到达的终点，是目标；球要送进的地方是球门；成功送进去的得分也叫 goal。',
 '中古英语 gol 有边界、界限义，后用于竞赛终点与目标；更远的障碍、标记词联系有不确定性，不强作定论。',G,
 'set a goal 设定目标，achieve a goal 达成目标，score a goal 进球，in goal 担任门将。',
 'set a goal；achieve a goal；score a goal；in goal。',
 'goal 想达成的结果，plan 达到结果的安排；一个 goal 可有多种 plan。goal 与同音近音的 go 不按现代加 l 造义。',
 ('Our goal is to make the service easier to use.','我们的目标是让服务更好用。'),('She scored the winning goal.','她打进了制胜球。'))
W('goalkeeper','英 /ˈɡəʊlkiːpə/；美 /ˈɡoʊlkiːpər/','守门员',
 '专门守住球门、阻止对方把球送进去的队员，具体规则随运动而变。',
 'goal 球门 + keeper 守护者，keeper 来自 keep + -er。不是 goal 的所有者或租客。',H('goal + keeper → goalkeeper','守护球门的人 → 守门员'),
 'a football goalkeeper 足球守门员，the opposing goalkeeper 对方门将，a goalkeeper’s save 门将扑救。',
 'the opposing goalkeeper；a goalkeeper’s save；replace the goalkeeper。',
 'goalkeeper 在多种有球门的运动中使用，不只足球；keeper 单独有时也是门将简称。',
 ('The goalkeeper saved the penalty.','守门员扑出了点球。'),('They replaced the injured goalkeeper before halftime.','中场前，他们换下了受伤门将。'))
W('goaltender','英 /ˈɡəʊltendə/；美 /ˈɡoʊltendər/','守门员；尤指冰球等运动的门将',
 '同样是守球门的人，北美冰球报道里特别常见。',
 'goal + tender 看守、照管者，tender 接 tend 照管 + -er，不是形容词温柔、鲜嫩。',H('goal + tender → goaltender','照管球门的人 → 守门员'),
 'a hockey goaltender 冰球门将，the starting goaltender 首发门将；也常简称 goalie。',
 'a hockey goaltender；the starting goaltender；a goaltender’s save。',
 'goaltender 与 goalkeeper 很多场景所指相同，实际选词随运动、地区惯例；不要按 tender 误译温柔球门。',
 ('The goaltender stopped all three shots.','门将挡住了三次射门。'),('The coach named the starting goaltender for the next game.','教练确定了下场比赛的首发门将。'))
W('goaltending','英 /ˈɡəʊltendɪŋ/；美 /ˈɡoʊltendɪŋ/','守门表现、守门活动；篮球干扰球',
 '冰球里通常说门将工作、表现；篮球里却可是一种干扰投篮的违例名称。',
 'goal + tending 看守活动；篮球术语沿用守住球门的画面，形成特定干扰球规则名。具体裁判标准按项目规则另看。',H('goal + tending → goaltending','守门活动；篮球中的特定干扰球违例'),
 'excellent goaltending 出色守门表现，a goaltending violation 干扰球违例。',
 'excellent goaltending；a goaltending violation；strong goaltending。',
 'goaltending 冰球可正面，篮球可指违例；同词换运动，不能沿用同一个评价。',
 ('Strong goaltending kept the team in the game.','出色守门表现让球队仍有机会。'),('The referee called a goaltending violation.','裁判吹罚了干扰球违例。'),sources=['https://official.nba.com/rule-no-11-basket-interference-goaltending/','https://en.wiktionary.org/wiki/goaltending#English'])
W('goalscorer','英 /ˈɡəʊlskɔːrə/；美 /ˈɡoʊlskɔːrər/','进球者；射手',
 '谁把球送进球门得分，就从这项表现叫谁进球者；也可指很擅长进球的球员。',
 'goal 进球 + scorer 得分者，后者 score + -er。不是 score 分数再加一个没有意义的 r。',H('goal + scorer → goalscorer','打入进球的人 → 射手'),
 'the leading goalscorer 进球最多者，a prolific goalscorer 高产射手。',
 'the leading goalscorer；a prolific goalscorer；the winning goalscorer。',
 'goalscorer 不一定固定前锋位置，后卫也可能成为这场的进球者；striker 更偏位置、角色。',
 ('She finished the season as the team’s leading goalscorer.','赛季结束时，她是队内进球最多的球员。'),('The club signed a proven goalscorer.','俱乐部签下了一名进球能力经过检验的射手。'))
W('goalscoring','英 /ˈɡəʊlskɔːrɪŋ/；美 /ˈɡoʊlskɔːrɪŋ/','进球；进球方面的',
 '把进球作为一种能力、记录或过程，不再指完成进球的那个人。',
 'goal + scoring，scoring 来自 score 去 e + -ing。与 goalscorer 的人物后缀对照。',H('goal + scoring → goalscoring','进球得分的活动、性质'),
 'goalscoring ability 进球能力，a goalscoring record 进球记录。',
 'goalscoring ability；a goalscoring record；goalscoring chances。',
 'goalscorer 人，goalscoring 活动或修饰性质；a goalscoring chance 是进球机会，不是射手本人。',
 ('The coach praised her goalscoring ability.','教练称赞了她的进球能力。'),('The team created several good goalscoring chances.','球队创造了几次很好的进球机会。'))
W('goalless','英 /ˈɡəʊlləs/；美 /ˈɡoʊlləs/','未进球的；零比零的',
 '比赛或这段时间没有进球；常见 goalless draw 就是零比零平局。',
 'goal + -less 没有，保留 goal 的 l，再加 -less，所以写双 l。',H('goal + -less → goalless','没有进球 → 未进球的'),
 'a goalless draw 零比零平局，a goalless first half 上半场无进球。',
 'a goalless draw；a goalless first half；remain goalless。',
 'goalless 在比赛报道主要说进球，不是说球场没有安装球门，也不等于人生没有目标。',
 ('The match ended in a goalless draw.','比赛以零比零平局结束。'),('The first half remained goalless.','上半场一直没有进球。'))
R('B3366','目标、球门与进球角色','GOAL：要到达的终点，也指球门和进球','goal 基本词后把守门者与守门活动放一起，再看进球者、进球表现和无进球。',
 '中古英语边界、终点词发展出现代目标义。具体球类术语按运动辨，尤其 goaltending 的篮球与冰球不同。',
 'goal + keeper/tender/tending；goal + scorer/scoring；goal + -less。',
 [['基本目标与守门','goal · goalkeeper · goaltender · goaltending'],['进球者、表现与否定','goalscorer · goalscoring · goalless']],
 'goalscorer 人、goalscoring 活动；goaltending 可是正常守门或篮球违例；goalless draw 零比零。',
 'The goalkeeper’s saves kept the match goalless.\n\n守门员的扑救让比赛保持零进球。',
 'goal goalkeeper goaltender goaltending goalscorer goalscoring goalless')
AD=[['拉丁 ad- 向 + -dere 放、置 → addere → 英语 add','放上去、加上'],['现代 add','增加、相加；补充发言']]
W('add','/æd/','加上；相加；补充说',
 '原来有一些，再把新的一份放上去；说话时加一条信息也用同一画面。',
 '借拉丁 addere 加上，历史是 ad- 向与 -dere 放、置的组合。现代不拆成 a- 与 dd 两个英语部分。',AD,
 'add salt 加盐，add two numbers 两数相加，add to 增加，add that... 补充说……；add up 合计、说得通。',
 'add to；add something to；add up；add that。',
 'add to it 给它增加，add it to... 把它加到……；词序和介词关系决定加的是什么。',
 ('Add a little water to the mixture.','往混合物里加一点水。'),('She added that the meeting would start at nine.','她补充说，会议九点开始。'))
W('adder','英 /ˈædə/；美 /ˈædər/','加法器；另源蝰蛇',
 '计算机里能做相加的部件是 adder；自然观察中 a common adder 则可能是一种蝰蛇。',
 '加法器义是 add + -er。蛇名接古英语 nædre，历史 a nadder 被重新分成 an adder，n 被听成冠词一部分；两条来源分开。',AD+[['另一路 nædre → nadder → adder','词界重分形成蛇名']],
 'a full adder 全加器，an electronic adder 电子加法器；a common adder 欧洲常见蝰蛇名。',
 'a full adder；an electronic adder；a common adder。',
 'adder 蛇不是会加法的蛇；n 的丢失是词界重分，不是所有 n- 开头名词都能照着变化。',
 ('The circuit contains a full adder.','电路包含一个全加器。'),('The guide identified the snake as a common adder.','向导认出那条蛇是一条欧洲蝰蛇。'))
R('B2502','加上、相加；加法器与另源蛇名','ADD：把新的一份放到原有东西上','add → adder 加法器很透明；同形蛇名另讲词界重分，不把两义混成一个故事。',
 'add 借拉丁加上词；蛇 adder 来自 nadder 旧形式，与加法器的 -er 无关。',
 'add → adder；蛇名 a nadder → an adder 为独立历史。',
 [['增加与执行器具','add · adder']],
 'adder 加法器与蛇两源；add up 还可说事情合乎逻辑。',
 'The adder adds the two binary values.\n\n加法器把两个二进制数相加。',
 'add adder')
if __name__=='__main__':save('continuation_20261030_d',ROOTS,WORDS)
