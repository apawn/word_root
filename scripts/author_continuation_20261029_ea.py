"""Step, bill and stuff: actions, documents and filled spaces."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
ST=[['古英语 steppan、stepe → 中古英语 steppen → step','迈步；一步、台阶'],['现代 step','脚的移动 → 程序步骤、进展与界限']]
def H(f,m):return ST+[[f,m]]
W('step','/step/','一步；台阶；步骤；迈步',
 '脚先从这里挪到那里，是一步；做事从一个阶段走向下一阶段，也能像走路一样分成步骤。',
 '继承古英语迈步、步伐词族。台阶是让人一步步上去的结构；抽象步骤由动作阶段扩展而来。继亲前缀 step- 接另一古词，不是走了一步就成继母。',ST,
 'take a step 迈一步，the next step 下一步，watch your step 小心脚下，也可提醒行为；step aside 让到一边。',
 'take a step；the next step；step by step；watch your step。',
 'step 一步、一个台阶，stairs 常指整组楼梯；a step forward 也可比喻取得进展。',
 ('Please take a step back from the edge.','请从边缘往后退一步。'),('The first step is to check the address.','第一步是核对地址。'))
W('stepping','/ˈstepɪŋ/','迈步；step 的进行形式',
 '看到脚正在移动，也可能是一个人正在接手职责或退出岗位；短语决定迈向哪里。',
 'step 双写 p + -ing，形成规则进行、动作形式。stepping stone 垫脚石再比喻通向下一阶段的机会。',H('step + -ing → stepping','迈步中的动作 → 相应进行、动作形式'),
 'stepping in 介入、接手，stepping down 辞职、卸任；a stepping stone to success 走向成功的一块垫脚石。',
 'stepping in；stepping down；a stepping stone。',
 'stepping down 可以是卸任，不是一定从台阶往下走；stepping on someone’s toes 可说侵犯他人职责、惹恼别人。',
 ('She is stepping in while the manager is away.','经理不在期间，她正暂时代管。'),('The role was a stepping stone to a more senior position.','这个岗位是她走向更高级职位的一块垫脚石。'))
W('stepper','英 /ˈstepə/；美 /ˈstepər/','踏步机；步进装置；迈步的人',
 '可能是模拟一步步上台阶的健身器材，也可能是每次按固定小步转动的机器部件。',
 'step 双写 p + -er，构成做踏步动作的人或装置。现代健身和 stepper motor 步进电机里常见。',H('step + -er → stepper','一步步动作的主体或装置 → 踏步机、步进装置'),
 'an exercise stepper 踏步机，a stepper motor 步进电机；后者按控制信号分步运动，不是在机器里装了人的脚。',
 'an exercise stepper；a stepper motor；use a stepper。',
 '-er 可指机器，也可指人；stepper motor 的 step 是小的离散运动，不必字面跨台阶。',
 ('The gym has two exercise steppers near the windows.','健身房窗边有两台踏步机。'),('A stepper motor moves the printer head in small increments.','步进电机以小步幅移动打印头。'))
W('stepwise','/ˈstepwaɪz/','逐步的；一步一步地',
 '把一个大过程拆成小阶段，完成一阶段再接下一阶段。',
 'step + -wise，后缀在这里表示按某种方式。可作形容词、副词，不是 step + wise 聪明人。',H('step + -wise → stepwise','以步骤为方式 → 逐步的、逐步地'),
 'a stepwise approach 分步骤的方法，increase stepwise 阶段性递增；学术、技术写作比日常口语常见。',
 'a stepwise approach；stepwise improvement；proceed stepwise。',
 'stepwise 与 step by step 意思接近，前者一个词、语气更书面；不是保证每一步都成功。',
 ('The guide uses a stepwise approach to explain the process.','指南采用分步骤的方法解释流程。'),('The temperature was increased stepwise during the experiment.','实验期间，温度分阶段提高。'))
W('overstep','英 /ˌəʊvəˈstep/；美 /ˌoʊvərˈstep/','越过界限；超越权限',
 '脚跨过了一条不该跨的线，现代常用来讲职责、礼貌或允许范围。',
 'over- 越过 + step，继承对应古英语组合，而非现代才首次把两词拼起。由跨越延伸为超出应有范围。',H('over- + step → overstep','跨过去 → 越界、越权'),
 'overstep the mark 做过头，overstep your authority 越权，overstep the bounds 超出界限。',
 'overstep the mark；overstep your authority；overstep the bounds。',
 'step over 可以说跨过实际物体，overstep 常说越过抽象界限，语气往往带负面评价。',
 ('The manager was accused of overstepping her authority.','经理被指越权。'),('I did not mean to overstep the mark by asking.','我这样问并不是有意冒犯、越界。'))
W('lockstep','英 /ˈlɒkstep/；美 /ˈlɑːkstep/','紧密一致的步伐；步调一致',
 '一群人的脚步像锁在同一个节拍上，再借来讲行动、观点一起变动。',
 'lock 锁定、紧扣 + step 步伐，先用于紧密同步的行进方式，后扩展为行为、变化同步。',H('lock + step → lockstep','紧密同步的步伐 → 一致行动、同步变化'),
 'in lockstep with 与……同步，move in lockstep 步调一致；既可中性说同步，也可批评没有独立思考。',
 'in lockstep with；move in lockstep；march in lockstep。',
 'lockstep 强调同步，不自动是团结合作的赞美；lockdown 封锁是另一个组合。',
 ('The two departments changed their plans in lockstep.','两个部门同步调整了计划。'),('The article criticizes leaders who follow each other in lockstep.','文章批评了那些毫无独立判断、彼此紧随的领导者。'))
W('quickstep','/ˈkwɪkstep/','快步舞；快步进行曲、快步行进',
 'quick 和 step 的快步画面，成词后还特指一种节奏轻快的舞蹈及相应音乐。',
 'quick 快 + step 步，先有快步、快步行进等组合背景，再见特定交际舞、音乐名称。现代语境要看是在舞场还是行进。',H('quick + step → quickstep','快步 → 快步舞、相关音乐或行进'),
 'dance the quickstep 跳快步舞，a quickstep routine 一套快步舞动作；普通快走通常说 walk quickly。',
 'dance the quickstep；a quickstep routine；quickstep music。',
 'quickstep 是固定舞种等词义，不等于任何速度快的脚步；step quickly 才是临时描述快点迈步。',
 ('They danced the quickstep in the final round.','他们在最后一轮跳了快步舞。'),('The band played a lively quickstep.','乐队演奏了一首活泼的快步舞曲。'))
W('instep','/ˈɪnstep/','脚背；鞋面覆盖脚背的部分',
 '脚上面、脚趾与脚踝之间拱起来的那片区域，足球里也常说用这里触球。',
 'in- + step 的历史组合，现代指脚的上部。不能把 in 字面套成脚底的内侧；身体部位名称按实际用法记。',H('in- + step → instep','历史脚部组合词 → 脚背'),
 'a high instep 高脚背，kick with the instep 用脚背踢；也可说鞋对应这一区域的部分。',
 'a high instep；the instep of the foot；kick with the instep。',
 'instep 脚背，sole 脚底，heel 脚跟；不是鞋子里的一步。',
 ('These shoes are tight across the instep.','这双鞋的脚背部位太紧。'),('She struck the ball with her instep.','她用脚背踢中了球。'))
R('B3625','迈步、步骤与抽象界限','STEP：脚挪一步，事情推进一步','先看 step、stepping，再读逐步、越界和同步；器材、舞蹈与脚背单列具体词义。',
 '步伐词继承古英语迈步词族；stepmother 等继亲前缀 step- 是另一历史来源，已在亲属词族解释，不从迈步硬编。',
 'step → stepping、stepper；-wise 逐步，over- 越过，lock- 同步，quick- 快；instep 为脚背名。共享 footstep、doorstep、misstep、sidestep。',
 [['动作与步骤','step · stepping · stepper · stepwise'],['界限与行进方式','overstep · misstep · sidestep · lockstep · quickstep'],['脚步、台阶与脚部','footstep · doorstep · instep']],
 'stepwise 逐步不是智慧；overstep 常越权；instep 脚背不是脚底；继亲 step- 与走路义分开。',
 'We need a stepwise plan that does not overstep our authority.\n\n我们需要一份分步骤、且不超出权限的计划。',
 'step stepping stepper stepwise overstep misstep sidestep lockstep quickstep footstep doorstep instep')
BI=[['中世纪拉丁 bulla 印封文件 → 法语 bille 等 → 英语 bill','书面文件 → 账单、法案、海报等'],['另一路古英语 bile → bill','鸟嘴；与文书义不同源']]
W('bill','/bɪl/','账单；法案；美式钞票；鸟嘴；开账单',
 '餐厅让你付的钱写在 bill 上，议会讨论的法案也叫 bill；鸭子的 bill 则是嘴，不是它欠的钱。',
 '文书义经法语接中世纪拉丁印封文件词族，扩展到账单、拟议法律、告示等。鸟嘴义继承古英语 bile，是另一来源；钞票义尤其常见美式。',BI,
 'pay the bill 付账，an electricity bill 电费账单，a bill in parliament 议会法案，a dollar bill 美元纸币；bill someone for something 就某项费用向某人开账单。',
 'pay the bill；an electricity bill；a dollar bill；bill someone for。',
 'bill 法案尚在立法程序中，act 常指通过后的法律文件；bill 账单与 receipt 收据也有先后、功能区别。',
 ('Could we have the bill, please?','请给我们账单，好吗？'),('The duck has a broad, flat bill.','这只鸭子有一张宽而扁的嘴。'))
W('billable','/ˈbɪləbəl/','可计费的；可向客户收费的',
 '做了这项工作，可以按约定写进给客户的账单；重点是费用能不能算给客户。',
 'bill 开账单 + -able 可被，形成可计费的。常用于律师、顾问、技术服务等的时间或工作项目。',BI[:1]+[['bill + -able → billable','可以列入账单 → 可计费的']],
 'billable hours 可计费工时，billable work 可收费工作；不是所有上班时间都必然属于 billable hours。',
 'billable hours；billable time；billable work。',
 'billable 可收费，paid 已付款、带薪；一段 billable time 可以尚未实际收款。',
 ('She recorded six billable hours for the project.','她为这个项目记录了六小时可计费工时。'),('The contract explains which expenses are billable.','合同说明了哪些开支可以向客户收费。'))
R('B3264','账单、法案、票据；另源的鸟嘴','BILL：先看文书，再分开鸟嘴','餐厅账单、议会法案和美式钞票都从文书分支理解；鸟嘴另源单列。',
 '文书义经法语接印封文件词；鸟嘴义继承古英语另一词。billboard 广告牌、playbill 演出单已经精讲，共享归在文书告示相关分支。',
 'bill → billable；bill + board → billboard；play + bill → playbill。',
 [['核心与计费','bill · billable'],['告示与演出单','billboard · playbill']],
 'bill 账单不是 receipt 收据；法案不是已通过法律的自动同义词；billable 可收费不等于已收钱。',
 'The bill lists the consultant’s billable hours.\n\n账单列出了顾问的可计费工时。',
 'bill billable billboard playbill')
SU=[['古法语 estoffe、estoffer → 中古英语 stuffe、stuffen','材料、配备；提供所需、填充'],['现代 stuff','东西、材料；把东西塞进去 → 充满、堵闷等分支']]
W('stuff','/stʌf/','东西；材料；事情；填、塞',
 '不知道或不需要细说是什么，就把一堆东西叫 stuff；作动词则是把东西往里面装、塞。',
 '经古法语材料、配备与提供所需的词形进入英语，背后联系日耳曼填塞相关动词。现代名词物品、材料与动词填塞可一起理解。',SU,
 'my stuff 我的东西，work stuff 工作上的事，stuff a bag 把包塞满；know your stuff 是懂行。名词通常不可数，不说 many stuffs 来泛指许多东西。',
 'my stuff；all this stuff；know your stuff；stuff into。',
 'stuff 东西、材料，staff 员工，发音与拼写都不同；stuff 语气随意，正式表达常换具体名词。',
 ('Please move your stuff off the table.','请把你的东西从桌上挪开。'),('He stuffed the jacket into his bag.','他把夹克塞进包里。'))
W('stuffed','/stʌft/','塞满的；填馅的；吃撑的；填充的',
 '里面已经装得满满的：包里塞衣服，食物里包馅，人肚子里也能像塞满一样表示撑了。',
 'stuff + -ed，保留双 f，末尾读 /t/。过去分词逐渐形成多种结果状态形容词。',SU+[['stuff + -ed → stuffed','填塞 → 已填满、填馅；吃撑']],
 'stuffed peppers 填馅甜椒，a stuffed toy 填充玩具；I am stuffed 口语吃撑了。stuffed animal 还可能是动物标本，要看语境。',
 'stuffed peppers；a stuffed toy；I am stuffed。',
 'stuffed 满、撑，stuffy 闷、不通风；a stuffed toy 是填充玩具，不是脾气古板的玩具。',
 ('The child carried a stuffed rabbit everywhere.','孩子走到哪儿都抱着一只填充兔玩具。'),('No more cake for me, thanks. I am stuffed.','谢谢，不再吃蛋糕了，我撑了。'))
W('stuffy','/ˈstʌfi/','闷、不通风的；鼻塞的；古板的',
 '屋里空气好像堵住了，鼻子也可能堵着；说人和气氛时，则像规矩太多、放不开。',
 'stuff + -y，接塞、堵的画面。由空气不流通、鼻部堵塞扩展到拘谨、古板的社会气氛与态度。',SU+[['stuff + -y → stuffy','堵塞、填满的感觉 → 闷；古板']],
 'a stuffy room 闷的房间，a stuffy nose 鼻塞，a stuffy atmosphere 拘谨古板的气氛。',
 'a stuffy room；a stuffy nose；a stuffy atmosphere。',
 'stuffy 可以形容空间或态度，stuffed 说塞满、吃撑；a stuffy dinner 可能气氛拘谨，不是人人吃撑。',
 ('The room was hot and stuffy, so we opened a window.','房间又热又闷，我们便开了扇窗。'),('The club felt too formal and stuffy for her.','她觉得那家俱乐部太正式、太古板。'))
R('B3600','东西、材料；塞满与堵闷','STUFF：一堆东西，往里面装、塞','先学不可数的东西，再用塞满的结果理解 stuffed，用堵着的状态理解 stuffy。',
 '名词和动词经法语材料、配备与提供所需的词形进入英语。现代抽象 stuff 还能指工作杂事、某方面内容。',
 'stuff → stuffed、stuffy；stuffed 为装满结果，stuffy 为堵闷状态和态度比喻。',
 [['材料、填塞与状态','stuff · stuffed · stuffy']],
 'stuff 东西，staff 员工；stuffed 吃撑，stuffy 闷、古板；泛指东西的 stuff 通常不可数。',
 'The room was full of stuff, and the air felt stuffy.\n\n房间里堆满东西，空气也显得闷。',
 'stuff stuffed stuffy')
if __name__=='__main__':save('continuation_20261029_ea',ROOTS,WORDS)
