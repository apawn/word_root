"""Frequent body-part plurals and related actions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2607':dict(words=['hand','hands'],label='hand → hands：双手、指针与递交',note='hands 可为名词复数，也可是把东西递过去的动词形式，分别从句法与对象判断。'),
 'B2752':dict(words=['eye','eyes'],label='eye → eyes：眼睛与注视',note='名词眼睛的复数和动词注视的第三人称都写 eyes、读 /aɪz/。'),
 'B2765':dict(words=['ear','ears'],label='ear → ears：耳朵与谷穗分两条来源',note='耳朵接古英语 eare，谷穗另接古英语 ear、aeher；复数同形，不能据同音认定它们是一条意义链。'),
 'B2769':dict(words=['leg','legs'],label='leg → legs：腿、支撑脚与行程段',note='leg 经北欧语进入英语，身体的腿、家具支撑和旅程阶段是现代常见分支。'),
 'B2678':dict(words=['finger','fingers'],label='finger → fingers：手指与用手触弄',note='fingers 可说多个手指，也可说某人用手指触弄；ng 后常见 g 音，词尾读 z。'),
 'B2608':dict(words=['toe','toes'],label='toe → toes：脚趾与固定搭配',note='toes 复数英 /təʊz/、美 /toʊz/；toe the line 的动词也可形成 toes the line，表示遵守要求。'),
 'B2771':dict(words=['knee','knees'],label='knee → knees：膝盖、衣裤膝部与姿势',note='knees 的 k 不发音，复数读 /niːz/；on your knees 说跪着的姿态。'),
 'B3333':dict(words=['nail','nails'],label='nail → nails：指甲、钉子与做得漂亮',note='名词的指甲、钉子都是 nails；动词 nail 的完成得很出色等义也能形成第三人称 nails。'),
 'B2683':dict(words=['thumb','thumbs'],label='thumb → thumbs：拇指、手势与翻看',note='thumbs 的 b 不发音；名词拇指、动词 thumb through 翻看都在常见表达中出现。'),
}
W('hands','/hændz/','手〔复数〕；指针；人手；递给、交出〔hand 的第三人称单数〕',
 '双手可以握住、递出东西；钟表伸出指向时间的部分也叫 hands；需要帮忙做事时，还会按手说人手。',
 'hand + -s，/d/ 后读 /z/。hand 接古英语身体部位名，名词扩展为指针、劳动力，动词发展为用手递交；现代两种词性同写 hands。',
 [['古英语 hand → hand','手；后来也指指针、人手'],['hand 名词、动词 + -s → hands','多只手、指针；单数主语递交']],
 'wash your hands 洗手；the hands of a clock 时钟指针；extra hands 额外人手；hands me a cup 递给我一只杯子；in good hands 交给可靠的人照管。',
 'hands on the table；hands over the keys。','all hands 常按人手说全体人员；She hands me the keys 中 hands 是动词，表示递交。用主语、后面的宾语区分。',
 ('She hands me a cup of tea every morning.','她每天早上递给我一杯茶。'),('The hands of the clock pointed to twelve.','钟表的指针指向十二点。'),sources=['https://en.wiktionary.org/wiki/hands#English','https://en.wiktionary.org/wiki/hand#English'])
W('eyes','/aɪz/','眼睛；眼光、注视〔复数用法〕；注视、打量〔eye 的第三人称单数〕',
 '眼睛是 eyes；把眼光放在某物上盯着看，eye 又能作动词。He eyes the cake 还可能带着想要那块蛋糕的眼神。',
 'eye 已有 e，直接加 s，复数和动词形式都读 /aɪz/。eye 承接古英语 eage 等眼词，动词由视觉器官名转为注视、观察。',
 [['古英语 eage 等 → eye','眼睛；视觉、眼光等'],['eye + -s → eyes','多个眼睛；或单数主语打量、注视']],
 'bright eyes 明亮的眼睛；in her eyes 在她看来；keep your eyes on ... 盯住、持续关注；eyes the last piece of cake 盯着最后一块蛋糕。',
 'close your eyes；all eyes were on ...。','eyes 和 ice 的尾音不同：eyes /z/，ice /s/。in my eyes 常是依我看，不能每次按眼睛里面直译。',
 ('Her eyes shone with excitement.','她的眼睛因兴奋而发亮。'),('He eyes the last piece of cake but says nothing.','他盯着最后一块蛋糕，却没有开口。'),sources=['https://en.wiktionary.org/wiki/eyes#English','https://en.wiktionary.org/wiki/eye#English'])
W('ears','英 /ɪəz/；美 /ɪrz/','耳朵；听觉、倾听〔相应表达〕；谷穗〔复数〕',
 '听声音的耳朵是 ears；玉米一穗一穗也可数成 ears。现代同音同拼写，历史上却有不同的底词。',
 '两种 ear 都直接加复数 s，读 /z/。耳朵义接古英语 eare；谷穗义另接 ear、aeher 等尖穗词，并不是耳朵形状比喻出全部谷穗用法。',
 [['古英语 eare → ear → ears','听觉器官 → 多个耳朵、听的能力'],['古英语 ear、aeher → ear → ears','植物穗 → 多个谷穗']],
 'cover your ears 捂住耳朵；I am all ears 我洗耳恭听；music to my ears 令人高兴的消息；two ears of corn 两穗玉米。',
 'listen with both ears；ears of wheat。','I am all ears 是愿意认真听的固定说法。two ears of corn 在谷物场景说两穗，不用把两个 ear 的词源强行并为同一个。',
 ('Tell me what happened; I am all ears.','告诉我发生了什么，我洗耳恭听。'),('We cooked two ears of corn for lunch.','午饭时，我们煮了两穗玉米。'),sources=['https://www.etymonline.com/word/ear','https://en.wiktionary.org/wiki/ears#English'])
W('legs','/leɡz/','腿；家具等的支撑脚；行程、赛程的阶段〔leg 的复数〕',
 '人的腿支撑身体，桌腿支撑桌面。旅程也可以分成一段段，像一步步推进的几个 legs。',
 'leg + -s，词尾 /ɡ/ 后读 /z/。leg 经古诺尔斯语 leggr 进入英语，身体部位名扩展到支撑结构与分段行程。',
 [['古诺尔斯语 leggr → leg','腿、肢骨等'],['leg + -s → legs','多个腿、支撑脚或行程段']],
 'table legs 桌腿；stretch your legs 活动一下腿、走走；the final legs of a journey 旅程最后几段；cross your legs 交叉双腿。',
 'four legs；the legs of the trip。','行程里的 leg 是一段路线或阶段。身体的腿、家具支撑和行程阶段，分别按相应名词、场景理解。',
 ('The table has four wooden legs.','这张桌子有四条木腿。'),('We travelled by train on the final two legs of the journey.','旅程最后两段我们乘火车。'),sources=['https://en.wiktionary.org/wiki/legs#English','https://en.wiktionary.org/wiki/leg#English'])
W('fingers','英 /ˈfɪŋɡəz/；美 /ˈfɪŋɡərz/','手指〔复数〕；用手指触弄；指认〔finger 的第三人称单数〕',
 '手上细长、能握住和触碰东西的 fingers，转作动词就能说用手指摸、拨弄；在调查语境里还可说指认某人。',
 'finger + -s，词尾读 /z/，ng 后的 /ɡ/ 在常见标准读音中保留。finger 接古英语手指名，现代动词与用手指触碰、指向的动作相连。',
 [['古英语 finger → finger','手指名称'],['名词、动词 finger + -s → fingers','多个手指；单数主语触弄、指认']],
 'cross your fingers 交叉手指祈求好运；run your fingers through your hair 用手指梳过头发；fingers the ribbon 用手指拨弄丝带。',
 'cold fingers；keep your fingers crossed。','日常细分时 fingers 常与 thumb 拇指分开说；较宽的用法也会统指手部各指。句中有后接宾语时，要考虑 fingers 是动词。',
 ('She ran her fingers through her hair.','她用手指梳了梳头发。'),('He fingers the edge of the ribbon while he waits.','等候时，他用手指拨弄着丝带边缘。'),sources=['https://en.wiktionary.org/wiki/fingers#English','https://en.wiktionary.org/wiki/finger#English'])
W('toes','英 /təʊz/；美 /toʊz/','脚趾；鞋头等〔toe 的复数〕；遵守要求〔toes the line 等〕',
 '脚前面一根根脚趾是 toes；鞋子盖住脚趾的前端也可叫 toes。脚趾排到规定线前，又能帮助记 toe the line 遵守要求。',
 'toe 已以 e 结尾，加 s，读 /z/。toe 接古英语 ta、tahe 等脚趾词，现代也作相应动作动词，第三人称同写 toes。',
 [['古英语脚趾词 → toe','脚趾；鞋等相应前端'],['toe + -s → toes','多个脚趾、鞋头；或单数主语的相关动作']],
 'stand on your toes 踮脚；wiggle your toes 动动脚趾；keep someone on their toes 让某人保持警觉；toes the line 遵守要求。',
 'the tips of your toes；pointed toes on shoes。','on your toes 可以是实际踮脚，也可以是保持警觉。toe the line 是按要求行事的固定搭配，学习时连同动词形式一起记。',
 ('She stood on her toes to reach the shelf.','她踮起脚去够架子。'),('The quick changes keep everyone on their toes.','快速的变化让大家都得保持警觉。'),sources=['https://en.wiktionary.org/wiki/toes#English','https://en.wiktionary.org/wiki/toe#English'])
W('knees','/niːz/','膝盖；衣裤的膝部〔knee 的复数〕',
 '两条腿中间弯曲的关节叫 knees；裤子磨损在膝盖对应的那两处，也会说 at the knees。',
 'knee 已有 e，直接加 s，开头 k 不发音，词尾读 /z/。接古英语 cneow 等膝部名称，经中古英语到现代 knee。',
 [['古英语 cneow → knee','膝盖、膝关节'],['knee + -s → knees','多个膝盖；衣裤的对应膝部']],
 'bend your knees 弯膝；on your knees 跪着；weak at the knees 双腿发软；worn at the knees 膝部磨损。',
 'both knees；a notebook on her knees。','on her knees 常说跪姿，也可能在特定场景说东西搁在膝上；要看是谁在什么位置。形容裤子的 knees，是按人体位置称对应衣物部位。',
 ('She rested the notebook on her knees.','她把笔记本放在膝上。'),('His old trousers were worn at the knees.','他的旧裤子膝部磨破了。'),sources=['https://en.wiktionary.org/wiki/knees#English','https://en.wiktionary.org/wiki/knee#English'])
W('nails','/neɪlz/','指甲、趾甲；钉子〔复数〕；钉牢、出色完成等〔nail 的第三人称单数〕',
 '身体末端的硬甲是 nails，拿锤子敲进木头的金属钉也叫 nails。动词可说钉牢，口语又可说某件事做得很到位。',
 'nail + -s，/l/ 后读 /z/。nail 继承古英语 naegl 指甲、钉相关词，早已有钉住的动词材料；现代出色完成义是动词扩展。',
 [['古英语指甲、钉词族 → nail','硬甲；固定用的钉；钉住'],['nail + -s → nails','多个甲、钉子；单数主语钉牢或出色完成']],
 'trim your nails 修剪指甲；paint your nails 涂指甲油；hammer and nails 锤子与钉子；nails the ending 把结尾处理得很出色。',
 'short nails；nails the performance。','指甲和钉子靠对象、动作区分。She nails the final line 常是说最后一句表现得极好，属于口语评价，不必每次找一枚实际的钉子。',
 ('The carpenter put the nails in a small tin.','木匠把钉子放进一个小铁盒。'),('Her nails were painted dark blue.','她的指甲涂成了深蓝色。'),('She nails the final line every time she performs the scene.','每次演这一场戏，她都把最后一句处理得很到位。'),sources=['https://www.merriam-webster.com/dictionary/nail','https://en.wiktionary.org/wiki/nails#English'])
W('thumbs','/θʌmz/','拇指〔复数〕；翻看等〔thumb 的第三人称单数〕',
 '两只拇指是 thumbs；用拇指一页页拨过书本，动词就可以说 thumbs through。b 写着，常见现代读音却不发出来。',
 'thumb + -s，词末 /m/ 后读 /z/。thumb 接古英语 thuma 等拇指词，b 是后来的拼写发展；动词由拇指的动作转用。',
 [['古英语 thuma → thumb','拇指；拼写后来加入 b'],['thumb 名词、动词 + -s → thumbs','多个拇指；单数主语翻看、拨弄等']],
 'thumbs up 竖拇指、赞成；thumbs down 不赞成；be all thumbs 笨手笨脚；thumbs through a book 快速翻书。',
 'twiddle your thumbs；give a thumbs up。','thumbs through 常说粗略翻看，而非逐字细读。be all thumbs 用来形容手上动作不灵巧；这些固定说法要连着理解。',
 ('He gave us a thumbs up after checking the equipment.','检查完设备后，他向我们竖起拇指。'),('She thumbs through the catalogue while she waits.','等候时，她随手翻看商品目录。'),sources=['https://www.merriam-webster.com/dictionary/thumb','https://en.wiktionary.org/wiki/thumbs#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vw',ROOTS,WORDS)
 extend_lessons()
