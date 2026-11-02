"""Humming, electronic beeps, quieting, air movement and dull impacts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4189':dict(words=['hum','hums','hummed','humming'],label='hum 的哼唱、低鸣与现代变化',note='声音 hum 接中古英语 hommen、hummen 等拟声材料，不是古典词根 hum- 土地；hummed 双写 m，再加完整 -ed。'),
 'B4010':dict(words=['buzz','buzzes','buzzed','buzzing'],label='buzz 的嗡鸣、忙碌与电话用法',note='buzz 拟昆虫声音，buzzes 的 -es 在 /z/ 后读 /ɪz/；buzzed 的 -ed 读 /d/，声音、联系人的搭配要分别解释。'),
 'A1760':dict(words='hum hums hummed humming buzz buzzes buzzed buzzing beep beeps beeped beeping hush hushes hushed hushing swish swishes swished swishing whoosh whooshes whooshed whooshing thud thuds thudded thudding thump thumps thumped thumping'.split(),label='低鸣、嘀声、安静、掠过与闷响动词的变化',note='这些拟声或由拟声发展的基础词分别解释，不是一条共同古根；thudded 因 /d/ 后接 -ed 多出 /ɪd/，hushed、swished、whooshed 末尾 -ed 则读 /t/。'),
}
HUM=[['中古英语 hommen、hummen 等 → hum','轻声发声、低鸣，大概拟声；后来发展出闭口哼唱'],['现代声音与活动的比喻','哼曲、机器低鸣；场所忙碌活跃，像蜂巢运转']]
W('hums','/hʌmz/','哼唱、低鸣〔第三人称单数〕；低鸣声、哼曲〔复数〕',
 '嘴唇合着，旋律在鼻腔、喉间“嗯嗯”走，用 hums；机器平稳低鸣，也能这样说。',
 'hum + -s，/m/ 后读 /z/。声音基础词不同于古典 hum- 土地，不用从 human、人类等词硬拆。',HUM+[['hum + -s → hums','他、她哼唱；它低鸣；多段哼曲、低声']],
 'hums a tune 是哼一段旋律，the fridge hums 是冰箱低鸣；the office hums with activity 是办公室忙碌运转。',
 'hums quietly 轻轻哼唱、低鸣；hums to himself 自顾自哼曲。',
 'hums a song 往往不把歌词清楚唱出；sings a song 通常说唱歌，是否有歌词要看具体形式。',
 ('She hums a tune while she cooks.','她做饭时哼着曲子。'),('The fridge hums quietly in the corner.','冰箱在角落里轻轻低鸣。'),sources=S('hums','hum'))
W('hummed','/hʌmd/','哼唱了、低鸣了；忙碌活跃地运转了',
 '刚才轻轻哼了一段曲子，或机器一阵平稳低响，用 hummed；场所忙碌，也能借这种持续运转的感觉。',
 'hum 双写 m + 完整 -ed → hummed，词尾 /d/；短元音重读单音节的拼写变化，元音不变。',HUM+[['hum 双写 m + -ed → hummed','过去哼唱、低鸣或忙碌运转']],
 'hummed a melody 是哼了旋律，hummed with activity 是忙得热火朝天；后一种不只是在描述噪音。',
 'hummed softly 轻轻哼；hummed all night 整夜低鸣。',
 'hummed 的词尾看基础词最后的音：hum 的 /m/ 后接 /d/，hush 的 /ʃ/ 后接 /t/；不是看到同样的 -ed 就一律同音。',
 ('He hummed the melody as we walked home.','回家路上，他哼着那段旋律。'),('The workshop hummed with activity before the opening.','开业前，作坊里一派忙碌。'),sources=S('hummed','hum'))
BUZZ=[['较早 buzzing 及 buzz 动词 → 现代 buzz','模仿蜜蜂等昆虫连续嗡声；分词记录可早于基础动词记录'],['嗡声 → 电话、忙碌、兴奋等用法','通过设备联系、低飞掠过、人群热议；按搭配分支']]
W('buzzes','/ˈbʌzɪz/','嗡嗡响、震动鸣响〔第三人称单数〕；嗡声、兴奋感〔复数〕',
 '昆虫“嗡嗡”飞、手机振动着响，用 buzzes。场所满是活动、谈论，也能说 buzzes with activity、excitement。',
 'buzz + -es，/z/ 后读 /ɪz/，多一个音节。已有 zz 保留，不把它改成一个 z。',BUZZ+[['buzz + -es → buzzes','它嗡响、忙碌活跃；多阵嗡声']],
 'buzzes around the room 是嗡嗡绕屋飞，buzzes with excitement 是到处洋溢兴奋感；先看声源和搭配。',
 'the phone buzzes 手机震响；the room buzzes with talk 满屋子议论声。',
 'buzzes 常带较密的嗡鸣、振动感，hums 更容易表现平稳的低鸣；两者都能写机器，听感略不同。',
 ('A fly buzzes around the window.','一只苍蝇绕着窗户嗡嗡飞。'),('My phone buzzes whenever a new message arrives.','新消息一到，我的手机就震响。'),sources=S('buzzes','buzz'))
W('buzzed','/bʌzd/','嗡嗡响了；用电话、对讲联系了；〔口语〕微醺的',
 '刚才设备、昆虫嗡地响了，用 buzzed；人被电话叫到、按门禁放入，也能进入 buzzed 的搭配。',
 'buzz + 完整 -ed，/z/ 后读 /d/；即使字母有 zz，也不加读 /ɪd/。口语形容词义要按上下文分辨。',BUZZ+[['buzz + -ed → buzzed','过去嗡响、联系；另有口语微醺状态']],
 'buzzed me 是给我打电话、通过设备联系我，buzzed me in 是按门禁让我进来；不是把我弄成嗡声。',
 'buzzed past 嗡嗡掠过；felt buzzed 感到微醺。',
 'buzzed in 依靠门禁系统放行，let in 只说让人进来；声音词扩到设备动作后，不能逐字翻成“嗡进去”。',
 ('My phone buzzed in my pocket.','我的手机在口袋里震响。'),('The receptionist buzzed me in through the main door.','接待员按了门禁，让我从正门进去。'),sources=S('buzzed','buzz'))
BEEP=[['二十世纪初 beep 表示汽车喇叭声 → 名词、动词','模仿短促“嘀”声；是近代拟声词，不需硬追成拉丁古根'],['汽车喇叭 → 电子设备提示声等','嘀声；使设备响、按喇叭提醒；用嘀声遮盖录音内容']]
W('beep','/biːp/','嘀地响；鸣喇叭提醒；一声嘀响；用嘀声遮盖',
 '像计时器到点“嘀”一下，或车喇叭短短一响，就是 beep。重点是一声短促、清楚的提示音。',
 '近代模仿汽车喇叭声音形成，随后作名词、动词，再用于电子提示音；不是所有拟声词都有可拆的古典词根。',BEEP,
 'a short beep 是短短一声嘀，beep the horn 是按喇叭；beep out a word 是在录音中用嘀声盖掉一个词。',
 'wait for the beep 等提示音；beep twice 嘀响两声。',
 'beep 常是短促提示音，buzz 更容易让人想到连续嗡声或振动声；同一台设备也可能有不同模式。',
 ('Leave your message after the beep.','听到嘀声后请留言。'),('The timer will beep when the eggs are ready.','鸡蛋煮好时，计时器会嘀响。'),sources=S('beep','beep'))
W('beeps','/biːps/','嘀地响、按喇叭〔第三人称单数〕；一声声嘀响',
 '设备每完成一步就短促“嘀”一下，用 beeps；名词复数则是几声提示音。',
 'beep + -s，/p/ 后读 /s/；三单、名词复数同形。',BEEP+[['beep + -s → beeps','它嘀响；多声提示音']],
 'beeps when finished 是完成时嘀响，three beeps 是三声提示音；具体提示什么由设备、场景交代。',
 'beeps loudly 大声嘀响；a series of beeps 一连串提示音。',
 'beeps 描述怎么响，不自动表示故障；完成、确认、倒计时等也能用嘀声提示。',
 ('The microwave beeps when the food is ready.','食物热好时，微波炉会嘀响。'),('Three short beeps came from the speaker.','扬声器传来三声短促嘀响。'),sources=S('beeps','beep'))
W('beeped','/biːpt/','嘀地响了、按喇叭了；用嘀声遮盖了',
 '设备刚才短短响了一声，或司机短按喇叭提醒，用 beeped；录音里盖掉某个词时，也可说 beeped out。',
 'beep + 完整 -ed，/p/ 后读 /t/；ee 元音保留，不多一个音节。',BEEP+[['beep + -ed → beeped','过去嘀响、鸣喇叭或用嘀声遮盖']],
 'beeped twice 是嘀响两声，beeped the horn 是按了喇叭，beeped out the name 是用嘀声盖掉名字。',
 'beeped at us 朝我们按喇叭；beeped softly 轻轻嘀响。',
 'beeped out 是音频处理的固定搭配；这里 out 不是声音“向外跑”，而是内容被遮掉。',
 ('The scanner beeped when it read the code.','扫描器读到代码时嘀地响了。'),('The driver beeped the horn to get our attention.','司机短按喇叭，引起我们的注意。'),sources=S('beeped','beep'))
W('beeping','/ˈbiːpɪŋ/','正在嘀响、鸣喇叭；嘀嘀提示声',
 '耳边的短促电子音正一声接一声响，是 beeping。单个 beep 很短，beeping 可以描述一整段反复提示。',
 'beep + 完整 -ing，直接加；ee 表示长元音，不能套短元音重读词的规则双写 p。',BEEP+[['beep + -ing → beeping','嘀响、鸣喇叭的过程与提示声']],
 'the beeping of an alarm 是警报嘀嘀声，a beeping timer 是正嘀响的计时器；也可写人正在按喇叭。',
 'constant beeping 不断的嘀嘀声；stop beeping 停止嘀响。',
 'beeping 通常把短声反复连起来；a continuous tone 则可以是一条不停顿的长音，节奏不同。',
 ('The beeping of the alarm woke me.','警报的嘀嘀声把我叫醒了。'),('Someone was beeping a horn outside the gate.','有人在大门外按喇叭。'),sources=S('beeping','beep'))
HUSH=[['较早中古英语 huisht 等 → hush','大概源于轻轻制止声；末尾 t 的消失或与过去式误解有关'],['使安静、安静下来 → 寂静名词及保密搭配','a hush 是突然或一片安静；hush up 是把事情压下、不让议论']]
W('hush','/hʌʃ/','嘘、安静些；使安静、静下来；一片寂静；〔hush up〕压下消息',
 '轻轻“嘘”一声，让声音停下来，就是 hush。a hush 则把现场安静下来的那一片寂静整体提出来。',
 '由较早 huisht 一类制止声发展，大概拟声；末尾 t 的消失有与过去式误解相连的分析，不是现代 hush 的词根里藏着 quiet。',HUSH,
 'Hush! 是安静点；hush the baby 是哄婴儿安静；a hush fell over the room 是屋里忽然安静下来。',
 'a sudden hush 突然的寂静；hush up a scandal 压下丑闻。',
 'hush up 在消息语境是让事情不被谈论、披露；它不只是把说话音量调小，常带隐瞒的意思。',
 ('A hush fell over the audience as the lights dimmed.','灯光暗下来时，观众席安静了。'),('She sang softly to hush the baby.','她轻声唱歌，哄婴儿安静。'),sources=S('hush','hush'))
W('hushes','/ˈhʌʃɪz/','使安静、静下来〔第三人称单数〕',
 '一个人轻轻示意大家别说话，或哄孩子静下来，用 hushes；接 up 一件事时，还可说把消息压下。',
 'hush + -es，/ʃ/ 后读 /ɪz/；不是直接接 /s/，要多一个音节。',HUSH+[['hush + -es → hushes','他、她使人安静；压下某事']],
 'hushes the crowd 是使人群安静，hushes the baby 是哄孩子别哭；hushes up the story 是把消息压住。',
 'hushes everyone 让大家安静；hushes us with a gesture 用手势示意我们安静。',
 'hushes 可以很温和，不等于 harshly silences 严厉制止；态度要看手势、语气和对象。',
 ('The teacher hushes the class with a gentle gesture.','老师用一个温和的手势让全班安静。'),('She hushes the baby by singing softly.','她轻声唱歌，哄婴儿安静。'),sources=S('hushes','hush'))
W('hushed','/hʌʃt/','使安静了、静下来了；压低声音的、静悄悄的；压下消息了',
 '说话声被收住、现场静下来，是 hushed；hushed voices 则是人有意压低、轻轻说的声音。',
 'hush + 完整 -ed，/ʃ/ 后读 /t/；可作过去式、过去分词或描述安静状态的形容词。',HUSH+[['hush + -ed → hushed','已经安静、压低声音；也可写消息被压下']],
 'in hushed voices 是压低声音交谈，a hushed room 是静悄悄的房间；hushed up a scandal 是压下了丑闻。',
 'hushed tones 低低的语调；the crowd hushed 人群静下来了。',
 'hushed 形容声音往往有刻意放轻、肃静的感觉；hoarse 是音色沙哑，两种性质不同。',
 ('They spoke in hushed voices outside the bedroom.','他们在卧室外压低声音说话。'),('The crowd hushed as the speaker stepped forward.','讲话者走上前时，人群安静下来。'),sources=S('hushed','hush'))
W('hushing','/ˈhʌʃɪŋ/','正在让人安静、静下来；制止声；正在压下消息',
 '有人正“嘘、嘘”地哄孩子、示意人群安静，叫 hushing；接 up 消息时，才转成压下议论的用法。',
 'hush + 完整 -ing，直接加；sh 是两个辅音字母，基础拼写不需要双写 h。',HUSH+[['hush + -ing → hushing','使安静的过程；hushing up 则是压消息']],
 'hushing the baby 是正哄婴儿安静，hushing the crowd 是让人群静下来；hushing up the matter 是压下这件事。',
 'gently hushing 温柔地哄静；a hushing gesture 示意安静的手势。',
 'hushing 的对象可以是人、声音，也可以在固定搭配里是消息；看宾语及 up，才能选对中文义。',
 ('She was hushing the baby when we arrived.','我们到时，她正哄婴儿安静。'),('The guide was hushing the group before the performance.','演出开始前，导游正示意大家安静。'),sources=S('hushing','hush'))
SWISH=[['十八世纪 swish 动词及后来的声音名词','大概模仿物体擦过、挥过空气的唰声'],['现代声音、动作及形容词扩展','尾巴、裙摆、水等唰地动；篮球空心入网；英口语还说时髦、气派']]
W('swish','/swɪʃ/','唰地移动、挥动；唰声；篮球空心入网；〔英口语〕时髦气派的',
 '裙摆、尾巴或刷子快速擦过“唰”一下，叫 swish。它把掠过的动作和轻细摩擦声放在一起。',
 '大概模仿物体擦过空气或表面的声音，随后有名词和其他用途；篮球空心入网也借球穿网的声音叫 swish。',SWISH,
 'swish a tail 是唰地甩尾巴，a swish of fabric 是衣料唰声；a swish hotel 在英口语里是时髦气派的酒店。',
 'swish through the grass 唰地穿过草丛；a swish of the skirt 裙摆唰地一动。',
 'swish 常贴着轻扫、摩擦的动作，whoosh 更容易让人想到快速通过空气的一大股呼声；并无严格声学分界。',
 ('The horse gave its tail a swish.','马唰地甩了一下尾巴。'),('They stayed in a rather swish hotel.','他们住进了一家挺气派的酒店。'),sources=S('swish','swish'))
W('swishes','/ˈswɪʃɪz/','唰地移动、挥动〔第三人称单数〕；一次次唰声；篮球空心入网〔复数〕',
 '尾巴一摆、衣摆一扫就“唰”地掠过，用 swishes；名词复数是一次次这样的声响或动作。',
 'swish + -es，/ʃ/ 后读 /ɪz/，多一个音节。作动词三单、动作或声音名词复数都可以。',SWISH+[['swish + -es → swishes','它唰地挥、扫；多次唰声或空心入网']],
 'swishes its tail 是唰地甩尾巴，swishes past 是唰地掠过；篮球语境中的 swishes 另看空心球。',
 'swishes through the water 唰地划过水；soft swishes 轻轻的唰声。',
 'swishes 不要求声音很大：裙摆、刷子、尾巴轻轻扫过，也能发出这种动作声。',
 ('The horse swishes its tail to keep the flies away.','马唰地甩尾巴赶苍蝇。'),('Her long skirt swishes as she walks.','她走路时，长裙唰唰作响。'),sources=S('swishes','swish'))
W('swished','/swɪʃt/','唰地挥动、掠过了；使球空心入网了',
 '尾巴、裙摆、水或别的东西刚才唰地一动，用 swished。常让人看见轻快扫过的路线。',
 'swish + 完整 -ed，/ʃ/ 后读 /t/，只有一个音节；不读 /ɪd/。',SWISH+[['swish + -ed → swished','过去唰地扫、挥、掠过；相应篮球用法']],
 'swished its tail 是唰地甩尾，swished past 是唰地经过；swished the ball through the hoop 是投出空心球。',
 'swished through the grass 唰地穿过草；swished around the glass 在杯中晃得唰响。',
 'swished 同时写动作和声响；swept 更重扫过、席卷等动作本身，不一定让读者听见唰声。',
 ('The cat swished its tail and turned away.','猫唰地甩尾，转身走开。'),('Her skirt swished against the grass.','她的裙摆擦过草，唰唰作响。'),sources=S('swished','swish'))
W('swishing','/ˈswɪʃɪŋ/','正在唰地挥动、掠过；唰唰声；相应篮球动作',
 '衣料、树枝、尾巴或水正一阵阵快速扫过，叫 swishing。可以写动作，也可把轻细摩擦声整体提出来。',
 'swish + 完整 -ing，直接相接；sh 作为基础拼写保留，不双写末尾 h。',SWISH+[['swish + -ing → swishing','唰地挥、扫、掠过的过程和声音']],
 'the swishing of skirts 是裙摆唰唰声，a swishing tail 是来回唰地摆动的尾巴；不是只有空气能发这类声。',
 'swishing through the grass 唰地扫过草；swishing water around 晃得水唰响。',
 'swishing 常伴有横扫、摆动、擦过的动作感；rustling 常更像轻薄材料一片片摩擦的沙沙声。',
 ('The swishing of the long grass followed us along the path.','我们沿小路走，高草一路唰唰擦响。'),('The dog stood there, swishing its tail from side to side.','狗站在那里，尾巴左右唰唰摆动。'),sources=S('swishing','swish'))
WHOOSH=[['十九世纪 whoosh 动词 → 名词、感叹用法','模仿东西快速通过空气的呼声'],['现代快速掠过、喷涌及比喻','声音伴随快动作；网上还可用 Whoosh 表示某人没听懂笑点']]
W('whoosh','/wʊʃ/；也读 /wuːʃ/','呼地、嗖地掠过；一阵呼声；嗖的一声',
 '一列车、一阵风或一股水快速冲过，带出“呼——”的一声，就是 whoosh。抓住速度快、气流或流动一下掠过去。',
 '近代拟声词，先有动词，随后有声音名词、感叹用法；声音和字形相互模仿，不需要硬拆成 who + 某个后缀。',WHOOSH,
 'with a whoosh 是呼的一声，whoosh past 是嗖地掠过；网上 Whoosh! 有时表示笑话从对方头顶飞过、对方没懂。',
 'a whoosh of air 一股气流呼地掠过；whoosh down 呼地冲下。',
 'whoosh 比 swish 常更有一大股快速流动的感觉；swish 更易突出轻扫、擦过的唰声，两者可重合。',
 ('The train passed with a whoosh.','火车呼地驶过。'),('We heard the water whoosh through the pipe.','我们听见水呼地冲过管道。'),sources=S('whoosh','whoosh'))
W('whooshes','/ˈwʊʃɪz/；也读 /ˈwuːʃɪz/','呼地、嗖地掠过〔第三人称单数〕；一阵阵呼声',
 '火车、风或水一股股快速掠过，用 whooshes；复数名词也能说一阵阵快速流动的呼声。',
 'whoosh + -es，/ʃ/ 后读 /ɪz/，多一个音节；基础词的短、长元音读法可相应保留。',WHOOSH+[['whoosh + -es → whooshes','它呼地冲、掠；多阵呼声']],
 'whooshes past 是嗖地掠过，whooshes down the pipe 是顺管道呼地冲下；方向词帮助看清运动路线。',
 'whooshes through 快速呼地穿过；short whooshes 一阵阵短呼声。',
 'whooshes 不只写风：水、列车、运动器材等只要有快速掠过的感觉，也能借用。',
 ('The express train whooshes past without stopping.','特快列车呼地驶过，没有停车。'),('Water whooshes down the pipe when the valve opens.','阀门打开时，水呼地冲下管道。'),sources=S('whooshes','whoosh'))
W('whooshed','/wʊʃt/；也读 /wuːʃt/','呼地、嗖地冲过了、掠过了',
 '某个东西刚才快速从身边、头顶掠过，带出呼声，用 whooshed。它比 went past 多了速度和声音。',
 'whoosh + 完整 -ed，/ʃ/ 后读 /t/；不因为词长就多读一个音节。',WHOOSH+[['whoosh + -ed → whooshed','过去快速呼地掠过、冲过']],
 'whooshed past us 是嗖地从身边掠过，whooshed down the slide 是呼地滑下滑梯；路线由后面部分说明。',
 'whooshed overhead 从头顶呼地掠过；whooshed through the door 呼地冲过门口。',
 'whooshed 是带速度、气流感的移动描写；它不自动说明速度具体多快，只给读者运动印象。',
 ('A cyclist whooshed past us on the path.','一个骑车的人嗖地从我们身边掠过。'),('The water whooshed down the drain.','水呼地流进排水口。'),sources=S('whooshed','whoosh'))
W('whooshing','/ˈwʊʃɪŋ/；也读 /ˈwuːʃɪŋ/','正在呼地掠过、冲过；快速流动的呼声',
 '一股气流、水流或车辆正快速掠过，声音像“呼——”，叫 whooshing。可以写过程，也能形容那阵声音。',
 'whoosh + 完整 -ing，直接加；两种常见元音读法在相应变化中保留。',WHOOSH+[['whoosh + -ing → whooshing','快速掠过、流动的过程与呼声']],
 'a whooshing sound 是一阵呼声，whooshing past 是呼地掠过；听到声音未必马上知道具体声源。',
 'whooshing water 快速冲流的水；the whooshing of traffic 车流快速掠过声。',
 'whooshing 常写一股流动、掠过感；hissing 更像狭缝持续出气的嘶声，叙述画面不同。',
 ('A whooshing sound came from the ventilation shaft.','通风井里传来一阵呼声。'),('We watched the trains whooshing past the platform.','我们看着列车呼地从站台旁驶过。'),sources=S('whooshing','whoosh'))
THUD=[['较早英语 þyddan、thudden 等推、击材料可比较','旧材料与现代闷响词如何连续，有不同分析；也可能多次拟声形成'],['现代 thud 的闷钝撞击义','重物落下、身体或物体撞上较不响亮的表面，发咚声']]
W('thud','/θʌd/','咚地闷响；发闷响地撞、落；一声闷响',
 '一本厚书掉在地毯上，或重物撞到不太会共鸣的表面，“咚”一下，像 thud。不是清脆、亮亮的金属响。',
 '有古英语 þyddan、中古英语 thudden 等推、击材料可比较，但现代拟声词也可能重新、多次形成；不把每一阶段都当确定连续链。',THUD,
 'with a thud 是咚的一声，hit the floor with a thud 是落地闷响；thud against the wall 是撞墙发闷声。',
 'a dull thud 一声钝闷响；a heavy thud 沉重的咚声。',
 'thud 偏闷、钝，clang 偏金属共鸣；落到地毯上的书和碰响的铁门，不能只用一个“响”抹平。',
 ('The bag landed on the floor with a thud.','袋子咚地落到地上。'),('We heard a dull thud from the room above.','我们听见楼上房间传来一声闷响。'),sources=S('thud','thud'))
W('thuds','/θʌdz/','咚地闷响、撞响〔第三人称单数〕；一声声闷响',
 '重物落下、球撞到墙时发出钝钝“咚”声，用 thuds；复数名词则是接连几记闷声。',
 'thud + -s，/d/ 后读 /z/；动词三单、声音名词复数同形，不多一个音节。',THUD+[['thud + -s → thuds','它闷声撞、落；多记闷响']],
 'thuds against the wall 是碰墙咚响，heavy thuds 是沉重闷声；常见于物体、脚步或撞击。',
 'thuds to the ground 咚地落地；a series of thuds 接连闷响。',
 'thuds 描写声音，不必每次都是摔倒；运动时球撞墙、箱子放下都可能发闷声。',
 ('The ball thuds against the wall on every bounce.','球每次弹到墙上都咚地响。'),('We heard heavy thuds on the stairs.','我们听见楼梯上沉重的咚咚声。'),sources=S('thuds','thud'))
W('thudded','/ˈθʌdɪd/','咚地闷响了、撞响了；重重落下了',
 '重东西刚才落地、撞墙，带出钝闷的一声，叫 thudded。叙事里常把着陆、撞击和声音写在一起。',
 'thud 双写 d + 完整 -ed → thudded；基础词以 /d/ 结尾，词尾读 /ɪd/，所以多一个音节。',THUD+[['thud 双写 d + -ed → thudded','过去闷声撞、落']],
 'thudded to the floor 是咚地落地，thudded against the door 是撞门发闷声；to、against 说明落向、撞向哪里。',
 'thudded heavily 沉沉地咚响；thudded onto the mat 咚地落到垫子上。',
 'thudded 的最后一节是 /ɪd/，thumped 则只有 /t/ 词尾；按基础最后的音分，不按中文都是“咚”。',
 ('The parcel thudded onto the doormat.','包裹咚地落到门垫上。'),('The ball thudded against the wooden fence.','球撞到木栅栏，咚地响。'),sources=S('thudded','thud'))
W('thudding','/ˈθʌdɪŋ/','正在闷声撞、响；咚咚闷声；怦怦跳',
 '闷闷的“咚、咚”正接连发生，是 thudding。也能把紧张、剧烈跳动的心跳写得像听得见。',
 'thud 双写 d + 完整 -ing → thudding；双写保留短元音基础词的拼写形式。',THUD+[['thud 双写 d + -ing → thudding','闷响、撞击过程；心跳的相似声音感']],
 'thudding footsteps 是沉闷的咚咚脚步，a thudding heart 是怦怦跳的心；可以是声音，也能是身体感受。',
 'thudding on the stairs 楼梯上的咚咚声；heart thudding 心怦怦跳。',
 'thudding heart 不保证旁人真听得见心跳；叙述常把当事人的强烈跳动感写成声音。',
 ('I could hear thudding footsteps overhead.','我听见头顶传来咚咚的脚步。'),('She waited by the door, her heart thudding.','她站在门边等，心怦怦跳。'),sources=S('thudding','thud'))
THUMP=[['十六世纪 thump 动词 → 名词','大概模仿重重敲打的声音；可与 thud、bump 等比较'],['重击、闷响 → 沉重脚步、心跳及口语强调','动作感比纯粹的一记响声更突出，具体语境仍会重合']]
W('thump','/θʌmp/','重重敲击、捶打；咚咚响、怦怦跳；一记重击、闷响',
 '拳头重重捶桌子“咚”一下，或心脏怦怦有力跳，叫 thump。既能写那一记动作，也能写发出的闷声。',
 '大概是重击声音的拟声词，先有动词记录，后有闷声、重击名词；不是 thumb 拇指加 p。',THUMP,
 'thump the table 是重重捶桌，a thump on the door 是一记重敲，my heart gave a thump 是心猛地跳一下。',
 'a heavy thump 一记沉重闷响；thump against the wall 重撞墙。',
 'thump 和 thud 很接近；thump 常更容易带敲、捶、跳动的动作感，thud 更先抓那一下钝闷声音。',
 ('He gave the table a thump with his fist.','他用拳头重重捶了一下桌子。'),('I felt my heart thump as the door opened.','门打开时，我感到心猛地跳了一下。'),sources=S('thump','thump'))
W('thumps','/θʌmps/','重敲、咚响、怦怦跳〔第三人称单数〕；重击、闷响〔复数〕',
 '鼓点一下下沉沉响，或心脏有力跳，用 thumps；名词复数则是几记重敲、重击。',
 'thump + -s，/p/ 后读 /s/；mp 读 /mp/，两个音都发，不往中间插元音。',THUMP+[['thump + -s → thumps','它咚响、怦怦跳；他、她重敲；几记重击']],
 'thumps against his ribs 是心撞着胸口怦怦跳，heavy thumps 是几声沉重闷响；也可说人重敲某物。',
 'thumps on the door 门上重敲声；the bass thumps 低音咚咚响。',
 'thumps 比 taps 常更重，taps 常是轻轻敲；敲门是提醒还是用力拍打，选词就能带出力度。',
 ('The bass thumps through the wall.','低音穿过墙，咚咚作响。'),('Three heavy thumps sounded at the door.','门上传来三记沉重敲击声。'),sources=S('thumps','thump'))
W('thumped','/θʌmpt/','重重敲打了、捶了；咚咚响了、怦怦跳了',
 '刚才拳头、脚步或心跳沉重有力地动了一下、一阵，用 thumped。它让动作有分量、声音偏闷。',
 'thump + 完整 -ed，/p/ 后读 /t/，结尾 /mpt/；基础词末尾有 mp，不双写 p。',THUMP+[['thump + -ed → thumped','过去重敲、沉重跳动、咚响']],
 'thumped the table 是重重捶桌了，heart thumped 是心怦怦跳；thumped down the stairs 是脚步咚咚地下楼。',
 'thumped loudly 咚咚响了；thumped against the wall 重重撞墙。',
 'thumped 是敲、捶、重响；thumbed 可以是用拇指翻、碰，拼写、发音和动作来源分开。',
 ('He thumped the table to get everyone’s attention.','他重重敲桌，想让大家注意。'),('Her heart thumped as she waited for the result.','等结果时，她的心怦怦跳。'),sources=S('thumped','thump'))
W('thumping','/ˈθʌmpɪŋ/','正在重敲、咚响、怦怦跳；沉重闷响；〔口语〕极大的',
 '重鼓、心跳或脚步正有力地“咚、咚”动，叫 thumping。口语里 a thumping victory 又像“重重压过去”，说大胜。',
 'thump + 完整 -ing，直接加；分词、声音活动名词之后，还能作口语强调修饰语，不必真的有声响。',THUMP+[['thump + -ing → thumping','重敲、跳动过程；后有极大、压倒性的强调义']],
 'thumping music 是节奏、低音很重的音乐，a thumping majority 是压倒性多数，a thumping headache 是怦怦痛的头疼。',
 'a thumping victory 一场大胜；a thumping heart 怦怦跳的心。',
 'thumping majority 是固定的口语强调，不是多数票发出咚声；音乐场景则常保留真实的重节拍。',
 ('Thumping music came from the flat upstairs.','楼上公寓传来重节拍的音乐。'),('The proposal passed with a thumping majority.','提案以压倒性多数通过。'),sources=S('thumping','thump'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfc',ROOTS,WORDS)
 extend_lessons()
