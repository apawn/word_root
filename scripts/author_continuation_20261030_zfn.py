"""Pouncing, bouncing, skipping and quick or smooth movement."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C1169':dict(words='pounce pounces pounced pouncing'.split(),label='pounce：从尖爪攫取到猛扑、迅速抓住',note='猛扑 pounce 联系较早猛禽尖爪与穿刺工具材料，古法语中间来源有不确定部分；粉末旧义另接浮石来源。现代本组聚焦常用猛扑、抓住机会义。'),
 'B3903':dict(words='bounce bounces bounced bouncing'.split(),label='bounce：反弹、退回与恢复活力',note='bounce 接中古英语打击材料，远源未定，弹回义后来发展；现代球反弹、邮件退回、bounce back 恢复等分别给出场景。'),
 'B2438':dict(words='leap leaps leapt leaped leaping'.split(),label='leap 的跳跃动作与大步变化',note='leap 承古英语跳、跑材料，名词也有古英语对应；leaps 的大幅进步不全是今天临时把动词变名词。'),
 'B3499':dict(words='hop hops hopped hopping'.split(),label='hop：短跳、短途移动；植物支线另分',note='跳跃词接古英语 hoppian，啤酒花名词另借中古荷兰语 hoppe；hopped、hopping 双写 p，不和希望 hope 的去 e 变化混淆。'),
 'B4334':dict(words='skip skips skipped skipping'.split(),label='skip 的轻跳、跳过和不同名词支线',note='轻跳、略过接北欧相关材料，废料斗名词另接筐、容器词；队长简称 skip 又接 skipper。现代同形 -s 不等于同一词源。'),
 'C0163':dict(words='scamper scampers scampered scampering'.split(),label='scamper 可能从离开场地到快步跑开',note='scamper 可能经弗拉芒语、法语逃离材料接俗拉丁语 *excampare，涉及 campus 场地；具体借入有不确定性，现代不可直接拆成 scam 加人物 -er。'),
 'B3301':dict(words='dash dashes dashed'.split(),label='dash 的急冲、打碎与短横符号',note='dash 的旧猛击、急冲义有北欧来源分析；dashed hopes 是希望像被打碎，dashes 另可指破折号、少量添入。'),
 'A1697':dict(words='sprint sprints sprinted sprinting glide glides glided gliding'.split(),label='sprint、glide 基础动作与人物工具派生的上下文',note='本组补 sprinter、glider 等已有讲解周边的基础动作变化；sprint、glide 自身不是人物 -er 派生词。glided 的完整 -ed 读 /ɪd/。'),
 'A1760':dict(words='pounce pounces pounced pouncing bounce bounces bounced bouncing leap leaps leaping hop hops hopped hopping skip skips skipped skipping scamper scampers scampered scampering scurry scurries scurried scurrying dash dashes dashed sprint sprints sprinted glide glides glided'.split(),label='扑跳、急跑、滑行的现代变化',note='pounced、bounced、hopped、skipped、dashed 的 -ed 读 /t/；scampered、scurried 读 /d/；sprinted、glided 读 /ɪd/。'),
}
POUNCE=[['较早猛禽尖爪、穿刺工具材料 → 用爪攫取的 pounce','可能经古法语相关尖工具词，上溯穿刺词族'],['攫取 → 突然扑上去 → 迅速抓住机会、错误','现代 pounce on 常像盯准了目标就马上动手']]
W('pounces','/ˈpaʊnsɪz/','猛扑、迅速抓住〔第三人称单数〕；猛扑动作〔复数〕',
 '猫盯住小球，忽然压身弹过去，是 pounces；有人话一出口就被抓住漏洞，也像被人盯准后扑上来。',
 'pounce + -s，基础末尾 ce 已有 e，直接加 s；/s/ 后读 /ɪz/。近源围绕猛禽尖爪、攫取材料，不是现代跳跃词的任意混成。',POUNCE+[['pounce + -s → pounces','它猛扑；他、她迅速抓住；几次猛扑']],
 'pounces on a toy 是扑向玩具，pounces on a mistake 是马上抓住错误不放；常用 on 或 upon 接目标。',
 'pounces from hiding 从藏身处扑出；pounces on the chance 马上抓住机会。',
 'pounces 比 jumps 更像针对一个目标突然扑上去；jumps 可以只是原地起跳，未必想抓什么。',
 ('The kitten pounces on the moving string.','小猫扑向移动的绳子。'),('She pounces on any chance to practise her French.','她一有机会就赶紧练法语。'),sources=S('pounces','pounce'))
W('pounced','/paʊnst/','猛扑了；迅速抓住机会、错误等了',
 '刚才突然扑向目标，是 pounced；听见一句能利用的话便马上抓住，也可以 pounced on it。',
 'pounce 去末尾不发音 e + 完整 -ed → pounced，/s/ 后读 /t/，结尾 /nst/。',POUNCE+[['pounce 去 e + -ed → pounced','过去猛扑、迅速攫取']],
 'pounced on the ball 是扑向球，pounced on the error 是立刻抓住错误；动作与比喻用同一个目标方向。',
 'pounced out from behind the chair 从椅后扑出来；pounced on an opportunity 抓住机会。',
 'pounced on an error 常显得反应快、抓得紧，也可能带批评急切的语气；noticed an error 只说注意到错误。',
 ('The cat pounced on the toy mouse.','猫扑向了玩具老鼠。'),('The editor pounced on the inconsistency in the story.','编辑马上抓住了故事里前后不一致的地方。'),sources=S('pounced','pounce'))
W('pouncing','/ˈpaʊnsɪŋ/','正在猛扑、迅速抓住；猛扑的',
 '猫身子压低后一下跃向猎物，是 pouncing；人急着抓别人一句话里的漏洞，也像等准时机就扑。',
 'pounce 去末尾 e + 完整 -ing → pouncing；c 在 i 前仍读 /s/，动作朝明确目标展开。',POUNCE+[['pounce 去 e + -ing → pouncing','猛扑、抓住机会等的过程']],
 'pouncing on a ball 是正扑球，pouncing on every mistake 是一有错就抓住；后者常带紧盯、急切的感觉。',
 'a pouncing cat 猛扑中的猫；pouncing from cover 从掩蔽处扑出。',
 'pouncing 通常带突然扑取的方向，leaping 只保证跳跃；向上跃过水坑可以 leaping，不必像捕猎。',
 ('The kitten practised pouncing on a feather.','小猫练习扑向一根羽毛。'),('He kept pouncing on every slip of the tongue.','他一直抓着每一次口误不放。'),sources=S('pouncing','pounce'))
BOUNCE=[['中古英语 bounsen 的捶击材料 → bounce','来源未定，可能借德荷相关词或拟声；弹回义后来发展'],['碰撞弹回 → 消息退回、支票退回、状态恢复','现代不同搭配抓住被弹回或重新弹起的画面，不作唯一词史先后']]
W('bounces','/ˈbaʊnsɪz/','弹起、反弹、跳动、退回〔第三人称单数〕；反弹次数〔复数〕',
 '球撞地后重新弹起来，是 bounces；邮件没送达又退回，也像被对面弹回来了。几个来回反弹则是名词复数。',
 'bounce + -s，基础已有末尾 e，直接加 s；/s/ 后读 /ɪz/，动词三单与名词复数同形。',BOUNCE+[['bounce + -s → bounces','它弹回、退回；几次反弹']],
 'bounces off the wall 是撞墙弹回，email bounces 是邮件退回；bounces back 可说受挫后重新恢复。',
 'bounces up and down 上下弹跳；count the bounces 数反弹次数。',
 'bounces 常包含接触后弹回的感觉，leaps 更像主动发力跃起；皮球自己弹起会 bounce，不需像人主动蹬地。',
 ('The ball bounces higher on the hard floor.','球在硬地板上弹得更高。'),('The message bounces back whenever I use that address.','我每次用那个地址，邮件都会被退回来。'),sources=S('bounces','bounce'))
W('bounced','/baʊnst/','弹起、反弹了；被退回了；跳动、恢复了',
 '球落地后弹了一下，是 bounced；邮件被退回，也是 bounced。bounce back 则像被压低后重新弹起，说恢复过来。',
 'bounce 去末尾 e + 完整 -ed → bounced，/s/ 后读 /t/，结尾 /nst/；不是 /ɪd/。',BOUNCE+[['bounce 去 e + -ed → bounced','过去反弹；消息等未被接收而退回']],
 'bounced off the wall 是从墙上弹回，the email bounced 是邮件退回；bounced back from defeat 是从失败中恢复。',
 'bounced on the bed 在床上弹跳了；bounced a ball 拍了球。',
 'bounced back 常关注恢复能力，went back 只说回去；恢复状态可以不涉及回到一个地方。',
 ('The ball bounced twice before he caught it.','球弹了两下，他才接住。'),('Our email bounced because the address was no longer active.','那个地址已停用，我们的邮件被退回了。'),sources=S('bounced','bounce'))
W('bouncing','/ˈbaʊnsɪŋ/','正在弹跳、反弹；活泼健壮的；弹跳动作',
 '球正一下一下弹，孩子在软垫上蹦，是 bouncing。a bouncing baby 则让人想到结实、有活力的宝宝，是固定形容用法。',
 'bounce 去末尾 e + 完整 -ing → bouncing；分词描写弹跳，健壮、有活力的形容义较早已固定。',BOUNCE+[['bounce 去 e + -ing → bouncing','反复弹起的过程；旺盛、有活力的形容']],
 'bouncing a ball 是正在拍球，bouncing on the bed 是在床上蹦；a bouncing baby 是健壮活泼的宝宝。',
 'keep the ball bouncing 让球继续弹；bouncing back 恢复状态。',
 'bouncing baby 不保证宝宝此刻真的蹦，词可以形容旺盛活力；bouncing on a bed 则直接是在描述动作。',
 ('The children were bouncing on the soft play mat.','孩子们正在柔软的游戏垫上蹦跳。'),('She was bouncing the ball while she waited.','她等着的时候一直在拍球。'),sources=S('bouncing','bounce'))
LEAP=[['古英语 hleapan 与相关跳跃名词 → leap','动词古义也有跑、行进；名词本身也有早期来源'],['身体越过距离 → 明显跃进、思路跳步','现代大幅变化像从一点直接跳到更远一点']]
W('leaps','/liːps/','跳跃、猛增〔第三人称单数〕；跳跃、大幅进步或变化〔复数〕',
 '人或动物一下跃过距离，动词用 leaps；进展不是一点点挪，而是一段一段大步前进，也能叫 leaps。',
 'leap + -s，/p/ 后读 /s/；动词三单与跳跃名词复数同形。名词也有古英语来源，并非一定在现代动词后才造出。',LEAP+[['leap + -s → leaps','它跃起、猛增；多次跳跃或大步变化']],
 'leaps over a wall 是跃过墙，by leaps and bounds 是突飞猛进；leaps in understanding 是理解上的大步提升。',
 'leaps into action 一跃而起行动；great leaps forward 巨大进步。',
 'leaps 常有跨越一段距离或阶段的幅度，steps 更能强调一步一步；用于进展时，一个像跃进，一个像逐步。',
 ('The deer leaps over the low fence.','鹿跃过低矮围栏。'),('Her confidence has grown by leaps and bounds.','她的信心突飞猛进。'),sources=S('leaps','leap'))
W('leaping','/ˈliːpɪŋ/','正在跳跃、跃过；跃起的；快速增长、跳步推断',
 '身体用力一下离地、跨过距离，是 leaping；思路一下跨到结论，也像把中间几步直接跳过去。',
 'leap + 完整 -ing，直接加；ea 的 /iː/ 保留，分词可讲实际跳跃，也可接已有比喻搭配。',LEAP+[['leap + -ing → leaping','身体或思路跨过中间距离的过程']],
 'leaping over a ditch 是跃过沟，leaping to conclusions 是急着下结论；leaping at the chance 是迫不及待抓住机会。',
 'leaping into the air 跃向空中；a leaping salmon 跃起的鲑鱼。',
 'leaping to conclusions 往往暗含中间证据没核实，reaching a conclusion 只是得出结论；跳步感让前者容易带批评。',
 ('We watched fish leaping out of the water.','我们看着鱼跃出水面。'),('You are leaping to conclusions before hearing the whole story.','事情还没听完整，你就急着下结论了。'),sources=S('leaping','leap'))
HOP=[['跳跃支线：古英语 hoppian → hop','短跳、单脚跳，后来也说轻快短途移动'],['植物支线：中古荷兰语 hoppe → hop、hops','啤酒花另一路借入；不能从上下跳的动作直接推出植物名']]
W('hops','英 /hɒps/；美 /hɑːps/','跳、轻快短途移动〔第三人称单数〕；短跳、短途行程〔复数〕；啤酒花',
 '鸟在地面上一下一下跳，是 hops；啤酒配料里的 hops 则是啤酒花，属于另一条词源，不是花在跳。',
 'hop + -s，/p/ 后读 /s/；跳跃三单、动作名词复数与植物复数同形。啤酒花通常用复数 hops。',HOP+[['hop + -s → hops','它跳；几次短跳；另一来源的啤酒花']],
 'hops on one foot 是单脚跳，short hops 是几段短途；beer made with hops 则说啤酒花原料。',
 'hops from branch to branch 在枝头间跳；aromatic hops 有香气的啤酒花。',
 'hops 与 hopes 希望差一个 e，发音也不同；hops 的元音较短，hop 的过去式要双写 p。',
 ('The bird hops along the garden path.','鸟沿花园小路一下一下跳。'),('The brewer added hops to the mixture.','酿酒师往混合液里加入啤酒花。'),sources=S('hops','hop'))
W('hopped','英 /hɒpt/；美 /hɑːpt/','跳了、轻快上去或短途去了；〔酿造〕加了啤酒花的',
 '刚才单脚跳、轻巧跳上车，用 hopped；说 hopped on a bus 常就是赶紧上公交。酿造里的 hopped 又属于啤酒花动词支线。',
 'hop 双写 p + 完整 -ed → hopped，/p/ 后读 /t/；跳跃和加啤酒花两条同形动词都可按这个规则变化。',HOP+[['hop 双写 p + -ed → hopped','过去跳、短途移动；另一支为添加啤酒花']],
 'hopped over a puddle 是跳过水坑，hopped on the bus 是迅速上公交；a heavily hopped beer 是用了较多啤酒花的啤酒。',
 'hopped onto the wall 跳上墙；hopped from one topic to another 话题轻快地换来换去。',
 'hopped 是 hop 的过去式，hoped 是 hope 的过去式；前者短元音且双 p，后者英 /həʊpt/、美 /hoʊpt/。',
 ('She hopped over the puddle without getting her shoes wet.','她跳过水坑，没有弄湿鞋子。'),('We hopped on a bus to the station.','我们赶紧上了一辆去车站的公交车。'),sources=S('hopped','hop'))
W('hopping','英 /ˈhɒpɪŋ/；美 /ˈhɑːpɪŋ/','正在跳、轻快辗转；跳跃；〔hopping mad〕气得跳脚',
 '单脚一下一下跳，或鸟在树枝间挪跳，是 hopping；hopping mad 把生气画成跳脚，表示气坏了。',
 'hop 双写 p + 完整 -ing → hopping；短元音保留。hope 去 e 加 -ing 成 hoping，是另一词、另一发音。',HOP+[['hop 双写 p + -ing → hopping','短跳的过程；气得跳脚的固定搭配']],
 'hopping on one leg 是单腿跳，hopping from place to place 是在各处轻快辗转；hopping mad 是非常愤怒。',
 'hopping over stones 跳过石头；keep hopping 继续跳。',
 'hopping 与 jumping 有重叠，hop 常是短跳、单脚跳或小动物跳；hopping mad 只说明很生气，不保证真的离地跳起来。',
 ('The children were hopping on one leg along the line.','孩子们正沿着那条线单腿跳。'),('He was hopping mad when he found the broken model.','发现模型坏了，他气得跳脚。'),sources=S('hopping','hop'))
SKIP=[['中古英语 skippen，可能借北欧跳跃材料 → skip','轻快跳动、跳过障碍，也较早有略过内容的用法'],['动作、略过分支继续发展；容器与队长另分近源','废料斗名词接筐、容器材料；队长 skip 是 skipper 的简称']]
W('skips','/skɪps/','轻跳、跳过、略过、不参加〔第三人称单数〕；轻跳、跳过处；废料斗〔复数〕',
 '小孩一蹦一跳走，叫 skips；读书直接略过一段，也像把中间那一段跳掉。英国工地的 skips 则是装废料的大斗，来源另分。',
 'skip + -s，/p/ 后读 /s/；轻跳、略过三单与若干不同来源名词的复数同形，要按语境辨。',SKIP+[['skip + -s → skips','它跳过；几次跳动；另一支多个废料斗']],
 'skips breakfast 是不吃早餐，skips a paragraph 是跳过一段，skips down the path 是沿路蹦跳；rubbish skips 是废料斗。',
 'skips a step 跳过一步；skips school 不去上学、逃学。',
 'skips 常带原本有个顺序、环节却没经过的感觉；forgets 说忘记，skip 可能有意，也可能无意，不能单凭词定原因。',
 ('She sometimes skips breakfast when she is in a hurry.','她赶时间时有时不吃早餐。'),('The child skips along the path beside his father.','孩子在爸爸身边沿小路一蹦一跳地走。'),sources=S('skips','skip'))
W('skipped','/skɪpt/','轻跳、跳过、略过、不参加了',
 '刚才从一个环节直接到下一个，中间没做，用 skipped；身体一蹦一跳，或石头在水上弹过，也可用它。',
 'skip 双写 p + 完整 -ed → skipped，/p/ 后读 /t/；是规则过去式，不改变基础短元音。',SKIP+[['skip 双写 p + -ed → skipped','过去轻跳；跳过某部分或没参加']],
 'skipped a page 是跳过一页，skipped the meeting 是没参加会议；skipped across the water 可说石头弹过水面。',
 'skipped a beat 心跳像漏了一拍；skipped to the end 直接跳到末尾。',
 'skipped the lesson 说没参加那节课，left the lesson 可能已参加后离开；是否中途离开不能靠 skip 自动推出。',
 ('I accidentally skipped a page while reading.','我读的时候不小心跳过了一页。'),('The flat stone skipped across the water.','扁石头在水面上弹跳着掠过。'),sources=S('skipped','skip'))
W('skipping','/ˈskɪpɪŋ/','正在轻跳、跳过、略过；跳绳；轻跳动作',
 '人一蹦一跳向前，或绳子转过脚下一次次跳，是 skipping；读文直接跳过部分内容，同样保留越过中段的感觉。',
 'skip 双写 p + 完整 -ing → skipping；可作动作分词或名词，英式 skipping 常用来指跳绳。',SKIP+[['skip 双写 p + -ing → skipping','轻跳、略过的过程；跳绳活动']],
 'skipping rope 可说跳绳活动，也可指跳绳用的绳；skipping meals 是不吃某些餐，skipping the introduction 是略过导言。',
 'a skipping rope 一根跳绳；skipping ahead 先跳到后面。',
 'skipping 的轻跳常有一跳一步的轻快节奏；hopping 更常让人想到短跳、单脚跳，两者在普通跳动场景里也可重叠。',
 ('The children were skipping rope in the playground.','孩子们正在操场上跳绳。'),('She was skipping the long descriptions to follow the story.','她正略过冗长描写，顺着情节往下读。'),sources=S('skipping','skip'))
SCAMPER=[['可能经弗拉芒语、古法语逃离材料 → scamper','更远或接俗拉丁语 *excampare，像离开场地、逃离战场'],['急速跑开 → 轻快小步奔跑','现代常见于小动物、小孩跑来跑去，重点不只是否在逃命']]
W('scamper','英 /ˈskæmpə/；美 /ˈskæmpər/','轻快小跑、急忙跑开；轻快奔跑',
 '松鼠几下窜上树，小孩一听可以玩就跑开，是 scamper：腿脚轻快，一连串小步迅速过去。',
 '可能经弗拉芒语的逃跑反复形式、古法语 escamper 接俗拉丁语 *excampare 离开场地；这是候选借入链，现代整词表示快跑。',SCAMPER,
 'scamper away 是轻快跑开，scamper up a tree 是窜上树，a quick scamper 是一阵轻快小跑；常见于动物和小孩。',
 'scamper across the grass 轻快跑过草地；scamper off to play 一溜跑去玩。',
 'scamper 比 run 更有轻快、短促小步的画面，sprint 更强调短距离全速冲；快跑不一定都用同一种词。',
 ('We watched the squirrel scamper up the tree.','我们看着松鼠轻快地窜上树。'),('The children were ready to scamper off to the playground.','孩子们已经准备好一溜跑去操场。'),sources=S('scamper','scamper'))
W('scampers','英 /ˈskæmpəz/；美 /ˈskæmpərz/','轻快小跑、急忙跑开〔第三人称单数〕；轻快小跑〔复数〕',
 '一只小动物小腿飞快地动，几下就跑远，是 scampers；人也能轻快跑过去，但常带活跃、步子小而快的感觉。',
 'scamper + -s，读 /z/；常用作动词三单，快速小跑也可当可数动作。',SCAMPER+[['scamper + -s → scampers','它轻快跑动；几次急速小跑']],
 'scampers across the lawn 是轻快跑过草坪，scampers up the trunk 是窜上树干；方向常接在动词后。',
 'scampers away 一溜跑开；scampers under the fence 窜过围栏下面。',
 'scampers 常让镜头关注快速的小步子，walks 只是走，runs 则更中性；说松鼠、小狗时这个动作很有画面。',
 ('The squirrel scampers along the wall.','松鼠沿墙头轻快地跑。'),('The little boy scampers upstairs when he hears his sister.','小男孩一听见姐姐的声音，就轻快地跑上楼。'),sources=S('scampers','scamper'))
W('scampered','英 /ˈskæmpəd/；美 /ˈskæmpərd/','轻快小跑、急忙跑开了',
 '刚才小动物一溜跑走，或小孩兴冲冲跑过院子，是 scampered。它把步子快、小而轻的样子带进叙述。',
 'scamper + 完整 -ed，读 /d/；基础 er 保留，不是删去人物后缀再变过去式。',SCAMPER+[['scamper + -ed → scampered','过去快速、轻巧地跑过去']],
 'scampered off 是一溜跑开，scampered across the floor 是轻快跑过地板；不需要跑得很远。',
 'scampered into the bushes 窜进灌木；scampered up the steps 轻快跑上台阶。',
 'scampered 可以因为开心、忙着玩或受惊；fled 更明确写逃离，不能只因词史提过战场，就把每次 scampered 都译成逃命。',
 ('A mouse scampered beneath the cupboard.','一只老鼠一溜窜到柜子下面。'),('The children scampered across the grass to greet us.','孩子们轻快跑过草地，来迎接我们。'),sources=S('scampered','scamper'))
W('scampering','英 /ˈskæmpərɪŋ/；美 /ˈskæmpərɪŋ/','正在轻快奔跑、急忙跑开；轻快跑动的',
 '小脚正快速交替，身体一溜越过地面，是 scampering。小动物或孩子成群跑来跑去时，画面尤其直观。',
 'scamper + 完整 -ing，直接加；英式单读词尾不发的 r 在这个元音词尾前发出。',SCAMPER+[['scamper + -ing → scampering','快速小步跑动的过程']],
 'scampering along the path 是沿小路轻快跑，scampering about 是跑来跑去；也可前置修饰一群活跃的小动物。',
 'scampering up a tree 窜上树；the sound of scampering feet 小脚飞跑的声音。',
 'scampering 注重身体跑得轻快，hurrying 更宽，可以是赶着收拾、说话或做事，并非一定用脚跑。',
 ('We saw squirrels scampering between the trees.','我们看见松鼠在树间轻快地跑来跑去。'),('The children came scampering down the path.','孩子们沿小路轻快地跑了过来。'),sources=S('scampering','scamper'))
SCURRY=[['近代英语 scurry，可能来自较早 hurry-scurry 的押韵形式','也有拟声分析；近源方向和更远基础不完全确定'],['急促小步移动 → 忙乱奔走、匆忙办事','现代不只小动物能用，人为赶时间跑来跑去也可 scurry']]
W('scurry','英 /ˈskʌri/；美 /ˈskɜːri/','急促小跑、匆忙奔走；一阵忙乱、急跑',
 '雨一下来，路人小步急跑找遮蔽；厨房里大家赶着端菜来回跑，都像 scurry：快，而且有点急。',
 '可能从较早 hurry-scurry 的押韵重叠形式分出，也有拟声说。现代 scurry 是完整动词，不把 sc- 当一个通用的匆忙前缀。',SCURRY,
 'scurry for shelter 是急忙跑去躲雨，scurry around 是忙着跑来跑去；a scurry of feet 是一阵急促脚步。',
 'scurry across the floor 小步急跑过地板；scurry to finish 忙着赶完。',
 'scurry 比 scamper 更容易带急切、忙乱感；scamper 常显得轻快活跃。两者都能说小动物，差别在镜头的感觉。',
 ('People began to scurry for shelter as the rain started.','雨一下来，人们就急忙跑去躲雨。'),('We heard a scurry of feet in the hallway.','我们听见走廊里一阵急促的脚步声。'),sources=S('scurry','scurry'))
W('scurries','英 /ˈskʌriz/；美 /ˈskɜːriz/','急促小跑、匆忙奔走〔第三人称单数〕；急跑、忙乱〔复数〕',
 '一个小动物赶紧跑进掩蔽处，或一个人忙着来回取东西，用 scurries；名词复数则把一阵阵忙跑分开看。',
 'scurry 的辅音字母 r 后 y 改 i，再加完整 -es → scurries；词尾读 /z/，不是多一个 /ɪz/ 音节。',SCURRY+[['scurry 改 y 为 i + -es → scurries','它急促跑动；几阵急跑、忙乱']],
 'scurries across the floor 是小步急跑过地板，scurries around the kitchen 是在厨房里忙着跑来跑去；动作带急切感。',
 'scurries into a hole 急忙窜进洞；scurries to answer the door 急忙跑去开门。',
 'scurries 的变化与 carries 相似，保留两个 r；意思却是匆忙移动，不能仅靠相同词尾替代基础动作理解。',
 ('The mouse scurries back into its hole.','老鼠急忙窜回洞里。'),('She scurries around the kitchen preparing lunch.','她在厨房里忙来忙去，准备午饭。'),sources=S('scurries','scurry'))
W('scurried','英 /ˈskʌrid/；美 /ˈskɜːrid/','急促小跑、匆忙奔走了',
 '刚才看见雨来了就赶紧跑到棚下，或忙着在两处间来回跑，是 scurried。画面像短步快速挪，不是从容行走。',
 'scurry 改末尾 y 为 i + 完整 -ed → scurried，词尾读 /d/；基础双 r 保留。',SCURRY+[['scurry 改 y 为 i + -ed → scurried','过去急跑、忙着奔走']],
 'scurried away 是匆忙跑开，scurried for cover 是急跑找遮蔽；scurried to get ready 是忙乱着准备。',
 'scurried across the road 急忙跑过道路；scurried upstairs 匆匆跑上楼。',
 'scurried 说赶紧移动的方式，hurried 可以泛指赶着完成某事；hurried a decision 是仓促作决定，不能照搬成 scurried a decision。',
 ('They scurried under the awning when the rain grew heavier.','雨变大时，他们急忙跑到遮雨篷下。'),('A small crab scurried across the sand.','一只小螃蟹急急地爬过沙地。'),sources=S('scurried','scurry'))
W('scurrying','英 /ˈskʌriɪŋ/；美 /ˈskɜːriɪŋ/','正在急促移动、匆忙奔走；忙乱跑动的',
 '小动物正快速窜来窜去，或人正为一件急事忙着取东西、跑上下楼，是 scurrying。动作中带一点赶、急。',
 'scurry + 完整 -ing，末尾 y 保留 → scurrying；与 scurried 的 y 改 i 不同，两个 i 不需挤在一起。',SCURRY+[['scurry + -ing → scurrying','急促跑动、忙乱奔走的过程']],
 'scurrying for shelter 是正急着找遮蔽，scurrying around 是忙着来回跑；sent everyone scurrying 是让大家赶紧忙起来。',
 'scurrying feet 急促的脚步；scurrying into hiding 急忙窜去藏起来。',
 'scurrying 可由赶时间、受惊等引起，但词本身主要写匆忙方式；具体原因仍需句子告诉你。',
 ('The sudden rain sent everyone scurrying for shelter.','突来的雨让大家赶紧跑去找地方躲。'),('We could hear mice scurrying behind the wall.','我们能听见老鼠在墙后急促窜动。'),sources=S('scurrying','scurry'))
DASH=[['中古英语 daschen 的猛击、急冲 → dash','可能接北欧相似词，较远或拟声；快速冲击感较早已有'],['急冲、撞击的不同分支 → 少量添入、短横符号、打碎希望','现代按搭配看画面，不把所有固定用法逐字硬译为打击']]
W('dashes','/ˈdæʃɪz/','急冲、猛撞、打碎〔第三人称单数〕；冲跑、破折号、少量添入〔复数〕',
 '人急急冲进屋，动词用 dashes；写字中的长横线、往饮料里少加的几滴，又是同形名词的常用分支。',
 'dash + -es，/ʃ/ 后读 /ɪz/；三单、名词复数同形。词史从猛击、急冲材料扩出多条常见用法。',DASH+[['dash + -es → dashes','它急冲、打碎；几次冲跑、几道横线或几份少量添入']],
 'dashes into the room 是冲进房间，two dashes of sauce 是少量几滴调味汁；dashes in a sentence 是句中的破折号。',
 'dashes out of the door 冲出门；short dashes 短横线或几次短跑，看语境。',
 'dash 与 hyphen 在标点中不同：dash 常是隔开话语的较长横线，hyphen 常把词的部分连接起来；这里不把所有横线混成一种。',
 ('He dashes upstairs as soon as the phone rings.','电话一响，他就冲上楼。'),('The sentence uses two dashes to set off the extra information.','这个句子用两道破折号隔开补充信息。'),sources=S('dashes','dash'))
W('dashed','/dæʃt/','冲去了、猛撞、摔碎了；希望等破灭的；虚线的',
 '人刚才一阵急冲，是 dashed；盼着的结果被消息一下打碎，是 hopes were dashed。a dashed line 则像一段段短划排成线。',
 'dash + 完整 -ed，/ʃ/ 后读 /t/；动词过去、分词及虚线形容词都接完整基础词，结尾不读 /ɪd/。',DASH+[['dash + -ed → dashed','过去急冲、猛击；已破灭；由短划组成']],
 'dashed to the station 是急冲去车站，dashed hopes 是破灭的希望；dashed line 是虚线，有间隔的小划。',
 'dashed off a note 匆匆写了便条；dashed against the rocks 撞向礁石。',
 'dashed hopes 的被打碎画面带失望，delayed plans 只说推迟；虚线 dashed 另走短划分支，不带这种失望。',
 ('We dashed to the station when we realised the time.','我们一看时间，赶紧冲向车站。'),('The cancelled trip dashed the children\'s hopes.','行程取消，孩子们的希望破灭了。'),sources=S('dashed','dash'))
SPRINT=[['较早 sprenten／sprint 的跃起、窜出材料','可能接北欧 spretta 等，具体改形路线保留不确定性'],['现代体育 sprint → 短距离全速跑及短时集中工作','冲刺名词与短跑复合词有记录关系，不把今天整词顺序当唯一史实']]
W('sprints','/sprɪnts/','短距离全速跑、冲刺〔第三人称单数〕；冲刺、短跑、短时集中工作〔复数〕',
 '一个人突然使出全速跑一段，是 sprints；训练里几次短冲刺，也叫 sprints。工作里限定时间集中做一轮任务，也借冲刺的画面。',
 'sprint + -s，/t/ 后读 /s/，结尾 /nts/；动词三单和名词复数同形，工作用法是短时集中推进的借用。',SPRINT+[['sprint + -s → sprints','他、她冲刺；多次短跑或多轮集中推进']],
 'sprints towards the line 是全速冲向终点，short sprints 是短距离冲刺；two-week sprints 是两周一轮的集中工作安排。',
 'sprints for the bus 冲跑赶公交；a series of sprints 一连串冲刺。',
 'sprints 强调短时间、全力跑，jogs 常是较慢、可持续的慢跑；不同速度、持续方式让两词画面不同。',
 ('She sprints towards the finish line.','她全速冲向终点。'),('The team works in short sprints with a clear goal for each one.','团队分成短轮次集中工作，每轮都有明确目标。'),sources=S('sprints','sprint'))
W('sprinted','/ˈsprɪntɪd/','全速短跑、冲刺了',
 '刚才突然拿出全速，冲到门口或终点，是 sprinted。重点像开了短时最大档，不是一路慢慢跑。',
 'sprint + 完整 -ed，/t/ 后读 /ɪd/，多一个音节；nt 后直接加，不双写 t。',SPRINT+[['sprint + -ed → sprinted','过去短时间全速跑动']],
 'sprinted across the field 是全速跑过球场，sprinted to catch the bus 是冲跑赶公交；方向可近可远，动作突出冲劲。',
 'sprinted for the door 冲向门口；sprinted the final stretch 冲刺最后一段。',
 'sprinted 可以为赶车、玩耍或比赛，raced 有时另暗含竞赛；仅凭 sprinted 不需要假定旁边一定有对手。',
 ('He sprinted across the field to catch the ball.','他全速跑过球场去接球。'),('We sprinted the last few metres to the gate.','我们冲刺着跑完了通向大门的最后几米。'),sources=S('sprinted','sprint'))
GLIDE=[['古英语 glidan 的平顺滑动材料 → glide','早期强变化动词；现代常用规则 glided'],['平滑移动 → 滑翔；事情、话题顺畅通过','现代核心常是不颠、不费劲地从一点移过另一点']]
W('glides','/ɡlaɪdz/','滑行、平顺移动、滑翔〔第三人称单数〕；滑行动作、语音滑音〔复数〕',
 '天鹅在水上不急不颠地过去，溜冰者几乎不费劲地划过冰面，是 glides；说事情轻易过关，也能借这种顺滑感。',
 'glide + -s，/d/ 后读 /z/，结尾 /dz/；动词三单与滑行、滑音等名词复数同形。',GLIDE+[['glide + -s → glides','它平滑移动；几次滑行或几种滑音']],
 'glides across the water 是滑过水面，glides through an exam 是轻松通过考试；语音 glides 指顺滑过渡的音类。',
 'glides above the trees 在树上方滑翔；glides from one topic to another 顺畅地换话题。',
 'glides 让人觉得平滑、轻松，slides 更能中性地说在表面滑动；滑倒、失去控制的 slide 不一定有 glide 的从容感。',
 ('The swan glides across the lake.','天鹅平顺地滑过湖面。'),('She glides from one topic to another without losing the audience.','她顺畅地转换话题，听众仍跟得上。'),sources=S('glides','glide'))
W('glided','/ˈɡlaɪdɪd/','平滑移动、滑行、滑翔了；顺畅通过了',
 '刚才船、鸟或滑冰者顺滑地过去，是 glided；一个人轻松通过难关，也能借用这幅没有磕绊的动作。',
 'glide 去末尾不发音 e + 完整 -ed → glided，/d/ 后读 /ɪd/。基础虽接古英语强变化词，现代常用规则过去式。',GLIDE+[['glide 去 e + -ed → glided','现代规则过去式；平顺地移过']],
 'glided into the room 是轻巧平顺地进入房间，glided over the water 是滑过水面；glided through the test 是轻松通过测试。',
 'glided past 平顺掠过；glided down towards the field 滑翔着降向田野。',
 'glided 更突出动作顺滑，flew 只说飞；鸟 glided 时常借气流少拍或不拍翅膀，讲它在怎样飞。',
 ('The canoe glided silently across the water.','独木舟无声地滑过水面。'),('The bird glided down towards the field.','鸟滑翔着向田野降去。'),sources=S('glided','glide'))

def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfn',ROOTS,WORDS)
 extend_lessons()
