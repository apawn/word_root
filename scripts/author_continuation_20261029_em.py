"""Dog and beat: familiar animals, persistence and rhythm."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
D=[['古英语 docga、dogga → 中古英语 dogge → dog','狗；更远来源不明'],['现代 dog 词族','犬种、用途；追逐、纠缠与坚持等联想']]
def H(f,m):return D+[[f,m]]
W('dog','英 /dɒɡ/；美 /dɔːɡ/、/dɑːɡ/','狗；追踪、纠缠',
 '名词是熟悉的动物；动词则像狗紧跟身后一样，说问题、指责一直缠着人。',
 '继承古英语 docga 等形式，更远来历不确定。后来 dog 逐渐替代 hound 成为狗的常用泛称，hound 则常收窄到猎犬等。',D,
 'walk the dog 遛狗，a guide dog 导盲犬；be dogged by problems 困扰不断，过去式读 /dɒɡd/ 等。',
 'walk the dog；a guide dog；dog someone’s steps；be dogged by。',
 'dog 动词分词 dogged 通常一音节 /dɒɡd/，dogged 坚毅的形容词通常两音节 /ˈdɒɡɪd/；拼写相同而读法有别。',
 ('We walk the dog before breakfast.','我们在早饭前遛狗。'),('The project was dogged by delays.','项目一直受延误困扰。'))
W('doggy','英 /ˈdɒɡi/；美 /ˈdɔːɡi/、/ˈdɑːɡi/','狗狗；小狗；狗的、像狗的',
 '比 dog 更像家里亲昵叫狗狗，也可用来形容与狗有关的东西。',
 'dog 双写 g + -y，昵称名词与性质形容词用法都可见。昵称不保证犬龄很小，成年狗也可被叫 doggy。',H('dog + -y → doggy','亲昵称呼狗；与狗有关的'),
 'a cute doggy 可爱的狗狗，a doggy smell 狗味；doggie 也是常见变体。',
 'a cute doggy；a little doggy；a doggy smell。',
 'doggy 亲昵语气，puppy 更明确幼犬；不要按昵称把年龄一律译成几个月的小狗。',
 ('The child pointed at the doggy in the park.','孩子指着公园里的狗狗。'),('The blanket had a faint doggy smell.','毯子带着一点狗味。'))
W('bulldog','英 /ˈbʊldɒɡ/；美 /ˈbʊldɔːɡ/','斗牛犬；强硬执着的人或风格',
 '犬名历史与旧时斗牛用途有关；后来借这种强韧形象形容不轻易放弃的态度。',
 'bull 公牛 + dog 狗，接旧时 bullbaiting 的犬种用途命名；现代犬种不能只靠名字推断个体性格。',H('bull + dog → bulldog','旧用途犬名 → 斗牛犬；坚韧形象'),
 'a bulldog puppy 斗牛犬幼犬，bulldog determination 顽强决心；比喻不代表人在斗牛。',
 'a bulldog puppy；bulldog determination；a bulldog expression。',
 'bull 是公牛，不是 brave 勇敢的某个后缀；bulldog 的用途历史与今天每只宠物行为分开。',
 ('A bulldog slept beside the sofa.','一只斗牛犬睡在沙发旁。'),('She pursued the case with bulldog determination.','她以顽强不屈的决心追查此案。'))
W('underdog','英 /ˈʌndədɒɡ/；美 /ˈʌndərdɔːɡ/','处于劣势者；不被看好的一方',
 '赛前大家认为它赢面小，处在弱势；但不意味着最后一定输。',
 'under 在下、居劣势 + dog，历史有争斗中处下风的狗的表达，后用于竞争中的弱势一方。不要把流行锯木工故事当定论。',H('under + dog → underdog','处下风的一方 → 弱势竞争者'),
 'root for the underdog 支持弱势方，the underdog in the final 决赛中不被看好的选手或队伍。',
 'root for the underdog；start as the underdog；an underdog victory。',
 'underdog 指预期、处境较弱，loser 指输了或带贬意的失败者；弱势方也能获胜。',
 ('The team entered the final as the underdog.','球队以不被看好的弱势方身份进入决赛。'),('Many fans love an underdog victory.','许多球迷喜欢看弱队逆袭取胜。'),sources=['https://www.etymonline.com/word/underdog','https://en.wiktionary.org/wiki/underdog#English'])
W('dogged','英 /ˈdɒɡɪd/；美 /ˈdɔːɡɪd/','顽强的；坚持不懈的',
 '咬定一个目标，碰到阻力也不松手。可以赞毅力，也可能带固执意味。',
 'dog + -ed，早期像狗的形容词曾多带负面评价，后来发展出坚持、顽强义。该形容词末尾 -ed 单独成音节 /ɪd/。',H('dog + -ed → dogged','像狗的旧评价 → 顽强坚持'),
 'dogged determination 顽强决心，dogged persistence 不懈坚持；别把历史贬义生搬到每个现代赞美里。',
 'dogged determination；dogged persistence；a dogged effort。',
 'dogged 坚毅的两音节；was dogged by delays 受延误困扰中的分词通常一音节。',
 ('Her dogged determination kept the project alive.','她顽强的决心让项目坚持了下来。'),('They made a dogged effort to find the missing records.','他们坚持不懈地寻找丢失记录。'),sources=['https://www.etymonline.com/word/dogged','https://en.wiktionary.org/wiki/dogged#English'])
W('sheepdog','英 /ˈʃiːpdɒɡ/；美 /ˈʃiːpdɔːɡ/','牧羊犬',
 '帮助看管、驱赶羊群的狗，名字直接抓住工作对象。',
 'sheep 羊 + dog 狗，按工作用途组合。sheep 单复数同形，不能在前部硬补 sheeps。',H('sheep + dog → sheepdog','为羊群工作的犬 → 牧羊犬'),
 'a trained sheepdog 训练过的牧羊犬，a sheepdog trial 牧羊犬技能比赛；也可用于具体犬种称呼。',
 'a trained sheepdog；a working sheepdog；a sheepdog trial。',
 'sheepdog 看用途或犬类称呼，不是 sheep 羊的幼崽；sheep 的幼崽是 lamb。',
 ('The sheepdog guided the flock through the gate.','牧羊犬把羊群引过了栅门。'),('Visitors watched a sheepdog trial at the fair.','游客在集市上观看了牧羊犬技能比赛。'))
R('B4609','狗、用途犬名与坚持、劣势','DOG：从动物出发，读用途和行为比喻','doggy 亲昵称呼紧接 dog；bulldog、sheepdog 讲用途，underdog 弱势，dogged 顽强。',
 'dog 古英语已有，更远来源不定，不编拟声或外语借入假说。dogged 的形容词与动词分词读音尤其值得区分。',
 'dog → doggy、dogged；bull、sheep、under + dog；共享 watchdog、dogfight。',
 [['基本词、昵称与性格','dog · doggy · dogged'],['用途与竞争位置','bulldog · sheepdog · underdog · watchdog · dogfight']],
 'underdog 不等于必败；doggy 不一定幼犬；dogged /ˈdɒɡɪd/ 坚持与 /dɒɡd/ 被纠缠分词分开。',
 'The underdog won through dogged determination.\n\n不被看好的一方凭顽强决心赢了。',
 'dog doggy dogged bulldog sheepdog underdog watchdog dogfight')
BE=[['古英语 bēatan → 中古英语 beten → beat','敲、打、击'],['现代 beat','连续敲击 → 节拍；击败、疲惫与特定巡行范围等']]
W('beat','/biːt/','击打；打败；跳动、节拍；使疲惫',
 '一下下打是基本动作，心脏一下下跳、音乐一拍一拍走也能连接；比赛里 beat 则是击败对手。',
 '继承古英语 bēatan。现代常用变化 beat—beat—beaten；口语 I am beat 是累坏了，用法另记。',BE,
 'beat an egg 打蛋，beat a team 击败队伍，the beat of music 音乐节拍；beat the traffic 提早走避开堵车。',
 'beat a team；beat an egg；keep the beat；I am beat。',
 'beat 接对手，win 接比赛或奖项：beat the team；win the match。不能机械说 win the team 表击败。',
 ('Our team beat the champions yesterday.','我们队昨天击败了冠军队。'),('The children clapped to the beat of the music.','孩子们跟着音乐节拍拍手。'))
W('beaten','/ˈbiːtən/','被打败的；被打过的；beat 的过去分词',
 '对手被战胜，材料被反复打过，都能用这一个结果形式。',
 'beat 的不规则过去分词，保留旧日耳曼分词变化。the beaten track 比喻很多人走过的常规路线。',BE+[['beat—beat—beaten','击打、击败 → 相应过去分词']],
 'a beaten team 被击败的队伍，beaten eggs 打散的蛋液，off the beaten track 偏僻、少有人去的地方。',
 'beaten eggs；a beaten team；off the beaten track。',
 'beaten eggs 只说经过搅打，不必是炒蛋；beat 过去式与现在原形同形，分词通常 beaten。',
 ('Add the beaten eggs to the mixture.','把打散的蛋液加入混合物。'),('They found a quiet village off the beaten track.','他们找到一座少有人去的安静村庄。'))
W('unbeatable','/ʌnˈbiːtəbəl/','无法击败的；无可比拟的',
 '对手赢不了它；广告里也常夸价格、服务好到难以超过。',
 'un- 不 + beatable 可被击败的，后者 beat + -able。否定整个可被击败的性质，不是停止打人。',BE+[['beat + -able → beatable；un- → unbeatable','可被战胜 → 无法战胜']],
 'an unbeatable team 无敌队伍，an unbeatable price 极具竞争力的价格；商业夸赞未必是严格验证的世界纪录。',
 'an unbeatable team；an unbeatable price；an unbeatable offer。',
 'unbeatable 宣称难以超过，unbeaten 尚未被击败；尚未输不等于逻辑上永远输不了。',
 ('At their best, the team seemed unbeatable.','球队状态最佳时，似乎无人能敌。'),('The café offers breakfast at an unbeatable price.','咖啡馆以极有竞争力的价格供应早餐。'))
W('beater','英 /ˈbiːtə/；美 /ˈbiːtər/','搅拌、打击用器具；旧车等口语称呼',
 '最常见可从打蛋器记：替你反复打、搅的器具。美式口语也可说一辆破旧但仍在用的车。',
 'beat + -er，执行击打、搅拌的人或物，相应词古英语已有。旧车俚语接被折腾得很旧的 beat 使用分支。',BE+[['beat + -er → beater','执行击打搅拌的器具；另有旧车俚语']],
 'an egg beater 打蛋器，electric beaters 电动搅拌器，an old beater 一辆旧破车。',
 'an egg beater；electric beaters；an old beater。',
 'beater 不一定是打人的人；egg beater 取厨房器具义，另一些俚语义需看上下文。',
 ('Use an egg beater to mix the eggs.','用打蛋器把蛋液搅匀。'),('He drove an old beater to work.','他开着一辆旧破车上班。'))
W('upbeat','形容词常 /ˈʌpbiːt/；音乐名词也见 /ʌpˈbiːt/','乐观、积极的；音乐的上拍、弱起相关用语',
 '日常说一个人精神明亮、对前景抱好态度；音乐里则有指挥上挥、节拍位置的具体含义。',
 'up + beat，音乐用法接上挥、弱拍位置等传统，后用于轻快、积极的态度。不能只从 up 高处推出所有人的情绪。',BE+[['up + beat → upbeat','音乐节拍用语 → 积极、乐观的形容词']],
 'an upbeat mood 积极情绪，an upbeat message 乐观信息，remain upbeat 保持乐观；音乐上下文再看实际拍位。',
 'remain upbeat；an upbeat mood；an upbeat message。',
 'upbeat 乐观，beat up 殴打、破旧等短语词义不同；词序与是否连写都重要。',
 ('She remained upbeat despite the delay.','尽管延误，她依然乐观。'),('The report ends on an upbeat note.','报告以积极乐观的语气收尾。'))
W('offbeat','英 /ˈɒfbiːt/；美 /ˈɔːfbiːt/','不寻常的；标新立异的；音乐弱拍相关的',
 '不是大家都按的常规节奏，日常便可形容点子、幽默或风格与众不同。',
 'off- 偏离 + beat 节拍，音乐里接弱拍、非重拍位置，后来形容不同寻常的风格。不是永远指演奏出错。',BE+[['off- + beat → offbeat','非主要拍位 → 不寻常的风格']],
 'offbeat humour 另类幽默，an offbeat idea 不寻常的点子；音乐名词重音可随用法、口音变化。',
 'offbeat humour；an offbeat idea；an offbeat film。',
 'offbeat 可赞有创意，不等于 wrong 错误；off the beat 是临时介词短语，按上下文读。',
 ('The film is full of offbeat humour.','电影充满另类幽默。'),('She suggested an offbeat way to present the results.','她提出了一种与众不同的成果展示方式。'))
W('drumbeat','/ˈdrʌmbiːt/','鼓点；持续反复出现的声音、呼声',
 '鼓一声声地敲，形成反复节奏；媒体也借它说某种呼声或信息不断重复。',
 'drum 鼓 + beat 一次敲击、节拍，实际鼓声扩展为持续反复的宣传、呼声等比喻。',BE+[['drum + beat → drumbeat','鼓的节奏 → 持续不断的声音或呼声']],
 'a steady drumbeat 稳定鼓点，a drumbeat of criticism 持续批评；不是只要敲一下就一定形成复杂节奏。',
 'a steady drumbeat；a distant drumbeat；a drumbeat of criticism。',
 'drumbeat 节奏、声音，drummer 鼓手；heartbeat 心跳是另一同类复合词。',
 ('A steady drumbeat accompanied the dance.','稳定鼓点伴随着舞蹈。'),('The minister faced a growing drumbeat of criticism.','部长面对越来越密集的持续批评。'))
R('B2738','击打、击败与节奏、态度','BEAT：一下下敲击，形成节拍与多条比喻','基本 beat、beaten 相邻，再看器具、不可战胜与音乐态度词；甲虫 beetle 不硬收进敲打词源。',
 '古英语击打词族。beetle 的甲虫义接 bite 咬的历史词，不因拼写近就写成 beat 的派生；用户先略生僻义，本页不展开古槌 beetle 等。',
 'beat → beaten、beater、unbeatable；up、off、drum + beat；共享 heartbeat、downbeat、deadbeat、beatbox。',
 [['动作、结果与器具','beat · beaten · beater · unbeatable'],['节奏与态度','upbeat · offbeat · downbeat · drumbeat · heartbeat · beatbox'],['已有相关人物词','deadbeat']],
 'beat 对手、win 比赛；unbeatable 无法打败与 unbeaten 尚未输不同；upbeat 不等于 beat up。',
 'The unbeaten team stayed upbeat before the next match.\n\n尚未败过的球队在下一场比赛前保持乐观。',
 'beat beaten beater unbeatable upbeat offbeat downbeat drumbeat heartbeat beatbox deadbeat')
if __name__=='__main__':save('continuation_20261029_em',ROOTS,WORDS)
