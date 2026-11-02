"""Wine makers, kinds of writers and things that drive."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
WI=[['拉丁 vīnum → 早期日耳曼语借词 → 古英语 wīn → wine','葡萄酒；英语保留早期借入的酒名']]
W('winemaker','英 /ˈwaɪnmeɪkə/；美 /ˈwaɪnmeɪkər/','葡萄酒酿造者、酿酒师',
 '把葡萄、发酵与后续处理变成一款酒的人或酿造方。不是只会倒酒、推荐酒的服务人员。',
 'wine 葡萄酒 + maker 制作者；中古英语已有 wynmaker 等写法。可以说现代组合，也保留很早的复合词历史。',WI+[['wine + maker → 中古英语 wynmaker → winemaker','制作葡萄酒的人']],
 'a local winemaker 当地酿酒师，an experienced winemaker 有经验的酿酒师，meet the winemaker 见酿酒者。',
 'a local winemaker；an experienced winemaker；meet the winemaker。',
 'winemaker 酿酒，winegrower 栽培酿酒葡萄，sommelier 侍酒师常负责选酒与服务；一个人可兼任，但名称侧重点不同。',
 ('The winemaker explained how the grapes were selected.','酿酒师解释了怎样挑选葡萄。'),('Several local winemakers took part in the festival.','几位当地酿酒师参加了节庆活动。'))
W('wino','英 /ˈwaɪnəʊ/；美 /ˈwaɪnoʊ/','酒鬼〔俚语，通常带贬义〕',
 '把人贴上老喝酒、喝得失控的标签，口气不客气；不是爱品葡萄酒者的中性职业名。',
 'wine + 人物名词尾 -o，形成俚语称呼。另有粒子物理学同形 wino，来自 W 与 -ino 的命名，读音、来源另辨，不并入酒义。',WI+[['wine + -o → wino','常饮酒者的贬义俚称']],
 'a wino 常见于小说、旧报道或人物对白，可能带污名。阅读知道意思即可，称呼真实的人更宜用具体、尊重的说法。',
 'a wino；the word wino；a character called a wino。',
 'wine lover 爱酒者中性得多，wino 通常贬义；不要把所有喝葡萄酒的人都叫 wino。',
 ('The narrator dismisses the old man as a wino.','叙述者轻蔑地把老人叫作酒鬼。'),('The editor replaced wino with a more respectful description.','编辑把 wino 换成了更尊重人的描述。'))
R('B2903','葡萄酒与酿造、酿造场所及人物称呼','WINE：酒名是早期借词，后面再长出酿造这一组','wine → winery、winemaking、winemaker；wino 作为阅读中须识别语气的俚称放在最后。',
 'winemaker 是酿酒者，winery 是酿酒场所、企业，winemaking 是酿酒活动。wino 贬义不用于中性赞美品酒爱好。',
 '拉丁 vīnum 经早期日耳曼语进入古英语 wīn；wine + -ery、making、maker、-o 分别产生场所、活动、人物等词。',
 [['基础词与酿造','wine · winery · winemaking · winemaker'],['人物俚称','wino']],
 'wine 与 win 拼写近但不是从赢加 e；winemaker/酒窖服务人员不同；wino 非 wine lover 的中性替换。',
 'The winemaker showed us around the winery.\n\n酿酒师带我们参观了酒庄。','wine winery winemaking winemaker wino')
WR=[['古英语 wrītan → write','刻写、写'],['write + -er → writer','从事写作的人']]
W('ghostwriter','英 /ˈɡəʊstraɪtə/；美 /ˈɡoʊstraɪtər/','代笔者、代笔作家',
 '真正把文字写出来的人，作品主要以别人的名字出现；ghost 借看不见的身影来表现幕后写作。',
 'ghost 幽灵、隐身的存在 + writer 作者，合成幕后代笔者的名称。两个材料并列组合，不是 ghost 先变成 writer。',WR+[['ghost + writer → ghostwriter','在署名者背后写作的人']],
 'hire a ghostwriter 雇代笔者，work with a ghostwriter 与代笔者合作，a memoir’s ghostwriter 回忆录代笔者。合作可以公开承认，不保证永远没人知道。',
 'hire a ghostwriter；work with a ghostwriter；a memoir’s ghostwriter。',
 'ghostwriter 代笔侧重实际写作与主要署名者分离；editor 编辑侧重整理修改，coauthor 合著者通常共同署名，具体工作仍可重叠。',
 ('She worked with a ghostwriter on her memoir.','她和一位代笔作家合作完成回忆录。'),('The ghostwriter interviewed him before drafting the first chapter.','代笔作家先采访了他，再起草第一章。'))
W('speechwriter','英 /ˈspiːtʃraɪtə/；美 /ˈspiːtʃraɪtər/','演讲稿撰写人',
 '替发言人把要说的话整理成能讲给听众听的稿子；speech 在这里是一场讲话，不是语言能力本身。',
 'speech 演讲 + writer 撰稿者，按写作对象命名。说话的人与写稿的人可以不同。',WR+[['speech + writer → speechwriter','以演讲稿为工作对象的写作者']],
 'a political speechwriter 政治演讲稿撰写人，the chief speechwriter 首席演讲撰稿人，work as a speechwriter 做演讲撰稿工作。',
 'a political speechwriter；the chief speechwriter；work as a speechwriter。',
 'speechwriter 写稿，speaker 演讲者；speechwriter 可做代笔，但词本身只说稿件类型，不保证署名、合作方式。',
 ('The speechwriter revised the opening paragraph.','演讲撰稿人修改了开头一段。'),('A good speechwriter thinks about how the words will sound aloud.','好的演讲撰稿人会考虑文字念出来是什么感觉。'))
R('B2582','写作者与按作品、协作方式分出的角色','WRITER：先看写什么，再看以谁的名字出现','writer 为基础；songwriter、screenwriter、scriptwriter、copywriter、speechwriter 按作品分；ghostwriter 按合作角色分；typewriter 是器物支线。',
 '不要看到 -writer 就全译作家：广告文案、演讲稿、剧本各有对象，typewriter 更是打字机。ghostwriter 的幕后关系也不等于所有合作都秘密。',
 'write + -er；作品名 + writer；ghost + writer；typewriter 中 -writer 指写出文字的机器。',
 [['基础角色','writer'],['按作品区分','songwriter · screenwriter · scriptwriter · copywriter · speechwriter'],['按协作区分','ghostwriter'],['机器名称','typewriter']],
 'writer/speaker 写与讲；ghostwriter/editor 代笔与编辑；screenwriter 与 scriptwriter 范围重叠但作品场景不同。',
 'The speechwriter and the speaker reviewed the draft together.\n\n演讲撰稿人与演讲者一起审阅了草稿。','writer songwriter screenwriter scriptwriter copywriter speechwriter ghostwriter typewriter')
D=[['古英语 drīfan → drive','驱使向前、赶动'],['drive + -er → driver','驱动的人或物；司机']]
W('driverless','英 /ˈdraɪvələs/；美 /ˈdraɪvərləs/','无人驾驶的、没有司机的',
 '车里没有坐着负责驾驶的司机；-less 拿掉的是 driver，不是车没动力、没法移动。',
 'driver + -less，表示没有驾驶员。现代常用于自动驾驶车辆，也可只描述某一刻无人驾驶的状态，须看上下文。',D+[['driver + -less → driverless','没有驾驶员的']],
 'a driverless train 无人驾驶列车，a driverless car 无人驾驶汽车，driverless technology 无人驾驶技术。',
 'a driverless train；a driverless car；driverless technology。',
 'driverless 描述没有司机，不直接保证是哪级自动化、更不自动保证任何情况下都安全；automatic 自动也未必说整车无人驾驶。',
 ('The airport uses a driverless train between terminals.','机场用无人驾驶列车连接航站楼。'),('The article discusses public attitudes toward driverless cars.','文章讨论公众对无人驾驶汽车的态度。'))
W('screwdriver','英 /ˈskruːdraɪvə/；美 /ˈskruːdraɪvər/','螺丝刀；螺丝起子；同名鸡尾酒',
 '让螺丝旋进、旋出的工具。driver 不只赶车的人，也可把某物推进去的器具。',
 'screw 螺丝 + driver 驱动器具，合成工具名。酒名是后来同形用法，常指伏特加加橙汁，不靠某个未经确证的酒吧故事来硬解释命名。',D+[['screw + driver → screwdriver','驱动螺丝的工具；后来也作酒名']],
 'a Phillips screwdriver 十字螺丝刀，a flathead screwdriver 一字螺丝刀，tighten a screw with a screwdriver 用螺丝刀拧紧螺丝。',
 'a Phillips screwdriver；a flathead screwdriver；use a screwdriver。',
 'screwdriver 拧螺丝，wrench/spanner 常拧螺母、螺栓；driver 在工具名里不必是人。',
 ('She tightened the loose screw with a screwdriver.','她用螺丝刀拧紧了松动的螺丝。'),('There is a small screwdriver in the toolbox.','工具箱里有一把小螺丝刀。'))
W('piledriver','英 /ˈpaɪlˌdraɪvə/；美 /ˈpaɪlˌdraɪvər/','打桩机；猛烈的一击〔比喻〕；摔角动作名',
 '把长桩向地下打进去的机器；pile 在这里是承重用的桩，driver 是把它驱入的东西。',
 'pile 桩 + driver 打入器具，合成工程机器名。也见分写 pile driver；这里保留不带连字符的词头。体育、口语可借强烈向下冲击的形象。',D+[['pile〔桩〕+ driver → piledriver','把桩打入地面的机器；再有猛烈冲击的比喻']],
 'a piledriver on the construction site 工地打桩机，the noise of a piledriver 打桩机噪声；报道中 a piledriver of a shot 可形容势大力沉的射门。',
 'a piledriver；the noise of a piledriver；a piledriver of a shot。',
 'pile 在此不是 a pile of books 一堆书；driver 在此是机器，不能译为开一堆东西的人。',
 ('We could hear the piledriver from the construction site.','我们能听见工地打桩机的声音。'),('The engineer checked the position of the piledriver.','工程师检查了打桩机的位置。'))
R('B3803','驾驶员与让物体动起来的器具','DRIVER：使什么向前动，就在“驱动”什么','driver → driverless；screwdriver、piledriver 展示 driver 也可以是工具、机器。',
 '驾驶只是 drive 的一个常见应用。驱动因素、软件驱动和把螺丝、桩推入的工具，都能从使东西行动这层看清。',
 'drive + -er；driver + -less；screw/pile + driver，合成词两项材料并列。',
 [['人物和无驾驶员状态','driver · driverless'],['驱动物体的工具','screwdriver · piledriver']],
 'driver 不限人；driverless 非没有动力；piledriver 的 pile 是桩，screwdriver 的酒名不强编唯一故事。',
 'The driver left a screwdriver in the toolbox.\n\n司机把一把螺丝刀放在工具箱里。','driver driverless screwdriver piledriver')
if __name__=='__main__':save('continuation_20261030_dc',ROOTS,WORDS)
