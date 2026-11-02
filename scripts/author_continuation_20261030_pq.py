"""Individually explained common states in -ness, plus missing adjective bases."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()

def N(word,ipa,meaning,base,base_meaning,sense,explanation,usage,contrast,*examples,split=None,history=None,sources=None):
    stem=base[:-1]+'i' if base.endswith('y') and base[-2] not in 'aeiou' else base
    assert stem+'ness'==word,(base,word)
    spelling='，y 改 i' if stem!=base else ''
    W(word,ipa,meaning,sense,
      split or f'现代构词对应 {base} + -ness{spelling} → {word}。-ness 把前面的性质作为状态、程度等来谈。',
      history or [[f'英语 {base}',base_meaning],[f'{base} + -ness → {word}',meaning]],
      explanation,usage,contrast,*examples,sources=sources)

N('homelessness','英 /ˈhəʊmləsnəs/；美 /ˈhoʊmləsnəs/','无家可归的处境','homeless','没有稳定居所的',
 '不是这一晚出门旅行，而是没有稳定、安全的住处；homelessness 把这种生活处境作为一个社会问题来谈。',
 'homeless 描述人无家可归，homelessness 说这种处境、现象；可以讨论原因、经历和变化。',
 'experience homelessness 经历无家可归；address homelessness 应对无家可归问题。',
 'homelessness 不是 homesickness 想家；有家却想念它，与没有稳定住处是不同处境。',
 ('The report examines the causes of homelessness.','报告考察无家可归现象的原因。'),('The organisation helps families experiencing homelessness.','机构帮助正经历无家可归处境的家庭。'))
N('cleanliness','/ˈklenlinəs/','清洁、卫生；爱干净','cleanly','爱干净、保持清洁的〔较旧形容词用法〕',
 '厨房表面没脏污、用品保持整洁，讲的是 cleanliness。它不只说今天扫过一次，也能说持续保持卫生的状态。',
 'a high standard of cleanliness 是较高的卫生、清洁水平；personal cleanliness 则是个人卫生。',
 'personal cleanliness 个人卫生；standards of cleanliness 卫生标准。',
 'cleanliness 的前部读 /klen-/，不同于 clean /kliːn/；词形经过 cleanly 的旧形容词材料，不是只接 clean + ness。',
 ('The kitchen was praised for its cleanliness.','厨房的清洁卫生受到称赞。'),('The inspection checked standards of cleanliness.','检查核查了卫生标准。'),
 split='由较旧形容词 cleanly 爱干净的 + -ness，y 改 i → cleanliness。它的常用前部发音 /klen-/ 与 clean 的 /kliːn/ 不同。',sources=['https://en.wiktionary.org/wiki/cleanliness#English','https://www.oxfordlearnersdictionaries.com/definition/english/cleanliness'])
N('tenderness','英 /ˈtendənəs/；美 /ˈtendərnəs/','温柔；柔嫩；触痛','tender','温柔的、柔嫩的；一碰就痛的',
 '抱孩子时动作轻，是温柔；肉容易咬开，是柔嫩；受伤部位轻轻一碰就疼，又是触痛。三个常用义要跟对象走。',
 'tenderness 可以是感情、食物质地，也可以是身体对按触的痛感。不是只背温柔就能读懂所有句子。',
 'with tenderness 温柔地；the tenderness of meat 肉的嫩度；tenderness around a joint 关节周围触痛。',
 'tenderness 的触痛义与普通 softness 柔软不同：一处按着痛，并不等于它摸起来特别软。',
 ('He spoke to the child with tenderness.','他温柔地对孩子说话。'),('She noticed tenderness around the bruise.','她注意到淤青周围一碰就痛。'))
Dz=[['古英语 dysig → 中古英语 dysy 等','愚昧、发懵等旧性质'],['现代 dizzy → dizziness','头晕、眩晕；相应不稳的感觉']]
W('dizzy','/ˈdɪzi/','头晕、眩晕的；使人目眩的',
 '身体像转完圈还没停稳，眼前、脚下不踏实，是 dizzy 的身体画面。数量、高度太惊人，也能比喻令人目眩。',
 '由古英语 dysig 经中古英语延续，旧有愚昧、发懵等义，后来集中到头晕、目眩；现代 -y 不能倒拆成一个常用英文 diz。',Dz,
 'feel dizzy 感到头晕；a dizzy height 令人眩晕的高度；dizzy with excitement 兴奋得晕乎乎。',
 'feel dizzy；a dizzy height。',
 'dizzy 常突出晕、失去稳定感觉，drowsy 是犯困；两种感觉可以同在，却不是同一个词义。',
 ('I felt dizzy after the ride.','坐完游乐设施后，我觉得头晕。'),('The view from that dizzy height was impressive.','从那令人目眩的高处看去，景色很震撼。'))
N('dizziness','/ˈdɪzinəs/','头晕、眩晕感','dizzy','头晕、目眩的',
 'dizzy 是人觉得晕，dizziness 是那阵不稳、晕乎的感觉本身。记录它何时开始、持续多久，就会用这个名词。',
 'a feeling of dizziness 是头晕感；a wave of dizziness 可说一阵晕眩，像突然涌上来。',
 'a feeling of dizziness；a wave of dizziness。',
 'dizziness 说晕眩感，tiredness 说疲惫，sleepiness 说困意；记录不同感觉时不要全译成累。',
 ('A wave of dizziness made her sit down.','一阵晕眩让她坐了下来。'),('The dizziness passed after a few minutes.','几分钟后，那阵头晕过去了。'),history=Dz+[['dizzy + -ness → dizziness','现代头晕、眩晕的名词对应']])
N('tiredness','/ˈtaɪədnəs/，美式带 /r/','疲劳、疲惫','tired','疲劳的',
 '做了一整天事情，精力像被慢慢用光，这份累就是 tiredness。它能是身体疲劳，也能是持续用脑后的疲惫。',
 'tired 描述人，tiredness 把疲惫状态拿出来说；不必每次都已经困到想睡。',
 'physical tiredness 身体疲劳；a feeling of tiredness 疲惫感；signs of tiredness 疲劳迹象。',
 'tiredness 是累，drowsiness 更聚焦昏昏欲睡；人运动后很累，也可能暂时兴奋得睡不着。',
 ('Tiredness made it difficult to concentrate.','疲惫让人难以集中注意力。'),('She could hear the tiredness in his voice.','她从他的声音里听出了疲惫。'))
Df=[['古英语 deaf → 中古英语 def、deef','听不见、失聪的'],['现代 deaf → deafness','听觉相关状态；聋人身份、语言文化另依语境']]
W('deaf','/def/','聋的；听不见的',
 '听觉有障碍、听不见声音，常用 deaf。交流可以依靠手语、文字等不同方式，词本身不说明一个人的思考、学习能力。',
 '由古英语 deaf 经中古英语延续，接日耳曼语听觉受阻、发懵的旧材料；标准常用读音 /def/，不是按 ea 一律读 /iː/。',Df,
 'deaf students 聋生；be deaf in one ear 一只耳朵听不见；turn a deaf ear to 对……充耳不闻。',
 'deaf students；turn a deaf ear to。',
 'deaf 是听觉方面的词；turn a deaf ear 是选择不理会的习语，不一定真听不见。',
 ('The school supports deaf students.','学校为聋生提供支持。'),('They turned a deaf ear to our requests.','他们对我们的请求充耳不闻。'))
N('deafness','/ˈdefnəs/','耳聋；听觉丧失','deaf','聋的、听不见的',
 'deaf 描述听觉状况，deafness 把这种听觉丧失作为状态、经历来谈。具体程度、背景仍要看上下文。',
 'research into deafness 是对失聪的研究；a history of deafness 可按文本说失聪经历、病史。',
 'research into deafness；a history of deafness。',
 'deafness 是听觉状况，silence 是环境无声；周围安静不等于一个人听觉受损。',
 ('The charity supports research into deafness.','慈善机构支持失聪相关研究。'),('Her deafness was first noticed in childhood.','她的听觉问题最初在童年被发现。'),history=Df+[['deaf + -ness → deafness','现代失聪状态的名词对应']])
N('silliness','/ˈsɪlinəs/','傻气；胡闹、可笑的举动','silly','傻的、可笑的',
 '朋友戴着纸皇冠胡闹，你可能觉得这份 silliness 很可爱；会议一直开玩笑不谈事，也可能是在批评胡闹。',
 'silliness 可以是令人放松的傻乐，也可以是欠考虑、无聊的行为，评价由场景决定。',
 'a moment of silliness 一时胡闹；pure silliness 纯属胡闹；enjoy the silliness 享受傻乐。',
 'silliness 常比 stupidity 语气轻、可带亲昵；两词都能批评人，但力度和场景不同。',
 ('The children enjoyed the silliness of the game.','孩子们喜欢游戏里那些傻乐的部分。'),('A moment of silliness made everyone laugh.','一小段胡闹逗得大家都笑了。'))
N('appropriateness','/əˈprəʊpriətnəs/，美式 /əˈproʊpriətnəs/','合适、得体；适当性','appropriate','适合某场合、用途的',
 '同一句玩笑，朋友聊天合适，严肃仪式上可能不合适。appropriateness 问的就是与场合、目的是否对得上。',
 '不是抽象地好不好，而是对谁、在什么时候、用于什么目的合不合适。',
 'the appropriateness of a remark 言语的得体性；appropriateness for a purpose 对用途的合适程度。',
 'appropriateness 是适合情境，correctness 是正确；一句语法正确的话，也可能在那个场合不合适。',
 ('They questioned the appropriateness of the joke.','他们质疑这个玩笑是否得体。'),('The review considered the appropriateness of the method.','评审考察了方法是否合适。'))
Dr=[['古英语 drusian 等低垂、困倦材料；drowse、drowsy 的对应','形容词 drowsy 的记录早于现代 drowse 动词记录'],['现代 drowsy → drowsiness','犯困、昏昏欲睡；困倦状态']]
W('drowsy','/ˈdraʊzi/','昏昏欲睡、犯困的',
 '眼皮往下沉，注意力开始飘，像随时会睡过去，是 drowsy。温暖的房间、安静的午后很容易给它一个画面。',
 '现代与 drowse 打瞌睡 + -y 对应，相关旧材料接古英语困倦、低垂等；现存记录中 drowsy 早于现代动词 drowse，不能强排动词必先。',Dr,
 'feel drowsy 感到犯困；a drowsy smile 睡意朦胧的笑；a drowsy afternoon 昏昏欲睡的下午。',
 'feel drowsy；a drowsy smile。',
 'drowsy 重接近入睡，dizzy 重头晕；听起来像晕乎，两词的身体感觉并不相同。',
 ('The warm room made me drowsy.','暖和的房间让我犯困。'),('He gave a drowsy smile and closed his eyes.','他睡意朦胧地笑了笑，闭上眼睛。'))
N('drowsiness','/ˈdraʊzinəs/','困倦、昏昏欲睡','drowsy','犯困的',
 'drowsy 是你快睡着，drowsiness 是那股困意本身：它一上来，听讲、阅读都会开始费劲。',
 '白天打瞌睡的感觉可说 daytime drowsiness；它描述接近入睡的状态。',
 'daytime drowsiness 白天困倦；overcome drowsiness 克服困意。',
 'drowsiness 与 fatigue 都可说不在状态，但前者更靠近想睡、要睡，后者可泛说疲劳。',
 ('Drowsiness made it hard to follow the lecture.','困意让人很难跟上讲课。'),('She tried to shake off her drowsiness.','她试着驱散困意。'),history=Dr+[['drowsy + -ness → drowsiness','困倦的状态']])
N('trustworthiness','英 /ˈtrʌstwɜːðinəs/；美 /ˈtrʌstwɜːrðinəs/','可信赖、可靠；值得信任的程度','trustworthy','值得信任的',
 '秘密交给他能守住，事情托给他能认真做，信息从这里来有依据，这种靠得住的性质是 trustworthiness。',
 '可以评价人、来源、系统；具体是诚信、能力还是资料可靠，要看对象。',
 'the trustworthiness of a source 来源的可信度；establish trustworthiness 建立可信赖性。',
 'trustworthiness 是值得被信任，trust 是实际给出的信任；有人被相信，不代表判断一定有充分依据。',
 ('The editor checked the trustworthiness of the source.','编辑核查了来源的可信度。'),('Her consistency helped establish her trustworthiness.','她一贯的表现帮助建立了可信赖的形象。'))
We=[['古英语 werig → 中古英语 weri、wery → weary','劳累、疲惫的'],['weary → weariness、wearily','疲惫状态；疲倦地行动、说话']]
W('weary','英 /ˈwɪəri/；美 /ˈwɪri/','疲倦的；厌倦的',
 '不只跑两步喘一口气，而像走了长路、听了太多重复借口，身心都倦了，是 weary。它常比 tired 多一点长久消耗感。',
 '由古英语 werig 经中古英语延续，是日耳曼语旧词；现代常用 weary of 表示对反复经历的事情厌倦。',We,
 'weary travellers 疲惫的旅人；grow weary 逐渐疲倦；be weary of something 厌倦某事。',
 'grow weary；be weary of。',
 'weary /ˈwɪəri/ 是疲惫、厌倦，wary /ˈweəri/ 是警惕；看到一个 y 的小差别，要连着元音和词义分。',
 ('The weary travellers stopped to rest.','疲惫的旅人停下来休息。'),('I grew weary of the same excuses.','我听腻了那些相同的借口。'))
N('weariness','英 /ˈwɪərinəs/；美 /ˈwɪrinəs/','疲惫；倦怠、厌倦','weary','疲倦、厌倦的',
 '长时间的劳作、奔波或重复经历，把人一点点耗空，留下的倦意是 weariness。可以从脚步、声音里听出来。',
 '身体疲倦可说 physical weariness，对争论听烦了也可说 weariness with the argument。',
 'a sense of weariness 倦怠感；weariness with something 对某事厌倦。',
 'weariness 是倦意，wariness 是戒心；一个想歇下来，一个在小心提防。',
 ('There was weariness in her voice.','她的声音里透着疲惫。'),('His weariness with the argument was obvious.','显然，他已经厌倦了这场争论。'),history=We+[['weary + -ness → weariness','现代疲倦、厌倦的名词对应']])
W('wearily','英 /ˈwɪərəli/；美 /ˈwɪrəli/','疲倦地；厌倦地',
 '拖着步子坐下、对老问题又叹一口气，这些动作怎样发生，可以用 wearily 来补上那股倦意。',
 'weary 的 y 改 i，加 -ly → wearily；中古英语已有相应形式。-ly 在这里把疲倦性质转成动作方式。',We+[['weary + -ly → wearily','带着疲倦、厌倦地行动']],
 'sigh wearily 疲倦地叹气；sit down wearily 疲惫地坐下；say wearily 厌倦地说。',
 'sigh wearily；sit down wearily。',
 'wearily 疲倦地与 warily 警惕地只差一字母；walk wearily 拖着倦步，walk warily 小心前行。',
 ('She sat down wearily at the kitchen table.','她疲惫地在餐桌旁坐下。'),('“Not again,” he said wearily.','“怎么又来了，”他厌倦地说。'))
W('selfless','/ˈselfləs/','无私的；为别人着想的',
 '做决定时把别人的需要放在前面，不只盘算自己能得什么，这种付出可以说 selfless。',
 'self 自己 + -less 无、少；现代固定为不以自己利益为中心的性质，不是说一个人没有身份。',
 [['self + -less → selfless','不以自身私利为中心'],['现代 selfless','愿意为他人付出的、无私的']],
 'a selfless act 无私举动；selfless service 无私服务；selfless devotion 无私奉献。',
 'a selfless act；selfless service。',
 'selfless 无私与 selfish 自私方向相反；selfless 评价动机、付出，quiet 安静并不能说明同样的品质。',
 ('It was a selfless act that helped the whole group.','那是帮助全组人的无私举动。'),('She is admired for her selfless service.','她因无私服务而受到敬重。'))
N('selflessness','/ˈselfləsnəs/','无私；无私付出','selfless','为他人着想、无私的',
 'selfless 描述那个人或举动，selflessness 是把先顾他人、不求私利的品质拿出来说。',
 '可说一次行动体现的无私，也可说某人一贯的品质。',
 'show selflessness 表现无私；an example of selflessness 无私付出的例子。',
 'selflessness 是无私的品质，selfishness 是以私利为中心；词干 selfless、selfish 决定方向。',
 ('Her selflessness impressed the whole team.','她的无私让全队印象深刻。'),('The rescue was an example of extraordinary selflessness.','这次救援体现了非凡的无私付出。'))
N('sexiness','/ˈseksinəs/','性感、性感吸引力','sexy','性感、有吸引力的',
 '一件衣服、一个造型让人感到性感，sexiness 就是这份吸引感本身；它不是指具体的性行为。',
 '常见于时尚、表演、广告的评价，语气比较正式的 sexual attractiveness 更口语。',
 'the sexiness of a design 设计的性感吸引力；a touch of sexiness 一点性感。',
 'sexiness 是性感吸引，sexuality 涉及性、性取向、性表达等更广领域；两个名词范围不同。',
 ('The dress combines elegance with a touch of sexiness.','连衣裙把优雅和一点性感结合起来。'),('The article discusses the role of sexiness in advertising.','文章讨论性感吸引力在广告里的作用。'))
N('nastiness','英 /ˈnɑːstinəs/；美 /ˈnæstinəs/','恶意、刻薄；令人不快的性质、事情','nasty','恶劣、刻薄、令人不快的',
 '一句话专门刺人，让人觉得恶毒，是 nastiness；某种味道、场面令人不快，也能说它的 nasty 性质。',
 '说人际行为时常重恶意、刻薄；其他对象可重脏、恶心、恶劣。',
 'the nastiness of a remark 言语的恶毒；unnecessary nastiness 无谓的刻薄。',
 'nastiness 不等于所有 criticism 批评；批评可具体而建设性，nastiness 常带伤人的恶意。',
 ('The nastiness of the comment shocked her.','评论的恶毒让她震惊。'),('There was no need for such nastiness.','没必要这么刻薄。'))
N('soundness','/ˈsaʊndnəs/','可靠、健全；完好、稳固','sound','完好的、可靠的、合乎道理的',
 '桥走上去稳，方案推敲后站得住，财务基础经得起检查，这种不容易垮的性质是 soundness。',
 '这里的 sound 是健全、可靠，不取声音义；可说结构、推理、经营等对象是否扎实。',
 'structural soundness 结构稳固；the soundness of an argument 论证的可靠性。',
 'soundness 不是音量大小；音量可用 loudness，前面的 sound 在这里是另一个形容词义。',
 ('The engineer checked the structural soundness of the bridge.','工程师检查了桥梁结构是否稳固。'),('They questioned the soundness of the plan.','他们质疑计划是否稳妥可靠。'))
N('playfulness','/ˈpleɪfəlnəs/','爱玩、嬉戏；轻松俏皮','playful','爱玩、逗趣的',
 '狗追着球玩，孩子带着笑尝试新动作，是 playfulness；设计、文字里轻快逗趣的劲头也能用。',
 '不只说真在做游戏，也可以说一段对话、一个作品的俏皮风格。',
 'a sense of playfulness 俏皮感；childlike playfulness 孩子般的嬉戏劲头。',
 'playfulness 是轻松、有玩趣，carelessness 是粗心；认真做的作品也可以很俏皮。',
 ('The puppy’s playfulness made everyone smile.','小狗爱玩的样子让大家都笑了。'),('The design has a sense of playfulness.','设计带着一种俏皮感。'))
N('inventiveness','/ɪnˈventɪvnəs/','善于发明；有巧思、创意','inventive','能想出新方法、有创造力的',
 '没有现成工具，却能把手边材料改成一个新办法，这种善于想招、动脑创造的能力是 inventiveness。',
 '常夸解决问题的巧思、作品的新颖安排，也可说技术发明能力。',
 'technical inventiveness 技术创造力；show inventiveness 展现巧思。',
 'inventiveness 强调想出新东西、新办法，imitation 模仿则借已有样式；实际创作也可能两者并用。',
 ('The solution showed remarkable inventiveness.','这个解决办法展现了出色巧思。'),('We admired the inventiveness of the stage design.','我们赞赏舞台设计的创造力。'))
N('loveliness','/ˈlʌvlinəs/','美丽、可爱；令人喜爱的美好','lovely','美丽、可爱、令人愉悦的',
 '眼前花园让你忍不住说真美，一个人的温柔举止也让你觉得可亲，这份令人喜爱的美好可以叫 loveliness。',
 '常带欣赏、喜爱的语气，形容景色、声音、人物或整体感觉。',
 'the loveliness of the garden 花园的美；simple loveliness 朴素的美好。',
 'lovely 是形容词，loveliness 接它形成名词；这里的 -ly 不把 lovely 当普通副词处理。',
 ('We admired the loveliness of the garden.','我们欣赏花园的美丽。'),('The song has a quiet loveliness.','歌曲有一种宁静的美。'))
N('uneasiness','/ʌnˈiːzinəs/','不安、担忧；不自在','uneasy','不安、心里不踏实的',
 '说不出一定会出什么事，心里却放不稳、总有一点不对劲，是 uneasiness。也能是与人相处时不自在。',
 '通常比强烈恐惧更含糊、持续；可以说不安来自什么，也可以先只描述那种感觉。',
 'a sense of uneasiness 不安感；uneasiness about something 对某事担忧。',
 'uneasiness 常是心里不安，disease 是疾病；它们虽都可联想到不舒适，现代词义和用途不同。',
 ('I felt a growing uneasiness about the plan.','我对计划越来越感到不安。'),('There was uneasiness in the room after his remark.','他说完那句话后，屋里有些不自在。'))
N('meanness','/ˈmiːnnəs/','刻薄、恶意；吝啬','mean','刻薄的；不愿给予的、吝啬的',
 '对人讲话总想刺一下，是刻薄；该分享时一点也不肯拿出来，是吝啬。meanness 接的是 mean 的这组性质。',
 '看行为对象决定重心：a mean remark 常是刻薄，mean with money 常是吝啬。',
 'the meanness of a remark 言语的刻薄；meanness with money 用钱上的吝啬。',
 'meanness 不取 mean 意味着、平均值等其他来源和用法；这里由形容词的刻薄、吝啬义决定。',
 ('The meanness of his reply upset her.','他回复里的刻薄让她难过。'),('His meanness with money surprised his friends.','他花钱的吝啬让朋友们吃惊。'))
N('fearlessness','英 /ˈfɪələsnəs/；美 /ˈfɪrləsnəs/','无畏、不惧','fearless','无畏、敢于面对危险的',
 '危险、压力就在眼前，仍敢向前、不被吓退，这份无畏是 fearlessness。可夸行为，也可夸表达立场的胆量。',
 '强调敢面对的品质；具体行动是否明智，还要看准备、判断等别的因素。',
 'show fearlessness 表现无畏；fearlessness in debate 辩论中的无畏。',
 'fearlessness 无畏与 recklessness 鲁莽不同：后者批评不顾风险，前者本身不说明判断是否周全。',
 ('Her fearlessness impressed the audience.','她的无畏让观众印象深刻。'),('The report praises his fearlessness in asking difficult questions.','报告赞扬他敢问难题的胆量。'))
N('ineffectiveness','/ˌɪnɪˈfektɪvnəs/','无效；不起作用、效果不佳','ineffective','不能产生所需效果的',
 '忙了很多，想解决的问题却还在，这种没能奏效的状态叫 ineffectiveness。',
 '常评价措施、工具、安排没有达到预期目的；是否费钱、费时是另一个比较角度。',
 'the ineffectiveness of a policy 政策无效；demonstrate ineffectiveness 显示没有效果。',
 'ineffectiveness 是没奏效，inefficiency 是效率低；做得慢但最终有效，与做了也没用不同。',
 ('The report highlights the ineffectiveness of the measure.','报告指出了这项措施没有奏效。'),('Repeated failures exposed the system’s ineffectiveness.','反复失败暴露了这套系统不起作用。'))
N('weightlessness','/ˈweɪtləsnəs/','失重；失重状态','weightless','处于失重状态的',
 '人在航天器里像漂浮着，不再被地板托出熟悉的体重感，这就是常见的 weightlessness 画面。',
 '轨道上的失重常来自人和航天器一起自由落体；引力仍在起作用，物体质量也没有消失。',
 'experience weightlessness 体验失重；a period of weightlessness 一段失重状态。',
 'weightlessness 是失重状态，不等于 masslessness 没有质量；也不能直接解释为空间里完全没有引力。',
 ('The astronauts experienced weightlessness in orbit.','宇航员在轨道上经历失重。'),('The film shows how objects move during weightlessness.','影片展示了物体在失重状态下怎样运动。'),sources=['https://en.wiktionary.org/wiki/weightlessness#English','https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/free-falling-objects/'])
N('divisiveness','/dɪˈvaɪsɪvnəs/','制造分裂、引发对立的性质','divisive','使人分裂、对立的',
 '一个话题不只是意见不同，还让人分成互相排斥的阵营，这种容易造成分裂的作用叫 divisiveness。',
 '可说言论、问题、政策带来的对立；常带批评这种分裂效果的语气。',
 'the divisiveness of an issue 议题引发对立的程度；political divisiveness 政治上的分裂对立。',
 'divisiveness 是导致对立，diversity 是多样性；人各有不同，不必自动分成互相敌对的阵营。',
 ('The debate revealed the divisiveness of the issue.','辩论显出了这个议题多容易引发对立。'),('The speaker tried to reduce the divisiveness of the discussion.','发言者试图减少讨论中的阵营对立。'))
N('clumsiness','/ˈklʌmzinəs/','笨拙；动作、表达不灵巧','clumsy','笨拙、不够灵巧的',
 '转身碰翻杯子，操作小零件总抓不稳，是动作笨拙；一句解释把简单事情绕乱，也能说表达 clumsiness。',
 '可以描述人的肢体动作，也可以评价设计、措辞处理得不够巧妙。',
 'physical clumsiness 动作笨拙；the clumsiness of a design 设计的不灵巧。',
 'clumsiness 是不灵巧，carelessness 是不仔细；认真小心的人也可能暂时手忙脚乱。',
 ('His clumsiness knocked the vase off the table.','他动作笨拙，把花瓶碰下了桌。'),('The clumsiness of the wording confused readers.','措辞笨拙，让读者看糊涂了。'))
W('wakeful','/ˈweɪkfəl/','不眠、清醒的；警醒的',
 '别人可能已经睡了，你仍醒着，或这一夜总没睡着，可以说 wakeful。它也能强调保持警醒。',
 'wake 醒 + -ful 具有、充满相应性质，形成清醒、不眠的形容词；再加 -ness 得 wakefulness。',
 [['wake + -ful → wakeful','处于醒着、不眠状态'],['wakeful → wakefulness','清醒或不眠的状态']],
 'a wakeful night 不眠之夜；a wakeful child 还醒着的孩子；remain wakeful 保持清醒。',
 'a wakeful night；remain wakeful。',
 'wakeful 是醒着的性质，awake 也说醒着；wakeful 更常突出难以入睡、持续不眠或警醒。',
 ('She spent a wakeful night worrying about the exam.','她担心考试，一夜没怎么睡。'),('The child was unusually wakeful.','孩子一反常态，一直醒着。'),sources=['https://en.wiktionary.org/wiki/wakeful#English','https://kaikki.org/dictionary/English/meaning/w/wa/wakeful.html'])
N('wakefulness','/ˈweɪkfəlnəs/','清醒；不眠状态','wakeful','醒着、不眠的',
 '不是睁开眼那一下，而是持续醒着的状态，叫 wakefulness。它可和睡眠作为两种状态对照。',
 'periods of wakefulness 是一段段清醒时间；夜里持续醒着也可这样描述。',
 'sleep and wakefulness 睡眠与清醒；periods of wakefulness 清醒时段。',
 'wakefulness 是醒着，awareness 是意识到、觉察；人在清醒时，也可能没觉察某个具体变化。',
 ('The study compares sleep and wakefulness.','研究比较睡眠与清醒状态。'),('The night included long periods of wakefulness.','那一夜有很长时间没睡着。'))
N('sleeplessness','/ˈsliːpləsnəs/','睡不着、失眠；不眠状态','sleepless','没有睡眠、睡不着的',
 '身体想休息，夜里却一直没睡着，这段缺少睡眠的状态是 sleeplessness。',
 'sleepless 描述那一夜、那个人，sleeplessness 把没睡的状态及影响拿出来谈。',
 'a period of sleeplessness 一段失眠时期；sleeplessness and tiredness 不眠与疲劳。',
 'sleeplessness 是没睡、睡不着，sleepiness 是困意；很想睡也可能仍然睡不着。',
 ('Worry contributed to her sleeplessness.','担忧让她睡不着。'),('Sleeplessness made the next day difficult.','一夜没睡让第二天很难熬。'))
Cl=[['拉丁 callum 硬皮、老茧 → callosus','皮肤变硬、变厚'],['英语 callous → callousness','像心长了硬茧 → 冷漠无情；相应性质']]
W('callous','/ˈkæləs/','冷漠无情、麻木不仁的',
 '别人正在受苦，他却像心上长了硬茧，感受不到痛，也不在意，是 callous 的比喻核心。',
 '借拉丁 callosus 硬皮的，来自 callum 硬皮、老茧；身体变硬的材料发展为对别人痛苦缺乏感受。',Cl,
 'a callous remark 冷酷言语；a callous disregard for suffering 对痛苦的冷漠无视；callous behaviour 冷酷行为。',
 'a callous remark；callous disregard。',
 'callous 重无视他人感受，calm 是平静；在困难时保持平静，不等于对痛苦无动于衷。',
 ('His callous remark upset the family.','他冷酷的话让家人难过。'),('The report criticised the callous treatment of the workers.','报告批评了对工人冷漠无情的待遇。'))
N('callousness','/ˈkæləsnəs/','冷酷、麻木不仁','callous','对他人痛苦冷漠无情的',
 'callous 描述那句伤人的话、那个不在乎的人，callousness 则是这种心像硬茧一样没反应的冷漠。',
 '常评价对痛苦、不幸、弱势处境的麻木态度，比普通不友好更重。',
 'the callousness of a remark 言语的冷酷；show callousness 表现冷漠。',
 'callousness 不是 mere bluntness 说话直接；直说事实与不顾对方痛苦，是两个不同评价。',
 ('The callousness of the response shocked everyone.','回应的冷酷让所有人震惊。'),('She was angered by his callousness.','他的麻木不仁让她愤怒。'),history=Cl+[['callous + -ness → callousness','冷漠无情的性质']])
N('liveliness','/ˈlaɪvlinəs/','活泼；生动、活跃','lively','活泼、生动的',
 '人说话有神采，街上有人声、活动，讨论你来我往，都能让人感到 liveliness。它是充满生气的感觉。',
 '可说人物性格，也可说环境、谈话或作品的活跃程度。',
 'the liveliness of a conversation 谈话的活跃；youthful liveliness 年轻的活力。',
 'liveliness 重有生气、有变化，loudness 只说音量；活跃不必靠吵闹。',
 ('Her liveliness brightened the room.','她的活泼让屋里气氛明快起来。'),('We enjoyed the liveliness of the discussion.','我们喜欢讨论的活跃气氛。'))
N('steadfastness','/ˈstedfæstnəs/','坚定、不动摇；忠贞','steadfast','立场、承诺坚定的',
 '压力来了，仍稳稳站在承诺的位置上，这份不轻易改心的坚持是 steadfastness。',
 '前面的 steadfast 含旧的站立位置与牢固材料，fast 在这里不是快；-ness 把坚定品质名词化。',
 'steadfastness in adversity 逆境中的坚定；steadfastness of purpose 目标坚定。',
 'steadfastness 常赞坚持信念，stubbornness 常批评拒不改变；具体评价看坚持的理由和情境。',
 ('Her steadfastness encouraged the rest of the team.','她的坚定鼓舞了其他队员。'),('The letter praises his steadfastness in difficult times.','信中赞扬了他在困难时期的不动摇。'))
N('saltiness','/ˈsɔːltinəs/','咸味、咸的程度','salty','有咸味的',
 '同样一碗汤，有人尝一口说太咸，讨论的就是 saltiness。它首先是人能尝到的味道性质。',
 '可说食物、饮料的咸味强弱；taste the saltiness 是尝到那股咸。',
 'the saltiness of soup 汤的咸味；a slight saltiness 一点咸味。',
 'saltiness 常说尝出的咸味，salinity 更常是水等的盐度、含盐量指标；两者相关，关注点不同。',
 ('The cheese added saltiness to the dish.','奶酪给菜增加了咸味。'),('She noticed a slight saltiness in the water.','她尝出水里有一点咸味。'))
N('wariness','英 /ˈweərinəs/；美 /ˈwerinəs/','警惕、戒心；谨慎提防','wary','警惕、小心提防的',
 '新的情况还不清楚，你没有马上相信或靠近，而是先留着一点戒心，是 wariness。',
 '可以是合理谨慎，也可以是因经验而来的不信任；程度要看修饰语。',
 'wariness of strangers 对陌生人的戒心；initial wariness 起初的警惕。',
 'wariness 戒心与 weariness 疲惫差一个元音；一个怕有风险，一个已被消耗得累。',
 ('Her initial wariness gradually disappeared.','她起初的戒心逐渐消失。'),('The proposal was greeted with wariness.','大家谨慎地看待这项提案。'))
N('cockiness','英 /ˈkɒkinəs/；美 /ˈkɑːkinəs/','自负、过分自信','cocky','自负、得意过头的',
 '像公鸡昂着头，觉得自己肯定高人一等，这种神气过头的自信是 cockiness。它通常带批评。',
 '不是有能力就一定 cocky，而是态度显得过分笃定、轻视别人。',
 'youthful cockiness 年轻人的自负；a touch of cockiness 一点自负。',
 'confidence 可以是适度自信，cockiness 通常说自信过头；夸自信与批评自负，语气不同。',
 ('His cockiness annoyed his teammates.','他的自负让队友反感。'),('The defeat took away some of her cockiness.','失败让她收敛了些自负。'))
Mk=[['古诺斯语 mjukr 柔软等 → 中古英语 meke','柔和、温顺的性质'],['英语 meek → meekness','温和谦顺；这种态度、品质']]
W('meek','/miːk/','温顺、谦顺的；不反抗的',
 '声音轻，不争强，受了要求也顺从，可以说 meek。有时是赞温和谦逊，有时是在批评过于顺从。',
 '中古英语 meke 等通常接古诺斯语 mjukr 柔软的；柔软的身体画面走到不强硬、温顺的态度。',Mk,
 'a meek voice 温顺的声音；a meek reply 谦顺回答；meek and mild 温和顺从。',
 'a meek reply；meek and mild。',
 'meek 是态度柔顺，weak 是力量、能力弱；一个人可以有能力却温和，也可以无力却很强硬。',
 ('She answered in a meek voice.','她用谦顺的声音回答。'),('He was far less meek than his quiet manner suggested.','他并不像安静的外表看起来那样顺从。'))
N('meekness','/ˈmiːknəs/','谦顺、温顺','meek','温和、顺从的',
 'meek 是人表现得柔和不争，meekness 则说这份谦顺本身。它的褒贬取决于文本是在赞谦逊，还是批评不反抗。',
 '文学、宗教语境可正面谈谦顺；普通叙事也可说态度过分顺从。',
 'with meekness 谦顺地；an appearance of meekness 温顺的外表。',
 'meekness 温顺与 weakness 弱小不等同；前者主要是态度，后者可说能力、力量。',
 ('He accepted the criticism with unexpected meekness.','他一反常态，谦顺地接受了批评。'),('The story contrasts her meekness with her inner strength.','故事对照了她外在的温顺与内心的力量。'),history=Mk+[['meek + -ness → meekness','谦顺、温顺的性质']])
N('worthlessness','英 /ˈwɜːθləsnəs/；美 /ˈwɜːrθləsnəs/','无价值、无用；无价值感','worthless','没有价值、用途的',
 '一个东西派不上用场、没有所需价值，叫 worthless；worthlessness 是这种无用、无价值状态，也能说人的主观无价值感。',
 '用于物品、资料时常评价用途；feelings of worthlessness 则着眼人的感受。',
 'the worthlessness of something 某物的无用；feelings of worthlessness 无价值感。',
 'worthlessness 是价值评价，helplessness 是无能为力；有帮助意愿却做不到，不等于毫无价值。',
 ('The test revealed the worthlessness of the old data.','测试显示旧数据已无使用价值。'),('The novel explores feelings of worthlessness.','小说探讨无价值感。'))
N('messiness','/ˈmesinəs/','凌乱；混乱、复杂难理','messy','凌乱、混乱的',
 '桌上东西堆着、线缠着，是 messiness；一件事牵涉很多关系、界限不清，也能用这种乱作比喻。',
 '可以是物理的不整齐，也可以是现实过程难按理想模型整齐切开的复杂。',
 'the messiness of a room 房间凌乱；the messiness of real life 现实生活的纷乱复杂。',
 'messiness 是杂乱，dirtiness 是脏污；桌面排布乱，未必有污垢。',
 ('The messiness of the desk made it hard to find anything.','桌面太乱，找东西很难。'),('The book captures the messiness of family life.','书中捕捉了家庭生活的纷乱复杂。'))
N('sloppiness','英 /ˈslɒpinəs/；美 /ˈslɑːpinəs/','马虎、草率；邋遢、不整齐','sloppy','草率、邋遢的',
 '该核对的数字没核对，写完就交；衣物、手稿随便糊弄，这种缺少仔细照料的马虎叫 sloppiness。',
 '常批评工作不仔细、外观不整洁；比单说东西放得乱更有草率评价。',
 'sloppiness in the work 工作马虎；careless sloppiness 粗心草率。',
 'sloppiness 重草率，messiness 重凌乱；很整齐的一张表也可能因漏核数据而表现 sloppiness。',
 ('The errors were caused by sloppiness.','错误是马虎造成的。'),('The editor criticised the sloppiness of the draft.','编辑批评初稿写得草率。'))
N('breathlessness','/ˈbreθləsnəs/','气喘、呼吸急促；喘不过气的感觉','breathless','气喘、来不及换气的',
 '跑上楼后话接不上，要停下来吸气，那份喘不过气的感觉是 breathlessness。也可在强烈激动、紧张的叙述里出现。',
 'breathless 描述人当时气喘，breathlessness 把这种呼吸感觉拿出来谈。',
 'a feeling of breathlessness 气喘感；sudden breathlessness 突然喘不过气。',
 'breathlessness 是气喘、呼吸困难感，breathing 是呼吸动作本身；后者不自动带不适。',
 ('She paused to recover from her breathlessness.','她停下来缓一缓气喘。'),('The report records episodes of breathlessness.','报告记录了几次喘不过气的情况。'))
N('timelessness','/ˈtaɪmləsnəs/','经久不衰；超越时代；时间仿佛停驻的感觉','timeless','不受时代限制、经久不衰的',
 '一首老歌隔很多年仍打动人，可说它有 timelessness；一个安静场景让人忘记钟表，也可带出时间停住的感觉。',
 '常评价艺术、风格、主题不随时尚过期；也可描写气氛中的时间感。',
 'the timelessness of a story 故事的历久弥新；a sense of timelessness 时间停驻感。',
 'timelessness 不是 timeliness 及时、合时宜；一个跨越时代，一个刚好赶上当下时机。',
 ('The film captures the timelessness of the story.','影片表现了这个故事历久弥新的力量。'),('The empty church had a sense of timelessness.','空荡的教堂让人觉得时间仿佛停住。'))
Rg=[['古诺斯语 rǫgg 毛簇、蓬乱等 → 中古英语 rugged','粗糙、蓬乱的外观'],['现代 rugged → ruggedness','崎岖、粗犷；坚固耐用的性质']]
W('rugged','/ˈrʌɡɪd/','崎岖不平的；粗犷的；坚固耐用的',
 '山地凹凸难走是 rugged；一个设备经得起磕碰、恶劣环境，也可叫 rugged。共同画面是粗硬、经得住折腾。',
 '接中古英语 rugged、roggyd 等，关联北欧语毛簇、蓬乱的材料；今天 -ed 保留 /ɪd/，这是固定形容词读音。',Rg,
 'rugged terrain 崎岖地形；rugged features 粗犷面容；a rugged device 坚固耐用的设备。',
 'rugged terrain；a rugged device。',
 'rugged 可以夸耐用，不一定是做工粗劣；rough 粗糙范围更广，未必包含经得住使用的评价。',
 ('The road crosses rugged terrain.','道路穿过崎岖地形。'),('They designed a rugged camera for outdoor use.','他们设计了一款适合户外使用的耐用相机。'))
N('ruggedness','/ˈrʌɡɪdnəs/','崎岖、粗犷；坚固耐用','rugged','崎岖、粗硬或坚固耐用的',
 '看山路时，ruggedness 说崎岖；看设备时，它说经得起磕碰、环境考验。对象不同，中文就要跟着变。',
 '可以评价自然地形、外表风格，也可以讨论产品的耐用程度。',
 'the ruggedness of the landscape 地貌崎岖；equipment ruggedness 设备耐用性。',
 'ruggedness 不等于精密度 precision；设备可既耐用又精密，两项性质并不冲突。',
 ('The ruggedness of the landscape slowed their progress.','地貌崎岖，拖慢了他们的前进。'),('The tests focused on the camera’s ruggedness.','测试重点考察相机是否耐用。'),history=Rg+[['rugged + -ness → ruggedness','崎岖、粗犷、耐用的性质']])
Sl=[['中古英语 slugge 懒散的人等 + -ish → sluggish','早期描述人、头脑迟钝懒散'],['现代 sluggish → sluggishness','反应慢、缺少活力；相应迟缓状态']]
W('sluggish','/ˈslʌɡɪʃ/','迟缓的；反应慢、缺少活力的',
 '点了按钮半天才反应，早晨脑子转不快，市场迟迟没活跃起来，都能 sluggish。它是该动却慢、没精神的感觉。',
 '接中古英语 slugge 懒散者等 + -ish 性质尾；不是必须从今天蛞蝓动物名反推动词先后，旧词族本就有慢、懒散材料。',Sl,
 'a sluggish response 迟缓反应；a sluggish economy 低迷经济；feel sluggish 感到没精神。',
 'a sluggish response；feel sluggish。',
 'sluggish 重缺少应有反应、活力，slow 只是速度慢；故意放慢做细工，不一定是 sluggish。',
 ('The computer became sluggish after the update.','更新后，电脑反应变慢了。'),('I felt sluggish all morning.','整个上午我都觉得没精神。'),sources=['https://en.wiktionary.org/wiki/sluggish#English','https://www.etymonline.com/word/sluggish'])
N('sluggishness','/ˈslʌɡɪʃnəs/','迟缓、反应慢；不活跃','sluggish','迟缓、缺少活力的',
 'sluggish 是系统、人或经济表现得慢，sluggishness 是把这种迟迟动不起来的状态拿来讨论。',
 '既可以说身体、头脑的迟钝感，也可以评价系统反应与市场活跃度。',
 'system sluggishness 系统迟缓；economic sluggishness 经济不活跃。',
 'sluggishness 不是稳定 steady；稳定说变化平稳，迟缓说反应、进展达不到所需速度。',
 ('Users complained about the system’s sluggishness.','用户抱怨系统反应迟缓。'),('The report notes continued sluggishness in demand.','报告指出需求持续不活跃。'),history=Sl+[['sluggish + -ness → sluggishness','迟缓、不活跃的状态']])
Al=[['含 loof 上风方向等材料的航海用语','让船保持距离；远源通常联系荷兰语 loef'],['英语 aloof → aloofness','空间上远离 → 人际态度疏远、冷淡']]
W('aloof','/əˈluːf/','冷淡疏远的；不参与的',
 '大家在热络聊天，他像站在圈外，保持距离，不愿加入，这种态度是 aloof。它常是情感、人际上的远。',
 '从含 loof 上风方向的航海用语发展，早期有保持离开某处、保持距离的材料；后来用来形容人疏远、置身事外。',Al,
 'remain aloof 保持疏远；aloof from the group 与群体保持距离；an aloof manner 冷淡态度。',
 'remain aloof；aloof from。',
 'aloof 常是态度上不亲近，alone 是一个人；独处的人未必冷淡，人多时也可显得 aloof。',
 ('She seemed aloof at the first meeting.','第一次见面时，她显得有些疏远。'),('He remained aloof from the argument.','他置身争论之外。'))
N('aloofness','/əˈluːfnəs/','疏远、冷淡；置身事外的态度','aloof','情感上保持距离、不愿亲近的',
 'aloof 描述那个人像站在圈外，aloofness 则是别人感到的那层距离：不容易接近，也不容易读懂态度。',
 '常说人际间的冷淡、保留；可带批评，也可只是描述尚未熟悉。',
 'an air of aloofness 疏离气质；apparent aloofness 表面冷淡。',
 'aloofness 重人与人之间的距离，shyness 重害羞；表面都少说话，原因不一定相同。',
 ('Her apparent aloofness disappeared as we got to know her.','熟悉起来后，她表面上的疏远消失了。'),('He greeted them with polite aloofness.','他礼貌却疏离地和他们打招呼。'),history=Al+[['aloof + -ness → aloofness','人际疏远、冷淡的性质']])
N('meaninglessness','/ˈmiːnɪŋləsnəs/','无意义；缺少目的、价值的感觉','meaningless','没有明确意义、目的或价值的',
 '反复做一件事，却看不出要达成什么，也看不出有什么作用，便会产生 meaninglessness。文字毫无可理解含义，也可这样说。',
 '可以评价符号、表述没有意义，也可以说生活、活动让人感到空洞无目的。',
 'a sense of meaninglessness 无意义感；the meaninglessness of a phrase 词句没有意义。',
 'meaninglessness 重没有意义、目的，uselessness 重派不上用场；一件无实用价值的纪念物仍可能很有意义。',
 ('The repetition gave him a sense of meaninglessness.','不断重复让他感到没有意义。'),('The essay discusses the meaninglessness of empty slogans.','文章讨论空洞口号为何毫无意义。'))
N('naughtiness','/ˈnɔːtinəs/','淘气、顽皮；不听话的行为','naughty','淘气、不听话的',
 '孩子明知不该，却偷偷闹一个小恶作剧，这种顽皮可以说 naughtiness。语气可责备，也常带一点亲昵。',
 '常用于儿童行为；用在成人玩笑里可能带调皮、暧昧等语气，需看情境。',
 'childhood naughtiness 童年淘气；a bit of naughtiness 一点顽皮。',
 'naughtiness 通常比 serious wrongdoing 轻；并不是所有严重伤害都适合轻描淡写地叫淘气。',
 ('The children’s naughtiness caused a little chaos.','孩子们的淘气惹出一点小乱子。'),('He remembered his childhood naughtiness with amusement.','他好笑地回想童年的顽皮。'))
N('neediness','/ˈniːdinəs/','匮乏、贫困；过分需要关注、认可的状态','needy','缺少所需的；过分依赖关心、支持的',
 '物质上一直缺少必需品，可以是 neediness；关系里不断需要别人确认喜欢自己，也常用来描述情感依赖。',
 '要看说的是生活资源，还是对关注、安慰、认可的强烈需求；后者在日常人际评价中常见。',
 'emotional neediness 情感依赖；financial neediness 经济匮乏。',
 'neediness 常是一种持续需求、依赖状态，a need 可以是任何具体必要；正常提出需要未必带这种评价。',
 ('He tried to hide his neediness.','他试图隐藏自己对关心的依赖。'),('Her neediness put pressure on the friendship.','她强烈的依赖需求给这段友谊带来压力。'))
N('cloudiness','/ˈklaʊdinəs/','多云；浑浊；不清晰','cloudy','多云、浑浊、不清楚的',
 '天空被云挡住，是 cloudiness；液体里看不透、照片轮廓不清，也借云遮住视线的画面。',
 '天气里常谈云量、阴云程度；描述液体、透明物体时常说浑浊。',
 'increasing cloudiness 云量增加；the cloudiness of water 水的浑浊。',
 'cloudiness 不一定指天空真有云；用在液体里是浑浊性质，物理对象决定具体义。',
 ('Increasing cloudiness hid the mountains.','云量增加，遮住了群山。'),('The cloudiness of the water made the bottom hard to see.','水很浑浊，难以看清底部。'))
N('wholesomeness','英 /ˈhəʊlsəmnəs/；美 /ˈhoʊlsəmnəs/','有益健康；健康质朴、纯朴温暖的性质','wholesome','有益身心、健康质朴的',
 '食物给人健康、踏实的感觉，作品给人纯朴温暖、不猎奇的感觉，都可说 wholesomeness。',
 'whole 的旧词族还含完整、健康的材料，经 wholesome 有益健康，再有这个性质名词。',
 'the wholesomeness of food 食物的健康质朴；family-film wholesomeness 家庭电影的纯朴温暖。',
 'wholesomeness 是一种健康、有益或纯朴评价，completeness 是完整；whole 的不同词族分支不能只按完整一义翻。',
 ('The campaign emphasised the wholesomeness of home cooking.','宣传活动强调家常烹饪健康质朴的形象。'),('Viewers enjoyed the wholesomeness of the family film.','观众喜欢这部家庭电影的纯朴温暖。'))
N('bleakness','/ˈbliːknəs/','荒凉、阴冷；黯淡无望','bleak','荒凉、冷清；前景黯淡的',
 '眼前是寒风、空地、没什么生气，感到 bleakness；未来看不到转机，也像同样荒凉的一片。',
 '可以说景色、天气，也可以说故事气氛、生活前景；物理的荒凉常借给心理与未来。',
 'the bleakness of the landscape 景色荒凉；the bleakness of the outlook 前景黯淡。',
 'bleakness 比普通 emptiness 空更带寒冷、无生气或无希望的感觉；空房间也可能明亮温暖。',
 ('The bleakness of the landscape surprised us.','景色的荒凉让我们意外。'),('The ending adds to the bleakness of the story.','结尾让故事更显黯淡无望。'))
N('edginess','/ˈedʒinəs/','紧张、易躁；尖锐前卫感','edgy','紧张、易受刺激；风格尖锐前卫的',
 '人的神经像绷在边缘，稍有动静就烦，是 edginess；艺术、音乐带一点锋利、敢冒险的风格，也可有它。',
 '说人的状态时常是紧张不安，说作品风格时可能是赞有锋芒、前卫。',
 'a sense of edginess 紧张感；the edginess of the music 音乐的前卫尖锐感。',
 'edginess 要随对象分义；人的烦躁与作品的前卫不能直接套同一个中文标签。',
 ('There was edginess in his voice before the interview.','面试前，他的声音里透着紧张。'),('The new arrangement preserved the song’s edginess.','新编曲保留了歌曲的尖锐前卫感。'))
N('unevenness','/ʌnˈiːvənnəs/','不平；不均匀；水平不一致','uneven','不平、不均匀的',
 '地板有高低，光有明暗，作品有的部分精彩有的部分差，都是 unevenness 的不同对象。',
 '共同核心是没有保持在相同高度、程度或水准；不只限于地面。',
 'the unevenness of a surface 表面不平；unevenness in quality 质量不一致。',
 'unevenness 可说物理不均、水平不一；unfairness 是不公平，不能每次见不均匀都自动作道德判断。',
 ('The unevenness of the floor made the table wobble.','地板不平，让桌子晃动。'),('Critics noted unevenness in the quality of the essays.','评论者指出文章质量参差不齐。'))
N('giftedness','/ˈɡɪftɪdnəs/','高天赋；突出的天资','gifted','有天赋、天资突出的',
 '有的人在某些领域学得格外快、理解得深，giftedness 就把这种突出的能力特征当成名词来谈。',
 '常用于教育、心理、艺术领域，具体怎样识别、界定会随所讨论的框架不同。',
 'musical giftedness 音乐天赋；identify giftedness 识别突出天资。',
 'giftedness 是天赋、能力特征，gifting 是送礼；gift 的给予材料在词族中走成了不同常用义。',
 ('The teacher noticed her musical giftedness.','老师注意到了她的音乐天赋。'),('The study explores different ways of identifying giftedness.','研究探讨识别突出天资的不同方式。'))
N('fuzziness','/ˈfʌzinəs/','毛绒感；模糊、不清晰','fuzzy','毛绒绒、模糊的',
 '手摸到细软绒毛是 fuzziness；眼睛看见轮廓不清，也像边缘起了绒。两种感觉沿软、散、不鲜明的画面相连。',
 '可以是触感，也可以是图像、思路、分类边界不够清楚。',
 'the fuzziness of a photo 照片模糊；fuzziness in the categories 分类界限模糊。',
 'fuzziness 不只低分辨率；思路、定义边界不清也能用，而 soft texture 专门聚焦触感。',
 ('The fuzziness of the photo hid the details.','照片模糊，细节看不清。'),('She liked the fuzziness of the blanket.','她喜欢毯子的毛绒触感。'))
N('spiciness','/ˈspaɪsinəs/','辛辣；香料味浓的程度','spicy','辛辣、香料味浓的',
 '同一锅咖喱，有人觉得香辣过瘾，有人觉得辣得受不了，讨论的就是 spiciness 这份辛辣、香料刺激的程度。',
 'spicy 在不同食物里可突出辣，也可突出香料味浓；不是所有 spice 都只带辣。',
 'the spiciness of a curry 咖喱的辛辣程度；adjust the spiciness 调整辣度。',
 'spiciness 是辛辣、香料味，saltiness 是咸味；吃起来刺激与盐多不属于同一种味觉描述。',
 ('The yoghurt softened the spiciness of the sauce.','酸奶缓和了酱汁的辛辣。'),('You can adjust the spiciness to your taste.','你可以按口味调整辣度。'))
Mo=[['古英语 modig','勇敢、高傲、意气强烈等旧义'],['中古英语 → 现代 moody','发展出易怒、阴郁和情绪多变等常用义']]
W('moody','/ˈmuːdi/','情绪多变的；闷闷不乐的；气氛忧郁的',
 '一个人一会儿好好的，一会儿又阴着脸、不想说话，可以说 moody。形容照片、音乐时，则常是带着阴郁、浓重情绪的氛围。',
 '延续古英语 modig；现代可认作 mood 情绪 + -y。旧义包括勇敢、高傲，后来有易怒、阴郁等义，不能把今天每一种 mood 都自动叫 moody。',Mo,
 'moody 不必每分钟都变脸，也能是持续的阴郁、不高兴；用来评价人的性格时带主观看法。',
 'a moody teenager 情绪多变的少年；moody lighting 营造阴郁氛围的灯光。',
 'moody 是情绪阴晴不定、阴郁；emotional 侧重情绪强烈、易激动。它们都不是单凭一个词就能确定的医学诊断。',
 ('He gets moody when he has not slept well.','他没睡好时容易闹情绪。'),('The film opens with moody shots of the empty town.','影片以一组气氛忧郁的空城镜头开场。'))
N('moodiness','/ˈmuːdinəs/','情绪多变；阴郁、闷闷不乐','moody','情绪多变、阴郁的',
 'moody 描述人，moodiness 把这种情绪阴晴不定、爱闷着的状态单独拿出来谈。',
 '不是情绪本身的总称，而是带着多变、阴郁等特点的情绪状态。',
 'a period of moodiness 一阵闷闷不乐；explain someone’s moodiness 解释某人的情绪变化。',
 'mood 是当时的心情；moodiness 常强调爱闹情绪、阴郁或变化多，语气更有评价色彩。',
 ('Her moodiness made the meeting uncomfortable.','她那阴晴不定的情绪让会议气氛有些别扭。'),('He attributed his recent moodiness to lack of sleep.','他觉得自己最近情绪不好是因为睡眠不足。'),history=Mo+[['moody + -ness → moodiness','现代情绪多变、阴郁的状态名词']])
Bl=[['拉丁 blandus','温和、讨人喜欢的'],['英语 bland','温和、不刺激；进一步常说味道、内容平淡']]
W('bland','/blænd/','味道淡的；平淡乏味的；温和不刺激的',
 '吃一口东西，没多少味道；看一段文字，没什么个性和刺激。这种平平的、没劲的感觉，就是 bland 最常用的画面。',
 '借拉丁 blandus 温和、讨人喜欢的材料；英语里发展出不刺激、清淡，再到缺少味道、个性。不能拆成 b + land。',Bl,
 '食物 bland 常嫌味淡；评论作品、说法时常嫌没有个性；有时也可中性表示温和。',
 'bland food 没什么味道的食物；a bland statement 平淡、四平八稳的表态。',
 'bland 是刺激或个性少；plain 是简单、朴素，朴素的食物也可能很好吃，不一定 bland。',
 ('The soup was bland until she added some herbs.','汤本来没什么味道，她加了些香草后才好些。'),('The brochure used bland language that said very little.','小册子的措辞平淡空泛，没说出多少内容。'))
N('blandness','/ˈblændnəs/','味道平淡；内容、风格乏味','bland','清淡、平淡乏味的',
 'bland 是说这东西没什么味，blandness 则把那种缺少滋味、个性的特点当成一件事来讨论。',
 '既能谈食物，也能谈作品、表达。前者是味觉，后者是吸引力、特色不足。',
 'the blandness of the food 食物味道寡淡；criticize the blandness 批评内容平庸。',
 'blandness 不等于 bitterness 苦味：一个是缺少味道、刺激，一个是具体的苦味。',
 ('A little lemon juice balanced the blandness of the sauce.','一点柠檬汁改善了酱汁的寡淡。'),('Reviewers criticized the blandness of the design.','评论者批评这个设计缺乏个性。'))
It=[['古英语 giccig → 中古英语','发痒的'],['现代 itchy；对应 itch + -y','身体发痒；比喻坐不住、想行动']]
W('itchy','/ˈɪtʃi/','发痒的；痒痒的；急着行动的',
 '皮肤上有一点让你想挠，是 itchy 的身体感觉。itchy feet 把这种忍不住想动的感觉放到脚上，表示待不住、想出去走走或旅行。',
 '延续古英语相应形容词，现代构词对应 itch 痒 + -y；ch 是词干的一部分，不是另外一个后缀。',It,
 'an itchy arm 手臂发痒；itchy skin 发痒的皮肤；get itchy feet 待不住、想旅行。',
 'feel itchy；get itchy feet。',
 'itchy 是想挠的痒；ticklish 是怕痒、轻触就想笑等。itchy feet 的脚也未必真的皮肤发痒。',
 ('The woollen sweater made my arms itchy.','羊毛衫让我的胳膊发痒。'),('After months at home, she was getting itchy feet.','在家待了几个月后，她开始想出去走走。'))
N('itchiness','/ˈɪtʃinəs/','发痒；瘙痒感','itchy','发痒的',
 'itchy 描述皮肤、人感觉痒，itchiness 指那种让你想挠的感觉本身。',
 '通常谈身体的痒感；不要看到 itchy feet 就把 itchiness 也生硬解释成旅行欲。',
 'skin itchiness 皮肤发痒；reduce itchiness 缓解痒感。',
 'itchiness 是痒感；a rash 是皮疹。可以有皮疹并发痒，但两词各自说的不是同一个现象。',
 ('The label says the fabric may cause itchiness.','标签说明这种面料可能引起痒感。'),('She described the itchiness as mild but annoying.','她说那种痒不算严重，却挺烦人。'))

R('A1839','把性质、状态、程度作为名词来谈','-NESS：从“它是什么样”转到“这份状态本身”','kind 善良的 → kindness 善意；dizzy 头晕的 → dizziness 头晕感。不是多出一件东西，而是能把性质单独说出来。',
 '说 she is tired，镜头对着她；说 her tiredness，镜头对着她的疲劳。最值得抓住的是这个视角变化。词义也会随常用场景变具体：business 已走到事务、生意，witness 已可指见证人，不能每个词只机械译成某某性。',
 '来自古英语 -nes、-ness 等日耳曼语抽象名词尾，现代仍能接形容词、分词等。常见 y 改 i：happy → happiness、weary → weariness；末尾 e 常保留：appropriate → appropriateness。lovely 中的 -ly 在这里属于形容词，loveliness 不是把副词直接硬接后缀。cleanliness 接 cleanly 清洁的这一历史形容词材料，注意与 clean 直接加后缀不同。business、busyness 同属 busy 词族，前者常已固定为事务、生意，后者突出忙碌。witness 早在古英语已有见证、证明及见证人等义，不宜编造严格的先事后人年代链。',
 [['身体感受与睡眠','dizzy · dizziness · tired · tiredness · drowsy · drowsiness · weary · weariness · wearily · wakeful · wakefulness · sleepless · sleeplessness · breathless · breathlessness · itchy · itchiness'],['体贴、无情与无私','tender · tenderness · selfless · selflessness · callous · callousness · meek · meekness'],['心情、戒备与姿态','uneasy · uneasiness · wary · wariness · cocky · cockiness · aloof · aloofness · moody · moodiness · fearless · fearlessness'],['品质、能力与适合程度','appropriate · appropriateness · trustworthy · trustworthiness · inventive · inventiveness · gifted · giftedness · sound · soundness'],['味道、触感与外观','salty · saltiness · spicy · spiciness · bland · blandness · fuzzy · fuzziness · rugged · ruggedness · uneven · unevenness'],['生活处境、意义与结果','homeless · homelessness · ineffective · ineffectiveness · weightless · weightlessness · meaningless · meaninglessness · worthless · worthlessness'],['行为、个性与活力','silly · silliness · playful · playfulness · clumsy · clumsiness · lively · liveliness · sluggish · sluggishness · naughty · naughtiness · needy · neediness'],['常用义发生固定化','busy · busyness · business · witness']],
 'weariness 疲倦与 wariness 警惕分清；soundness 可说结构、方案可靠，并非声音大小；tenderness 随对象可指温柔、食物柔嫩或压痛；weightlessness 的失重不意味着质量或引力消失。',
 'Her tiredness was obvious, but she answered everyone with kindness.\n\n她显然很疲惫，但对每个人仍很和善。',
 'homeless homelessness clean cleanly cleanliness tender tenderness dizzy dizziness tired tiredness deaf deafness silly silliness appropriate appropriateness drowsy drowsiness trustworthy trustworthiness weary weariness wearily selfless selflessness sexy sexiness nasty nastiness sound soundness playful playfulness inventive inventiveness lovely loveliness uneasy uneasiness mean meanness fearless fearlessness ineffective ineffectiveness weightless weightlessness divisive divisiveness clumsy clumsiness wakeful wakefulness sleepless sleeplessness callous callousness lively liveliness steadfast steadfastness salty saltiness wary wariness cocky cockiness meek meekness worthless worthlessness messy messiness sloppy sloppiness breathless breathlessness timeless timelessness rugged ruggedness sluggish sluggishness aloof aloofness meaningless meaninglessness naughty naughtiness needy neediness cloudy cloudiness wholesome wholesomeness bleak bleakness edgy edginess uneven unevenness gifted giftedness fuzzy fuzziness spicy spiciness moody moodiness bland blandness itchy itchiness busy business busyness witness awareness happiness illness fitness darkness weakness consciousness goodness effectiveness kindness madness sadness willingness fairness thickness greatness loneliness readiness brightness seriousness sweetness bitterness competitiveness blindness mindfulness openness correctness likeness usefulness preparedness toughness attractiveness selfishness uniqueness stiffness hardness laziness unhappiness closeness fondness completeness freshness unwillingness craziness foolishness nervousness responsiveness fullness sharpness awkwardness faithfulness soreness softness stillness ugliness lightness nothingness tightness redness hopelessness dryness friendliness politeness weirdness helplessness lawlessness rudeness boldness eagerness randomness shyness calmness drunkenness numbness cuteness shortness aggressiveness smoothness carelessness quickness robustness stubbornness coolness unfairness firmness restlessness togetherness recklessness gentleness indebtedness alertness cleverness unconsciousness loudness strangeness timeliness baldness vastness harshness hotness coldness worthiness wholeness assertiveness slowness connectedness inclusiveness newness heaviness truthfulness forgetfulness vagueness remoteness nakedness sleepiness pettiness resourcefulness thoughtfulness powerlessness reasonableness ruthlessness unpleasantness frankness hardiness dampness directness gladness idleness wildness badness deliciousness thoroughness quietness distinctiveness tardiness flatness otherness earnestness lateness swiftness thankfulness thinness dullness defensiveness sameness niceness cohesiveness uselessness genuineness incompleteness compactness expressiveness fatness attentiveness cheerfulness conscientiousness bluntness steadiness childishness rightness stickiness viciousness nearness graciousness ripeness awfulness fierceness helpfulness joblessness naturalness peacefulness rawness youthfulness cheapness strictness narrowness neatness shallowness indecisiveness keenness roundness smallness decisiveness lawfulness smartness looseness crispness prettiness wrongness gratefulness seasickness steepness vividness obviousness creepiness possessiveness sourness suddenness agreeableness meaningfulness greenness healthiness rebelliousness')
R('B4385','疲惫的；厌倦的；使疲惫、使厌烦','WEARY：累到身心有点撑不动，或对反复的事感到厌烦','a weary traveller 累坏的旅人；weary of arguments 厌倦争吵；weariness 是那份疲倦，wearily 是疲惫地。',
 '不只是体力用完，反复解释、等待也能把人弄得心累。weary 可以说人疲惫，也能用作动词表示使疲惫、厌烦；先记最常见的形容词搭配。',
 '延续古英语 werig 疲倦的材料。现代 weary + -ness，y 改 i → weariness；weary + -ly，y 改 i → wearily。外形相近的 wary 是警惕的，不是同一个现代词干。',
 [['先看疲惫、厌倦','weary'],['把感觉作为名词','weariness'],['描述动作带着疲惫','wearily']],
 'weary 疲倦，wary 警惕；wearily 疲惫地，warily 警惕地。',
 'The weary traveller sat down and sighed wearily.\n\n疲惫的旅人坐下来，疲倦地叹了口气。','weary weariness wearily')
if __name__=='__main__':save('continuation_20261030_pq',ROOTS,WORDS)
