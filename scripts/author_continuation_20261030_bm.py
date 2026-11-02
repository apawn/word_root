"""Guide, sick and ill: direction, physical states and everyday figurative uses."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
GU=[['古法语 guier、guider 等 → 中古英语 guiden → guide','带路、引导；更远通常接日耳曼指路词'],['现代 guide','向导；指南；带领、指导；引导判断']]
def G(f,m):return GU+[[f,m]]
W('guide','/ɡaɪd/','向导；指南；带领、指引、指导',
 '你不熟路，有个人或一份说明帮你知道下一步往哪儿走、怎么做。',
 '经中古英语、法语相关形式，通常再接日耳曼指路词。gu- 在这里读 /ɡ/，中间 ui 不按每个字母单独拼读；名动词都围绕带路。',GU,
 'a tour guide 导游，a guide to grammar 语法指南，guide someone through 逐步带人做，be guided by evidence 由证据引导判断。',
 'a tour guide；a guide to；guide someone through；be guided by。',
 'guide 可带领、给方向，force 强迫行为；a guide to something 中 to 常是介词，后接主题或活动名称。',
 ('Our guide showed us the old part of the city.','导游带我们看了城市老区。'),('The teacher guided us through the first exercise.','老师一步步带我们做第一道练习。'),sources=['https://www.etymonline.com/word/guide','https://en.wiktionary.org/wiki/guide#English'])
W('guidance','/ˈɡaɪdəns/','指导；指引；导航、制导〔特定领域〕',
 '不是替你把所有事做完，而是帮你判断方向、下一步；也可指设备对路线的引导。',
 'guide 去 e + -ance，形成引导活动、过程名词。历史是英语动词与相应名词后缀的组合，不是 guidance 里多出独立 dance。',G('guide + -ance → guidance','指导、引导的过程和帮助'),
 'under someone’s guidance 在某人指导下，seek guidance 寻求指点，career guidance 职业指导。通常不可数。',
 'under the guidance of；seek guidance；career guidance。',
 'guidance 通常整体指导帮助，a guideline 是一条准则；需要几条具体建议可用 guidelines 或 pieces of advice，不随意说 three guidances。',
 ('She completed the project under her tutor’s guidance.','她在导师指导下完成了项目。'),('We asked for guidance on how to proceed.','我们就下一步怎么做寻求指导。'))
W('guideline','/ˈɡaɪdlaɪn/','指导原则；行动准则；参照线',
 '先画一条线，让后面的行动有个参照；抽象里就是大体照着走的原则。',
 'guide + line，早期可指切割等操作前画出的参照线，后来用于抽象指导原则。别只从现代原则义猜成古代法律条文。',G('guide + line → guideline','引导操作的线 → 指导原则、行动准则'),
 'follow the guidelines 按指导准则做，clear guidelines 清楚准则，guidelines for writing 写作指南。',
 'follow the guidelines；clear guidelines；guidelines for。',
 'guideline 常指导性原则，rule 可明确规则；具体文件可能有强制效力，不能仅凭叫 guideline 就断言可以随便不遵守。',
 ('The editor gave us clear guidelines for the article.','编辑给了我们清楚的文章写作准则。'),('Use the pencil mark as a guideline when cutting.','切割时，把铅笔记号作为参照线。'))
R('B3605','带路、指方向与逐步帮助；指南、指导、准则','GUIDE：有人或说明帮你知道往哪儿、怎么做','guide → guidance → guideline；人物与文档、整体帮助与具体准则按角色连读，偏专门 waveguide 暂略。',
 '法语带路词借入，后来既用于旅行，也用于学习、判断和操作。guideline 的实体线与抽象原则都有实际用法。',
 'guide + -ance；guide + line；guide 的 gu- 读 /ɡ/。',
 [['引导者、帮助和参照原则','guide · guidance · guideline']],
 'guidance 通常不可数，a guideline 可一条；guide to 后 to 常介词；文件效力不能只由名字 guideline 判断。',
 'The guide offered guidance and explained the guidelines.\n\n向导提供指点，并解释了相关准则。',
 'guide guidance guideline')
SI=[['古英语 sēoc → 中古英语 sik、sike → sick','患病、不适'],['现代 sick','生病；恶心、厌烦；有病的贬称及很棒的俚语等分支']]
def S(f,m):return SI+[[f,m]]
W('sick','/sɪk/','生病的；恶心、想吐的；厌烦的；很棒的〔俚语〕',
 '身体不舒服是中心，胃里想吐也是常见；受够某件事可以说 sick of，年轻人口语还可能反过来夸太酷。',
 '继承古英语 sēoc。心理厌烦、贬评和赞叹俚语分别发展，现代不能把每个 sick 都按一种病译。',SI,
 'a sick child 生病孩子，feel sick 感到不适、恶心，be sick of delays 厌烦延误，That trick was sick! 那个动作太酷了〔口语〕。',
 'a sick child；feel sick；be sick of；call in sick。',
 '英式 be sick 常可呕吐，美式 be sick 更常泛指生病；具体仍看上下文。sick of 是受够，不是对某东西患医学疾病。',
 ('She called in sick this morning.','她今天早上打电话请了病假。'),('I’m sick of waiting for an answer.','我受够了等一个答复。'))
W('sickness','/ˈsɪknəs/','疾病、不适；恶心、呕吐感',
 '把生病、胃里翻腾的状态当一个名词来说；不是每次都某一种具体病名。',
 'sick + -ness，古英语 sēocness 等形式已存在。不同地区、搭配中可泛病，也可特别指恶心。',SI+[['古英语 sēocness → sickness','患病状态；现代也可恶心']],
 'absence due to sickness 因病缺席，travel sickness 晕车、晕交通工具，a feeling of sickness 恶心感。',
 'absence due to sickness；travel sickness；a feeling of sickness。',
 'sickness 可泛病或恶心，illness 通常泛疾病、不健康状态；具体搭配 travel sickness 不机械换成 travel illness。',
 ('Several staff members were absent due to sickness.','几名员工因病缺席。'),('She sometimes experiences travel sickness on long journeys.','长途旅行时，她有时会晕车。'))
W('sickly','/ˈsɪkli/','体弱多病的；病态、苍白的；甜腻得令人不适的',
 '看着虚弱、没精神；味道过甜，甜到让人胃里不舒服，也可以 sickly。',
 'sick + 形容词 -ly，中古英语已有相关形式，也有其他旧同族影响的分析。这里常作形容词，不是所有 -ly 都是副词。',S('sick + -ly → sickly','易病、病态；令人不适的味道、颜色等'),
 'a sickly child 体弱孩子，a sickly smile 病态、虚弱的笑，a sickly sweet smell 甜腻气味。',
 'a sickly child；a sickly smile；sickly sweet。',
 'sick 当前病或不适，sickly 更容易说长期体弱、病态外观；sickly sweet 甜腻，不是甜食自己生病。',
 ('He was a sickly child but became stronger as he grew.','他小时候体弱，长大后强壮了些。'),('A sickly sweet smell filled the room.','房间里弥漫着甜腻得让人不舒服的气味。'))
W('sicken','/ˈsɪkən/','使恶心、厌恶；使生病、变得不适',
 '食物或气味让胃里不舒服，残忍举动也能让人心里反胃；是引起不适或厌恶的动作。',
 'sick + -en，中古英语已有 sekenen 等同族形式。可及物使人不适，也可说某人逐渐生病，现代厌恶义很常见。',S('sick + -en → sicken','使变成 sick；引起身体不适或厌恶'),
 'be sickened by 因……恶心、厌恶，The smell sickened me. 气味让我作呕。',
 'be sickened by；the smell sickened；sicken at the thought。',
 'sicken 动作使不适、使厌恶，sickness 状态名词；be sickened by cruelty 常是道德厌恶，不必真的感染疾病。',
 ('The smell of the rubbish sickened me.','垃圾气味让我作呕。'),('She was sickened by the cruelty in the story.','故事里的残忍行为让她深感厌恶。'))
W('sicko','英 /ˈsɪkəʊ/；美 /ˈsɪkoʊ/','变态、恶心的人〔侮辱称呼〕',
 '骂别人趣味、行为扭曲得令人恶心；这不是对普通生病者的中性称呼。',
 'sick 的病态、扭曲评价义 + 人物后缀 -o。整个词带侮辱、贬低语气，不是疾病分类名称。',S('sick + -o → sicko','病态、扭曲的人这一贬称'),
 'call someone a sicko 骂某人变态；影视对白中常带强烈厌恶，不宜当普通 sick person 的缩略。',
 'call someone a sicko；a twisted sicko；the word sicko。',
 'sick person 生病的人，sicko 侮辱行为、趣味扭曲的人；换一个后缀，语气和指向差很大。',
 ('The character calls the villain a sicko.','角色骂反派是个变态。'),('She objected when he used the insult sicko.','他用 sicko 这个侮辱词时，她表示反对。'))
R('B3389','疾病与恶心；厌烦、体弱和贬称分场景','SICK：身体不适；也可胃里反感、心里受够','sick → sickness、sickly、sicken、sicko；已有 homesick、lovesick、seasick 共享，分别想家、苦恋与晕船。',
 '先抓身体不适，再看厌恶、俚语夸赞等固定现代用法，不把想家当具体传染病。',
 'sick + -ness/-ly/-en/-o；home/love/sea + sick，部分词有名词逆构历史。',
 [['基本状态、性质和变化','sick · sickness · sickly · sicken'],['固定组合和侮辱称呼','homesick · lovesick · seasick · sicko']],
 'sick of 厌烦；英式 be sick 可呕吐；sickly sweet 甜腻；sicko 贬称不等于普通病人。',
 'The sickly sweet smell sickened the traveller, who was already seasick.\n\n甜腻的气味让本已晕船的旅客更恶心了。',
 'sick sickness sickly sicken homesick lovesick seasick sicko')
IL=[['古诺尔斯语 illr、illa 等 → 中古英语 ille → ill','坏、恶、不好；更远来源有争议'],['现代 ill','生病的；恶意、不良的；不好地、艰难地等副词用法']]
W('ill','/ɪl/','生病的；不良、恶意的；不好地〔副词〕；弊病〔名词复数〕',
 '今天最常见身体状态不好；旧的坏还留在 ill will 恶意、speak ill of 说坏话等。',
 '借北欧 illr 等坏、不好词，后来病义突出。更远来源不确定，ill 也不是把 illness 截短的现代新缩写。',IL,
 'be seriously ill 病重，ill health 健康不佳，ill will 恶意，speak ill of 说坏话，can ill afford 实在承受不起。',
 'seriously ill；ill health；ill will；speak ill of；can ill afford。',
 'ill 生病常见于表语，sick 更常直接放名词前如 a sick child；这是常见用法倾向，不是 ill 绝不修饰名词。ill 的副词也不只说生病。',
 ('He was too ill to attend the meeting.','他病得没法参加会议。'),('She bears him no ill will.','她对他没有恶意。'),sources=['https://www.etymonline.com/word/ill','https://en.wiktionary.org/wiki/ill#English'])
W('illness','/ˈɪlnəs/','疾病；生病、不健康状态',
 '把身体出了问题的状态，或一段具体疾病经历作为名词来说。',
 'ill + -ness，取 ill 的生病义形成性质、状态名词。可不可数谈健康状态，也可数指某种或某次疾病。',IL+[['ill + -ness → illness','生病状态；具体疾病、患病经历']],
 'a serious illness 严重疾病，recover from an illness 从疾病中恢复，absence due to illness 因病缺席。',
 'a serious illness；recover from illness；due to illness。',
 'illness 常健康问题、患病经历，disease 更常具体病种、病理概念；许多语境重合，不必把二者写成完全隔开的两类。',
 ('She returned to work after a long illness.','长期患病后，她回去工作了。'),('The trip was cancelled because of illness.','旅行因有人生病而取消。'))
R('B3865','坏、不好到身体不适；疾病、恶意和副词保留','ILL：身体不好是常用义，旧坏义仍在固定搭配里','ill → illness；含连字符组合按要求先略，ill will、speak ill of 放基础词讲常用旧义保留。',
 '来自北欧坏、不好词，远源不强定。别把所有 ill 都当生病，副词和恶意名词搭配尤其要看对象。',
 'ill + -ness；ill health、ill will、speak ill of、can ill afford 等固定搭配。',
 [['状态、旧坏义与疾病名词','ill · illness']],
 'ill 常表语但并非绝不前置；ill will 恶意不指一种病；illness/disease 常有重合而着眼不同。',
 'Though he was ill, he spoke with no ill will towards anyone.\n\n他虽然病着，说话却不对任何人带恶意。',
 'ill illness')
if __name__=='__main__':save('continuation_20261030_bm',ROOTS,WORDS)
