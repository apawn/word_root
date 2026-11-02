"""Common abstract plurals: feeling/thought, choices, values and properties."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2857':dict(words=['feeling','feelings'],label='feel → feeling → feelings：感受与情绪',note='feeling 由感知过程发展为可数感受、情绪；feelings 常说感情感受。'),
 'B2745':dict(words=['thought','thoughts'],label='think／thought → thoughts：一个个念头',note='thought 名词和动词过去形式都有古老历史；thoughts 是名词复数。'),
 'B2521':dict(words=['skill','skills'],label='skill → skills：能分辨，再能熟练做好',note='古诺尔斯语辨别、理解的词族发展出实践能力。'),
 'C0446':dict(words=['effort','efforts'],label='effort → efforts：投入力量与多次尝试',note='强壮、有力量的词族，与使劲、付出努力相连。'),
 'C0154':dict(words=['decision','decisions'],label='decide／decision → decisions：作出一个个取舍',note='切断、了结的画面关联下判断；decision 本身经法语借入。'),
 'C0906':dict(words=['option','options'],label='option → options：摆在面前的选择',note='option 接拉丁 optio，英语 opt 出现较后；这里不倒置历史。'),
 'C1090':dict(words=['policy','policies'],label='policy → policies：方针与保险单的两条来源',note='治理方针与证明文书分别演化，最终拼成同一个英语词。'),
 'C1602':dict(words=['value','values'],label='value → values：数值、价值观与珍视',note='值得、有力量的早期词族，后有价值名词及估价、珍视动词。'),
 'B2974':dict(words=['interest','interests'],label='interest → interests：兴趣、利益与牵涉其中',note='与自己相关、影响自己，能帮助区分关注的兴趣与涉及的利益。'),
 'C1135':dict(words=['property','properties'],label='property → properties：特有属性与拥有的资产',note='自己的、特有的这一核心分向属性与所有物。'),
 'B3894':dict(words=['matter','matters'],label='matter → matters：事情与事情要紧',note='材料、内容词族发展到讨论的事；动词进一步说有重要性。'),
 'C0682':dict(words=['letter','letters'],label='letter → letters：字母、书信与学问',note='拉丁 littera 的复数早已能说书信、文献，英语承接了相连的分支。'),
}
W('feelings','/ˈfiːlɪŋz/','感受；情绪；感情；感觉〔feeling 的复数〕',
 '把一个人心里实际体验到的情绪、感受放在一起，就是 feelings；被一句话伤到，也是在说这些内心感受。',
 'feel + -ing → feeling，再加 -s → feelings。feel 接古英语 fēlan 的感知词族；名词 feeling 可说感知、情绪，复数词尾在 /ŋ/ 后读 /z/。',
 [['古英语感知词族 → feel → feeling','感知 → 感觉、感受、情绪'],['feeling + -s → feelings','多种感受；内心感情']],
 'hurt someone’s feelings 伤害某人的感情；mixed feelings 五味杂陈、心情复杂；feelings about the change 对变化的感受；have feelings for someone 对某人有感情。',
 'express your feelings；talk about your feelings。','feelings 多说主观感受；thoughts 多说脑中的想法，两者会互相影响。mixed feelings 常表示既高兴、期待，又担心、不舍等感受同时存在。',
 ('She had mixed feelings about leaving her hometown.','要离开家乡，她心里五味杂陈。'),('I did not realize that my joke had hurt his feelings.','我没意识到那个玩笑伤害了他的感情。'),sources=['https://en.wiktionary.org/wiki/feelings#English','https://en.wiktionary.org/wiki/feeling#English'])
W('thoughts','英 /θɔːts/；美 /θɔːts, θɑːts/','想法；念头；思绪；意见〔thought 的复数〕',
 '脑子里冒出的一个个念头，或针对一件事整理出的想法，就是 thoughts。',
 'thought 名词加 -s，/t/ 后读 /s/。名词接古英语 þoht、geþoht，think 的过去式另有 þohte 等形式，两者同族而各有历史；thoughts 本身是名词复数。',
 [['古英语 þoht、geþoht → thought 名词','思考、念头'],['thought + -s → thoughts','一个个想法；思绪、意见']],
 'share your thoughts 分享想法；lost in thought 陷入沉思〔单数固定用法〕；second thoughts 再考虑、犹豫；gather your thoughts 理清思绪。',
 'my thoughts on the proposal；write down your thoughts。','thoughts on something 常是对某事的意见；thoughts of home 常说想起家。have second thoughts 表示重新考虑、开始犹豫，未必已经改变决定。',
 ('Write down your thoughts before the meeting.','开会前先把你的想法写下来。'),('She paused for a moment to gather her thoughts.','她停了一会儿，理了理思绪。'),sources=['https://en.wiktionary.org/wiki/thoughts#English','https://en.wiktionary.org/wiki/thought#English'])
W('skills','/skɪlz/','技能；本领；技巧〔skill 的复数〕',
 '知道怎么做，并且经过练习能把它做好，这一项项本领就是 skills。',
 'skill + -s，/l/ 后读 /z/。skill 经中古英语接古诺尔斯语 skil 辨别、理解，关联 skilja 分开、辨认；从能判断发展到熟练做事的能力。',
 [['古诺尔斯语 skil、skilja → 中古英语 → skill','区分、判断、理解 → 实践能力'],['skill + -s → skills','不同方面的熟练本领']],
 'communication skills 沟通能力；practical skills 实用技能；learn new skills 学新本领；improve your skills 提高技能。',
 'basic cooking skills；skills developed through practice。','skill 可说整体熟练程度，如 with great skill；skills 常指可分开的能力，如 reading and writing skills。knowledge 侧重知道的内容，skills 侧重能做成什么。',
 ('The course helps students develop practical cooking skills.','这门课帮助学生掌握实用的烹饪技能。'),('Her communication skills made the group work easier.','她的沟通能力让小组合作更顺利。'),sources=['https://en.wiktionary.org/wiki/skills#English','https://en.wiktionary.org/wiki/skill#English'])
W('efforts','英 /ˈefəts/；美 /ˈefərts/','努力；付出的心力；多次尝试〔effort 的复数〕',
 '为把事情做成而一次次使劲、想办法，这些付出就是 efforts。它既能指实际行动，也能把一个人投入的心力合起来说。',
 'effort + -s，/t/ 后读 /s/。effort 经法语接古法语 esforz、esforcier，通常追到重建的通俗拉丁 *exfortiāre，关联 ex- 与 fortis 强壮、有力。',
 [['拉丁 fortis；重建 *exfortiāre → 古法语相关形式 → effort','力量 → 使劲、付出努力'],['effort + -s → efforts','多次尝试；一系列付出']],
 'make efforts to improve 努力改进；despite our efforts 尽管我们作了努力；joint efforts 共同努力；efforts to find the answer 寻找答案的努力。',
 'all her efforts；recognize someone’s efforts。','effort 作不可数时可说费力程度，如 with little effort；efforts 常把多次行动或一段时间的付出作为整体。一次有目标的尝试也常说 an effort。',
 ('Their efforts to repair the old boat finally paid off.','他们修理旧船的努力终于有了成果。'),('Thank you for all your efforts in organizing the event.','感谢你为组织这次活动付出的所有努力。'),sources=['https://en.wiktionary.org/wiki/efforts#English','https://en.wiktionary.org/wiki/effort#English'])
W('decisions','/dɪˈsɪʒənz/','决定；决策；判断结果〔decision 的复数〕',
 '几条路摆在眼前，最后把一种选定、不再悬着，这一个个定下来的结果就是 decisions。切断犹豫是理解词源的形象线索。',
 'decision + -s，/n/ 后读 /z/。decision 经法语接拉丁 dēcīsiō，来自 dēcīdere 切断、了结、裁定；其中 de- 与 caedere 切、砍的词族相连，复合形式见 -cid-、-cis-。',
 [['拉丁切断词族 → dēcīdere、dēcīsiō → 法语 → decision','切断、了结 → 作判断、决定'],['decision + -s → decisions','多个决定、判断结果']],
 'make decisions 作决定；difficult decisions 艰难的决定；decisions about the future 关于未来的决定；review past decisions 回顾过去的决策。',
 'informed decisions；decisions made together。','decide 是作决定的动作，decision 是决定这一名词，英语中还可用 make a decision。decision 的 -sion 接在较早拉丁名词历史里，不能简单理解成英语 decide 后来临时改出的词。',
 ('We made the important decisions together.','重要决定都是我们一起作的。'),('Small daily decisions can shape a person’s habits.','每天的小决定能够塑造一个人的习惯。'),sources=['https://en.wiktionary.org/wiki/decisions#English','https://en.wiktionary.org/wiki/decision#English'])
W('options','英 /ˈɒpʃənz/；美 /ˈɑːpʃənz/','选项；可选办法；选择权；期权〔特定语境〕',
 '眼前有几条可以走的路，这些可以选的路就是 options；有资格在约定条件下选择某件事，也可以说拥有某种 option。',
 'option + -s，/n/ 后读 /z/。option 经法语接拉丁 optiō 选择、选择权，与 optāre 选择、希望同族；英语 option 早于 opt，不能倒说成 opt 首先派生出所有 option 用法。',
 [['拉丁 optāre、optiō → 法语 option → 英语 option','选择、希望 → 选择权、可选方案'],['option + -s → options','多个选项；特定的选择权']],
 'explore the options 考虑各种办法；menu options 菜单选项；keep your options open 保留选择余地；stock options 股票期权。',
 'several options available；choose between two options。','options 指可选的项目、路径，decision 指最后作出的取舍。金融语境的 options 是有特定约定条件的权利，普通界面的 options 通常只需理解为选项。',
 ('The menu gives you three options for dessert.','菜单上有三种甜点可选。'),('We decided to keep our options open until Friday.','我们决定到周五前先保留各种选择。'),sources=['https://en.wiktionary.org/wiki/options#English','https://en.wiktionary.org/wiki/option#English'])
W('policies','英 /ˈpɒləsiz/；美 /ˈpɑːləsiz/','政策；方针、办事原则；保险单〔复数〕',
 '一个组织定下“这类事以后怎样处理”的规则，就是一条条 policies；保险语境里，它则常指一份份保险合同文件。两种意思有不同来路。',
 'policy 的辅音加 y 结尾变为 -ies → policies。方针义经法语 policie、拉丁 polītīa 接希腊 politeía 治理；保险单义经法语 police、意大利语 polizza、中世纪拉丁 apodissa，接希腊 apódeixis 证明。',
 [['希腊 politeía → 拉丁、法语相关形式 → policy','治理 → 方针、政策'],['希腊 apódeixis → 中世纪拉丁、意大利语、法语 → policy','证明文书 → 保险单'],['policy 变 y 为 ies → policies','多条方针；多份保险单']],
 'school policies 学校规章方针；return policies 退货政策；environmental policies 环境政策；insurance policies 保险单。',
 'review the policies；policies on attendance。','policy 是处理一类事务时采用的方针，politics 多说政治活动、权力关系等。insurance policies 中按保险文件理解，不从“治理城邦”强行推导。',
 ('The school explained its attendance policies to the parents.','学校向家长说明了出勤方面的规定。'),('She kept the insurance policies in a labelled folder.','她把保险单放在一个贴好标签的文件夹里。'),sources=['https://en.wiktionary.org/wiki/policies#English','https://en.wiktionary.org/wiki/policy#English'])
W('values','/ˈvæljuːz/','数值、价值〔复数〕；价值观；珍视、重视；估价',
 '把东西看成值得多少，是 value 的价格、数值分支；一个人心里认为什么值得坚持，这些原则就是 values；动词 values 则说他很重视某事。',
 'value + -s，元音后读 /z/。名词经古法语 value、valoir 接拉丁 valēre 有力量、值得；动词既有名词转用分析，也有关联法语 valuer 的借入影响。',
 [['拉丁 valēre → 法语 valoir、value／valuer → 英语 value','有力量、有用、值得 → 价值、估价'],['value + -s → values','多个数值；价值观；单数主语珍视']],
 'family values 家庭方面的价值观；numerical values 数值；property values 房产价值；values your opinion 重视你的意见。',
 'shared values；enter the missing values。','values 表示价值观时，是认为值得追求、遵守的原则；表示数字时要看表格、测量等语境。valuable 是有价值的，values 是名词复数或动词形式。',
 ('The two friends share many of the same values.','这两个朋友有许多相同的价值观。'),('She values the time she spends with her grandparents.','她很珍惜与祖父母相处的时间。'),sources=['https://en.wiktionary.org/wiki/values#English','https://en.wiktionary.org/wiki/value#English'])
W('interests','英 /ˈɪntrəsts/；美 /ˈɪntrəsts, ˈɪntərəsts/','兴趣爱好；利益；权益、业务关联；使感兴趣',
 '一件事让你愿意关注，是兴趣；一件事影响你能获得什么、保住什么，是利益。interests 经常在这两种“与自己有关”之间切换。',
 'interest + -s，/t/ 后读 /s/。interest 经法语接拉丁 interesse，字面 inter- 在之间与 esse 存在，实际早有相关、有影响、重要等义；权益、补偿及后来兴趣、利息等分支不能硬串成唯一简单直线。',
 [['拉丁 interesse → 法语、英语 interest','相关、有影响 → 权益；后来有兴趣、利息等分支'],['interest + -s → interests','多项兴趣、利益；单数主语使人感兴趣']],
 'common interests 共同兴趣；protect their interests 维护他们的利益；business interests 商业利益、业务权益；interests me 让我感兴趣。',
 'in the interests of safety；someone’s personal interests。','名词 interests 可以是爱好，也可以是利益，靠对象、上下文判断。借款的利息一般说不可数 interest，如 pay interest；普通学习场景不把付利息机械写成 pay interests。',
 ('Their shared interests include music and local history.','他们共同的兴趣包括音乐和地方历史。'),('The new arrangement protects the interests of both groups.','新的安排维护了两个群体的利益。'),sources=['https://en.wiktionary.org/wiki/interests#English','https://en.wiktionary.org/wiki/interest#English'])
W('properties','英 /ˈprɒpətiz/；美 /ˈprɑːpərtiz/','性质、属性；房产、地产〔复数〕',
 '一个东西自己带有的特点，是 properties；某个人拥有的一处处房产，也叫 properties。“自己的、特有的”是两条分支之间的联系。',
 'property 的辅音加 y 变 -ies → properties。property 经法语接拉丁 proprietās，来自 proprius 自己的、特有的；历史上整词借入，现代 proper + -ty 只是帮助对应的结构。',
 [['拉丁 proprius → proprietās → 法语 → property','自己的、特有的 → 所有物；特有性质'],['property 变 y 为 ies → properties','多种属性；多处房产']],
 'physical properties 物理性质；properties of a material 材料的性质；rental properties 出租房产；object properties 对象属性。',
 'compare their properties；two neighbouring properties。','property 表示财产总体时通常不可数，如 personal property；properties 可说一处处地产，也可说一项项性质。材料的 properties 说它本身有什么特点。',
 ('The two materials have very different physical properties.','这两种材料的物理性质很不一样。'),('A narrow path runs between the two properties.','两处地产之间有一条窄路穿过。'),sources=['https://en.wiktionary.org/wiki/properties#English','https://en.wiktionary.org/wiki/property#English'])
W('matters','英 /ˈmætəz/；美 /ˈmætərz/','事情、事项〔复数〕；要紧、有影响〔第三人称单数〕',
 '摆到面前需要处理的一件件事，是名词 matters；一句话说“这件事有分量、值得在意”，就是动词 matters。',
 'matter + -s，读 /z/。matter 经法语 matere、matiere 接拉丁 materia，早有材料、木材、内容等义；事情、问题的名词分支发展后，英语形成“要紧”的动词用法。',
 [['拉丁 materia → 法语相关形式 → 英语 matter','材料、内容 → 事情、问题等'],['matter + -s → matters','多件事情；单数主语具有重要性']],
 'personal matters 私事；practical matters 实际事务；what matters 要紧的是什么；make matters worse 使情况更糟。',
 'it matters to me；discuss several matters。','These matters are urgent 中是复数名词；Your opinion matters 中是动词。no matter what 是无论什么的结构；What is the matter? 常问怎么了。',
 ('We still have a few practical matters to discuss.','我们还有几个实际问题要讨论。'),('What matters most is that everyone gets home safely.','最要紧的是每个人都平安到家。'),sources=['https://en.wiktionary.org/wiki/matters#English','https://en.wiktionary.org/wiki/matter#English'])
W('letters','英 /ˈletəz/；美 /ˈletərz/','字母；书信；文学、学问〔特定表达〕',
 '写下来可辨认的一个个字母是 letters；用这些文字写成、寄给别人的一封封信，也叫 letters。这两种意思在早期来源中已经相连。',
 'letter + -s，读 /z/。letter 经古法语 letre 接拉丁 littera／litera；拉丁复数 litterae 已可指文字、书信、文献或学问，英语承接相关分支。',
 [['拉丁 littera／litterae → 古法语 letre → 英语 letter','字母；书信、文献等'],['letter + -s → letters','多个字母、多封信；文学学问相关用法']],
 'capital letters 大写字母；write letters 写信；letters of recommendation 推荐信；a person of letters 文学之士、学者。',
 'letters from home；spell it in clear letters。','letters 在拼写场景说字母，在邮寄、通信场景说书信。characters 范围更广，数字、汉字、标点也可叫字符；letter of the law 中 letter 常说条文的字面规定。',
 ('Please write your name in capital letters.','请用大写字母写下你的名字。'),('She kept all the letters her father had sent her.','她保存着父亲寄给她的所有信。'),sources=['https://en.wiktionary.org/wiki/letters#English','https://en.wiktionary.org/wiki/letter#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xl',ROOTS,WORDS)
 extend_lessons()
