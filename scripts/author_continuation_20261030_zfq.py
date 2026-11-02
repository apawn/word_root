"""Grasping, gripping tight, pinching and making small adjustments."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3641':dict(words='grab grasp grasps grasped grasping'.split(),label='grasp 的实物抓握、理解与贪抓',note='grasp 可能由较早 grapsen 音位换位，联系 grab 的抓取材料；grasping 贪婪形容词记录很早，不把它当现代理解义之后才出现。'),
 'B4116':dict(words=['clip','clipped'],label='clipped：剪短、夹住与短促语气',note='剪切 clip 接北欧材料，夹紧支接古英语 clyppan；两条现代同形都可双写 p 加完整 -ed，短促言语又联系剪短支。'),
 'A1851':dict(words='snip snips snipped snipping'.split(),label='snippet 周围的 snip 基础动作变化',note='本组给 snippet 小片段的基础词补语境；snip 本身不是 -et 小称后缀词，名词剪下小片记录早于相应剪切动词。'),
 'A1760':dict(words='grasp grasps grasped grasping clutch clutches clutched clutching clench clenches clenched clenching pinch pinches pinched pinching snip snips snipped snipping clip clipped nip nips nipped nipping tweak tweaks tweaked tweaking'.split(),label='抓、攥、捏、剪、咬和微调的词形',note='grasped、clutched、clenched、pinched、snipped、clipped、nipped、tweaked 的 -ed 都读 /t/，但基础词末尾辅音组合各异；不要统一再添 /ɪd/。'),
}
GRASP=[['较早抓摸材料、grapsen 等 → 可能换位为 grasp','日耳曼 *grap-、*grab- 一系，相关路线有重建和分析部分'],['抓、摸材料继续发展 → 抓牢、理解；贪抓形容较早已见','用脑把意思抓住是现代好用的图景；各义记录不硬排成简单直线']]
W('grasps','英 /ɡrɑːsps/；美 /ɡræsps/','抓牢、抓住；理解〔第三人称单数〕；抓握〔复数〕',
 '手伸出把栏杆抓住，叫 grasps；脑子把一个道理弄明白，也像终于把它抓牢。实物和意思都能成为被抓住的对象。',
 'grasp + -s，/p/ 后读 /s/，结尾 /sps/；动词三单与抓握名词复数同形，历史与 grab 的抓摸材料相关。',GRASP+[['grasp + -s → grasps','他、她抓住东西或弄懂意思']],
 'grasps the handle 是抓住把手，grasps the point 是领会重点；grasps at a chance 是急着抓机会，at 带伸手追抓感。',
 'grasps the idea 理解想法；grasps it firmly 抓牢它。',
 'grasps 的理解义像抓牢重点，memorises 是记住；背得下来不一定真的 grasp the idea。',
 ('She grasps the rail before stepping onto the boat.','她先抓住栏杆，再踏上船。'),('He quickly grasps the main idea.','他很快就领会了主要意思。'),sources=S('grasps','grasp'))
W('grasped','英 /ɡrɑːspt/；美 /ɡræspt/','抓牢、抓住了；领会、理解了',
 '刚才手把绳头抓牢，或听到解释后突然懂了，是 grasped。后一种像原本滑走的道理终于落进掌心。',
 'grasp + 完整 -ed，/p/ 后读 /t/，结尾 /spt/；sp 后直接加，不双写 p。',GRASP+[['grasp + -ed → grasped','过去抓牢；已理解重点']],
 'grasped her hand 是握住她的手，grasped the meaning 是领会含义；had not grasped the problem 是还没弄懂问题。',
 'grasped the opportunity 抓住机会；grasped what had happened 弄明白发生了什么。',
 'grasped 关注拿住或领会，不只看见、听见；heard the explanation 是听到解释，grasped it 才是懂了。',
 ('He grasped the rope with both hands.','他双手抓牢绳子。'),('I finally grasped why the two answers were different.','我终于弄懂了两个答案为什么不同。'),sources=S('grasped','grasp'))
W('grasping','英 /ˈɡrɑːspɪŋ/；美 /ˈɡræspɪŋ/','正在抓住、领会；贪婪的、贪得无厌的',
 '手正伸出去抓，或脑子正试着弄懂，是 grasping；形容一个人总想多抓好处，a grasping person 就是贪婪的人。',
 'grasp + 完整 -ing，直接加；贪婪形容词很早已有，不能只按今天学习顺序写成理解义之后才生出来。',GRASP+[['grasp + -ing → grasping','抓取、理解过程；贪抓利益的性质']],
 'grasping the handle 是正抓住把手，grasping the problem 是领会问题；a grasping attitude 是贪得无厌的态度。',
 'grasping for support 伸手抓支撑；grasping at straws 抓住一点不可靠希望。',
 'grasping 作人物形容词有贪婪评价，grasping a difficult idea 却只是理解动作；同形 -ing 不固定带同一种褒贬。',
 ('She climbed onto the boat, grasping the rail tightly.','她紧抓栏杆，爬上船。'),('The story portrays a grasping landlord who always wants more.','故事刻画了一个总嫌不够、贪得无厌的房东。'),sources=S('grasping','grasp'))
CLUTCH=[['抓握支：古英语 clyccan 的合拢、弯指材料 → clutch','手指弯起来抓紧，后来也受爪相关形式影响'],['抓握 → 离合器的接合、分离；紧要关头','机械把工作部件接合像抓住；一窝蛋另来自孵化支线']]
W('clutch','/klʌtʃ/','紧抓、抱紧；抓握、控制；离合器；小手包；一窝蛋；关键时刻',
 '怕东西掉，手紧紧攥住，是 clutch。离合器把传动部分接上、分开，像抓住再放开；手拿的小包也叫 a clutch。一窝蛋是另一条来源。',
 '抓握动词接古英语 clyccan 的弯指、合拢材料；机械、小包义围绕抓持展开。一窝蛋另接 cletch、cleck 的孵化材料，不是母鸟用爪攥出的词。',CLUTCH,
 'clutch a bag 是紧抱包，release the clutch 是松离合器，a clutch of eggs 是一窝蛋；in the clutch 是关键时刻，美式体育也常用 clutch 形容关键时刻发挥好。',
 'clutch at a rope 伸手紧抓绳；in someone\'s clutches 落在某人控制中。',
 'clutch 常比 hold 更有紧、急、不愿松手的感觉；hold 只要拿着，clutch 往往让人想到担心失去、需要抓牢。',
 ('She kept a tight clutch on her bag in the crowd.','在人群里，她一直紧紧抓着包。'),('Press the clutch before changing gear.','换挡前踩下离合器。'),sources=S('clutch','clutch'))
W('clutches','/ˈklʌtʃɪz/','紧抓、抱紧〔第三人称单数〕；掌控、抓握；离合器、小手包、窝蛋〔复数〕',
 '一个人把包紧抱住，用 clutches；in his clutches 像落进他攥紧的手里，表示受他控制。几套离合器、几窝蛋又是相应名词复数。',
 'clutch + -es，/tʃ/ 后读 /ɪz/；动词三单与不同来源名词的复数同形，一窝蛋支仍和抓握支近源分开。',CLUTCH+[['clutch + -es → clutches','他、她紧抓；控制之手；多套装置或多窝蛋']],
 'clutches her bag 是紧抱包，escape his clutches 是逃出他的控制；several clutches of eggs 是几窝蛋。',
 'clutches at the rail 伸手紧抓栏杆；the clutches of fear 恐惧的控制。',
 'clutches 在掌控搭配里常带被控制、难脱身的感觉；hands 只说手，不能在所有语境里替换出这种压力。',
 ('She clutches her bag as the train fills up.','车厢挤满人时，她紧抱着包。'),('The hero finally escapes the villain\'s clutches.','主人公终于逃出了反派的控制。'),sources=S('clutches','clutch'))
W('clutched','/klʌtʃt/','紧抓、攥住、抱紧了',
 '刚才身子不稳，立刻把栏杆攥牢，或把信压在胸前不放，是 clutched。动作有一股抓得紧、贴得近的感觉。',
 'clutch + 完整 -ed，/tʃ/ 后读 /t/，结尾 /tʃt/；现代规则过去式，不额外加 /ɪd/。',CLUTCH+[['clutch + -ed → clutched','过去紧抓、抱牢']],
 'clutched the rail 是紧抓栏杆，clutched the letter to her chest 是把信紧抱在胸前；clutched at 是伸手急抓。',
 'clutched in one hand 紧攥在一只手里；clutched at his sleeve 急抓他的袖子。',
 'clutched 是抓住一个对象，clenched 常把手、牙关等本身合紧；clutched a bag 是抱包，clenched a fist 是攥拳。',
 ('He clutched the rail as the boat rocked.','船晃时，他紧紧抓住栏杆。'),('She clutched the letter to her chest.','她把信紧紧抱在胸前。'),sources=S('clutched','clutch'))
W('clutching','/ˈklʌtʃɪŋ/','正在紧抓、抱牢；紧攥着的',
 '手或胳膊正把东西抓得很紧、不想让它离开，是 clutching；像人挤在车里护住包，或紧攥一张重要纸条。',
 'clutch + 完整 -ing，直接加；ch 的 /tʃ/ 保留，分词描写紧抓过程、伴随姿势。',CLUTCH+[['clutch + -ing → clutching','抓紧不放的过程']],
 'clutching a ticket 是紧攥着票，clutching a bag to her chest 是把包紧抱在胸前；clutching at straws 是抓不可靠的希望。',
 'clutching the rail 紧抓栏杆；clutching at support 伸手急抓支撑。',
 'clutching 常有急切、用力抱持的画面，carrying 只说携带；包轻松拎着是 carrying，担心丢了紧抱是 clutching。',
 ('She ran towards us, clutching the ticket we had been looking for.','她紧攥着我们一直在找的那张票，朝我们跑来。'),('He stood clutching the rail with both hands.','他站着，双手紧抓栏杆。'),sources=S('clutching','clutch'))
CLENCH=[['古英语 (be)clencan 的抓牢、使贴紧 → clench','历史上是 clingan 一系的使动材料，可联系 cling、clinch'],['使紧固 → 攥拳、咬紧牙等合紧动作','现代最常见对象是 fist、teeth、jaw，像把松开的部分收拢锁紧']]
W('clench','/klentʃ/','攥紧、咬紧、使紧闭；紧握、合紧',
 '五指缩进去，把拳头攥牢；牙齿上下压紧，都是 clench。像把原来有空隙的部位合上、收紧。',
 '承古英语 clencan 的抓牢、使贴紧义，是 clingan 一系的旧使动材料，和 cling、clinch 有历史联系；现代整词表示合紧。',CLENCH,
 'clench your fists 是攥紧拳头，clench your teeth 是咬紧牙，clench your jaw 是绷紧牙关；也能紧握着东西。',
 'a tight clench 紧紧一握；clench in frustration 因懊恼攥紧。',
 'clench 常收紧拳、牙关等部位，clutch 常抓着外部对象；握拳的形状是 clench，紧抱手包则 clutch。',
 ('Try not to clench your jaw while you concentrate.','专注时尽量别把牙关绷得那么紧。'),('He began to clench his fists under the table.','他开始在桌下攥紧拳头。'),sources=S('clench','clench'))
W('clenches','/ˈklentʃɪz/','攥紧、咬紧、合紧〔第三人称单数〕；紧握动作〔复数〕',
 '一个人把拳头收牢、牙关压紧，用 clenches；主语也可以直接是手、牙关，表示那个部位自己紧起来。',
 'clench + -es，/tʃ/ 后读 /ɪz/，多一个音节；常见作动词三单，也有相应动作名词复数。',CLENCH+[['clench + -es → clenches','他、她或身体部位合紧']],
 'clenches his fists 是攥拳，her jaw clenches 是她牙关一紧；前者让人动作，后者把身体反应放在主语。',
 'clenches her teeth 咬紧牙；clenches in frustration 懊恼得紧起来。',
 'clenches 不自动等于发怒，也可能紧张、专注或用力；是否生气要看情境，词先描写合紧的动作。',
 ('He clenches his fists when the match gets tense.','比赛紧张时，他会攥紧拳头。'),('Her jaw clenches whenever she concentrates too hard.','她一过分专注，牙关就会绷紧。'),sources=S('clenches','clench'))
W('clenched','/klentʃt/','攥紧、咬紧了；紧闭、合紧的',
 '拳头已缩得紧紧，牙关已绷住，是 clenched。a clenched fist 让人看见五指收在掌心，手没有张开。',
 'clench + 完整 -ed，/tʃ/ 后读 /t/，结尾 /ntʃt/；过去式、过去分词和状态形容词同形。',CLENCH+[['clench + -ed → clenched','已经攥紧、咬紧的动作或状态']],
 'clenched fists 是攥紧的拳头，through clenched teeth 是从咬紧的牙缝间说；可描写紧张、怒气或强忍。',
 'clenched jaw 绷紧的牙关；clenched in his hand 紧握在手中。',
 'clenched 强调合紧的力量，closed 只说关闭状态；手轻轻合上可以 closed，攥得用力才更像 clenched。',
 ('She clenched her fists and waited for the result.','她攥紧拳头，等着结果。'),('He spoke through clenched teeth.','他咬着牙，从牙缝里说话。'),sources=S('clenched','clench'))
W('clenching','/ˈklentʃɪŋ/','正在攥紧、咬紧、合紧；攥握、咬紧动作',
 '手正从张开变成拳头，牙关正越来越绷紧，是 clenching。也可把反复这样用力当作一个动作习惯来讲。',
 'clench + 完整 -ing，直接加；ch 保留 /tʃ/，现代词尾接完整 clench，不需改基础元音。',CLENCH+[['clench + -ing → clenching','从松开到合紧的过程']],
 'clenching his fists 是正在攥拳，jaw clenching 是咬紧牙关这个动作；可出现于紧张、专注、压抑情绪的描写。',
 'clenching her teeth 咬紧牙；keep clenching 反复合紧。',
 'clenching 主要写向内收紧，gripping 主要写抓牢某个对象；攥空拳用 clenching，抓紧栏杆通常 gripping。',
 ('He was clenching and unclenching his fists.','他正反复攥紧、松开拳头。'),('She noticed herself clenching her jaw during the difficult puzzle.','做那道难题时，她发现自己把牙关绷紧了。'),sources=S('clenching','clench'))
PINCH=[['中古英语 pinchen，借法语捏、夹材料 → pinch','法语更远来源未定；穿刺、点等拉丁词源属于候选分析'],['夹压动作、疼痛、吝啬等分支；名词急用处境较早已见','一撮盐是两指捏起的一点；in a pinch 的紧急处境名词记录更早']]
W('pinch','/pɪntʃ/','捏、夹、夹痛；节省、偷拿〔口语〕；一捏、一撮；急用关头',
 '两根手指往中间夹一点，是 pinch；一撮盐就像两指捏住的那一点。鞋太紧夹得脚疼、手头紧得开支被挤，也能借这个夹压画面。',
 '经中古英语 pinchen 借法语捏夹材料，更早来源不定。名词紧要关头的记录早于“一捏、一撮”，学习图景不代表所有义都按物理名词先后派生。',PINCH,
 'a pinch of salt 是一撮盐，shoes pinch 是鞋夹脚；in a pinch 是急用时、必要时，take it with a pinch of salt 是别全信。',
 'pinch the edge 捏住边；feel the pinch 感到手头紧；pinch pennies 精打细算、抠钱。',
 'pinch 是局部从两边夹，squeeze 更宽，可以整手、整个空间挤压；取一撮盐用 pinch，挤柠檬通常 squeeze。',
 ('Add a pinch of salt to the mixture.','往混合物里加一撮盐。'),('These shoes pinch my toes.','这双鞋夹我的脚趾。'),sources=S('pinch','pinch'))
W('pinches','/ˈpɪntʃɪz/','捏、夹痛、节省、偷拿〔第三人称单数〕；几捏、几撮〔复数〕',
 '一个人捏住小部分，或鞋紧得夹脚，动词用 pinches；调味时加几小撮，也叫 a few pinches。',
 'pinch + -es，/tʃ/ 后读 /ɪz/；动词三单与捏夹、少量名词复数同形。',PINCH+[['pinch + -es → pinches','它夹压；几下捏夹或几撮']],
 'pinches the fabric 是捏住布，pinches at the heel 是在脚跟处夹痛；two pinches of salt 是两撮盐。',
 'pinches her nose 捏住鼻子；pinches pennies 在小开支上非常节省。',
 'pinches 可以写实际夹痛，也能说花钱抠得紧；pinches pennies 的意思在整个搭配里，不能译成捏几枚硬币。',
 ('The new shoe pinches at the heel.','新鞋在脚跟处夹得疼。'),('She added two pinches of salt.','她加了两撮盐。'),sources=S('pinches','pinch'))
W('pinched','/pɪntʃt/','捏、夹、偷拿了；被夹压的；瘦削憔悴的、拮据的',
 '手指刚才被门夹了，或一处布被两指捏起，是 pinched；脸显得又瘦又紧、生活手头紧，也像被挤得没有余量。',
 'pinch + 完整 -ed，/tʃ/ 后读 /t/，结尾 /ntʃt/；分词还固定成憔悴、拮据等形容用法。',PINCH+[['pinch + -ed → pinched','过去捏夹；夹紧、削瘦或资源紧的状态']],
 'pinched her fingers 是夹了她的手指，a pinched face 是瘦削憔悴的脸；pinched a biscuit 是口语偷拿了一块饼干。',
 'pinched the edge together 把边捏拢；financially pinched 手头拮据。',
 'pinched 的瘦削义常带疲惫、不好过的紧缩感，slim 可以只说苗条；形容脸时不能全当中性的瘦。',
 ('He pinched the edges of the dough together.','他把面团的边捏拢。'),('Her face looked pinched after the sleepless night.','一夜没睡，她的脸显得瘦削憔悴。'),sources=S('pinched','pinch'))
W('pinching','/ˈpɪntʃɪŋ/','正在捏夹、夹痛、节省、偷拿；捏夹动作',
 '两指正把布夹起一点，鞋正把脚挤得不舒服，是 pinching；pinching pennies 则像连小钱都抓得紧紧的。',
 'pinch + 完整 -ing，直接加；分词能描述夹压动作，也可把捏夹看作一类行为。',PINCH+[['pinch + -ing → pinching','捏夹、局部挤压的过程']],
 'pinching the fabric 是捏着布，shoes are pinching 是鞋正在夹脚；pinching pennies 是在开支上非常节省。',
 'pinching the ends together 把两端捏拢；a pinching sensation 像被夹的感觉。',
 'pinching 常是局部夹压，clenching 常是把拳、牙关收紧；两指取少量盐像 pinching，不是把整只拳头攥住。',
 ('She was pinching the fabric to mark where the fold should go.','她正捏着布，标出该折的位置。'),('My shoes were pinching by the end of the walk.','走到最后，我的鞋已经夹得脚疼。'),sources=S('pinching','pinch'))
SNIP=[['德荷相关剪切材料 → 英语 snip 小片段名词','较早指剪下的一小片，可能有拟声基础'],['小片段名词 → 快速剪切动词','后来动作、剪下物都可用 snip，现代扩展再接完整词尾']]
W('snips','/snɪps/','剪一小下、剪断〔第三人称单数〕；小剪口、剪下小片；小剪钳〔复数〕',
 '剪刀咔嚓一小下，剪掉线头，是 snips；剪下的小片、几次小剪也可同形。工具 snips 常是一种小剪子、剪钳。',
 'snip + -s，/p/ 后读 /s/；动词三单与动作、小片段等名词复数同形，工具复数用法也常见。',SNIP+[['snip + -s → snips','它轻快剪断；几小片或小剪钳']],
 'snips off a thread 是剪掉线头，a few snips 是咔嚓剪几下；metal snips 是剪薄金属用的剪钳。',
 'snips the ribbon 剪丝带；small snips of paper 剪下的小纸片。',
 'snips 比 cuts 更有剪刀短促剪下一点的感觉；cut 可以很长、很慢，也可以不是用剪刀。',
 ('She snips off the loose thread.','她剪掉松线头。'),('A few careful snips made the edge even.','仔细剪了几下，边缘就齐了。'),sources=S('snips','snip'))
W('snipped','/snɪpt/','剪了一小下、剪掉、剪断了',
 '刚才用剪刀把线头、纸角咔嚓剪掉，是 snipped；让人想到一个短而清楚的小剪切。',
 'snip 双写 p + 完整 -ed → snipped，/p/ 后读 /t/；短元音重读单音节按规则双写。',SNIP+[['snip 双写 p + -ed → snipped','过去轻快剪断、剪掉一点']],
 'snipped off the corner 是剪去一角，snipped through the string 是剪断细绳；off 常指出被剪掉的部分。',
 'snipped the ribbon 剪断丝带；snipped into small pieces 剪成小片。',
 'snipped 的动作通常较小、短促，sliced 更像用刀沿面切开；剪一根线头常用 snipped。',
 ('He snipped the string with small scissors.','他用小剪刀剪断细绳。'),('She snipped a damaged leaf off the plant.','她从植物上剪掉一片损坏的叶子。'),sources=S('snipped','snip'))
W('snipping','/ˈsnɪpɪŋ/','正在轻快剪切、剪掉；小剪切动作',
 '剪刀正一口一口剪，把线头、细枝、小纸片剪下来，是 snipping；画面是短促的小开合。',
 'snip 双写 p + 完整 -ing → snipping；分词和动作名词都接固定的 snip，不改基础元音。',SNIP+[['snip 双写 p + -ing → snipping','剪刀轻快剪切的过程']],
 'snipping loose threads 是剪线头，snipping paper into shapes 是把纸剪成形状；也可听见 the snipping of scissors。',
 'snipping off the tips 剪掉尖端；keep snipping 继续一小下下剪。',
 'snipping 常强调剪刀多次小动作，tearing 是用手拉裂；同样让纸变小片，边缘和动作画面不同。',
 ('She sat snipping paper into small stars.','她坐着，把纸剪成小星星。'),('We could hear him snipping loose threads from the curtain.','我们能听见他在剪窗帘上的松线头。'),sources=S('snipping','snip'))
CLIP=[['剪切支：北欧 klippa 等 → clip','剪短、修剪，后来也说说话短促、截短'],['夹住支：古英语 clyppan 抱住 → clip','拥抱、围住的旧义发展为夹紧，两支现代拼写同形']]
W('clipped','/klɪpt/','剪短、修剪了；夹住、扣上了；擦碰了；短促生硬的',
 '树篱被剪齐，纸被夹在板上，都可 clipped，却分属剪、夹两条来源。a clipped voice 像话音被剪短，说话很短促，常显得生硬。',
 'clip 双写 p + 完整 -ed → clipped，/p/ 后读 /t/；剪切支借北欧材料，夹紧支承古英语抱住材料。',CLIP+[['clip 双写 p + -ed → clipped','两支同形过去式；短促言语的状态']],
 'clipped the hedge 是修剪树篱，clipped the pass to his shirt 是把通行证夹在衣服上；clipped tones 是短促生硬的语调。',
 'neatly clipped 修剪整齐的；clipped to a board 夹在板上；clipped the kerb 擦碰路缘。',
 'clipped 的剪、夹需看对象和介词；a clipped reply 说回答短促，并不是把那句话用夹子夹住。',
 ('She clipped the note to the front of the folder.','她把便条夹在文件夹正面。'),('He answered in a clipped, impatient voice.','他用短促、不耐烦的声音回答。'),sources=S('clipped','clip'))
NIP=[['中古英语 nippen，可能借或同源于德荷捏咬材料 → nip','尖锐地夹、突然咬，确切词干演变未定'],['夹咬 → 掐去尖端、冷得刺人；近代快去快回','酒的一小口名词或短自 nipperkin，不能全当现代咬一下直接变来']]
W('nip','/nɪp/','轻咬、夹、掐去；冷得刺人；快去快回；一咬、寒意；一小口酒',
 '小狗不是狠狠咬住，而是牙尖快碰一下，是 nip；冷风让皮肤像被轻咬，也有 a nip in the air。英式 nip out 则是快出去一趟。',
 '承中古英语 nippen，可能接德荷捏夹、咬的材料，更早演变不明；一小口酒的名词另有短自 nipperkin 的分析，和动作关系保留余地。',NIP,
 'nip at someone\'s heels 是咬脚跟、比喻紧追不舍，nip out to the shop 是快去趟商店；nip it in the bud 是在萌芽时止住。',
 'a nip in the air 空气里一丝刺冷；a nip of whisky 一小口威士忌。',
 'nip 常是短促、小范围的咬夹，bite 更宽；nip out 是固定的快速移动搭配，不能硬译成咬出门。',
 ('There was a nip in the air when we left home.','我们出门时，空气里有一丝刺冷。'),('I will nip to the shop before lunch.','我午饭前快去一趟商店。'),sources=S('nip','nip'))
W('nips','/nɪps/','轻咬、夹、冷得刺人；快去快回〔第三人称单数〕；轻咬、一小口〔复数〕',
 '一只小狗牙尖碰着轻咬，或一个人赶紧去隔壁再回来，动词都可用 nips；几次轻咬、几小口又可作名词复数。',
 'nip + -s，/p/ 后读 /s/；动词三单、动作名词复数等同形，酒的少量名词另有自己的近源分析。',NIP+[['nip + -s → nips','它轻咬；他、她快去一趟；几次轻咬或几小口']],
 'nips at my fingers 是轻咬我的手指，nips to the bakery 是快去趟面包店；little nips 是几下小咬或几小口。',
 'nips out for milk 出去快买牛奶；nips the leaves 冷气冻伤叶片。',
 'nips 的小咬不一定严重，但动作仍是牙夹一下；licks 是舔，感觉和接触方式不同。',
 ('The puppy nips at the loose end of the rope.','小狗轻咬着绳子松开的那头。'),('She often nips to the bakery before work.','她常在上班前快去一趟面包店。'),sources=S('nips','nip'))
W('nipped','/nɪpt/','轻咬、夹、掐断、冻伤了；快去快回了',
 '刚才牙尖快咬一下，或霜把叶尖伤了，是 nipped；英式 I nipped out 也能说我赶紧出去了一趟。',
 'nip 双写 p + 完整 -ed → nipped，/p/ 后读 /t/；短元音单音节双写，动作各支同用这个现代词形。',NIP+[['nip 双写 p + -ed → nipped','过去短促咬夹、受冷损伤或快去一趟']],
 'nipped his finger 是轻咬了手指，nipped out for bread 是快去买面包；nipped the problem in the bud 是把问题止在萌芽。',
 'nipped off the tip 掐掉尖端；leaves nipped by frost 被霜伤到的叶片。',
 'nipped out 通常暗含出去时间短、很快回来，went out 只说出去了；加上 nipped 会有小差事迅速办完的感觉。',
 ('The puppy nipped my finger while playing.','玩耍时，小狗轻咬了我的手指。'),('I nipped out to buy some bread.','我赶紧出去买了点面包。'),sources=S('nipped','nip'))
W('nipping','/ˈnɪpɪŋ/','正在轻咬、夹、掐；正快去快回；刺冷的',
 '小狗追着绳头快咬几下，是 nipping；人正快去隔壁办件小事，也能用这个词。说风 nipping，像冷气轻咬皮肤。',
 'nip 双写 p + 完整 -ing → nipping；短促咬夹、快速移动等现代搭配都接完整词尾。',NIP+[['nip 双写 p + -ing → nipping','短促咬夹、快去一趟的过程；刺冷性质']],
 'nipping at his heels 是追着咬他脚跟，nipping out for milk 是正出去快买牛奶；比喻竞争者 nipping at the heels 是紧追在后。',
 'a nipping wind 刺冷的风；nipping the buds off 掐掉芽。',
 'nipping 的快速移动常要配 out、in、to 等方向；单写 a dog nipping at a rope 则仍是小口快咬。',
 ('The puppy kept nipping at the loose rope.','小狗不停轻咬那根松绳。'),('I am nipping out for some milk.','我正要快出去买点牛奶。'),sources=S('nipping','nip'))
TWEAK=[['古英语 twiccian 等拔、急扯材料 → 中古英语 twikken → tweak','早期说捏、扯、拧一小下；具体形成仍有不确定部分'],['小幅拧动 → 近现代精细调整','像拧旋钮只改一点，让它更合适，不必大改重来']]
W('tweak','/twiːk/','微调、小改；捏扯、拧一下；一处小调整',
 '音量不合适，把旋钮只拧一点；一句话不顺，改两个词，就是 tweak。它不像拆掉重做，而是给现有东西动一点小手脚。',
 '可能承中古英语 twikken 与古英语 twiccian 的拔、扯材料；捏拧旧动作后来扩到精细调整，现代微调义是较晚发展。',TWEAK,
 'tweak the settings 是微调设置，tweak the wording 是小改措辞；a small tweak 是一处小调整，也仍可说轻捏、拧动。',
 'tweak the design 微调设计；a tweak to the schedule 时间表的一处小改动。',
 'tweak 强调改得小、精细，overhaul 是全面整修；可以对现有设计 tweak，不必整个推倒重做。',
 ('We only need to tweak the wording of the final sentence.','我们只需小改最后一句的措辞。'),('A small tweak to the layout made the page easier to read.','稍微调了一下布局，页面就更好读了。'),sources=S('tweak','tweak'))
W('tweaks','/twiːks/','微调、捏拧〔第三人称单数〕；几处小调整〔复数〕',
 '一个人把参数一点点调好，用 tweaks；设计里做的几处小改动，也叫 tweaks，不是全部换一套。',
 'tweak + -s，/k/ 后读 /s/；动词三单与小调整名词复数同形，基础 ee 保留长元音。',TWEAK+[['tweak + -s → tweaks','他、她微调；几处细小改动']],
 'tweaks the volume 是微调音量，a few tweaks to the design 是对设计的几处小改动；通常对象已存在、已有基础。',
 'minor tweaks 小幅修改；tweaks the settings 调整设置。',
 'tweaks 比 changes 更明确带小幅精修的感觉；changes 可以从一点到全部，tweaks 常在原框架上改。',
 ('She tweaks the volume until everyone can hear clearly.','她微调音量，直到大家都能听清。'),('The draft needs only a few minor tweaks.','草稿只需几处小修改。'),sources=S('tweaks','tweak'))
W('tweaked','/twiːkt/','微调、小改了；捏拧了；〔口语〕扭伤、拉到了一点',
 '刚才把现有设计改得更合适，是 tweaked；也可说小幅捏拧。I tweaked my shoulder 则像肩被拧了一下，口语说把肩拉到了。',
 'tweak + 完整 -ed，/k/ 后读 /t/；ee 保持长元音，不双写 k。微调义沿小幅拧动扩展，身体义仍抓住扭到的感觉。',TWEAK+[['tweak + -ed → tweaked','过去作小幅调整、拧动或拉到身体部位']],
 'tweaked the design 是微调设计，tweaked the wording 是小改措辞；tweaked my back 是把背拉到了一下的口语。',
 'slightly tweaked 稍微改过的；tweaked the settings 微调了设置。',
 'tweaked 的微调义不保证原东西很差，可能只是想更合适；fixed 则更常明确原来有问题、现在修好。',
 ('We tweaked the layout after seeing it on a small screen.','看到小屏幕上的效果后，我们微调了布局。'),('She tweaked the wording to make the message warmer.','她小改了措辞，让消息显得更亲切。'),('I tweaked my shoulder while lifting the suitcase.','抬行李箱时，我把肩拉到了一下。'),sources=S('tweaked','tweak')+['https://www.merriam-webster.com/dictionary/tweak'])
W('tweaking','/ˈtwiːkɪŋ/','正在微调、小改、捏拧；微调工作',
 '对着成品边看边改一点，调两个参数、挪一小块位置，是 tweaking。像手指在旋钮上转小角度，努力调到刚合适。',
 'tweak + 完整 -ing，直接加；基础 ee、k 保留，分词和动作名词都能讲小幅调整过程。',TWEAK+[['tweak + -ing → tweaking','在现有基础上精细小改的过程']],
 'tweaking the settings 是正微调设置，needs some tweaking 是还得小改一下；常见对象有措辞、设计、时间表等。',
 'a little tweaking 一点微调；keep tweaking 继续小幅改动。',
 'tweaking 侧重小改，rewriting 可以整体重写；一段话改几个词像 tweaking，换思路重新写整段则更像 rewriting。',
 ('She spent the morning tweaking the design.','她花了一上午微调设计。'),('The schedule still needs a little tweaking.','时间表还需要稍微调整。'),sources=S('tweaking','tweak'))

def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfq',ROOTS,WORDS)
 extend_lessons()
