"""Hoisting, redirecting, plucking and prising loose."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4358':dict(words='shove shoves shoved'.split(),label='shove：用力推过去、塞进去',note='shove 接古英语推、搡的材料，现代 shoved 去不发音 e 加完整 -ed，结尾 /vd/；同轻推 nudge 的力度分开理解。'),
 'B3860':dict(words='wrist wrest wrests wrested wresting'.split(),label='wrest、wrist 的扭转材料',note='wrest 承古英语 wraestan 与北欧同族词的扭、拧材料，可联系 wrist 的转动关节词族；现代夺取像用力扭拉过来。'),
 'C1118':dict(words='prize pry pries pried prying prized prizing'.split(),label='pry 的撬动支与 prize 的抓取材料',note='此处只把 pry 撬动支联系较早 prize、prise 的杠杆、抓持材料；pry 打探支近源不同，prize 珍视支也另接价值词族。'),
 'C1122':dict(words='prize prized prizing'.split(),label='prize：高度看重、珍视',note='prized、prizing 的珍视义接价值、评价材料；同形撬动义另经法语 prise 连接抓取材料，不都归 pretium。'),
 'C0669':dict(words='lever levers levered levering'.split(),label='lever：举起工具到撬动',note='lever 的法语举起工具名接拉丁语 levare 抬起，名词早于英语撬动动词；杠杆本身与借杆撬起分开讲。'),
 'A1788':dict(words='heave heft hefts hefted hefting hoist hoists hoisted hoisting'.split(),label='heft 的旧名词形态与 hoist 的固定词尾',note='heft 重量名词联系 heave 的旧名词类推及旧分词，后来动词由名词产生；hoist 则接更早 hoise 等材料，不能把现代最后的 t 一概认成普通过去式。'),
 'A1760':dict(words='hoist hoists hoisted hoisting shove shoves shoved shunt shunts shunted shunting pluck plucks plucking wrest wrests wrested wresting pry pries pried prying prize prized prizing lever levers levered levering heft hefts hefted hefting'.split(),label='吊起、推转、撬取和掂量的现代词形',note='hoisted、shunted、wrested、hefted 的 -ed 读 /ɪd/；shoved、pried、prized、levered 读 /d/。pry 的 pried 改 y 为 i，prying 则保留 y。'),
}
HOIST=[['较早 hoise、hysse 等航海提举材料 → hoist','可能借荷兰语等相近词，t 或受较早过去式影响并入；传播起点未定'],['用绳、机械拉高 → 举起、吊起；起重装置','现代完整 hoist 再作规则变化，常见对象有旗、帆、重物']]
W('hoist','/hɔɪst/','举起、吊起、升起；吊升、起重装置',
 '拉绳让旗子爬上杆，用起重装置把箱子提到空中，是 hoist。人把沉包一下举到肩上，也能用它。',
 '接较早 hoise、hysse 等航海词，可能借荷兰语等；t 或受旧过去式影响并入基础词，现代过去式再加 -ed 成 hoisted。',HOIST,
 'hoist a flag 是升旗，hoist the sail 是升帆；a hoist 可是举升重物的装置，不是只限一种吊车。',
 'hoist it onto a shoulder 举到肩上；a mechanical hoist 机械起重装置。',
 'hoist 通常更有向高处提、借绳或费劲举的感觉，lift 更宽；抬一张轻纸也可 lift，不必有 hoist 的分量。',
 ('They used a small hoist to lift the engine.','他们用小型起重装置抬起发动机。'),('We watched the crew hoist the sail.','我们看着船员升起船帆。'),sources=S('hoist','hoist'))
W('hoists','/hɔɪsts/','举起、吊起、升起〔第三人称单数〕；吊升装置、举升动作〔复数〕',
 '一个人把旗升高、把包举上去，动词用 hoists；几台帮人抬重物的装置也叫 hoists，按用途叫名。',
 'hoist + -s，/t/ 后读 /s/，结尾 /sts/；基础 st 保留，名词复数与动词三单同形。',HOIST+[['hoist + -s → hoists','他、她举起；多台起重装置或多次举升']],
 'hoists the flag 是升起旗子，hoists the child onto his shoulders 是把孩子举到肩上；electric hoists 是电动起重装置。',
 'hoists a bag 举起包；ceiling hoists 安装在上方的吊升装置。',
 'hoists 如果有一个被举物体作宾语，通常是动词；two hoists 则是两台装置或两次举升，看量词和场景。',
 ('She hoists the bag onto her shoulder.','她把包举到肩上。'),('The workshop has two electric hoists.','车间里有两台电动起重装置。'),sources=S('hoists','hoist'))
W('hoisted','/ˈhɔɪstɪd/','举起、吊起、升起了',
 '刚才旗、帆或重物被拉高，是 hoisted；人使劲把箱子举到高处，也能这样写。重点是从低位提上去。',
 'hoist + 完整 -ed，/t/ 后读 /ɪd/；现代基础词已有 t，仍需另加完整过去词尾。',HOIST+[['hoist + -ed → hoisted','过去举高、吊升']],
 'hoisted the flag 是升了旗，hoisted aboard 是吊上船，hoisted onto the roof 是吊上屋顶；可主动也可被动。',
 'hoisted into place 吊升到位；hoisted onto his back 举到背上。',
 'hoisted 向高处提举的画面较强，hauled 可以沿地面拖很远；一件重物可能先 hauled 到吊机旁，再 hoisted 上去。',
 ('They hoisted the flag above the entrance.','他们把旗升到入口上方。'),('The crate was hoisted onto the ship.','木箱被吊上了船。'),sources=S('hoisted','hoist'))
W('hoisting','/ˈhɔɪstɪŋ/','正在举起、吊起、升起；吊升工作',
 '绳索正收紧，重物一点点离开地面，是 hoisting；升旗、升帆也能把镜头放在这段向上拉的过程。',
 'hoist + 完整 -ing，直接加；st 保留，词尾可将提举看成正在发生的动作或一项工作。',HOIST+[['hoist + -ing → hoisting','把对象向上提举的过程']],
 'hoisting a sail 是升帆，hoisting heavy loads 是吊重物；hoisting equipment 是起重设备，说明用途。',
 'hoisting the flag 升旗；a hoisting rope 吊升绳索。',
 'hoisting 把向上提的动作说出来，loading 只说装载；把货平推入车厢也可 loading，不一定是 hoisting。',
 ('The crew were hoisting the sail when we arrived.','我们到时，船员们正在升帆。'),('The crane was hoisting a steel beam into position.','起重机正把一根钢梁吊到位。'),sources=S('hoisting','hoist'))
SHOVE=[['古英语 scufan、sceofan → 中古英语 shouven → shove','推、搡、向前挤，较早有强变化形式'],['现代用力推、塞入；shove off 等搭配','现代常见 shoved 为规则变化，不沿用每个古英语词形']]
W('shoves','/ʃʌvz/','用力推、搡、塞〔第三人称单数〕；推搡动作〔复数〕',
 '手掌顶着箱子用力推开，或把衣服随手塞进袋里，是 shoves；几下不客气的推搡也可作名词复数。',
 'shove + -s，/v/ 后读 /z/，结尾 /vz/；o 的基础读音 /ʌ/ 保留，不按 move 的 /uː/ 读。',SHOVE+[['shove + -s → shoves','他、她推搡、塞入；几下推搡']],
 'shoves the door open 是用力推门，shoves the papers into a bag 是把纸塞进包；pushes and shoves 是推推搡搡。',
 'shoves past someone 挤过某人；a few hard shoves 几下用力推搡。',
 'shoves 比 pushes 更容易显得用力、不太轻柔；nudges 则是轻碰、小推，力度和待人感觉都不同。',
 ('He shoves the heavy door open with his shoulder.','他用肩膀把沉门顶开。'),('A few hard shoves moved the cupboard away from the wall.','使劲推了几下，柜子被挪离墙边。'),sources=S('shoves','shove'))
W('shoved','/ʃʌvd/','用力推、搡、塞了；挤过去了',
 '刚才用力把东西推到一边，或不太讲究地把纸塞进袋子，是 shoved；人在人群中使劲往前挤也可用它。',
 'shove 去末尾 e + 完整 -ed → shoved，/v/ 后读 /d/；现代规则过去式，元音仍是 /ʌ/。',SHOVE+[['shove 去 e + -ed → shoved','过去推搡、随手塞入']],
 'shoved aside 是用力推到一旁，shoved into a drawer 是塞进抽屉；shoved past me 是从我身边挤过去。',
 'shoved the gate open 推开大门；shoved his hands into his pockets 把手插进袋里。',
 'shoved 在塞物场景常显得匆忙、随意，placed 更像放好；同一份文件 shoved into a bag 与 placed in a folder 的动作感觉不同。',
 ('She shoved the papers into her bag.','她把那些纸塞进包里。'),('He shoved the box aside to clear the doorway.','他把箱子推到一旁，腾出门口。'),sources=S('shoved','shove'))
SHUNT=[['中古英语 shunten 的突然移开、退避 → shunt','可能联系 shun，并受其他相似形式影响，具体早期形成未定'],['拨到一边 → 铁路转轨、调车；物或人转往别处','像把原本沿主线走的对象拨入另一条路径']]
W('shunt','/ʃʌnt/','转移、推到一边；给列车转轨、调车；旁路、分流通路',
 '把车厢从主轨拨去侧轨，是 shunt；一个人被一处推给另一处、得不到正面处理，也像被不断拨到别的支路。',
 '承中古英语 shunten 的突然移开、退避义，可能联系 shun 的避开材料。铁路采用后，侧轨画面很适合理解后来的转移用法。',SHUNT,
 'shunt wagons into a siding 是把货车厢调入侧线，shunt someone around 是把人转来转去；电路 shunt 则是分流、旁路。',
 'shunt aside 拨到一边；an electrical shunt 电路中的分流支路或装置。',
 'shunt 常带被拨离主线、转到别处的感觉，move 更中性；说人被 shunted around，常暗含处理不够重视。',
 ('The engine will shunt the wagons into a siding.','机车会把货车厢调入侧线。'),('They kept trying to shunt the problem onto another department.','他们一直想把问题推给另一个部门。'),sources=S('shunt','shunt'))
W('shunts','/ʃʌnts/','转移、调车、拨开〔第三人称单数〕；旁路、分流装置〔复数〕',
 '一台机车把车厢推到另一条轨，叫 shunts；电流多走一条旁路的装置，也可用名词复数 shunts。',
 'shunt + -s，/t/ 后读 /s/，结尾 /nts/；动词三单与旁路、分流等名词复数同形。',SHUNT+[['shunt + -s → shunts','它把对象拨到另一条路径；多个分流装置']],
 'shunts the wagons 是调动车厢，shunts the request elsewhere 是把请求转到别处；current shunts 是电流分流器。',
 'shunts traffic onto a side road 把车流导向支路；electrical shunts 分流装置。',
 'shunts 的铁路、一般转移、分流都能抓住改走支路的画面；技术名词的具体装置仍要由场景判断。',
 ('The small engine shunts wagons around the yard.','小机车在调车场里调动车厢。'),('The engineer checked the shunts in the circuit.','工程师检查了电路里的分流装置。'),sources=S('shunts','shunt'))
W('shunted','/ˈʃʌntɪd/','转移、调车、拨到一边了；被转来转去的',
 '刚才车厢被移去侧轨，或请求被推到另一个部门，是 shunted。说人被这样安排，常有没被放在主要位置的感觉。',
 'shunt + 完整 -ed，/t/ 后读 /ɪd/；nt 后直接加，现代规则过去、过去分词。',SHUNT+[['shunt + -ed → shunted','过去转到支路、别处；被拨开']],
 'shunted into a siding 是调入侧线，shunted from office to office 是被各办公室转来转去；shunted aside 是被搁到一边。',
 'shunted onto a side road 被导向支路；shunted out of the way 被挪开。',
 'shunted 在被转来转去的场景常有被动、不受重视的感觉；transferred 可以中性地说正式调动，不必含这种语气。',
 ('The wagons were shunted onto a side track.','货车厢被调入侧轨。'),('She felt she was being shunted from one office to another.','她觉得自己正被一个办公室推给另一个办公室。'),sources=S('shunted','shunt'))
W('shunting','/ˈʃʌntɪŋ/','正在转移、拨开、调车；调车、分流',
 '车厢正被一节节挪向另一条轨，是 shunting；把问题、人转来转去，也可沿这个“拨到别处”的动作理解。',
 'shunt + 完整 -ing，直接加；既可描述进行动作，也可作铁路调车、分流等动作名词。',SHUNT+[['shunt + -ing → shunting','改走支路、调动车厢的过程']],
 'a shunting yard 是铁路调车场，shunting wagons 是调车；shunting responsibility elsewhere 是把责任推往别处。',
 'shunting operations 调车作业；shunting people around 把人转来转去。',
 'shunting 是调整车厢位置、路线的操作，travelling by train 是乘车旅行；两者都有火车，却在讲不同活动。',
 ('The engine was shunting wagons in the yard.','机车正在调车场里调动车厢。'),('They were shunting the responsibility from one team to another.','他们正把责任从一个团队推给另一个团队。'),sources=S('shunting','shunt'))
PLUCK=[['古英语 pluccian、ploccian → 中古英语 plukken → pluck','拔出、摘下；更远与拉丁拔毛材料的关系有证据争议'],['从原处拉出 → 摘花、拔毛、拨弦等常用动作','勇气名词另有内脏、心等历史中间材料，不能只用一幅拔取画面包办']]
W('plucks','/plʌks/','摘、拔、拨弦〔第三人称单数〕；拔取、拨弦动作〔复数〕',
 '手指把花从枝上摘下，或拉一下琴弦再放开，是 plucks：从原处抓住、拉开一点。名词复数可以是几下拨弦。',
 'pluck + -s，/k/ 后读 /s/；动词三单、拔取或拨弦名词复数同形，基础接古英语拔取材料。',PLUCK+[['pluck + -s → plucks','他、她摘取、拨弦；几次拨动']],
 'plucks a flower 是摘花，plucks the strings 是拨琴弦；plucks up courage 是鼓起勇气，用法要把 up 一起记。',
 'plucks a loose thread 拔掉松线头；gentle plucks on the strings 轻轻几下拨弦。',
 'plucks 常像用手指或细小抓取把东西拉离，pulls 更宽；拉整扇沉门通常 pull，不必有 pluck 的小巧动作。',
 ('She plucks a few leaves from the herb plant.','她从香草上摘下几片叶子。'),('He plucks the guitar strings with his fingers.','他用手指拨吉他弦。'),sources=S('plucks','pluck'))
W('plucking','/ˈplʌkɪŋ/','正在摘取、拔除、拨弦；拨弦、拔取动作',
 '手正一片片摘叶子、一根根拔毛，或指头一下一下拨琴弦，是 plucking。常有细小、逐个处理的动作感。',
 'pluck + 完整 -ing，直接加；ck 保留，不再双写 k，动作名词和分词同形。',PLUCK+[['pluck + -ing → plucking','摘、拔、拨动的过程']],
 'plucking feathers 是拔羽毛，plucking a guitar 是拨吉他；plucking up courage 是正鼓起勇气，不是把一个实体拉出来。',
 'plucking leaves 摘叶子；a plucking motion 像拨弦、拔取的动作。',
 'plucking strings 是拉开再放回的拨动，strumming 更像手一次扫过几根弦；两者都是弹吉他，却描写不同手法。',
 ('She was plucking leaves from a sprig of mint.','她正从一枝薄荷上摘叶子。'),('He practised plucking one string at a time.','他练习一次拨一根弦。'),sources=S('plucking','pluck'))
WREST=[['古英语 wraestan 与北欧同族扭转材料 → 中古英语 wresten → wrest','用力拧、扭、挣，与 wrist 的转动材料相连'],['用力扭拉脱开 → 奋力夺取控制、优势、胜利','像从紧抓着的手里硬把目标拉到自己这边']]
W('wrest','/rest/','用力拧夺、抢走；奋力夺取、争得',
 '对方抓得很紧，你用力扭拉，把东西夺到手，是 wrest。比赛、谈判中艰难争得控制权，也像把优势从对方手里拽过来。',
 '承古英语 wræstan 与北欧同族词的扭、拧义，较远联系 wrist 转动关节的词族；开头 w 在现代不发音。',WREST,
 'wrest something from someone 是从某人手里用力夺得，wrest control from 是夺取控制；通常暗含阻力、不容易。',
 'wrest a victory 奋力争得胜利；wrest the object free 扭拉使物体脱开。',
 'wrest 比 take 更强调用力、克服抵抗；get a result 可以很轻松，wrest a result 往往让人想到费劲争取。',
 ('He tried to wrest the rope from her hands.','他试图从她手中用力夺过绳子。'),('The team managed to wrest control of the match from their opponents.','球队设法从对手手中夺回了比赛控制权。'),sources=S('wrest','wrest'))
W('wrests','/rests/','用力夺取、艰难争得〔第三人称单数〕',
 '一个人从紧握的手里夺走东西，或一方经过较量拿到主导权，用 wrests。动作像用力把原来属于对方的控制拉过来。',
 'wrest + -s，/t/ 后读 /s/，结尾 /sts/；w 不发音，三单接在完整动词后。',WREST+[['wrest + -s → wrests','他、她或它克服阻力夺得']],
 'wrests the bag from someone 是用力夺过包，wrests control from a rival 是从对手处夺得控制；from 经常标出原持有者。',
 'wrests an advantage 争得优势；wrests it free 使劲夺开。',
 'wrests 与 rests 发音相同，前者写夺取，后者可说休息、放置；句子宾语和 from 等结构能帮助分清。',
 ('In the story, the hero wrests the key from the guard.','故事里，主人公从守卫手中夺过钥匙。'),('The winning move wrests control of the centre from the other player.','那步妙棋从对手手中夺走了中心控制权。'),sources=S('wrests','wrest'))
W('wrested','/ˈrestɪd/','用力夺得、艰难争取到了',
 '刚才从对方手里硬夺过东西，或经过一番较量终于争到主导，是 wrested。它给拿到手的结果加上了阻力和付出的劲。',
 'wrest + 完整 -ed，/t/ 后读 /ɪd/；w 不发音，st 后直接加词尾。',WREST+[['wrest + -ed → wrested','过去用力夺得、争得']],
 'wrested it from his grasp 是从他的紧握中夺出，wrested back control 是夺回控制权；back 与 from 可连用交代方向。',
 'wrested a concession 费力争得让步；wrested the rope free 使劲把绳子夺开。',
 'wrested 常是克服抵抗而取得，received 是收到；别人主动送来东西用 received，自身不含夺的过程。',
 ('She wrested the rope from his grip.','她从他的紧握中夺出了绳子。'),('The team wrested back control in the second half.','球队在下半场夺回了比赛控制权。'),sources=S('wrested','wrest'))
W('wresting','/ˈrestɪŋ/','正在用力夺取、奋力争取',
 '对象还被另一方抓着，你正一点点把它扭拉过来，是 wresting；争主导权也像这场有阻力的拔取。',
 'wrest + 完整 -ing，直接加；w 不发音。wrestle 的摔跤动词另有历史反复动作形式，wresting 是 wrest 自己的现代变化。',WREST+[['wrest + -ing → wresting','正在克服抵抗取得']],
 'wresting control from someone 是正从某人处夺取控制，wresting it free 是正用力夺开；常接能体现阻力的对象。',
 'wresting back the initiative 夺回主动；wresting a victory 奋力争取胜利。',
 'wresting 侧重把控制、东西争到自己手里，wrestling with a problem 则是和难题缠斗、费力处理；形式和句型别换错。',
 ('The film shows the hero wresting the key from the guard.','影片拍出了主人公从守卫手里夺钥匙的过程。'),('Wresting control of the game took the team most of the second half.','球队花了下半场大部分时间，才把比赛控制权夺到手。'),sources=S('wresting','wrest'))
PRY=[['打探支：中古英语 prien → pry','较早是好奇窥看，最远来源未定，或联系较早眨眼材料'],['撬动支：旧 prize 的杠杆、抓持名词 → pry','可能把末尾音误当复数而改形，接法语 prise 抓取材料；与打探支近源分开']]
W('pry','/praɪ/','打探、窥探；撬开、撬动；逼问出',
 '有人不想讲私事，你还探头问下去，是 pry；用工具把紧盖子撬起，也叫 pry。两幅现代画面可帮助理解，但历史近源分两条。',
 '打探义接中古英语 prien，早源未定；撬动义接旧 prize 的杠杆名词，变形涉及把末尾音看作复数的分析，不从“好奇”直接造出撬棍。',PRY,
 'pry into private matters 是打探私事，pry the lid off 是撬下盖子；pry information out of someone 是设法问出消息。',
 'I do not mean to pry 我无意打探；pry it open 把它撬开。',
 'pry into 常带越过私人边界、令人不舒服的语气，ask 只是问；撬开用法常见于美式英语，英式也常用 prise。',
 ('I do not want to pry into your personal life.','我不想打探你的私生活。'),('He used a flat tool to pry the lid off the box.','他用扁工具把盒盖撬下来。'),sources=S('pry','pry'))
W('pries','/praɪz/','打探、撬开、逼问出〔第三人称单数〕',
 '一个人爱追问私事，用 pries；手拿工具把紧处撬开，也用 pries。两条来源在现代碰巧用同一组变化。',
 'pry 改 y 为 i + 完整 -es → pries，读 /praɪz/；打探与撬动两条动词均作此三单变化。',PRY+[['pry 改 y 为 i + -es → pries','他、她打探或撬开']],
 'pries into private affairs 是打探私事，pries the lid open 是撬开盖；pries an answer out of someone 是设法逼问出答案。',
 'pries too much 过分打探；pries it loose 把它撬松。',
 'pries 和 prize 同音但不是相同拼写：she pries 是她打探、撬动，a prize 是奖品；句型可直接分出。',
 ('She never pries into her neighbours\' private lives.','她从不打探邻居的私生活。'),('He pries the lid open with a small tool.','他用小工具撬开盖子。'),sources=S('pries','pry'))
W('pried','/praɪd/','打探、撬开、逼问出了',
 '刚才追问某件私事，或把紧紧贴住的盖子撬开，是 pried；若接消息和 out of，也可能像把话从人嘴里撬出来。',
 'pry 改 y 为 i + 完整 -ed → pried，词尾读 /d/；两条近源不同的动词在现代用同形过去式。',PRY+[['pry 改 y 为 i + -ed → pried','过去打探、撬动或问出']],
 'pried into the matter 是追问、打探，pried the lid off 是撬下盖子；pried a name out of someone 是费劲问出名字。',
 'pried it apart 把它撬开；pried too far 打探过头。',
 'pried open 强调克服贴合、闭合而撬，opened 只说打开；松松的盖子轻拿下来也可 opened，不必 pried。',
 ('She pried the lid off the old tin.','她把旧铁罐的盖子撬下来。'),('He never pried into why she had left.','他从不打探她为什么离开。'),sources=S('pried','pry'))
W('prying','/ˈpraɪɪŋ/','正在打探、撬动；爱打探的、窥探的',
 '一直探问别人不愿讲的事，是 prying；手正把缝隙一点点撬开，也能用同形分词。prying eyes 则像探头探脑的目光。',
 'pry + 完整 -ing，保留末尾 y → prying；打探分词还固定作形容词，常修饰问题、目光或爱探问的人。',PRY+[['pry + -ing → prying','打探、撬动过程；窥探性质']],
 'prying questions 是打探隐私的问题，away from prying eyes 是避开窥探的目光；prying a lid open 则讲实际撬盖。',
 'stop prying 别再打探；prying the boards apart 撬开木板。',
 'curious 只是好奇，prying 通常觉得探得不合适；同样想了解，用词会给对方不同评价。',
 ('She disliked his prying questions about her family.','她不喜欢他打探自己家事的问题。'),('He was prying the boards apart with a flat tool.','他正用扁工具把木板撬开。'),sources=S('prying','pry'))
PRIZE=[['价值支：拉丁语 pretium → 法语价值、评价材料 → prize','奖赏名词与珍视动词在这里相关'],['抓取支：拉丁语 prehendere、prendere → 法语 prise → prize','战利品、杠杆抓持材料；撬动动词另走此支']]
W('prized','/praɪzd/','珍视、看重了；珍贵的、深受珍视的；撬开了',
 '一件老物件未必值很多钱，却被主人当宝贝，是 prized。另一个同形动词可说用工具撬开，英式也常写 prised，来源与珍视分开。',
 'prize 去末尾 e + 完整 -ed → prized，/z/ 后读 /d/；珍视支接价值词族，撬动支接抓取、杠杆材料。',PRIZE+[['prize 去 e + -ed → prized','已看重、珍视；珍爱的状态；另一支撬开']],
 'a prized possession 是珍爱之物，prized for its beauty 是因美而受珍视；prized open 则是撬开，读句子宾语即可分出。',
 'highly prized 很受珍视；prized the lid off 撬下盖子。',
 'prized 描写被看重，expensive 描写价格高；一本旧本子可能非常 prized，却不贵。',
 ('The old camera was one of her most prized possessions.','那台旧相机是她最珍爱的物品之一。'),('He prized the lid off with a small tool.','他用小工具把盖子撬下来。'),sources=S('prized','prize'))
W('prizing','/ˈpraɪzɪŋ/','正在珍视、看重；正在撬开、撬取',
 '把诚实、自由放在心里很高的位置，是 prizing；手正用工具把缝隙撬开，也可能拼作 prizing。两条词史不因同形就合成一条。',
 'prize 去末尾 e + 完整 -ing → prizing，z 读 /z/；撬动义的 prise 对应 prising 也是常见写法。',PRIZE+[['prize 去 e + -ing → prizing','看重的过程；另一支撬动过程']],
 'prizing honesty above comfort 是把诚实看得比安逸更重要；prizing the lid open 是撬开盖子，具体对象会把义项分明。',
 'prizing independence 珍视独立；prizing two boards apart 撬开两块木板。',
 'prizing 与 pricing 只差中间字母，却是不同动作：prize 是珍视或撬，price 是定价；后者中间读 /s/。',
 ('She grew up prizing honesty above popularity.','她从小就把诚实看得比受欢迎更重要。'),('He was prizing the lid open with a flat tool.','他正用扁工具撬开盖子。'),sources=S('prizing','prize'))
LEVER=[['古法语举起工具名 → 英语 lever','接拉丁语 levare 抬起、levis 轻的材料，名词杠杆较早'],['杠杆名词 → 英语 lever 撬动动词','像把省力的支点办法变成一个可做的动作']]
W('levers','英 /ˈliːvəz/；美 /ˈlevərz/','杠杆、操纵杆〔复数〕；用杠杆撬动〔第三人称单数〕',
 '一根硬杆靠支点把另一端撬起，是 lever；几根操纵杆叫 levers。动词 levers 则把工具变成动作：借杠杆把重处撬起来。',
 'lever + -s，读 /z/；基础词在英美常见读音不同，名词复数与较晚从名词来的动词三单同形。',LEVER+[['lever + -s → levers','多个杠杆；他、她借杠杆撬动']],
 'control levers 是操纵杆，levers the stone up 是把石头撬起；levers of power 像控制机器的杆，指影响权力的手段。',
 'pull the levers 拉操纵杆；levers the board loose 撬松木板。',
 'levers 的工具义与动作义看句型；lifts 只说举起，levers 还说明借杆、支点的撬法。',
 ('The machine has three control levers.','机器有三根操纵杆。'),('He levers the stone up with a metal bar.','他用金属杆把石头撬起来。'),sources=S('levers','lever'))
W('levered','英 /ˈliːvəd/；美 /ˈlevərd/','用杠杆撬起、撬动了；借力挤出、抬起了',
 '刚才把杆子插进缝里，借支点把重板撬起来，是 levered；身体撑着某处费力起来，也能借这股撬升的画面。',
 'lever + 完整 -ed，读 /d/；基础 er 留着，杠杆名词较早，现代动词再接过去词尾。',LEVER+[['lever + -ed → levered','过去用杆或支点撬动']],
 'levered the lid off 是撬下盖子，levered the slab up 是撬起板块；levered himself out 是撑着把自己从低处挪起。',
 'levered it loose 撬松；levered apart 撬开。',
 'levered 强调借支点的撬法，yanked 强调急促猛拉；结果都可能让物体脱开，但用力方式不同。',
 ('They levered the heavy slab up with a bar.','他们用杆子把沉板撬起来。'),('He levered himself out of the low chair.','他撑着身子，费劲从低椅子里站起来。'),sources=S('levered','lever'))
W('levering','英 /ˈliːvərɪŋ/；美 /ˈlevərɪŋ/','正在用杠杆撬动、撑起；撬动行为',
 '硬杆一端往下压，另一端把板、石头顶起来，是 levering；它让人看到力量通过支点换了方向。',
 'lever + 完整 -ing，直接加；英式在元音词尾前发 r，动作分词仍来自整个杠杆动词。',LEVER+[['lever + -ing → levering','借支点撬动的过程']],
 'levering up a slab 是正撬起石板，levering a lid off 是撬下盖子；levering himself up 是撑着把自己弄起。',
 'levering it into place 把它撬到位；levering two pieces apart 撬开两块。',
 'levering 与 prying 在撬开东西时常重叠，levering 更直接让人想到杠杆和支点；prying 还另有打探隐私的来源分支。',
 ('They were levering the slab up with a metal bar.','他们正用金属杆撬起石板。'),('He loosened the lid by levering it upwards.','他把盖子向上撬，弄松了它。'),sources=S('levering','lever'))
HEFT=[['heave 的抬举材料 → heft 的重量名词','受 theft、weft 一类旧名词模式和旧分词影响，不是现代 heave 规则过去式'],['重量、分量名词 → heft 的抬起掂量动词','拿起来，才摸得到、试得到它有多沉']]
W('hefts','/hefts/','举起掂量、抬起〔第三人称单数〕；重量、举起动作〔复数〕',
 '手把石头或包提起来，试试到底多沉，是 hefts。动作不只是移位置，还像在手里感受、承担它的分量。',
 'heft + -s，/t/ 后读 /s/；动词由更早重量名词发展，名词又联系 heave 的旧材料，不能机械排成现代动词先于名词。',HEFT+[['heft + -s → hefts','他、她举起试分量；几次举起或不同分量']],
 'hefts the bag 是举起包掂掂分量，hefts the hammer 是拿起锤子试手感；名词 heft 更多常直接说整体分量。',
 'hefts it in one hand 单手举着掂量；hefts the stone 抬起石头试分量。',
 'hefts 常有拿起来感受重量的意味，weighs 可以用秤精确称；手里一掂不一定得到数字。',
 ('She hefts the bag before putting it in the trolley.','她先掂了掂包的分量，再把它放进推车。'),('He hefts the hammer to test its balance.','他拿起锤子掂了掂，试试重心。'),sources=S('hefts','heft'))
W('hefted','/ˈheftɪd/','举起掂量了；抬起、提起了',
 '刚才把包拿起来，在手里感受了一下沉不沉，是 hefted；也能单说费劲提起一个有分量的东西。',
 'heft + 完整 -ed，/t/ 后读 /ɪd/，多一个音节；ft 后直接加，词根本身的 t 原本就有。',HEFT+[['heft + -ed → hefted','过去举起、感受分量']],
 'hefted the stone in his hand 是拿石头掂量，hefted the pack onto his shoulder 是把背包提到肩上；后者可突出搬起重量。',
 'hefted it experimentally 试着掂了掂；hefted the sack onto his back 把袋子提到背上。',
 'hefted 与 heaved 都可抬重物，hefted 常更像拿起、试分量，heaved 更明显写费大劲挪抬；具体句子中也能重叠。',
 ('He hefted the stone in his hand before setting it down.','他在手里掂了掂石头，随后放下。'),('She hefted the bag onto her shoulder.','她把包提到肩上。'),sources=S('hefted','heft'))
W('hefting','/ˈheftɪŋ/','正在举起掂量、抬起；掂量动作',
 '手正提起东西、试它的分量，是 hefting。像不用秤，先让手和胳膊告诉你它有多沉、握着顺不顺。',
 'heft + 完整 -ing，直接加；现代分词接已固定的 heft 动词，不把它重新当作 heave 的过去式再加词尾。',HEFT+[['heft + -ing → hefting','举起、手试分量的过程']],
 'hefting a bag 是提包掂重，hefting a tool 是拿起工具试手感；into、onto 后可指出要移到的位置。',
 'hefting it in one hand 单手掂量；hefting the pack onto his back 把背包提到背上。',
 'hefting 重在拿起来、感到分量，judging the weight 可以只凭看或估算；它把抽象估重变成具体手上动作。',
 ('She was hefting two bags to decide which was lighter.','她正掂着两个包，判断哪个更轻。'),('He stood hefting the new hammer in one hand.','他站在那里，单手掂着新锤子。'),sources=S('hefting','heft'))

def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfp',ROOTS,WORDS)
 extend_lessons()
