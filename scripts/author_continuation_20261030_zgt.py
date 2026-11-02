"""Quavering, quaking and different kinds of unsteadiness."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1697':dict(words='quaver quavers quavered quavering'.split(),label='quaver 的旧 -er：反复颤动，不是做事的人',note='quaver 可能承旧 cwavien 颤动材料加反复动作尾，远源可能拟声；八分音符名词由这一动词发展。相同 -er 外形不能一律译为某某者。'),
 'A1741':dict(words='quake quakes quaked quaking earthquake'.split(),label='quake：地面震、人发抖；earthquake 再加 earth',note='quake 承古英语 cwacian，早期已有地面震动、身体颤抖材料，最远来源未定。现代名词 quake 常缩自 earthquake，但 quake 动词并非现代把 earthquake 截短才有。'),
 'B2969':dict(words='shake shaky shakier shakiest shakily shakiness'.split(),label='shaky：身体、结构、论据都可能缺稳定',note='shaky 接 shake 与 -y；木材裂隙等较早材料和抽象不可靠义都很早，学习画面可以从不稳来串联，不把具体、抽象硬排成唯一先后。'),
 'A1699':dict(words='wobble wobbly wobblier wobbliest wobbliness'.split(),label='wobbly：支撑不稳，左右晃',note='wobble 可能借低地德语 wabbeln，旧拼法 wabble 更早；wobbly 去 e 加 -y，再有比较、最高级和 -ness，不把 -ly 误判为普通副词尾。'),
 'C1542':dict(words='tremulous tremulously tremulousness'.split(),label='tremulous：从拉丁颤抖性质到副词、名词',note='tremulous 借拉丁 tremulus，和 tremble 共享材料但有自己的借入路线；再加 -ly、-ness 是英语中的扩展。'),
}
QUAVER=[['旧 cwavien 等颤抖材料 → quaveren、quaver','可能有反复动作尾，远源可能拟声，不能把 quav 说成现代独立英语词'],['颤动、声音发颤 → 名词颤音与音乐八分音符','八分音符名词记录早于某些声音一颤名词记录，不按现代讲解顺序倒排']]
QUAKE=[['古英语 cwacian → 中古英语 quaken → quake','地面震、身体发抖等旧用法，最远来源未定'],['quake 动词、名词；earth + quake → earthquake','现代单独名词 quake 常是 earthquake 的缩称，不意味着古老动词由现代长词才造出']]
SHAKY=[['古英语 sceacan 等 → shake','摇、晃、震动；也可让信心、秩序不稳'],['shake + -y → shaky','木材裂隙、不可靠、身体不稳等早期用法分别发展，不硬按先物理后抽象排年代']]
WOBBLY=[['旧拼法 wabble → wobble','可能借低地德语 wabbeln，来回摆的更远材料与 weave 联系只是可能分析'],['wobble + -y → wobbly','桌腿、轮子等松晃，也写心里、决定不够稳；现代再接比较或名词词尾']]
TREMULOUS=[['拉丁 tremere → tremulus → 英语 tremulous','颤抖的、不稳的，与 tremble 同族但独立借入'],['tremulous 接 -ly、-ness','发颤地；发颤、不稳的性质，仍保留书面、叙事色彩']]
W('quaver','英 /ˈkweɪvə/；美 /ˈkweɪvər/','声音发颤；微颤；颤音；八分音符〔英式音乐术语〕',
 '努力说稳，尾音却一颤一颤，这声音会 quaver；音乐里 a quaver 在英式叫八分音符，不是只有唱得发抖才算这个音符。',
 '可能承旧 cwavien 颤动材料的反复形式，远源可能拟声；名词颤音、八分音符由动词发展，不能把 -er 当人名尾。',QUAVER,
 'a quaver in the voice 声音里一丝颤；voice begins to quaver 声音开始发颤。',
 'play a quaver 演奏一个八分音符；quaver with emotion 激动得声音发颤。',
 'a quaver 是英式八分音符，美式常说 an eighth note；它标记时值，不直接保证音高、音量或唱得颤。',
 ('Her voice began to quaver as she spoke.','她说着说着，声音开始发颤。'),('The score calls for a quaver followed by a rest.','谱面要求先奏一个八分音符，再休止。'),sources=S('quaver','quaver'))
W('quavers','英 /ˈkweɪvəz/；美 /ˈkweɪvərz/','声音发颤〔第三人称单数〕；颤音、八分音符〔复数〕',
 '他的嗓音一谈到家人就抖，是 his voice quavers；乐谱上一串八分音符，则是 quavers。名词音乐义不等于所有声音都不稳定。',
 'quaver + -s，读 /z/；动词三单与不同名词义的复数同形。',QUAVER+[['quaver + -s → quavers','声音发颤；多个八分音符、颤音']],
 'a pair of quavers 两个八分音符；his voice quavers 他的声音发颤。',
 'quavers with emotion；a passage of quavers 一段八分音符。',
 'quavers 写时值，quivering 写颤动；八分音符可以弹得很稳，不必字面模仿动词发抖。',
 ('His voice quavers when he talks about home.','他谈到家时，声音会发颤。'),('The melody begins with two quavers.','旋律以两个八分音符开始。'),sources=S('quavers','quaver'))
W('quavered','英 /ˈkweɪvəd/；美 /ˈkweɪvərd/','声音发颤了；颤着声说了',
 '一句话说出口，尾音不稳、像压着情绪，是 quavered；叙事里也能直接接引语，表示颤声说。',
 'quaver + 完整 -ed，读 /d/；规则过去形式，承颤动到声音颤动的动词支线。',QUAVER+[['quaver + -ed → quavered','过去声音发颤，或颤声说']],
 'her voice quavered 她的声音发颤了；quavered with fear 怕得声音发颤。',
 'quavered an answer 颤声回答；the final note quavered 尾音发颤。',
 'quavered 常突出嗓音不稳，whispered 是低声耳语；声音可以轻但稳定，也可以轻且发颤。',
 ('“Are you sure?” she quavered.','“你确定吗？”她颤声问。'),('His voice quavered on the final word.','他说到最后一个词时，声音发颤了。'),sources=S('quavered','quaver'))
W('quavering','英 /ˈkweɪvərɪŋ/；美 /ˈkweɪvərɪŋ/','声音发颤的；正在颤声说、唱',
 '话不是平稳出来，而是尾音细细摇，叫 a quavering voice。它常在故事里把紧张、激动、虚弱等表现写进声音。',
 'quaver + -ing；动作形式也可作形容词，描述声音里颤动、不稳的性质。',QUAVER+[['quaver + -ing → quavering','声音发颤的过程或性质']],
 'a quavering voice 发颤的声音；a quavering note 颤动的音。',
 'quavering with emotion；a quavering reply 颤声回答。',
 'quavering voice 可以透露不稳，loud voice 只说明声音大；大声也会发颤，不是固定反义。',
 ('He answered in a quavering voice.','他用发颤的声音回答。'),('The singer held a long, quavering note.','歌手拖住一个长长的颤音。'),sources=S('quavering','quaver'))
W('quake','/kweɪk/','震动、发抖；地震〔earthquake 的常用缩称〕',
 '地面震起来，或人怕得身体发抖，都能 quake；新闻里的 a quake 多是一次地震。可以用同一个震动意象串起来，但动词比现代缩称古老。',
 '承古英语 cwacian 地面震、身体颤动材料，远源未定。名词早有颤动义，现代地震名词常缩自 earthquake，不能倒说古老动词来自现代长词缩短。',QUAKE,
 'quake with fear 吓得发抖；quake in your boots 吓得直哆嗦；a powerful quake 强烈地震。',
 'the ground began to quake 地面开始震动；a quake struck 发生地震。',
 'quake 可以说身体发抖，earthquake 才明确地震；he was quaking 不应译成他在发生地震。',
 ('The ground began to quake beneath our feet.','我们脚下的地面开始震动。'),('The museum reopened months after the quake.','地震几个月后，博物馆重新开放。'),sources=S('quake','quake'))
W('quakes','/kweɪks/','震动、发抖〔第三人称单数〕；地震〔复数〕',
 '地面一阵阵震，动词可用 quakes；几次地震则是名词 quakes。动作、事件都围绕震动，但句法角色不同。',
 'quake + -s，/k/ 后读 /s/；古老动词三单与现代常缩自 earthquake 的名词复数同形。',QUAKE+[['quake + -s → quakes','它震动、发抖；多次地震']],
 'minor quakes 小地震；the ground quakes 地面震动；quakes with fear 吓得发抖。',
 'frequent quakes；a region prone to quakes 地震多发地区。',
 'the ground quakes 是主语加动词，several quakes 是数量加事件名词；不能把每个 s 都当多个对象。',
 ('Several small quakes were recorded overnight.','夜间记录到了几次小地震。'),('He quakes at the thought of speaking to such a large audience.','一想到要对这么多观众讲话，他就吓得发抖。'),sources=S('quakes','quake'))
W('quaked','/kweɪkt/','震动了；发抖了',
 '爆炸震得窗户、地面晃一下，或人心里很怕、身体直抖，过去发生了就是 quaked。',
 'quake 去 e 加完整 -ed，/k/ 后读 /t/；现代常用规则过去式，不必套古代曾有的其他变化。',QUAKE+[['quake → quaked','过去震动或身体发抖']],
 'quaked with fear 怕得发抖；the building quaked 楼房震动。',
 'quaked beneath our feet；quaked at the prospect 一想到前景就发怵。',
 'quaked 只写震动，不保证造成破坏；collapsed 才明确倒塌，别把震一下自动写成塌下来。',
 ('The windows quaked as the heavy trucks passed.','重型卡车经过时，窗户震动起来。'),('She quaked with fear before stepping onto the stage.','上台前，她怕得直发抖。'),sources=S('quaked','quake'))
W('quaking','/ˈkweɪkɪŋ/','正在震动；发抖、害怕得哆嗦的',
 '脚下地面正晃，是 quaking；人被吓得站在那里直哆嗦，也能这样说。它可写过程或人的当下状态。',
 'quake 去 e 加 -ing；动作形式也可作形容词，接古老地面、身体颤动材料。',QUAKE+[['quake → quaking','震动、发抖的过程或性质']],
 'quaking with fear 吓得发抖；quaking in his boots 吓得直哆嗦。',
 'a quaking voice 发颤的声音；quaking ground 震动的地面。',
 'quaking in your boots 可以夸张地说害怕，不要求真的穿靴子；但反讽句可能用来表示根本没被吓住，仍要看语气。',
 ('The children were quaking with fear during the storm.','暴风雨中，孩子们吓得直发抖。'),('He admitted that he had been quaking in his boots before the interview.','他承认，面试前自己怕得直哆嗦。'),sources=S('quaking','quake'))
W('shakier','英 /ˈʃeɪkiə/；美 /ˈʃeɪkiər/','更发抖、不稳的；更薄弱、不可靠的',
 '手比刚才更抖，是 shakier；一个解释的依据更站不稳，也像支架晃得更厉害，叫 shakier。',
 'shaky 的 y 变 i 加完整 -er；内层 shake 去 e 加 -y，比较稳定、可信的程度。具体、抽象用法都很早，不按记忆意象硬排年代。',SHAKY+[['shaky → shakier','身体更颤、结构更不稳；论据等更薄弱']],
 'shakier hands 更发抖的手；on shakier ground 依据更薄弱、处境更不稳。',
 'a shakier argument；confidence grew shakier。',
 'shakier evidence 是可靠性更低，不是证据纸张在发抖；比较句的对象决定是物理还是抽象。',
 ('My hands became shakier as I grew more nervous.','我越紧张，手就抖得越厉害。'),('His explanation looked shakier after we checked the figures.','核对数字后，他的解释显得更站不住脚。'),sources=S('shakier','shaky'))
W('shakiest','/ˈʃeɪkiɪst/','最发抖、不稳的；最薄弱、不可靠的',
 '几处理由里最撑不起结论的，是 the shakiest part；身体动作也可在某一时刻抖得最厉害。',
 'shaky 的 y 变 i 加完整 -est；在所比范围内，不稳、缺把握的程度最高。',SHAKY+[['shaky → shakiest','最不稳、最缺乏可靠支撑']],
 'the shakiest argument 最站不住脚的论证；the shakiest part 最薄弱的部分。',
 'our shakiest assumption；the shakiest table。',
 'shakiest assumption 是依据最薄弱，不是一定已被证明错误；uncertain 与 false 的判断层次要分开。',
 ('This is the shakiest assumption in the whole plan.','这是整个计划中依据最薄弱的假设。'),('We put the shakiest table against the wall.','我们把最不稳的那张桌子靠墙放了。'),sources=S('shakiest','shaky'))
W('shakily','/ˈʃeɪkɪli/','颤抖地；不稳地；不太有把握地',
 '手指抖着系扣子，或刚听到惊险消息，声音不稳地笑一下，都可以用 shakily。它把动作里的不稳定写出来。',
 'shaky 的 y 变 i 加 -ly；内层 shake + -y，外层副词描述方式。',SHAKY+[['shaky + -ly → shakily','以发颤、不稳、缺把握的方式做事']],
 'stood shakily 颤巍巍站着；laughed shakily 带着颤音笑；spoke shakily 说话不稳。',
 'shakily signed her name；shakily got to his feet。',
 'shakily 可以是动作不稳，也可以是把握不足的表现；quietly 只说安静、音量小，不自动带不稳。',
 ('He got shakily to his feet.','他颤巍巍地站了起来。'),('“We made it,” she said shakily.','“我们挺过来了。”她声音发颤地说。'),sources=S('shakily','shaky'))
W('shakiness','/ˈʃeɪkinəs/','颤抖、不稳；依据薄弱、缺把握的状态',
 '把手抖、结构不稳，或论证撑不住的性质整体提出来，就是 shakiness。它不是单次摇一下，而是整体不稳定。',
 'shaky 的 y 变 i 加 -ness；把物理、抽象不稳的性质名词化。',SHAKY+[['shaky + -ness → shakiness','发颤、不稳定、可靠性不足的性质']],
 'shakiness in the hands 手部颤抖；the shakiness of the argument 论证的薄弱。',
 'a little shakiness in her voice；shakiness after the shock。',
 'shakiness 命名不稳性质，a shake 可是一次摇动；不是把后者任意变复数就能完全替代前者。',
 ('There was a little shakiness in her voice.','她的声音里有一点颤。'),('The review exposed the shakiness of the original argument.','审查暴露了原先论证的薄弱。'),sources=S('shakiness','shaky'))
W('wobblier','英 /ˈwɒbliə/；美 /ˈwɑbliər/','更晃、更不稳的；更缺乏信心的',
 '桌腿本来松，现在放杯水都摇，是 wobblier；走远后双腿更撑不住、发软，也能这样说。',
 'wobbly 的 y 变 i 加完整 -er；内层 wobble 去 e 加 -y，外层比较松晃、不稳程度。',WOBBLY+[['wobbly → wobblier','更加不稳、晃动或心里动摇']],
 'a wobblier table 更晃的桌子；legs grew wobblier 双腿越来越不稳。',
 'wobblier than before；a wobblier decision。',
 'wobblier 常有支撑不稳、左右晃的画面，twitchier 更像短促抽动、敏感不安；不稳定的运动模式不同。',
 ('The table became wobblier after we moved it.','搬过以后，桌子更晃了。'),('His legs grew wobblier as the climb went on.','越往上爬，他的双腿越不稳。'),sources=S('wobblier','wobble'))
W('wobbliest','英 /ˈwɒbliɪst/；美 /ˈwɑbliɪst/','最晃、最不稳的；最易动摇的',
 '几把椅子里，坐上去最摇、最撑不住的，是 the wobbliest。也能比较某段过程里信心最不稳的时候。',
 'wobbly 的 y 变 i 加完整 -est；形容词最高级，不是 wobble 动词接一个独立的 -iest。',WOBBLY+[['wobbly → wobbliest','所比范围内晃动、不稳定程度最高']],
 'the wobbliest chair 最不稳的椅子；the wobbliest part of the structure 结构最晃的部分。',
 'our wobbliest shelf；at its wobbliest 最不稳定时。',
 'wobbliest 说明不稳，oldest 说明年代最久；旧物可能很稳，新物也可能装得松晃。',
 ('We removed the wobbliest chair from the room.','我们把屋里最不稳的椅子搬走了。'),('The narrow shelf was the wobbliest part of the unit.','那块窄隔板是整个架子最晃的部分。'),sources=S('wobbliest','wobble'))
W('wobbliness','英 /ˈwɒblinəs/；美 /ˈwɑblinəs/','松晃、不稳定；信心动摇的状态',
 '不再说桌子 wobbly，而是讨论它为什么会晃、那份松动有多大，就是 wobbliness。人腿软站不稳，也能把状态这样命名。',
 'wobbly 的 y 变 i 加 -ness；内层是 wobble + -y，整个形容词性质再名词化。',WOBBLY+[['wobbly + -ness → wobbliness','左右晃、支撑不稳的性质或状态']],
 'the wobbliness of the chair 椅子的松晃；wobbliness in the knees 膝腿不稳。',
 'reduce wobbliness；a moment of emotional wobbliness 一时情绪不稳。',
 'wobbliness 侧重支撑、平衡不稳，jerkiness 侧重运动一顿一顿；椅子能松晃，视频能断续，不能一律只译成抖。',
 ('Tightening the screws reduced the chair’s wobbliness.','拧紧螺丝减轻了椅子的松晃。'),('She noticed some wobbliness in her legs after the long climb.','长时间攀爬后，她注意到双腿有些站不稳。'),sources=S('wobbliness','wobble'))
W('tremulously','/ˈtremjələsli/','颤抖地；声音发颤、不稳地',
 '想平静说一句话，声音里却漏出颤抖、激动，是 tremulously。较常见于书面叙事，写声音、微笑、伸出的手等。',
 'tremulous + -ly；tremulous 借拉丁 tremulus 颤抖的，与 tremble 同族，但不是现代英语 tremble 换尾；副词才是英语后接的扩展。',TREMULOUS+[['tremulous + -ly → tremulously','带着细微颤抖、不稳的方式']],
 'said tremulously 颤声说；smiled tremulously 颤着微笑。',
 'tremulously asked；reached out tremulously。',
 'tremulously 在语体上常比 shakily 更书面，核心仍是颤、不稳；不能为凑区别编成一种只适用于高兴、另一种只适用于害怕。',
 ('“Is it really over?” she asked tremulously.','“真的结束了吗？”她颤声问。'),('He smiled tremulously when he saw his family.','看见家人时，他颤着露出笑容。'),sources=S('tremulously','tremulous'))
W('tremulousness','/ˈtremjələsnəs/','颤抖、微颤；带情绪的不稳状态',
 '声音里那一点压不住的颤，拿出来当一种性质讲，就是 tremulousness。它可以传达情绪，也可以只描述动作不稳。',
 'tremulous + -ness；把形容词性质整体名词化。tremulous 自己接拉丁颤抖材料，不由英语 tremble 直接换尾。',TREMULOUS+[['tremulous + -ness → tremulousness','发颤、不稳的性质或程度']],
 'tremulousness in her voice 声音里的微颤；the tremulousness of his hands 双手的颤抖。',
 'a trace of tremulousness；noticeable tremulousness。',
 'tremulousness 是较书面的性质名词，a tremor 可以是一次颤动或某种震颤现象；具体能否替换，要看是否正在数动作。',
 ('A slight tremulousness in her voice revealed her excitement.','她声音里轻微的颤抖透露出她的激动。'),('He tried to hide the tremulousness of his hands.','他试图掩饰双手的颤抖。'),sources=S('tremulousness','tremulous'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgt',ROOTS,WORDS)
 extend_lessons()
