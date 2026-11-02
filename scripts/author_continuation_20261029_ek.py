"""Range and rate: spread, assessment and the separate scolding verb."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
RA=[['古法语 renc、rang 行列 → rengier 排列 → 英语 range','排成一行、布置'],['现代 range','一列 → 连续范围；活动、可及距离与分布']]
W('range','/reɪndʒ/','范围；一系列；山脉；射程；从……到……变化',
 '把东西按一列展开，就能看见它从这一头到那一头覆盖多大范围；商品、数字、距离都可以这样看。',
 '经古法语行列、排列相关词进入英语，现代名词、动词有连续范围、排列、活动区域等分支。不是 rain 雨加 ge。',RA,
 'a range of products 一系列产品，a price range 价格范围，a mountain range 山脉；range from A to B 从 A 到 B 不等。',
 'a range of；range from...to...；within range；a mountain range。',
 'range 可以是一组多样选择，rank 更强调等级、排名；out of range 超出可及范围，不只是东西排列错了。',
 ('The shop offers a wide range of sizes.','商店提供多种尺码。'),('Prices range from ten to fifty pounds.','价格从十英镑到五十英镑不等。'))
W('ranger','英 /ˈreɪndʒə/；美 /ˈreɪndʒər/','护林员；公园巡护员；特定军职称呼',
 '在一片区域中巡护、管理的人；自然公园里常负责保护、介绍环境和帮助游客。',
 'range 巡行、活动 + -er，形成相关人员名词。军事中的 ranger 是特定部队、职责名称，不与每位护林员混作同一身份。',RA+[['range + -er → ranger','巡行区域的人 → 巡护员等']],
 'a park ranger 公园巡护员，a forest ranger 护林员；具体工作由机构职责决定。',
 'a park ranger；a forest ranger；ask a ranger。',
 'ranger 公园人员并非一定只是警察或导游；rancher 牧场主是另一词，别被相近拼写带偏。',
 ('A park ranger explained why the trail was closed.','公园巡护员解释了步道关闭的原因。'),('The forest ranger checked the area after the storm.','风暴过后，护林员检查了这片区域。'))
W('rangefinder','英 /ˈreɪndʒfaɪndə/；美 /ˈreɪndʒfaɪndər/','测距仪',
 '帮助你知道目标离自己多远的仪器，不是查商品种类的搜索器。',
 'range 距离 + finder 测定、寻找者，按测定距离的作用命名。不同仪器可能用光学或电子方法。',RA+[['range + finder → rangefinder','测定距离的器具 → 测距仪']],
 'a laser rangefinder 激光测距仪，use a rangefinder 测距离；用于测绘、运动、摄影等不同领域。',
 'a laser rangefinder；an optical rangefinder；use a rangefinder。',
 'rangefinder 测距离，viewfinder 取景器看构图；相机相关设备不都做同一件事。',
 ('The surveyor used a rangefinder to measure the distance.','测量员用测距仪测量距离。'),('The camera has a built-in rangefinder.','这台相机内置测距装置。'))
W('downrange','/ˌdaʊnˈreɪndʒ/','朝射击、发射方向的；沿发射方向下游',
 '站在发射点看，沿目标、飞行方向那一头，是相对于起点的下游方向。',
 'down 沿既定方向向前 + range 射击、飞行范围，形成特定方向表达；不是往低海拔，也不是价格下降。',RA+[['down + range → downrange','沿射击、发射方向向前']],
 'a downrange station 沿飞行方向的跟踪站，farther downrange 更沿前方；可作副词和形容词。',
 'a downrange station；farther downrange；downrange tracking。',
 'downrange 要有发射、射击等方向背景，不泛指任何在下方的区域。',
 ('A tracking station farther downrange received the signal.','沿飞行方向更远处的一座跟踪站收到了信号。'),('The report mapped the downrange observation sites.','报告标出了沿发射方向的观测点。'))
R('B3804','范围、距离与巡护','RANGE：把一列展开，看两端覆盖多远','range 多种范围义先讲，ranger 讲在区域巡行的人，rangefinder 讲测距；downrange 是较专门的方向词。',
 '历史接法语行列、排列词族。rangeland 牧场草地已有精讲，可以连接空间与活动范围。',
 'range → ranger；range + finder → rangefinder；down + range → downrange；range + land → rangeland。',
 [['基本范围与人员','range · ranger'],['距离、方向与土地','rangefinder · downrange · rangeland']],
 'range 范围、系列，rank 等级；rangefinder 测距，不等于取景器；downrange 不只是下方。',
 'The ranger used a rangefinder to measure the gap.\n\n巡护员用测距仪测量间距。',
 'range ranger rangefinder downrange rangeland')
RT=[['拉丁 rata 规定、核定的部分 → 法语、英语 rate','固定份额、数值 → 比率、价格、评估'],['现代 rate','单位数量的量、频率；评价高低'],['另一路 rate 斥责 → berate','斥责词远源不明；不从比率硬推出来']]
W('rate','/reɪt/','比率；速度、频率；费用；评价',
 '通常要问每多少单位有多少：每小时多少钱、每分钟多少次。作动词则是给水平、质量打评价。',
 '比率、核定数值词经法语等接拉丁 rata 规定份额，关联 reri 计算、判断。旧的斥责动词 rate 另源不明，留在 berate 中。',RT,
 'an hourly rate 每小时收费，a growth rate 增长率，rate a film 给电影评分；at this rate 照这样下去。',
 'an hourly rate；a growth rate；rate highly；at this rate。',
 'rate 往往要有分母或比较基准，total 总量不一样；high birthrate 高出生率不等于总人口必然世界最多。',
 ('What is your hourly rate?','你每小时收费多少？'),('How would you rate the service?','你会怎样评价这项服务？'))
W('rater','英 /ˈreɪtə/；美 /ˈreɪtər/','评分者；评定人员',
 '拿着同一套标准，对答案、表现或作品给分的人。',
 'rate 去末尾 e，加完整表人后缀 -er，成为 rater。主要接评估、评分动词义。',RT[:2]+[['rate + -er → rater','执行评价的人 → 评分者']],
 'independent raters 独立评分者，a trained rater 受训评分员；研究中常比较不同评分者的一致性。',
 'independent raters；a trained rater；agreement between raters。',
 'rater 评分者，不是评分得到的 rating 分数、评级；两者在句子里所指不同。',
 ('Two independent raters assessed each answer.','两名独立评分者评估了每份答案。'),('The raters used the same scoring guide.','评分人员使用同一份评分指南。'))
W('underrate','英 /ˌʌndəˈreɪt/；美 /ˌʌndərˈreɪt/','低估；评价过低',
 '实际本事、价值比给出的评价更高，是你把它看低了。',
 'under- 低于应有程度 + rate 评价。不是只说某物费用便宜，重点是判断低估。',RT[:2]+[['under- + rate → underrate','给出过低评价 → 低估']],
 'underrate someone’s ability 低估能力，an underrated film 被低估的电影；常见分词 underrated。',
 'underrate ability；an underrated film；underrate the importance of。',
 'underrate 低估，overrate 高估；underpay 是少付钱，不能只因都带 under 互换。',
 ('Do not underrate the importance of a clear plan.','不要低估清晰计划的重要性。'),('Many critics initially underrated the film.','许多评论者起初低估了这部电影。'))
W('ratepayer','英 /ˈreɪtpeɪə/；美 /ˈreɪtpeɪər/','地方税缴纳者；公共事业付费用户',
 '根据某类 rates 费用缴款的人；在英国常见地方税背景，在美国报道也可能说水、电等服务用户。',
 'rate 的 rates 地方税、费率分支 + payer 支付者。不同地区制度不同，不能统一只译成纳税人。',RT[:2]+[['rate + payer → ratepayer','按相应税、费缴款的一方']],
 'local ratepayers 地方税缴纳者，electricity ratepayers 电力付费用户；先看国家、行业上下文。',
 'local ratepayers；electricity ratepayers；the cost to ratepayers。',
 'taxpayer 泛指纳税人，ratepayer 受 rates 的具体地区、费用义限制；电费用户不等于因电费就缴了税。',
 ('The council discussed the cost to local ratepayers.','地方议会讨论了本地缴税者承担的成本。'),('The utility said the change would benefit ratepayers.','公用事业公司表示，改动将使付费用户受益。'))
W('berate','/bɪˈreɪt/','严厉斥责；痛骂',
 '不是普通提醒一下，而是带着很强的责备，狠狠说对方一通。',
 'be- + rate 旧义斥责，后者来源不明；不接费率、评分那条拉丁来源，不解释成给人打低分就变痛骂。',RT[2:]+[['be- + rate（斥责）→ berate','加强斥责 → 严厉训斥']],
 'berate someone for something 因某事严厉责备某人；不需要再加 at。',
 'berate someone for；publicly berate；berate yourself。',
 'criticize 批评可理性、温和，berate 通常态度强烈；不要把所有指出错误都夸大成 berate。',
 ('He berated himself for forgetting the appointment.','他因忘记约会而狠狠责怪自己。'),('The manager berated the team for missing the deadline.','经理因团队错过截止日期而严厉训斥大家。'))
R('B3138','比率、费用与评价；另源严厉斥责','RATE：每单位多少；评价多高；BERATE 另源','rate 的数值、评价先接 rater、underrate；ratepayer 看费用。berate 单列旧斥责词。',
 '数值义接拉丁规定份额词；berate 的 rate 旧斥责义来源不同且不明确，不能用相似拼写制造一条确定演化。',
 'rate → rater、underrate；rate + payer → ratepayer；共享 bitrate、birthrate；另源 be- + rate → berate。',
 [['数值与评价','rate · rater · underrate'],['费用与数量复合词','ratepayer · bitrate · birthrate'],['另源斥责','berate']],
 'rate 比率不等于 total 总量；ratepayer 因地区、行业有不同所指；berate 不是比率词的直接义变。',
 'The rater warned us not to underrate the new approach.\n\n评定人员提醒我们不要低估新方法。',
 'rate rater underrate ratepayer bitrate birthrate berate')
if __name__=='__main__':save('continuation_20261029_ek',ROOTS,WORDS)
