"""Race: running and ancestry are different historical branches."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
RA=[['古英语 rǣs、古诺尔斯语 rás 等 → 英语竞速 race','奔涌、快跑 → 速度竞赛'],['另一支：法语 race、意大利语 razza → 英语群体 race','血统、类别等，更远来源不确定']]
W('race','/reɪs/','竞赛；快速奔跑；种族；人类等群体称呼',
 '跑道上 race 是比快，社会话题中 race 是种族；拼写相同，历史不从同一个现代意思串出来。',
 '竞速分支接古英语 rǣs、古诺尔斯语 rás 等快跑词；血统、种族分支经法语 race、联系意大利语 razza，更远不确定。不能编成不同族群比赛所以出现种族义。',RA,
 'win a race 赢比赛，race against time 争分夺秒；the human race 人类，race and ethnicity 种族与族裔。race 作动词也可说心跳、思绪飞快。',
 'win a race；race against time；the human race；a racing heart。',
 'race 比速度，match 比赛可有更广项目；race 种族通常涉及社会历史中的人群分类，不等于国籍 nationality。',
 ('She won the race by a narrow margin.','她以微弱优势赢了比赛。'),('The museum explores how ideas about race changed over time.','博物馆探讨人们关于种族的观念如何随时间变化。'),sources=['https://en.wiktionary.org/wiki/race#English','https://www.etymonline.com/word/race'])
W('racer','英 /ˈreɪsə/；美 /ˈreɪsər/','竞速选手；赛车、赛马等',
 '参加速度比赛的人、动物或车辆，先看句子到底说谁在参赛。',
 'race 的竞速动词义 + -er；-er 不一定只形成表示人的词。另有按快速移动命名的动物用法，本轮主学常用竞赛义。',RA[:1]+[['race + -er → racer','竞速 → 参赛人、动物、车辆']],
 'a motorcycle racer 摩托车赛车手，a road racer 公路赛选手或赛车；a racer 在车辆叙述中也可能是车本身。',
 'a motorcycle racer；a professional racer；a racing car and its racer。',
 'racer 竞速者，racist 种族主义者；两者不能只按更短、更长的人物后缀互换。',
 ('The young racer completed every lap.','年轻赛车手跑完了每一圈。'),('The old racer is now displayed in a museum.','那辆旧赛车如今陈列在博物馆里。'))
W('racehorse','英 /ˈreɪshɔːs/；美 /ˈreɪshɔːrs/','赛马',
 '主要为竞速比赛训练、使用的马，不是马跑起来就临时都成了赛马。',
 'race 速度竞赛 + horse 马，按用途形成动物角色名称。',C('race 速度竞赛','horse 马','racehorse','供竞速比赛的马'),
 'train a racehorse 训练赛马，a retired racehorse 退役赛马；退役后仍可用这个称谓说明其经历。',
 'a racehorse；train a racehorse；a retired racehorse。',
 'racehorse 是马，racer 既可能是人也可能是马、车；racecourse、racetrack 是竞赛场地。',
 ('The racehorse was resting in its stable.','赛马正在马厩里休息。'),('She helped care for a retired racehorse.','她帮忙照料一匹退役赛马。'))
W('racetrack','/ˈreɪstræk/','赛道；跑道；赛马场',
 '把比赛路线做成专门场地，让人、动物或车辆沿规定路线比快。',
 'race 竞速 + track 轨迹、跑道，形成比赛场地名称。不同项目赛道形状、材料不同，不只椭圆跑道。',C('race 竞速','track 跑道、路线','racetrack','用于竞速比赛的专门路线或场地'),
 'a motor racetrack 赛车道，a horse racetrack 赛马场；on the racetrack 在赛道上。',
 'a motor racetrack；on the racetrack；a racetrack circuit。',
 'racetrack 与 racecourse 在赛马场等范围有重叠，track 更凸显路线、跑道；racecourse 也随地区有不同习惯。',
 ('The driver tested the car on a closed racetrack.','车手在封闭赛道上测试汽车。'),('Spectators gathered around the racetrack.','观众聚集在赛道周围。'))
W('raceway','/ˈreɪsweɪ/','赛道；水道；电线、机械等的导槽',
 '让某种运动沿一个限定通道进行；有时跑的是赛车，有时走的是水、电缆或机械滚动部件。',
 'race 奔流、通行或竞速相关义 + way 通道，形成多种专门槽道名称。竞赛、水流、机械、电气的具体义项分别认，不把每个 raceway 都译赛车场。',C('race 奔流、通行、竞速相关义','way 通道','raceway','竞速赛道；水流或部件、线缆通道'),
 'a motor raceway 赛车道；a cable raceway 线缆槽道；在轴承等机械语境里还可指滚道。',
 'a motor raceway；a cable raceway；a bearing raceway。',
 'raceway 比较依赖技术语境，racehorse 明确是马；cable raceway 是布置线缆的通道，不是电线比谁跑得快。',
 ('The raceway hosted a weekend motor event.','赛车场周末举办了一场汽车赛事。'),('The cables run through a plastic raceway.','线缆穿过一条塑料线槽。'))
W('racial','/ˈreɪʃəl/','种族的；与种族有关的',
 '只说这件事涉及种族分类、身份或关系；本身还没说立场是支持还是反对歧视。',
 'race 的种族分支 + -ial，去 e，形成相关形容词；读音中 c 对应 /ʃ/，和 racism 中 /s/ 不同。',RA[1:]+[['race + -ial → racial','种族 → 与种族有关的']],
 'racial identity 种族身份，racial equality 种族平等，racial discrimination 种族歧视；被修饰的名词决定具体在讲什么。',
 'racial equality；racial identity；racial discrimination；racial diversity。',
 'racial 种族相关，racist 种族主义的；racial equality 种族平等恰恰不是 racist equality。',
 ('The course discusses racial identity in literature.','课程讨论文学中的种族身份。'),('The organisation works to promote racial equality.','这个组织致力于促进种族平等。'))
W('racism','/ˈreɪsɪzəm/','种族主义；种族歧视',
 '把人按种族分出高低、据此偏见对待，或让某些群体在制度、行为中持续处于不利位置。',
 '联系法语 racisme，现代可认 race 种族 + -ism 思想、做法。不是关于竞赛的一门理论，也不只限于当面骂人的话。',RA[1:]+[['法语 racisme；race + -ism → racism','种族分类 → 种族优劣观、歧视及相关结构实践']],
 'challenge racism 反对种族主义，institutional racism 制度层面的种族歧视；具体讨论会有不同理论框架，应看作者如何界定。',
 'challenge racism；institutional racism；experience racism；racism in sport。',
 'racism 是思想、行为、结构等问题，racist 可是形容词或持相关偏见的人；racial 则只是有关种族，评价不同。',
 ('The documentary examines racism in professional sport.','纪录片考察职业体育中的种族歧视。'),('Students discussed ways to challenge racism at school.','学生们讨论了如何反对校园里的种族歧视。'))
W('racist','/ˈreɪsɪst/','种族主义者；种族主义的、带种族歧视的',
 '可说持种族偏见、歧视立场的人，也可直接评价一句话、一项做法带有这类歧视。',
 'race 种族 + -ist，联系 racism 的人物、性质词。不是 racer 赛车手，也不是一切谈种族的人。',RA[1:]+[['race + -ist → racist','种族主义立场的人；带种族歧视的']],
 'a racist remark 带种族歧视的话，racist abuse 种族歧视性辱骂；作名词 a racist 是种族主义者。',
 'a racist remark；racist abuse；racist attitudes；a racist。',
 'racial 说明话题有关种族，racist 评价歧视性质；研究 racial history 的人，不因此就成为 racist。',
 ('The club condemned the racist abuse directed at the player.','俱乐部谴责了针对那名球员的种族歧视性辱骂。'),('The essay explains why the remark was racist.','文章解释了那句话为什么带有种族歧视。'))
W('racy','/ˈreɪsi/','生动有活力的；带性暗示、香艳的',
 '文字、故事很有味道、很带劲，现代还常暗示内容有点大胆、带性意味。',
 '来自 race 较旧的风味、品种特质义 + -y，较早用于酒、水果等有鲜明风味，后来有生动、有劲，再到大胆、带性暗示。不是竞速快所以有色情义。',
 [['旧 race 的风味、品种特质义 + -y → racy','风味鲜明、带活力的'],['英语 racy 的后续引申','生动鲜活 → 大胆、带性暗示的']],
 'a racy novel 香艳、情节大胆的小说，racy dialogue 大胆、有性暗示的对白；a racy style 在较传统文评里也可赞文风生动。',
 'a racy novel；racy dialogue；a racy style。',
 'racy 不等于 racial 种族的，也不是 racing 正在比赛；现代小说介绍里常先考虑大胆、性暗示义。',
 ('The review describes the novel as racy but well written.','书评说这部小说内容大胆，不过文笔很好。'),('The editor removed some racy dialogue from the family edition.','编辑从家庭阅读版中删去了一些带性暗示的对白。'),sources=['https://en.wiktionary.org/wiki/racy#English','https://www.etymonline.com/word/racy'])
R('B2805','竞速、比赛；另源的血统与种族词族','RACE：竞速和种族分两条来源','跑道上的 race 与社会话题中的 race 不强串；racer 是参赛者，racist 则完全是另一分支的人物、性质词。',
 '竞速分支接古英语、古诺尔斯语奔跑、奔流词族；种族分支经法语、意大利语来，更远不确定。racy 接旧风味、特质义，另列历史辨析。',
 '竞速 race → racer、racehorse、racetrack、raceway、racecourse；群体 race → racial、racism、racist；旧风味义 → racy。',
 [['竞速及场地','race · racer · racehorse · racetrack · racecourse · raceway'],['种族相关及歧视','racial · racism · racist'],['旧特质分支的固定词','racy']],
 'racer 不是 racist；racial 不等于 racist；racy 不从赛车刺激硬推，也不等于 racial。',
 'The racer joined a campaign against racism in sport.\n\n赛车手参加了反对体育中种族歧视的活动。',
 'race racer racehorse racetrack racecourse raceway racial racism racist racy')
if __name__=='__main__':save('continuation_20261029_cz',ROOTS,WORDS)
