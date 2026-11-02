"""Translation across fields, seeds, racial descriptors, hiring and chemistry."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['拉丁 trāns- + ferre 的不规则分词路线 → trānslātus','带到另一边，转移'],['拉丁 trānslātiō → 法语、英语 translation','转移；翻译及各领域相应过程'],['translation + -al → translational','与相应转移、翻译过程有关的']]
W('translational','/trænzˈleɪʃənəl/','翻译的；平移的；科研转化的；生物学翻译过程的',
 '共同抓住从一处、一个表达体系转到另一处。具体转什么，要看语言、运动、科研还是生物学语境。',
 'translation + -al，形成相关形容词。translation 接拉丁 trānslātiō；trānslāt- 中 lāt- 来自 ferre 带的不规则分词路线，不是晚 late。',T,
 'translational choices 翻译选择；translational motion 平移运动；translational research 把发现推进到实际应用的研究；translational control 蛋白质合成中翻译环节的调控。',
 'translational research；translational motion；translational control。',
 '科研转化不是把论文译成别国语言。纯平移强调物体不随之转向，不把所有轨迹都限定为直线；生物学翻译是按 mRNA 信息组装氨基酸链，也不是人类语言。',
 ('The centre supports translational research that connects laboratory findings with practical use.','该中心支持把实验室发现与实际应用连接起来的转化研究。'),('The model separates translational motion from rotation.','模型把平移运动和转动分开分析。'),sources=['https://en.wiktionary.org/wiki/translational#English','https://ncats.nih.gov/about/about-translational-science','https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/aircraft-translations/','https://www.genome.gov/genetics-glossary/Translation'])
R('B2517','转移、翻译，以及各领域的相关性质','TRANSLATION：带过去；具体带的是内容、位置还是研究成果','translation → translational；mis- + translation → mistranslation。',
 '词源给一条转移的线，专业语境再决定转移对象。研究成果落到应用，不等于把一篇外语论文翻译出来。',
 'trāns- + ferre / lātus → trānslātiō → translation；接 -al，或前接 mis-。',
 [['过程及相关性质','translation · translational'],['翻译出错','mistranslation']],
 'translational research 不是普通笔译研究；mistranslation 指误译，不只是任何不喜欢的译文。',
 'The translation explains what translational research means.\n\n这份译文解释了转化研究是什么意思。','translation translational mistranslation')
S=[['古英语 sēd/sǣd → 中古英语 seed → seed','播下去的东西，种子'],['实体与比喻的生长起点','种子 → 起初的想法、资金、条件'],['固定扩展和构词','比赛分散安排强手 → 种子选手；seed 接各类词尾、植物名称']]
W('seed','/siːd/','种子；开端、萌芽；种子选手；播种、设定初始条件',
 '一粒小东西种下，后面长出一大片。这个起点的画面可讲植物，也可讲想法、创业资金和程序的起始条件。',
 '接古英语 sēd、sǣd，远源与 sow 播种同族。体育种子义联系把强手分散放进签表，避免过早相遇；不是说选手年幼。',S,
 'plant seeds 播种，the seeds of doubt 怀疑的萌芽，seed funding 启动资金，the top seed 头号种子选手，a random seed 伪随机生成器的起始值。',
 'plant seeds；the seeds of doubt；seed funding；the top seed；a random seed。',
 'seed 作动词可给土地播种，菜谱里又可指去籽，要看对象。程序的 seed 决定相应生成过程的起点，不是让结果必然真正随机。',
 ('We planted the seeds in small pots.','我们把种子种进小花盆。'),('Her question planted the seeds of doubt in his mind.','她的问题在他心里埋下了怀疑的种子。'),('The top seed reached the final.','头号种子选手进入了决赛。'),sources=['https://en.wiktionary.org/wiki/seed#English','https://www.etymonline.com/word/seed'])
W('seedy','/ˈsiːdi/','破旧寒酸的；不体面的、名声不好的；多籽的',
 '读到 a seedy hotel，通常是在说看起来破旧、让人不太放心的旅馆，不是旅馆里撒满了种子。',
 'seed + -y，本可表示多籽。破败义可能借植物结籽、过了盛放期的画面发展，具体语义连接不说成绝无疑问的唯一故事。',S[:1]+[['seed + -y → seedy','多籽的'],['可能借过了盛放期的植物作比喻','贫困、失去光鲜 → 寒酸、破败、名声不佳']],
 'a seedy hotel 破旧而不体面的旅馆，a seedy bar 名声不佳的酒吧，look seedy 看起来邋遢或气色差。字面多籽义仍可存在。',
 'a seedy hotel；a seedy bar；look seedy。',
 'seedy 常带负面观感，不等于看到某地旧就已证明那里违法；seedless 和 seedy 的字面种子义可相对，不能拿来反推道德好坏。',
 ('They stayed in a seedy hotel near the station.','他们住在车站附近一家破旧而不体面的旅馆。'),('The film begins in a seedy bar on the edge of town.','电影从城边一家名声不佳的酒吧开场。'))
W('seedling','/ˈsiːdlɪŋ/','幼苗，尤指由种子长出的苗',
 '种子已经发芽，长成小小的一株，还远没到成熟植物的样子；这就是 seedling。',
 'seed + -ling，-ling 在此给幼小的个体命名。由种子长出的苗是核心用法，也可较宽泛地指待移栽幼苗。',S[:1]+[['seed + -ling → seedling','从种子长出的幼小植株']],
 'tomato seedlings 番茄幼苗，young seedlings 小苗，transplant seedlings 移栽幼苗。',
 'tomato seedlings；young seedlings；transplant seedlings。',
 'seed 是种子，seedling 已经是长出的植株；sapling 通常是年轻树木，不能无差别用于所有蔬菜小苗。',
 ('Tiny seedlings appeared a week later.','一周后冒出了细小的幼苗。'),('Each seedling was labelled with the date it was planted.','每株幼苗都标上了种植日期。'))
W('flaxseed','/ˈflæksiːd/，也读 /ˈflæksˌsiːd/','亚麻籽',
 '前半交代是哪种植物，后半交代它的种子：flax 亚麻 + seed，合起来就是亚麻籽。',
 'flax 接古英语 fleax 这一亚麻植物名，和 seed 组成复合词。连读时两个相邻 /s/ 常合成较长或单个 /s/。',
 [['古英语 fleax → flax','亚麻植物，可提供纤维与种子'],['flax + seed → flaxseed','亚麻的种子']],
 'flaxseed oil 亚麻籽油，ground flaxseed 磨碎的亚麻籽，a bag of flaxseed 一袋亚麻籽。linseed 也是这类种子的常见名称。',
 'flaxseed oil；ground flaxseed；a bag of flaxseed。',
 'flaxseed 指种子，不是把亚麻布磨成籽。linen 联系亚麻纤维制品；flaxseed、linseed 常对应同类种子，具体产品用途看标签。',
 ('The label lists ground flaxseed as an ingredient.','标签把磨碎的亚麻籽列为一种配料。'),('The exhibit shows both flax fibres and flaxseed.','展览同时展示了亚麻纤维和亚麻籽。'))
W('seedless','/ˈsiːdləs/','无籽的，没有明显种子的',
 '吃葡萄时不用反复吐硬籽，商品就可能标 seedless。它讲的是种子这一项特征，不是没有果肉或没有繁殖方式。',
 'seed + -less，无、没有。常见水果用法也涵盖没有明显成熟硬籽，不能拿标签要求每个果实绝不存在任何微小种子痕迹。',S[:1]+[['seed + -less → seedless','没有种子或没有明显硬籽的']],
 'seedless grapes 无籽葡萄，a seedless watermelon 无籽西瓜，seedless varieties 无籽品种。',
 'seedless grapes；a seedless watermelon；seedless varieties。',
 'seedless 是性质，seeded 在菜谱里可能是去过籽，也可能表示有籽、播过种，须看场景；词形不能替你选定同一个方向。',
 ('The shop sells both seeded and seedless grapes.','店里既卖有籽葡萄，也卖无籽葡萄。'),('The description identifies it as a seedless variety.','说明把它标为无籽品种。'))
R('B3511','播下生长的起点，及种子相关性质、幼苗和作物名','SEED：小小起点，后面长出东西','seed → seedling / seedless / seedy；flaxseed、rapeseed、oilseed 看前半的植物或用途。',
 '实体词最容易带出画面：种子成为苗，资金和疑问也能先有一个萌芽。但 seedy 的破败义已经走到负面比喻，不能逐字猜成有前途。',
 'sēd/sǣd → seed；接 -ling、-less、-y；flax/rape/oil + seed。',
 [['种子、幼苗和性质','seed · seedling · seedless · seedy'],['植物与用途组合','flaxseed · rapeseed · oilseed']],
 'seedling 不是种子本身；seedless 不表示所有组织都无任何种子痕迹；seedy 常用义是寒酸破败。',
 'The seed grew into a seedling, while the bag was labelled flaxseed.\n\n种子长成了幼苗，袋上则标着亚麻籽。','seed seedling seedless seedy flaxseed rapeseed oilseed')
C=[['法语 race、意大利语 razza → 英语 race 的群体义','血统、群体等；更远词源不确定'],['race + -ial → racial','与种族、相应社会分类有关'],['相关前后缀扩展','racially 副词；bi-/inter-/multi- 指涉及数量或关系']]
W('racially','/ˈreɪʃəli/','在种族方面；涉及种族地',
 'diverse 是多样，再加 racially，就说清多样性指种族背景这一方面，而不是年龄、职业或兴趣。',
 'racial + -ly，性质形容词变为限定方面或方式的副词。前面的 race 是群体分类义，和赛跑那条来源分开。',C,
 'racially diverse 种族背景多样的，racially mixed 种族背景混合的，racially motivated 出于种族因素的。',
 'racially diverse；racially mixed；racially motivated。',
 'racially 说明讨论的维度，本身不等于 racist 带歧视的；具体褒贬来自后接内容和整句。',
 ('The school serves a racially diverse community.','这所学校服务于种族背景多样的社区。'),('The report examines whether the incident was racially motivated.','报告调查这一事件是否出于种族因素。'))
W('biracial','/ˌbaɪˈreɪʃəl/','有两种种族背景的；涉及两个种族群体的',
 'bi- 给的是二，racial 给的是种族背景这个维度。常用来描述个人的家庭背景，也可描述涉及两个群体的情况。',
 'bi- 二 + racial。表示两种背景或两个群体，不是说一个人必定被划成可精确量出的两半。',C[:2]+[['bi- + racial → biracial','两种种族背景的、两个群体相关的']],
 'a biracial family 有两种种族背景的家庭，biracial identity 双种族背景身份认同，a biracial character 有两种种族背景的角色。',
 'a biracial family；biracial identity；a biracial character。',
 'biracial 常侧重两种背景，multiracial 更宽；interracial 常说不同群体之间的关系或互动。标签含义还受语境、自我认同影响。',
 ('The novel follows a biracial teenager growing up in a small town.','小说描写一位有两种种族背景的少年在小镇成长的经历。'),('She writes about biracial identity in her essays.','她在随笔中讨论双种族背景的身份认同。'))
R('B4138','种族维度、背景数量与群体之间的关系','RACIAL：先定讨论维度，再看前后缀','racial → racially；bi- 两种、multi- 多种、inter- 群体之间。',
 '把词形对应到一个清楚的问题：讨论哪方面、个人有哪些背景，还是群体之间怎样互动。不要把所有词都一口气背成种族歧视。',
 'race 的群体义 + -ial；racial + -ly；bi-/inter-/multi- + racial。',
 [['性质与方面','racial · racially'],['背景与群体关系','biracial · multiracial · interracial']],
 'racial 不自动等于 racist；biracial 的二不要求用百分比描述一个人的身份。',
 'The exhibition explores biracial identity in a racially diverse city.\n\n展览探讨一座种族背景多样的城市中的双种族背景身份认同。','racial racially biracial multiracial interracial')
H=[['古英语 hȳr、hȳrian → hire','为服务或使用付钱；雇用、租用'],['英语现代用法','雇人、租器具；新雇来的员工也可叫 a hire']]
W('hire','英 /ˈhaɪə/；美 /haɪr/','雇用；租用；雇来的人；租用状态',
 '不是把东西永远买下，而是付钱获得一段时间的服务或使用。人可以 hire，英式英语里车和器材也常 hire。',
 '接古英语 hȳr 工钱、雇用关系与 hȳrian 雇用。人和器物有不同现代搭配，不把每次 hire 都译成招长期员工。',H,
 'hire a designer 雇设计师，hire a car 租车〔英式常见〕，a new hire 新员工，for hire 可供租用、可受雇。美式租车通常说 rent a car。',
 'hire a designer；hire a car；a new hire；for hire。',
 'hire 常侧重取得服务或开始雇用；employ 可描述持续雇用关系。hire out 表把自己的物品、服务租出去，要分清谁提供谁使用。',
 ('The studio plans to hire two designers.','工作室计划雇两名设计师。'),('We hired a car for the weekend.','我们租了一辆车过周末。'))
W('rehire','英 /ˌriːˈhaɪə/；美 /ˌriːˈhaɪr/','重新雇用；重新雇回的人',
 '这个人以前在这里做过，离开后又雇回来。re- 强调同一雇用关系重新开始，不只是公司又招了一个陌生人。',
 're- 再次 + hire 雇用。名词 a rehire 可指被重新雇回的前员工。',H+[['re- + hire → rehire','重新雇用；被重新雇回的人']],
 'rehire a former employee 重新雇用前员工，eligible for rehire 符合再次受雇条件，a recent rehire 最近重新雇回的员工。',
 'rehire a former employee；eligible for rehire；a recent rehire。',
 'rehire 说明重新雇用，不保证岗位、薪资和合同条款都与从前一样；renew a contract 续约也不必先经历离职。',
 ('The company decided to rehire a former editor.','公司决定重新雇用一名前编辑。'),('Several of the new team members are rehires.','新加入团队的几个人都是重新雇回的员工。'))
R('B3944','付钱取得服务、使用，及重新雇用','HIRE：用付费换来服务或暂时使用','hire → rehire；人、器物搭配不同，租出去又要看 hire out。',
 '雇设计师、租车都可涉及 hire，关键是付钱取得服务或使用。re- 再把时间拉到以前雇过、现在又开始。',
 'hȳr / hȳrian → hire；re- + hire。',
 [['雇用、租用与重新雇用','hire · rehire']],
 'hire 不等于永久买断；rehire 不是随便又招一个新人。',
 'The studio will rehire the designer it hired last year.\n\n工作室会重新雇用去年请过的那位设计师。','hire rehire')
K=[['希腊炼金术名称 → 阿拉伯 al-kīmiyāʔ → 欧洲拉丁、法语形式','炼金术；更远的希腊名称来源有争议'],['alchimista 等缩减 → chimista / chimiste → chemist','炼金术实践者，后来也指化学家'],['chemist + -ry → chemistry','早期也说炼金术，后来形成现代化学学科义；人与人契合的比喻也很早']]
W('chemistry','/ˈkemɪstri/','化学；物质的化学性质与变化；人与人之间的吸引、默契',
 '学科上问东西由什么组成、为什么这样反应；说两个人有 chemistry，则像在说他们碰到一起自然有反应、很合拍。',
 'chemist + -ry，词尾可表示相关实践或领域。chemist 经法语、拉丁词形联系 alchemy 炼金术名称；更远的希腊名称来源有争议，不硬定成唯一的倒液体或埃及黑土地故事。',K,
 'study chemistry 学化学，organic chemistry 有机化学，the chemistry of water 水的化学性质与相关反应，screen chemistry 银幕上的默契或吸引。ch 读 /k/。',
 'study chemistry；organic chemistry；the chemistry of water；screen chemistry。',
 'chemical 是相关形容词或化学物质名词，chemistry 是学科、性质或默契。人与人的 chemistry 不保证一定发展成恋爱；比喻义也不必编成现代实验室之后才有。',
 ('She studies chemistry at university.','她在大学学化学。'),('The two actors have great chemistry on screen.','两位演员在银幕上很有默契。'),sources=['https://en.wiktionary.org/wiki/chemistry#English','https://www.etymonline.com/word/chemistry','https://www.etymonline.com/word/alchemy'])
R('B3152','物质组成与变化的学问，及相应研究分支','CHEMISTRY：看东西由什么组成、怎样相互作用','chemistry 前加 bio-/geo-/electro-/stereo-，限定生命、地球、电或空间结构相关领域。',
 '前半先告诉你从哪个角度研究化学。人的 chemistry 是相处时的反应和默契，另看语境即可，不把人当实验药剂。',
 '炼金术名称 → chemist → chemist + -ry；现代各学科前缀 + chemistry。',
 [['基本学科及研究角度','chemistry · biochemistry · geochemistry · electrochemistry · stereochemistry']],
 'chemist 人，chemical 相关性质或物质，chemistry 学科或默契；远源不确定的部分保留不确定。',
 'Her chemistry course includes an introduction to biochemistry.\n\n她的化学课程包含生物化学入门。','chemistry biochemistry geochemistry electrochemistry stereochemistry')
if __name__=='__main__':save('continuation_20261030_ij',ROOTS,WORDS)
