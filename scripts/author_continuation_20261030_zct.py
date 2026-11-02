"""Sounds, laughter and emotional expression, with common family forms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A2238':dict(words=['giggle','giggles','giggled','giggling','chuckle','chuckles','chuckled','chuckling'],label='giggle 与 chuckle 各自的常用形式：笑声与动作',note='两词有拟声及历史反复动作材料，但近源路线不必讲成完全一样；现代扩展按基词成组。'),
 'B4221':dict(words=['chuckle','chuckles','chuckled','chuckling'],label='chuckle → chuckles、chuckled、chuckling：轻轻笑',note='chuck 咯咯声支加旧 le 反复动作材料；现代去 e 加完整 ed、ing。'),
 'B3849':dict(words=['yell','yells','yelled'],label='yell → yells、yelled：大声叫喊',note='古英语 giellan 继承，原因可能是愤怒、兴奋或呼唤，不一概骂人。'),
 'A1741':dict(words=['moan','moans','moaned','weep','weeps'],label='moan 抱怨、低声呻吟；weep 流泪：各自扩展',note='不同词族分别理解；不因都表达不快就说词源相同。'),
 'A1699':dict(words=['stink','stinks','stinking'],label='stink → stinks、stinking：散发气味到发臭',note='古英语可泛指气味，现代常带负面；三单读 ks，ing 不换成过去式 stank。'),
}
W('giggles','/ˈɡɪɡəlz/','咯咯笑、忍不住轻笑〔第三人称单数〕；咯咯笑声〔复数〕',
 '笑声一小阵一小阵冒出来，轻快、像忍不住漏出的咯咯声，是 giggles。可以说某个人这样笑，也能数那些笑声。',
 'giggle 大概有拟声起源，亦有联系旧咯吱声材料加 -le、或荷兰语相应形式的分析，路线未定。现代加 -s，/l/ 后读 /z/。',
 [['拟声、日耳曼相关材料 → giggle','具体路径未定；咯咯轻笑'],['giggle + -s → giggles','某人咯咯笑；几阵笑声']],
 'quiet giggles 轻轻的咯咯笑；a fit of giggles 一阵忍不住的笑；giggles at a joke 听了笑话咯咯笑。',
 'bursts into giggles 忍不住咯咯笑起来；suppressed giggles 压住的笑声。',
 'giggles 常偏轻快、反复的笑，不一定是很大声的大笑。名词复数与动词三单同形，按句子里位置看。',
 ('She giggles whenever the puppet appears.','木偶一出现，她就咯咯笑。'),('Quiet giggles came from the back of the room.','房间后面传来轻轻的咯咯笑声。'),sources=['https://en.wiktionary.org/wiki/giggles#English','https://en.wiktionary.org/wiki/giggle#English'])
W('giggled','/ˈɡɪɡəld/','咯咯笑了、忍不住轻笑了〔过去式、过去分词〕',
 '一个小小的笑点让人咯咯笑出声，事情已经发生，就是 giggled。它通常给人轻快、压不太住笑的感觉。',
 'giggle 接拟声及相关日耳曼材料，具体近源有不同分析。现代去末尾 e，加完整 -ed，/l/ 后读 /d/，不是新增 /ɪd/ 音节。',
 [['早期拟声等材料 → giggle','反复、轻快的咯咯笑声'],['giggle 去 e + -ed → giggled','已经轻声咯咯笑过']],
 'giggled at the joke 听笑话咯咯笑了；giggled together 一起咯咯笑；giggled nervously 紧张地轻笑。',
 'giggled behind a hand 用手挡着嘴轻笑；giggled with delight 高兴得咯咯笑。',
 'giggled 也可能出于紧张或不好意思，不保证人在嘲笑谁。at 后面可能是笑点，也可能是对象，语境决定态度。',
 ('The children giggled at the funny drawing.','孩子们看着有趣的画咯咯笑了。'),('She giggled nervously before beginning her speech.','开始讲话前，她紧张地轻笑了一下。'),sources=['https://en.wiktionary.org/wiki/giggled#English','https://en.wiktionary.org/wiki/giggle#English'])
W('giggling','/ˈɡɪɡəlɪŋ/','咯咯笑、忍不住轻笑〔现在分词、动名词〕',
 '一边想忍住，一边笑声又一小阵一小阵出来，是 giggling 很常见的画面。它也可以只是单纯轻快地笑。',
 'giggle 的拟声来源及相关旧动作材料有不同分析；现代 giggle 去末尾 e 加完整 -ing，词干末 /l/ 保留。',
 [['拟声等材料 → giggle','咯咯、轻快反复的笑'],['giggle 去 e + -ing → giggling','正在轻笑；轻笑过程']],
 'giggling quietly 轻轻咯咯笑；a giggling child 咯咯笑的孩子；stop giggling 别再咯咯笑了。',
 'giggling at the picture 看图咯咯笑；giggling together 一起轻笑。',
 'giggling 把过程放在眼前，giggled 则把动作放在过去。两者末尾都不保留 giggle 的不发音 e，但后缀分别是完整 ing、ed。',
 ('The children were giggling behind the curtain.','孩子们在幕布后咯咯笑。'),('She could not stop giggling at the drawing.','她看着那幅画，忍不住一直轻笑。'),sources=['https://en.wiktionary.org/wiki/giggling#English','https://en.wiktionary.org/wiki/giggle#English'])
W('chuckles','/ˈtʃʌkəlz/','轻声笑、低低地笑〔第三人称单数〕；轻笑声〔复数〕',
 '不是放声大笑，而是胸口轻轻冒出几声觉得好笑的声音，是 chuckles 的现代常用感觉。',
 'chuckle 接 chuck、chukken 咯咯声的拟声支，加 -le 等旧反复动作材料；历史也曾有较大笑声用法。现代加 -s，/l/ 后读 /z/。',
 [['拟声 chuck 等 + 旧动作尾 → chuckle','笑声动作 → 现代常用轻笑'],['chuckle + -s → chuckles','某人低低地笑；几声轻笑']],
 'quiet chuckles 轻轻的笑声；chuckles to himself 独自轻笑；chuckles at the memory 想起往事轻笑。',
 'a few chuckles 几声轻笑；warm chuckles 温暖、友善的轻笑声。',
 'chuckles 与 giggles 有重叠；前者常让人想到低低、从容的轻笑，后者常偏轻快、反复冒出的咯咯笑，不是死板的音量分类。',
 ('He chuckles whenever he remembers the incident.','他一想起那件事就轻声笑。'),('A few chuckles broke the silence.','几声轻笑打破了安静。'),sources=['https://en.wiktionary.org/wiki/chuckles#English','https://en.wiktionary.org/wiki/chuckle#English'])
W('chuckled','/ˈtʃʌkəld/','轻声笑了、低低地笑了〔过去式、过去分词〕',
 '觉得有趣，没大笑，只是低低笑出声，就是 chuckled。小说里常用它描写一个短短的反应。',
 'chuckle 接 chuck、chukken 的咯咯声拟声材料与旧 -le 动作尾。现代去末尾 e，加完整 -ed，/l/ 后读 /d/。',
 [['拟声 chuck 等 → chuckle','现代常用低声、轻轻地笑'],['chuckle 去 e + -ed → chuckled','已经轻声笑过']],
 'chuckled softly 轻轻笑了；chuckled to herself 独自轻笑；chuckled at the joke 听了笑话轻笑。',
 'chuckled with amusement 觉得有趣地轻笑；chuckled and nodded 轻笑并点头。',
 'chuckled 可以友善、得意、带嘲意，不能只凭动作词确定态度。softly、warmly 等修饰词能进一步说明感觉。',
 ('He chuckled at the unexpected reply.','听到意外的回答，他轻声笑了。'),('She chuckled to herself while reading the letter.','她读信时独自轻笑了起来。'),sources=['https://en.wiktionary.org/wiki/chuckled#English','https://en.wiktionary.org/wiki/chuckle#English'])
W('chuckling','/ˈtʃʌkəlɪŋ/','轻声笑、低低地笑〔现在分词、动名词〕',
 '低低的笑声还在继续，是 chuckling。它常能给人物反应添一点觉得有趣、心领神会的感觉。',
 'chuckle 的拟声与旧反复动作材料在词内，现代变化则去末尾 e 加完整 -ing；/l/ 保留，不新添第二个 l。',
 [['拟声 chuck 等 → chuckle','咯咯声、笑声动作'],['chuckle 去 e + -ing → chuckling','正在轻声笑；轻笑过程']],
 'chuckling quietly 低声轻笑；chuckling to himself 独自轻笑；still chuckling 仍在轻笑。',
 'walked away chuckling 轻笑着走开；chuckling at the thought 想到此事轻笑。',
 'He walked away chuckling 里，chuckling 描写走开的同时还在轻笑；不必每次都用 be 才能出现现在分词。',
 ('He walked away chuckling to himself.','他独自轻笑着走开了。'),('They were still chuckling at the story.','他们还在为那个故事轻声发笑。'),sources=['https://en.wiktionary.org/wiki/chuckling#English','https://en.wiktionary.org/wiki/chuckle#English'])
W('yells','/jelz/','大喊、叫喊〔第三人称单数〕；喊声〔复数〕',
 '把声音一下提得很响，想让别人听见，是 yells。可能生气、兴奋，也可能是在远处呼喊。',
 'yell 继承古英语 giellan，经中古英语 yellen 延续，既是动作，也能数一声叫喊。现代加 -s，/l/ 后读 /z/。',
 [['古英语 giellan → 中古英语 yellen → yell','响亮、尖厉地发声 → 大喊'],['yell + -s → yells','某人叫喊；多声喊声']],
 'yells across the room 隔着房间喊；yells with delight 高兴得大叫；loud yells 响亮喊声。',
 'yells for help 大声呼救；yells someone’s name 大喊某人名字。',
 'yells 不一概是骂人。yells at someone 常带冲着人喊的感觉，yells to someone 也能只是为了让远处的人听见。',
 ('She yells my name from the garden.','她从花园里大声喊我的名字。'),('Loud yells came from the playground.','操场上传来响亮喊声。'),sources=['https://en.wiktionary.org/wiki/yells#English','https://en.wiktionary.org/wiki/yell#English'])
W('yelled','/jeld/','大喊了、叫喊了〔过去式、过去分词〕',
 '一句话或一个声音已经被大声喊出来，是 yelled。用在叙事里，它能直接把声音的突然、响亮带出来。',
 'yell 接古英语 giellan、后来 yellen 的响亮叫声词族。现代直接加完整 -ed，/l/ 后读 /d/，词干已经双 l，不再添第三个 l。',
 [['古英语响亮发声材料 → yell','叫喊、喊出内容'],['yell + -ed → yelled','已经大声喊过']],
 'yelled her name 大喊了她的名字；yelled with excitement 兴奋地大叫；yelled across the field 隔着田地喊。',
 'yelled to someone 向某人喊话；yelled over the noise 压过噪声喊。',
 'yelled 只给出声音方式，喊的内容可放引号或接名词。at、to 和语气能帮助判断是在责骂还是远距离传话。',
 ('He yelled my name across the field.','他隔着田地大声喊我的名字。'),('The children yelled with excitement when the curtain rose.','幕布升起时，孩子们兴奋地大叫。'),sources=['https://en.wiktionary.org/wiki/yelled#English','https://en.wiktionary.org/wiki/yell#English'])
W('moans','英 /məʊnz/；美 /moʊnz/','呻吟、低声哀叹、抱怨〔第三人称单数〕；呻吟声、抱怨〔复数〕',
 '低沉、拖长地发出不舒服的声音，是 moans 的基本感觉。口语里总在说这不满意、那不满意，也会被叫 moans。',
 'moan 接中古英语 mone、monen 等哀叹、悲伤、抱怨材料，和更早英语词的具体承接有讨论。现代加 -s，/n/ 后读 /z/。',
 [['中古英语 mone、monen 等 → moan','哀叹、悲伤、抱怨 → 低沉呻吟声'],['moan + -s → moans','某人呻吟、抱怨；多声呻吟、几次抱怨']],
 'moans about the weather 抱怨天气；moans of pain 痛苦呻吟；constant moans 不停抱怨。',
 'moans and groans 唉声叹气；the wind moans 风低沉呼啸〔比喻〕。',
 'moans 可以是不成词的声音，也可以是说得出内容的抱怨。形容别人 moans 往往带对其抱怨太多的不耐烦。',
 ('He moans about the weather every morning.','他每天早晨都抱怨天气。'),('The audience heard low moans from behind the stage.','观众听到舞台后传来低低的呻吟声。'),sources=['https://en.wiktionary.org/wiki/moans#English','https://en.wiktionary.org/wiki/moan#English'])
W('moaned','英 /məʊnd/；美 /moʊnd/','呻吟了、哀叹了；抱怨了〔过去式、过去分词〕',
 '不舒服时拖着声音哼了一声，或带不满地说了几句，就是 moaned。共同点是低沉、不太愉快的表达。',
 'moan 的中古英语材料已有哀叹、悲伤、抱怨用法，后来低沉呻吟义也常见。现代直接加完整 -ed，/n/ 后读 /d/。',
 [['中古英语哀叹、抱怨材料 → moan','悲伤的声音、话语 → 呻吟、口语抱怨'],['moan + -ed → moaned','已经呻吟、哀叹或抱怨']],
 'moaned about the delay 抱怨延误；moaned softly 低低呻吟；moaned in the wind 在风里低鸣。',
 'moaned that… 抱怨说……；moaned all afternoon 抱怨了一下午。',
 'moaned that 后面常能看见抱怨内容，moaned softly 则可能只是声音。不能每次都译为身体疼痛。',
 ('He moaned about the long wait.','他抱怨等得太久。'),('The old gate moaned in the wind.','旧门在风中发出低沉的响声。'),sources=['https://en.wiktionary.org/wiki/moaned#English','https://en.wiktionary.org/wiki/moan#English'])
W('stinks','/stɪŋks/','发臭、有难闻气味；很糟、很差劲〔第三人称单数〕',
 '气味难闻到让人想躲开，是 stinks。口语说一个安排 stinks，就是觉得它糟糕、令人不满，像一股讨厌的味道。',
 'stink 继承古英语 stincan，早期可以泛说散发气味，难闻义后来占主导。现代加 -s，/k/ 后读 /s/，尾 /ŋks/。',
 [['古英语 stincan → stink','散发气味 → 发臭、令人不快'],['stink + -s → stinks','某物发臭；口语某事很糟']],
 'stinks of smoke 满是难闻烟味；stinks up the room 弄得满屋臭味；this plan stinks 这个计划很糟〔口语〕。',
 'the rubbish stinks 垃圾发臭；stinks at a game 玩某游戏很差〔口语〕。',
 'stinks 作评价时语气直接、带贬义。它不仅表示一般不喜欢，还常有很糟、让人受不了的感觉。',
 ('The wet bag stinks of old fish.','湿袋子散发着陈鱼的臭味。'),('In the dialogue, she says the whole arrangement stinks.','对话里，她说整个安排糟透了。'),sources=['https://en.wiktionary.org/wiki/stinks#English','https://en.wiktionary.org/wiki/stink#English'])
W('stinking','/ˈstɪŋkɪŋ/','发臭、臭烘烘的〔现在分词、形容词〕；极其〔部分口语搭配〕',
 '难闻气味正不断散出来，是 stinking。形容物品时可直接说臭烘烘的；某些口语搭配又用它把程度说得很重。',
 'stink 继承古英语 stincan 气味材料，现代常是臭味。直接加完整 -ing，词干 /ɪ/ 和末尾 /k/ 保留，不用过去式 stank 的元音。',
 [['古英语 stincan → stink','散发气味 → 发臭'],['stink + -ing → stinking','正在发臭、臭的；口语程度加强']],
 'stinking boots 臭烘烘的靴子；stinking rubbish 发臭垃圾；stinking rich 富得流油〔口语，常带评价〕。',
 'stinking up the hall 弄得大厅臭烘烘；a stinking smell 难闻臭味。',
 'stinking rich 是极有钱，不是说那个人真的有臭味。直接形容物品时，则通常仍在说气味或强烈负面评价。',
 ('He left his stinking boots outside the door.','他把臭烘烘的靴子留在门外。'),('The rubbish was stinking in the heat.','垃圾在高温下发着臭。'),sources=['https://en.wiktionary.org/wiki/stinking#English','https://en.wiktionary.org/wiki/stink#English'])
W('weeps','/wiːps/','流泪、哭泣；哀悼〔第三人称单数〕',
 '眼泪不断流出来，是 weeps。可以伤心、悼念，也可以高兴得流泪；相较 cry，它常更突出流泪，也更有书面叙事感。',
 'weep 接古英语 wēpan 的哭泣、哀悼词族。现代第三人称单数直接加 -s，/p/ 后读 /s/；过去式、分词另是 wept。',
 [['古英语 wēpan → weep','流泪、哭诉、哀悼'],['weep + -s → weeps','某人流泪、哭泣']],
 'weeps with joy 喜极而泣；weeps for someone 为某人流泪、哀悼；weeps quietly 静静流泪。',
 'weeps alone 独自哭泣；weeps at the ending 看到结尾流泪。',
 'weeps 不一定有很响的哭声，也不保证原因是悲伤。with joy 等搭配会把原因说明白。',
 ('The character weeps when he reads the letter.','那个角色读信时流下了眼泪。'),('She weeps with joy at the end of the play.','戏剧结尾，她喜极而泣。'),sources=['https://en.wiktionary.org/wiki/weeps#English','https://en.wiktionary.org/wiki/weep#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zct',ROOTS,WORDS)
 extend_lessons()
