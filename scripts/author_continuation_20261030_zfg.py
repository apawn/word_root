"""Pouring, thin flows, scattered particles, moisture and old boiling words."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3632':dict(words=['drain','drains','drained','draining'],label='drain 从排液到耗尽精力',note='draining 可写水正排出，也可形容事情耗神；不按现代 d + rain 雨来拆。'),
 'B4059':dict(words=['leak','leaks','leaked','leaking'],label='leak 的漏液与信息泄露',note='leaking 接整个漏的动词，实体水流与消息外泄分别给例；不是所有信息泄露都像水滴那样一点一点。'),
 'B3213':dict(words=['damp','dampen','dampens','dampened','dampening'],label='dampen 的削弱与弄湿：历史先后另看记录',note='dampen 的削弱、压低记录早于弄湿，不把现代湿布压火的助记画面当作唯一演化过程。'),
 'A1783':dict(words=['damp','dampen','dampens','dampened','dampening'],label='damp 加使动 -en，再接现代词尾',note='damp + -en → dampen；dampened、dampening 的 -ed、-ing 加在完整动词后，不漏掉使动层。'),
 'A1697':dict(words=['sprinkle','sprinkler','sprinklers','spray','sprayer','sprayers'],label='sprinkler、sprayer 的工具 -er',note='sprinkle 去 e 后加完整 -er 成 sprinkler；spray 保留 y 后加 -er 成 sprayer，再加复数 -s，不把 sprinkler 拆成只加了 -r。'),
 'A2238':dict(words=['sprinkle','sprinkles','sprinkled','sprinkling','drizzle','drizzles','drizzled','drizzling'],label='sprinkle、drizzle 的旧小量反复动作材料',note='sprinkle 联系 sprenge、荷兰语撒散材料，有不同早期分析；drizzle 也有联系旧降落词反复形式的分析，均保留不确定部分。'),
 'A1760':dict(words='trickle trickles trickled trickling pour pours poured pouring sprinkle sprinkles sprinkled sprinkling drizzle drizzles drizzled drizzling seep seeps seeped seeping leak leaking spout spouts spouted spouting drain draining dampen dampens dampened dampening seethe seethes seethed seething sodden'.split(),label='细流、降雨、渗漏与沸腾动词及分词',note='seethed 是现代规则 -ed 形式，sodden 则保留旧强变化分词的历史并发展成湿透形容词，不能分析为现代 sod 加使动 -en。'),
}
TRICKLE=[['中古英语 triklen → trickle','细流、滴流；或联系 stricklen 与旧 striken 移动材料，来源未定'],['细小流动 → 人、消息、钱少量陆续到来','一个个、慢慢来，不是一次涌入很多']]
W('trickles','/ˈtrɪkəlz/','细细流、陆续少量到来〔第三人称单数〕；一股股细流',
 '水沿石头细细往下走，或消息、人一点点到来，用 trickles。抓住量不大、慢慢连续或断续推进。',
 'trickle + -s，保留 e，/l/ 后读 /z/；更早来源未定，不能把 trick 把戏当现代基础。',TRICKLE+[['trickle + -s → trickles','它细流；少量陆续到来；多股细流']],
 'water trickles down 是水细细流下，information trickles in 是消息一点点传来；不必每次真有水。',
 'trickles through the gap 从缝里细流；small trickles of water 几股小细流。',
 'trickles in 与 pours in 都可写人或消息，前者少而慢，后者通常多而集中涌入。',
 ('Water trickles down the rock face.','水沿岩壁细细流下。'),('News of the event trickles in throughout the morning.','整个上午，活动消息一点点传来。'),sources=S('trickles','trickle'))
W('trickled','/ˈtrɪkəld/','细细流下了；一点点陆续到来了',
 '刚才有细水慢慢流下，或人没有一齐到、而是零星走进来，用 trickled。',
 'trickle 去 e + 完整 -ed，/l/ 后读 /d/；基础词已有 ck 保留，不再多添 k。',TRICKLE+[['trickle 去 e + -ed → trickled','过去细流、少量陆续来到']],
 'trickled down her face 是沿她脸细细流下，trickled into the room 是零星走进房间；方向词保留流动路线。',
 'trickled through the stones 从石缝细流；trickled in slowly 慢慢陆续来。',
 'trickled 可以写人，有一点点汇进来的画面；walked in 只说走进，不说明人数、节奏。',
 ('A tear trickled down her cheek.','一滴泪沿她脸颊缓缓流下。'),('Guests trickled into the room after seven.','七点后，客人零星走进房间。'),sources=S('trickled','trickle'))
W('trickling','/ˈtrɪklɪŋ/','正在细流、陆续少量到来；细细流动的',
 '少量水正沿着表面往下走，或信息正一点点传来，是 trickling。比起猛烈涌出，动作轻、慢、小。',
 'trickle 去 e + 完整 -ing，常读 /ˈtrɪklɪŋ/；可表示进行，也可形容细流的状态。',TRICKLE+[['trickle 去 e + -ing → trickling','细流过程；零星陆续到来']],
 'a trickling stream 是细细流的小溪，details trickling in 是细节正一点点传来；动作节奏是同一画面。',
 'water trickling over stones 水流过石头；people trickling out 人们零星离开。',
 'trickling 常是缓缓的流线，dripping 常是分开一滴滴落；看水有没有形成细流，有助于选词。',
 ('We listened to water trickling over the stones.','我们听着水细细流过石头。'),('People were trickling out of the hall.','人们正零星走出大厅。'),sources=S('trickling','trickle'))
POUR=[['中古英语 pour 的相关形式 → pour','来源未定；联系法语方言 purer 的分析只是一种可能'],['倒成一股 → 大雨、人大量到来、感情倾诉','实际动作的流量感，扩成事情一股脑涌来']]
W('pours','英 /pɔːz/；美 /pɔːrz/','倒出、涌出、倾诉〔第三人称单数〕；下大雨',
 '把壶一倾，水成一股往外流，用 pours；雨大得像从天上倒，也说 it pours。人、消息大量涌来还能借这个画面。',
 'pour + -s，读 /z/；基础词中古英语已有，确切来源未定，不把某条法语、拉丁候选路线说成定论。',POUR+[['pour + -s → pours','他、她倒；它涌出；雨倾盆而下']],
 'pours tea 是倒茶，pours into the hall 是涌进大厅，pours out her feelings 是把感情一股脑说出来。',
 'it pours 雨下得很大；pours money into a project 大量投入资金。',
 'pours 强调成股、量多或连续涌来的感觉；drizzles 常是细小雨滴或往菜上轻细淋一点液体。',
 ('She pours tea into the small cups.','她往小杯里倒茶。'),('Whenever we plan a picnic, it pours.','我们一计划野餐，雨就下得特别大。'),sources=S('pours','pour'))
W('poured','英 /pɔːd/；美 /pɔːrd/','倒出了、涌入了、倾诉了；下了大雨',
 '水刚才成一股倒出来，或人、信件一大批涌进来，用 poured。说心事也能像倒水一样一下放出来。',
 'pour + 完整 -ed，读 /d/；英式基础词最后虽不读 r，仍由最后的元音接 /d/。',POUR+[['pour + -ed → poured','过去倾倒、涌流或倾诉']],
 'poured a drink 是倒了一杯饮料，poured into the street 是大量涌到街上；poured out her worries 是倾诉忧虑。',
 'poured with rain 下着大雨；poured into the cup 倒进杯子。',
 'poured 不一定全是液体：人群涌来、资源投入、感情倾诉都借成股而出的动作，不要逐字翻成倒人。',
 ('He poured water into the jug.','他把水倒进水壶。'),('People poured into the square after the concert.','音乐会后，人群大量涌进广场。'),sources=S('poured','pour'))
W('pouring','英 /ˈpɔːrɪŋ/；美 /ˈpɔːrɪŋ/','正在倾倒、涌来、倾诉；大雨倾盆的',
 '水正成股流、雨正密密大大地落，或消息正一大批传来，是 pouring。力度、数量感比零星滴流强。',
 'pour + 完整 -ing；英式后接元音时 r 发出来。可作进行分词，也可形容雨势大。',POUR+[['pour + -ing → pouring','倾倒、涌流过程；倾盆雨状态']],
 'pouring rain 是倾盆大雨，pouring tea 是正在倒茶，messages pouring in 是消息大量涌来。',
 'pouring down 雨倾盆而下；pouring out his heart 倾诉心事。',
 'pouring rain 与 drizzle 的画面相反：前者雨大像倒，后者雨细；并非所有 raining 都等于 pouring。',
 ('We walked home in the pouring rain.','我们冒着倾盆大雨走回家。'),('Messages were pouring in after the announcement.','消息公布后，留言大量涌来。'),sources=S('pouring','pour'))
SPRINKLE=[['中古英语 sprenklen 等 → sprinkle','联系 sprenge 及荷兰语等撒散材料，早期借入、反复动作分析有不同解释'],['撒细粒、洒水滴 → 零星小雨、点缀','名词可说撒下的一点东西，sprinkles 又常指蛋糕彩糖粒']]
W('sprinkles','/ˈsprɪŋkəlz/','撒、洒、零星降雨〔第三人称单数〕；彩糖粒、零星洒落物〔复数〕',
 '盐、水、糖粒不是一股倒下，而是分散地落在表面，用 sprinkles。蛋糕上彩色小糖针、糖粒也常直接叫 sprinkles。',
 'sprinkle + -s，保留 e，/l/ 后读 /z/；动词三单、名词复数同形，基础包含旧的撒散、反复动作材料。',SPRINKLE+[['sprinkle + -s → sprinkles','他、她撒洒；彩糖粒等撒落物']],
 'sprinkles salt over the soup 是往汤上撒盐，chocolate sprinkles 是巧克力糖粒；名词常直接是可吃的装饰。',
 'sprinkles of rain 零星雨点；colourful sprinkles 彩糖粒。',
 'sprinkles 可撒干颗粒，也可洒水滴；sprays 更常是把液体喷成细滴，别只因为都分散就混用。',
 ('She sprinkles a little salt over the tomatoes.','她往番茄上撒一点盐。'),('The children decorated the cupcakes with sprinkles.','孩子们用彩糖粒装饰纸杯蛋糕。'),sources=S('sprinkles','sprinkle'))
W('sprinkled','/ˈsprɪŋkəld/','撒了、洒了；点缀了、零星分布的',
 '小颗粒、液滴刚才分散落到表面，叫 sprinkled；故事里点几个笑话，也能像撒调料一样 sprinkled。',
 'sprinkle 去 e + 完整 -ed，/l/ 后读 /d/；保留基础词 nk 的 /ŋk/，不多读 /ɪd/。',SPRINKLE+[['sprinkle 去 e + -ed → sprinkled','过去撒洒；少量分散点缀']],
 'sprinkled cheese over the pasta 是往意面撒奶酪，sprinkled with flowers 是零星点缀着花；with、over 提示东西和表面。',
 'sprinkled sugar on top 在上面撒糖；sprinkled jokes into the speech 在演讲中穿插笑话。',
 'sprinkled 常是一点点、分散地加，covered 可以整片覆盖；a speech sprinkled with jokes 不是整场只有笑话。',
 ('He sprinkled grated cheese over the pasta.','他往意面上撒了奶酪碎。'),('Her talk was sprinkled with gentle jokes.','她的讲话里穿插着几个温和的笑话。'),sources=S('sprinkled','sprinkle'))
W('sprinkling','/ˈsprɪŋklɪŋ/','正在撒、洒；少量撒落物；零星、少许',
 '细粒正分散洒下，是 sprinkling；a sprinkling of something 又把少量、零星分布的一点东西提出来。',
 'sprinkle 去 e + 完整 -ing，常读 /ˈsprɪŋklɪŋ/；活动名词后来也可说少量分布，不全是正在做。',SPRINKLE+[['sprinkle 去 e + -ing → sprinkling','撒洒过程；少量分散的东西或人']],
 'a sprinkling of sugar 是撒上一点糖，a sprinkling of visitors 是零星几个游客；不要求每个对象真被撒下来。',
 'a light sprinkling of rain 零星小雨；sprinkling herbs over the dish 往菜上撒香草。',
 'a sprinkling of people 强调人数少、散布着；a crowd of people 是一群人，数量、聚集感不同。',
 ('Add a light sprinkling of sugar before serving.','上桌前轻轻撒一点糖。'),('Only a sprinkling of visitors remained in the gallery.','画廊里只剩零星几个游客。'),sources=S('sprinkling','sprinkle'))
DRIZZLE=[['十六世纪 drizzle → 小滴洒落、细雨','来源未定；或改自较早 drysning，或联系 dresen 等降落材料的反复形式'],['雨细细落 → 少量液体轻淋在食物上','不必从天空下雨才造出所有主动洒落义，早期也有及物用法']]
W('drizzle','/ˈdrɪzəl/','毛毛雨、细雨；下细雨；轻细淋洒少量液体',
 '细得像雾、轻轻落的雨，是 drizzle；做菜时把一点油、蜂蜜细细淋上去，也用 drizzle。',
 '具体来源未定，或联系较早 drysning、dresen 等降落材料；旧反复动作分析是一种解释，不是现代 drizzle 可随意拆成 drip + 某段字母。',DRIZZLE,
 'a light drizzle 是毛毛雨，drizzle oil over the salad 是往沙拉上细细淋油；主语、宾语一看就能分天气和做菜。',
 'fine drizzle 细密小雨；a drizzle of honey 细淋的一点蜂蜜。',
 'drizzle 的雨比 pouring rain 细、小；做菜里 drizzle 也比 pour 常更少、更轻细，不是整壶倒下。',
 ('A light drizzle began as we left the house.','我们出门时，下起毛毛雨。'),('Drizzle a little olive oil over the salad.','往沙拉上细细淋一点橄榄油。'),sources=S('drizzle','drizzle'))
W('drizzles','/ˈdrɪzəlz/','下毛毛雨；轻细淋洒〔第三人称单数〕；少量淋洒物〔复数〕',
 '天气细细飘小雨，或一个人轻轻把少量液体淋上菜，用 drizzles。它不带大股、猛冲的感觉。',
 'drizzle + -s，保留 e，/l/ 后读 /z/；词内 zz 属基础词，不使结尾读成 /ɪz/。',DRIZZLE+[['drizzle + -s → drizzles','天下细雨；他、她轻细淋洒']],
 'it drizzles 是下毛毛雨，she drizzles honey 是她细细淋蜂蜜；主语、宾语让两类场景分清。',
 'drizzles all morning 整个上午下细雨；drizzles oil over vegetables 给蔬菜细淋油。',
 'drizzles 的 -s 接在 /l/ 后读 /z/，gushes 的 -es 接在 /ʃ/ 后读 /ɪz/；看基础最后的音。',
 ('It often drizzles here in the early morning.','这里清晨常下毛毛雨。'),('She drizzles honey over her yoghurt.','她往酸奶上细细淋蜂蜜。'),sources=S('drizzles','drizzle'))
W('drizzled','/ˈdrɪzəld/','下过细雨了；轻细淋洒了；淋有少量液体的',
 '刚才细雨慢慢飘，或把一点油、酱、蜂蜜细细淋上去，叫 drizzled。既能写天气，也能写做菜。',
 'drizzle 去 e + 完整 -ed，/l/ 后读 /d/；已有 zz 留在基础词里，尾音不是 /ɪd/。',DRIZZLE+[['drizzle 去 e + -ed → drizzled','过去下细雨、轻细淋洒']],
 'drizzled all afternoon 是下午一直下细雨，drizzled with honey 是淋着一点蜂蜜；后者能修饰食物。',
 'drizzled oil onto the bread 往面包细淋油；chocolate-drizzled cake 淋着巧克力的蛋糕。',
 'drizzled with oil 常是一点点淋在表面，soaked in oil 则是浸在油里或油浸得很透；量、接触方式不同。',
 ('It drizzled throughout the afternoon.','整个下午都在下毛毛雨。'),('He drizzled a little oil over the warm bread.','他往温热面包上细细淋了一点油。'),sources=S('drizzled','drizzle'))
W('drizzling','/ˈdrɪzlɪŋ/','正在下毛毛雨、轻细淋洒；细雨',
 '雨细细密密地飘，或一点液体正轻细淋到表面，叫 drizzling。动作不猛烈，分量、雨滴通常都小。',
 'drizzle 去 e + 完整 -ing，常读 /ˈdrɪzlɪŋ/；已有 zz 保留，不再添 z。',DRIZZLE+[['drizzle 去 e + -ing → drizzling','下细雨或轻细淋洒的过程']],
 'it is drizzling 是正在下毛毛雨，drizzling chocolate over a cake 是往蛋糕上细淋巧克力；两义都很日常。',
 'drizzling outside 外面飘细雨；drizzling oil over the dish 给菜淋少量油。',
 'drizzling 是细雨，spraying 通常是把液体分成喷滴；看到水滴小，也要分天气降落还是主动喷洒。',
 ('It was still drizzling when we reached the station.','我们到车站时，还在飘毛毛雨。'),('She was drizzling chocolate over the cake.','她正往蛋糕上细细淋巧克力。'),sources=S('drizzling','drizzle'))
SEEP=[['较早 sipe 一系 → 近代 seep 变体','更早或联系古英语 sipian；具体延续路线保留可能性'],['孔隙慢慢渗透 → 感觉、影响、消息逐渐进入','不一定有明显大洞，也不一定真有液体']]
W('seeps','/siːps/','慢慢渗入、渗出〔第三人称单数〕；渗出液、渗漏处〔复数〕',
 '水慢慢穿过土、布、墙的小孔隙，用 seeps；寒意、影响一点点进入，也能借这种不知不觉渗透感。',
 'seep + -s，/p/ 后读 /s/；基础接较早 sipe 变体，更早上接古英语 sipian 是可能分析，不从 sea 海加 p。',SEEP+[['seep + -s → seeps','它慢慢渗入、渗出；名词也可数渗漏处']],
 'seeps through the wall 是穿墙渗出，seeps into the ground 是渗进地里；through、into 等说明方向。',
 'seeps in 慢慢渗入；seeps from a crack 从裂缝渗出。',
 'seeps 常侧重通过细孔、缝隙慢慢走，gushes 更像大股冲出；是流量、路径和速度的综合画面。',
 ('Water seeps through the old stone wall.','水慢慢渗过旧石墙。'),('Cold air seeps in around the window frame.','冷空气沿窗框缝隙一点点渗进来。'),sources=S('seeps','seep'))
W('seeped','/siːpt/','慢慢渗入、渗出了；逐渐浸透、进入了',
 '水一点点穿过表面，或寒意、某种感受慢慢进入，用 seeped。动作通常不猛，像悄悄走进细缝。',
 'seep + 完整 -ed，/p/ 后读 /t/；ee 长元音保留，不双写 p。',SEEP+[['seep + -ed → seeped','过去缓慢渗透、进入']],
 'seeped into the carpet 是慢慢渗进地毯，seeped through the roof 是从屋顶渗下；比喻影响也可 seep into。',
 'seeped under the door 从门下渗入；seeped into the soil 渗入土中。',
 'seeped into 强调逐渐浸入，spilled onto 常强调一时洒到表面；同一杯水洒出后，还可能继续渗进去。',
 ('Rainwater seeped under the door.','雨水从门下慢慢渗进来。'),('The spilled tea seeped into the carpet.','洒出的茶慢慢渗进地毯。'),sources=S('seeped','seep'))
W('seeping','/ˈsiːpɪŋ/','正在缓慢渗入、渗出；逐渐浸透',
 '液体正悄悄穿孔隙、缝隙进入另一边，是 seeping；冷、恐惧、影响等也能借这种渐渐渗透的感觉。',
 'seep + 完整 -ing，直接加；ee 长元音后不双写 p，基础 /siːp/ 保留。',SEEP+[['seep + -ing → seeping','缓慢渗透的过程']],
 'water seeping through 是水正在渗过，cold seeping into the room 是寒意逐渐进入房间；路径比一条明显流线更重要。',
 'seeping from the wall 墙里渗出；seeping into the fabric 渗进布料。',
 'seeping 与 leaking 常接近，前者更突出缓慢穿透；leaking 更突出从原来该关住的地方漏进、漏出。',
 ('We found water seeping through a crack in the wall.','我们发现水正从墙缝慢慢渗出。'),('Cold air was seeping into the room.','冷空气正一点点渗进房间。'),sources=S('seeping','seep'))
W('leaking','/ˈliːkɪŋ/','正在漏入、漏出；正在泄露消息；漏的',
 '本该把东西关住的管道、屋顶、袋子留了出口，东西正在漏，就是 leaking；消息从保密范围跑出去，也用同一画面。',
 'leak + 完整 -ing；基础动词可能借中古荷兰语 leken 或古诺尔斯 leka，不能仅因音近就当 lake 湖的现代派生。',
 [['中古荷兰语 leken、或古诺尔斯 leka 等 → leak','让水进入、漏出；相关古英语材料并非确定直接延续'],['leak + -ing → leaking','实体泄漏；后来有秘密、消息外泄']],
 'a leaking roof 是漏雨屋顶，leaking information 是泄露信息；水可进入容器，也可从容器流出。',
 'leaking from a pipe 管子里漏出；a leaking bottle 漏液的瓶子。',
 'leaking 不是一定缓慢：流速由场景决定。seeping 更经常突出细孔、缝隙里的慢渗。',
 ('The pipe under the sink is leaking.','水槽下的管子正在漏水。'),('Someone had been leaking details of the plan to the press.','一直有人把计划细节泄露给媒体。'),sources=S('leaking','leak'))
SPOUT=[['中古英语 spouten → spout','日耳曼喷、吐材料，最终大概有拟声基础；与 sputter 等可比较'],['喷出 → 喷口、壶嘴等；口语滔滔说','器具名指液体经出的嘴、管；人像开了水龙头一样不停讲']]
W('spout','/spaʊt/','喷出、喷涌；壶嘴、出水口；滔滔不绝地说',
 '液体从一个口朝外喷，是 spout；壶伸出的一小段嘴也叫 a spout。人话像开了龙头般往外冒，也能用这个词。',
 '接中古英语 spouten 的喷、吐材料，与日耳曼相关词可比较；名词后来表示排水管、器皿出液口，不是现代 spurt 的规则变形。',SPOUT,
 'a teapot spout 是茶壶嘴，water spouts out 是水喷出；spout nonsense 是滔滔说些胡话，语气常带不赞成。',
 'a narrow spout 细壶嘴；spout off about politics 滔滔不绝谈政治。',
 'spout 既能说喷，也能说喷口；gush 更重液体大量冲出的动作，未必自带某个器具口。',
 ('The teapot has a long, curved spout.','茶壶有一根弯弯的长嘴。'),('Water began to spout from the fountain.','水开始从喷泉口喷出来。'),sources=S('spout','spout'))
W('spouts','/spaʊts/','喷出、滔滔说〔第三人称单数〕；壶嘴、出水口、喷流〔复数〕',
 '水从口朝外涌、一个人话说个不停，用 spouts；几只壶的嘴、几个喷口也可用名词复数。',
 'spout + -s，/t/ 后读 /s/；名词、动词同形变化，ou 的 /aʊ/ 保留。',SPOUT+[['spout + -s → spouts','它喷；他、她滔滔说；多个壶嘴、喷口']],
 'spouts water 是喷水，spouts nonsense 是滔滔说胡话；teapot spouts 是茶壶嘴，先按宾语或名词搭配分义。',
 'spouts from the rock 从岩石喷出；long spouts 长壶嘴。',
 'spouts about a subject 常带嫌人说太多、内容未必高明的感觉；explains 可以中性地说明，不带这层评价。',
 ('The fountain spouts water into the pool.','喷泉把水喷进池子。'),('The two teapots have unusually long spouts.','这两把茶壶的嘴特别长。'),sources=S('spouts','spout'))
W('spouted','/ˈspaʊtɪd/','喷出了、喷涌了；滔滔不绝说了',
 '水刚才从口、孔向外喷，叫 spouted；人把一大串观点、套话倒出来，也能用它，常有嫌话多的语气。',
 'spout + 完整 -ed，/t/ 后读 /ɪd/，多一个音节；基础词 ou 的 /aʊ/ 保留。',SPOUT+[['spout + -ed → spouted','过去喷出或滔滔说']],
 'spouted from the pipe 是管口喷出，spouted a stream of excuses 是滔滔说一串借口；比喻保留成股往外倒的感觉。',
 'spouted into the air 喷向空中；spouted nonsense 滔滔说胡话。',
 'spouted 在说话场景不只等于 talked：它常暗含说得多而不够有价值，态度比中性叙述强。',
 ('Water spouted from a hole in the pipe.','水从管子上的一个孔喷出。'),('He spouted a stream of excuses for being late.','他为迟到滔滔不绝找了一串借口。'),sources=S('spouted','spout'))
W('spouting','/ˈspaʊtɪŋ/','正在喷出、喷涌；滔滔不绝地说；喷流',
 '一股水正从口向外喷，或人正把一串话不停倒出来，叫 spouting。液体、话语共享向外不断喷的形象。',
 'spout + 完整 -ing，直接加；末尾 ou 表示双元音 /aʊ/，不双写 t。',SPOUT+[['spout + -ing → spouting','喷出过程；话语不停涌出']],
 'spouting water 是喷水，spouting opinions 是滔滔发表意见；spouting off 常更显说得多、让人嫌烦。',
 'spouting into the air 向空中喷；spouting nonsense 滔滔说胡话。',
 'spouting 是往外喷、倒话，sprouting 是植物萌芽；多一个 r，就换了基础词和动作。',
 ('The fountain was spouting water high into the air.','喷泉正把水高高喷向空中。'),('He kept spouting nonsense throughout the meeting.','整个会议他都在滔滔不绝说胡话。'),sources=S('spouting','spout'))
W('draining','/ˈdreɪnɪŋ/','正在排液、流走；耗尽资源的、令人精疲力尽的',
 '水正从出口一点点排走，是 draining；做一件事把人的精力一点点抽空，也可形容 emotionally draining。',
 'drain + 完整 -ing；基础承古英语 dreahnian，经中古英语 dreinen，与变干材料相关，不能拆成现代 d + rain。',
 [['古英语 dreahnian → 中古英语 dreinen → drain','把液体渐渐引走，使干'],['drain + -ing → draining','排液过程；资源、精力逐渐耗尽的比喻']],
 'draining the bath 是给浴缸排水，a draining day 是特别耗神的一天；draining away 是逐渐流失。',
 'emotionally draining 让人情绪、精神被耗空；water draining away 水正在排走。',
 'draining 形容事情耗人，drained 则可形容人已经累空；a draining meeting 之后，人可能 feel drained。',
 ('The water was draining slowly from the bath.','浴缸里的水正慢慢排走。'),('It had been an emotionally draining day.','那一天让人精神上格外疲惫。'),sources=S('draining','drain'))
SPRINKLER=[['sprinkle 的分散撒洒动作 → sprinkler','去末尾 e，再加执行者、工具后缀 -er'],['器具名词 → 现代洒水、消防喷淋器','把水分散洒到一片范围，具体用途由修饰词说明']]
W('sprinkler','英 /ˈsprɪŋklə/；美 /ˈsprɪŋklər/','洒水器；喷淋头、消防喷淋装置',
 '把水分散成小滴、洒到一片地面或室内空间的装置，叫 sprinkler。花园浇草坪、建筑消防都可能见到。',
 'sprinkle 去 e + 完整 -er → sprinkler；-er 在这里指做撒洒动作的器具，不是只加一个 -r。',SPRINKLER,
 'a lawn sprinkler 是草坪洒水器，a fire sprinkler 是消防喷淋头；都从分散洒水这一功能命名。',
 'turn on the sprinkler 打开洒水器；a sprinkler system 喷淋系统。',
 'sprinkler 常负责向一片范围分散洒水，sprayer 范围更广，可是手持喷壶、喷雾器等；用途能重合。',
 ('We put a sprinkler in the middle of the lawn.','我们在草坪中央放了一个洒水器。'),('The building has a fire sprinkler system.','这栋楼装有消防喷淋系统。'),sources=S('sprinkler','sprinkler'))
W('sprinklers','英 /ˈsprɪŋkləz/；美 /ˈsprɪŋklərz/','洒水器、喷淋头、消防喷淋装置〔复数〕',
 '草坪上有几台洒水器、天花板上有多个喷淋头，叫 sprinklers。是可数器具，和撒糖粒的 sprinkles 分开。',
 'sprinkle 去 e + 完整 -er → sprinkler，再加复数 -s，读 /z/；工具层和数量层都写出来。',SPRINKLER+[['sprinkler + -s → sprinklers','多个洒水、喷淋器具']],
 'garden sprinklers 是花园洒水器，ceiling sprinklers 是天花板喷淋头；工具叫什么，取决于它执行撒洒动作。',
 'automatic sprinklers 自动喷淋装置；turn off the sprinklers 关掉洒水器。',
 'sprinklers 是器具，sprinkles 可指蛋糕彩糖粒或撒洒三单；多出的 -er 对意思很关键。',
 ('The sprinklers turn on early in the morning.','洒水器清晨启动。'),('We could see several sprinklers in the ceiling.','我们看见天花板上有几个喷淋头。'),sources=S('sprinklers','sprinkler'))
W('sprayers','英 /ˈspreɪəz/；美 /ˈspreɪərz/','喷洒器、喷雾器；喷洒人员〔复数〕',
 '把液体喷成细滴的设备、喷壶有几个，叫 sprayers；有时也指执行喷洒工作的人，先看说设备还是人员。',
 'spray + 完整 -er → sprayer，保留 y，再加复数 -s，读 /z/；不要把 sprays、sprayers 混成同一层。',
 [['中古荷兰语 sprayen 等 → spray','分散喷洒液滴'],['spray + -er + -s → sprayers','多个喷洒器具、执行者']],
 'hand sprayers 是手持喷雾器，paint sprayers 是喷漆设备；-er 给出执行喷洒功能的东西，再用 -s 数多个。',
 'garden sprayers 园艺喷雾器；a row of sprayers 一排喷洒设备。',
 'sprayers 侧重设备或人员，sprays 常是液体喷雾、喷剂或动词；有无 -er 决定是不是执行者。',
 ('The gardeners carried small hand sprayers.','园丁们带着小型手持喷雾器。'),('The workshop uses paint sprayers for large panels.','作坊用喷漆设备处理大型板面。'),sources=S('sprayers','spray'))
DAMPEN=[['damp + 使动 -en → dampen','较早已有削弱、压低作用的用法'],['弄湿义后来也常用','现代可说微微弄湿，也可说压低热情；现代助记不等于记录先后']]
W('dampens','/ˈdæmpənz/','使微湿；减弱、打击热情〔第三人称单数〕',
 '把布稍微弄湿，或让原本很高的兴致低下来，都用 dampens。现代可用湿布压火帮助联想，但历史不是先湿后扫兴这一条线。',
 'damp + 使动 -en → dampen，再加三单 -s，/n/ 后读 /z/；保留完整的使动层。',DAMPEN+[['dampen + -s → dampens','它使微湿、减弱或扫兴']],
 'dampens the cloth 是把布弄微湿，dampens enthusiasm 是减弱热情；削弱义记录早于弄湿义。',
 'dampens spirits 打击兴致；dampens the surface 把表面稍微润湿。',
 'dampens 常是降低强度，不一定完全消灭；dampens enthusiasm 不等于 everyone gives up 所有人放弃。',
 ('The bad weather dampens our enthusiasm for the trip.','坏天气让我们对旅行的热情低了些。'),('She dampens the cloth before wiping the table.','她擦桌子前先把布稍微弄湿。'),sources=S('dampens','dampen'))
W('dampened','/ˈdæmpənd/','弄微湿了；减弱了、使扫兴了',
 '布刚才被稍微润湿，或一条消息给热情泼了点冷水，用 dampened。两义都常见，但真实记录先有削弱义。',
 'damp + -en → dampen，再加完整 -ed，/n/ 后读 /d/；不是 damp 直接加一个 -ened 后缀。',DAMPEN+[['dampen + -ed → dampened','过去弄微湿、压低强度或兴致']],
 'dampened cloth 是润湿的布，dampened our hopes 是打击了希望；可以有程度轻重，并非一律全毁。',
 'slightly dampened 稍微润湿、削弱；dampened spirits 受挫的兴致。',
 'dampened 讲影响后的变化，damp 可直接形容微湿状态；a damp cloth 不交代谁、何时把它弄湿。',
 ('He dampened the cloth with a little water.','他用一点水把布润湿。'),('The delay dampened our excitement.','延误让我们的兴奋劲低了些。'),sources=S('dampened','dampen'))
W('dampening','/ˈdæmpənɪŋ/','正在弄微湿、减弱；使人扫兴的',
 '湿度正被稍微加上去，或兴致、强度正被压低，是 dampening。把 damp 的相关状态变成使它发生的动作，再展开过程。',
 'damp + 使动 -en → dampen，再加完整 -ing；没有去掉 en，也不再双写 n。',DAMPEN+[['dampen + -ing → dampening','使微湿、减弱的过程或作用']],
 'dampening the paper 是把纸稍微润湿，dampening enthusiasm 是正减弱热情；声学等也可写降低振动、声音。',
 'a dampening effect 压低强度、兴致的作用；dampening a cloth 润湿布。',
 'dampening 是过程、作用，dampness 是微湿这一状态；不是看见 damp 开头就都译成潮气。',
 ('She was dampening the paper before shaping it.','她正把纸稍微润湿，再做造型。'),('The long wait was dampening everyone’s enthusiasm.','久等正在消磨大家的热情。'),sources=S('dampening','dampen'))
SEETHE=[['古英语 seoþan → 中古英语 sethen → seethe','煮、沸腾；古英语也已有受忧虑、烦扰的比喻材料'],['现代主要心理、翻涌用法','心里怒气翻腾；液体、群体翻动；旧强变化分词在 sodden 中另发展']]
W('seethe','/siːð/','怒气在心里翻腾；翻涌、沸腾',
 '表面可能没喊，心里却像一锅水一直翻滚，叫 seethe。今天最常见的画面之一，是压着但停不下来的怒气。',
 '承古英语 seoþan 煮、沸腾，经中古英语 sethen 延续；早期已有烦扰的比喻，不能把一切心理义都说成现代才新造。',SEETHE,
 'seethe with anger 是怒气翻腾，seethe in silence 是一声不吭却气得不行；海水等也可 seethe，强调翻涌不一定靠加热。',
 'seethe with resentment 心里怨气翻腾；seethe over the decision 因决定愤愤不平。',
 'seethe 不要求大喊大叫，可能是内里的怒火；shout 描写喊出声音，两者可以同时发生，也可以只发生一种。',
 ('Some fans began to seethe at the referee’s decision.','一些球迷因裁判的决定气得心里直翻腾。'),('We watched the sea seethe below the cliffs.','我们看着悬崖下海水翻涌。'),sources=S('seethe','seethe'))
W('seethes','/siːðz/','怒气翻腾、翻涌〔第三人称单数〕',
 '一个人表面在听，心里却越想越气，用 seethes。它强调持续在里面翻腾，不只是一瞬间不高兴。',
 'seethe + -s，保留 e，/ð/ 后读 /z/；词尾 /ðz/ 连着发，不添 /ɪz/。',SEETHE+[['seethe + -s → seethes','他、她心里怒火翻腾；它翻涌']],
 'seethes with anger 是气得内心翻腾，seethes at the unfairness 是因不公平愤愤不平；可以同时保持沉默。',
 'seethes quietly 默默生着闷气；seethes with resentment 怨气在心里翻腾。',
 'seethes 描写持续的内在怒气，snaps 更像突然厉声说出一句话；心里翻腾和外露的动作侧重不同。',
 ('He seethes with anger whenever he recalls the insult.','每次想起那次侮辱，他都怒气翻腾。'),('She seethes in silence during the discussion.','讨论时，她默不作声，心里却气得不行。'),sources=S('seethes','seethe'))
W('seethed','/siːðd/','怒气翻腾了；翻涌、沸腾了',
 '刚才一直压着怒气、心里翻腾，用 seethed；液体、海水等翻涌，也可这样写，今天心理义尤其常见。',
 '现代 seethe 去 e + 完整 -ed，/ð/ 后读 /d/；过去曾有强变化形式，但普通现代过去式、过去分词用 seethed。',SEETHE+[['现代 seethe 去 e + -ed → seethed','过去心里翻腾、液体翻涌']],
 'seethed with anger 是怒火翻腾，seethed in silence 是闷着气；不像 exploded 那样必然让人想到突然发作。',
 'seethed all afternoon 整个下午愤愤不平；seethed at the injustice 因不公而怒气翻腾。',
 'seethed in silence 比 was angry 更有画面：人没出声，怒气却在里面不停翻滚。',
 ('I seethed in silence while he took all the credit.','他把功劳全揽走时，我默默气得不行。'),('The crowd seethed with anger at the announcement.','听到宣布，人群怒气翻腾。'),sources=S('seethed','seethe'))
W('seething','/ˈsiːðɪŋ/','怒气翻腾的；翻涌的；拥挤翻动的',
 '内里像沸水一样不停翻，是 seething。最常见可说气得不行，也能形容一大群人挤挤攘攘地动。',
 'seethe 去 e + 完整 -ing；分词、形容词把翻腾动作展开成持续状态，现代词尾接在完整动词后。',SEETHE+[['seethe 去 e + -ing → seething','内在怒火、液体或人群持续翻动']],
 'seething with rage 是怒火翻腾，a seething mass of people 是翻动拥挤的一大群人；不要求所有人都愤怒。',
 'quietly seething 默默气得不行；a seething crowd 挤挤攘攘的人群。',
 'seething crowd 可以强调人多、活动剧烈；seething with anger 才把怒气说清楚，不能见人群就默认暴怒。',
 ('She was still seething with anger when I arrived.','我到时，她仍气得不行。'),('We looked down at the seething mass of people in the square.','我们俯看广场上挤挤攘攘、不断翻动的人群。'),sources=S('seething','seethe'))
W('sodden','英 /ˈsɒdən/；美 /ˈsɑːdən/','湿透的、浸得发软的',
 '鞋、衣服、地面吸满了水，湿得沉沉软软，叫 sodden。比一点微潮强得多，有泡透、湿塌的感觉。',
 '承古英语 soden，是 seoþan 煮、沸腾的旧强变化过去分词，和 seethe 有历史联系；不是现代 sod 草皮加使动 -en。',
 [['古英语 seoþan 的过去分词 soden → 中古英语 sodden','煮过的、在水里处理过的'],['较像久煮后浸软 → 现代 sodden','浸水、湿透、软塌的状态；不再按 seethe 的普通现代分词用']],
 'sodden clothes 是湿透的衣服，a sodden field 是积湿、湿透的场地；东西不必真的被煮过。',
 'rain-sodden ground 雨浸透的地面；sodden shoes 湿透的鞋。',
 '现代 seethe 的普通过去分词是 seethed；sodden 主要单独作湿透形容词。历史亲缘存在，今天不能随便互换。',
 ('We took off our sodden shoes at the door.','我们在门口脱下湿透的鞋。'),('The match was cancelled because of the sodden pitch.','场地湿透了，比赛被取消。'),sources=S('sodden','sodden'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfg',ROOTS,WORDS)
 extend_lessons()
