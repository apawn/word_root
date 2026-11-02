"""Common processes, participles and ordinary verbs behind them."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1741':dict(words=['captivate','captivating','bruise','bruising','yield','yielding','gape','gaping','practise','practising','cheer','leader','cheerleader','cheerleading','merchandise','merchandising'],label='吸引、受挫、让步与行业活动的常见扩展',note='captivating 是令人着迷，bruising 可比喻激烈而令人受挫；yielding 既有让步也有柔软易受压的形容词义；practising 还指在执业、仍奉行某宗教的；merchandising 取 merchandise 动词义。'),
 'A1760':dict(words=['abort','aborted','water','watered'],label='中途终止与加水、浇水的完成形式',note='aborted 指被中止、提前终止；watered 接 water 的相应动词用法，watered down 又有稀释、削弱的比喻。'),
}
W('captivating','/ˈkæptɪveɪtɪŋ/','迷人的、令人着迷的',
 '故事、笑容、表演把人的注意力抓住，让人忍不住继续看。captivating 的画面就是心神被吸住了。',
 'captivate 使着迷 + -ing；更早拉丁语 captivare 俘获等与 capere 抓住同族。抓住人的材料进入吸引注意、感情的比喻。',
 [['capere、captivare 等抓住词族 → captivate','由俘获、抓住联系到使人着迷'],['captivate + -ing → captivating','具有吸住注意、感情的效果']],
 'a captivating story 迷人的故事；a captivating smile 迷人的笑容；a captivating performance 令人着迷的表演。',
 'a captivating voice；find something captivating。','captivating 描写带来吸引力的事物；captivated 常说人被迷住。The story is captivating；I’m captivated by the story。',
 ('She told a captivating story about her travels.','她讲了一个关于旅行的迷人故事。'),('The singer’s captivating voice held the audience’s attention.','歌手迷人的嗓音牢牢吸引着观众。'),sources=['https://www.etymonline.com/word/captivate','https://en.wiktionary.org/wiki/captivating#English'])
W('bruise','/bruːz/','瘀伤、青紫痕；碰伤、挫伤；伤害感情、自尊',
 '撞一下，表皮未必破，但里面受伤、留下青紫；水果被压也会出现软烂色斑。自尊被伤到，也借用 bruise。',
 '古英语 brysan 的压碎、挫伤材料与法语 bruiser 等击碎、压伤材料发生融合。现代动词说挫伤，名词说留下的瘀伤。',
 [['古英语与法语相关词的融合','压、击打、挫伤'],['现代 bruise 的身体、果实与情感义','瘀伤；水果碰伤；自尊等受挫']],
 'a bruise on the arm 手臂上的瘀伤；bruise easily 容易碰伤、产生瘀痕；bruise someone’s pride 伤了某人的自尊。',
 'a bruised apple；a bruised ego。','cut 常说割破、切开的伤口；bruise 侧重撞压造成的瘀伤，表面未必破。水果 bruised 也不等于已经完全腐烂。',
 ('He had a bruise on his knee after the fall.','摔倒后，他的膝盖上有一块瘀伤。'),('The apples bruise easily, so handle them gently.','这些苹果很容易碰伤，拿的时候轻一点。'),sources=['https://www.etymonline.com/word/bruise','https://en.wiktionary.org/wiki/bruise#English'])
W('bruising','/ˈbruːzɪŋ/','瘀伤、挫伤；激烈而令人受挫的',
 '具体是一片片瘀痕；比喻 a bruising debate，则像争辩中来回挨打，激烈、耗人、让人受挫。',
 'bruise + -ing；一支把挫伤作为过程、结果名称，一支形成造成伤害或严酷考验的形容词。',
 [['bruise 挫伤 + -ing','挫伤过程、瘀伤情况'],['bruising 的比喻形容词','激烈、严酷、让人受打击的']],
 'bruising on the skin 皮肤上的瘀伤；a bruising encounter 激烈冲突；a bruising election campaign 激烈而令人疲惫受挫的竞选。',
 'a bruising battle；signs of bruising。','bruising 可以说身体瘀伤，也可以评价竞争激烈；bruised 则通常看已经受伤、受挫的对象。',
 ('There was some bruising around his elbow.','他的手肘周围有些瘀伤。'),('The proposal survived a bruising debate.','这项提案在激烈争辩后得以保留。'))
W('aborted','英 /əˈbɔːtɪd/；美 /əˈbɔːrtɪd/','被中止的、提前终止的；abort 的过去式、过去分词',
 '事情还没按原计划走完，就被停下了。航行、起飞、发射、谈判等都可能被描述为 aborted。',
 'abort + -ed。abort 更早接拉丁语 aboriri、abortus 等未正常完成、流产的材料，英语扩展到提前中止行动。',
 [['较早 abort 的未完成、终止材料','未能或未让发展完成'],['abort + -ed → aborted','中止了；被提前终止的']],
 'an aborted takeoff 中止的起飞；an aborted mission 中止的任务；an aborted attempt 中途放弃的尝试。其他语境也可取生殖相关义。',
 'an aborted launch；the operation was aborted。','failed 是未成功，aborted 强调过程被中止，可能正是为了避免继续出错。事情被中止不等于所有环节都已失败。',
 ('The launch was aborted because of a technical fault.','由于技术故障，发射被中止了。'),('The report described an aborted attempt to reach the summit.','报告描述了一次中途放弃的登顶尝试。'),sources=['https://www.etymonline.com/word/abort','https://en.wiktionary.org/wiki/aborted#English'])
W('yield','/jiːld/','产出、带来；让步、屈服；产量、收益等〔名词〕',
 '地把收成给出来，人把坚持的位置让出来。把几支常见意思都抓成“交出、给出”，再看是给成果还是退让。',
 '古英语 gieldan 有支付、给予、回报等义，经中古英语 yelden 发展。英语后来形成产出、回报、交出控制、屈服等分支，不能把所有分支都硬说成同时新造。',
 [['古英语 gieldan → 中古英语 yelden','支付、给予、回报；交出'],['现代 yield 的多支发展','产出、带来；让步；相应产量、收益']],
 'yield a harvest 产出收成；yield results 带来结果；yield to pressure 向压力屈服；crop yield 作物产量；yield 也见于金融收益、收益率语境。',
 'yield useful information；a high crop yield。','give way 侧重退让，produce 侧重产出；yield 可以跨这两个方向，靠宾语和 to 等搭配判断。',
 ('The field yielded a good harvest.','那块田收成很好。'),('The search yielded several useful clues.','搜寻带来了几条有用线索。'),('She refused to yield to pressure.','她拒绝向压力屈服。'),sources=['https://www.etymonline.com/word/yield','https://en.wiktionary.org/wiki/yield#English'])
W('yielding','/ˈjiːldɪŋ/','易弯曲、受压变形的；顺从、肯让步的；正在产出等',
 '手按下去，材料让开一点，是 yielding；人遇到要求容易退让，也叫 yielding。作分词还可能只是说产出结果。',
 'yield + -ing；从让出、受力退让的动词形成柔软、肯让步的形容词，也保留产出的动词分支。',
 [['yield 让步、受力退让 + -ing','材料受压让开；人肯退让'],['yielding 的分词与形容词','柔软、顺从；也可说正在产出']],
 'soft, yielding ground 松软的地面；a yielding nature 易顺从的性格；yielding good results 带来好结果。',
 'a yielding surface；yielding to persuasion。','unyielding 常说坚硬、不肯让步；yielding 常说易受压或愿退让。好坏评价随场景而变，柔软材料不必是缺点。',
 ('Their feet sank into the soft, yielding ground.','他们的脚陷进松软的地面。'),('The new method is yielding promising results.','新方法正在取得令人鼓舞的结果。'),sources=['https://www.etymonline.com/word/yield','https://en.wiktionary.org/wiki/yielding#English'])
W('gape','/ɡeɪp/','张大嘴惊看；大大敞开',
 '看到惊人的东西，嘴巴不自觉地张开、盯着看，是 gape；一个裂口像嘴张着，也可以说 gape。',
 '中古英语 gapen 与古诺斯语 gapa 等张嘴材料相连，具体本族延续与借入分析有讨论。与 gap 缺口同族。',
 [['较早日耳曼、北欧张嘴词族 → 中古英语 gapen','把嘴张开'],['现代 gape 的人和开口用法','张嘴惊看；洞、裂口大大敞开']],
 'gape at someone 张着嘴惊看某人；gape in astonishment 惊得目瞪口呆；a hole gapes open 洞大大敞开。',
 'stand and gape；gape at the sight。','stare 是盯着看，gape 往往多出张嘴、惊讶或发愣的画面。不是给 gap 名词随意加一个 e 形成的现代规则。',
 ('We gaped at the enormous cake.','我们张着嘴，惊讶地看着那个巨大的蛋糕。'),('A large hole gaped in the roof.','屋顶上裂开了一个大洞。'),sources=['https://www.etymonline.com/word/gape','https://en.wiktionary.org/wiki/gape#English'])
W('gaping','/ˈɡeɪpɪŋ/','大张着的、大敞开的；巨大、明显的〔缺口等〕',
 '口子敞得很大，像张着嘴。a gaping hole 常能看见具体破洞，也能说计划里一个明显的大漏洞。',
 'gape 去末尾 e 加 -ing；由大大张开，形成开口宽大、缺失明显的状态描写。',
 [['gape 大张、敞开 + -ing','正在敞开、张嘴的'],['gaping 修饰缺口等','巨大敞口；明显严重的缺失']],
 'a gaping hole 大洞；a gaping gap 巨大缺口；gaping mouths 张大的嘴；gaping at something 张嘴惊看。',
 'a gaping hole in the argument；a gaping entrance。','gaping 更突出开口大、缺口显眼；empty 是里面没有东西。a gaping hole 也可以是论证中的明显漏洞。',
 ('The storm left a gaping hole in the roof.','风暴在屋顶上留下了一个大洞。'),('There is a gaping hole in his explanation.','他的解释里有一个明显的大漏洞。'))
W('watered','英 /ˈwɔːtəd/；美 /ˈwɔːtərd/〔也见 /ˈwɑːtərd/〕','浇了水、加了水；water 的过去式、过去分词',
 'water 作为动词可以给植物浇水，也可以往液体中加水。watered down 就是兑淡了，还能说内容、力度被削弱。',
 'water 名词转动词，再接 -ed；这些动词用法有较早英语历史。加水带来的稀释，后来借来形容内容、要求减弱。',
 [['water 名词 → 浇水、加水等动词','供水、兑水；另有眼睛流泪用法'],['water + -ed 与 watered down','完成的动作；被稀释、被削弱']],
 'freshly watered plants 刚浇过水的植物；watered milk 加了水的牛奶；watered down the proposal 削弱了提案的内容或力度。',
 'well watered；a watered down version。','watered 不只等于浇过花，要看 water 的动词义。eyes watered 则说眼里流泪，也不是往眼里浇水。',
 ('She watered the plants before leaving.','离开前，她给植物浇了水。'),('The final proposal had been watered down.','最终提案的力度已被削弱。'))
W('practising','/ˈpræktɪsɪŋ/','练习、从事；执业的；仍奉行某宗教的〔英式拼写〕',
 '正在练技能是 practising；a practising lawyer 是在执业的律师；a practising Catholic 则是实际奉行信仰的天主教徒。',
 'practise 去末尾 e 加 -ing，承接实行、从事、反复练习等词义。英式常区分动词 practise 与名词 practice；美式动词通常也写 practice。',
 [['practise 实行、练习 + -ing','正在实行、练习'],['practising 的人物状态用法','正在执业的；实际奉行宗教的']],
 'practising the piano 练钢琴；a practising doctor 执业医生；a practising Buddhist 实际奉行信仰的佛教徒。美式通常写 practicing。',
 'keep practising；a practising architect。','a practising doctor 不是实习医生，重点是正在从事这一职业；练习义与执业义取 practise 的不同常见分支。',
 ('She is practising the piano upstairs.','她正在楼上练钢琴。'),('He worked as a practising architect for many years.','他从事建筑师工作多年。'))
W('cheerleading','英 /ˈtʃɪəliːdɪŋ/；美 /ˈtʃɪrliːdɪŋ/','啦啦队活动、竞技啦啦操；热情支持、鼓吹〔比喻〕',
 '把口号、舞蹈、技巧动作等组织起来，为队伍助威或参加比赛。比喻时，也说为某事积极叫好、鼓动支持。',
 'cheerlead + -ing，与 cheer 助威、leader 领头者、cheerleader 啦啦队员同族。活动名称同时保留助威和现代竞技运动的发展。',
 [['cheer、lead、cheerleader 等助威词族','带领、组织为队伍加油'],['cheerlead + -ing → cheerleading','啦啦队活动；比喻热情鼓动支持']],
 'a cheerleading team 啦啦队；a cheerleading competition 竞技啦啦操比赛；political cheerleading 为政治人物或政策热情站台。',
 'competitive cheerleading；uncritical cheerleading。','cheerleading 可以是有技巧、编排和竞赛的运动；比喻义有时暗含只顾叫好、缺少审视，要看上下文。',
 ('She joined the school’s cheerleading team.','她加入了学校啦啦队。'),('The article offered analysis rather than simple cheerleading.','那篇文章提供了分析，而不只是热情叫好。'),sources=['https://en.wiktionary.org/wiki/cheerleading#English'])
W('merchandising','英 /ˈmɜːtʃəndaɪzɪŋ/；美 /ˈmɜːrtʃəndaɪzɪŋ/','商品销售推广、陈列促销；角色、品牌周边商品的经营',
 '让商品更好卖：怎样摆、怎样展示、怎样配合促销。影视语境里，也常说把角色、标志做成玩具、衣服等周边来卖。',
 'merchandise 动词经营、销售商品 + -ing；更早词族经法语联系商人、货品、贸易。后来发展出零售推广和品牌周边经营等用法。',
 [['merchandise 的贸易、商品词族与动词','经营、销售商品'],['merchandise + -ing → merchandising','销售推广、陈列；品牌或作品周边经营']],
 'visual merchandising 视觉陈列；retail merchandising 零售商品经营推广；film merchandising 电影周边商品经营。',
 'a merchandising strategy；merchandising rights。','merchandise 作名词常指货品，merchandising 常说经营、展示、推广活动。品牌周边语境也可能把相关商品经营合在一起谈。',
 ('She is responsible for visual merchandising in the store.','她负责这家店的视觉陈列。'),('The studio earns money from film merchandising.','那家电影公司通过电影周边商品经营赚钱。'),sources=['https://en.wiktionary.org/wiki/merchandising#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_ts',ROOTS,WORDS)
    extend_lessons()
