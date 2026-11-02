"""Wavering lights, blinking, outward rays and glossy or showy appearances."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1697':dict(words=['flicker','flickers','flickered','flickering'],label='flicker 的旧反复动作 -er 与明灭不定',note='古英语 flicorian 先有轻快振翅的动作画面，后来描述摇曳亮光；这里 -er 不表示做事的人。'),
 'B4361':dict(words=['blink','blinks','blinked','blinking'],label='blink 的眼皮开合与灯光闪灭',note='中古英语相关词接日耳曼闪光材料，早期路线有讨论；眼皮短暂开合、灯光短暂明灭是现代常见分支。'),
 'B3142':dict(words=['flash','flashes','flashed','flashy','flashier','flashiest'],label='flash 的突现、闪光与 flashy 的浮华程度',note='短暂出现的强光走向显眼外观；flashier、flashiest 形容更、最浮华，不要求真的安装闪灯。'),
 'B3936':dict(words=['glower','glowers','glowered','glowering','glitter','glittery','glitz','glitzy'],label='发光词族的目光、闪粉性质与华丽外观',note='glower 早期有发亮、瞪视材料，具体北欧或荷兰来源有不同分析；glitzy 接意第绪语发光材料，英语名词 glitz 有从它逆构的分析。'),
 'C1198':dict(words=['radiant','radiantly','radiate','radiates','radiated','radiating','radiator','radiators'],label='radius 的辐条、光线与向外散发',note='radiant、radiate 各有拉丁借词路线；现代副词、动词变化接已固定的基础词，radiators 是散热装置名称的复数。'),
 'A1761':dict(words=['radiator','radiators'],label='radiator → radiators：向外放热的装置',note='-or 命名散发、散热的设备，房间供暖与汽车冷却里的用途分别按系统理解。'),
 'A1699':dict(words=['flashy','flashier','flashiest','glitter','glittery','shiny','shinier','shiniest','glossy','glossier','glossiest'],label='亮光性质词：-y 与比较、最高程度',note='glitter + -y 成 glittery；shiny、glossy、flashy 去 y 后接完整 -er、-est；光泽、浮华的具体含义不同。'),
 'B2971':dict(words=['shiny','shinier','shiniest'],label='shine → shiny → shinier、shiniest',note='shine 去 e 接 -y 成 shiny，比较、最高级再在形容词上变，不把整个 shiny 一次拆成不相干词尾。'),
 'A1823':dict(words=['gleeful','gleefully'],label='glee → gleeful → gleefully：喜悦的方式',note='gleeful 加完整 -ly，形成表示欢喜表现方式的副词，两个 l 分属 ful、ly。'),
}
FLICKER=[['古英语 flicorian → 中古英语 flikeren','鸟翼轻快反复动作，带旧日耳曼反复构件'],['英语 flicker 的光与名词用途','摇曳、明灭的光 → 短暂一闪、情绪迹象']]
W('flicker','英 /ˈflɪkə/；美 /ˈflɪkər/','摇曳、明灭不定；短暂一闪、微弱迹象',
 '蜡烛受风，光忽强忽弱，好像在轻轻抖，就是 flicker。一个表情只露一下，也像一丝光闪过。',
 '接古英语 flicorian 鸟翼轻快动作、中古英语 flikeren，含旧反复动作材料；摇曳发光义后来发展，名词由动词形成。',FLICKER,
 'a flicker of hope 是一丝短暂希望；lights flicker 是灯光明灭不稳，不必每次彻底熄灭。',
 'a flicker of a smile 一闪而过的笑意；flicker in the wind 在风中摇曳。',
 'glow 常是持续光泽，flicker 强调不稳定地变亮、变暗；画面里有轻微反复变化。',
 ('The candle began to flicker in the draught.','蜡烛在气流中开始摇曳。'),('I noticed a flicker of a smile on her face.','我注意到她脸上一闪而过的笑意。'),sources=['https://www.etymonline.com/word/flicker','https://en.wiktionary.org/wiki/flicker#English'])
W('flickers','英 /ˈflɪkəz/；美 /ˈflɪkərz/','明灭、摇曳〔第三人称单数〕；短暂闪光、迹象〔复数〕',
 '一盏灯亮度轻轻跳动，是 flickers；几丝短暂露头的希望，也可以叫 flickers of hope。',
 'flicker + -s，末尾读 /z/。旧词的反复动作形象保留，现代名词、动词分别加尾。',
 FLICKER+[['flicker + -s → flickers','它摇曳；几丝闪光、迹象']],
 'the screen flickers 是屏幕闪烁，flickers of recognition 是刚刚认出来的一点神情。',
 'flickers on and off 忽明忽暗；faint flickers 微弱闪光。',
 'flickers 可以不规则、像灯接触不稳，blinks 则常描述一次次短暂开关；二者仍可重叠。',
 ('The old lamp flickers whenever the door closes.','每当门关上，那盏旧灯就闪几下。'),('There were faint flickers of hope in his words.','他的话里透出几丝微弱希望。'),sources=['https://en.wiktionary.org/wiki/flickers#English','https://www.etymonline.com/word/flicker'])
W('flickered','英 /ˈflɪkəd/；美 /ˈflɪkərd/','摇曳、闪烁了；短暂显现了',
 '刚才灯光晃了几下，或者某种情绪从脸上短暂掠过，都可以说 flickered。',
 'flicker + 完整 -ed，词尾读 /d/。基础词 -er 保留，不先当作人物后缀删掉。',
 FLICKER+[['flicker + -ed → flickered','过去明灭不稳、短暂显现']],
 'flickered across her face 是神情在脸上一闪而过；flickered in the wind 是光在风中摇曳。',
 'flickered briefly 短暂闪动；flickered out 闪几下后熄灭。',
 'flashed 可以是明亮地突然一闪，flickered 更突出微弱、不稳的反复变化。',
 ('The candle flickered in the breeze.','蜡烛在微风中摇曳。'),('A look of surprise flickered across her face.','她脸上一闪而过惊讶的神情。'),sources=['https://en.wiktionary.org/wiki/flickered#English','https://www.etymonline.com/word/flicker'])
W('flickering','/ˈflɪkərɪŋ/','摇曳、明灭不定的；短暂闪现的',
 '火光、屏幕亮度正在轻轻跳动，像不断小幅开合，就是 flickering 的状态。',
 'flicker + -ing；r 后接元音，常见英式也读出 /r/。分词可形容光源，也可直接讲动作在进行。',
 FLICKER+[['flicker + -ing → flickering','明灭、摇曳的过程、状态']],
 'flickering candlelight 是摇曳烛光，a flickering screen 是闪烁屏幕；原因随具体设备、环境而异。',
 'flickering flames 摇曳火焰；flickering lights 忽明忽暗的灯。',
 'shimmering 常让人看到表面柔光微颤，flickering 常把注意力放到光本身忽强忽弱。',
 ('We ate by the flickering candlelight.','我们在摇曳烛光中吃饭。'),('The image kept flickering on the old screen.','图像在旧屏幕上不断闪烁。'),sources=['https://en.wiktionary.org/wiki/flickering#English','https://www.etymonline.com/word/flicker'])
BLINK=[['中古英语 blynken、blenken 与日耳曼闪光材料','早期继承、借入路线有不同分析；不认定重构古英语形式是存世拼写'],['英语 blink','眼皮短暂开合；光源明灭；也可比喻迟疑、退缩']]
W('blinks','/blɪŋks/','眨眼、闪烁〔第三人称单数〕；眨眼动作〔复数〕',
 '眼皮短暂合上又打开，是 blinks；灯、光标短暂灭掉又亮起，也像这样开合。',
 'blink + -s，/k/ 后读 /s/。基础词接中古英语与更早日耳曼闪光材料，现代眼睛、灯光用途并行。',
 BLINK+[['blink + -s → blinks','他、她眨眼；它闪烁；几次眨眼']],
 'she blinks 是她眨眼；the cursor blinks 是光标闪烁，一个关注眼皮，一个关注光点明灭。',
 'blinks rapidly 快速眨眼；blinks on and off 反复亮灭。',
 'blink 的开合可以自然发生，也可以描述灯的信号动作；它不必带 flicker 那种不稳定、摇曳感。',
 ('She blinks whenever the camera flashes.','相机每次闪光，她都会眨眼。'),('The cursor blinks at the end of the line.','光标在行末闪烁。'),sources=['https://en.wiktionary.org/wiki/blinks#English','https://en.wiktionary.org/wiki/blink#English'])
W('blinked','/blɪŋkt/','眨眼、闪烁了；迟疑、退缩了〔比喻〕',
 '刚才眼皮闭开一下，叫 blinked；面对压力若连眼都没眨，也可比喻毫不迟疑、没有退缩。',
 'blink + 完整 -ed，/k/ 后读 /t/；词末 /ŋkt/ 连读，不多添一个 /ɪd/ 音节。',
 BLINK+[['blink + -ed → blinked','过去眨眼、短暂明灭；比喻迟疑、退缩']],
 'blinked in surprise 是惊讶地眨眼；never blinked 可说面对某事一点不退缩，语气要看场景。',
 'blinked twice 眨了两下眼；blinked at the light 被亮光照得眨眼。',
 'blinked 是短暂眼皮开合，stared 是持续盯着；did not blink 还可有毫不迟疑的比喻。',
 ('He blinked twice in surprise.','他惊讶地眨了两下眼。'),('The small light blinked once and went dark.','小灯闪了一下就暗了。'),sources=['https://en.wiktionary.org/wiki/blinked#English','https://en.wiktionary.org/wiki/blink#English'])
W('blinking','/ˈblɪŋkɪŋ/','正在眨眼；闪烁的、反复明灭的',
 '一双眼睛正在开合，或一个提示灯正在一亮一灭，都可以叫 blinking。',
 'blink + -ing，保留基础拼写；分词既可讲动作，也能直接修饰 light、cursor 等光点对象。',
 BLINK+[['blink + -ing → blinking','眼皮开合的进行；反复亮灭的状态']],
 'a blinking light 是闪烁灯，keep blinking 是不停眨眼；后者看主语是不是人。',
 'blinking cursor 闪烁光标；blinking rapidly 快速眨眼。',
 'glowing 是持续亮着的感觉，blinking 是一亮一灭；在描述指示灯时差别尤其直观。',
 ('She stood blinking in the bright sunlight.','她站在明亮阳光里眨着眼。'),('A blinking light marked the entrance.','一盏闪烁灯标示着入口。'),sources=['https://en.wiktionary.org/wiki/blinking#English','https://en.wiktionary.org/wiki/blink#English'])
FLASH=[['中古英语 flashen、flasken 等','喷溅、突然涌动等旧用法，有拟声、北欧联系等分析'],['英语 flash 的后续用途','短暂强光；消息、想法、表情突然出现；迅速展示']]
W('flashes','/ˈflæʃɪz/','闪光、短暂闪现〔复数〕；闪现、迅速展示〔第三人称单数〕',
 '相机忽然亮一下，是 flashes；脑中想法突然冒出来，也像一闪。重心在短、快、突然。',
 'flash + -es，/ʃ/ 后读 /ɪz/。基础词旧有突涌、喷溅画面，后来用于光、消息、表情等突然出现。',
 FLASH+[['flash + -es → flashes','几次闪光、闪现；它闪出、迅速展示']],
 'flashes of lightning 是一道道闪电，flashes of inspiration 是一闪而过的灵感。',
 'camera flashes 相机闪光；flashes a smile 迅速露出笑容。',
 'flashes 常强调突然一亮、一次短暂出现；flickers 更容易是轻微、不稳定的反复变化。',
 ('Flashes of lightning lit the clouds.','一道道闪电照亮了云。'),('She flashes a smile whenever we meet.','我们每次见面，她都会迅速露出笑容。'),sources=['https://en.wiktionary.org/wiki/flashes#English','https://www.etymonline.com/word/flash'])
W('flashed','/flæʃt/','闪光、闪现了；迅速亮出、展示了',
 '光突然亮一下，念头突然掠过，或者有人快速亮出证件，都可以说 flashed。对象不同，短暂、迅速的感觉一样。',
 'flash + 完整 -ed，/ʃ/ 后读 /t/；末尾连成 /ʃt/，不多一个音节。',
 FLASH+[['flash + -ed → flashed','过去闪现、迅速展示']],
 'flashed through my mind 是从脑中一闪而过，flashed a smile 是快速露出一个笑。',
 'flashed briefly 短暂闪现；flashed an ID 快速亮出证件。',
 'showed 可以慢慢给人看，flashed 常带一晃而过的速度；亮出后很快收起也能这样说。',
 ('A warning flashed on the screen.','屏幕上闪现一条提示。'),('The thought flashed through my mind.','这个念头从我脑中一闪而过。'),sources=['https://en.wiktionary.org/wiki/flashed#English','https://www.etymonline.com/word/flash'])
FLASHY=FLASH+[['flash + -y → flashy','闪亮、炫示的画面 → 显眼浮华的性质']]
W('flashier','/ˈflæʃiə/〔英〕；/ˈflæʃiər/〔美〕','更显眼、更华丽炫目的',
 '两套衣服、两种包装相比，一种更抢眼、更像要把注意力拉到自己身上，就是 flashier。',
 'flashy 去 y，加完整比较级 -er → flashier；基础 flash + -y 给出显眼、炫示性质。',
 FLASHY+[['flashy + -er → flashier〔y 改 i〕','更浮华、炫目']],
 'a flashier jacket 是更惹眼的夹克；flashier design 常说设计更强调外表吸引力。',
 'look flashier 显得更张扬；a flashier version 更花哨的版本。',
 'brighter 更亮、更鲜艳，flashier 常还带炫示、浮华的评价；不是单纯测亮度。',
 ('He chose a flashier jacket for the performance.','他为演出选了一件更抢眼的夹克。'),('The new packaging is flashier than the old design.','新包装比旧设计更花哨。'),sources=['https://en.wiktionary.org/wiki/flashier#English','https://en.wiktionary.org/wiki/flashy#English'])
W('flashiest','/ˈflæʃiɪst/','最显眼、最华丽炫目的',
 '一排车、一组衣服里，最抢眼、最有炫示感的那一个，可以叫 flashiest。',
 'flashy 去 y，加完整最高级 -est → flashiest。-est 比较整个显眼、浮华性质，不是只数闪光次数。',
 FLASHY+[['flashy + -est → flashiest〔y 改 i〕','比较范围中最抢眼、最浮华']],
 'the flashiest outfit 是最张扬的穿搭；the flashiest design 是最花哨设计，常有说话人的审美判断。',
 'the flashiest car 最抢眼的车；the flashiest costume 最华丽惹眼的演出服。',
 'flashiest 未必是 best；这个词强调外表抢眼程度，不替作品、东西的整体质量排名。',
 ('She wore the flashiest costume in the show.','她穿了演出中最华丽抢眼的服装。'),('The flashiest design was not the one we chose.','最花哨的设计并不是我们选中的那款。'),sources=['https://en.wiktionary.org/wiki/flashiest#English','https://en.wiktionary.org/wiki/flashy#English'])
GLOWER=[['中古英语发亮、直视用法；可能有北欧或荷兰语来源','与日耳曼 glo- 发光材料相关，具体近源未定'],['glower 的现代常用义；拼写受 glow 影响','阴沉、威胁地盯视；名词由动词发展']]
W('glower','英 /ˈɡlaʊə/；美 /ˈɡlaʊər/','阴沉怒视；阴沉的怒目',
 '脸沉下来，眼睛死死盯着，像把不满压在目光里，这就是 glower。',
 '可能经北欧相关词或联系荷兰语 gluren 一族，较远与 glow 同族，拼写也受 glow 影响。常见读音用 /aʊ/，不能只照 glow 的元音读。',GLOWER,
 'glower at someone 是阴沉地怒视某人；a glower 是那种带威胁、不满的目光。',
 'glower silently 默默怒视；give someone a glower 怒视某人一眼。',
 'glare 也常指刺眼强光，glower 的现代常见用法集中在不满、威胁的眼神；比 ordinary look 情绪重。',
 ('He continued to glower at me from his chair.','他继续坐在椅子上阴沉地怒视我。'),('She answered the question with a glower.','她用一记阴沉目光回应了问题。'),sources=['https://www.etymonline.com/word/glower','https://en.wiktionary.org/wiki/glower#English'])
W('glowers','英 /ˈɡlaʊəz/；美 /ˈɡlaʊərz/','阴沉怒视〔第三人称单数〕；怒目〔复数〕',
 '说一个人沉着脸一直盯别人，用 glowers；把几次这种目光分别拿来数，也能用同形名词。',
 'glower + -s，词末读 /z/。基础词的现代阴沉怒视义与较早的发亮、直视词族相连。',
 GLOWER+[['glower + -s → glowers','他、她怒视；几次怒目']],
 'glowers at us 是朝我们阴沉怒视；angry glowers 是充满怒意的目光。',
 'glowers from the doorway 从门口阴沉盯视；hostile glowers 敌意目光。',
 'beams 是满脸笑容，glowers 是脸色阴沉地盯；眼神描写里情绪方向相反。',
 ('He glowers at anyone who moves his papers.','谁动他的文件，他就阴沉地瞪谁。'),('She ignored the glowers from the other side of the room.','她没理会房间另一头投来的阴沉目光。'),sources=['https://en.wiktionary.org/wiki/glowers#English','https://www.etymonline.com/word/glower'])
W('glowered','英 /ˈɡlaʊəd/；美 /ˈɡlaʊərd/','阴沉怒视了',
 '刚才那个人沉着脸、满眼不快地盯过来，可以说 glowered。动作发生过，阴沉情绪仍由基础词带出。',
 'glower + 完整 -ed，末尾读 /d/；不删掉基础词里的 -er，也不把元音改成 glow 的读法。',
 GLOWER+[['glower + -ed → glowered','过去阴沉、威胁地盯视']],
 'glowered at me 是朝我阴沉瞪视；glowered from his seat 是坐在位置上满脸怒气地盯着。',
 'glowered silently 默默怒视；glowered across the table 隔桌怒视。',
 'frowned 常突出皱眉，glowered 常突出阴沉的目光、表情；两种反应可以同时发生。',
 ('He glowered at the pile of unfinished work.','他阴沉地盯着那堆没做完的工作。'),('She glowered across the table but said nothing.','她隔着桌子阴沉瞪视，却什么也没说。'),sources=['https://en.wiktionary.org/wiki/glowered#English','https://www.etymonline.com/word/glower'])
W('glowering','/ˈɡlaʊərɪŋ/','正在阴沉怒视；满脸怒意的',
 '镜头定在一张沉下来的脸上，眼睛正狠狠盯着，就是 glowering。表情本身在传递不满。',
 'glower + -ing，r 后接元音，常见英式也读 /r/。分词可以说明正在怒视，也可作形容词描写人、神情。',
 GLOWER+[['glower + -ing → glowering','阴沉怒视的动作、状态']],
 'a glowering expression 是阴沉怒容；glowering at someone 是正在怒视某人。',
 'a glowering face 阴沉的脸；glowering in silence 默默怒视。',
 'glowing 是光泽、喜悦或赞许，glowering 则常是怒意目光；近形词的现代情绪不能按一段字母硬推。',
 ('He stood by the door, glowering at us.','他站在门边，阴沉地怒视我们。'),('Her glowering expression ended the conversation.','她阴沉的怒容让谈话停了下来。'),sources=['https://en.wiktionary.org/wiki/glowering#English','https://www.etymonline.com/word/glower'])
RADIATE=[['拉丁 radius','辐条、光线；从中心向外的形象'],['拉丁 radiare → radiatus → 英语 radiate','发出光线 → 散发、放射、向外伸展']]
W('radiantly','/ˈreɪdiəntli/','容光焕发地、喜悦灿烂地；明亮地',
 '一个人的笑容像向四周送出光，让人一眼看出喜悦，这种笑的方式可以说 radiantly。',
 'radiant + 完整 -ly。radiant 借拉丁 radians、radiant- 的现在分词材料，有自己的借词路线，不是在英语 radiate 后临时换尾才出现。',
 [RADIATE[0],['拉丁 radiare → radians、radiant- → radiant','正在发光的；喜悦焕发的'],['radiant + -ly → radiantly','明亮、喜悦焕发的方式']],
 'smiled radiantly 是笑得喜悦灿烂；radiantly happy 是明显、灿烂地幸福。',
 'smile radiantly 灿烂微笑；radiantly beautiful 光彩照人的美丽。',
 'radiant 可修饰 smile，radiantly 可修饰 smiled；把笑容的性质换成微笑动作的方式。',
 ('She smiled radiantly when she saw the children.','看见孩子们时，她露出灿烂笑容。'),('He looked radiantly happy after the concert.','音乐会结束后，他看起来喜悦焕发。'),sources=['https://en.wiktionary.org/wiki/radiantly#English','https://www.etymonline.com/word/radiant'])
W('radiates','/ˈreɪdieɪts/','散发、放射；向外伸展〔第三人称单数〕',
 '像车轮辐条从中心往外伸，光、热、声音可以从一个源头向外送，人的喜悦也能借这个画面描述。',
 'radiate + -s，保留末尾 e，/t/ 后读 /s/。动词借拉丁 radiatus、radiare，接 radius 光线、辐条。',
 RADIATE+[['radiate + -s → radiates','它向外散发；他、她显露某种情绪']],
 'radiates heat 是向外放热，radiates confidence 是明显散发自信；后者是感受，不是真测到一束物理光。',
 'radiates warmth 散发温暖；radiates from the centre 从中心向外延伸。',
 'emits 泛说发出，radiates 更容易让人看到从一个中心向周围散开的方向。',
 ('The stove radiates heat into the room.','炉子向房间散发热量。'),('She radiates confidence on stage.','她在舞台上散发自信。'),sources=['https://en.wiktionary.org/wiki/radiates#English','https://www.etymonline.com/word/radiate'])
W('radiated','/ˈreɪdieɪtɪd/','散发、放射、向外延伸了',
 '刚才热、光从源头往外送，或者某个人明显流露喜悦、自信，用 radiated。',
 'radiate 去末尾 e，加完整 -ed；/t/ 后读 /ɪd/，所以词尾另有轻读音节。',
 RADIATE+[['radiate + -ed → radiated〔去 e〕','过去向外散发、显露情绪']],
 'radiated warmth 是散出温暖，也可比喻待人的温暖；radiated joy 是喜悦明显流露。',
 'radiated from the fire 从火中向外散发；radiated happiness 洋溢幸福。',
 'radiated 关注往外散发、伸展，reflected 关注把接来的光等反射回去；源头与反射面不同。',
 ('Heat radiated from the stone walls.','热量从石墙向外散发。'),('Her face radiated joy.','她脸上洋溢喜悦。'),sources=['https://en.wiktionary.org/wiki/radiated#English','https://www.etymonline.com/word/radiate'])
W('radiating','/ˈreɪdieɪtɪŋ/','正在散发、放射；向外延伸的',
 '从一个点向外看，路线像轮辐展开，热量、情绪也像往外送，这种进行中的散发叫 radiating。',
 'radiate 去末尾不发音 e，加完整 -ing。基础词的中心向外方向保留。',
 RADIATE+[['radiate + -ing → radiating〔去 e〕','向外散发、伸展的过程或状态']],
 'roads radiating from a square 是从广场向外伸的道路；radiating confidence 则把方向图景借给自信。',
 'radiating heat 正在放热；radiating from the centre 从中心放射状展开。',
 'radiating 可讲路线、光热、神情等多种对象，不能一见它就缩成某一种专门辐射技术。',
 ('The map shows roads radiating from the central square.','地图显示了从中央广场向外延伸的道路。'),('She stood on stage, radiating confidence.','她站在舞台上，散发着自信。'),sources=['https://en.wiktionary.org/wiki/radiating#English','https://www.etymonline.com/word/radiate'])
W('radiators','英 /ˈreɪdieɪtəz/；美 /ˈreɪdieɪtərz/','暖气片、散热器〔复数〕',
 '房间里的暖气片把热送到室内，汽车散热器把多余热散出去。两种方向的系统任务不同，但设备都在向外放热。',
 'radiator + -s。英语 radiate + -or 命名散发、散热的装置，复数再加 -s；不是把 radio 收音机直接加一个字母。',
 RADIATE+[['radiate + -or → radiator → radiators','散发、散热装置；多个装置']],
 'central-heating radiators 是供暖暖气片，car radiators 是汽车散热器；用途要看所在系统。',
 'warm radiators 发热暖气片；replace radiators 更换散热器、暖气片。',
 'heaters 泛说取暖设备，radiators 可在供暖和冷却系统里工作；共同点是让热向外传。',
 ('The radiators warmed the rooms throughout the house.','暖气片把全屋各个房间都暖了起来。'),('The workshop repairs old car radiators.','修理间维修旧汽车散热器。'),sources=['https://en.wiktionary.org/wiki/radiators#English','https://en.wiktionary.org/wiki/radiator#English'])
W('glittery','英 /ˈɡlɪtəri/；美 /ˈɡlɪtəri/','闪闪发亮的；带闪粉、亮片效果的',
 '卡片、衣服上有许多小反光点，像撒过闪粉，就是 glittery。它强调那种细碎、装饰感的亮。',
 'glitter + 性质后缀 -y；保留完整 glitter。r 后接元音，常见英式也读出 /r/。',
 [['glitter 动词、闪光及闪粉名词','细碎亮点；制造这种效果的材料'],['glitter + -y → glittery','带闪亮、闪粉效果的性质']],
 'glittery paper 是闪粉纸，glittery shoes 是闪亮鞋；不要求每件物品都真的撒了粉。',
 'a glittery dress 闪亮礼服；glittery decorations 闪光装饰。',
 'glittering 既可说正在闪亮，也可比喻辉煌事业；glittery 常更直接描述表面闪亮、装饰效果。',
 ('She used glittery paper to make the card.','她用闪粉纸制作卡片。'),('The dancers wore glittery shoes.','舞者们穿着闪亮鞋子。'),sources=['https://en.wiktionary.org/wiki/glittery#English','https://en.wiktionary.org/wiki/glitter#English'])
SHINY=[['古英语 scinan → 英语 shine','发光、反光'],['shine 去 e + -y → shiny','带明显光泽的性质']]
W('shinier','英 /ˈʃaɪniə/；美 /ˈʃaɪniər/','更有光泽、更亮的',
 '同一双鞋擦过以后更反光，或两个表面相比一个更亮，就是 shinier。',
 'shiny 去 y，加完整比较级 -er → shinier；前一层 shiny 又对应 shine 去 e + -y，两次构词分开。',
 SHINY+[['shiny + -er → shinier〔y 改 i〕','表面光泽程度更高']],
 'shinier shoes 是更亮的鞋，shinier finish 是更有光泽的表面处理。',
 'look shinier 看着更亮；make it shinier 让它更有光泽。',
 'brighter 可以是光源更亮或颜色更鲜，shinier 更容易关注表面反光、光泽。',
 ('The polish made the shoes shinier.','鞋油让鞋更亮了。'),('The new coating looks shinier than the old one.','新涂层看起来比旧涂层更有光泽。'),sources=['https://en.wiktionary.org/wiki/shinier#English','https://en.wiktionary.org/wiki/shiny#English'])
W('shiniest','/ˈʃaɪniɪst/','最有光泽、最亮的',
 '一排石头、鞋子或金属片里，最能反出亮光的那个，可以叫 shiniest。它是在一个范围里比较光泽。',
 'shiny 去 y，加完整最高级 -est → shiniest。先有 shine 与 -y 的形容词，再在形容词上比较程度。',
 SHINY+[['shiny + -est → shiniest〔y 改 i〕','某范围内光泽最明显']],
 'the shiniest stone 是最有光泽的石头，the shiniest shoes 是最亮的鞋；比较对象由上下文给出。',
 'the shiniest surface 最有光泽的表面；the shiniest coin 最亮的硬币。',
 'shiniest 说光泽最高程度，flashiest 常含最花哨、最炫目的评价；表面亮与风格张扬不完全相同。',
 ('He picked the shiniest stone from the pile.','他从那堆石头里挑出最亮的一块。'),('Those are the shiniest shoes in the room.','那是房间里最亮的一双鞋。'),sources=['https://en.wiktionary.org/wiki/shiniest#English','https://en.wiktionary.org/wiki/shiny#English'])
GLOSSY=[['gloss 的光泽一支','近源与同形的注释 gloss 分开'],['gloss + -y → glossy','光滑有光泽；也可形容精美包装、刊物风格']]
W('glossier','英 /ˈɡlɒsiə/；美 /ˈɡlɑːsiər/','更有光泽、更光滑反亮的；外观更精美的',
 '两张纸、两块漆面相比，一块表面更平滑反光，就是 glossier；展示包装更精美也能这样形容。',
 'glossy 去 y，加完整比较级 -er → glossier。基础 glossy 是 gloss 光泽 + -y，不取 gloss 注释的同形支。',
 GLOSSY+[['glossy + -er → glossier〔y 改 i〕','光泽、精美外观程度更高']],
 'glossier paper 是更有光泽的纸，glossier presentation 是外观呈现更精美。',
 'a glossier finish 更亮滑的表面；look glossier 显得更有光泽。',
 'shinier 泛说更亮、更有光泽，glossier 常更容易想到光滑表面的反光；如 glossy paper、glossy paint。',
 ('This paper is glossier than the sample we used before.','这张纸比之前的样品更有光泽。'),('The new paint gives the door a glossier finish.','新油漆让门的表面更亮滑。'),sources=['https://en.wiktionary.org/wiki/glossier#English','https://en.wiktionary.org/wiki/glossy#English'])
W('glossiest','英 /ˈɡlɒsiɪst/；美 /ˈɡlɑːsiɪst/','最有光泽、最亮滑的；外观最精美的',
 '一组样本中，那块表面最平滑、最反亮的，是 glossiest。也可形容一组包装、刊物里外观最精美的。',
 'glossy 去 y，加完整最高级 -est → glossiest。比较的是光泽、精美外观，不是在数注释有多少。',
 GLOSSY+[['glossy + -est → glossiest〔y 改 i〕','比较范围中光泽、精美外观程度最高']],
 'the glossiest paper 是光泽最强的纸，the glossiest magazine 可说外观最精美、亮面的杂志。',
 'the glossiest finish 最亮滑的表面；the glossiest sample 最有光泽的样品。',
 'glossier 只需要与参照比较更亮滑，glossiest 则在给定范围里挑出最高程度。',
 ('She chose the glossiest paper for the cover.','她选了光泽最强的纸做封面。'),('This is the glossiest finish among the samples.','这是这些样品里最亮滑的表面。'),sources=['https://en.wiktionary.org/wiki/glossiest#English','https://en.wiktionary.org/wiki/glossy#English'])
W('gleefully','/ˈɡliːfəli/','欢喜地、兴高采烈地；幸灾乐祸地〔按语境〕',
 '高兴藏不住，笑着宣布、蹦着去做，动作带着明显喜悦，就是 gleefully。若高兴的是别人倒霉，也会带幸灾乐祸。',
 'glee 欢喜 + -ful → gleeful，再加完整 -ly → gleefully；两个 l 分属 -ful 与 -ly，不把整个 -fully 当这一步唯一拆分。',
 [['古英语 gleo 等 → glee','欢乐、娱乐等历史材料'],['glee + -ful → gleeful + -ly → gleefully','喜悦的性质 → 带喜悦的动作方式']],
 'said gleefully 是高兴地说，laughed gleefully 是欢喜地笑；语境决定是纯粹喜悦还是带幸灾乐祸。',
 'announce gleefully 欢喜地宣布；grin gleefully 咧嘴乐笑。',
 'happily 范围更广，gleefully 常让人感到明显、压不住的兴奋喜悦。',
 ('She gleefully announced that the exams were over.','她兴高采烈地宣布考试结束了。'),('The children gleefully jumped into the puddles.','孩子们高高兴兴地跳进水洼。'),sources=['https://en.wiktionary.org/wiki/gleefully#English','https://en.wiktionary.org/wiki/gleeful#English'])
GLITZ=[['德语 glitzern、意第绪语 glitz 等发光材料 → 英语 glitzy','耀眼、浮华的形容词；与 glitter 的较远日耳曼词族相连'],['英语 glitzy → 逆构名词 glitz','较短英语名词后形成，指耀眼浮华的外观']]
W('glitz','/ɡlɪts/','耀眼华丽、浮华外观',
 '红毯、亮灯、华丽衣服全聚到眼前，形成一片耀眼排场，这种外表光彩叫 glitz，有时带浮华感。',
 '英语名词有从较早的 glitzy 逆构而来的分析；glitzy 接意第绪语 glitz、德语 glitzern 的发光材料。英语短名词与外语同形材料的先后要分开。',GLITZ,
 'glitz and glamour 是耀眼华丽的排场；behind the glitz 可把镜头从外表转到背后的工作、生活。',
 'Hollywood glitz 好莱坞式华丽排场；full of glitz 满是耀眼装饰。',
 'glitter 还可具体指闪粉，glitz 常说整体外观、场面的华丽浮华；两个词不在每个对象上互换。',
 ('The ceremony was full of glitz and glamour.','典礼满是耀眼华丽的排场。'),('Behind the glitz, the performers worked long hours.','华丽外表背后，表演者长时间工作。'),sources=['https://www.etymonline.com/word/glitz','https://www.etymonline.com/word/glitzy','https://en.wiktionary.org/wiki/glitz#English'])
W('glitzy','/ˈɡlɪtsi/','华丽耀眼、浮华的',
 '闪亮装饰、灯光、名流聚在一起，外观很抢眼的场合，可以说 glitzy；语气可以带一点对浮华的评判。',
 '现代对应 glitz + -y，实际英语 glitzy 的记录较早，接意第绪语 glitz 等发光材料；英语名词 glitz 又有由它逆构的分析。',GLITZ,
 'a glitzy party 是华丽聚会，a glitzy awards ceremony 是耀眼颁奖礼；不一定每件东西都撒了闪粉。',
 'a glitzy hotel 装饰华丽的酒店；a glitzy event 华丽抢眼的活动。',
 'glittery 更容易描述表面细碎闪亮、闪粉效果，glitzy 更常描述整个场所、活动的华丽浮华风格。',
 ('They attended a glitzy awards ceremony.','他们参加了一场华丽耀眼的颁奖礼。'),('The hotel has a glitzy lobby with mirrored walls.','酒店大堂装饰华丽，墙面铺着镜子。'),sources=['https://www.etymonline.com/word/glitzy','https://www.etymonline.com/word/glitz','https://en.wiktionary.org/wiki/glitzy#English'])

def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_zem',ROOTS,WORDS)
    extend_lessons()
