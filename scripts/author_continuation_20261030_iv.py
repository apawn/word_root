"""Composing and decomposition, plus selected -gen examples."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['拉丁 com- + pōnere → compōnere，分词 compositus','放到一起、组合；分词词干 composit-'],['不同借入路线','法语 composer → compose；拉丁 compositiō、法语 composicion → composition'],['英语的对应词与现代扩展','composer 人物；compositional 性质；decompose/decomposition 分开、分解']]
W('compose','英 /kəmˈpəʊz/；美 /kəmˈpoʊz/','创作、作曲；组成；安排构图；使平静、镇定',
 '把音符、句子、画面元素组织成一件完整作品。情绪乱了再把自己整理好，compose yourself 就是先定定神。',
 '借法语 composer，是对拉丁 compōnere 放在一起的改造形式，法语 poser 也参与词形影响。不是所有字母 pose 都直接由拉丁 pōnere 原样变来。',C[:2]+[['英语 compose 的动作扩展','组织作品、构成整体；整理情绪使镇静']],
 'compose music 作曲，compose an email 写邮件，compose a picture 安排构图，compose yourself 定定神，be composed of 由……组成。',
 'compose music；compose an email；compose yourself；be composed of。',
 'A is composed of B 是整体由部分组成；B composes A 可说部分构成整体，方向要看主语。compose yourself 不是为自己作一首曲子。',
 ('She composed a short piece for the piano.','她创作了一首钢琴小曲。'),('He paused to compose himself before speaking.','他停下来定了定神，再开口说话。'))
W('composer','英 /kəmˈpəʊzə/；美 /kəmˈpoʊzər/','作曲家；创作者〔较宽用法〕',
 '把音符组织成乐曲的人。日常单独说 composer 通常先想到作曲家，不能把所有写一封邮件的人都叫专业 composer。',
 'compose 去 e + -er，从事者名词。虽然 compose 的对象可以很多，composer 的常用身份义集中在音乐创作。',C[:2]+[['compose + -er → composer','创作者，尤指作曲者、作曲家']],
 'a film composer 电影配乐作曲家，a classical composer 古典音乐作曲家，the composer of the piece 这首曲子的作者。',
 'a film composer；a classical composer；the composer of the piece。',
 'composer 作曲家，songwriter 歌曲作者可涉及旋律、歌词等，performer 表演者；同一人能兼任，但名字说的工作不同。',
 ('The composer wrote the score for the film.','作曲家为电影创作了配乐。'),('The programme lists the composer beside each piece.','节目单在每首曲子旁列出了作曲者。'))
W('composition','英 /ˌkɒmpəˈzɪʃən/；美 /ˌkɑːmpəˈzɪʃən/','组成、成分；作文、作品；作曲；构图',
 '整体由什么拼成、怎样安排，是 composition。化学看成分，作文看句子组织，音乐看乐音，绘画看元素摆放，核心都是部分如何成整体。',
 '经法语 composicion 或直接接拉丁 compositiō，来自 compōnere 的旧分词 composit-。现代与 compose 对应，但名词并非英语随手把 compose 的结尾改成 sition。',C,
 'chemical composition 化学成分，write a composition 写作文，musical composition 作曲或音乐作品，the composition of a painting 一幅画的构图。',
 'chemical composition；write a composition；musical composition；the composition of a painting。',
 'composition 可说过程，也可说结果、结构或作品；chemical composition 不是化学作文，a piano composition 是钢琴作品，不是钢琴的金属成分。',
 ('The analysis revealed the chemical composition of the sample.','分析揭示了样本的化学成分。'),('The class discussed the composition of the painting.','全班讨论了那幅画的构图。'),('She performed one of her own compositions.','她演奏了自己创作的一首作品。'),sources=['https://en.wiktionary.org/wiki/composition#English','https://www.etymonline.com/word/composition'])
W('compositional','英 /ˌkɒmpəˈzɪʃənəl/；美 /ˌkɑːmpəˈzɪʃənəl/','组成、成分或创作相关的；组合式的',
 '看前文正在讲什么：材料的 compositional differences 是成分差异，作曲里的 compositional technique 是创作技法，语言学里又可讲部分如何决定整体意思。',
 'composition + -al，相关形容词。语义学专门义强调整体意义由部分意义及其组合结构决定，不是只把几个词义无序相加。',C[:2]+[['composition + -al → compositional','关于组成、创作的；某些领域指由部分与结构组合而成']],
 'compositional differences 成分差异，compositional techniques 创作技法，compositional meaning 组合性意义。',
 'compositional differences；compositional techniques；compositional meaning。',
 'compositional 要补清领域；The dog bit the man 与 The man bit the dog 用相同词却结构角色不同，不能把组合性理解成忽略顺序、结构的词义相加。',
 ('The study compares compositional differences between the samples.','研究比较样本之间的成分差异。'),('The lecture introduces the composer’s main compositional techniques.','讲座介绍那位作曲家的主要创作技法。'),sources=['https://en.wiktionary.org/wiki/compositional#English','https://plato.stanford.edu/entries/compositionality/'])
W('decomposition','英 /ˌdiːkɒmpəˈzɪʃən/；美 /ˌdiːkɑːmpəˈzɪʃən/','分解、腐解；将整体拆成部分的分析',
 '原来合在一起，现在拆开：落叶逐渐腐解，数学把复杂对象分成较易处理的组成。不是所有 decomposition 都在描述腐烂。',
 'de- 分开、解除 + composition，或对应 decompose 与过程名词形式。来源说明可联系法语 décomposition 及相应英语构词关系，不把每种分解都假定恰好倒放一次最初制造。',C[:2]+[['de- + composition → decomposition','从整体到部分；在生物、化学、数学等各有具体分解义']],
 'the decomposition of leaves 落叶分解，chemical decomposition 化学分解，matrix decomposition 矩阵分解，task decomposition 任务分解。',
 'the decomposition of leaves；matrix decomposition；task decomposition。',
 '生物腐解只是一个分支；数学分解不意味着数值烂掉。化学分解产物也不必等于原来制造时用过的每样原料。',
 ('The fallen leaves are at different stages of decomposition.','落叶处于不同的分解阶段。'),('The diagram shows a decomposition of the task into smaller steps.','图中展示了把任务分解成较小步骤的方式。'))
R('B4220','放在一起形成整体，及反向拆分','COMPOSITION：看部分怎样组成、安排成一个整体','compose 动作 → composer 人、composition 过程与结构 → compositional 性质；decompose/decomposition 分开。',
 '音乐、作文、绘画、材料的对象不同，部分成整体的核心相通。词形对应帮助理解，历史上 compose 与 composition 却经过不同借入路线。',
 'com- + pōnere → compōnere / composit-；法语 composer → compose；compositiō → composition；接 -er、-al，前接 de-。',
 [['创作、作者与整体结构','compose · composer · composition · compositional'],['拆分动作与过程','decompose · decomposition']],
 'composition 不只作文；compose yourself 是定神；组合性还看结构，不是无序相加；decomposition 不全是腐烂。',
 'The composer discussed the composition of the piece before the class tried its decomposition into short phrases.\n\n作曲家先讲解乐曲结构，随后全班尝试把它拆成短乐句。','compose composer composition compositional decompose decomposition')
G=[['希腊生育、产生一组词根 → 科学构词 -gen','生成、引起者；可命名物质或来源'],['不同名词各有固定对象','pathogen 致病者；allergen 引发过敏的物质；fibrinogen 形成纤维蛋白的前体'],['历史命名不等于永恒定义','oxygen 酸生成者保留旧命名假设；-gen 不在每词里都直接指 gene 基因']]
W('fibrinogen','/faɪˈbrɪnədʒən/，中间也可保留 /əʊ/、/oʊ/','纤维蛋白原，参与凝血的一种血浆蛋白',
 '血凝块里的纤维蛋白像形成网的材料，fibrinogen 是能够转成它的前体。中文的原也在提醒你：还没转成最终的 fibrin。',
 'fibrin 纤维蛋白 + 连接元音 -o- + -gen 生成、来源相关成分。名字指可形成纤维蛋白的前体蛋白，不是 gene 基因直接塞在末尾。',G[:1]+[['fibrin + -o- + -gen → fibrinogen','与形成纤维蛋白相关的前体名称'],['凝血过程中的具体对应','纤维蛋白原转为纤维蛋白']],
 'plasma fibrinogen 血浆纤维蛋白原，a fibrinogen test 纤维蛋白原检测，fibrinogen levels 纤维蛋白原水平。',
 'plasma fibrinogen；a fibrinogen test；fibrinogen levels。',
 'fibrinogen 前体与 fibrin 形成后的纤维蛋白分开；词尾解释名称关系，不能单凭名字推出某个检测值的具体含义。',
 ('The diagram shows fibrinogen being converted into fibrin.','图中展示纤维蛋白原转变为纤维蛋白。'),('The report lists the fibrinogen level in the sample.','报告列出了样本中的纤维蛋白原水平。'),sources=['https://en.wiktionary.org/wiki/fibrinogen#English','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/fibrinogen','https://www.merriam-webster.com/dictionary/fibrinogen'])
W('hallucinogen','英 /həˈluːsɪnədʒən/；美 /həˈluːsənədʒən/，也有其他重音形式','致幻物质、致幻剂',
 '重点不是一种幻觉本身，而是能引发幻觉、改变感知的那类物质。-gen 把引发者和产生的现象分开。',
 'hallucination 幻觉的 hallucin- 词干 + 连接元音 -o- + -gen 引起者。不是把完整 hallucination 后不作变化地再接 ogen。',G[:1]+[['hallucination 的词干 + -o- + -gen → hallucinogen','能够诱发幻觉的物质名称']],
 'a hallucinogen 致幻物质，the effects of hallucinogens 致幻物质的作用，research on hallucinogens 关于致幻物质的研究。',
 'a hallucinogen；the effects of hallucinogens。',
 'hallucination 是感知经验，hallucinogen 是可能引发它的物质；hallucinogenic 是相关性质形容词。名字不表示它只会产生一种完全相同的体验。',
 ('The chapter explains how a hallucinogen can alter perception.','这一章解释致幻物质如何改变感知。'),('The glossary distinguishes a hallucinogen from a hallucination.','词汇表区分了致幻物质和幻觉。'),sources=['https://en.wiktionary.org/wiki/hallucinogen#English','https://www.merriam-webster.com/dictionary/hallucinogen'])
R('A1999','生成、引起者，以及带有历史认识的科学命名','-GEN：产生或引发什么，看前半与具体物质','pathogen 致病，allergen 致敏，carcinogen 致癌，mutagen 致突变；fibrinogen 是可形成纤维蛋白的前体。',
 '词尾搭桥，前半指定对象，但科学名称不是把物质的所有作用一次说完。oxygen 的产酸者命名还保留过时认识，不能反过来用词源证明所有酸含氧。',
 '希腊生成相关成分 → -gen；前接词干，常有连接 -o-；各词也可能经法语等科学命名路线进入英语。',
 [['引起某现象的物质或来源','pathogen · allergen · carcinogen · mutagen · hallucinogen'],['生理作用与蛋白前体','estrogen · androgen · fibrinogen'],['保留旧理论的元素名','oxygen']],
 '-gen 不等于所有词中直接是基因；fibrinogen 不是已经形成的 fibrin；oxygen 名称里的旧假设不作现代定义。',
 'The glossary explains the different naming patterns in pathogen, hallucinogen and fibrinogen.\n\n词汇表解释了 pathogen、hallucinogen 和 fibrinogen 的不同命名方式。','pathogen allergen carcinogen mutagen hallucinogen estrogen androgen fibrinogen oxygen')
if __name__=='__main__':save('continuation_20261030_iv',ROOTS,WORDS)
