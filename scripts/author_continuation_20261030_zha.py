"""Squelch, squish, scrunch, crunch and crush: distinct physical pictures."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1760':dict(words='squelch squelches squelched squelching'.split(),label='squelch：湿软踩压声与压下去的画面',note='squelch 的来源可能带拟声性质，早有重压、踩软物材料，后来写彻底压制。与 squeeze、squash 便于并读，但不能因此断成同一个词根。'),
 'C1188':dict(words='squash squish squishes squished squishing squishy'.split(),label='squish：软物被挤压的触感',note='squish 很可能是 squash 动词的变体，可能受旧 squiss 影响；squishy 加 -y。此处的 squash 是压碎动词，不能与另一来源的瓜类名词混为一条。'),
 'A1699':dict(words='crunch crunches crunched crunching scrunch scrunches scrunched scrunching'.split(),label='crunch 与 scrunch：咯吱、揉挤的声音和动作',note='crunch 经旧 craunch，可能拟声；scrunch 常分析为增强声感的相关形式。scr- 不是可随意套给所有单词的普通前缀。'),
 'A1697':dict(words='crush crushes crushing crushingly'.split(),label='crush：挤压、压倒与沉重打击',note='crush 经法语 cruissir、croissir，可能远接法兰克材料；抽象压倒义在早期英语已有。暗恋名词有后来的独立词义发展，不能给每个 crush 动词套上爱情解释。'),
 'A2238':dict(words='crumble crumbly'.split(),label='crumbly：碰一下就容易散成屑',note='crumble 去 e 加 -y，形成易散碎的性质。它与 crunchy 的咬下去清脆感不同，食物可能兼有两种性质。'),
}
SQUELCH=[['早期 squelch：重踩、压在软物上','来源未全定，可能模仿压踩声'],['压踩动作 → 完全压制等抽象用法','现代也写踩着湿泥发声行走']]
SQUISH=[['squash 动词 → 可能的变体 squish','也可能受旧 squiss 挤、压影响'],['挤压软物的动作、声音 → squishy','用软软、容易挤变形的触感串联']]
CRUNCH=[['旧 craunch → crunch','可能模仿咬碎、压碎时的咯吱声'],['crunch → 相关增强声感形式 scrunch','scrunch 后来也说揉成一团、缩拢身体；不把所有 scr- 都当同一前缀']]
CRUSH=[['古法语 cruissir、croissir → crush','咬碎、压碎等，更远可能接法兰克材料'],['压碎、压倒 → 心理上击垮等现代搭配','早期英语已有抽象压倒义，不能给所有意义硬排物理先、心理后']]
W('squelch','/skweltʃ/','踩着湿软物扑哧作响；压下、制止',
 '靴子踩进烂泥，挤出“扑哧”一声，是 squelch。把某件事压得冒不出来，也能用这个词：squelch a rumour 把传言压下去。',
 '较早写重重踩压软物，可能带拟声来源；后来有完全压制、制止义。现代湿泥声的画面帮助记忆，但不能据它硬造一个古拉丁拆法。',SQUELCH,
 'squelch through mud 踩着泥扑哧走；squelch rumours 压住传言；squelch enthusiasm 打消热情。',
 'squelch an idea 压下想法；wet shoes squelch 湿鞋扑哧作响。',
 'squelch 强调压住、闷下去或湿软踩压声，splash 更突出液体溅开；踩同一块泥可能两种情况都有。',
 ('Our boots began to squelch in the wet mud.','我们的靴子在湿泥里开始扑哧作响。'),('He tried to squelch the rumours by explaining what had happened.','他解释了事情经过，试图把传言压下去。'),sources=S('squelch','squelch'))
W('squelches','/ˈskweltʃɪz/','扑哧作响、压制〔第三人称单数〕；扑哧声〔复数〕',
 '湿鞋每走一步都扑哧响，可以说 it squelches；一个人总把别人的新点子压下去，动词也这样用。',
 'squelch + -es，/tʃ/ 后读 /ɪz/，多一个音节。词义按湿泥、声音或抽象压制等对象分别理解。',SQUELCH+[['squelch + -es → squelches','它扑哧响或压制；多次扑哧声']],
 'squelches through the mud 扑哧走过泥地；squelches new ideas 压下新点子。',
 'water squelches in his shoes；a series of squelches。',
 'squelches an idea 常带压制的强劲感，discusses an idea 是拿来讨论；把它压下去不等于认真驳倒了它。',
 ('Water squelches in his shoes with every step.','他每走一步，鞋里的水就扑哧响。'),('The manager squelches every suggestion before anyone can discuss it.','还没等大家讨论，经理就把每个建议都压了下去。'),sources=S('squelches','squelch'))
W('squelched','/skweltʃt/','踩着湿泥扑哧走了；压制、打消了',
 '走完一段泥地，鞋子一路扑哧作响，或一句冷话让兴奋一下闷住，都可以用 squelched。',
 'squelch + 完整 -ed，/tʃ/ 后读 /t/；过去式、过去分词，不另加一个音节。',SQUELCH+[['squelch + -ed → squelched','过去带扑哧声行走，或把某事压下去']],
 'squelched through the field 扑哧走过田地；squelched our excitement 打消我们的兴奋。',
 'squelched the rumours；squelched along the path。',
 'squelched our excitement 写热情被压下去，disappointed us 写让人失望；可以相关，但前者更像把兴头闷住。',
 ('We squelched across the muddy field.','我们踩着泥，扑哧扑哧地走过田地。'),('His dismissive comment squelched our excitement.','他那句轻蔑的话打消了我们的兴奋。'),sources=S('squelched','squelch'))
W('squelching','/ˈskweltʃɪŋ/','正在湿软物中扑哧行走；正在压制；扑哧声',
 '草地泡透了，脚下每一步都软软挤出水声，叫 squelching；动词也能写正在压住反对、热情等。',
 'squelch + -ing；可表示动作过程，也可把持续的踩压声作为名词谈。',SQUELCH+[['squelch + -ing → squelching','湿软踩压、发声或压制的过程']],
 'a squelching noise 扑哧声；squelching through wet grass 踩着湿草扑哧走。',
 'squelching dissent 压制异议；squelching footsteps 扑哧脚步声。',
 'squelching 常突出湿软挤压的声感，crunching 常像踩碎硬脆物的咯吱声；脚步声让人联想到的地面不同。',
 ('A squelching noise came from his soaked boots.','他湿透的靴子里传出扑哧声。'),('We heard someone squelching through the wet grass.','我们听见有人踩着湿草扑哧扑哧地走来。'),sources=S('squelching','squelch'))
W('squish','/skwɪʃ/','挤压、压扁软物；软物受压的声响',
 '把熟香蕉按扁，或手指捏进软泥里，软软地变形，叫 squish。它不像砸玻璃那样突出硬脆碎裂。',
 '很可能是 squash 动词的变体，也可能受旧 squiss 挤、压影响；确切形成不宜说成几个现代英语短词硬拼。',SQUISH,
 'squish a banana 把香蕉按扁；squish together 挤到一起。',
 'squish underfoot 在脚下被压扁；a wet squish 湿软挤压声。',
 'squish 常带软物挤变形的感觉，smash 更容易是猛击、打碎；力量、材料不同会改变选词。',
 ('Do not squish the berries at the bottom of the bag.','别把袋子底下的浆果压坏。'),('The mud made a wet squish under my boot.','泥在我的靴子底下发出湿软的扑哧声。'),sources=S('squish','squish'))
W('squishes','/ˈskwɪʃɪz/','挤压、软软变形〔第三人称单数〕；软物挤压声〔复数〕',
 '软球被手一捏就变形，可以说 it squishes；一脚脚踩软物发出的声音，也可数成 squishes。',
 'squish + -es，/ʃ/ 后读 /ɪz/；多一个音节，动词三单与声音名词复数同形。',SQUISH+[['squish + -es → squishes','它挤压、软软变形；多次软物挤压声']],
 'squishes easily 容易捏扁；squishes between the fingers 在指间被挤压。',
 'a series of squishes；squishes the clay 挤压黏土。',
 'squishes easily 说受挤会变形，breaks easily 说容易破裂；软玩具可变形而没有坏掉。',
 ('The soft ball squishes easily in your hand.','这个软球在手里很容易捏变形。'),('The child squishes the clay between her fingers.','孩子用手指挤压黏土。'),sources=S('squishes','squish'))
W('squished','/skwɪʃt/','挤扁、压软变形了；被挤在狭小位置',
 '挤上后座，几个人肩贴肩，身体缩在一起，也可说 squished。它不要求人真被压坏，只是挤得空间很小。',
 'squish + 完整 -ed，/ʃ/ 后读 /t/；既说过去挤压动作，也可作分词描述挤扁、挤在一起的结果。',SQUISH+[['squish + -ed → squished','过去挤压了，或处于被挤扁、挤拢的状态']],
 'squished berries 压坏的浆果；squished together 挤在一起。',
 'squished into the back seat 挤进后座；squished under the box。',
 'squished together 可以口语形容人挤在一起，crushed 在相同场景下可能暗示更重的挤压、伤害；按实际意思选。',
 ('The strawberries were squished under the milk carton.','草莓被牛奶盒压坏了。'),('We were squished together in the back seat.','我们在后座挤成一团。'),sources=S('squished','squish'))
W('squishing','/ˈskwɪʃɪŋ/','正在挤压、压软变形；湿软挤压声',
 '一双手反复捏软泥，让它从指缝挤出来，是 squishing。重点是柔软材料受力变化的触感。',
 'squish + -ing；现代动作形式，也可用来描述持续的湿软挤压声音。',SQUISH+[['squish + -ing → squishing','软物受挤、变形或发声的过程']],
 'squishing clay 挤压黏土；squishing through mud 踩着湿泥走。',
 'a squishing sound 湿软挤压声；squishing the cushion。',
 'squishing 与 squeezing 可以重叠，前者更有软物压变形的触感、声感；squeezing 的用途更广。',
 ('The children were squishing soft clay into different shapes.','孩子们正把软黏土捏成不同形状。'),('I could hear a squishing sound inside my wet shoes.','我能听见湿鞋里传来扑哧声。'),sources=S('squishing','squish'))
W('squishy','/ˈskwɪʃi/','软软的、容易捏变形的；湿软的',
 '手一压就凹进去，松手又慢慢鼓回来，像软玩具、熟果肉那样，就是 squishy。它写的是触感，未必真有水。',
 'squish + -y；较早已有软、湿的性质义，现代也用于不湿却柔软可挤的物体。',SQUISH+[['squish + -y → squishy','软、易受挤变形的性质']],
 'a squishy toy 软捏玩具；squishy ground 湿软地面。',
 'squishy cushions 软软的垫子；soft and squishy。',
 'squishy 比 soft 更容易让人想到按下去会变形；soft music 是柔和音乐，不能照搬成 squishy music。',
 ('The children loved the squishy toy.','孩子们很喜欢那个软捏玩具。'),('The ground was squishy after the rain.','下雨后，地面湿软。'),sources=S('squishy','squish'))
W('scrunch','/skrʌntʃ/','揉皱、挤成一团；缩拢身体；咯吱压碎',
 '废纸往掌心一揉，变成皱巴巴一团，是 scrunch up。阳光太刺眼，脸也可以像纸一样缩皱起来。',
 '通常分析为 crunch 的增强声感形式，最终可能带拟声来源；较早咬碎，后来写揉挤、缩成紧凑形状。scr- 不能当成随便添到所有词前的生产性前缀。',CRUNCH,
 'scrunch up paper 把纸揉皱成团；scrunch up your face 把脸皱起来。',
 'scrunch your toes 蜷起脚趾；scrunch down 缩低身子。',
 'scrunch 强调揉皱、缩拢成紧凑形状，fold 常是沿折痕整齐折叠；纸张最后的样子不同。',
 ('Scrunch the paper into a ball before throwing it away.','把纸揉成一团再扔掉。'),('Try not to scrunch up your face for the photo.','拍照时尽量别把脸皱成一团。'),sources=S('scrunch','scrunch'))
W('scrunches','/ˈskrʌntʃɪz/','揉皱、缩拢、咯吱压碎〔第三人称单数〕',
 '有人写错一个字就把纸揉掉，有人怕光时鼻子、脸一齐皱起，主语是他、她时都能用 scrunches。',
 'scrunch + -es，/tʃ/ 后读 /ɪz/，多一个音节；相关声音名词的复数也可同形，日常常见还是动词。',CRUNCH+[['scrunch + -es → scrunches','他或它把东西揉拢、皱起']],
 'scrunches up her nose 皱起鼻子；scrunches the paper 把纸揉皱。',
 'scrunches into a small space 缩进狭小空间；scrunches up his shoulders。',
 'scrunches up her nose 常写鼻子连脸部一起皱缩，sniffs 则是吸鼻子、嗅；动作不是同一回事。',
 ('She scrunches up her nose when she dislikes a smell.','她不喜欢某种气味时就皱起鼻子。'),('He scrunches each failed sketch into a ball.','他把每张画坏的草图都揉成一团。'),sources=S('scrunches','scrunch'))
W('scrunched','/skrʌntʃt/','揉皱、缩拢了；被挤成一团的',
 '便条被揉得皱巴巴，膝盖蜷着挤在小椅子里，都可以用 scrunched。它把东西或身体的形状往里收紧。',
 'scrunch + 完整 -ed，/tʃ/ 后读 /t/；不另加音节。分词可描述揉挤后的形态。',CRUNCH+[['scrunch + -ed → scrunched','过去揉皱、缩拢，或呈挤拢状态']],
 'scrunched up the note 把便条揉皱；scrunched into a corner 蜷缩在角落。',
 'scrunched shoulders 缩起的肩；scrunched paper。',
 'scrunched up 常是挤皱、蜷拢，stretched out 是伸展开；同一身体从紧凑到舒展，动作方向相反。',
 ('She scrunched up the note and put it in her pocket.','她把便条揉皱，塞进口袋。'),('We sat scrunched together on the tiny bench.','我们挤在那张小长凳上坐着。'),sources=S('scrunched','scrunch'))
W('scrunching','/ˈskrʌntʃɪŋ/','正在揉皱、缩拢；咯吱作响的压踩',
 '拿纸在手里反复揉、把脚趾蜷紧，scrunching 写这个过程；踩碎石时也可突出咯吱声。',
 'scrunch + -ing；延续揉压、缩拢、咯吱声等动作分支，不能只给所有场景套一个揉纸义。',CRUNCH+[['scrunch + -ing → scrunching','揉拢、缩拢或带咯吱声压踩的过程']],
 'scrunching up paper 揉皱纸张；scrunching your toes 蜷紧脚趾。',
 'scrunching across gravel 踩着碎石咯吱走过；a scrunching sound。',
 'scrunching paper 不要求把纸撕破，tearing paper 则写撕裂；揉皱和断开不能混在一起。',
 ('Stop scrunching the paper while I am reading.','我看书时，别一直揉纸。'),('He was scrunching his toes inside his shoes.','他在鞋里蜷着脚趾。'),sources=S('scrunching','scrunch'))
W('crunches','/ˈkrʌntʃɪz/','咯吱咬碎、压碎〔第三人称单数〕；卷腹〔复数〕',
 '咬硬脆食物时咯吱响，是 crunches；健身时一组收腹抬起上身的动作，也可叫 crunches，是后来固定的运动用法。',
 'crunch + -es，/tʃ/ 后读 /ɪz/；动词三单、名词复数同形。crunch 可能经旧 craunch 拟声形成，卷腹要按固定名词义学。',CRUNCH+[['crunch + -es → crunches','它咯吱咬、压；多个卷腹动作等']],
 'do crunches 做卷腹；crunches an apple 咯吱咬苹果。',
 'a set of crunches 一组卷腹；crunches underfoot 在脚下咯吱响。',
 'crunches 卷腹通常只抬起上背一部分，sit-ups 仰卧起坐常把躯干抬得更高；两种运动名称不宜一概混译。',
 ('The dog crunches its biscuits noisily.','狗咯吱咯吱地大声嚼着饼干。'),('She finished the workout with a set of crunches.','她做了一组卷腹，结束训练。'),sources=S('crunches','crunch'))
W('crunched','/krʌntʃt/','咯吱咬碎、踩压了；处理了数字数据',
 '咬脆苹果、踩碎石，都能听到咯吱感，用 crunched；crunched the numbers 则把一堆数字“嚼开处理”，是计算数据的固定说法。',
 'crunch + 完整 -ed，/tʃ/ 后读 /t/。处理数字的比喻用法单独记搭配，不表示数字真的碎了。',CRUNCH+[['crunch + -ed → crunched','过去咯吱压咬；也可写进行了大量计算']],
 'crunched on an apple 咯吱咬苹果；crunched the numbers 计算、分析数字。',
 'boots crunched on gravel 靴子踩碎石咯吱响；crunched through data 处理数据。',
 'crunched the numbers 着重做计算分析，不必意味着数字被减少；cut the numbers 的意思要看具体上下文。',
 ('Our boots crunched on the frozen snow.','我们的靴子踩在冻雪上，咯吱作响。'),('We crunched the numbers before choosing a supplier.','我们先算了各项数字，再选供应商。'),sources=S('crunched','crunch'))
W('crunching','/ˈkrʌntʃɪŋ/','正在咯吱咬碎、踩压；数字处理',
 '脚下踩着枯叶，一步一声咯吱，是 crunching；人忙着算预算，也可说 crunching the numbers。',
 'crunch + -ing；动作过程可以是物理咬压、发声，也可以是已固定的计算数据用法。',CRUNCH+[['crunch + -ing → crunching','咬压、踩压、发声或计算的过程']],
 'crunching leaves 咯吱踩叶；crunching the numbers 计算数据。',
 'a crunching sound 咯吱声；crunching through the snow。',
 'crunching 突出硬脆压碎声，chewing 只说嚼；嚼软面包不一定有 crunching 那种声音。',
 ('We heard footsteps crunching through the dry leaves.','我们听见脚步踩过枯叶的咯吱声。'),('She spent the afternoon crunching the numbers for the budget.','她花了一下午计算预算数字。'),sources=S('crunching','crunch'))
W('crushes','/ˈkrʌʃɪz/','压碎、压倒〔第三人称单数〕；迷恋、暗恋对象〔复数〕',
 '机器把石头压碎，是 it crushes；青春期偷偷喜欢过的几个人，也可以叫 crushes。词义已分支，不能把暗恋硬讲成真的把人压扁。',
 'crush + -es，/ʃ/ 后读 /ɪz/；动词三单与名词复数同形。名词迷恋对象、迷恋感是较晚的英语用法，不能单凭压碎画面确立具体历史比喻步骤。',CRUSH+[['crush + -es → crushes','它压碎、压倒；多次迷恋或多个迷恋对象']],
 'crushes rocks 压碎石头；school crushes 学生时代的暗恋对象。',
 'crushes the opposition 压倒对手；have crushes on people 迷恋别人。',
 'crushes 作暗恋相关名词时，未必有确定恋爱关系；partners 则指伴侣、搭档等已建立的相应关系。',
 ('The machine crushes rocks into small pieces.','机器把石头压成小块。'),('We laughed about our old school crushes.','我们说起学生时代的暗恋对象，笑了起来。'),sources=S('crushes','crush'))
W('crushing','/ˈkrʌʃɪŋ/','正在压碎、挤压；压倒性的；沉重打击的',
 '一块重物压下去，东西撑不住；一次失败让人觉得被压得抬不起头，也可以用 crushing。它说打击、优势的强度很重。',
 'crush + -ing，动作形式也形成性质形容词。早期 crush 已有抽象压倒义，现代不能把每种心理用法都说成最近才从机器压碎借来。',CRUSH+[['crush + -ing → crushing','正在压碎，或足以压倒、打垮的性质']],
 'a crushing defeat 惨败；a crushing blow 沉重打击；crushing pressure 巨大压力。',
 'crushing disappointment 极大的失望；crushing garlic 捣碎蒜。',
 'a crushing defeat 是自己惨败，a crushing victory 是己方压倒性获胜；crushing 的强度相近，成败方向由名词决定。',
 ('The team suffered a crushing defeat in the final.','球队在决赛中惨败。'),('Losing the contract was a crushing blow to the business.','失去合同对这家公司是沉重打击。'),sources=S('crushing','crush'))
W('crushingly','/ˈkrʌʃɪŋli/','令人受重挫地；极其、压倒性地',
 '一句话让人像被重物压住，信心一下垮下去，可以说 crushingly blunt；也能加强某些负面评价，如 crushingly dull 无聊得让人难受。',
 'crushing 形容词 + -ly，写造成强烈压倒、挫败感的程度或方式。不是过去分词 crushed 加 -ly。',CRUSH+[['crushing + -ly → crushingly','像被压倒般令人受挫地，或程度极强地']],
 'crushingly disappointing 令人极度失望的；crushingly blunt 直白得令人受打击的。',
 'crushingly dull 无聊透顶的；crushingly obvious 明摆着、毫无悬念的。',
 'crushingly 常有令人受挫、受压的强评价，very 更中性；不宜把它无差别加到所有积极形容词前。',
 ('The result was crushingly disappointing after months of work.','忙了几个月后，这个结果令人极度失望。'),('Her reply was crushingly blunt.','她的回答直白得让人很受打击。'),sources=S('crushingly','crush'))
W('crumbly','/ˈkrʌmbli/','易碎成屑的、松散掉渣的',
 '饼干一掰就掉渣，奶酪轻轻一碰散成小块，都是 crumbly。它说的是容易散开，未必是在夸香脆。',
 'crumble 去不发音 e 加 -y；crumble 本身接 crumb 碎屑及较早反复动作材料。现代形容词这层写易散碎的性质。',
 [['crumb 碎屑等材料 → crumble','散碎、弄成屑，含较早反复动作构词'],['crumble + -y → crumbly','容易散成小碎屑、小块']],
 'crumbly cheese 易碎散的奶酪；a crumbly biscuit 松酥掉渣的饼干。',
 'crumbly soil 松散易碎的土；a crumbly texture 松散掉渣的质地。',
 'crumbly 着重容易散碎，crunchy 着重咬下去清脆、咯吱；一块饼干可以又 crunchy 又 crumbly。',
 ('The cheese was dry and crumbly.','这块奶酪干干的，容易碎散。'),('The crumbly biscuit fell apart in my hand.','那块容易掉渣的饼干在我手里散开了。'),sources=S('crumbly','crumble'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zha',ROOTS,WORDS)
 extend_lessons()
