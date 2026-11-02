"""Trial, sudden and glass: tests, abrupt arrival and material-based meanings."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['盎格鲁法语 trier → trial、triel → 中古英语 trial','挑选、试验；检验的过程'],['英语 trial','试验、试用；审理；考验']]
W('trial','/ˈtraɪəl/','试验、试用；审判、审理；考验',
 '先放到实际条件下试一试，再决定是否合适、说法是否成立。产品试用和法庭审理是不同场景，不必强行译成同一个中文词。',
 '经盎格鲁法语 trial、triel，与 trier 挑选、试验同族，和 try 有历史联系。词尾 -al 在这里是动作名词材料。常见试验义不是 tri- 三加 -al；语言学上表三数的同形 trial 则另有来源。',T,
 'a free trial 免费试用，trial and error 反复试错，a clinical trial 临床试验；stand trial 受审。a trial period 是试用期，a trial of patience 是耐心的考验。',
 'a free trial；a trial period；trial and error；stand trial。',
 'try 常用动词，trial 常用名词；在法庭语境 trial 是审理程序，不等于 verdict 判决结果。本文说明用语，不把具体法律程序推广为所有地区都相同。',
 ('We tested the software during a free trial.','我们在免费试用期间测试了这款软件。'),('The case went to trial last month.','这起案件上个月进入了审理阶段。'))
W('retrial','/ˌriːˈtraɪəl/','重新审理、再审',
 '同一案件再进行一次审理。再来一次的是审理过程，不是只把原判决多读一遍。',
 're- 再次 + trial 审理，形成名词。日常最常见法律语境；何时能够重审依具体制度与案件而定。',T+[['re- + trial → retrial','重新进行审理']],
 'order a retrial 下令重审，face a retrial 面临重新审理，at the retrial 在重审时。',
 'order a retrial；face a retrial；at the retrial。',
 'retrial 重新审理，appeal 上诉、请求复核，二者可能相关但并非同义；mistrial 指审理不能有效继续或作结的情形，不直接等于第二次审理。',
 ('The judge ordered a retrial.','法官下令重新审理。'),('New evidence was presented at the retrial.','重审时提交了新证据。'))
R('B3375','试验、试用、审理；实际检验的过程','TRIAL：放到实际条件下检验','trial → pretrial、mistrial、retrial；法庭扩展集中在后面。',
 '与 try 同族但保留法语名词路径。常见 trial 不拆成 tri- 三；表三数的术语另源，暂略。',
 '法语 trier 与名词 -al；pre-/mis-/re- + trial。',
 [['检验与试用','trial'],['审理相关','pretrial · mistrial · retrial']],
 'trial 过程、verdict 结果；retrial 不等于 appeal；免费试用和法庭审理依语境分译。',
 'The trial ended without a verdict, and a retrial was later ordered.\n\n审理结束时未作出裁决，后来又决定重新审理。','trial pretrial mistrial retrial')
S=[['拉丁语 subīre → subitus、subitāneus','来到、临近等；突然发生的'],['通俗拉丁语重建形 *subitānus → 法语 sodain、subdain → 中古英语 sodeyn → sudden','突然、出乎预料的']]
def SH(f,m):return S+[[f,m]]
W('sudden','/ˈsʌdən/','突然的、骤然的',
 '你还没做好准备，事情已经发生了。重点在没什么预告，不只是动作速度快。',
 '经法语 sodain 等接拉丁语 subitus、subitāneus；更早 subīre 含 sub- 与 īre 去，词义有走近、来到等发展。现代 sudden 已不能逐字拆成 sud 与 den。中间 *subitānus 是重建形。',S,
 'a sudden noise 突然的声响，a sudden change 骤变，a sudden loss 突如其来的损失；all of a sudden 突然。',
 'a sudden change；a sudden noise；a sudden urge；all of a sudden。',
 'sudden 强调突发、出乎预料，fast 强调速度；一辆一直高速行驶的车可以 fast，但不必有 sudden change。',
 ('A sudden noise made everyone turn around.','一声突如其来的响动让所有人都转过头去。'),('There was a sudden change in the weather.','天气突然发生了变化。'))
W('suddenly','/ˈsʌdənli/','突然、忽然',
 '镜头像被猛地切了一下：前一刻还正常，下一刻事情就变了。',
 'sudden + -ly，形成副词，中古英语已有 sodenly 等形式。它修饰发生、出现、变化的方式。',SH('sudden + -ly → suddenly','以突发方式；忽然'),
 'suddenly stop 突然停下，suddenly realize 突然意识到，suddenly disappear 突然不见；可放句首，也可放动词前。',
 'suddenly realize；suddenly stop；suddenly disappear。',
 'sudden 形容词，suddenly 副词：a sudden stop 与 stop suddenly。suddenly 不等于 finally 终于，后者说等待后的结果。',
 ('The lights suddenly went out.','灯突然全灭了。'),('She suddenly realized that she had left her keys inside.','她突然意识到自己把钥匙落在里面了。'))
W('suddenness','/ˈsʌdənnəs/','突然性、突如其来的程度',
 '不是在说发生了哪件事，而是把“来得这么突然”这个特点单独拿出来说。',
 'sudden + -ness，形成性质名词。词干末尾 n 与后缀开头 n 都保留在拼写中。',SH('sudden + -ness → suddenness','突发、没有预告这一性质'),
 'the suddenness of the change 变化的突然性，with surprising suddenness 出人意料地突然。',
 'the suddenness of；with suddenness；shocked by the suddenness。',
 'suddenness 突然这一特点，speed 速度；令人吃惊的往往是没预告，而不只是物理运动快。',
 ('We were shocked by the suddenness of his departure.','他离开得这么突然，让我们很吃惊。'),('The storm arrived with surprising suddenness.','暴风雨来得出人意料地突然。'))
R('B3920','没有多少预告就出现、变化','SUDDEN：还没来得及准备，事情就发生','sudden → suddenly → suddenness，先性质，再发生方式，最后性质名词。',
 '近源经法语接拉丁语突然义；保留旧形，不靠现代字母拼出新故事。突然和快速分开讲。',
 'sudden + -ly/-ness；suddenness 拼写保留两个相邻 n。',
 [['性质、方式、性质名词','sudden · suddenly · suddenness']],
 'sudden/suddenly 词性不同；suddenness/speed 突发与速度不同；all of a sudden 是常用短语。',
 'The sudden silence made us look up.\n\n突然安静下来，我们便抬头看了看。','sudden suddenly suddenness')
G=[['古英语 glæs → 中古英语 glas → glass','玻璃这种材料'],['英语 glass 的材料、制品与镜片用法','玻璃 → 玻璃杯、杯中一份饮料；镜片 → 眼镜、光学器具']]
def GH(f,m):return G+[[f,m]]
W('glass','英 /ɡlɑːs/；美 /ɡlæs/','玻璃；玻璃杯、一杯；眼镜〔glasses〕',
 '先是透明硬材料，再用材料叫它做成的杯子、镜片。glass 不可数和 a glass 可数，镜头已经从材料移到具体制品。',
 '古英语 glæs 经中古英语延续。更远与发光词的联系有不同分析，不必为了记忆强作确定结论。杯、杯中量、光学器具等义由材料与用途扩展。',G,
 'made of glass 玻璃做的，a glass of water 一杯水，a pair of glasses 一副眼镜。glasses 也可能是几个杯子，依上下文区分。',
 'a glass of water；broken glass；a pair of glasses；glass windows。',
 'glass 材料不说 a glass，除非说一个杯子、某类玻璃等可数用法；glasses 眼镜通常用复数，不把一副写成 a glasses。',
 ('The door is made of glass.','这扇门是玻璃做的。'),('He put on his glasses and poured a glass of water.','他戴上眼镜，倒了一杯水。'))
W('glassy','英 /ˈɡlɑːsi/；美 /ˈɡlæsi/','像玻璃般光滑、光亮的；目光呆滞的',
 '湖面平得像整块玻璃；人的眼睛像隔着一层亮膜、没有反应，也可说 glassy。',
 'glass + -y，中古英语 glasy 已有。先认识像玻璃的外观，再区分光滑表面与呆滞目光两种常见场景。',GH('glass + -y → glassy','像玻璃的；目光缺少反应的'),
 'a glassy surface 玻璃般平滑的表面，glassy eyes 呆滞的双眼，a glassy stare 发直的目光。',
 'a glassy lake；a glassy surface；glassy eyes。',
 'glassy 像玻璃，不保证材料真是玻璃；glassy eyes 不是在说戴眼镜，后者是 wearing glasses。',
 ('The boat moved across the glassy lake.','小船驶过镜面般平静的湖面。'),('He stared at the screen with glassy eyes.','他双眼呆滞地盯着屏幕。'))
W('glassware','英 /ˈɡlɑːsweə/；美 /ˈɡlæsweər/','玻璃器皿、玻璃制品〔总称〕',
 '把杯、壶、玻璃碗或实验室瓶管放成一类，统称 glassware；不是只说一杯饮料。',
 'glass 玻璃 + ware 制品，构成集合用语。-ware 告诉你这一类制品，不能拆成 glass + aware“意识到”。',GH('glass + ware → glassware','玻璃制成的一类器皿、用品'),
 'laboratory glassware 实验室玻璃器皿，delicate glassware 易碎玻璃器皿。通常不可数，一件说 a piece of glassware。',
 'laboratory glassware；wash the glassware；a piece of glassware。',
 'glassware 一类器物，glass 材料或杯子；crockery 常指陶瓷餐具，范围不相同。',
 ('Please wash the glassware by hand.','请手洗这些玻璃器皿。'),('The laboratory stores its glassware in this cabinet.','实验室把玻璃器皿放在这个柜子里。'))
W('eyeglass','英 /ˈaɪɡlɑːs/；美 /ˈaɪɡlæs/','眼用镜片；眼镜〔通常复数 eyeglasses〕',
 '给眼睛用的玻璃镜片。今天日常说戴着的整副眼镜，通常用 eyeglasses，尤其美式表达。',
 'eye 眼 + glass 镜片，合成名词。单数历史上可指单片眼镜等；复数 eyeglasses 用作普通眼镜称呼。',GH('eye + glass → eyeglass','眼用镜片；复数常指一副眼镜'),
 'a pair of eyeglasses 一副眼镜，eyeglass frames 眼镜框；作定语 eyeglass 保持单数形式。',
 'a pair of eyeglasses；eyeglass frames；an eyeglass case。',
 'eyeglasses 眼镜，eye 眼睛；eyeglass case 是眼镜盒，不是眼睛病例。日常 glasses 往往就够了。',
 ('She keeps a spare pair of eyeglasses at work.','她在工作地点放了一副备用眼镜。'),('He chose thin metal eyeglass frames.','他选了细金属眼镜框。'))
W('glazier','英 /ˈɡleɪziə/；美 /ˈɡleɪʒər/','玻璃安装工、玻璃工',
 '窗户碎了，负责切合尺寸、把新玻璃装进窗框的工匠，就是常见语境中的 glazier。',
 '接中古英语 glasier、glazier 等，是 glass + 人物后缀的旧派生，词尾又受其他人物词形式影响。现代可与 glaze 安装玻璃联系记忆；不要把 -ier 误当成比较级。',G[:1]+[['中古英语 glaser、glasier 等 → glazier','从事装玻璃等工作的人']],
 'call a glazier 请玻璃工，a qualified glazier 有资质的玻璃工；常用于窗、门等玻璃安装。读音有 /zj/、/ziə/、/ʒ/ 等变体。',
 'call a glazier；a local glazier；a qualified glazier。',
 'glazier 玻璃工，glacier 冰川；两词拼写近，常用意义和来源不同。',
 ('We called a glazier to replace the broken pane.','我们请玻璃工来更换碎掉的那块窗玻璃。'),('The glazier measured the window before cutting the glass.','玻璃工切玻璃前先量了窗户尺寸。'))
W('spyglass','英 /ˈspaɪɡlɑːs/；美 /ˈspaɪɡlæs/','小型望远镜〔常指手持单筒式〕',
 '远处的船看不清，举起一根镜筒，把远处细节拉到眼前。海盗、航海故事里常见这件东西。',
 'spy 看见、窥看 + glass 光学镜具，合成名词。这里 spy 是观察动作，不代表只有间谍能使用。',GH('spy + glass → spyglass','用来观察远处的便携光学镜具'),
 'look through a spyglass 用小望远镜看，raise a spyglass 举起镜筒；普通现代总称也可说 telescope。',
 'look through a spyglass；raise a spyglass；a brass spyglass。',
 'spyglass 常带小型手持镜筒的画面，binoculars 通常双筒望远镜；magnifying glass 放大镜则多看近处小物。',
 ('The captain raised his spyglass to inspect the distant ship.','船长举起小望远镜，观察远处的船。'),('The child looked through a toy spyglass.','孩子透过玩具望远镜看远处。'))
R('B3358','玻璃材料；杯、镜片与相关器具','GLASS：一块材料，按用途变成杯、镜片和器具名','glass → glassy、glassware；eyeglass、spyglass 光学一组，hourglass、glasshouse 等合成词归用途，再讲 glazier 职业。',
 '材料名与制品名分清可数性。旧派生 glazier 不强拆成现代比较级，冷门人物变体暂略。',
 'glass + -y/ware；eye/spy/hour + glass；glass + house；glazier 接中古英语旧人物派生。',
 [['材料及性质、制品','glass · glassy · glassware'],['镜片与观察','eyeglass · spyglass'],['器具、建筑与职业','hourglass · glasshouse · glazier']],
 'glass 材料与 a glass 杯子不同；glassy eyes 非戴眼镜；glazier 玻璃工、glacier 冰川。',
 'The glazier replaced the glass while I cleaned my eyeglasses.\n\n玻璃工更换玻璃时，我擦了擦自己的眼镜。',
 'glass glassy glassware eyeglass spyglass hourglass glasshouse glazier')
if __name__=='__main__':save('continuation_20261030_bx',ROOTS,WORDS)
