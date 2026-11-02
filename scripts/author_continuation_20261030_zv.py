"""Common words: retaliation, disorder, visual identity and engulfing."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C1208':dict(words=['revenge','vengeance','vengeful'],label='revenge：把伤害还回去的报复',note='古法语 revengier 接 re- 与 vengier；这里 re- 可能起加强作用，不能固定译成再次。'),
 'C0015':dict(words=['avenge','avenged'],label='avenge → avenged：为所受的伤害讨还',note='古法语 a- 接拉丁 ad-，后半与 vengier、拉丁 vindicare 相连；avenge 与 revenge 是相关借词。'),
 'A2286':dict(words=['chaos','chaotic'],label='chaos → chaotic：混乱状态与混乱的',note='chaos 接希腊张开的虚空、原初无定形状态；chaotic 的借入与英语类推构形有不同分析，逐词保留。'),
 'C0685':dict(words=['logo','logos','logogram','logotype'],label='logo：从表词符号、组合铅字到识别标志',note='logo 是较长词的缩短，来源有 logogram 或 logotype 的解释；现代 logos 也能是 logo 的复数，与希腊概念 logos 分读。'),
 'C0603':dict(words=['gulf','gulfs','engulf','engulfed'],label='gulf → engulf → engulfed：海湾、鸿沟与吞没',note='这里 en- 经法语接拉丁 in-；engulf 可分析为 en- 加 gulf，也可能借古法语 engolfer。gulf 是理解整个动词的基础词，不是带 in- 的派生词。'),
}
W('revenge','/rɪˈvendʒ/','报复、复仇；报仇',
 '别人让我吃了亏，我要让对方也吃亏：这个把伤害还回去的念头，是 revenge 的核心。体育报道也会借它说输过以后赢回来、雪耻。',
 '古法语 revengier 等 = re- + vengier 报仇，后者接拉丁 vindicare 主张权利、惩罚、报仇。这里 re- 可能只是加强动作。英语名词又接法语 revenge 等形式，不能把今天名词简单当英语动词新加尾。',
 [['拉丁 vindicare → 古法语 vengier、revengier','主张、惩罚、讨还 → 报仇'],['法语相关形式 → 英语 revenge','报复动作 → 报复的念头、行为；比赛中雪耻']],
 'take revenge on someone for something：因为某事报复某人。on 接对象，for 接缘由；get revenge 也常见。',
 'seek revenge 寻求报复；a story of revenge 复仇故事；get revenge for an earlier defeat 为先前的失利雪耻。',
 'revenge 通常把焦点放在还击、报复；avenge 常把受害者或要讨还的伤害放进宾语。这是常见视角差别，词本身不能证明报复就合理。',
 ('The novel follows a character who is consumed by a desire for revenge.','小说写了一个满心只想复仇的人。'),('The team got revenge for its earlier defeat with a clear win.','这支队伍以一场明显的胜利，为先前的失利雪了耻。'),sources=['https://en.wiktionary.org/wiki/revenge#English','https://www.etymonline.com/word/revenge'])
W('avenge','/əˈvendʒ/','为……报仇；报……之仇；雪耻',
 '把一件没有讨回来的伤害记在账上，后来替受害者讨还：这是 avenge 的画面。宾语通常告诉你替谁报仇，或要报哪一笔仇。',
 '经盎格鲁法语 avenger、古法语 avengier 等借入：a- 朝向，接拉丁 ad-；vengier 报仇接拉丁 vindicare。a- 在这里有实际历史来源。',
 [['拉丁 ad- 与 vindicare 相关材料 → 古法语 avengier','朝着所受的伤害去讨还'],['法语 → 英语 avenge','为人报仇、报某种伤害之仇；后来也用于比赛雪耻']],
 'avenge a victim 为受害者报仇；avenge a wrong 报所受不公之仇；avenge a defeat 一雪败绩。',
 'avenge a friend 为朋友报仇；avenge the loss 把那次失利赢回来。较常出现在故事、历史叙述和体育报道。',
 'avenge someone 可以表示为这个人报仇；若要表达报复这个人，常用 take revenge on someone。两句的对象关系不同。',
 ('In the story, the hero returns to avenge his brother.','故事里，主人公回来为兄弟报仇。'),('They hoped to avenge their defeat in the previous final.','他们希望一雪上次决赛失利之耻。'),sources=['https://en.wiktionary.org/wiki/avenge#English','https://www.etymonline.com/word/avenge'])
W('avenged','/əˈvendʒd/','报了……之仇；雪了耻〔过去式、过去分词〕',
 '先前受了伤害或输了一场，这次讨还、赢回来了：avenged 把 avenge 放到已经发生或已经完成的叙述里。',
 'avenge 去 e + -ed → avenged；拼写时先去 e，再加完整 -ed。末尾 /dʒ/ 是浊音，因此过去式结尾读 /d/，合成 /dʒd/，不另加一个 /ɪ/ 音节。',
 [['古法语 avengier → 英语 avenge','为人报仇、雪耻'],['avenge 去 e + -ed → avenged','报仇、雪耻发生了；也可作过去分词']],
 'avenged the defeat 雪了败绩之耻；has avenged 已经报了仇；the defeat was avenged 那次失利之耻得以洗雪。',
 'They avenged their earlier loss. 他们把上次输掉的比赛赢回来了。',
 'avenged 是 avenge 的形式；不是 revenge 的过去式，后者是 revenged。先看句中是为谁、为哪件事讨还。',
 ('The team avenged last season’s defeat in the opening match.','这支队伍在揭幕战中，一雪上赛季失利之耻。'),('By the final chapter, the hero has avenged his friend.','到最后一章时，主人公已经为朋友报了仇。'),sources=['https://en.wiktionary.org/wiki/avenged#English','https://www.etymonline.com/word/avenge'])
W('chaos','英 /ˈkeɪɒs/；美 /ˈkeɪɑːs/','混乱、乱成一团；原初的无定形状态',
 '事情还没有排出先后、东西还没有各就各位，整个场面乱成一团，就是日常说的 chaos。它更早的画面却是张开、空旷、没有定形的原初空间。',
 '古法语 chaos 或直接拉丁 chaos，接希腊 khaos 张开的虚空、深渊。后来由宇宙形成秩序以前的无定形状态，扩展到生活中的混乱。',
 [['希腊 khaos → 拉丁 chaos → 法语或直接借入英语','张开的虚空 → 原初无定形状态'],['原初未有秩序 → chaos 的日常义','事情没有组织好、场面失去秩序']],
 'chaos 通常不可数：in chaos 处于混乱中；cause chaos 造成混乱；total chaos 一片混乱。',
 'The room was in chaos. 房间乱成一团。chaotic 是形容词，可以说 a chaotic room。',
 'chaos 是状态名词，chaotic 是性质形容词。科学里的 chaos 有专门含义，不能直接等同于完全没有规则或纯粹随机。',
 ('The office was in chaos during the move.','搬迁期间，办公室乱成一团。'),('A power failure caused chaos at the station.','一次停电让车站陷入混乱。'),sources=['https://en.wiktionary.org/wiki/chaos#English','https://www.etymonline.com/word/chaos'])
W('logo','英 /ˈləʊɡəʊ/；美 /ˈloʊɡoʊ/','标志、标识；用于识别品牌或机构的图形',
 '看到一个小图形、一组特别设计的字，马上认出是哪家公司或机构，这个识别记号就是 logo。它可以主要是字，也可以主要是图。',
 '较长词的缩短：词典有 logogram 或 logotype 的来源解释。较早的 logo- 来自希腊 logos 话语、词；gram 是写出的记号，type 接印记、字模材料。不是现代把 log 和 o 随便拼起来。',
 [['希腊 logos 等材料 → logogram、logotype','表词符号；组合字模、字样等'],['较长词缩短 → 英语 logo','文字、图形符号 → 用来识别品牌或机构的标志']],
 'design a logo 设计标志；a company logo 公司标志；put the logo on the box 把标志放到盒子上。',
 'a new logo 新标志；the logo for a museum 一家博物馆的标识。复数 logos，英 /ˈləʊɡəʊz/、美 /ˈloʊɡoʊz/。',
 'logo 是视觉标识；slogan 是一句口号。一个 logo 可以成为 trademark 的一种，但两词焦点不同。logos 若指希腊哲学、修辞概念，读音与这个普通复数也不同。',
 ('The designer simplified the logo so it would be clear on a small screen.','设计师简化了标志，让它在小屏幕上也能看清。'),('The museum’s logo appears on every ticket.','博物馆的标志印在每张门票上。'),sources=['https://en.wiktionary.org/wiki/logo#English','https://www.etymonline.com/word/logo'])
W('gulf','/ɡʌlf/','海湾；鸿沟、巨大差距',
 '先想海水伸进陆地，形成一个深深的弯。再把两个人的看法摆在很远的两岸：中间仿佛隔着这样一道深水，这就成了意见、生活条件上的 gulf。',
 '古法语 golf 接意大利语 golfo，再经晚期拉丁 colfos 接希腊 kolpos。希腊词的胸怀、衣褶、波谷、海湾等意思共享弯进去或兜住的形状；英语又扩展成巨大间隔。',
 [['希腊 kolpos → 晚期拉丁 colfos → 意大利 golfo → 古法语 golf','胸怀、弯折等形象 → 海湾、深处'],['古法语 → 英语 gulf；具体空间 → 抽象差距','海湾、深渊 → 两方之间难跨越的鸿沟']],
 'a gulf between two views 两种观点间的巨大差距；bridge the gulf 缩小、跨越鸿沟；a deep gulf 深深的鸿沟。',
 'a boat in the gulf 海湾里的船；a gulf in understanding 理解上的巨大差距。',
 'gulf 和 bay 都能称海湾，名称并没有始终一致的大小界线。gulf 的比喻义常强调差距大，比普通 difference 更有隔得很远的感觉。',
 ('The boat crossed the gulf before sunset.','船在日落前横穿了海湾。'),('The discussion revealed a gulf between their expectations.','这场讨论显露出双方期望之间的巨大差距。'),sources=['https://en.wiktionary.org/wiki/gulf#English','https://www.etymonline.com/word/gulf'])
W('gulfs','/ɡʌlfs/','多个海湾；多道鸿沟、巨大差距〔复数〕',
 '地图上不止一处海湾，或人与人之间隔着不止一道深深的差距，就能用 gulfs。',
 'gulf + -s → gulfs。f 保留，/f/ 后的 s 读 /s/，末尾 /fs/；并不是所有 f 结尾的名词都改成 ves。',
 [['希腊 kolpos 经拉丁、意大利语、法语 → gulf','弯入的海湾；后来也比喻巨大间隔'],['gulf + -s → gulfs','多处海湾；多个巨大的间隔']],
 'bays and gulfs 大大小小的海湾；gulfs between communities 社群之间的多道鸿沟。',
 'wide gulfs 巨大差距；the gulfs along a coast 沿岸的海湾。',
 'gulfs 保持 /f/；wolf → wolves 才有 /f/ 到 /v/ 的变化。具体空间和抽象差距，要看它修饰、连接的对象。',
 ('The map shows the bays and gulfs along the coast.','地图标出了沿岸的海湾。'),('The project aims to bridge the gulfs between these communities.','这个项目希望跨越这些社群之间的鸿沟。'),sources=['https://en.wiktionary.org/wiki/gulfs#English','https://www.etymonline.com/word/gulf'])
W('engulf','/ɪnˈɡʌlf/','吞没、淹没；笼罩、压倒',
 '一股很大的东西涌过来，把眼前的目标整个盖住、吞进去：这是 engulf。最早容易想到海水、漩涡，后来烟雾、火、情绪也能占满这个画面。',
 '可分析为英语 en- 放入、使进入 + gulf 深处、海湾，也有借古法语 engolfer 的解释。这里 en- 经法语接拉丁 in-；词源资料保留两条可能路线。',
 [['gulf 深处、海湾；en- 放入、使进入','卷入深处、吞入其中的画面'],['英语构形或古法语 engolfer → engulf','海水吞没 → 烟雾、火等覆盖；情绪或事件压倒']],
 'engulf a building 吞没、笼罩一幢建筑；be engulfed in smoke 被烟雾笼罩；a wave engulfs something 浪头把某物淹没。',
 'Mist engulfed the valley. 雾气笼罩了山谷。也可说 be engulfed by emotion，被强烈的情绪淹没。',
 'engulf 突出覆盖、吞入的整体感觉；surround 只说围在四周，未必把目标盖住。',
 ('Thick fog began to engulf the village.','浓雾开始笼罩村庄。'),('A wave of relief seemed to engulf her.','她仿佛被一阵强烈的宽慰感包围了。'),sources=['https://en.wiktionary.org/wiki/engulf#English','https://www.etymonline.com/word/engulf'])
W('engulfed','/ɪnˈɡʌlft/','吞没、笼罩了；被淹没、被压倒〔过去式、过去分词〕',
 '原来还能看见的目标，后来被雾、浪或一股强烈感受整个覆盖：engulfed 说这个变化已经发生，也常放在 be 后描述被笼罩的处境。',
 'engulf + -ed → engulfed。/f/ 是清音，ed 在这里读 /t/，末尾 /ft/，不多读一个音节。',
 [['gulf 与 en- 的历史构形，或古法语 engolfer → engulf','卷入深处 → 吞没、笼罩'],['engulf + -ed → engulfed','吞没发生了；be engulfed 描述被吞没、笼罩']],
 'engulfed in fog 被雾笼罩；engulfed by a wave 被浪淹没；was engulfed 已被覆盖、压倒。',
 'The hills were engulfed in mist. 群山被薄雾笼罩。后面的 in、by 看具体结构，不把一个介词固定到所有场景。',
 'engulfed 后的 /t/ 是过去式、分词标记的读音；原词的 /f/ 仍然保留。engulfing 则把焦点放在正在吞没或吞没作用上。',
 ('Within minutes, the harbour was engulfed in fog.','几分钟内，港口就被雾笼罩了。'),('She was engulfed by a sudden sense of relief.','她突然涌起一股强烈的宽慰感。'),sources=['https://en.wiktionary.org/wiki/engulfed#English','https://www.etymonline.com/word/engulf'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zv',ROOTS,WORDS)
 extend_lessons()
