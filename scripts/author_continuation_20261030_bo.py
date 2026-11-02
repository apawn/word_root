"""Lie has two histories; belie needs direction, and disease is more than modern wordplay."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
LI=[['古英语 liċġan → 中古英语 liggen、lien → lie〔躺、位于〕','身体横放、处于某位置；lie—lay—lain'],['另源古英语 lēogan、名词 lyġe → lie〔说谎、谎言〕','欺骗、说不实话；lie—lied—lied']]
W('lie','/laɪ/','躺、平放着；位于；说谎；谎言',
 '同一拼写装着两套词：一个说身体放在哪儿，一个说话是否诚实。先分两套，变化就不乱。',
 '躺义接古英语 liċġan，说谎义另接 lēogan，谎言名词也有旧 lyġe。现代同形不等于同源；躺 lie—lay—lain，说谎 lie—lied—lied。',LI,
 'lie down 躺下，lie on the bed 躺床上，lie to someone 对某人说谎，tell a lie 说一个谎。lie in 也可在于。',
 'lie down；lie on；lie to someone；tell a lie；lie in。',
 '躺的过去 lay 又与另一个原形 lay 放置同形：lay a book—laid—laid。I lay down yesterday 昨天躺下，I lied yesterday 昨天说谎，不能混。',
 ('I lay on the sofa for an hour yesterday.','昨天我在沙发上躺了一小时。'),('He lied about where he had been.','他对自己去过哪里撒了谎。'),sources=['https://www.etymonline.com/word/lie','https://en.wiktionary.org/wiki/lie#English'])
W('liar','英 /ˈlaɪə/；美 /ˈlaɪər/','说谎者；骗子〔强调不诚实言语〕',
 '把说假话这件事落到人：他知道或意图让别人相信不实话；直接叫人 liar 评价很重。',
 '接古英语 lēogere、lēgere 等人物词，中古英语多种拼写后定型为 liar。现代可对照 lie + 人物后缀 -ar，但别拿常见 -er 自创拼写替代。',LI[1:]+[['古英语 lēogere 等 → 中古英语 lier 等 → liar','说谎的人；现代标准常用拼写 liar']],
 'call someone a liar 指责某人说谎，a habitual liar 惯常说谎者，a convincing liar 很会把谎说得可信的人。',
 'call someone a liar；a habitual liar；a convincing liar。',
 'liar 说谎者，lier 较少见可说躺着的人；日常骗子不要按普通人物后缀拼作 lier。弄错事实也不自动证明故意撒谎。',
 ('The detective suspected that the witness was a liar.','侦探怀疑证人是个说谎者。'),('She was angry that he had called her a liar.','他指责她说谎，让她很生气。'))
W('underlie','英 /ˌʌndəˈlaɪ/；美 /ˌʌndərˈlaɪ/','位于……下面；构成……基础；是背后原因',
 '看得见的事情下面，还有看不见的结构、假设或原因在撑着它。',
 '古英语 underliċġan 等旧组合延续，under- 下面 + lie 位于、躺。接位置那条 lie，不接说谎；变化 underlay、underlain。',LI[:1]+[['古英语 underliċġan → underlie','处在下面 → 作为基础、背后因素']],
 'assumptions that underlie a theory 理论的基础假设，factors that underlie a problem 问题背后的因素。',
 'underlie a theory；underlie a problem；assumptions that underlie。',
 'underlie 原因、基础在下方支撑，understand 理解是另一个词；A underlies B 是 A 构成 B 基础，主客体别反过来。',
 ('Several assumptions underlie the model.','这个模型以几个假设为基础。'),('A lack of trust underlies much of the conflict.','很多冲突背后的原因是缺乏信任。'))
W('belie','/bɪˈlaɪ/','使显得不真实、证明不符；表象掩盖实情',
 '有两种常见画面：证据让一句话站不住，或平静外表让你看不出心里其实紧张。',
 '现代常用义接古英语 belēogan 用谎欺骗，be- + 说谎那条 lie；后来发展为显示不实、给人错误印象。另有接躺义的同形旧词，但不是这里常用义。',LI[1:]+[['古英语 belēogan → 中古英语 bilien → belie','欺骗、说不实 → 显出不符，或以表象掩盖实情']],
 'The evidence belies his claim. 证据证明他的说法不实。Her smile belies her worry. 笑容让人看不出她其实担忧；担忧本身是真的。',
 'belie a claim；belie expectations；a calm voice belies anxiety。',
 'belie 不等于只说 deny 否认。表象 belies 内在时，常是表象误导、内在仍真；证据 belies 说法时，则是说法被证明不符。按主语判断方向。',
 ('Her calm voice belied her anxiety.','她平静的声音掩盖了内心的焦虑。'),('The figures belie his claim that sales are falling.','这些数字证明了他关于销量下降的说法不实。'),sources=['https://www.etymonline.com/word/belie','https://en.wiktionary.org/wiki/belie#English'])
R('B2890','躺、位于与说谎两源；基础和误导表象分支','LIE：两个旧词合成同一拼写，先分来源再看变形','lie 基础词明确两套；underlie 接躺、位于；liar、belie 接说谎、欺骗。较少见 lier 暂不列词头。',
 '不能画成一个人躺着所以懒得说真话的故事。belie 也需要看主语是证据还是表象，才知道哪里被证明不符、哪里被掩盖。',
 '躺 lie—lay—lain；说谎 lie—lied—lied；under- + 位于义 lie；be- + 欺骗义 lie；liar 旧人物词。',
 [['躺、位于与基础','lie · underlie'],['不实话、人物与表象关系','liar · belie']],
 'lay 是躺义过去式，也另作放置原形；liar 不拼 lier；belie 的表象可能误导而内在是真的。',
 'The calm explanation belied the fear that underlay his decision.\n\n那段平静解释掩盖了决定背后的恐惧。',
 'lie underlie liar belie')
DI=[['古法语 des- + aise → desaise → 中古英语 disese','缺少舒适、困扰、不适'],['现代 disease','义项集中到疾病；旧宽泛不适义逐渐淡出']]
W('disease','/dɪˈziːz/','疾病；病害',
 '旧字面是失去舒适，今天却是更具体的疾病词；人、动物、植物都可有 disease。',
 '经法语 desaise 进入英语，des- 缺少、离开 + aise 舒适，现代可对应 dis- + ease。后来专门化为疾病，不是所有短暂不舒服都自动等于一种 disease。',DI,
 'heart disease 心脏病，plant disease 植物病害，the spread of disease 疾病传播。并非 disease 都传染。',
 'heart disease；plant disease；the spread of disease；a common disease。',
 'disease 常说病种、病理问题，illness 也可着眼患病经历；infection 感染只是其中相关概念，不能把所有 disease 都当传染。',
 ('The textbook describes several common plant diseases.','教材介绍了几种常见植物病害。'),('The research focuses on heart disease.','研究聚焦心脏病。'),sources=['https://www.etymonline.com/word/disease','https://en.wiktionary.org/wiki/disease#English'])
W('diseased','/dɪˈziːzd/','患病、病变的；有病害的',
 '不是在说疾病这个名称，而是描述组织、植物等已经有疾病、病变的状态。',
 'disease + -ed；基础词末尾 /z/ 后读 /d/，不额外读成 /ɪd/。形容词可指患病、被病害影响。',DI+[['disease + -ed → diseased','具有疾病、病变或病害的']],
 'diseased tissue 病变组织，diseased plants 患病植物，diseased branches 有病害的枝条。',
 'diseased tissue；diseased plants；diseased branches。',
 'disease 名词疾病，diseased 描述对象状态；描述人时常用 a person with a disease 更具体，避免把形容词误当完整病名。',
 ('The gardener removed the diseased branches.','园丁剪掉了有病害的枝条。'),('The slide shows healthy and diseased tissue.','幻灯片展示了健康组织和病变组织。'))
R('B2512','缺少舒适的旧义到疾病；状态形容词另说明','DISEASE：旧不适词专门化为疾病，不能只靠字面诊断','disease → diseased；与刚写的 ill、illness、sick、sickness 参照词性和搭配。',
 '经法语借入并发生义项专门化，拆成 dis+ease 是历史线索，不是今天疾病的完整判定标准。',
 '法语 des- + aise → disease；disease + -ed。',
 [['疾病与患病状态','disease · diseased']],
 'disease 不自动传染；diseased 形容组织、植物状态；dis-ease 的字面联想不等于所有不适都是疾病。',
 'The book contrasts healthy plants with plants affected by disease.\n\n这本书把健康植物与受病害影响的植物作了对照。',
 'disease diseased')
if __name__=='__main__':save('continuation_20261030_bo',ROOTS,WORDS)
