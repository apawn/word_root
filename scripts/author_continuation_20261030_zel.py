"""Distinct kinds of shining: glitter, glisten, glint, shimmer, glare and blaze."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3936':dict(words=['glitter','glitters','glittered','glittering','glisten','glistens','glistened','glistening','glint','glints','glinted','glinting','glare','glares','glared','glaring'],label='发光远亲的不同画面：glitter、glisten、glint、glare',note='这些词与 glow 在更远层常同列重构发光词族，近源却有各自的古英语、北欧或低地德语材料；同列比较不等于从现代 glow 逐个派生。'),
 'A1697':dict(words=['glitter','glitters','glittered','glittering','shimmer','shimmers','shimmered','shimmering'],label='glitter、shimmer 的旧反复动作构件 -er',note='尾部是旧日耳曼反复、细小动作材料，和现代人物 -er 分用；两词不是把一个现代动作改成发光的人。'),
 'B2971':dict(words=['shine','shimmer','shimmers','shimmered','shimmering'],label='shine 的较远发光词族与 shimmer 的柔光',note='shimmer 接古英语 scimerian，关联 scimian 等发光材料；与 shine 在较远重构层联系，不是现代 shine 直接改字母产生。'),
 'A2238':dict(words=['twinkle','twinkles','twinkled','twinkling','dazzle','dazzles','dazzled'],label='twinkle、dazzle 的旧 -le 材料与常用形式',note='twinkle 有古英语 twinclian 背景，dazzle 与 daze 相关的反复形式相连；现代变化接完整基础词。'),
 'B3737':dict(words=['blaze','blazes','blazed','blazing'],label='blaze 的火光、亮色与开路标记',note='火焰义接古英语相关形式，白斑、树皮路标义经另一近源借入；blaze a trail 的开路意义不从纵火硬推。'),
}
GLITTER=[['中古英语 glideren、gliteren，联系古英语或北欧来源','早期继承、借入路线未定；较远接日耳曼发光材料'],['glitter 动词 → 名词','细碎闪亮 → 闪光、后来命名装饰用闪粉']]
W('glitter','英 /ˈɡlɪtə/；美 /ˈɡlɪtər/','闪闪发亮；闪光；闪粉',
 '许多细小反光点一起跳进眼睛，是 glitter；手工装饰撒下去的那种亮片粉，也按这个效果叫 glitter。',
 '中古英语有 glideren、gliteren，可能承未留记录的古英语形式或借北欧相关词；尾部含旧反复动作材料，名词后由动词发展。',GLITTER,
 'glitter in the light 是在光下细碎闪亮；a tube of glitter 是一管装饰闪粉，物质名通常不按颗粒逐个数。',
 'gold glitter 金色闪粉；glitter in the sun 在太阳下闪亮。',
 'glow 常是持续的光泽，glitter 更容易看见许多亮点反射；glitter 还可指制造这种效果的装饰材料。',
 ('The decorations glitter in the candlelight.','装饰物在烛光下闪闪发亮。'),('She sprinkled glitter over the card.','她在卡片上撒了闪粉。'),sources=['https://www.etymonline.com/word/glitter','https://en.wiktionary.org/wiki/glitter#English'])
W('glitters','英 /ˈɡlɪtəz/；美 /ˈɡlɪtərz/','闪闪发亮〔第三人称单数〕',
 '一件东西上有许多细小亮点反光，说它 glitters。真正发光的也许是太阳、灯，它的表面把光闪给你看。',
 'glitter + -s，末尾读 /z/。基础发光动词已有旧反复动作材料，现代 -s 加在全词最后。',
 GLITTER+[['glitter + -s → glitters','它细碎闪亮']],
 'glitters with jewels 是珠宝在上面闪亮；glitters in the sun 是在阳光下闪光。',
 'glitters in the light 在光下闪亮；glitters like gold 像金子般闪光。',
 '闪粉物质名 glitter 常不可数；这里 glitters 的 -s 最常是动词三单，别看见 s 就当许多闪粉。',
 ('The necklace glitters in the sunlight.','项链在阳光下闪闪发亮。'),('The costume glitters with tiny sequins.','服装上的细小亮片闪闪发光。'),sources=['https://en.wiktionary.org/wiki/glitters#English','https://www.etymonline.com/word/glitter'])
W('glittered','英 /ˈɡlɪtəd/；美 /ˈɡlɪtərd/','闪闪发亮了',
 '刚才首饰、水面、雪地上出现一片细小反光，过去可说 glittered；重点在亮点一起闪的视觉效果。',
 'glitter + 完整 -ed，末尾读 /d/。原有 tt 属于基础拼写，不是这次加 -ed 才双写出来。',
 GLITTER+[['glitter + -ed → glittered','过去发出细碎闪光']],
 'glittered in the light 在光下闪光；eyes glittered 还可形容眼里有鲜明神采、强烈情绪。',
 'glittered with jewels 珠宝闪光；glittered in the sun 在太阳下闪亮。',
 'glittered 讲反光、闪亮现象，sparked 可讲冒火星或引起事情；亮光画面不同。',
 ('The snow glittered in the morning sun.','雪在晨光中闪闪发亮。'),('Her earrings glittered as she turned her head.','她转头时，耳环闪闪发亮。'),sources=['https://en.wiktionary.org/wiki/glittered#English','https://www.etymonline.com/word/glitter'])
W('glittering','英 /ˈɡlɪtərɪŋ/；美 /ˈɡlɪtərɪŋ/','闪闪发亮的；辉煌耀眼的',
 '眼前有亮点不断闪，或一个人的事业光彩照人，都可说 glittering。后者把视觉上的耀眼借给成就、地位。',
 'glitter + -ing；r 后接元音，常见英式也读出 /r/。分词形容词保留细碎亮光，又能比喻辉煌。',
 GLITTER+[['glitter + -ing → glittering','正在闪亮；光彩、事业辉煌的']],
 'a glittering dress 是闪亮礼服，a glittering career 是辉煌事业；两者不都是指衣服上的闪粉。',
 'glittering jewels 闪亮珠宝；a glittering performance 耀眼的表演。',
 'glittering 可强调华丽耀眼，glistening 更容易让人想到湿润、光滑表面的光泽。',
 ('She wore a glittering dress on stage.','她穿着闪亮礼服登台。'),('The award capped a glittering career.','这个奖项为一段辉煌事业添上了收官荣誉。'),sources=['https://en.wiktionary.org/wiki/glittering#English','https://www.etymonline.com/word/glitter'])
GLISTEN=[['古英语 glisnian → 中古英语及现代 glisten','发亮、泛光；较远接日耳曼发光词族'],['现代 glisten 的常见表面画面','湿润、光滑的东西亮亮地反光，眼中泪光也常这样说']]
W('glisten','/ˈɡlɪsən/','泛光、闪亮〔常指湿润或光滑表面〕',
 '雨后的叶片、眼角的泪水、擦亮的金属，表面有一层亮亮的光，可以说 glisten。湿亮感是很有用的记忆画面。',
 '接古英语 glisnian 发亮，较远是日耳曼 glis- 一族。现代拼写保留 t，常见读音却没有 /t/。',GLISTEN,
 'glisten with rain 是因雨水泛亮，eyes glisten with tears 是眼里闪着泪光；不要求所有对象一定是湿的。',
 'glisten in the sun 在太阳下泛光；glisten with moisture 带着湿亮光泽。',
 'glisten、listen 都常不读 t，但一个说亮光、一个说听；不是在 listen 前随意加 g 形成意思。',
 ('The wet leaves glisten in the morning light.','湿叶子在晨光中泛亮。'),('Her eyes began to glisten with tears.','她眼里开始闪着泪光。'),sources=['https://www.etymonline.com/word/glisten','https://en.wiktionary.org/wiki/glisten#English'])
W('glistens','/ˈɡlɪsənz/','泛光、闪亮〔第三人称单数〕',
 '说一块湿石头、一片叶子表面亮亮地反光，单数主语可以用 glistens。',
 'glisten + -s，/n/ 后读 /z/；中间 t 仍保留在拼写里，不因此多读一个 /t/。',
 GLISTEN+[['glisten + -s → glistens','它泛着亮光']],
 'glistens with rain 是表面雨水反光；glistens in the light 是在光里泛亮。',
 'glistens with tears 闪着泪光；glistens after the rain 雨后泛亮。',
 'glitters 更容易想到许多细碎亮点，glistens 更容易想到光滑、湿润表面的一层亮光；这是常见画面，不是硬性分类。',
 ('The stone glistens after the rain.','石头雨后泛着亮光。'),('Her forehead glistens with sweat.','她额头上的汗泛着光。'),sources=['https://en.wiktionary.org/wiki/glistens#English','https://www.etymonline.com/word/glisten'])
W('glistened','/ˈɡlɪsənd/','泛光、闪亮了',
 '刚才雨水、泪水把表面映得亮亮的，是 glistened。把那层光泽放到过去，而不是说突然燃起火花。',
 'glisten + 完整 -ed，末尾 /n/ 后读 /d/。词中 t 仍不发音，原有 n 保留。',
 GLISTEN+[['glisten + -ed → glistened','过去泛光、闪亮']],
 'glistened in the light 是在光里泛亮，glistened with tears 是闪着泪光。',
 'glistened with rain 带着雨水泛亮；glistened softly 柔柔地泛光。',
 'sparked 容易指冒出火星或引起某事，glistened 通常描述表面光泽，不带点燃后续反应的意思。',
 ('The wet pavement glistened under the streetlights.','湿路面在街灯下泛着光。'),('Tears glistened in her eyes.','她眼里闪着泪光。'),sources=['https://en.wiktionary.org/wiki/glistened#English','https://www.etymonline.com/word/glisten'])
W('glistening','/ˈɡlɪsənɪŋ/','泛亮的、带光泽的；正在闪亮',
 '把雨后亮晶晶的叶片、带泪光的眼睛定格看，就是 glistening 的样子。',
 'glisten + -ing，保留全部基础字母，常见读音仍没有 /t/。分词能直接作形容词说明表面状态。',
 GLISTEN+[['glisten + -ing → glistening','正在泛光；有光泽的状态']],
 'glistening eyes 是泛光的眼睛，glistening skin 可说皮肤亮亮的；原因看汗水、泪水、光照等场景。',
 'glistening leaves 泛亮叶片；glistening with moisture 带湿亮光泽的。',
 'shining 更广，glistening 常使人注意到表面那层光泽；两者有交集，不靠字典近义词硬划边界。',
 ('Glistening leaves covered the path after the rain.','雨后泛亮的叶子铺满小路。'),('She looked up with glistening eyes.','她抬起头，眼睛泛着光。'),sources=['https://en.wiktionary.org/wiki/glistening#English','https://www.etymonline.com/word/glisten'])
GLINT=[['中古英语 glenten、glent 与北欧发光材料 → 苏格兰 glint','闪亮、亮光；具体词形有地方延续、变化'],['苏格兰用法进入现代文学英语 glint','一点清亮闪光；眼神中短暂透出的情绪']]
W('glint','/ɡlɪnt/','一闪的亮光；闪出亮光；眼里透出一丝神情',
 '戒指转个角度，突然亮一下；眼睛里忽然露出一点笑意，也像这样一闪。这是 glint 很好记的画面。',
 '现代形式经苏格兰用法，接中古英语 glenten、glent 及北欧发光词族。名词、动词都可用，不是现代 gleam 任意改几个字母。',GLINT,
 'a glint of light 是一点闪光，a glint of amusement 是眼里一丝笑意；后者是神情的比喻。',
 'glint in the sun 在阳光下闪一下；a glint in her eyes 她眼里的一点神采。',
 'gleam 可泛说亮光、反光，glint 更容易强调小而清亮、随着角度闪出来的一点。',
 ('I saw her ring glint in the sun.','我看见她的戒指在阳光下闪了一下。'),('There was a glint of amusement in his eyes.','他眼里有一丝笑意。'),sources=['https://www.etymonline.com/word/glint','https://en.wiktionary.org/wiki/glint#English'])
W('glints','/ɡlɪnts/','几点闪光〔复数〕；闪出亮光〔第三人称单数〕',
 '树叶间、金属边缘露出几点清亮反光，叫 glints；说一件首饰一转就闪，也可以用 glints。',
 'glint + -s，/t/ 后读 /s/。基础词经苏格兰与中古英语相关形式而来，现代名词、动词各自变化。',
 GLINT+[['glint + -s → glints','几处小闪光；它闪亮']],
 'glints of sunlight 是几点阳光，the blade glints 是刀刃闪光；名词和动词可从句子位置分。',
 'silver glints 银色闪光；glints in the light 在光下闪亮。',
 'glints 常是可见的一点点光，glows 作动词常是持续发亮的整体感；都是发光，镜头大小不同。',
 ('Glints of sunlight appeared between the leaves.','叶片间露出几点阳光。'),('The metal buckle glints as he moves.','他一动，金属扣就闪光。'),sources=['https://en.wiktionary.org/wiki/glints#English','https://www.etymonline.com/word/glint'])
W('glinted','/ˈɡlɪntɪd/','闪出亮光了；眼里透出了一丝情绪',
 '刚才戒指、玻璃边闪了一下，或者眼里忽然现出笑意，都可以说 glinted。',
 'glint + 完整 -ed，/t/ 后读 /ɪd/。结尾另有一个轻读音节，t 在基础词里也发音。',
 GLINT+[['glint + -ed → glinted','过去闪亮、透出眼神']],
 'glinted in the sunlight 是在阳光下闪光；eyes glinted with amusement 是眼里闪着笑意。',
 'glinted briefly 短暂闪亮；glinted in the light 在光下闪光。',
 'glinted 保留小而清亮的闪光画面，glared 常更强烈、刺眼，或说怒目看人。',
 ('The ring glinted as she lifted her hand.','她抬手时戒指闪了一下。'),('His eyes glinted with amusement.','他眼里闪着笑意。'),sources=['https://en.wiktionary.org/wiki/glinted#English','https://www.etymonline.com/word/glint'])
W('glinting','/ˈɡlɪntɪŋ/','正在闪光的；闪着小亮点的',
 '银色边缘、玻璃碎片随着光线、角度亮起来，这种闪着小光点的状态是 glinting。',
 'glint + -ing，保留完整词干；/t/ 后接 /ɪŋ/。分词可修饰物体，也可在句中说动作正在发生。',
 GLINT+[['glint + -ing → glinting','闪光的过程、状态']],
 'glinting metal 是闪光金属，glinting in the sun 是正在阳光下反亮。',
 'glinting glass 闪光玻璃；glinting eyes 有一丝神采的眼睛。',
 'glistening 容易想到表面一层亮光，glinting 容易想到角度中跳出的小亮点；具体光照可能同时带出两种感觉。',
 ('We spotted a key glinting in the grass.','我们发现一把钥匙在草里闪光。'),('The river was dotted with glinting patches of sunlight.','河面点缀着一块块闪亮阳光。'),sources=['https://en.wiktionary.org/wiki/glinting#English','https://www.etymonline.com/word/glint'])
SHIMMER=[['古英语 scimerian、scimian 等 → 中古英语 shimeren','发光，带旧反复、细小动作材料'],['英语 shimmer；名词由动词发展','柔和、颤动的光感；与 shine 在更远重构层有联系']]
W('shimmer','英 /ˈʃɪmə/；美 /ˈʃɪmər/','闪着柔光；微微颤动的光泽',
 '丝绸一动，水面微波一晃，光像薄薄一层在颤，这是 shimmer 很直观的感觉。',
 '接古英语 scimerian、中古英语 shimeren，关联旧 scimian 发亮等材料；尾部有旧反复动作构件，名词后来由动词发展。',SHIMMER,
 'a shimmer of light 是一层微颤柔光；silk shimmers 是丝绸泛着会随角度变化的光泽。',
 'a soft shimmer 柔和微光；shimmer in the sunlight 在阳光下泛柔光。',
 'glitter 容易看见细碎亮点，shimmer 更像柔光铺在表面、微微波动；这是感受区别，不是两套物理分类。',
 ('The water began to shimmer in the evening light.','水面在暮光中开始泛起微颤柔光。'),('The fabric had a soft shimmer.','布料带着柔和光泽。'),sources=['https://www.etymonline.com/word/shimmer','https://en.wiktionary.org/wiki/shimmer#English'])
W('shimmers','英 /ˈʃɪməz/；美 /ˈʃɪmərz/','闪着柔光〔第三人称单数〕；微颤光泽〔复数〕',
 '说一片水、一块丝绸表面的光微微晃动，常用 shimmers；几片这样的光感也能用作名词复数。',
 'shimmer + -s，末尾读 /z/。基础动词接古英语的发光、反复动作材料，现代变化不删掉 -er。',
 SHIMMER+[['shimmer + -s → shimmers','它泛柔光；数处微颤光泽']],
 'shimmers in the light 是在光下泛柔光；the lake shimmers 常是水面光影轻轻波动。',
 'shimmers softly 柔和泛光；shimmers in the heat 热气中呈现颤动光影。',
 'shimmers 可是物体表面光泽，也能是热气造成的视觉晃动；不一定是物体自身发光。',
 ('The silk shimmers when she moves.','她一动，丝绸就泛起柔光。'),('The sea shimmers in the afternoon sun.','海面在午后阳光下泛着微颤柔光。'),sources=['https://en.wiktionary.org/wiki/shimmers#English','https://www.etymonline.com/word/shimmer'])
W('shimmered','英 /ˈʃɪməd/；美 /ˈʃɪmərd/','泛起柔光、微微闪亮了',
 '刚才湖面、衣料上有一层波动的光，或热气里的远处景物看着轻轻晃动，都可说 shimmered。',
 'shimmer + 完整 -ed，词尾读 /d/。两个 m 已在 shimmer 的基础拼写中，不是这次过去式才双写。',
 SHIMMER+[['shimmer + -ed → shimmered','过去泛柔光、呈现微颤光影']],
 'shimmered in the sun 是在阳光下微闪；shimmered in the heat 可说热气中影像微颤。',
 'shimmered softly 柔和泛光；shimmered on the water 在水面微闪。',
 'glinted 更像一点清亮反光，shimmered 更像一层柔光波动；观察尺度不同，实际场景也可重叠。',
 ('The lake shimmered in the moonlight.','湖面在月光下泛着微颤柔光。'),('The road shimmered in the afternoon heat.','道路在午后热气中看起来微微晃动。'),sources=['https://en.wiktionary.org/wiki/shimmered#English','https://www.etymonline.com/word/shimmer'])
W('shimmering','/ˈʃɪmərɪŋ/','泛着柔光的；光影微颤的',
 '把柔光在水面、衣料上轻轻晃的样子定格，就是 shimmering；眼睛感到的是薄而流动的一层光。',
 'shimmer + -ing，r 后接元音，常见英式也读出 /r/。分词形容词可直接放在物体前描写光泽。',
 SHIMMER+[['shimmer + -ing → shimmering','正在泛柔光；微颤闪亮的状态']],
 'a shimmering dress 是泛柔光的礼服，shimmering water 是光影轻动的水面。',
 'shimmering silk 泛柔光丝绸；a shimmering reflection 微颤的倒影。',
 'glowing 常让人想到持续暖光，shimmering 更突出表面光影的轻微颤动；可以用具体画面选词。',
 ('She wore a dress made of shimmering silk.','她穿着泛柔光的丝绸礼服。'),('We watched the shimmering reflections on the lake.','我们看着湖面上微微颤动的倒影。'),sources=['https://en.wiktionary.org/wiki/shimmering#English','https://www.etymonline.com/word/shimmer'])
TWINKLE=[['古英语 twinclian → 中古英语 twinclen → twinkle','反复眨、闪；旧 -le 材料与细小反复动作对应'],['现代 twinkle','星光时亮时暗；眼中闪现神采；相应名词用途']]
W('twinkles','/ˈtwɪŋkəlz/','闪烁〔第三人称单数〕；点点闪光〔复数〕',
 '远处一颗星像轻轻眨眼，时亮时暗，可以说 twinkles；眼里一点活泼笑意，也像小光点这样跳出来。',
 'twinkle + -s，保留词尾 e，末尾读 /z/。基础词承古英语反复眨、闪的动作，现代名词、动词都常见。',
 TWINKLE+[['twinkle + -s → twinkles','它闪烁；几处小闪光']],
 'a star twinkles 是一颗星闪烁；twinkles in his eyes 可说眼里点点神采。',
 'twinkles in the sky 在天空闪烁；twinkles with amusement 眼中闪着笑意。',
 'twinkles 容易想到时亮时暗的小光点，glows 常是持续光泽；先凭画面理解频率感。',
 ('A single star twinkles above the roof.','一颗星在屋顶上方闪烁。'),('His eyes had little twinkles of amusement.','他眼里闪着点点笑意。'),sources=['https://en.wiktionary.org/wiki/twinkles#English','https://en.wiktionary.org/wiki/twinkle#English'])
W('twinkled','/ˈtwɪŋkəld/','闪烁了；眼里闪现了神采',
 '刚才星光一亮一暗，或者一个人眼里忽然有了调皮笑意，过去就说 twinkled。',
 'twinkle 去末尾 e，加完整 -ed；/l/ 后读 /d/。中间 nk 对应 /ŋk/，保留基础词的声音。',
 TWINKLE+[['twinkle + -ed → twinkled〔去 e〕','过去闪烁、透出活泼神情']],
 'twinkled above us 是在上方闪烁；eyes twinkled with mischief 是眼里闪着调皮劲。',
 'twinkled in the dark 在暗处闪烁；twinkled with delight 闪着喜悦。',
 '眼睛 twinkled 常是神情带着活泼、愉快，glared 常是生气瞪人；两种眼神画面很不同。',
 ('The stars twinkled above the quiet village.','星星在安静村庄上方闪烁。'),('Her eyes twinkled when she heard the joke.','听到笑话时，她眼里闪着笑意。'),sources=['https://en.wiktionary.org/wiki/twinkled#English','https://en.wiktionary.org/wiki/twinkle#English'])
W('twinkling','/ˈtwɪŋklɪŋ/','闪烁的；闪烁；一眨眼的短暂时间〔特定短语〕',
 '小亮点像眨眼一样一明一暗，是 twinkling；in the twinkling of an eye 则借眨眼说快得一瞬间。',
 'twinkle 去末尾 e，加完整 -ing。旧动词已有反复眨、闪材料，分词还可形成描写星光、眼神的形容词。',
 TWINKLE+[['twinkle + -ing → twinkling〔去 e〕','闪烁过程、状态；眨眼的瞬间']],
 'twinkling stars 是闪烁星星；twinkling eyes 常是有笑意、活力的眼睛。',
 'twinkling lights 闪烁小灯；in the twinkling of an eye 转眼间。',
 'twinkling 描写亮点时明时暗，sparkling water 在饮料里常说有气泡；相近的亮光字不能在每个固定搭配互换。',
 ('Twinkling lights decorated the trees.','闪烁小灯装点着树木。'),('The children disappeared in the twinkling of an eye.','孩子们一眨眼就跑没影了。'),sources=['https://en.wiktionary.org/wiki/twinkling#English','https://en.wiktionary.org/wiki/twinkle#English'])
GLARE=[['中古英语 glaren 与荷兰语、低地德语相关发亮词','早期继承、借入路径有不同分析；较远接发光词族'],['glare 的亮光与眼神用途','强烈发亮、刺眼 → 凶狠直视；名词也有强光、怒视用途']]
W('glare','英 /ɡleə/；美 /ɡler/','刺眼强光；怒视、瞪视；发强光',
 '强光直逼眼睛，是 glare；一个人生气地盯过来，也像目光直逼你，可以说 glare at you。',
 '接中古英语 glaren，与低地德语、荷兰语发亮词相连，早期路线有不同分析。先有发亮义，英语后来也用来表示凶狠盯视。',GLARE,
 'the glare of the sun 是太阳刺眼的光，give someone a glare 是瞪某人一眼，glare at someone 是怒目盯着。',
 'reduce glare 减少眩光；glare angrily 愤怒地瞪视。',
 'stare 泛说盯着看，glare 通常带生气、不满；bright light 不一定刺眼，glare 更强调强烈逼眼。',
 ('The glare from the windows made the screen hard to see.','窗户反来的强光让屏幕难以看清。'),('She began to glare at him across the table.','她开始隔着桌子怒目盯着他。'),sources=['https://www.etymonline.com/word/glare','https://en.wiktionary.org/wiki/glare#English'])
W('glares','英 /ɡleəz/；美 /ɡlerz/','怒视、刺眼发亮〔第三人称单数〕；怒目、强光〔复数〕',
 '说一个人生气盯着看，可以用 glares；他的一次次怒目也能数成 glares。强光义仍要靠光线场景选出。',
 'glare + -s，保留词尾 e，末尾读 /z/。发亮与凶狠直视的基础词各有名词、动词用途。',
 GLARE+[['glare + -s → glares','他、她怒视；几次怒视、强光等']],
 'glares at someone 是瞪某人，exchange glares 是互相瞪眼；直接对象常由 at 引出。',
 'glares angrily 愤怒地瞪；hostile glares 敌意目光。',
 'glances 常是快速看一眼，glares 常是带怒气地直盯；同样是眼神，情绪、持续方式不同。',
 ('He glares at anyone who interrupts him.','谁打断他，他就瞪谁。'),('The two players exchanged angry glares.','两位球员互相怒目而视。'),sources=['https://en.wiktionary.org/wiki/glares#English','https://www.etymonline.com/word/glare'])
W('glared','英 /ɡleəd/；美 /ɡlerd/','怒视了；刺眼地照耀了',
 '刚才有人生气地一直盯着你，是 glared；强光逼眼地照着，也可用这个过去式。',
 'glare 去末尾 e，加完整 -ed；末尾读 /d/，不另加 /ɪd/ 音节。',
 GLARE+[['glare + -ed → glared〔去 e〕','过去凶狠直视、强烈发亮']],
 'glared at me 是怒视我；the sun glared down 是太阳刺眼地照下来。',
 'glared across the table 隔桌怒视；glared in the sunlight 在阳光下刺眼发亮。',
 'looked 只说看，glared 加上不满、怒气；在光线场景则强调强烈刺眼。',
 ('She glared at him without saying a word.','她一句话没说，只怒视着他。'),('The sun glared down on the empty square.','太阳刺眼地照着空广场。'),sources=['https://en.wiktionary.org/wiki/glared#English','https://www.etymonline.com/word/glare'])
W('glaring','英 /ˈɡleərɪŋ/；美 /ˈɡlerɪŋ/','刺眼的；明显得无法忽视的；正在怒视',
 '光强到躲不开，是 glaring light；错误大到一眼就看见，是 a glaring error。两者都很显眼，后者常带批评。',
 'glare 去末尾 e，加完整 -ing。分词形容词从强烈、直逼注意的画面发展出显眼、明显的用法。',
 GLARE+[['glare + -ing → glaring〔去 e〕','强光、怒目状态；后来形容极明显的错误等']],
 'glaring sunlight 是刺眼阳光，a glaring omission 是明显遗漏；be glaring at someone 是正在怒视。',
 'a glaring error 明显错误；a glaring difference 明显差别。',
 'obvious 可中性说明显，glaring 在 error、omission 等搭配里常强调严重得很难忽略。',
 ('The report contains a glaring error.','报告里有一个明显错误。'),('He was glaring at me from across the room.','他正从房间另一头怒视着我。'),sources=['https://en.wiktionary.org/wiki/glaring#English','https://www.etymonline.com/word/glare'])
DAZZLE=[['daze 等发懵材料 + 旧反复构件 → dazzle','使一时难以看清、辨清'],['现代 dazzle 的具体与比喻义','强光晃眼；才华、美貌、表现令人惊叹']]
W('dazzles','/ˈdæzəlz/','晃眼；使惊艳、使赞叹〔第三人称单数〕',
 '光太亮，把眼睛一下晃住；表现太出色，把观众一下镇住。dazzles 用同样强烈的印象连接两种场景。',
 'dazzle + -s，保留末尾 e，/l/ 后读 /z/。基础 dazzle 与 daze、旧反复动作构件相连。',
 DAZZLE+[['dazzle + -s → dazzles','它晃眼；他、她令人惊艳']],
 'dazzles the audience 是让观众惊叹，dazzles with skill 是凭技巧使人赞叹。',
 'dazzles the eye 晃眼；dazzles the crowd 使人群惊叹。',
 'impresses 可泛说给人深刻印象，dazzles 更强烈、耀眼，像一时看得愣住。',
 ('The reflected sunlight dazzles my eyes.','反射的阳光晃得我眼花。'),('She dazzles the audience with her footwork.','她的步法让观众惊叹。'),sources=['https://en.wiktionary.org/wiki/dazzles#English','https://en.wiktionary.org/wiki/dazzle#English'])
W('dazzled','/ˈdæzəld/','被强光晃了眼；被惊艳了、赞叹不已的',
 '忽然对上强光，眼前一晃，是 dazzled；遇到特别出色的人、表演，一下看得赞叹，也可这样说。',
 'dazzle 去末尾 e，加完整 -ed；/l/ 后读 /d/，双 z 已属于基础词拼写。',
 DAZZLE+[['dazzle + -ed → dazzled〔去 e〕','过去晃眼、使赞叹；相应受到强烈印象的状态']],
 'dazzled by the lights 是被灯晃眼，dazzled by her performance 是被她的表演惊艳。',
 'dazzled by brilliance 被才华折服；dazzled the audience 让观众赞叹了。',
 'dazzled 说受到强烈印象的人，dazzling 常修饰造成这种效果的光、人物或表演。',
 ('I was dazzled by the bright lights.','我被强光晃了眼。'),('We were dazzled by her performance.','她的表演让我们赞叹不已。'),sources=['https://en.wiktionary.org/wiki/dazzled#English','https://en.wiktionary.org/wiki/dazzle#English'])
BLAZE=[['火焰支：古英语 blæse 等 → blaze','明亮火焰、亮色及燃烧动作'],['白斑、路标支：通常联系古诺斯 blesi，也有荷兰、低地德语来源说','显眼白斑、树皮记号 → 标路、开辟道路；近源与火焰支不同']]
W('blazes','/ˈbleɪzɪz/','火焰、白斑或路标〔复数〕；熊熊燃烧、开路〔第三人称单数〕',
 '火焰很亮，是一支 blaze；树干上显眼的白色路标，是另一近源支。blazes 的拼写把这些用法聚到一起。',
 'blaze + -s，保留 e，/z/ 后另读 /ɪz/。火焰义接古英语，白斑、标路义经另一日耳曼借词路线，不把标路解释成放火烧路。',
 BLAZE+[['blaze + -s → blazes','多团火焰、多个白斑路标；它燃烧、标路']],
 'a fire blazes 是火熊熊烧；white blazes on trees 是树上的白色标记，帮助人沿路线行走。',
 'blazes brightly 明亮燃烧；trail blazes 路线标记。',
 'blaze a trail 的开辟新路义接做标记、引路的画面；与明火燃烧的同形词分开理解。',
 ('The fire blazes in the fireplace.','壁炉里的火熊熊燃烧。'),('White blazes marked the trail through the forest.','白色标记标出了穿过森林的路线。'),sources=['https://en.wiktionary.org/wiki/blazes#English','https://en.wiktionary.org/wiki/blaze#English','https://www.etymonline.com/word/blaze'])
W('blazed','/bleɪzd/','熊熊燃烧、强烈照耀了；开辟、标出了道路',
 '太阳炽烈地照过来，是 blazed；有人先走出、标明一条路，带后人前进，也是另支 blazed。',
 'blaze 去末尾 e，加完整 -ed；/z/ 后读 /d/。火光支与白斑、标路支各自按同样规则变化。',
 BLAZE+[['blaze + -ed → blazed〔去 e〕','过去燃烧、照耀；过去标路、开辟']],
 'the sun blazed 是太阳强烈照耀；blazed a trail 是开辟、标出路线，也可比喻开创先河。',
 'blazed all night 烧了一整夜；blazed a trail for others 为后来者开路。',
 'blazed a trail 突出先走、引导后人，followed a trail 是循已有道路走，方向不同。',
 ('The sun blazed down on the open field.','太阳炽烈地照着空旷田野。'),('She blazed a trail for young researchers.','她为年轻研究者开辟了新路。'),sources=['https://en.wiktionary.org/wiki/blazed#English','https://en.wiktionary.org/wiki/blaze#English','https://www.etymonline.com/word/blaze'])
W('blazing','/ˈbleɪzɪŋ/','熊熊燃烧、炽烈的；正在开辟道路',
 '大火燃得旺，太阳热得强，都是 blazing 的强烈亮热感；blazing a trail 则转到开路那条标记支线。',
 'blaze 去末尾 e，加完整 -ing。动词进行、分词形容词同形；用 trail 等对象区分不同近源支。',
 BLAZE+[['blaze + -ing → blazing〔去 e〕','正在燃烧、强烈照耀；正在标路、开创新路']],
 'a blazing fire 是熊熊大火，blazing sunshine 是炽烈阳光，blazing a trail 是开辟新路。',
 'blazing heat 炽热；a blazing fire 熊熊大火。',
 'glowing coals 常是无明显火焰的红亮炭，blazing fire 更突出火焰旺盛；两个画面不同。',
 ('We sat beside a blazing fire.','我们坐在熊熊大火旁。'),('They are blazing a trail in digital art.','他们正在数字艺术领域开辟新路。'),sources=['https://en.wiktionary.org/wiki/blazing#English','https://en.wiktionary.org/wiki/blaze#English','https://www.etymonline.com/word/blaze'])

def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_zel',ROOTS,WORDS)
    extend_lessons()
