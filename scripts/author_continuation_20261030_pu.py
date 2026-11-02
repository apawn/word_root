"""The roles, responsibilities, relationships and skills expressed by -ship."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def S(word,ipa,meaning,base,base_meaning,sense,explanation,usage,contrast,*examples,history=None,sources=None):
 assert base+'ship'==word
 W(word,ipa,meaning,sense,f'{base} + -ship。这里把{base_meaning}相关的身份、职责、技能或整体状态作为名词来谈；具体落点看用法。',history or [[base,base_meaning],[word,meaning]],explanation,usage,contrast,*examples,sources=sources)
S('premiership','英 /ˈpremiəʃɪp/；美 /prɪˈmɪrʃɪp/','总理职务、任期；某些体育顶级联赛或其冠军','premier','总理、首要的',
 'premier 是担任总理的人，premiership 是这份职位或任期。体育里还可用来命名某些顶级联赛、冠军，具体是哪一项要看上下文。',
 'during her premiership 是她任总理期间；不能只看 ship 就想到船。体育名称不要一律翻成某个固定国家的联赛。',
 'during someone’s premiership；win a premiership。',
 'premiership 是职务、任期或体育相关名称；premiere 是首演、首映，多一个末尾 e，重音也常不同。',
 ('The policy was introduced during her premiership.','这项政策在她任总理期间推出。'),('The club celebrated its first premiership.','俱乐部庆祝拿到首个联赛冠军。'),sources=['https://en.wiktionary.org/wiki/premiership#English','https://www.oxfordlearnersdictionaries.com/definition/english/premiership'])
Ap=[['拉丁 apprehendere → 法语 aprendre','抓住；在头脑中掌握、学习'],['法语 aprentiz 等 → 英语 apprentice','学习某门手艺、行业工作的人']]
W('apprentice','/əˈprentɪs/','学徒；使当学徒',
 '不是只坐着听理论，而是跟着有经验的人学一门手艺、一种工作，边做边学，这个人叫 apprentice。',
 '经法语学习者的相应形式进入英语，上接拉丁 apprehendere 抓住、掌握。先有学徒名词，英语又用作使当学徒的动词。',Ap,
 'an apprentice electrician 电工学徒；be apprenticed to someone 跟某人当学徒。',
 'an apprentice carpenter；be apprenticed to。',
 'apprentice 常有具体行业、师傅和实践训练；student 泛指学生，intern 常指实习生，不能仅凭都是新人就当成相同制度。',
 ('She began work as an apprentice electrician.','她从电工学徒做起。'),('He was apprenticed to a local carpenter.','他跟当地一位木匠当学徒。'),sources=['https://en.wiktionary.org/wiki/apprentice#English','https://www.etymonline.com/word/apprentice'])
S('apprenticeship','/əˈprentɪsʃɪp/','学徒期；学徒训练、学徒岗位','apprentice','学习行业技能的学徒',
 'apprentice 是学徒本人，apprenticeship 是跟着学、边做边练的那段训练安排或时期。',
 'serve an apprenticeship 是当一段时间学徒；complete an apprenticeship 是完成学徒训练。',
 'an apprenticeship in carpentry；complete an apprenticeship。',
 'apprenticeship 不是 scholarship 奖学金；一个说训练、身份，一个常说资助或学术研究。',
 ('She completed a three-year apprenticeship.','她完成了三年的学徒训练。'),('The workshop offers apprenticeships in furniture making.','这家工坊提供家具制作的学徒岗位。'),history=Ap+[['apprentice + -ship → apprenticeship','学徒身份、时期、训练安排']])
S('stewardship','英 /ˈstjuːədʃɪp/；美 /ˈstuːərdʃɪp/','受托管理；尽责照管','steward','替他人管理、照管的人',
 '资源交到你手上，不是让你随意耗尽，而是托你照管好、传下去；stewardship 常带着这种负责保管的意味。',
 '可以说机构、土地、自然资源的管理，重点常是受托与照管责任；不一定拥有这些东西。',
 'environmental stewardship；under someone’s stewardship。',
 'ownership 是所有权；stewardship 是管理照管的责任。管理得好的人不必就是所有者。',
 ('The garden flourished under her stewardship.','在她的照管下，花园生机勃勃。'),('The programme promotes responsible environmental stewardship.','这个项目倡导负责任地照管环境。'),history=[['古英语 stigweard 等 → steward','管理家务、庄园等事务的人'],['steward + -ship → stewardship','管理照管的职责、做法']],sources=['https://en.wiktionary.org/wiki/stewardship#English','https://www.etymonline.com/word/steward'])
S('craftsmanship','英 /ˈkrɑːftsmənʃɪp/；美 /ˈkræftsmənʃɪp/','手艺；精湛工艺；制作技艺','craftsman','工匠、有手艺的人',
 '桌子的接缝严丝合缝，雕花细致，细节能看出制作者的功夫；这份工艺水平就是 craftsmanship。',
 '常赞物品制作的技能、精细程度，也可比喻文章、电影等创作的娴熟技巧。',
 'fine craftsmanship；traditional craftsmanship。',
 'craftsmanship 常强调技艺和精细制作；craft 指手艺、工艺门类，也可说小型制作活动，不能每次直接互换。',
 ('The cabinet shows exceptional craftsmanship.','这个柜子体现了非凡的制作工艺。'),('The film combines strong storytelling with visual craftsmanship.','影片既会讲故事，视觉制作也很见功夫。'))
S('workmanship','英 /ˈwɜːkmənʃɪp/；美 /ˈwɜːrkmənʃɪp/','做工；制作质量','workman','做实际制作、施工等工作的人',
 '看看缝线齐不齐、瓷砖铺得平不平，评价的就是 workmanship：这件成品到底做得怎么样。',
 '常用来评价具体制作、施工质量，good、poor、shoddy 等可直接说明好坏。',
 'poor workmanship；the quality of workmanship。',
 'workmanship 可中性评价做工好坏；craftsmanship 常更容易突出精湛技艺，但两者也有重合。',
 ('Poor workmanship caused the frame to come apart.','做工差，框架散开了。'),('The price reflects the quality of the workmanship.','这个价格体现了做工的质量。'))
S('guardianship','英 /ˈɡɑːdiənʃɪp/；美 /ˈɡɑːrdiənʃɪp/','监护；监护身份、职责','guardian','监护人、保护者',
 'guardian 是承担照顾、保护职责的人，guardianship 是这份监护关系和责任。法律语境尤其不能只理解成偶尔帮忙看一下。',
 'under someone’s guardianship 在某人的监护下；legal guardianship 法律上的监护。不同地方的具体制度不靠词尾就能推定。',
 'legal guardianship；under the guardianship of。',
 'guardianship 是监护关系、职责；friendship 是友谊。感情亲近与具有监护身份不是一回事。',
 ('The document identifies the person responsible for guardianship.','文件说明了谁承担监护职责。'),('The child was placed under her aunt’s guardianship.','孩子被交由姨妈监护。'),sources=['https://en.wiktionary.org/wiki/guardianship#English','https://www.oxfordlearnersdictionaries.com/definition/english/guardianship'])
S('partisanship','英 /ˌpɑːtɪˈzænʃɪp/；美 /ˌpɑːrtɪˈzænʃɪp/','党派立场；偏袒己方、党派偏见','partisan','坚定支持某一方、党派的人',
 '先问是不是自己这一边，再决定支持还是反对，partisanship 常在说这种鲜明的站队、偏袒。',
 '政治中可指党派忠诚，也常批评党派偏见压过对事情本身的判断。',
 'political partisanship；put aside partisanship。',
 'partisanship 是党派、阵营取向；participation 是参与。看起来有相似字母，含义和词族不同。',
 ('The debate was dominated by bitter partisanship.','辩论被尖锐的党派对立主导了。'),('She asked the committee to put partisanship aside.','她请委员会暂且放下党派立场。'))
S('receivership','英 /rɪˈsiːvəʃɪp/；美 /rɪˈsiːvərʃɪp/','接管状态；由接管人管理','receiver','接管人〔这里用专业义〕',
 '公司陷入财务困境，由指定的 receiver 接手管理，处于这种状态就叫 in receivership。这里不是收到了一个包裹。',
 '词中 receiver 用的是接管人义，-ship 把这种管理身份、状态名词化；常见搭配是 go into receivership。',
 'in receivership；go into receivership。',
 'receiver 在不同场景还能指接收器、收件人；receivership 的常见商业法律义不能照搬这些日常义。',
 ('The company went into receivership after months of financial trouble.','经历数月财务困难后，公司进入接管状态。'),('The factory continued operating while it was in receivership.','工厂在接管期间继续运营。'),sources=['https://en.wiktionary.org/wiki/receivership#English','https://www.oxfordlearnersdictionaries.com/definition/english/receivership'])
S('professorship','英 /prəˈfesəʃɪp/；美 /prəˈfesərʃɪp/','教授职位、教授席位','professor','教授',
 'professor 是人，professorship 是这份教授职位；一个人可以申请、获得、担任这个职位。',
 'a professorship in physics 是物理学教授职位；an endowed professorship 是受捐资支持的教授席位。',
 'hold a professorship；a professorship in。',
 'professorship 是职位；profession 是职业、专业，不能因为都有 profess 就把所有职业叫教授职位。',
 ('She accepted a professorship in physics.','她接受了一个物理学教授职位。'),('He held the professorship for twelve years.','他担任这个教授职位十二年。'))
S('ridership','英 /ˈraɪdəʃɪp/；美 /ˈraɪdərʃɪp/','乘客群体；客运量、乘车人次','rider','乘车的人〔这里用交通义〕',
 '从一个 rider 乘客，换到整条线路有多少人坐、哪些人在坐，交通报告里常用 ridership。',
 '常指公共交通的乘客或乘坐总量；具体统计是人次、人数还是某时段平均值，要看报告口径。',
 'bus ridership；increase ridership。',
 'ridership 不自动等于独立人数：同一个人往返多次可能贡献多人次。别光凭中文乘客量就替数据定口径。',
 ('Bus ridership increased after fares were reduced.','降价后，公交客运量增加了。'),('The agency published monthly ridership figures.','机构公布了每月的乘车统计。'))
S('marksmanship','英 /ˈmɑːksmənʃɪp/；美 /ˈmɑːrksmənʃɪp/','射击技术；射术','marksman','善于射击的人',
 'marksman 是善射的人，marksmanship 是这份射击技术，常在体育比赛或训练评价里出现。',
 'mark 在这个词族里联系目标、标记，man 在旧构词里表示人，-ship 把它转成技能名词。',
 'excellent marksmanship；a test of marksmanship。',
 'marksmanship 是射击能力，不是 craftsmanship 一般工艺；都谈技能，但对象不同。',
 ('The competition tested accuracy and marksmanship.','比赛考验准确性和射击技术。'),('The coach praised her consistent marksmanship.','教练赞扬她稳定的射术。'))
S('showmanship','英 /ˈʃəʊmənʃɪp/；美 /ˈʃoʊmənʃɪp/','表演技巧；吸引观众的本领','showman','善于向观众展示、表演的人',
 '不仅会做，还知道怎样让观众愿意看、看得兴奋，这份带动气氛、呈现效果的本领叫 showmanship。',
 '可以赞舞台魅力，也可以批评只顾场面、缺乏内容；褒贬取决于它和什么对照。',
 'a flair for showmanship；a display of showmanship。',
 'showmanship 是呈现、吸引观众的能力；technical skill 是技术能力。有人两样都强，也有人只有场面。',
 ('The concert combined musicianship with dazzling showmanship.','音乐会把音乐功底和夺目的表演技巧结合起来。'),('The launch had plenty of showmanship but little substance.','这场发布会场面十足，实质内容却很少。'))
S('horsemanship','英 /ˈhɔːsmənʃɪp/；美 /ˈhɔːrsmənʃɪp/','骑术；驾驭、照管马的技能','horseman','骑马、熟悉马的人',
 '不只是坐在马背上，而是懂怎样与马配合、驾驭它，谈这份技术就会用 horsemanship。',
 '常见于骑马教学、马术活动；用 -ship 把相关人的本领作为名词。',
 'good horsemanship；horsemanship skills。',
 'horsemanship 是技能，horseback riding 是骑马这项活动；参加活动不自动等于已经具备高超技术。',
 ('The course teaches basic horsemanship.','课程教授基本骑术。'),('Her calm horsemanship impressed the instructor.','她沉稳的驭马技巧让教练印象深刻。'))
Ck=[['希腊 klerikos → 晚期拉丁 clericus','教士、教会人员；也与有学识者相关'],['古英语 clerc → 现代 clerk','由识字、记录工作的联系发展出文书、职员等义']]
W('clerk','英 /klɑːk/；美 /klɜːrk/','文书、办事员；店员；做文书工作',
 '办理登记、整理文件、在柜台处理事务的人可以叫 clerk；美式还常说商店店员。工作的具体范围靠前面的修饰词决定。',
 '经古英语 clerc 接晚期拉丁 clericus，历史与教士、识字者相联，再走向记录、文书工作。不是 clear 清楚去掉尾部变出来的。',Ck,
 'a hotel clerk 酒店前台职员；a court clerk 法院书记员、文书人员；a store clerk 店员〔常见美式〕。',
 'a desk clerk；a store clerk。',
 'clerk 的典型英式 /klɑːk/ 与美式 /klɜːrk/ 差异较大；clarify 澄清是另一个词，不能只凭辅音像就混起来。',
 ('The clerk checked our reservation.','前台职员核对了我们的预订。'),('She worked as a store clerk during the summer.','暑假里她做过商店店员。'))
S('clerkship','英 /ˈklɑːkʃɪp/；美 /ˈklɜːrkʃɪp/','文书、助理等职位或任期；临床实习阶段〔医学教育〕','clerk','文书、职员等〔具体角色随专业变化〕',
 'clerkship 可以是担任某种 clerk 的职位、时期；法律里常见法官助理岗位，医学教育里则可说临床实习阶段。',
 '不要只看 clerk 店员就把 medical clerkship 译成商店工作。这个词随专业保留不同角色与培训用法。',
 'a judicial clerkship；a clinical clerkship。',
 'clerkship 的具体岗位、训练安排要看专业和地区；internship 泛指实习，两词不能在所有制度里无差别替换。',
 ('She applied for a judicial clerkship.','她申请了一个法官助理岗位。'),('Students discussed their experiences during the clinical clerkship.','学生们讨论了临床实习阶段的经历。'))
S('seamanship','/ˈsiːmənʃɪp/','航海技能；船舶操纵、管理本领','seaman','海员',
 '懂海上情况、会配合操船，不只是人在船上，而是能把船与航行事务应付好，这份本领叫 seamanship。',
 'sea + man 构成 seaman，再加 -ship 说相关技能；这里的 ship 是技能词尾，不能因为整词谈航海就只译成海员的船。',
 'good seamanship；practical seamanship。',
 'seamanship 说航海本领，a seaman 说人；词尾 -ship 与独立词 ship 船在这里不是同一个构词来源。',
 ('The voyage tested the crew’s seamanship.','这次航行考验了船员的航海技能。'),('The training combines navigation with practical seamanship.','训练把导航与实用航海技能结合起来。'))
S('judgeship','/ˈdʒʌdʒʃɪp/','法官职位、任期','judge','法官〔这里用职位义〕',
 'judge 可以是法官，judgeship 是这份职位。谈任命、空缺、任期，而不是在讨论某次判断对不对。',
 '保留 judge 后再加 -ship；不是 judgment 判断、判决的另一种随意拼法。',
 'a vacant judgeship；an appointment to a judgeship。',
 'judgeship 是职务，judgment 是判断、裁决；一个讲位置，一个讲作出的判断。',
 ('She was appointed to a judgeship.','她获任法官职位。'),('The article discusses the vacant judgeship.','文章讨论了那个空缺的法官职位。'))
S('statesmanship','/ˈsteɪtsmənʃɪp/','政治家才能；治国、处理公共事务的能力','statesman','政治家',
 '不只赢下一次争论，还能把长远利益、不同群体与困难选择放在一起处理好，称赞这种政治才能时常用 statesmanship。',
 'statesman 加 -ship，说相关才能、行为；state 在这里是国家、政治事务，不是动词陈述。',
 'a display of statesmanship；an act of statesmanship。',
 'statesmanship 通常带政治判断力、领导才能的赞许；politics 是政治活动本身，不保证做得高明。',
 ('The agreement was praised as an act of statesmanship.','这份协议被称赞为政治家远见的体现。'),('The crisis demanded patience and statesmanship.','危机需要耐心和处理公共事务的智慧。'))
S('trusteeship','/trʌˈstiːʃɪp/','受托人职责、职位；托管','trustee','受托管理财产、机构事务等的人',
 '东西、事务交给 trustee 受托管理，trusteeship 是这份职务、责任或托管安排；重点是替他人、为指定目的管理。',
 'trustee + -ship；trustee 自身与 trust 信托、信任相联。具体权利义务要看制度，词尾本身只帮助认出身份、职责。',
 'accept a trusteeship；under trusteeship。',
 'trustworthiness 是值得信赖的品质；trusteeship 是受托人的职责、职位。人很可靠不自动说明已经被正式委任。',
 ('She accepted a trusteeship at the museum.','她接受了博物馆受托管理人的职务。'),('The report reviews the responsibilities of trusteeship.','报告梳理了受托管理的职责。'),sources=['https://en.wiktionary.org/wiki/trusteeship#English','https://www.oxfordlearnersdictionaries.com/definition/english/trusteeship'])
W('salesman','/ˈseɪlzmən/','男销售员；推销员',
 '负责把产品介绍给客户、促成销售的人。salesman 通常指男性；不强调性别时可以用 salesperson。',
 'sales 销售 + man 人、男人 → salesman；中间 s 属 sales 这一材料，不另造一个 sale-sm 词根。',
 [['sales + man','从事销售的人'],['salesman → salesmanship','销售员；相关销售技巧']],
 'a car salesman 汽车销售员；a travelling salesman 旅行推销员。复数 salesmen，读 /ˈseɪlzmən/，常与单数弱读听起来相同。',
 'a car salesman；an experienced salesman。',
 'salesman 说人，salesmanship 说本领；salesperson 是不强调性别的常用对应，不是销售技巧。',
 ('The salesman explained the differences between the two models.','销售员解释了两款型号的区别。'),('He worked as a car salesman for several years.','他做过几年汽车销售员。'))
S('salesmanship','/ˈseɪlzmənʃɪp/','销售技巧；推销本领','salesman','销售员',
 '懂产品还不够，还要知道怎样说明价值、听懂需求，让顾客愿意买，这份本领叫 salesmanship。',
 '常用来谈销售能力，也可比喻把一个想法推介给别人的本领；不只指职业头衔。',
 'good salesmanship；a display of salesmanship。',
 'salesmanship 是销售技巧，sales 是销售活动或销售额；成交多寡还受产品、价格等影响，不能把两者当同一个量。',
 ('Good salesmanship begins with listening to customers.','好的销售技巧从倾听顾客开始。'),('The presentation showed more salesmanship than technical depth.','这次展示的推销技巧比技术深度更突出。'))
S('traineeship','/ˌtreɪˈniːʃɪp/','培训岗位；受训期、培训安排','trainee','正在接受岗位等训练的人',
 'trainee 是受训的人，traineeship 是提供训练的岗位、项目或那段受训期。',
 'trainee + -ship；trainee 中的 -ee 在这里指接受训练的人。不同项目的期限、是否带薪不靠这个词就能判断。',
 'a traineeship in finance；complete a traineeship。',
 'traineeship 泛说受训安排；apprenticeship 常有具体行业技能的学徒模式。实际项目名称仍按机构使用来理解。',
 ('She secured a traineeship in digital design.','她获得了一个数字设计培训岗位。'),('The traineeship includes practical work and classroom sessions.','这个培训项目包括实践工作和课堂学习。'))
R('A1830','身份、职责、关系、状态、技能；也可指相关群体','-SHIP：把人所处的位置、关系或本领拿出来谈','friend 朋友 → friendship 友谊；apprentice 学徒 → apprenticeship 学徒训练；craftsman 工匠 → craftsmanship 手艺。先看基础词，再判断具体是哪一面。',
 '这个词尾不是船。最直观的是从人转向他所处的关系、担的职责、会的本领：professor 是教授，professorship 是职位；showman 是会表演的人，showmanship 是呈现给观众的技巧。membership、ridership 等还可能说整体成员或乘客量。',
 '来自古英语 -scipe、-scip，中古英语 -schipe 等日耳曼语材料，历史与形成、创造的词族相关；与 ship 船的独立词源不同。现代常直接接名词，形成角色、关系、技能等名词。-manship 常可进一步看见 man + -ship，但也有类推使用；并不要求今天使用这类技能的人必须是男性。worship 历史与值得、尊重的材料相联，landscape 的 -scape 则经荷兰语有关形式进入，不把字面相似当成现代直接加 ship。',
 [['训练身份与岗位','apprentice · apprenticeship · trainee · traineeship · clerk · clerkship'],['职责、职位与照管','premier · premiership · professor · professorship · guardian · guardianship · trustee · trusteeship · judge · judgeship · steward · stewardship'],['制作、销售与呈现技巧','craftsman · craftsmanship · workman · workmanship · salesman · salesmanship · showman · showmanship'],['射击、骑马与航海本领','marksman · marksmanship · horseman · horsemanship · seaman · seamanship'],['政治立场、公共事务和接管状态','partisan · partisanship · statesman · statesmanship · receiver · receivership'],['个人转为群体、数量视角','rider · ridership · member · membership']],
 'ownership 是所有权，stewardship 是照管责任；workmanship 评价做工，craftsmanship 常突出技艺；ridership 的统计口径要读报告；scholarship 的奖学金、学术研究等义不能全用身份代替。',
 'Her apprenticeship developed the craftsmanship that later became the workshop’s strength.\n\n学徒训练磨炼了她的手艺，后来成了工坊的优势。',
 'premier premiership apprentice apprenticeship steward stewardship craftsman craftsmanship workman workmanship guardian guardianship partisan partisanship receiver receivership professor professorship rider ridership marksman marksmanship showman showmanship horseman horsemanship clerk clerkship seaman seamanship judge judgeship statesman statesmanship trustee trusteeship salesman salesmanship trainee traineeship member membership relationship leadership championship partnership ownership friendship worship scholarship citizenship township fellowship censorship sponsorship dictatorship internship entrepreneurship hardship dealership companionship courtship authorship kinship viewership readership chairmanship governorship mentorship kingship homeownership musicianship editorship directorship bipartisanship comradeship lectureship gamesmanship ambassadorship')
for x in WORDS:
 if x['word']=='apprenticeship':x['sources'].append('https://www.etymonline.com/word/-ship')
if __name__=='__main__':save('continuation_20261030_pu',ROOTS,WORDS)
