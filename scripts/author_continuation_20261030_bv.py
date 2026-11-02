"""Score: marks, results, written records and emphasis."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['古诺尔斯语 skor、skora 等 → 中古英语 scor、scoren','刻痕、刻记；用刻记计数'],['英语 score','刻线、记数 → 分数、得分；记录各声部的总谱等']]
def H(f,m):return S+[[f,m]]
W('score','英 /skɔː/；美 /skɔːr/','分数、比分；得分；刻痕、刻线；总谱；二十〔旧用法〕',
 '先想在东西上刻一道记号，再想把记号累计成成绩。比赛得几分、考试拿多少分，由这里理解最直观。',
 '接中古英语 scor、scoren，与古诺尔斯语表示刻痕、刻记的词相连。旧英语也有二十这一支的记录。名词、动词历史互相关联，不把所有现代意思硬说成同一天产生。',S,
 'score a goal 进球，a test score 考试分数，the final score 最终比分；score the surface 刻划表面。a musical score 是乐谱、总谱。a score 表二十是旧式计数，scores of 表许多，不必逐个数成整二十。',
 'score a goal；a high score；the final score；a film score；scores of people。',
 'score 结果或得分，grade 可是等级、评分；音乐 score 不表示歌曲拿到的比赛分数。settle a score 可比喻报复旧怨。',
 ('She scored twice in the final ten minutes.','她在最后十分钟两次得分。'),('The orchestra is rehearsing the film score.','管弦乐团正在排练那部电影的配乐总谱。'),
 sources=['https://en.wiktionary.org/wiki/score#English','https://scrabble.m-w.com/dictionary/score','https://www.dictionary.com/browse/score'])
W('scorer','英 /ˈskɔːrə/；美 /ˈskɔːrər/','得分者；记分员',
 '一个把分拿到手的人，或一个把大家的分记下来的人。-er 只告诉你跟这个动作有关，具体是哪种角色要看比赛语境。',
 'score + -er，词尾 e 与后缀衔接形成 scorer。接得分、记分两条动词义。',H('score + -er → scorer','得分的人；负责记录比分的人'),
 'the top scorer 头号得分手，the official scorer 官方记分员；前者创造得分，后者记录得分。',
 'top scorer；leading scorer；official scorer。',
 'scorer 得分者或记分员，score 分数；the leading scorer 通常是得分领先者，不是字写得最快的记分员。',
 ('She finished the season as the team’s top scorer.','这个赛季结束时，她是全队得分最多的球员。'),('The official scorer corrected the total after the break.','官方记分员在中场休息后更正了总分。'))
W('scoreless','英 /ˈskɔːləs/；美 /ˈskɔːrləs/','未得分的；没有进球、得分的',
 '分数栏还没添上一笔。它可以说整场双方都没得分，也可以只说其中一队或一段时间没得分。',
 'score + -less，没有得分。-less 否定的是得分，不自动保证双方比分相同。',H('score + -less → scoreless','没有得分的'),
 'a scoreless draw 零比零平局，a scoreless first half 上半场双方无进球，hold a team scoreless 让某队一分未得。',
 'a scoreless draw；a scoreless first half；hold them scoreless。',
 'scoreless 无得分，draw 平局；2–2 是平局但不是 scoreless。对方得了分，本队仍可 remain scoreless。',
 ('The match ended in a scoreless draw.','比赛以零比零平局结束。'),('The visitors remained scoreless while the home team scored twice.','主队两次得分，客队仍一分未得。'))
W('outscore','英 /ˌaʊtˈskɔː/；美 /ˌaʊtˈskɔːr/','得分超过',
 '比较的不是谁动作多，而是谁分数更多。out- 在这里表示在某项表现上超过对方。',
 'out- 超过 + score 得分，组成及物动词，后接被超过的球队、对手。',H('out- + score → outscore','得分比对手多'),
 'outscore the opposition 得分超过对手，outscore someone by ten points 比某人多得十分。只说一节得分更多，不保证整场获胜。',
 'outscore the opposition；outscore them 20–12；outscore by ten points。',
 'outscore 比得分，outplay 比场上整体表现；打得更好也可能没有得更多分。',
 ('Our team outscored them 18–10 in the final quarter.','最后一节，我们队以十八比十的单节得分压过他们。'),('She outscored every other player in the tournament.','这次锦标赛中，她的得分超过了其他所有球员。'))
W('scoreline','英 /ˈskɔːlaɪn/；美 /ˈskɔːrlaɪn/','〔尤英式〕比分',
 '看见赛后写着 2–1 那一行数字，就抓住了它的意思。讨论的是双方得分关系，不是在讨论画线技术。',
 'score 比分 + line 一行记录，合成表示比分的名词。',H('score + line → scoreline','记录双方得分的比分'),
 'the final scoreline 最终比分，a 3–0 scoreline 三比零的比分，a flattering scoreline 比实际场面更好看的比分。',
 'the final scoreline；a 2–1 scoreline；the scoreline suggests。',
 'scoreline 双方比分，scorer 得分者；比分可能掩盖实际比赛过程，不能凭它推断每一方打得怎样。',
 ('The final scoreline was 2–1.','最终比分是二比一。'),('The scoreline makes the match look easier than it was.','看比分，这场比赛似乎比实际轻松得多。'))
W('scoresheet','英 /ˈskɔːʃiːt/；美 /ˈskɔːrʃiːt/','记分表、计分单',
 '一张专门把得分、进球人等记下来的纸或电子表；填进去的项目依比赛而定。',
 'score 记分 + sheet 表单、纸张，合成记录比赛分数的名词。',H('score + sheet → scoresheet','用于记分的表单'),
 'fill in a scoresheet 填记分表，get on the scoresheet〔体育报道〕取得进球、得分而被记上。',
 'fill in the scoresheet；check the scoresheet；get on the scoresheet。',
 'scoresheet 比赛记录表，sheet music 乐谱；两者不能只凭 sheet 一律互换。scoreboard 通常用于展示比分。',
 ('The referee checked the scoresheet before signing it.','裁判签字前核对了记分表。'),('She finally got on the scoresheet in the second half.','她终于在下半场取得进球，名字登上了得分记录。'))
W('underscore','名词：英 /ˈʌndəskɔː/、美 /ˈʌndərskɔːr/；动词常读：英 /ˌʌndəˈskɔː/、美 /ˌʌndərˈskɔːr/','强调、突出；在下方划线；下划线字符 _',
 '给一句话底下划一道线，是为了让人别漏看。后来即使没真画线，也能表示把某点的重要性凸显出来。',
 'under 下方 + score 刻划、画线。先有在下面画线的动作，继而用作强调；名词也命名下划线字符。这里 score 用画线支，不是低于分数。',H('under + score → underscore','下方划线 → 强调；下划线字符'),
 'underscore the importance of 强调……的重要性；an underscore 下划线字符。文件名中的下划线通常就是 _。',
 'underscore the importance；underscore the need；an underscore in a filename。',
 'underline 也可画线或强调；underscore 名词 _ 与 hyphen 连字符 - 不同。动词重音常在后，词典也收前重音变体。',
 ('The mistake underscores the need for clearer instructions.','这个失误凸显了把说明写清楚的必要性。'),('Use an underscore between the two words in the filename.','文件名里两个单词之间用一个下划线。'),
 sources=['https://en.wiktionary.org/wiki/underscore#English','https://www.etymonline.com/word/underscore'])
R('B3367','刻记、计数，再到分数、比分与书面记录','SCORE：刻下一道记号，再累计成分数','score → scorer、scoreless、outscore；记录工具、比分表达放一组；underscore 单列画线到强调的支线。',
 '二十是历史计数义，现代成绩和刻痕不是拼巧的同形词。音乐总谱也保留为独立用法，不把所有谱强说成体育成绩。',
 'score + -er/-less；out- + score；score + board/card/line/sheet；under + score。',
 [['分数与得分','score · scorer · scoreless · outscore'],['比分和记录工具','scoreline · scoreboard · scorecard · scoresheet'],['画线和强调','underscore']],
 'scoreless 不一定双方平局；outscore 某一节不保证赢整场；scoresheet 记分表、scoreboard 记分牌；underscore _ 与连字符 - 不同。',
 'The scorer checked the scoresheet before changing the scoreboard.\n\n记分员先核对记分表，再修改记分牌。',
 'score scorer scoreless outscore scoreline scoreboard scorecard scoresheet underscore')
if __name__=='__main__':save('continuation_20261030_bv',ROOTS,WORDS)
