"""Launch, revolution and the process of bringing something inside."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
L=[['拉丁 lancea、lanceāre → 古法语 lancher、lancier → 中古英语 launchen → launch','矛、投掷 → 使突然向前、投出'],['现代动作与启动分支','下水、发射 → 推出产品、开展活动'],['船名 launch 的另一路','葡萄牙语 lancha 等 → launch，较远常联系马来语相应船名']]
W('launch','英 /lɔːntʃ/；美 /lɔːntʃ/ 或 /lɑːntʃ/','发射、使下水；推出、开展；发布活动；汽艇〔另名词来源〕',
 '把原来准备着的东西送出去开始运行：船下水、火箭升空、产品上市都能串起来。a motor launch 那种艇名则有另一条借词路径。',
 '启动动词经法语接投矛、投出的词族，从向前送出扩展到开始。船名经葡萄牙语 lancha 等，常联系马来语 lancharan，不把所有 launch 都当发射动词直接名词化。',L,
 'launch a rocket 发射火箭，launch a product 推出产品，launch an investigation 开展调查，a product launch 产品发布，a motor launch 汽艇。',
 'launch a product；launch an investigation；a product launch；launch into。',
 'launch 强调正式开始、送出去，release 可释放、发行，用法有重叠；船名另源，launch into a speech 是开始滔滔讲话。',
 ('The company launched a new service.','公司推出了一项新服务。'),('The book launch attracted many readers.','新书发布活动吸引了许多读者。'),('A small motor launch carried us across the harbour.','一艘小汽艇载我们穿过港口。'),
 sources=['https://en.wiktionary.org/wiki/launch#English','https://www.etymonline.com/word/launch'])
W('launcher','英 /ˈlɔːntʃə/；美 /ˈlɔːntʃər/ 或 /ˈlɑːntʃər/','发射装置；启动器、应用启动工具',
 '帮某样东西开始运行、送出去的工具。软件里点图标开应用的 launcher，不必和火箭装置长一样。',
 'launch + -er，先可指执行启动的人，后来常指器具、软件工具；-er 不只人物。',L[:2]+[['launch + -er → launcher','执行发射、启动的人或工具']],
 'an app launcher 应用启动器，a game launcher 游戏启动器，a rocket launcher 火箭发射装置。',
 'an app launcher；a game launcher；a rocket launcher。',
 'launcher 帮你启动，launch 是动作或一次发布；软件 launcher 不一定是应用本身的全部功能。',
 ('The app launcher organizes the programs into groups.','应用启动器把程序分组整理。'),('The museum displayed an old launcher.','博物馆展出了一套旧发射装置。'))
W('relaunch','英 /ˌriːˈlɔːntʃ/；美 /ˌriːˈlɔːntʃ/ 或 /ˌriːˈlɑːntʃ/','重新推出、重新启动；重新发布活动',
 '东西曾经推出过，修改后再正式放到公众面前；不是只给它换个名字就一定完成改进。',
 're- 再 + launch，形成再次启动动词，也可名词说重新发布。',L[:2]+[['re- + launch → relaunch','再次下水、启动、推出；再发布']],
 'relaunch a website 重新推出网站，a magazine relaunch 杂志改版重发，relaunch the service 重新推出服务。',
 'relaunch a website；relaunch the service；a magazine relaunch。',
 'relaunch 强调再次正式推出，restart 可机器、进程重新开动；两者能重叠，但网站改版发布不一定只一次程序重启。',
 ('They relaunched the website with a simpler design.','他们用更简洁的设计重新推出网站。'),('The relaunch introduced the magazine to a new audience.','重新发布让杂志接触到一批新读者。'))
R('B3279','向外送出、正式开始与重新启动','LAUNCH：从准备状态送出去，让一项活动真正开始','launch → launcher；relaunch 再次推出。基础词另辨船名的葡萄牙语、马来语背景。',
 '发射、下水、产品发布有送出开始的画面；汽艇名称不是任何船能 launch 就都自动叫 launch。',
 'lancea、lanceāre 经法语 → 动词 launch；launch + -er；re- + launch；船名另经 lancha 等。',
 [['动作、工具与再次启动','launch · launcher · relaunch']],
 'launch/release 发射推出与释放发行；launcher 工具；relaunch/restart 正式重推与重新开动；船名另源。',
 'The new launcher was introduced at the product relaunch.\n\n新启动器在产品重新发布时推出。','launch launcher relaunch')
RV=[['拉丁 re- + volvere → revolvere → revolūtiō','向回、再次 + 滚动 → 转回、循环'],['法语 revolucion、拉丁名词等 → 英语 revolution','转动、天体循环 → 局势巨变、革命'],['现代引申','制度彻底变化；技术、生活方式的重大变革']]
W('revolution','/ˌrevəˈluːʃən/','转动一周、公转；革命、重大变革',
 '一个物体转一圈回到相应位置，是 revolution；社会秩序、技术体系发生翻天覆地的变化，也沿状态翻转的旧背景叫 revolution。',
 '经法语或拉丁 revolūtiō 接 revolvere，re- 回、再 + volvere 滚动。英语早期有天体循环、转动义，后来政治、社会变化义扩展，不是只为现代革命活动才造出来。',RV,
 'one revolution 一圈，revolutions per minute 每分钟转数，a political revolution 政治革命，a technological revolution 技术革命。',
 'one revolution；revolutions per minute；a political revolution；a technological revolution。',
 'revolution 一周、巨变，revolt 起义、反抗更侧重行动；evolution 演变通常强调发展变化，不能只当少一个 r 的同义词。',
 ('The wheel makes one revolution every two seconds.','轮子每两秒转一圈。'),('The invention brought a revolution in communication.','这项发明带来了通信领域的重大变革。'),
 sources=['https://en.wiktionary.org/wiki/revolution#English','https://www.etymonline.com/word/revolution'])
W('revolutionary','英 /ˌrevəˈluːʃənəri/；美 /ˌrevəˈluːʃəneri/','革命的；带来重大变革的；革命者',
 '可以是参与政治革命的人、事，也可以是让旧做法彻底变样的新方法。revolutionary design 常在赞设计大幅突破，不必涉及推翻政府。',
 'revolution + -ary，与法语 révolutionnaire 等相应形式相关；形容词又可用于人物名词。不同场景不能只按一种政治意义包办。',RV[:2]+[['revolution + -ary → revolutionary','与革命有关、变革性的；再指革命者']],
 'a revolutionary movement 革命运动，a revolutionary idea 突破性想法，a revolutionary 革命者。',
 'a revolutionary idea；a revolutionary design；a revolutionary movement。',
 'revolutionary 不等于 reactionary 反动、主张恢复旧秩序的；日常宣传的变革性也不自动证明实际效果。',
 ('The engineer proposed a revolutionary design.','工程师提出了一个突破性设计。'),('The book follows the life of a young revolutionary.','书中讲述了一位年轻革命者的一生。'))
W('revolutionize','/ˌrevəˈluːʃənaɪz/','彻底改变、使发生革命性变化',
 '不只是修补细节，而是把原来的做法、可能性大幅翻新；有时宣传中也用得很夸张。',
 'revolution + -ize，动词使发生重大变革。英式也见 revolutionise，本页同词说明，不另设重复词头。',RV[:2]+[['revolution + -ize → revolutionize','使制度、技术、做法等彻底改变']],
 'revolutionize transport 彻底改变交通，revolutionize the way we work 彻底改变工作方式，revolutionize an industry 改造某行业。',
 'revolutionize transport；revolutionize the way；revolutionize an industry。',
 'revolutionize 强调巨大变化，improve 改善可以很小；一个细节优化不必夸成颠覆全行业。',
 ('The railway revolutionized travel between the cities.','铁路彻底改变了城市间的出行方式。'),('The new method could revolutionize the way the team processes data.','新方法可能彻底改变团队处理数据的方式。'))
R('B4181','转一圈与社会、技术的重大翻转','REVOLUTION：滚回、转一周，后来也说旧格局被彻底改变','revolution → revolutionary、revolutionize，分变化、性质人物、使发生巨变。',
 '机械转数不谈政治，革命性设计也不一定政治革命。revolutionise 是同词英式拼写，不为尾字母再拆新词族。',
 're- + volvere → revolvere → revolūtiō，经法语等 → revolution；revolution + -ary/-ize。',
 [['循环、巨变与派生','revolution · revolutionary · revolutionize']],
 'revolution/evolution/revolt 不同；revolutionary 非 reactionary；revolutionize 比 improve 强，但宣传语不等于实证。',
 'The technological revolution introduced revolutionary methods.\n\n技术变革带来了突破性方法。','revolution revolutionary revolutionize')
ROOTS[-1]['exclude']['revolutionise']='revolutionize 的常见英式拼写，词义、构词与主体相同，已在同条说明。'
I=[['拉丁 internus、internālis → internal','内部的、在里面的'],['internal 的现代派生','内部进行；让外在规则、观念成为内在的一部分']]
W('internally','英 /ɪnˈtɜːnəli/；美 /ɪnˈtɜːrnəli/','在内部、在体内；在内心',
 '公司内部先讨论，是 internally；外面平静，心里很紧张，也可以用它把镜头转到里面。',
 'internal + -ly，副词接身体、组织、心中等不同内部范围，不把每次内部都当一个器官。',I+[['internal + -ly → internally','在相应范围里面']],
 'discuss internally 内部讨论，developed internally 内部开发，internally consistent 内部一致，internally anxious 内心焦虑。',
 'discuss internally；developed internally；internally consistent。',
 'internally 在内部，internationally 在国际上；两词很长也不能只扫开头 in、尾部 ly 就混读。',
 ('The team discussed the problem internally first.','团队先在内部讨论了问题。'),('The system was developed internally.','系统由内部团队开发。'))
W('internalize','英 /ɪnˈtɜːnəlaɪz/；美 /ɪnˈtɜːrnəlaɪz/','内化、使成为内在认识；把情绪等往心里收',
 '原来是别人提醒你的规则，后来不用提醒也自然按它想、按它做，就内化了；也可说把批评、情绪收进心里。',
 'internal + -ize，使进入内部、成为内在的一部分。英式也见 internalise；具体是学习规则还是把情绪往心里吞，要看对象。',I[:1]+[['internal + -ize → internalize','使外在内容成为内部认识、反应的一部分']],
 'internalize a rule 内化规则，internalize a lesson 真正吸收教训，internalize criticism 把批评往心里收。',
 'internalize a rule；internalize a lesson；internalize criticism。',
 'internalize 常不止 memorize 记住，还涉及变成习惯、理解；internalize criticism 也不一定表示批评真实正确。',
 ('With practice, she internalized the basic rules.','通过练习，她把基本规则变成了自然习惯。'),('He tended to internalize every criticism.','他总倾向于把每句批评都往心里收。'))
W('internalization','英 /ɪnˌtɜːnəlaɪˈzeɪʃən/','内化、内化过程',
 '把外部的规则、观念吸收成自己的一部分，这个逐渐发生的过程叫 internalization。',
 'internal + -ization，或对应 internalize 的动作名词，形成过程、结果名称。不要把内化直接理解成把一件实物搬进内脏。',I[:1]+[['internal + -ization → internalization','从外在信息到内在观念、习惯的过程']],
 'the internalization of norms 规范内化，internalization of rules 规则内化，a process of internalization 内化过程。',
 'the internalization of；internalization of rules；a process of internalization。',
 'internalization 内化过程，internalize 是动作，internally 是内部地；了解一条规则不保证已经把它变成自然习惯。',
 ('The chapter discusses the internalization of social norms.','这一章讨论社会规范的内化。'),('Repeated practice supported the internalization of the rules.','反复练习帮助规则逐渐内化。'))
R('B2907','内部进行与把外在内容变成内在认识','INTERNAL：边界里面；学习时也可说规则进入习惯','internal → internally；internalize → internalization，动作与过程相邻。',
 '公司内部、身体内部、内心是不同范围，语义核心都向里。内化不等于仅背会文字，也不保证外界批评一定正确。',
 'internus、internālis → internal；internal + -ly/-ize/-ization。',
 [['内部性质与方式','internal · internally'],['内化动作与过程','internalize · internalization']],
 'internally/internationally 内部与国际；internalize/memorize 内化与记忆；internalization 非物理吞入。',
 'Practice helped the students internalize the rules.\n\n练习帮助学生把规则变成内在习惯。','internal internally internalize internalization')
if __name__=='__main__':save('continuation_20261030_ee',ROOTS,WORDS)
