"""Creaking boards, rustling leaves, low rumbles and small ringing sounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3527':dict(words=['crack','crackle','crackles','crackled','crackling'],label='crack 与 crackle：一声啪响到接连噼啪',note='crackle 接中古英语 crackelen，是 cracken 的旧反复动作形式；crackling 另有烤肉脆皮名词义，不能只解释成进行时。'),
 'A2238':dict(words=['crackle','crackles','crackled','crackling','tinkle','tinkles','tinkled','tinkling'],label='crackle、tinkle 的旧反复动作材料',note='crackle 联系 crack；tinkle 大概是较早 tink、tinken 的反复动作形式。-le 的具体历史按词解释，不把所有末尾 -le 的词都套进同一个故事。'),
 'A1699':dict(words=['creak','creaks','creaked','creaking','creaky'],label='creak 到 creaky：嘎吱响变成一种特点',note='creaky 的 -y 写容易嘎吱响；还可以比喻制度老旧、不灵活，和 creek 小溪不是同一现代词。'),
 'A1760':dict(words='creak creaks creaked creaking crackle crackles crackled crackling rustle rustles rustled rustling rumble rumbles rumbled rumbling clink clinks clinked clinking jingle jingles jingled jingling jangle jangles jangled jangling tinkle tinkles tinkled tinkling'.split(),label='嘎吱、沙沙、隆隆及叮当动词的变化',note='rustle 的声音、忙着弄来和偷牲口等义有不同历史分析，jingle 与 jangle 也不能仅按现代音近排成母子词。-ed 的发音取决于基础词最后的音。'),
}
CREAK=[['中古英语 creken → creak','粗涩的叫声材料，大概拟声；可与古英语 cræccettan 比较'],['后来常写门轴、木板、关节等嘎吱声','动词 → 声音名词；再有 creaky 易嘎吱响、老旧不灵活']]
W('creak','/kriːk/','嘎吱响；嘎吱声',
 '踩到旧木地板、慢慢推开生涩的门，听见拉扯摩擦般的“嘎吱”，就是 creak。常是东西受力或移动时发出的粗涩声。',
 '接中古英语 creken 的旧发声材料，大概拟声；后来用于门轴、木板等摩擦声。现代 creak 是完整基础词。',CREAK,
 'the floorboards creak 是地板嘎吱响，with a creak 是伴着一声嘎吱；动作慢慢展开时尤其有画面感。',
 'a creak from the stairs 楼梯传来的嘎吱声；creak under someone’s weight 被人踩得嘎吱响。',
 'creak 与 creek 小溪常同音，来源、拼写分开。squeak 偏更细高的吱声，creak 常更粗、更像受力摩擦。',
 ('The old stairs began to creak under our weight.','我们走上去，旧楼梯开始嘎吱响。'),('The door opened with a long creak.','门伴着长长一声嘎吱打开了。'),sources=S('creak','creak'))
W('creaks','/kriːks/','嘎吱响〔第三人称单数〕；一声声嘎吱响',
 '每走一步地板就粗粗摩擦一响，用 creaks；名词复数则是那些零星的嘎吱声。',
 'creak + -s，/k/ 后读 /s/；动词三单、声音名词复数同形。',CREAK+[['creak + -s → creaks','它嘎吱响；多声嘎吱响']],
 'creaks in the wind 是风吹得嘎吱响，a few creaks 是几声嘎吱；常见于木结构、门或椅子。',
 'creaks underfoot 脚下一踩就嘎吱响；faint creaks 轻微的嘎吱声。',
 'creaks 是嘎吱发声，cracks 常说裂开或啪地一响；地板 creaks 不等于叙述它裂成了几块。',
 ('The wooden floor creaks near the window.','窗边的木地板一踩就嘎吱响。'),('A few creaks broke the silence of the house.','几声嘎吱响打破屋里的寂静。'),sources=S('creaks','creak'))
W('creaked','/kriːkt/','嘎吱响了；嘎吱响着移动了',
 '门刚才慢慢动开、地板被脚踩得粗粗一响，叫 creaked。它能把动作和摩擦声一起写出来。',
 'creak + 完整 -ed，/k/ 后读 /t/，仍是一个音节。',CREAK+[['creak + -ed → creaked','过去发嘎吱声']],
 'creaked open 是嘎吱响着打开，creaked beneath his feet 是脚下嘎吱响；open、beneath 等帮助搭出场景。',
 'creaked loudly 大声嘎吱响；creaked in the wind 在风里嘎吱作响。',
 'creaked open 与 opened 动作相近，前者让读者听见生涩的声音；不需要额外加“门坏了”的推断。',
 ('The gate creaked open in the wind.','大门被风吹得嘎吱打开。'),('The floorboards creaked beneath his feet.','木地板在他脚下嘎吱响。'),sources=S('creaked','creak'))
W('creaking','/ˈkriːkɪŋ/','正在嘎吱响；嘎吱声；嘎吱响的',
 '门轴、木板或旧椅子的粗涩声正响着，叫 creaking。可以把响声当名词，也可以修饰正在响的东西。',
 'creak + 完整 -ing，直接相接；保留 ea 的 /iː/，不双写 k。',CREAK+[['creak + -ing → creaking','嘎吱响的过程、声音或状态']],
 'a creaking chair 是嘎吱响的椅子，the creaking of the stairs 是楼梯嘎吱声；也可比喻老系统吃力运转。',
 'creaking floorboards 嘎吱响的地板；creaking under the strain 重压下吃力运转。',
 'creaking 偏当前的响声、运作，creaky 常直接说东西容易这样响或显得老旧；两个形式有重合。',
 ('The creaking of the stairs woke me.','楼梯嘎吱的声音把我弄醒了。'),('He settled into a creaking wooden chair.','他在一把嘎吱响的木椅上坐下。'),sources=S('creaking','creak'))
W('creaky','/ˈkriːki/','容易嘎吱响的；老旧、运转不灵活的',
 '旧椅子、木楼梯一动就嘎吱响，叫 creaky；说制度、设施 creaky，则像旧机器一样不太灵活、跟不上需要。',
 'creak + 形容词后缀 -y；把嘎吱声变成经常表现的特点，再借这种老旧吃力的画面说系统。',CREAK+[['creak + -y → creaky','容易嘎吱响；比喻老旧、运行吃力']],
 'a creaky staircase 是容易嘎吱响的楼梯，a creaky system 是老旧、不灵活的系统；后一种不必真有声音。',
 'creaky floorboards 嘎吱响的地板；creaky infrastructure 老旧、运转吃力的基础设施。',
 'creaky 不只等于 old：新的东西也可能嘎吱响；比喻系统时，往往还嫌它迟缓、过时。',
 ('We climbed a narrow, creaky staircase.','我们走上一段狭窄、嘎吱响的楼梯。'),('The company still relies on a creaky booking system.','公司仍依赖一个老旧、不太灵活的预订系统。'),sources=S('creaky','creak'))
CRACKLE=[['古英语 cracian → crack；中古英语 crackelen → crackle','由啪响材料形成旧反复动作形式'],['现代 crackle 与 crackling 的扩展','接连噼啪声；紧张、兴奋感；烤肉脆皮有专门名词义']]
W('crackles','/ˈkrækəlz/','噼啪作响〔第三人称单数〕；一声声噼啪响',
 '柴火里接连冒出“啪、啪”的小爆裂声，用 crackles；收音机的电流杂音也能这样响。',
 'crackle + -s，保留 e，/l/ 后读 /z/；基础词里的旧 -le 已表达反复动作材料。',CRACKLE+[['crackle + -s → crackles','它接连噼啪响；多声小爆裂响']],
 'the fire crackles 是火噼啪响，crackles with excitement 还能比喻气氛兴奋、带电般活跃。',
 'crackles in the fireplace 在壁炉里噼啪响；static crackles 电流杂音噼啪响。',
 'cracks 可是一声啪或裂开，crackles 常是一连串小啪响；不要把“反复”丢掉。',
 ('The fire crackles softly in the fireplace.','壁炉里的火轻轻噼啪响。'),('The radio crackles whenever the train enters the tunnel.','火车每次进隧道，收音机就发出噼啪杂音。'),sources=S('crackles','crackle'))
W('crackled','/ˈkrækəld/','噼啪作响了；充满强烈张力、兴奋感',
 '火、纸或电流刚才连续噼啪响，叫 crackled；气氛像带电一样紧绷、兴奋，也能用它来写。',
 'crackle 去 e + 完整 -ed，/l/ 后读 /d/；不是 crack 直接加 -ed 的 cracked。',CRACKLE+[['crackle 去 e + -ed → crackled','过去接连噼啪响；比喻张力强烈']],
 'crackled in the hearth 是在炉里噼啪响，crackled with tension 是充满紧张感；比喻不必有真实电火花。',
 'crackled with excitement 兴奋感十足；crackled on the line 电话线路里噼啪杂响。',
 'crackled 与 cracked 不同：前者可只是小爆裂声，后者还常说物体裂了；纸噼啪响不一定撕裂。',
 ('Dry twigs crackled in the fire.','干树枝在火里噼啪作响。'),('The room crackled with excitement before the announcement.','消息公布前，房间里兴奋的气氛几乎要溢出来。'),sources=S('crackled','crackle'))
W('crackling','/ˈkræklɪŋ/','正在噼啪响；噼啪声；烤肉的脆皮〔尤指猪皮〕',
 '听火时，是一连串小小的“噼啪”；看烤猪肉时，crackling 又可指那层烤得酥脆的皮。场景换了，词性和具体意思也要跟着换。',
 'crackle 去 e + 完整 -ing；声音活动名词、分词之外，还发展出烹饪中的脆皮名词义，不能都按正在进行翻译。',CRACKLE+[['crackle 去 e + -ing → crackling','噼啪过程、响声；烤肉脆皮的名词用法']],
 'the crackling of the fire 是火的噼啪声，pork crackling 是烤猪皮；两义都能联想脆、细小爆裂的声音，但食物义是固定用法。',
 'a crackling fire 噼啪响的炉火；crisp crackling 酥脆的烤肉皮。',
 'a plate of crackling 里是食物，不是在吃“正在发声”这个动作；the crackling of logs 则是木柴燃烧声。',
 ('We listened to the crackling of the fire.','我们听着火的噼啪声。'),('The roast pork had a layer of crisp crackling.','烤猪肉外面有一层酥脆的皮。'),sources=S('crackling','crackle'))
RUSTLE=[['中古英语 rustling 等记录 → rustle 声音词','来源不完全确定，可能拟声；轻薄物移动时沙沙响'],['忙着弄来、赶快张罗及偷牲口的用法','可能另接美国西部忙着做事的词，甚至有 rush、hustle 混合分析；不硬说全从树叶声演变']]
W('rustle','/ˈrʌsəl/','沙沙响、使沙沙响；〔rustle up〕赶快张罗；偷牲口',
 '树叶、纸张、衣料轻轻摩擦出“沙沙”声，叫 rustle；rustle up a meal 则是赶快张罗一顿饭，要整体记这个搭配。',
 '声音词见中古英语 rustling 一系，可能拟声。忙着弄来、偷牲口等义可能有不同发展，不把它们编成树叶响一步步变成偷牛的确定故事。',RUSTLE,
 'the rustle of leaves 是树叶沙沙声，rustle some papers 是把纸弄得沙沙响；rustle up something to eat 是很快找点吃的。',
 'a soft rustle 轻轻的沙沙声；rustle up dinner 赶快张罗晚饭。',
 'rustle 的 t 通常不发音，读 /ˈrʌsəl/；rust 生锈的 t 发音。二者近形，不能据此拆成 rust + le 来解释树叶声。',
 ('We heard the rustle of leaves beside the path.','我们听见小路旁树叶沙沙响。'),('I can rustle up a quick lunch from what is in the fridge.','我能用冰箱里的东西很快张罗一顿午饭。'),sources=S('rustle','rustle'))
W('rustles','/ˈrʌsəlz/','沙沙响、使沙沙响〔第三人称单数〕；沙沙声〔复数〕；赶快张罗',
 '纸张、衣服一动就轻轻“沙沙”响，用 rustles。若接 up 一顿饭、一笔钱等，则看赶快张罗的搭配。',
 'rustle + -s，保留 e，/l/ 后读 /z/；t 仍不发音。声音名词复数也可用这一形式。',RUSTLE+[['rustle + -s → rustles','它沙沙响；多阵沙沙声；他、她赶快张罗']],
 'rustles in the breeze 是微风里沙沙响，rustles up a meal 是赶快张罗一餐；不能把 up 忽略。',
 'rustles softly 轻轻沙沙响；faint rustles 隐约的沙沙声。',
 'rustles 多是轻薄物摩擦声，rattles 更像硬物连续碰撞；两者中文都可写响，画面却不同。',
 ('Her coat rustles as she walks.','她走路时，外套沙沙作响。'),('On busy evenings, he rustles up a simple meal.','忙碌的晚上，他就很快张罗一顿简单饭菜。'),sources=S('rustles','rustle'))
W('rustled','/ˈrʌsəld/','沙沙响了、使沙沙响了；赶快张罗了；偷了牲口',
 '树叶、衣料刚才轻轻摩擦了一阵，用 rustled；接 up 时则可以说很快弄来、备好东西。偷牲口义看相应情境另分。',
 'rustle 去 e + 完整 -ed，/l/ 后读 /d/；t 不发音，不能按字母 t 去把词尾读成 /ɪd/。',RUSTLE+[['rustle 去 e + -ed → rustled','过去沙沙响；张罗、偷牲口等用法另按情境理解']],
 'rustled the papers 是翻得纸沙沙响；rustled up some sandwiches 是赶快弄了几个三明治。',
 'rustled in the wind 在风中沙沙响；rustled up some cash 很快凑来一点钱。',
 'rustled up 不是“往上沙沙响”；这个固定搭配写快速张罗、弄到，不能逐字硬翻。',
 ('The leaves rustled in the evening breeze.','树叶在晚风里沙沙作响。'),('She rustled up some sandwiches before we left.','我们离开前，她很快做了几个三明治。'),sources=S('rustled','rustle'))
W('rustling','/ˈrʌslɪŋ/','正在沙沙响；沙沙声；赶快张罗、偷牲口的活动',
 '轻薄的叶子、纸或衣料正一阵阵摩擦，叫 rustling。听起来细碎、轻，不像硬物哐当撞。',
 'rustle 去 e + 完整 -ing，t 不发音；早期已有相应分词记录，现代规则拆分不代表历史记录一定先有基础词。',RUSTLE+[['rustle 去 e + -ing → rustling','沙沙响的过程、声音；其他动词义也可变化']],
 'the rustling of leaves 是树叶沙沙声；rustling up lunch 是赶快张罗午饭；cattle rustling 是偷牲口活动。',
 'rustling paper 沙沙响的纸；a faint rustling 细微的一阵沙沙声。',
 '声音词 rustling 与 cattle rustling 的近源分析不宜混成一条确定故事；具体句子仍要按搭配辨义。',
 ('The rustling of paper broke the silence.','纸张沙沙的声音打破了寂静。'),('We could hear something rustling in the bushes.','我们听见灌木丛里有什么在沙沙动。'),sources=S('rustling','rustle'))
RUMBLE=[['中古英语 rumblen → rumble','低沉、连续的声响材料，大概拟声，与其他日耳曼语相近形式可比较'],['雷、车轮、腹部等低声 → 动作、比喻','隆隆、咕噜；也可带着这种声音移动，不限定一个声源']]
W('rumbles','/ˈrʌmbəlz/','隆隆响、咕噜响〔第三人称单数〕；一阵阵隆隆声',
 '远雷在低处滚，重车低低响过，或肚子“咕噜”一响，用 rumbles。共同点是低沉、带滚动感。',
 'rumble + -s，保留 e，/l/ 后读 /z/。名词复数则数一阵阵隆隆声。',RUMBLE+[['rumble + -s → rumbles','它隆隆、咕噜响；多阵低沉声']],
 'thunder rumbles 是雷隆隆响，my stomach rumbles 是肚子咕噜叫；rumbles in the distance 是远处几阵低响。',
 'distant rumbles 远处隆隆声；rumbles past 隆隆响着经过。',
 'rumbles 偏低沉、持续，clinks 偏轻脆短响；中文都写“响”会丢掉英语选词的听感。',
 ('My stomach rumbles when I miss breakfast.','我没吃早饭时，肚子会咕噜叫。'),('We heard distant rumbles of thunder.','我们听见远处阵阵低沉雷声。'),sources=S('rumbles','rumble'))
W('rumbled','/ˈrʌmbəld/','隆隆、咕噜地响了；隆隆响着移动了；〔英口语〕识破了',
 '雷声刚才低低滚过，或一辆重车带着低沉声驶过，用 rumbled。它常把声响和移动一起打包。',
 'rumble 去 e + 完整 -ed，/l/ 后读 /d/；已有 mb 的 /mb/ 保留，不把 b 当哑字母。',RUMBLE+[['rumble 去 e + -ed → rumbled','过去低沉作响、隆隆移动']],
 'rumbled in the distance 是远处雷声隆隆，rumbled past 是隆隆驶过；写人低声说话时也可借这种深沉听感。',
 'rumbled along the road 沿路隆隆驶过；rumbled beneath our feet 脚下隆隆响。',
 '英口语 We have been rumbled 是我们被识破了，不是真有人在隆隆响。这个固定用法另记，不硬编成已确定的声音演化链。',
 ('Thunder rumbled beyond the hills.','山那边雷声隆隆。'),('A heavy lorry rumbled past the house.','一辆重型卡车隆隆驶过屋旁。'),('We have been rumbled; she knows about the surprise party.','我们被识破了；她已经知道惊喜派对的事。'),sources=S('rumbled','rumble')+['https://dictionary.cambridge.org/us/dictionary/english/rumbled'])
W('rumbling','/ˈrʌmblɪŋ/','正在隆隆、咕噜响；低沉连续的声响；隆隆响着移动',
 '低沉声音正滚动、持续，叫 rumbling。远雷、车轮、肚子都能成为声源，听感像在低处“隆隆”推进。',
 'rumble 去 e + 完整 -ing，常读 /ˈrʌmblɪŋ/；基础词里的 b 发音，不按 thumb 的 mb 处理。',RUMBLE+[['rumble 去 e + -ing → rumbling','低沉作响的过程、声音与状态']],
 'a rumbling stomach 是咕噜叫的肚子，the rumbling of thunder 是隆隆雷声；也能修饰深沉的声音。',
 'low rumbling 低沉隆隆声；a rumbling train 隆隆行驶的火车。',
 'rumbling 常给人持续、滚动感；a bang 更像突然一记巨响。描述同一场雷雨，可以按声音变化选不同词。',
 ('The rumbling of thunder grew louder.','隆隆雷声越来越响。'),('His rumbling stomach made us both laugh.','他的肚子咕噜叫，让我们俩都笑了。'),sources=S('rumbling','rumble'))
CLINK=[['中古英语 clinken 等 → clink','金属、玻璃清脆短响；大概拟声，与日耳曼语相近响声词可比较'],['动词 → 声音名词','轻轻一碰发“叮”声；另有监狱口语义，联系特定旧狱名，具体更早命名有分析分歧']]
W('clink','/klɪŋk/','叮地碰响；轻轻碰杯；一声清脆碰响',
 '两只玻璃杯轻轻一碰“叮”一声，或硬币、钥匙小小碰响，就是 clink。比 clank 更轻、比 clang 更不轰亮。',
 '接中古英语 clinken 一类拟声材料；可与荷兰语、德语的鸣响词比较，不必硬写成从现代 clank 直接变元音。',CLINK,
 'clink glasses 是碰杯，the clink of coins 是硬币清脆碰响；in the clink 另是坐牢的口语，联系旧监狱名。',
 'a gentle clink 轻轻一声叮响；clink against glass 碰玻璃叮响。',
 'clink 通常是轻脆的硬物碰响，clank 更沉硬；不是所有“金属声”都要译成哐当。',
 ('They raised their glasses and gave them a gentle clink.','他们举杯，轻轻碰出一声叮响。'),('We heard the coins clink as he counted them.','他数硬币时，我们听见清脆的碰响。'),sources=S('clink','clink'))
W('clinks','/klɪŋks/','叮地碰响〔第三人称单数〕；一声声清脆碰响',
 '勺子轻碰杯口、钥匙相互碰到，发出“叮”声，用 clinks；复数名词是几声轻脆响。',
 'clink + -s，/k/ 后读 /s/；nk 的 /ŋk/ 留下，不把 k 省掉。',CLINK+[['clink + -s → clinks','它叮响；多声轻脆碰响']],
 'clinks against the cup 是碰杯子叮响，soft clinks 是轻轻的碰响；短、轻、硬是常见听感。',
 'clinks gently 轻轻叮响；the clinks of glasses 杯子的碰响。',
 'clinks 可以是一下一下的碰杯声；jingles 更容易让人想到小铃、钥匙连着叮当响。',
 ('The spoon clinks against the rim of the cup.','勺子碰到杯沿，叮地响。'),('Soft clinks of glass came from the dining room.','餐厅传来几声轻轻的玻璃碰响。'),sources=S('clinks','clink'))
W('clinked','/klɪŋkt/','叮地碰响了；轻轻碰杯了',
 '两只杯子、几枚硬币刚才清清脆脆碰了一下，叫 clinked。声音小而亮，不像重铁门哐当关上。',
 'clink + 完整 -ed，/k/ 后读 /t/，结尾 /ŋkt/；仍是一个音节。',CLINK+[['clink + -ed → clinked','过去轻脆碰响、碰杯']],
 'clinked glasses 是碰了杯，clinked against the bottle 是碰到瓶子叮响；可写主动碰，也可写东西自己碰响。',
 'clinked gently 轻轻碰响；clinked together 相碰叮响。',
 'clinked glasses 写具体的碰杯动作和响声；drank a toast 写举杯祝酒，未必强调杯子相碰。',
 ('We clinked glasses to celebrate the opening.','我们碰杯庆祝开业。'),('The coins clinked together in his pocket.','硬币在他口袋里碰得叮响。'),sources=S('clinked','clink'))
W('clinking','/ˈklɪŋkɪŋ/','正在叮地碰响、碰杯；清脆碰响声',
 '杯子、硬币、钥匙的轻脆碰响正接连发生，是 clinking。常是餐厅、宴会或小金属物件移动的背景声。',
 'clink + 完整 -ing，直接加；/ŋk/ 保留，听感与 clanging、clanking 各有轻重、共鸣差别。',CLINK+[['clink + -ing → clinking','轻脆碰响的过程、声音']],
 'the clinking of glasses 是杯子相碰的清脆声，clinking coins 是碰得响的硬币；碰杯动作也能用进行式。',
 'glasses clinking 杯子叮地碰响；a gentle clinking 轻轻一阵叮响。',
 'clinking 不自动表示庆祝：餐具收拾、硬币计数也会响。庆祝的画面来自酒杯、祝词等上下文。',
 ('The clinking of glasses filled the dining room.','餐厅里满是杯子清脆的碰响。'),('She walked towards us with coins clinking in her pocket.','她向我们走来，口袋里的硬币叮叮碰响。'),sources=S('clinking','clink'))
JINGLE=[['中古英语 gingeln 等 → jingle','小金属、小铃连续轻脆鸣响，大概拟声'],['动词 → 声音名词 → 好记的韵句、广告短曲','从叮当声到朗朗上口的短句、旋律；不等于原本由 jangle 规则变来']]
W('jingle','/ˈdʒɪŋɡəl/','叮当响、摇得叮当响；叮当声；广告短歌、好记的短曲',
 '小铃、钥匙接连“叮叮当当”，叫 jingle；广告里那段短短、好记、会在脑中转的旋律，也叫 a jingle。',
 '承中古英语 gingeln 一系拟声材料；声音名词后来扩到朗朗上口的韵句、广告短歌。与 jangle 近形，不代表原本同一个来源。',JINGLE,
 'jingle the keys 是把钥匙摇得叮当响；an advertising jingle 是广告短歌，不是所有歌曲的通称。',
 'the jingle of bells 小铃叮当声；a catchy jingle 朗朗上口的广告短曲。',
 'jingle 常让人想到小金属连续清脆响；jangle 常更杂、更刺耳。广告短歌义则是固定名词用法。',
 ('We heard the jingle of bells as the door opened.','门打开时，我们听见小铃叮当响。'),('I could not get the advertising jingle out of my head.','那段广告短歌一直在我脑子里转。'),sources=S('jingle','jingle'))
W('jingles','/ˈdʒɪŋɡəlz/','叮当响、摇得响〔第三人称单数〕；广告短曲、叮当声〔复数〕',
 '钥匙、小铃动起来连续叮当响，用 jingles；名词复数也能说几段广告短歌。',
 'jingle + -s，保留 e，/l/ 后读 /z/。ng 在这个基础词里有 /ŋɡ/，与单音节 ring 的 /ŋ/ 不同。',JINGLE+[['jingle + -s → jingles','它叮当响；多段广告短歌、多阵叮当声']],
 'jingles in her pocket 是在口袋里叮当响，writes jingles 是写广告短歌；主语、宾语让两义很清楚。',
 'jingles cheerfully 清脆叮当响；radio jingles 电台广告短曲。',
 'jingles 作广告名词时通常很短、强调好记；songs 范围更广，不一定有广告功能。',
 ('The little bell jingles whenever the cat moves.','猫每次一动，小铃就叮当响。'),('She writes jingles for radio advertisements.','她为电台广告写短歌。'),sources=S('jingles','jingle'))
W('jingled','/ˈdʒɪŋɡəld/','叮当响了；摇得叮当响了',
 '一串钥匙、几只小铃刚才清脆地连着响，叫 jingled。人摇它们，也能把发声物作宾语。',
 'jingle 去 e + 完整 -ed，/l/ 后读 /d/；保留基础词的 /ŋɡ/。',JINGLE+[['jingle 去 e + -ed → jingled','过去叮当响或使其响']],
 'jingled the keys 是摇响钥匙，bells jingled 是铃自己响；都保留轻脆、连续的叮当感。',
 'jingled in his pocket 在口袋里叮当响；jingled softly 轻轻叮当响。',
 'jingled 不一定像大钟那样轰亮；小铃、钥匙、硬币的连续清脆声更典型。',
 ('He jingled the keys to show that he was ready to leave.','他摇得钥匙叮当响，表示准备走了。'),('The bells jingled as the sleigh moved forward.','雪橇向前移动，小铃叮当响。'),sources=S('jingled','jingle'))
W('jingling','/ˈdʒɪŋɡlɪŋ/','正在叮当响；叮当的；连续清脆响声',
 '小铃、钥匙一边晃一边清脆连响，是 jingling。它常把轻快的声音铺成场景背景。',
 'jingle 去 e + 完整 -ing，常读 /ˈdʒɪŋɡlɪŋ/；保留 g 音，不仿照 ring 只读 /ŋ/。',JINGLE+[['jingle 去 e + -ing → jingling','连续叮当的过程、状态']],
 'jingling keys 是叮当响的钥匙，the jingling of bells 是铃的叮当声；也可写人正在把钥匙摇响。',
 'jingling in a pocket 在口袋里叮当响；jingling bells 叮当响的小铃。',
 'jingling 常清脆轻快，jangling 常更杂乱扎耳；同一串钥匙摇的方式不同，也能产生不同听感。',
 ('The jingling of bells announced their arrival.','一阵小铃叮当声传来，表示他们到了。'),('She stood at the door, jingling the keys in her hand.','她站在门口，把手里的钥匙摇得叮当响。'),sources=S('jingling','jingle'))
JANGLE=[['古法语 jangler、jangle → 中古英语 jangeln、jangle','早期多指闲扯、争吵；更远或属日耳曼拟声材料'],['后来发展出不和谐、刺耳的碰响','也可把心神搅乱，常见于 nerves 神经的搭配']]
W('jangle','/ˈdʒæŋɡəl/','刺耳、杂乱地叮当响；使心烦意乱；杂乱刺耳声',
 '钥匙被用力乱晃，金属“叮叮哐哐”搅在一起，有点扎耳朵，像 jangle；也能比喻声音把人弄得心烦意乱。',
 '经古法语 jangler、jangle 借入，早期有闲扯、争吵义，后来发展出刺耳响声。不能只因音近就说从现代 jingle 变来。',JANGLE,
 'jangle the keys 是把钥匙摇得乱响；jangle someone’s nerves 是让人神经紧绷、心烦不安。',
 'a jangle of bells 一阵杂乱铃响；jangled nerves 紧绷不安的神经。',
 'jingle 常偏清脆轻快，jangle 常偏杂乱刺耳；两词近形，实际历史并没有可确定的直接母子关系。',
 ('He gave the keys an impatient jangle.','他不耐烦地把钥匙摇得叮当乱响。'),('Sudden alarms can jangle your nerves.','突如其来的警报会让人心神紧张。'),sources=S('jangle','jangle'))
W('jangles','/ˈdʒæŋɡəlz/','杂乱刺耳地叮当响、使心烦〔第三人称单数〕；杂乱铃响〔复数〕',
 '钥匙、铃或别的金属东西一晃就乱响，用 jangles；声音、事件使人心神不定，也能进入这个动词的比喻用法。',
 'jangle + -s，保留 e，/l/ 后读 /z/；ng 在基础词里读 /ŋɡ/。',JANGLE+[['jangle + -s → jangles','它杂乱叮当；它使心烦；多阵杂响']],
 'jangles in her hand 是在她手里乱响，jangles my nerves 是让我心神不宁；nerves 提示心理比喻。',
 'jangles loudly 刺耳叮当响；jangles against the gate 碰大门杂乱作响。',
 'jangles 不只是音量大，还常有不协调、刺耳感；a bell rings 则可以是中性地说铃响。',
 ('The loose chain jangles against the gate.','松动的铁链碰着大门，叮当乱响。'),('That sharp alarm jangles my nerves every morning.','那刺耳的警报每天早上都把我弄得心神不宁。'),sources=S('jangles','jangle'))
W('jangled','/ˈdʒæŋɡəld/','杂乱刺耳地响了；心神紧绷、不安的',
 '金属刚才被摇得乱响，叫 jangled；jangled nerves 则像神经被猛晃了一阵，紧张、烦乱，安定不下来。',
 'jangle 去 e + 完整 -ed，/l/ 后读 /d/；作形容用法时仍保留“被搅乱”的结果感。',JANGLE+[['jangle 去 e + -ed → jangled','过去刺耳碰响；被搅得紧绷不安']],
 'jangled the keys 是把钥匙摇得乱响，soothe jangled nerves 是安抚紧绷的神经、让人放松；不是神经真发金属声。',
 'jangled loudly 刺耳地响了；her jangled nerves 她紧张烦乱的心神。',
 'jangled nerves 比 damaged nerves 更像情绪、心神受扰的说法，不能自动理解成身体组织损伤。',
 ('He jangled the keys impatiently.','他不耐烦地把钥匙摇得乱响。'),('A quiet walk helped soothe my jangled nerves.','安静散步让我紧张烦乱的心神缓了下来。'),sources=S('jangled','jangle'))
W('jangling','/ˈdʒæŋɡlɪŋ/','正在杂乱刺耳地叮当响；使人烦乱的；杂乱响声',
 '一串金属声音正乱响、扎耳朵，叫 jangling；也能描述让人心神紧绷的刺激感。',
 'jangle 去 e + 完整 -ing，常读 /ˈdʒæŋɡlɪŋ/。ng 的 /ŋɡ/ 保留，旧法语基础已成完整英语词。',JANGLE+[['jangle 去 e + -ing → jangling','杂乱叮当的过程；扰乱心神的状态']],
 'jangling keys 是乱响的钥匙，jangling bells 是杂乱响的铃；the jangling of metal 把声音整体提出来。',
 'jangling in his hand 在他手里叮当乱响；a jangling noise 刺耳杂响。',
 'jangling 与 jingling 都可写钥匙、铃声；前者更容易有乱、刺耳的评价，后者更常显得轻脆。',
 ('The jangling of keys distracted me from my work.','钥匙叮当乱响，让我工作分了神。'),('The cart passed with bells jangling on its harness.','车经过时，挽具上的铃铛叮当乱响。'),sources=S('jangling','jangle'))
TINKLE=[['中古英语 tinklen → tinkle','大概是较早 tink、tinken 的反复动作形式，最终有拟声基础'],['细小叮声 → 声音名词及后来口语用途','轻细铃声、玻璃碰响；儿童式口语还用来委婉说撒尿']]
W('tinkle','/ˈtɪŋkəl/','叮叮轻响；一阵轻细铃响；〔儿童式口语〕撒尿',
 '小铃或薄玻璃发出轻轻细细的“叮叮”，像 tinkle。它比沉重的金属哐当声小、亮、轻。',
 '大概由较早 tink、tinken 的鸣响材料加旧反复动作形式而来；后来儿童式口语借来委婉说撒尿。',TINKLE,
 'a tinkle of glass 是玻璃轻响，bells tinkle 是小铃叮叮；have a tinkle 在儿童式口语里是撒个尿，不是一般正式表达。',
 'a faint tinkle 隐约的细铃声；tinkle gently 轻轻叮响。',
 'tinkle、clink 都轻脆，tinkle 更容易表现接连细铃声；在孩子说尿尿的场景，要换到固定的委婉口语义。',
 ('We heard a faint tinkle of glass from the next room.','我们听见隔壁玻璃轻轻叮响。'),('The child said he needed to have a tinkle before we left.','孩子说出发前要先尿个尿。'),sources=S('tinkle','tinkle'))
W('tinkles','/ˈtɪŋkəlz/','叮叮轻响〔第三人称单数〕；细小铃响〔复数〕；〔儿童式口语〕撒尿',
 '小铃、玻璃饰物一动就细细叮响，用 tinkles；作复数名词则是几声轻细响。尿尿的口语义要看场景。',
 'tinkle + -s，保留 e，/l/ 后读 /z/；三单、声音名词复数同形。',TINKLE+[['tinkle + -s → tinkles','它轻细叮响；数声细响；其他动词义的三单']],
 'tinkles in the breeze 是微风里叮叮响，soft tinkles 是几声轻轻细响；常见主语有铃、玻璃或小饰物。',
 'tinkles softly 轻细叮响；the tinkles of a small bell 小铃的细响。',
 'tinkles 比 clangs 更容易让人想到轻、小、细的铃声；不是“所有铃响”的唯一说法。',
 ('The small bell tinkles whenever the door opens.','门每次打开，小铃就轻轻叮响。'),('Soft tinkles came from the glass ornaments by the window.','窗边的玻璃饰物传来几声轻细叮响。'),sources=S('tinkles','tinkle'))
W('tinkled','/ˈtɪŋkəld/','叮叮轻响了；〔儿童式口语〕撒尿了',
 '轻细铃声、玻璃碰声刚才叮叮响起，叫 tinkled。写孩子时也可能是尿尿的委婉说法，先看上下文。',
 'tinkle 去 e + 完整 -ed，/l/ 后读 /d/；基础词的 /ŋk/ 保留。',TINKLE+[['tinkle 去 e + -ed → tinkled','过去轻细叮响；另有口语撒尿义']],
 'bells tinkled 是小铃轻响，glasses tinkled 是杯子清脆轻碰；声响通常比 clanked 的金属哐当轻。',
 'tinkled softly 轻轻叮响；tinkled in the breeze 在微风里细细响。',
 'tinkled 的轻细感来自声音词本身，不能把它译成震耳欲聋；要保留小而亮的听感。',
 ('The little bells tinkled as the cat walked past.','猫走过时，小铃轻轻叮响。'),('The glasses tinkled as she set them on the tray.','她把杯子放到托盘上，杯子轻轻叮地碰响。'),sources=S('tinkled','tinkle'))
W('tinkling','/ˈtɪŋklɪŋ/','正在轻细叮响；轻细铃声、清脆声；〔儿童式口语〕撒尿',
 '耳边正是一阵轻轻细细、亮亮的叮声，是 tinkling。也可形容像小铃一样清脆的笑声或琴声。',
 'tinkle 去 e + 完整 -ing，常读 /ˈtɪŋklɪŋ/；同时可作声音名词或修饰语，不全是正在进行时。',TINKLE+[['tinkle 去 e + -ing → tinkling','轻细鸣响的过程、声音；相应口语义也可变化']],
 'the tinkling of bells 是小铃细响，tinkling laughter 是清脆笑声；若在儿童如厕语境，才另按尿尿理解。',
 'tinkling glasses 轻脆碰响的杯子；a tinkling piano melody 清脆轻巧的钢琴旋律。',
 'tinkling laughter 是把铃声般的清脆感借给笑声，不表示有人真的拿铃铛；形象可以跨声源使用。',
 ('The tinkling of bells drifted through the open window.','小铃的细响从敞开的窗户飘进来。'),('Her tinkling laughter made us smile.','她清脆的笑声让我们也笑了。'),sources=S('tinkling','tinkle'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfb',ROOTS,WORDS)
 extend_lessons()
