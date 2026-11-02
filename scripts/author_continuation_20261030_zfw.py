"""Sideways approach, crawling, trailing and concealed action."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3311':dict(words='side sidle sidles sidled sidling sidelong sideways'.split(),label='side：侧身挪近和斜眼一看',note='sidle 通常从旧方向副词 sideling 逆构；sidelong 也是旧 sideling 的变化，后半受 long 影响，不能按现代 long 很长直接推义。'),
 'B4275':dict(words='crawl crawls crawled crawling crawler crawlers'.split(),label='crawl 的贴地爬行、缓慢前进与爬虫',note='crawl 接北欧爬、抓行材料；现代 crawled 用规则 -ed，crawler 加人物、工具后缀，网络爬虫是程序逐页访问的比喻。'),
 'B2781':dict(words='trail trails trailed trailing'.split(),label='trail：拖在后面、跟随与落后',note='trail 经法语接拖行、循迹材料；现代 trailed、trailing 可用于身体跟随、拖曳、比分落后、话音渐弱等场景。'),
 'B4091':dict(words='sneak sneaky sneakier sneakiest sneakily'.split(),label='sneaky 的比较程度和动作方式',note='sneaky 为 sneak + -y；比较级、最高级改 y 为 i 加完整 -er、-est，副词为 sneakily，不把形容词末尾 -y 当 -ly。'),
 'B4579':dict(words='steal stealth stealthy stealthier stealthiest stealthily stealthiness'.split(),label='stealth 从秘密行动到隐蔽的性质、方式',note='stealth 的旧名词材料与 steal 相关，但现代元音不同；stealthy 加 -y，后续比较、方式和性质扩展分别解释。'),
 'A1697':dict(words='lurk lurks lurked lurking lurker lurkers prowl prowler prowlers'.split(),label='lurker、prowler 的人物角色与复数',note='lurk、prowl 分别加 -er 表示做这种动作的人，再加复数 -s；潜藏与游走搜寻是不同画面，列在同页作对照。'),
 'A1839':dict(words='furtive furtively furtiveness stealthy stealthiness'.split(),label='furtiveness、stealthiness 把隐蔽的性质当名词',note='furtiveness 由 furtive 加 -ness，保留 e；stealthiness 由 stealthy 改 y 为 i 加 -ness。furtive 接拉丁小偷、偷窃词族，和英语 fur 皮毛另路。'),
 'A1760':dict(words='skulk skulks skulked skulking lurk lurks lurked lurking'.split(),label='skulk、lurk 的躲藏、潜伏词形',note='skulk 可能借北欧躲藏、逃避责任的词；lurk 也有北欧来源线索，不能据近义就当彼此派生。现代过去式分别加完整 -ed，均读 /t/。'),
}
SIDLE=[['side + 旧方向副词词尾 -ling → sideling','早期说侧向、斜向的方式，并非现代进行式'],['sideling → 逆构 sidle → 现代规则词形','动词按 -le 结尾形式形成，现代侧身挪动、悄悄靠近']]
W('sidles','/ˈsaɪdəlz/','侧身挪动、悄悄靠近〔第三人称单数〕',
 '不正面大步走来，而是从边上一点点挪到你身旁，好像不想引起太多注意，这个动作叫 sidles。',
 'sidle + -s，词尾读 /z/；sidle 通常从旧 sideling 逆构，不能直接把 e 前随意切成 side + le。',SIDLE+[['sidle + -s → sidles','他、她侧身、悄悄挪动']],
 'sidles up to someone 悄悄凑到某人身旁；sidles through the gap 侧身挪过缝隙。',
 'sidles away；sidles over for a chat。',
 'sidles up to 常带谨慎、羞怯或别有想法的姿态，但动作本身并不保证恶意。',
 ('He sidles up to me whenever he wants a favour.','他每次想请我帮忙，就悄悄挪到我身旁。'),('The cat sidles through the narrow gap.','猫侧着身，从窄缝里悄悄挪过去。'),sources=S('sidles','sidle'))
W('sidled','/ˈsaɪdəld/','侧身挪过去了；悄悄凑近、溜开了',
 '刚才他没有直接站到你面前，而是小步侧着挪近，这个过去的动作叫 sidled。',
 'sidle 去末尾不发音 e，加完整 -ed，词尾读 /d/；历史逆构的方向与现代加过去词尾是两回事。',SIDLE+[['sidle → sidled','把侧向、悄悄挪动放到过去']],
 'sidled up to me 悄悄挪到我身旁；sidled past 侧着身悄悄经过。',
 'sidled into the room；sidled away from the group。',
 'stepped up 只说走上前；sidled up 把侧身、小步、不想太显眼的样子一起写出来。',
 ('She sidled up to me and whispered a question.','她悄悄挪到我身边，小声问了个问题。'),('We sidled past the sleeping dog.','我们侧着身，悄悄从睡着的狗旁边挪过。'),sources=S('sidled','sidle'))
W('sidling','/ˈsaɪdlɪŋ/','正在侧身挪动、悄悄靠近的',
 '身体斜着一点，脚步小一点，人正从边上挪过去，这段进行中的动作叫 sidling。',
 '现代 sidle 去 e 加 -ing → sidling。较早的 sideling 是方向副词材料，历史上不能倒说它一开始就是现代 sidle 的进行式。',SIDLE+[['现代 sidle → sidling','去 e 加 -ing，写正在发生的侧身挪动']],
 'sidling up to someone 正悄悄凑近；sidling through a crowd 侧着身挪过人群。',
 'come sidling over；sidling towards the door。',
 'sidling 与 sidelong 都有侧向画面：sidling 是挪动的动作形式，sidelong 常形容斜着看的一眼。',
 ('I saw him sidling towards the door.','我看见他正悄悄往门边挪。'),('She came sidling over to ask about the surprise.','她悄悄挪过来，想问那份惊喜是什么。'),sources=S('sidling','sidle'))
W('sidelong','英 /ˈsaɪdlɒŋ/；美 /ˈsaɪdlɔːŋ/','斜着的；从眼角看的；侧向地',
 '头没有完全转过去，眼睛却从旁边瞥了一下，这叫 a sidelong glance：视线从侧边出去。',
 '旧 sideling、sidelings 变为 sidelong，后半可能受 long 拼写影响；历史尾部是方向副词材料，不是说旁边很长。',SIDLE+[['sideling → sidelong','旧方向副词形式变化；后来也作形容词']],
 'a sidelong glance 斜瞥的一眼；look sidelong at someone 斜眼看某人；走过时也可以 turn sidelong 侧过身。',
 'cast a sidelong look；a sidelong smile 侧着脸露出的笑。',
 'sideways 范围更广，常说身体、物体横向移动；sidelong 尤其常见于一瞥、眼神的描写。',
 ('She gave me a sidelong glance and hid a smile.','她斜瞥了我一眼，忍住了笑。'),('He looked sidelong at the unopened letter.','他从眼角瞥向那封没拆的信。'),sources=S('sidelong','sidelong'))
CRAWL=[['北欧语言的爬行、抓行材料 → 中古英语 creulen → crawl','可比较古诺尔斯语 krafla 等；不能把未见记录的古英语推定形式当实证'],['贴地爬 → 极慢地前进；后来也用于程序逐页访问','慢与逐步推进是常见学习桥梁；泳姿、爬行程序等需按场景选义']]
W('crawls','英 /krɔːlz/；美 /krɔːlz/','爬行、缓缓前进〔第三人称单数〕；爬行、缓慢移动〔复数〕',
 '婴儿手膝着地爬过去，用 crawls；车流慢到像挪着爬，也用 crawls。不是每次都真有肚子贴着地。',
 'crawl + -s，词尾读 /z/；北欧旧动作材料演变成基础 crawl，现代才在此基础上加词尾。',CRAWL+[['crawl + -s → crawls','它、他、她爬、极慢前进；数次这种移动']],
 'crawls on hands and knees 手膝着地爬；traffic crawls 车流缓慢挪动。',
 'crawls across the floor；crawls along at walking speed。',
 'crawls 在婴儿、动物场景多指真实爬行；说车时是速度比喻，不要求车轮出了故障。',
 ('The baby crawls towards the bright red ball.','婴儿朝鲜红的球爬过去。'),('Traffic crawls through the centre of town.','车流穿过镇中心时缓缓挪动。'),sources=S('crawls','crawl'))
W('crawled','英 /krɔːld/；美 /krɔːld/','爬过去了；缓慢前进了；检索、抓取了〔网页〕',
 '身体放低一点点往前爬，是 crawled；一路堵车，只挪出一点点路，也能这样写。程序逐页访问网站，则借用同一动作词。',
 'crawl + -ed，词尾读 /d/；规则过去形式，不像 creep 的 crept 那样改元音。',CRAWL+[['crawl + -ed → crawled','过去爬动、缓慢前进，或程序已经逐页访问']],
 'crawled under the table 爬到桌下；crawled home 缓缓回家；the bot crawled the site 程序抓取了该网站。',
 'crawled through a tunnel；crawled along the road。',
 'crawled 和 crept 都能写慢移；crept 更常突出悄悄、难察觉，crawled 更容易突出慢得像在爬。',
 ('We crawled through the low tunnel on our hands and knees.','我们手膝着地，爬过低矮的隧道。'),('The bus crawled home through heavy traffic.','公交车穿过拥堵车流，缓缓往回开。'),sources=S('crawled','crawl'))
W('crawling','英 /ˈkrɔːlɪŋ/；美 /ˈkrɔːlɪŋ/','正在爬、缓慢前进；爬满的；网页抓取',
 '一只只虫在表面爬，看起来到处都是，叫 crawling with insects；车一点点挪、程序逐页抓取，也各有 crawling 的场景。',
 'crawl + -ing；既能组成进行式，也可作形容词、过程名词。crawling with 后面写密布、到处都是的东西。',CRAWL+[['crawl + -ing → crawling','正在爬动；扩展为爬满、逐页访问的状态或过程']],
 'crawling under the fence 从篱笆下爬过；crawling with ants 爬满蚂蚁；web crawling 网页抓取。',
 'crawling traffic 缓慢挪动的车流；made my skin feel as if it were crawling 让我浑身发毛。',
 'crawling with 可以夸张说某处到处是某类人，不是那些人真在地上爬；说话人的态度可能带嫌弃。',
 ('The old log was crawling with ants.','那根旧木头上爬满了蚂蚁。'),('We were crawling along behind a long line of trucks.','我们跟在一长串卡车后面，缓缓往前挪。'),sources=S('crawling','crawl'))
W('crawlers','英 /ˈkrɔːləz/；美 /ˈkrɔːlərz/','爬行者、爬行物；网络爬虫程序〔复数〕',
 '把会爬、慢慢推进的对象叫 crawler；在网站之间逐页访问、收集页面的程序，也像一路爬着查看，叫 crawlers。',
 'crawl + -er → crawler，再加复数 -s，词尾读 /z/；-er 可以指人，也可以指动物、机器、程序等行动主体。',CRAWL+[['crawl + -er + -s → crawlers','多个爬行者、爬行物，或逐页访问的程序']],
 'search engine crawlers 搜索引擎爬虫；tiny crawlers 小小的爬行物，需看上下文是虫、婴儿还是别的对象。',
 'web crawlers；crawlers visiting the site 访问网站的爬虫程序。',
 'crawlers 是抓取页面的程序，网页本身不是 crawler；search engine 则还包括索引、检索等其他环节。',
 ('Search engine crawlers visit the public pages of the site.','搜索引擎爬虫会访问网站的公开页面。'),('The chart shows how often crawlers returned to each page.','图表显示爬虫返回每个页面的频率。'),sources=S('crawlers','crawl'))
TRAIL=[['古法语 trailler 等拖行、循迹材料 → 英语 trail','更远通常联系拉丁语拖拉词族，具体中间路线保留可能性'],['拖在后面、跟着痕迹 → 跟随、落后；话音逐渐弱去','现代学习画面是后面留一段、跟一段，但不把全部义项硬排成一条历史顺序']]
W('trailed','/treɪld/','拖在后面了；跟随、追踪了；落后了；话音弱下去了',
 '长裙拖在身后，孩子跟在后头，队伍比分落在别人后面，都能用 trailed；话尾越说越弱，则常接 off。',
 'trail + -ed，词尾读 /d/；基础词经法语接拖行、循迹材料，现代过去式按规则构成。',TRAIL+[['trail + -ed → trailed','过去拖曳、跟随或处于落后位置']],
 'trailed behind 跟在后面、落在后面；trailed by two points 落后两分；voice trailed off 声音逐渐弱下去。',
 'trailed a hand in the water 把手垂在水里拖着；trailed after someone。',
 'trailed 后接人可说跟随，接比分差常用 by；看到同一形式，先找它跟着谁、落后多少。',
 ('The children trailed behind us along the path.','孩子们沿着小路跟在我们后面。'),('Her voice trailed off when she saw the empty chair.','看见那把空椅子时，她的声音渐渐弱了下去。'),sources=S('trailed','trail'))
W('trailing','/ˈtreɪlɪŋ/','拖在后面的；跟随、落后的；垂蔓的；位于末尾的',
 '前面的已经走了，后面还拖着、跟着一段，这就是 trailing 的画面。衣服下摆、植物蔓条、比分落后，都可放进不同场景。',
 'trail + -ing，既可作进行形式，也可形容后随、下垂、位于末尾的性质。',TRAIL+[['trail + -ing → trailing','正在拖随、落后；或把末尾、下垂当作性质']],
 'trailing plants 垂蔓植物；a team trailing by one goal 落后一球的队；trailing spaces 文本末尾的空格。',
 'a trailing scarf 拖在后面的围巾；trailing behind the others。',
 'trailing spaces 是字符串末尾的空格，leading spaces 是开头的空格；编程用法借位置画面，不是键盘上真有拖行。',
 ('Her long scarf was trailing on the ground.','她的长围巾拖在地上。'),('Remove any trailing spaces before saving the text.','保存文本前，删掉末尾多余的空格。'),sources=S('trailing','trail'))
LURK=[['中古英语 lurken：躲藏、藏而不露 → lurk','可能接北欧相关材料，较远来源不完全确定'],['不露面的存在 → 危险、疑虑隐存；网络只看不发言','现代有隐藏、不易察觉的感觉，不要求人一直在移动']]
W('lurks','英 /lɜːks/；美 /lɝːks/','潜伏、隐藏〔第三人称单数〕；〔网络〕只看不发言',
 '东西就在那儿，却没摆到明面上：角落藏着危险，心里留着疑虑，都可以用 lurks。人在群里只看不说话，也是这种不露面。',
 'lurk + -s，/k/ 后读 /s/；基础词可能借自北欧语言，现代不再拆出额外前缀。',LURK+[['lurk + -s → lurks','它隐存；他、她躲着或只看不发言']],
 'danger lurks 危险潜伏；doubt lurks at the back of the mind 疑虑藏在心底；lurks on the forum 在论坛潜水。',
 'lurks in the shadows；lurks behind a friendly smile。',
 'prowls 侧重四处找目标的活动；lurks 可以一动不动地藏着，核心是存在却不显露。',
 ('A small doubt still lurks at the back of my mind.','我心底还藏着一点疑虑。'),('He lurks on the forum but never posts anything.','他在论坛里潜水，却从不发帖。'),sources=S('lurks','lurk'))
W('lurked','英 /lɜːkt/；美 /lɝːkt/','躲藏、潜伏了；隐存着；〔网络〕曾只看不发言',
 '过去有个人藏在后面，或某种担心一直没说出口，就用 lurked；它强调没露面，不一定突然跳出来。',
 'lurk + 完整 -ed，/k/ 后读 /t/，结尾 /kt/；拼写仍是 ed。',LURK+[['lurk + -ed → lurked','过去处在隐藏、不显露的状态']],
 'lurked behind the door 藏在门后；fear lurked beneath the excitement 兴奋底下藏着害怕。',
 'lurked online for months；lurked in the background。',
 'lurked 可以写持续隐存，hid 更一般地说藏起来或藏着；不是每个隐藏场景都带 lurk 的潜在、暗中感。',
 ('A fox lurked behind the shed.','一只狐狸藏在棚子后面。'),('I lurked in the group for weeks before introducing myself.','我在群里潜水了几周，才作自我介绍。'),sources=S('lurked','lurk'))
W('lurkers','英 /ˈlɜːkəz/；美 /ˈlɝːkərz/','潜伏、躲藏的人；〔网络〕只看不发言的人〔复数〕',
 '一个群里，发言的人只有几个，默默看消息的却可能很多；这些只看不公开回应的人就是 lurkers。',
 'lurk + -er → lurker，再加 -s；人物名词很早已有，网络义是后来把不露面的画面搬到线上。',LURK+[['lurk + -er + -s → lurkers','多个藏着不露面的人；后来也指网络潜水者']],
 'forum lurkers 论坛潜水者；welcome the lurkers 邀请一直默默看的人也参与。',
 'lurkers and regular posters 潜水者与经常发帖者；many silent lurkers。',
 'lurkers 在线上并不自动指恶意窥探者，往往只是选择不发言的读者；动机不能只凭这个名词判断。',
 ('The forum has far more lurkers than regular posters.','论坛里潜水的人远比经常发帖的人多。'),('Several lurkers introduced themselves during the anniversary event.','周年活动时，几位一直潜水的成员作了自我介绍。'),sources=S('lurkers','lurk'))
SNEAKY=[['sneak：避开注意地行动 → sneak + -y → sneaky','把偷偷做事的样子变成形容词，可带不诚实、耍小聪明的评价'],['sneaky → sneakier、sneakiest、sneakily','程度与方式分别扩展，不给每个变化形式另编古代来源']]
W('sneakier','英 /ˈsniːkiə/；美 /ˈsniːkiər/','更偷偷摸摸的；更狡猾隐蔽的',
 '原来是明着试，后来改成绕开别人视线、暗暗动手脚；手段变得更不容易被发现，就可说 sneakier。',
 'sneaky 改 y 为 i，加完整比较级 -er；更前面是 sneak + 形容词 -y。',SNEAKY+[['sneaky → sneakier','比较偷偷摸摸、隐蔽耍巧的程度']],
 'a sneakier way 更隐蔽、耍小聪明的办法；get sneakier 变得更鬼鬼祟祟。',
 'sneakier than before；a much sneakier trick。',
 'cleverer 可只是更聪明，sneakier 通常额外带避人注意、手段不够光明的评价，也能半开玩笑地使用。',
 ('He found a sneakier way to hide the extra biscuits.','他想了个更隐蔽的办法，把多拿的饼干藏起来。'),('The second trick was much sneakier than the first.','第二个把戏比第一个更狡猾隐蔽。'),sources=S('sneakier','sneaky'))
W('sneakiest','/ˈsniːkiɪst/','最偷偷摸摸的；最狡猾隐蔽的',
 '几个办法里，这一个最会绕过人的注意，最让人不容易察觉，可以说 the sneakiest。',
 'sneaky 改 y 为 i，加完整最高级 -est；读音中 /i/ 后接 /ɪst/。',SNEAKY+[['sneaky → sneakiest','在范围内把隐蔽耍巧的程度推到最高']],
 'the sneakiest trick 最狡猾的把戏；the sneakiest way 最偷偷摸摸的办法。',
 'one of the sneakiest tricks；the sneakiest person in the group。',
 'sneakiest 是评价隐蔽、狡猾的程度，不等于最成功；最难被发现的尝试也可能失败。',
 ('That was the sneakiest trick in the whole game.','那是整场游戏里最狡猾隐蔽的一招。'),('She found the sneakiest hiding place for the surprise gift.','她给惊喜礼物找了个最让人猜不到的藏处。'),sources=S('sneakiest','sneaky'))
W('sneakily','/ˈsniːkɪli/','偷偷摸摸地；暗中耍巧地',
 '同样是拿一块饼干，公开伸手和趁人转身偷偷拿，方式不同；后者就能用 sneakily 修饰。',
 'sneaky 改 y 为 i，加副词 -ly → sneakily；最后仍是完整 -ly，不把整个 -ily 当另一个词根。',SNEAKY+[['sneaky → sneakily','把偷偷摸摸的性质变成做事方式']],
 'sneakily take something 偷偷拿某物；sneakily change a rule 暗中改规则。',
 'smile sneakily 带点狡黠地笑；sneakily add another spoonful。',
 'quietly 只说安静，sneakily 还带避开别人注意的意图；安静做事不一定是在偷偷做。',
 ('He sneakily took the largest slice of cake.','他偷偷挑走了最大的一块蛋糕。'),('She sneakily added her favourite song to the playlist.','她悄悄把自己最爱的歌添进了播放列表。'),sources=S('sneakily','sneaky'))
STEALTHY=[['与 steal 同族的中古英语 stelthe → stealth','旧偷窃义扩到秘密、难被察觉的行动；更早古英语名词为推定形式'],['stealth + -y → stealthy','把不容易惊动别人、被别人察觉的方式当作性质'],['stealthy 的程度、方式和性质扩展','stealthier、stealthiest；stealthily；stealthiness']]
W('stealthy','/ˈstelθi/','悄无声息的；隐蔽、不易察觉的',
 '猫已经靠近了，老鼠还没察觉；人放轻每一步，尽量不引起注意，这样的动作或行动者叫 stealthy。',
 'stealth + 形容词 -y；stealth 属 steal 的旧抽象名词词族，但现代 /stelθ/ 的元音不是 steal 的 /iː/。',STEALTHY,
 'stealthy movements 悄无声息的动作；a stealthy approach 隐蔽接近；a stealthy animal 行动不易被察觉的动物。',
 'a stealthy step；make a stealthy exit 悄悄离开。',
 'stealthy 侧重避免被察觉，sneaky 更容易带不诚实、耍小聪明的评价；猫 stealthy 不一定是在做人类意义的坏事。',
 ('The cat approached with slow, stealthy movements.','猫用缓慢而悄无声息的动作靠近。'),('We made a stealthy exit while everyone was watching the stage.','大家看着舞台时，我们悄悄离开了。'),sources=S('stealthy','stealthy'))
W('stealthier','英 /ˈstelθiə/；美 /ˈstelθiər/','更隐蔽的；更悄无声息的',
 '同样靠近一个目标，这次动作更轻、更少暴露自己，就是 stealthier。它比较的是被察觉的难易。',
 'stealthy 改 y 为 i，加完整比较级 -er；较早基础为 stealth + -y。',STEALTHY+[['stealthy → stealthier','比较行动的隐蔽、不易察觉程度']],
 'a stealthier approach 更隐蔽的接近方式；become stealthier 变得更难察觉。',
 'stealthier than before；a stealthier animal。',
 'stealthier 不是简单等于 quieter；少出声只是隐蔽的一种方式，减少显眼的动作也可能让行动更 stealthy。',
 ('The cat chose a stealthier approach through the long grass.','猫选了一条更隐蔽的接近路线，从长草里穿过去。'),('Her second attempt was slower but stealthier.','她第二次尝试更慢，但更不容易被察觉。'),sources=S('stealthier','stealthy'))
W('stealthiest','/ˈstelθiɪst/','最隐蔽的；最悄无声息的',
 '几个行动者里，最会不惊动别人就靠近的那个，可以叫 the stealthiest；比较的是隐藏行动的能力。',
 'stealthy 改 y 为 i，加完整最高级 -est；/θ/ 后接 /iɪst/，不省掉基础辅音。',STEALTHY+[['stealthy → stealthiest','在范围内隐蔽程度最高、最难被察觉']],
 'the stealthiest approach 最隐蔽的接近方式；one of the stealthiest animals 最善于隐蔽行动的动物之一。',
 'the stealthiest player；the stealthiest route。',
 'stealthiest 需要比较范围，不是绝对保证永远没人发现；句子是在说谁、哪种方式相对最隐蔽。',
 ('She was the stealthiest player in our game of hide and seek.','在我们玩的捉迷藏里，她最能悄无声息地行动。'),('He looked for the stealthiest way to reach the biscuit tin.','他想找一个最不引人注意的办法靠近饼干盒。'),sources=S('stealthiest','stealthy'))
W('stealthily','/ˈstelθɪli/','悄无声息地；隐蔽地',
 '不是仅仅声音低，而是整个动作尽量不让别人察觉，比如放轻脚步从旁边靠近，叫 stealthily。',
 'stealthy 改 y 为 i，加副词 -ly → stealthily；修饰动作的进行方式。',STEALTHY+[['stealthy → stealthily','以不易被察觉的方式做事']],
 'move stealthily 悄悄移动；approach stealthily 隐蔽靠近；slip stealthily out 悄无声息地溜出。',
 'stealthily open the door；stealthily follow someone。',
 'silently 只强调没有声音，stealthily 还强调避开注意；一个人可以无声却大摇大摆地走，不一定 stealthily。',
 ('The fox moved stealthily along the hedge.','狐狸沿树篱悄无声息地移动。'),('She stealthily opened the door and peeked inside.','她悄悄打开门，往里看了一眼。'),sources=S('stealthily','stealthy'))
W('stealthiness','/ˈstelθinəs/','隐蔽性；悄无声息、不易察觉的程度',
 '不再说某一个动作，而是把“不容易让人察觉”这项特点拿出来讨论，就用 stealthiness。',
 'stealthy 改 y 为 i，加性质名词 -ness；stealth → stealthy → stealthiness，分清基础行动名词与形容词的性质名词。',STEALTHY+[['stealthy → stealthiness','把隐蔽、悄无声息的性质作为讨论对象']],
 'the stealthiness of its movements 它行动的隐蔽性；rely on stealthiness 靠不易察觉的特点。',
 'speed and stealthiness 速度与隐蔽性；the animal’s stealthiness。',
 'stealth 更常直接说隐蔽行动、秘密手段；stealthiness 更像点名某物的隐蔽特点，在比较特征时使用。',
 ('The camera revealed the surprising stealthiness of the fox.','摄像头让人看清了狐狸行动有多么隐蔽。'),('The game rewards stealthiness rather than speed.','这个游戏奖励的是行动隐蔽，而不是速度快。'),sources=S('stealthiness','stealthy'))
FURTIVE=[['拉丁语 fur 小偷 → furtum 偷窃 → furtivus 偷来的、隐秘的','这里的拉丁 fur 与英语 fur 皮毛不是同一个来源'],['法语 furtif 等 → 英语 furtive → furtiveness','偷偷摸摸、遮掩的性质，现代不要求真的偷了东西']]
W('furtiveness','英 /ˈfɜːtɪvnəs/；美 /ˈfɝːtɪvnəs/','鬼鬼祟祟、偷偷摸摸的样子；遮掩的神态',
 '说话前先四处看，东西往身后藏，行动像不想让别人知道；把这种遮遮掩掩的样子当成一个特点，就叫 furtiveness。',
 'furtive + -ness，保留不发音 e；前面经法语接拉丁 furtivus、furtum、fur 的偷窃词族。',FURTIVE,
 'an air of furtiveness 一种遮遮掩掩的神态；the furtiveness of someone’s movements 某人鬼鬼祟祟的动作样子。',
 'a sense of furtiveness；furtiveness in his manner。',
 'privacy 是保留私人空间、信息；furtiveness 写躲避别人注意的神态，语气通常更可疑。',
 ('There was an odd furtiveness in his manner.','他的神态有种奇怪的遮掩感。'),('The furtiveness of her glance made me curious.','她偷偷瞥的那一下，让我好奇起来。'),sources=S('furtiveness','furtive'))
SKULK=[['中古英语 skulken → skulk','接北欧躲藏、悄行、逃避责任等相关材料'],['藏着躲着地行动 → 可疑地躲在某处、偷偷避开事情','现代常带不赞成的语气；不把它与 skull 头骨作字母上的牵强联系']]
W('skulk','/skʌlk/','鬼鬼祟祟地躲着；偷偷摸摸地走动；躲懒',
 '不光是安静，而是缩在角落、藏着不露面，好像在躲人或躲事，这种让旁人觉得可疑的状态可以叫 skulk。',
 '承中古英语 skulken，接北欧躲藏、逃避行动的相关词；现代常用在责怪某人藏着不出来的句子里。',SKULK,
 'skulk around 在附近鬼鬼祟祟地晃；skulk in the corner 躲在角落里；skulk away 偷偷溜开。',
 'stop skulking 别再躲躲藏藏；skulk behind the door。',
 'lurk 可以只是隐存、不露面，skulk 往往带更明显的责怪：为什么藏着、鬼鬼祟祟地不出来。',
 ('There is no need to skulk in the doorway; come in.','别躲在门口了，进来吧。'),('He tried to skulk away before the cleaning began.','开始打扫前，他想偷偷溜走。'),sources=S('skulk','skulk'))
W('skulks','/skʌlks/','鬼鬼祟祟地躲着、走动；躲懒〔第三人称单数〕',
 '该露面的时候，他却总在边上藏着，像怕被看见或怕被叫去干活，动词用 skulks。',
 'skulk + -s，/k/ 后读 /s/，结尾 /lks/；基础词中的 u 读 /ʌ/。',SKULK+[['skulk + -s → skulks','他、她躲躲藏藏、不愿露面']],
 'skulks in the shadows 躲在暗处；skulks around the back gate 在后门附近鬼鬼祟祟地晃。',
 'skulks away from the group；skulks behind the shed。',
 'skulks 描写时带说话人的态度，不能只凭用了这个动词就断定那个人真的在犯罪或偷东西。',
 ('He skulks at the back whenever volunteers are needed.','每次需要志愿者，他就缩在后面躲着。'),('The cat skulks behind the shed after knocking over the pot.','猫碰倒花盆后，就躲到棚子后面去了。'),sources=S('skulks','skulk'))
W('skulked','/skʌlkt/','鬼鬼祟祟地躲着、走动了；偷偷溜开了',
 '刚才没有光明正大地走开，而是藏着、躲着从边上离开，用 skulked 会把这种可疑、畏缩的样子写出来。',
 'skulk + 完整 -ed，/k/ 后词尾读 /t/，结尾 /lkt/；不额外添 /ɪd/。',SKULK+[['skulk + -ed → skulked','过去躲藏、悄行或避开事情']],
 'skulked away 偷偷溜走；skulked at the back 缩在后面；skulked around outside 在外头鬼鬼祟祟地晃。',
 'skulked behind the curtain；skulked back to his room。',
 'slunk away 也能写心虚地溜走；skulked 更常把躲藏、回避或鬼鬼祟祟的状态突出出来。',
 ('He skulked away before anyone could ask him to help.','没等谁开口叫他帮忙，他就偷偷溜走了。'),('We skulked at the back, hoping not to be called on.','我们缩在后面躲着，希望别被叫到。'),sources=S('skulked','skulk'))
W('skulking','/ˈskʌlkɪŋ/','正在躲躲藏藏、鬼鬼祟祟地走动；躲懒',
 '人一直在附近，却躲在边上不出来，别人看见了就可能说 stop skulking around：别再鬼鬼祟祟地晃了。',
 'skulk + -ing，保留基础 /lk/；可作进行形式，也可直接形容躲藏、悄行的人。',SKULK+[['skulk + -ing → skulking','正在躲躲藏藏；也把这种样子作修饰语']],
 'skulking around the house 在屋子附近鬼鬼祟祟地晃；a skulking figure 一个躲躲藏藏的人影。',
 'caught someone skulking；skulking in a corner。',
 'skulking 的不赞成感通常比 resting 强得多；普通休息不会仅因不动就自动成为 skulking。',
 ('Why are you skulking in the corridor instead of coming in?','你为什么不进来，反而在走廊里躲躲藏藏？'),('I saw someone skulking behind the garden wall.','我看见有人鬼鬼祟祟地躲在花园墙后。'),sources=S('skulking','skulk'))
PROWLER=[['中古英语 prollen → prowl：四处潜行搜寻','基础词更早来源未定'],['prowl + -er → prowler','把游走搜寻的动作变成行动者；用于人时常带可疑、暗中窥探的感觉']]
W('prowler','英 /ˈpraʊlə/；美 /ˈpraʊlər/','暗中游荡、窥探的人；游走觅食的动物',
 '夜里在屋外转来转去、像在找机会的人，可以叫 a prowler；动物一带一带寻找猎物，也能这样称呼。',
 'prowl + 人物、行动者后缀 -er；它点名做这个动作的对象，基础 prowl 的来源未定。',PROWLER,
 'a prowler outside the house 房子外暗中游荡的人；a nocturnal prowler 夜间游走觅食的动物、行动者。',
 'spot a prowler；a prowler in the garden。',
 'passerby 只是经过的人；prowler 会让人感觉对方正在附近搜寻、窥探，语气更可疑。',
 ('The camera caught a prowler near the back door.','摄像头拍到有人在后门附近暗中游荡。'),('The fox is a patient nocturnal prowler.','狐狸是耐心的夜间游猎者。'),sources=S('prowler','prowl'))
W('prowlers','英 /ˈpraʊləz/；美 /ˈpraʊlərz/','暗中游荡、窥探的人；游走觅食的动物〔复数〕',
 '不止一个人在暗处四处转、找目标，或有几只夜间觅食动物，这些对象合起来叫 prowlers。',
 'prowl + -er → prowler，再加复数 -s，词尾读 /z/；不是动词三单，动词三单是 prowls。',PROWLER+[['prowler + -s → prowlers','多个暗中游走、寻找目标的行动者']],
 'night prowlers 夜间游荡、觅食的行动者；keep prowlers away 防止可疑游荡者靠近。',
 'prowlers around the building；a pair of nocturnal prowlers。',
 'prowlers 写行动者，prowls 可以是动词三单或活动名词复数；多了 -er，视角从做什么转到谁在做。',
 ('The lights switch on when prowlers approach the gate.','有人暗中游荡到门边时，灯就会亮起。'),('The camera revealed several nocturnal prowlers in the garden.','摄像头拍到了花园里几只夜间游走觅食的动物。'),sources=S('prowlers','prowl'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfw',ROOTS,WORDS)
 extend_lessons()
