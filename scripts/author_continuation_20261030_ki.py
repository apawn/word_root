"""Stroke, install and tooth: motions, placement and shape."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['中古英语 strok 等；联系 strike 一族','一下击打、一次动作 → 笔画、划桨、游泳动作'],['古英语 strācian → stroken → stroke','手轻轻沿表面移动、抚摸；与前一词有历史联系'],['一次突发、有效动作等比喻','a stroke of luck；masterstroke；脑卒中的固定医学名称']]
W('stroke','英 /strəʊk/；美 /stroʊk/','一下击打、笔画、划水动作；抚摸；脑卒中',
 '想象一个完整动作：笔划过纸是一笔，桨划过水是一下，手沿猫背轻轻划过是抚摸。stroke 的不同用法围绕这些动作发展，但医学名称需单独认。',
 '击打名词见中古英语 strok 等，联系 strike 一族；抚摸动词承古英语 strācian、中古英语 stroken。现代动作、笔画、突发效果等用法并非全由一个现代动词刚刚派生。',S,
 'a brush stroke 一笔，a swimming stroke 泳姿、划水动作，stroke a cat 抚摸猫，a stroke of luck 一次好运，at the stroke of midnight 午夜钟声敲响时。a stroke 在医学里可指脑卒中。',
 'a brush stroke；stroke a cat；a stroke of luck。',
 'stroke a cat 是轻抚；strike a cat 则是打猫。stroke 的医学义是固定病名，不能把 sunstroke 按字面当成同一种脑卒中。',
 ('She stroked the cat’s back gently.','她轻轻抚摸猫的背。'),('The artist made the shape with three bold strokes.','画家用三笔有力的笔画勾出了形状。'),sources=['https://en.wiktionary.org/wiki/stroke#English','https://www.etymonline.com/word/stroke'])
W('masterstroke','英 /ˈmɑːstəstrəʊk/；美 /ˈmæstərstroʊk/','妙招、神来之笔',
 '关键时刻一个很高明的动作，整件事因它变好，便可称 a masterstroke。master 在这里借高手的本领，stroke 借一次有效行动。',
 'master 高手、精湛 + stroke 一次行动，组合成赞叹高明做法的名词。',S[:1]+[['master + stroke → masterstroke','高手般的一招 → 妙招、神来之笔']],
 'a masterstroke of diplomacy 外交妙招，prove a masterstroke 证明是一步妙棋。可说策划、选角、设计等。',
 'a masterstroke of planning；prove a masterstroke。',
 'masterstroke 强调特别高明、效果好的关键行动；milestone 强调重要阶段、里程碑。',
 ('Moving the event indoors proved a masterstroke.','把活动改到室内，后来证明是个妙招。'),('Casting an unknown actor was a masterstroke.','选一位无名演员担纲，是神来之笔。'))
R('B3134','一次动作、抚摸与动作留下的痕迹，再看固定转义','STROKE：动作划过一次，或留下一笔','stroke → masterstroke；keystroke、backstroke、breaststroke 分别看键、游泳动作；sunstroke 另认固定医学名。',
 '先用动作把笔画、划桨、抚摸串起来，再把疾病等已经固定的词义单独记，避免用一个比喻包办全部意义。',
 'strok 击打名词与 strācian 抚摸动词有历史联系；master 高手，key 键，back 背，breast 胸。',
 [['基础与巧妙行动','stroke · masterstroke'],['身体、按键与固定名称','backstroke · breaststroke · keystroke · sunstroke']],
 'stroke 动词可轻抚，strike 可击打；masterstroke 是妙招；sunstroke 不等于脑卒中。',
 'With one confident stroke, she completed what proved to be a masterstroke of design.\n\n她自信地落下一笔，完成了设计中的神来之笔。','stroke masterstroke backstroke breaststroke keystroke sunstroke')
I=[['日耳曼语位置、座位词 → 中世纪拉丁 stallum','固定位置、席位'],['in- 在内 + stallum → installāre → 法语 installer → install','使就位、就任 → 安装、安置'],['另一路：法语 estaler 等 → installment','安排付款 → 每期付款、分期提供的一部分']]
W('install','英 /ɪnˈstɔːl/；美 /ɪnˈstɔːl/，部分美音 /ɪnˈstɑːl/','安装、设置好；使就任；安置',
 '把设备放到该在的位置，接好、设好，能用起来，是 install；把人正式安置到职位上，也可用这个旧核心。',
 '经法语 installer 上接中世纪拉丁 installāre，in- 在内 + stallum 席位、位置，后者来自日耳曼语言。早期任职就位义再扩到设备、软件安装。',I[:2],
 'install a heater 安装暖气设备，install an app 安装应用，install someone as chair 让某人正式就任主席，install yourself in a chair 在椅子里安坐。',
 'install an app；install a heater；install someone as chair。',
 'download 把数据下载过来，install 把东西设置成可用状态。软件有时下载后还需安装，两个动作不总是同一步。',
 ('They installed new lights in the kitchen.','他们在厨房安装了新灯。'),('I installed the app after downloading it.','下载后，我安装了这个应用。'))
W('installation','/ˌɪnstəˈleɪʃən/','安装、就任；整套设备、设施；装置艺术作品',
 '可以说把设备装好的过程，也可以说已经布置好的一整套设备。艺术里用空间、物件等布置出的作品，也叫 installation。',
 '经法语 installation 上接中世纪拉丁 installātiō，现代对应 install + -ation。名词从动作扩到安排好的系统、设施、作品。',I[:2]+[['installātiō → installation','安装、就任；安装好的设备、设施与空间作品']],
 'software installation 软件安装，an electrical installation 电气装置，an art installation 装置艺术作品，a military installation 军事设施。',
 'software installation；an art installation。',
 'installation 既可不可数地说安装过程，也可用 an installation 说一套装置、一个作品。不是每次都翻成安装操作。',
 ('The installation took less than an hour.','安装花了不到一小时。'),('Visitors walked through the light installation.','观众从那件灯光装置作品中走过。'))
W('installer','英 /ɪnˈstɔːlə/；美 /ɪnˈstɔːlər/','安装工；安装程序',
 '安装的人是 installer；软件里替你复制文件、完成设置的程序，也用 -er 叫 installer。',
 'install + -er，标示安装这一动作的执行者，可是人，也可是程序。',I[:2]+[['install + -er → installer','安装的人或程序']],
 'a window installer 窗户安装工，a software installer 软件安装程序，run the installer 运行安装程序。',
 'a software installer；run the installer。',
 'installer 是执行安装的人或程序，installation 是安装过程或装好的设施。',
 ('The installer checked that every window closed properly.','安装工检查每扇窗是否能正常关上。'),('The installer asked me to choose a folder.','安装程序让我选择一个文件夹。'))
W('uninstall','英 /ˌʌnɪnˈstɔːl/；美 /ˌʌnɪnˈstɔːl/','卸载、移除已安装的软件或硬件',
 '东西先被安装进系统，再把相应安装关系撤去，就是 uninstall。常见的是卸载应用。',
 'un- 逆转动作 + install。这里不是形容某物尚未安装，而是说执行卸载。',I[:2]+[['un- + install → uninstall','撤销安装、卸载']],
 'uninstall an app 卸载应用，uninstall a driver 卸载驱动，an uninstall option 卸载选项。',
 'uninstall an app；an uninstall option。',
 'uninstall 与 delete 不总是同一操作；只删桌面图标通常并没有卸载程序。具体残留数据取决于软件。',
 ('She uninstalled the game to free some space.','她卸载游戏，腾出一些空间。'),('The menu includes an option to uninstall the program.','菜单中有卸载程序的选项。'))
W('reinstall','英 /ˌriːɪnˈstɔːl/；美 /ˌriːɪnˈstɔːl/','重新安装；重新使就任',
 '原来装过，再装一遍，是 reinstall。重点是安装这个动作再做一次。',
 're- 再 + install，与 uninstall 的撤销方向不同。',I[:2]+[['re- + install → reinstall','再次安装、重新就位']],
 'reinstall an app 重新安装应用，reinstall the operating system 重新安装操作系统。',
 'reinstall an app；reinstall the software。',
 'reinstall 是重装，restart 是重新启动。关掉再打开程序，不一定发生重新安装。',
 ('He reinstalled the app after replacing his phone.','换手机后，他重新安装了应用。'),('The instructions explain how to reinstall the software.','说明解释了怎样重新安装软件。'))
W('installment','英 /ɪnˈstɔːlmənt/；美 /ɪnˈstɔːlmənt/','分期付款中的一期；连载、系列的一期、一部',
 '总额分几次交，每次是一笔 installment；故事分几次发表，每期也可以是 installment。共同点是整件事分批提供。',
 '常用分期义是 estallment 的变形，联系法语 estaler 安排付款、estal 固定位置等，不能全按 install 安装 + -ment 解释。另有历史同形词确实指就任、安装。',I[2:]+[['分批付款 → installment 的一般扩展','系列中按次提供的一部分']],
 'pay in installments 分期付款，a monthly installment 每月一期款，the latest installment 最新一集、一部。英式也常拼 instalment。',
 'pay in installments；a monthly installment；the latest installment。',
 '常用 installment 是分期提供的一部分，installation 才常说安装、设施。分期总额、次数等要另外说明，词本身不规定。',
 ('They paid for the furniture in six installments.','他们分六期支付了家具款。'),('The next installment of the story appears on Friday.','故事的下一期周五刊出。'),sources=['https://en.wiktionary.org/wiki/installment#English','https://www.etymonline.com/word/installment'])
R('B4378','使设备、软件或人就位，另分清分期义的 installment','INSTALL：安置到位，让设备或职务开始运作','install → installation、installer、uninstall、reinstall；installment 的常用分期义走相关但不同的法语路径。',
 '安装一组看就位与动作方向，分期一组看分批提供。字形接近不代表现代 install 直接派生了所有意义。',
 'in- + stallum 位置 → install；-ation 名词，-er 执行者，un- 撤销，re- 再；estaler 等 → 分期 installment。',
 [['安装、过程与执行者','install · installation · installer'],['撤销与重新安装','uninstall · reinstall'],['分期提供的另一支','installment']],
 'download、install、restart 是不同动作；installment 不要误当现代安装名词。',
 'The installer completed the installation, so there was no need to reinstall the app.\n\n安装程序完成了安装，因此无需重装应用。','install installation installer uninstall reinstall installment')
T=[['古英语 tōþ → 中古英语 toth → tooth','牙；与其他印欧语言的齿名有共同历史'],['身体形态用于器具','锯齿、齿轮的齿；比喻执行力量'],['后缀与复合词','toothed、toothless、toothy；sawtooth 等']]
W('tooth','/tuːθ/','牙齿；锯齿、齿轮齿等；执行力量〔常见复数比喻〕',
 '牙负责咬、切、磨；锯和齿轮上的凸起像牙，也叫 tooth。规则若真能咬得动、执行得下去，便可说 it has teeth。',
 '承古英语 tōþ，经中古英语 toth 等传下。复数 teeth /tiːθ/ 保存旧的元音变化；不是通常的 tooths。',T[:2],
 'a loose tooth 松动的牙，brush your teeth 刷牙，the teeth of a saw 锯齿，give a rule teeth 让规则有执行力，a sweet tooth 爱吃甜食。',
 'brush your teeth；a sweet tooth；give rules teeth。',
 'tooth 单数、teeth 复数；复合词常用单数作前部，如 toothbrush。a sweet tooth 是爱好，不是某颗牙味甜。',
 ('The child has a loose tooth.','孩子有一颗牙松了。'),('The old rules had no teeth.','旧规则没有实际约束力。'))
W('toothed','/tuːθt/，也读 /tuːðd/','有牙、带齿的；有某类牙齿的',
 '锯片边上一排尖齿，是 toothed；描述动物时也可配其他成分，说牙长什么样。',
 'tooth + -ed，表示有某物、带某种结构的性质。这里不必理解为过去有人执行了一个长牙动作。',T[:2]+[['tooth + -ed → toothed','有牙齿或类似齿状凸起']],
 'a toothed blade 带齿刀片，a toothed wheel 齿轮；动物名称里也见相应组合。',
 'a toothed blade；a toothed wheel。',
 'toothed 说有齿；toothy 常说牙显眼、露齿的表情。-ed 在这里常构成有……的形容词。',
 ('The machine uses a toothed belt.','机器使用齿形带。'),('A toothed wheel turned inside the case.','一个齿轮在机壳里转动。'))
W('toothless','/ˈtuːθləs/','没有牙的；缺少执行力、无实权的',
 '没有牙，就少了咬住、咬动的能力。比喻里，一个机构、规定看起来存在，却没有实际执行力量，也叫 toothless。',
 '古英语已有 tōþlēas，现代对应 tooth + -less。字面的无牙，再借牙的力量形象扩到无实权。',T[:1]+[['tōþlēas → toothless','没有牙；比喻不能有效执行、约束']],
 'a toothless smile 无牙的笑容，a toothless law 缺乏执行力的法律，a toothless committee 无实权的委员会。',
 'a toothless smile；a toothless committee。',
 'toothless 的比喻常批评执行力量不足，不一定说文字内容完全不存在或完全没有任何作用。',
 ('The baby gave a toothless smile.','婴儿露出无牙的笑容。'),('Critics called the committee toothless.','批评者称委员会没有实权。'))
W('toothy','/ˈtuːθi/','牙齿显眼的、露齿的',
 '笑得露出一排牙，照片里牙很显眼，就是 a toothy grin。说的是可见的样子。',
 'tooth + -y，表示牙齿显眼、突出的性质。固定搭配里常修饰 smile、grin。',T[:2]+[['tooth + -y → toothy','牙显眼、露齿的样子']],
 'a toothy grin 露齿的大笑，a toothy smile 露齿微笑。通常只是描写表情、外观，褒贬看语境。',
 'a toothy grin；a toothy smile。',
 'toothy smile 强调露齿，toothless smile 则不露牙或没有牙；仅说 toothed 不能自然替代常用表情搭配。',
 ('He greeted the camera with a toothy grin.','他对着镜头露齿大笑。'),('The cartoon crocodile has a huge toothy smile.','卡通鳄鱼咧嘴露出一大排牙。'),sources=['https://en.wiktionary.org/wiki/toothy#English','https://www.merriam-webster.com/dictionary/toothy'])
W('sawtooth','英 /ˈsɔːtuːθ/；美 /ˈsɔːtuːθ/，也读 /ˈsɑːtuːθ/','锯齿；锯齿形、锯齿状波形',
 '一排尖峰像锯子的齿，便可叫 sawtooth。图表、屋顶、电子波形都能借这个形状名称。',
 'saw 锯 + tooth 齿；由真实锯齿扩到相似尖峰、波形。saw 在这里是锯，不是 see 的过去式。',T[:2]+[['saw + tooth → sawtooth','锯齿 → 相似形状、波形']],
 'a sawtooth roof 锯齿形屋顶，a sawtooth pattern 锯齿图案，a sawtooth wave 锯齿波。',
 'a sawtooth roof；a sawtooth pattern；a sawtooth wave。',
 'sawtooth 强调一侧渐变、另一侧骤回等锯齿轮廓的语境很常见；triangle wave 是另一类波形，不能只因都有尖角就混为一谈。',
 ('The old factory has a sawtooth roof.','旧工厂有一个锯齿形屋顶。'),('The chart shows a repeating sawtooth pattern.','图表显示反复出现的锯齿形走势。'))
R('B2763','口中的牙、器具上的齿，以及咬合、执行力量的比喻','TOOTH：能咬住的结构，也成为形状与力量的形象','tooth → toothed、toothless、toothy；sawtooth 看锯齿；toothbrush 等看口腔用品。',
 '牙、锯齿、规则有没有牙，分别是身体、形态、能力的三层。先找层次，再记派生词。',
 'tōþ → tooth，复数 teeth；-ed 有，-less 无，-y 性质；saw 锯、brush 刷、paste 膏、pick 剔取。',
 [['基础与性质','tooth · toothed · toothless · toothy'],['器具形状与日用品','sawtooth · toothbrush · toothpaste · toothpick · houndstooth']],
 '复数 teeth；toothed 带齿、toothy 常露齿；toothless 的比喻说执行力量。',
 'The child put down the toothbrush and gave a toothy grin.\n\n孩子放下牙刷，露齿笑了。','tooth toothed toothless toothy sawtooth toothbrush toothpaste toothpick houndstooth')
if __name__=='__main__':save('continuation_20261030_ki',ROOTS,WORDS)
