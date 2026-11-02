"""Drying out, wilting, shrivelling, small folds and gradual fading."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4553':dict(words=['drip','drop','droop','droops','drooped','drooping'],label='drip、drop 与 droop 的下落、下垂材料',note='droop 接古诺尔斯 drupa，经中古英语 droupen，和英语 drop、drip 属相关旧词族；现代不靠把 drop 的元音随意拉长来造词。'),
 'B3778':dict(words=['fade','fades','faded','fading'],label='fade 的颜色、声音和记忆渐弱',note='fade 联系中古英语及法语苍白、衰弱材料；褪色、渐弱是常用动词义，高尔夫球术语只是较专门的另一用法。'),
 'A2238':dict(words=['crinkle','crinkles','crinkled','crinkling'],label='crinkle 的弯曲材料与旧反复形式',note='crinkle 接古英语 crincan、cringan 一系弯曲材料的反复动作形式，可与 cringe 比较；不从现代 wrinkle 换开头造词。'),
 'A1760':dict(words='parch parched wilt wilts wilted wilting wither withers withered withering shrivel shrivels shrivelled shrivelling shriveled shriveling crinkle crinkles crinkled crinkling rumple rumples rumpled rumpling crease creases creased creasing fade fades faded fading droop droops drooped drooping'.split(),label='干枯、萎蔫、褶皱和渐弱动词的现代变化',note='shrivelled、shrivelling 多见英式双 l，shriveled、shriveling 多见美式单 l，含义相同；rumple 的名词记录早于现存动词记录，不能硬画成现代动词先造全部名词。'),
}
PARCH=[['中古英语 parchen 等 → parch','较早有烘干谷物等义；具体来源未定，若干更早候选仍属假说'],['热、干燥使水分散失 → 干得厉害、口干难耐','parched 今天常形容土地干裂，或人口渴得不行']]
W('parch','英 /pɑːtʃ/；美 /pɑːrtʃ/','使干透、烤干、使焦渴',
 '热太阳、干风把水分抽走，地干、嘴也干得难受，叫 parch。抓住热或干燥把水耗掉的感觉。',
 '接中古英语 parchen 等；更早来源未定，曾有联系 perish 一系或从 parchment 逆构等假说，不把某条猜测写成已确定借入史。',PARCH,
 'parch the ground 是把地晒干，parch the throat 是使喉咙干得难受；日常更常遇到形容状态的 parched。',
 'parch the soil 晒干土壤；a parching wind 使人、土地干燥的风。',
 'parch 往往多了干得厉害、由热干造成的感觉；dry 范围更广，风干、擦干等都能说。',
 ('The summer sun can parch the ground in a few days.','夏日太阳几天就能把地晒干。'),('Hot, dry winds began to parch the leaves.','炎热干风开始把叶子吹得干枯。'),sources=S('parch','parch'))
W('parched','英 /pɑːtʃt/；美 /pɑːrtʃt/','干透、干裂的；口干难耐、渴极了的',
 '土干到水分被抽空，或走了很久嘴干得想喝水，叫 parched。形容人时常带口语夸张：我渴坏了。',
 'parch + 完整 -ed，/tʃ/ 后读 /t/，结尾 /tʃt/；可作过去分词或状态形容词。',PARCH+[['parch + -ed → parched','被热、干燥弄干；口渴难耐']],
 'parched ground 是干透的地，a parched throat 是干得难受的嗓子；I am parched 很常是在说渴极了。',
 'parched fields 干枯田地；feel parched 觉得口干难耐。',
 'parched 比 thirsty 更有嘴干、渴得厉害的感觉；形容土地则是水分匮乏，不是土地真的在说想喝水。',
 ('The fields were parched after weeks without rain.','几周没下雨，田地干透了。'),('I am parched after that long walk.','走了那么久，我渴坏了。'),sources=S('parched','parch'))
WILT=[['较早 welk、welken 一系 → 近代 wilt','大概为形式变化，或联系荷兰语、低地德语；更早来源未定'],['植物软塌、失去挺立 → 人泄气、没精神','压力、热、疲劳都能借这种支撑不住的画面']]
W('wilt','/wɪlt/','萎蔫、打蔫；使萎蔫；泄气、失去精神',
 '原本挺着的叶子、花茎软下来、垂下去，是 wilt。人被热、压力、疲劳弄得蔫了，也像这样失去支撑。',
 '大概由较早 welk、welken 一系变化，相关荷兰语、低地德语形式可比较；现代 wilt 已是完整基础动词，再接 -ed、-ing 等词尾。',WILT,
 'flowers wilt 是花打蔫，wilt in the heat 是热得没精神；炒菜里 wilt spinach 可指把菠菜加热到软下来。',
 'wilt under pressure 压力下泄气、撑不住；wilted leaves 蔫叶。',
 'wilt 是软塌、失去挺劲，不一定已经枯死；die 才直接说死亡，植物稍蔫也可能恢复。',
 ('The flowers began to wilt in the heat.','花在热天开始打蔫。'),('She refused to wilt under pressure.','她没有在压力下泄气。'),sources=S('wilt','wilt'))
W('wilts','/wɪlts/','萎蔫、使萎蔫；泄气〔第三人称单数〕',
 '一盆植物在太阳下慢慢软塌，或一个人在强压下蔫下来，用 wilts。仍保留“挺不住、没精神”的形象。',
 'wilt + -s，/t/ 后读 /s/；现代三单加在萎蔫基础动词后，不改变元音。',WILT+[['wilt + -s → wilts','它软塌；他、她泄气、失去精神']],
 'wilts quickly 是很快蔫，wilts in the heat 是热得没精神；可用人或植物作主语。',
 'wilts under criticism 被批评得泄气；wilts in direct sun 直晒下打蔫。',
 'wilts 强调挺立、活力减弱，shrivels 更容易让人看见干缩、表面皱起；不只是中文枯的同义替换。',
 ('The basil wilts quickly without water.','罗勒没水很快就蔫。'),('He wilts in the afternoon heat.','下午一热，他就没精神。'),sources=S('wilts','wilt'))
W('wilted','/ˈwɪltɪd/','萎蔫、软塌了；蔫的；受挫、没精神的',
 '花、叶已经失去挺劲、垂软下来，是 wilted；人的兴致、精神被消磨，也能这样写。',
 'wilt + 完整 -ed；/t/ 后读 /ɪd/，多一个音节。既可过去式，也可描述结果状态。',WILT+[['wilt + -ed → wilted','过去软塌；已经萎蔫、没精神']],
 'wilted flowers 是蔫花，wilted spinach 是加热变软的菠菜；后者可以是正常菜肴状态，并不代表坏了。',
 'wilted in the heat 热得发蔫；slightly wilted 有点蔫。',
 'wilted spinach 可以是食谱刻意要的软化结果；rotten 则说腐烂，两者不能只凭叶子不挺就混用。',
 ('The flowers had wilted by the end of the day.','到一天结束时，花已经蔫了。'),('We served the fish with wilted spinach.','我们给鱼配了炒软的菠菜。'),sources=S('wilted','wilt'))
W('wilting','/ˈwɪltɪŋ/','正在萎蔫、软塌；正在泄气、没精神',
 '叶子、花茎正慢慢撑不住往下垂，或人正在疲劳、压力下蔫下来，是 wilting。',
 'wilt + 完整 -ing，直接加；基础末尾 lt 两字母保留，不双写 t。',WILT+[['wilt + -ing → wilting','变软塌、失去活力的过程']],
 'wilting flowers 是正蔫的花，wilting in the heat 是热得没精神；wilt 作及物动词时也能说正把菜叶炒软。',
 'wilting leaves 正打蔫的叶；wilting under pressure 压力下撑不住。',
 'wilting 常看见一个变化过程，wilted 常看见已经软下来的状态；同一盆花在不同叙述阶段可用不同形式。',
 ('The flowers were wilting in the hot room.','花在闷热房间里正慢慢打蔫。'),('By mid-afternoon, we were all wilting in the heat.','到下午三四点，我们都热得没精神了。'),sources=S('wilting','wilt'))
WITHER=[['中古英语 widderen、wederen 等 → wither','干枯、失去活力，通常联系较早 weather 经风吹日晒的动词材料'],['植物干枯 → 人、希望衰弱；话语、目光使人难堪','教学先从干枯画面理解，记录中人物比喻也很早出现，不硬排成现代才转义']]
W('wither','英 /ˈwɪðə/；美 /ˈwɪðər/','干枯、枯萎；使衰弱、消退；以冷峻态度使人难堪',
 '植物一点点干、失去鲜活，像 wither；希望、感情也能像叶子一样衰弱。一个冷眼把人气势压下去，则保留使人萎缩的感觉。',
 '接中古英语 widderen 等，通常联系旧的 wederen 经受天气材料，后来形式分化；人物比喻记录也很早，不简单说只在现代从植物新造。',WITHER,
 'plants wither 是植物干枯，hopes wither 是希望衰退；wither under criticism 是被批评得气势、精神萎缩。',
 'wither away 一点点衰败消失；wither in the heat 热得干枯。',
 'wilt 更常突出软塌、下垂，wither 更容易想到干枯、失去生命力；现实植物的两个过程可能同时出现。',
 ('Without enough water, the leaves began to wither.','水不够，叶子开始干枯。'),('Their hopes began to wither as the weeks passed.','几个星期过去，他们的希望渐渐衰弱。'),sources=S('wither','wither'))
W('withers','英 /ˈwɪðəz/；美 /ˈwɪðərz/','干枯、衰弱、使萎缩〔第三人称单数〕',
 '叶子在热、干中失去鲜活，或某种希望、关系一点点衰退，用 withers。画面像水分、活力被抽走。',
 'wither + -s，读 /z/；基础 wither 是整个动词，词内 -er 不表示某种职业、人物。',WITHER+[['wither + -s → withers','它干枯、衰弱；它使气势萎缩']],
 'withers in the heat 是热中干枯，enthusiasm withers 是热情衰退；away 又常加强渐渐消失的结果。',
 'withers away 渐渐衰败；withers without care 缺乏照料而衰弱。',
 'withers 常比 disappears 有逐渐丧失活力的过程；后者只说不见了，未必给出干枯般的变化感。',
 ('The plant withers in the dry summer heat.','植物在夏天干热中枯萎。'),('His enthusiasm withers whenever the plan is delayed again.','计划每次又延期，他的热情就低下去。'),sources=S('withers','wither'))
W('withered','英 /ˈwɪðəd/；美 /ˈwɪðərd/','干枯、枯萎了；枯干的；希望、活力衰退了',
 '叶子已经没了鲜活、水分，叫 withered；希望、关系被长期冷落、打击，也可以写成已经枯萎。',
 'wither + 完整 -ed，读 /d/；基础最后是轻元音或 r，不读 /ɪd/。可过去式，也可形容结果。',WITHER+[['wither + -ed → withered','已枯萎、干枯；活力已衰弱']],
 'withered leaves 是干枯叶子，withered hopes 是衰退的希望；不一定只描述某次突然事件。',
 'withered flowers 枯花；withered away 渐渐衰败了。',
 'withered 常突出鲜活已失，creased 只是有折痕、皱线；表面有皱不等于生命力正在枯萎。',
 ('Withered leaves covered the path.','干枯叶子铺满小路。'),('Their interest withered as the project dragged on.','项目拖了下去，他们的兴趣渐渐衰退。'),sources=S('withered','wither'))
W('withering','英 /ˈwɪðərɪŋ/；美 /ˈwɪðərɪŋ/','正在干枯、衰弱；冷峻伤人、让人难堪的',
 '叶子正失水、干枯，是 withering；a withering look 则像一个眼神就把人气势压蔫，表示冷峻、鄙夷得让人难堪。',
 'wither + 完整 -ing；英式后接元音时发 /r/。分词写干枯过程，形容词可写言语、目光的压迫、伤人效果。',WITHER+[['wither + -ing → withering','干枯过程；使人气势萎缩的目光、批评']],
 'withering plants 是正枯萎的植物，withering criticism 是毫不留情、让人难堪的批评；a withering look 是冷峻鄙夷的一眼。',
 'a withering reply 冷峻伤人的答复；withering leaves 正干枯的叶。',
 'withering look 不只说 angry 生气，还强调对方被看得难堪、气势缩下去；它传达的是眼神的效果。',
 ('She gave him a withering look.','她冷冷鄙夷地看了他一眼，让他很难堪。'),('The garden was full of withering plants after the drought.','旱情过后，园里满是正在枯萎的植物。'),sources=S('withering','wither'))
SHRIVEL=[['十六世纪 shrivel，较早见 shriveled 一类形式','来源未定，或联系北欧皱缩材料；与 shrink、shrimp 的更远联系只属可能'],['皱缩、干瘪 → 感情、信心等萎缩','像葡萄失水变小、表面起皱；不等于普通折一道直痕']]
W('shrivel','/ˈʃrɪvəl/','皱缩、干瘪；使皱缩；使信心等萎缩',
 '葡萄失水变成小小皱皱的样子，像 shrivel。抓住体积缩下去、表面也皱起来，不只是向下垂。',
 '来源未定，可能有北欧皱缩词参与；更远与 shrink、shrimp 的联系保留为可能，不把它们排成确定直系派生。',SHRIVEL,
 'shrivel up 是干缩、皱缩，shrivel in the sun 是晒得干瘪；confidence can shrivel 是信心也会一点点缩下去。',
 'shrivel with heat 受热皱缩；shrivel up completely 完全干瘪。',
 'shrivel 常带表面皱、体积小，wilt 主要是软塌、蔫下去；一张叶子可先蔫，再干缩起皱。',
 ('The grapes began to shrivel in the sun.','葡萄在太阳下开始干缩起皱。'),('Plants can shrivel up during a long drought.','长时间干旱会让植物干瘪。'),sources=S('shrivel','shrivel'))
W('shrivels','/ˈʃrɪvəlz/','皱缩、干瘪；使萎缩〔第三人称单数〕',
 '水果、叶子失水后缩小起皱，或一个人的信心像这样一点点缩水，用 shrivels。',
 'shrivel + -s，/l/ 后读 /z/；直接加三单，单、双 l 的地区差异主要在 -ed、-ing 等形式中。',SHRIVEL+[['shrivel + -s → shrivels','它干缩起皱；信心等萎缩']],
 'shrivels in the heat 是热中干缩，shrivels up 是缩成干瘪一团；形容精神状态时可借缩水感。',
 'shrivels slowly 慢慢干缩；shrivels into a small lump 缩成一个小团。',
 'shrivels 常有缩小和皱起两个侧面，dries 只说水分减少；干燥不一定都明显缩皱。',
 ('The fruit shrivels if it is left in the sun.','水果放在太阳下会干缩起皱。'),('His confidence shrivels whenever he is mocked.','每次被嘲笑，他的信心就缩下去。'),sources=S('shrivels','shrivel'))
W('shrivelled','/ˈʃrɪvəld/','皱缩、干瘪了；干瘪的〔常见英式拼法〕',
 '果皮、叶子已经失水变小、皱巴巴，叫 shrivelled。它让人看到收缩后的干瘪样子。',
 'shrivel 常见英式双写 l + 完整 -ed → shrivelled，/l/ 后读 /d/；美式常写 shriveled，意思相同。',SHRIVEL+[['shrivel 双写 l + -ed → shrivelled','英式常见过去式、过去分词；已干缩']],
 'shrivelled grapes 是干瘪葡萄，shrivelled leaves 是皱缩叶子；也可比喻希望、信心萎缩。',
 'shrivelled up 干缩成一团；a shrivelled apple 干瘪苹果。',
 'shrivelled 与 shriveled 是同一个词的拼写变体，发音通常相同，不表达不同干燥程度。',
 ('The apples had shrivelled in the heat.','苹果在热中已经干瘪。'),('A few shrivelled leaves clung to the branch.','枝头还挂着几片干缩的叶子。'),sources=S('shrivelled','shrivel'))
W('shriveled','/ˈʃrɪvəld/','皱缩、干瘪了；干瘪的〔常见美式拼法〕',
 '水果表面皱了、整个缩小了，可以写 shriveled；它和双 l 的 shrivelled 表示同样的干缩结果。',
 'shrivel + 完整 -ed → shriveled，常见美式保留单 l；词尾读 /d/。英式常见双 l 形式也正确。',SHRIVEL+[['shrivel + -ed → shriveled','美式常见单 l；过去干缩或已干瘪']],
 'shriveled fruit 是干瘪水果，shriveled up 是已经干缩；比喻信心、希望时仍保留失去分量的感觉。',
 'shriveled leaves 干缩叶子；shriveled in the sun 晒得干瘪。',
 'shriveled 是皱缩、干瘪，shredded 是撕、切成细条；两个结果外形不同，不能只按开头 shr- 混记。',
 ('The tomatoes had shriveled on the vine.','番茄在藤上已经干瘪。'),('He picked up a shriveled leaf from the ground.','他从地上捡起一片干缩的叶子。'),sources=S('shriveled','shrivel'))
W('shrivelling','/ˈʃrɪvəlɪŋ/','正在皱缩、干瘪；使萎缩〔常见英式拼法〕',
 '水分正在散掉，东西一点点变小、起皱，是 shrivelling。它更像动态的干缩过程，和已经干瘪的结果分开。',
 'shrivel 常见英式双写 l + 完整 -ing → shrivelling；美式常写 shriveling，发音、主要意义相同。',SHRIVEL+[['shrivel 双写 l + -ing → shrivelling','英式常见拼法；正在干缩']],
 'shrivelling leaves 是正干缩的叶子，shrivelling in the heat 是热中干缩；抽象信心也可用这个过程画面。',
 'shrivelling up 正缩小起皱；shrivelling fruit 正干瘪的水果。',
 'shrivelling 是体积、表面在变，withering 更强调活力衰退、干枯；两种描写可能覆盖同一个过程。',
 ('The leaves were shrivelling in the dry wind.','叶子正在干风里缩小起皱。'),('We noticed the fruit shrivelling near the window.','我们发现窗边的水果正在干瘪。'),sources=S('shrivelling','shrivel'))
W('shriveling','/ˈʃrɪvəlɪŋ/','正在皱缩、干瘪；使萎缩〔常见美式拼法〕',
 '原来饱满的东西正在慢慢缩水、皱起，可以写 shriveling；这是单 l 的常见美式形式。',
 'shrivel + 完整 -ing → shriveling，美式常不双写 l；与双 l 的 shrivelling 同义，基础词读音保留。',SHRIVEL+[['shrivel + -ing → shriveling','美式常见单 l；干缩过程']],
 'shriveling in the sun 是晒得正干缩，shriveling up 是正在缩瘪；写心理感受时可借这种收缩感。',
 'shriveling leaves 正干缩的叶子；shriveling fruit 正缩水起皱的水果。',
 'shriveling、shrivelling 的选择主要是拼写习惯；不需要为它们分别记两套植物或情绪含义。',
 ('The grapes were shriveling on the tray.','葡萄正在托盘上干缩。'),('The plants were shriveling under the hot lights.','植物在热灯下正慢慢干瘪。'),sources=S('shriveling','shrivel'))
CRINKLE=[['古英语 crincan、cringan 一系弯曲、屈服材料 → 中古英语 crenclen → crinkle','有旧反复动作形式；可与 cringe 比较'],['小弯折、小皱纹 → 揉动薄材料的窸窣声','眼角细纹、薄纸褶皱常见，不限于坏掉、干枯的东西']]
W('crinkle','/ˈkrɪŋkəl/','起细褶、细皱；使起褶；窸窣响；一条细皱纹',
 '眼睛一笑，眼角出一圈小细纹；薄纸轻轻一揉，表面小褶皱、声音也窸窣，这些都像 crinkle。',
 '接中古英语 crenclen，联系古英语 crincan、cringan 一系弯曲材料与旧反复动作形式；与 cringe 有历史联系。',CRINKLE,
 'eyes crinkle 是眼角笑出细纹，crinkle the paper 是把纸弄出小褶，the crinkle of a wrapper 是包装纸窸窣声。',
 'crinkle at the corners 眼角起细纹；crinkle softly 轻轻窸窣响。',
 'crinkle 常是许多小细褶，crumple 更容易让人想到把纸、衣料揉皱成一团；程度、形状不同。',
 ('Her eyes crinkle when she smiles.','她一笑，眼角就起细纹。'),('The thin paper began to crinkle in his hands.','薄纸在他手里开始起细褶、窸窣响。'),sources=S('crinkle','crinkle'))
W('crinkles','/ˈkrɪŋkəlz/','起细褶、窸窣响〔第三人称单数〕；细褶、细纹〔复数〕',
 '眼角、纸面出现许多小线、小弯折，叫 crinkles；薄材料一动就细响，也可用同形动词。',
 'crinkle + -s，保留 e，/l/ 后读 /z/；动词三单、细纹名词复数同形。',CRINKLE+[['crinkle + -s → crinkles','它起细褶、细响；多条细纹']],
 'crinkles around the eyes 是眼周细纹，paper crinkles 是纸窸窣响、起褶；前者名词，后者可作动词。',
 'small crinkles 小细褶；crinkles at the edges 边缘起皱。',
 'crinkles 可是笑容带出的自然细纹，不自动带老、丑的评价；评价要看上下文怎么写。',
 ('Tiny crinkles appeared around her eyes as she laughed.','她笑起来时，眼周出现细细的纹路。'),('The wrapper crinkles whenever I touch it.','我每次碰包装纸，它就窸窣响。'),sources=S('crinkles','crinkle'))
W('crinkled','/ˈkrɪŋkəld/','起细褶、弄皱了；有细纹的；窸窣响了',
 '纸或眼角已经出现小细褶，叫 crinkled；动词过去式也能描述笑时眼角一下皱起来、薄纸被揉响。',
 'crinkle 去 e + 完整 -ed，/l/ 后读 /d/；可过去式、过去分词或形容细皱状态。',CRINKLE+[['crinkle 去 e + -ed → crinkled','过去起细褶；已有细纹、细褶']],
 'crinkled paper 是有细褶的纸，eyes crinkled 是眼角笑皱了；不用把每一种皱都理解成干枯。',
 'crinkled at the corners 眼角起了细纹；a crinkled wrapper 揉出细褶的包装纸。',
 'crinkled 强调细小、多处弯折，a sharply creased sheet 可强调一条压得清晰的折线。',
 ('Her eyes crinkled with amusement.','她觉得好笑，眼角笑出细纹。'),('He smoothed the crinkled paper on the table.','他把桌上有细褶的纸抚平。'),sources=S('crinkled','crinkle'))
W('crinkling','/ˈkrɪŋklɪŋ/','正在起细褶、窸窣响；薄材料的细响声',
 '小褶皱正随着手、脸的动作出现，或薄纸正一阵细细作响，是 crinkling。形状和声音在这个词里常一起出现。',
 'crinkle 去 e + 完整 -ing，常读 /ˈkrɪŋklɪŋ/；nk 的 /ŋk/ 保留。',CRINKLE+[['crinkle 去 e + -ing → crinkling','起细褶过程；包装纸等窸窣声']],
 'eyes crinkling with a smile 是眼角笑出细纹，the crinkling of paper 是薄纸窸窣声；按对象选中文。',
 'crinkling plastic 起褶作响的塑料；a crinkling sound 窸窣细响。',
 'crinkling 偏薄材料一边变褶一边响，clattering 偏硬物接连碰撞，声音的材料感不同。',
 ('The crinkling of the wrapper broke the silence.','包装纸窸窣的声音打破寂静。'),('She smiled, her eyes crinkling at the corners.','她笑了，眼角泛起细纹。'),sources=S('crinkling','crinkle'))
RUMPLE=[['较早 rimple、古英语 hrympel 等皱褶材料可能参与 → rumple','具体路径不确定，也有荷兰语影响分析'],['rumple 的褶皱名词与动词','名词记录较早；动词后来常写把衣服、头发弄皱、弄乱，历史顺序不只靠现代拆分判断']]
W('rumple','/ˈrʌmpəl/','弄皱、揉乱；起皱；褶皱',
 '原本平整的衬衫被挤出一片乱褶，头发被手揉乱，像 rumple。重点是弄得不平、不整齐，未必要缩成一个球。',
 '来源不全确定，可能与 rimple、古英语 hrympel 等皱褶材料有关，并受荷兰语影响；名词记录早于现存常引动词记录。',RUMPLE,
 'rumple a shirt 是把衬衫弄皱，rumple someone’s hair 是揉乱头发；动作可以亲昵，也可以只是挤压所致。',
 'rumple the sheets 弄皱床单；rumple easily 容易起皱。',
 'rumple 常让人想到衣服、头发不整齐，crumple 更容易是把柔软材料揉成更明显的一团，二者有重合。',
 ('Packing too tightly can rumple your clothes.','装得太紧会把衣服挤皱。'),('He reached over to rumple the boy’s hair.','他伸手揉乱男孩的头发。'),sources=S('rumple','rumple'))
W('rumples','/ˈrʌmpəlz/','弄皱、揉乱、起皱〔第三人称单数〕；乱褶〔复数〕',
 '某件事把衬衫挤乱、头发揉乱，用 rumples；名词复数则是那些不平整的褶皱。',
 'rumple + -s，保留 e，/l/ 后读 /z/；动词、名词现代变化相同，早期来源仍按基础词说明。',RUMPLE+[['rumple + -s → rumples','它弄皱、揉乱；多处乱褶']],
 'rumples his hair 是把他头发揉乱，rumples the bedspread 是弄皱床罩；不是只有纸才能这样变形。',
 'rumples easily 容易起乱褶；rumples the fabric 弄皱衣料。',
 'rumples 的不整齐通常来自挤、揉、压；folds 可以是有意整齐折好，结果不一定凌乱。',
 ('The tight seat belt rumples his shirt.','过紧的安全带把他的衬衫压皱。'),('She rumples his hair with an affectionate hand.','她亲昵地伸手揉乱他的头发。'),sources=S('rumples','rumple'))
W('rumpled','/ˈrʌmpəld/','弄皱、揉乱了；皱巴巴、不整齐的',
 '衬衫一夜睡皱、床单挤成乱褶，或头发乱乱，叫 rumpled。它常直接形容一种有生活感的不整齐样子。',
 'rumple 去 e + 完整 -ed，/l/ 后读 /d/；过去分词可转作衣物、头发状态的形容词。',RUMPLE+[['rumple 去 e + -ed → rumpled','已弄乱、起乱褶；皱巴巴的']],
 'a rumpled shirt 是皱巴巴衬衫，rumpled hair 是揉乱、睡乱的头发；不必含干燥、衰老的意思。',
 'rumpled sheets 皱乱床单；a slightly rumpled suit 稍显皱乱的西装。',
 'rumpled 强调外表不整齐，dirty 说有脏污；衬衫可以干净却皱，不能自动合成同一个评价。',
 ('He arrived in a rumpled shirt.','他穿着皱巴巴的衬衫来了。'),('She smoothed the rumpled sheets on the bed.','她把床上皱乱的床单抚平。'),sources=S('rumpled','rumple'))
W('rumpling','/ˈrʌmplɪŋ/','正在弄皱、揉乱；起乱褶的过程',
 '手、座椅或包里空间正把衣物、头发弄得不平整，是 rumpling。动作可以轻，也可以因挤得太紧而发生。',
 'rumple 去 e + 完整 -ing，常读 /ˈrʌmplɪŋ/；mp 两个辅音字母保留，不双写 p。',RUMPLE+[['rumple 去 e + -ing → rumpling','弄乱、挤皱的过程']],
 'rumpling his hair 是正在揉乱头发，rumpling the jacket 是正在把外套压皱；不要求一定伴随很响的声音。',
 'rumpling the cloth 揉乱布料；rumpling up the sheets 把床单弄皱乱。',
 'rumpling 先写形状、整齐程度变化，crinkling 还常让人听见薄纸、包装材料的细响。',
 ('He laughed, rumpling the child’s hair.','他笑着揉乱孩子的头发。'),('The straps were rumpling the shoulders of her jacket.','背带正把她外套的肩部压皱。'),sources=S('rumpling','rumple'))
CREASE=[['较早英语 creaste 脊、隆起线 → crease','可能是 crest 的变体；布折起后形成一条小脊线，关联仍保留可能性'],['折痕名词与动词 → 面部纹路、笑等表达','可有意压出整齐折线，也可意外压皱']]
W('creases','/ˈkriːsɪz/','折痕、皱线〔复数〕；使起折痕、起皱〔第三人称单数〕',
 '把纸折一下，展开后留下清楚的线，就是 creases；裤腿烫出的直线也能是它。折痕不一定是坏事。',
 'crease + -s，基础保留 e，/s/ 后读 /ɪz/；名词复数、动词三单同形，基础可能联系较早 creaste 脊线材料。',CREASE+[['crease + -s → creases','多条折线；它容易起折、使人皱脸等']],
 'sharp creases 是清晰折痕，creases in the trousers 是裤子折线；the fabric creases easily 是布容易压出皱痕。',
 'iron out the creases 烫平折痕；creases around the eyes 眼周纹路。',
 'creases 可以是一条条明确折线，crinkles 常偏细小、多处弯纹；压好裤线与把衣服揉乱，画面不同。',
 ('He ironed the creases out of the shirt.','他把衬衫的折痕烫平。'),('This fabric creases easily.','这种布容易起折痕。'),sources=S('creases','crease'))
W('creased','/kriːst/','折出痕、弄皱了；有折痕的；脸上起纹、笑开了',
 '纸、衣服被折压出清晰线，叫 creased；脸笑起来形成纹路，也能说 his face creased into a smile。',
 'crease 去 e + 完整 -ed，/s/ 后读 /t/；基础词尾音保持清音 /s/，不是读 /z/。',CREASE+[['crease 去 e + -ed → creased','过去压出折痕；已有折线或笑纹']],
 'creased trousers 是起了折痕的裤子，creased paper 是有折线的纸；face creased into a smile 则把面部动作写出来。',
 'badly creased 皱得厉害；creased at the edges 边缘有折痕。',
 'creased 不等于 torn 撕破：一张纸有折痕仍可完整，tear 才是纤维裂开、纸破掉的动作。',
 ('The letter was creased from being folded in his pocket.','信折在口袋里，已经有了折痕。'),('His face creased into a warm smile.','他脸上泛起纹路，温暖地笑了。'),sources=S('creased','crease'))
W('creasing','/ˈkriːsɪŋ/','正在起折痕、压皱；压出折线的过程',
 '纸、布正因折、压形成一条条线，是 creasing；脸部动作也能让纹路出现。重点是线状折痕正在形成。',
 'crease 去 e + 完整 -ing，/s/ 保留；不是加 -ing 后就把词尾自动浊化成 /z/。',CREASE+[['crease 去 e + -ing → creasing','形成折线、皱痕的过程']],
 'creasing the paper 是正给纸压折线，avoid creasing 是避免起折痕；可在折纸、包装、衣物场景用。',
 'creasing at the knees 膝部正压出折痕；creasing into a smile 笑得脸上起纹。',
 'creasing 可以是有意压一条折线；crumpling 通常更像把材料揉得乱、不平，动作结果不同。',
 ('She was creasing the paper before folding the box.','她正给纸压折线，再折成盒子。'),('The trousers were creasing at the knees.','裤子膝盖处正压出折痕。'),sources=S('creasing','crease'))
FADE=[['中古英语 fade、vade 等及法语 fader、fade 材料 → fade','苍白、衰弱、失去鲜活；更远具体来源有不同分析'],['色泽减弱 → 声音、光、记忆等渐弱','并非突然消失；音频、影像里可人为控制渐入、渐出']]
W('fades','/feɪdz/','褪色、渐弱、渐渐消失〔第三人称单数〕；渐变效果〔复数〕',
 '颜色一点点浅、音乐一点点轻，或记忆不再清晰，用 fades。共同点是强度逐渐退下去，不是啪地立刻没了。',
 'fade + -s，保留 e，/d/ 后读 /z/；基础联系中古英语、法语的苍白、衰弱材料。',FADE+[['fade + -s → fades','它逐渐变浅、变弱；多次渐变效果']],
 'colour fades 是颜色褪，music fades out 是音乐渐渐弱到听不见，memory fades 是记忆变淡。',
 'fades slowly 慢慢变淡；fades into the distance 渐渐远去看不清。',
 'fades 侧重逐渐变弱，vanishes 更容易只是交代消失；描写节奏不同。',
 ('This fabric fades in strong sunlight.','这种布在强阳光下会褪色。'),('The music fades out at the end of the scene.','场景结束时，音乐渐渐弱下去。'),sources=S('fades','fade'))
W('faded','/ˈfeɪdɪd/','褪色、渐弱了；颜色浅旧的；记忆、希望变淡了',
 '原来鲜明的颜色、声音已经退了一层，叫 faded；照片、衣服的 faded 常直接让人想到用了很久的浅旧颜色。',
 'fade 去 e + 完整 -ed；基础以 /d/ 结尾，词尾读 /ɪd/，多一个音节。',FADE+[['fade 去 e + -ed → faded','过去逐渐变弱；已经浅旧、变淡']],
 'a faded photograph 是褪色照片，faded jeans 是颜色洗淡的牛仔裤；hopes faded 是希望渐渐减弱。',
 'badly faded 褪色厉害；faded into the background 逐渐淡出注意。',
 'faded 说鲜明度减弱，withered 常说植物、活力枯萎；一张照片褪色不意味着照片像植物干死。',
 ('The curtains had faded in the sun.','窗帘在太阳下已经褪色。'),('She kept a faded photograph in her wallet.','她钱包里放着一张褪色照片。'),sources=S('faded','fade'))
W('fading','/ˈfeɪdɪŋ/','正在褪色、渐弱、变淡；逐渐消退的',
 '光线正一点点暗、声音正远去、记忆正模糊，是 fading。它把渐渐退场的过程保留下来。',
 'fade 去 e + 完整 -ing；词干的 /d/ 后直接接 /ɪŋ/，不双写 d。',FADE+[['fade 去 e + -ing → fading','色、光、声、印象逐渐减弱的过程']],
 'fading light 是渐暗的光，a fading memory 是渐淡的记忆；fading in 是从弱到强渐显，fading out 是渐隐。',
 'fading hopes 渐渐消退的希望；fading into the distance 渐远渐淡。',
 'fading in 是让内容渐渐出现，fading out 是让它渐渐退去；基础给渐变过程，方向由 in、out 明确。',
 ('We walked home in the fading light.','我们在渐暗的光线里走回家。'),('The sound of the train was fading into the distance.','火车声正向远处渐渐弱去。'),sources=S('fading','fade'))
DROOP=[['古诺尔斯 drupa → 中古英语 droupen → droop','垂下、低头、精神低落；与英语 drop、drip 的旧词族相关'],['物体下垂 → 疲倦、泄气的姿态','仍挂着、连着，往下弯，不一定掉到地上']]
W('droop','/druːp/','下垂、耷拉；低垂、没精神；下垂姿态',
 '耳朵、肩膀、叶子还连在原处，却软软往下垂，就是 droop。人的精神低下来，也常从肩、眼皮这种姿态看出来。',
 '借古诺尔斯 drupa，经中古英语 droupen；与 drop、drip 是相关旧词族，各自发展出现代形式，不靠任意拉长元音造词。',DROOP,
 'ears droop 是耳朵耷拉，shoulders droop 是肩膀垮下，eyelids droop 是眼皮困得往下垂。',
 'droop in the heat 热得垂软；droop with tiredness 累得没精神。',
 'droop 常还连着，只是垂软下去；drop 可直接掉下、落下。叶子低头和叶子掉落是两个画面。',
 ('The dog’s ears began to droop.','狗的耳朵开始耷拉。'),('The flowers droop in the afternoon heat.','花在午后热气里垂软下来。'),sources=S('droop','droop'))
W('droops','/druːps/','下垂、耷拉、低落〔第三人称单数〕',
 '一根花茎、一顶帽边或人的头软软垂下来，用 droops。抓住还连接着却失去向上支撑的样子。',
 'droop + -s，/p/ 后读 /s/；oo 保留长元音 /uː/，不双写 p。',DROOP+[['droop + -s → droops','它下垂；他、她垂头、没精神']],
 'head droops 是头垂下去，the brim droops 是帽檐软垂；with fatigue 可点明因疲劳。',
 'droops over the edge 垂过边；droops with sleepiness 困得垂下来。',
 'droops 的 oo 读 /uː/，drops 的 o 另读短元音；一个是耷拉下垂，一个常是掉落、降低。',
 ('His head droops when he gets sleepy.','他一困，头就垂下来。'),('The flower droops over the edge of the pot.','花垂过了花盆边。'),sources=S('droops','droop'))
W('drooped','/druːpt/','下垂、耷拉了；精神、姿态低落了',
 '刚才肩膀、头、叶子软软垂下，叫 drooped。叙述常用这个姿态让读者看出累、热或失望。',
 'droop + 完整 -ed，/p/ 后读 /t/；oo 长元音后不双写 p，仍是一个音节。',DROOP+[['droop + -ed → drooped','过去垂软、耷拉或泄气']],
 'shoulders drooped 是肩膀垮下，leaves drooped 是叶子垂软；原因可能水少、太热或人的情绪疲倦。',
 'drooped with exhaustion 累得垂头；drooped over his eyes 垂到眼前。',
 'drooped 描写下垂姿态，dropped 常说落下、掉落；his shoulders drooped 是垮肩，不是肩膀掉下来了。',
 ('Her shoulders drooped when she heard the news.','听到消息，她的肩膀垮了下来。'),('The leaves drooped in the midday heat.','正午热气里，叶子垂软了。'),sources=S('drooped','droop'))
W('drooping','/ˈdruːpɪŋ/','正在下垂、耷拉；低垂、软垂的',
 '眼皮正困得往下合、花茎正失去挺劲垂下来，是 drooping。它可以写过程，也能直接描写姿态。',
 'droop + 完整 -ing，直接加；oo 长元音保留，不双写 p。',DROOP+[['droop + -ing → drooping','下垂过程；软垂的状态']],
 'drooping eyelids 是耷拉的眼皮，drooping flowers 是垂软的花；不必已经干瘪、死亡。',
 'drooping branches 低垂树枝；drooping shoulders 垮下的肩。',
 'drooping 先写向下弯、失去支撑，shrivelling 更写干缩、起皱；方向和表面变化各有重点。',
 ('She tried to keep her drooping eyelids open.','她想撑开困得往下垂的眼皮。'),('We watered the drooping flowers by the window.','我们给窗边垂软的花浇了水。'),sources=S('drooping','droop'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfi',ROOTS,WORDS)
 extend_lessons()
