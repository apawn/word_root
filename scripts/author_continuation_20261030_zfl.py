"""Twisting, restricted walking and movement away from balance."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A2238':dict(words='wriggle wriggles wriggled wriggling shuffle shuffles shuffled shuffling hobble hobbles hobbled hobbling'.split(),label='wriggle、shuffle、hobble：各有来源的重复小动作',note='wriggle 借低地德语扭动材料；shuffle 可能接 shove 的旧反复形式，也有低地德语来源说；hobble 或联系 hop 的反复形式。各词近源分开，不把任何 -le 都当成同一条确定派生。'),
 'B3499':dict(words='hop hobble hobbles hobbled hobbling'.split(),label='hobble 与 hop 的可能联系',note='hobble 较早说摇动，可能借或同源于荷兰语、德语相关材料，也可能联系 hop 的反复形式；束住牲畜腿的支线或由 hopple 变来。'),
 'B4358':dict(words='shove shuffle shuffles shuffled shuffling'.split(),label='shuffle 与 shove 的推移材料',note='shuffle 可能接 shove 的旧反复形式，或借低地德语；现代洗牌、拖步与重排不是现代 shove 随意换几个字母造出的。'),
 'B2998':dict(words='swing sway sways swayed swaying'.split(),label='sway、swing 的摆动材料比较',note='sway 可能借北欧的弯、摆材料并合入英语同族形式，与 swing 的更远联系仍属分析；摆动、影响、支配按现代用法分别理解。'),
 'A1760':dict(words='wriggle wriggles wriggled wriggling squirm squirms squirmed squirming hobble hobbles hobbled hobbling shuffle shuffles shuffled shuffling stagger staggers staggered staggering lurch lurches lurched lurching sway sways swayed swaying teeter teeters teetered teetering'.split(),label='扭动、拖步、踉跄与摇摆的现代变化',note='本组 -ed 多读 /d/；lurched 的 /tʃ/ 后读 /t/。staggered 可说踉跄、震惊或错开安排，须结合宾语辨义。'),
}
WRIGGLE=[['低地德语 wrigglen → 英语 wriggle','短促、反复地扭转；较远联系转、弯的材料'],['身体扭动挤出 → 想办法脱开责任、承诺','wriggle out of 的画面像扭着身子从夹住的地方钻出去']]
W('wriggles','/ˈrɪɡəlz/','扭动、扭着钻行〔第三人称单数〕；扭动动作〔复数〕',
 '小孩在怀里扭来扭去，虫子一小节一小节拧着身子，都像 wriggles。说人 wriggles out of a promise，则像从承诺里扭身钻出去。',
 'wriggle + -s，/l/ 后读 /z/；开头 w 不发音。名词复数和动词三单同形，基础词借低地德语扭转材料。',WRIGGLE+[['wriggle + -s → wriggles','它反复扭动；几次短促扭动']],
 'wriggles in her arms 是在她怀里扭，wriggles free 是扭着脱身；a few wriggles 是几下扭动。',
 'wriggles through a gap 扭着身子挤过缝；wriggles out of trouble 设法脱离麻烦。',
 'wriggles 常有身体短促扭转的形状，moves 更宽；不是所有来回移动都在 wriggle。',
 ('The baby wriggles whenever I try to dress him.','我一给宝宝穿衣服，他就扭来扭去。'),('A worm wriggles through the wet soil.','一条蚯蚓扭动着钻过湿土。'),sources=S('wriggles','wriggle'))
W('wriggled','/ˈrɪɡəld/','扭动了；扭着钻出、挤过了；设法摆脱了',
 '身体弯着扭着，从窄缝里钻出来，是 wriggled；责任像套住人的绳子，wriggled out of it 就是想办法逃开。',
 'wriggle 去末尾 e + 完整 -ed → wriggled，/l/ 后读 /d/；原有 gg 保留，不再增写。',WRIGGLE+[['wriggle 去 e + -ed → wriggled','过去反复扭动或扭着脱身']],
 'wriggled out of his grasp 是扭身挣脱他的抓握，wriggled under the fence 是扭着钻过围栏下面；比喻用法也常接 out of。',
 'wriggled free 扭动脱身；wriggled through a hole 扭着钻过洞。',
 'wriggled 强调扭曲身体的小动作，ran away 强调跑开；逃开同一个地方，镜头关注点不同。',
 ('The kitten wriggled out of my arms.','小猫扭着身子，从我怀里挣出去了。'),('He wriggled out of helping with the cleaning.','他找借口躲掉了帮忙打扫的事。'),sources=S('wriggled','wriggle'))
W('wriggling','/ˈrɪɡəlɪŋ/','正在扭动、扭着钻行；扭来扭去的',
 '抱着的小狗一直拧身体，虫子在手心弯来弯去，是 wriggling；画面小而连续，不像整个物体平平地滑动。',
 'wriggle 去末尾 e + 完整 -ing → wriggling；发音中保留 /ɡ/，开头 w 仍不发音。',WRIGGLE+[['wriggle 去 e + -ing → wriggling','短促反复扭动的过程']],
 'a wriggling puppy 是扭来扭去的小狗，wriggling through a gap 是扭身挤过缝隙；也可说 wriggling out of a promise。',
 'wriggling on the hook 在钩上扭动；wriggling under a blanket 在毯子下扭动。',
 'wriggling 常能直接看见身体在拧；squirming 也能扭，却更常用来写不舒服、难堪得坐立不安。',
 ('She tried to hold the wriggling puppy still.','她试着抱稳那只扭来扭去的小狗。'),('The child was wriggling under the blanket.','孩子正在毯子下面扭动。'),sources=S('wriggling','wriggle'))
SQUIRM=[['十七世纪方言 squirm','早期说鳗鱼等扭动；来源未定，或有拟声基础'],['身体扭来扭去 → 心里难受、难堪得不自在','比喻像内心也在扭动，坐不住、想避开眼前处境']]
W('squirm','英 /skwɜːm/；美 /skwɜːrm/','扭动、蠕动；难堪或不舒服得坐立不安',
 '椅子上坐得不舒服，孩子屁股挪来挪去、身体扭着，是 squirm。被当众问到难堪问题，心里也像这样扭着想逃。',
 '较早是说鳗鱼扭动的方言词，来源不确定；有人联系 worm、swarm，也有拟声说，不能写成确定的混成拆法。',SQUIRM,
 'squirm in a seat 是在座位上扭动，squirm with embarrassment 是难堪得浑身不自在；后者未必真有大幅动作。',
 'make someone squirm 使人难堪不安；squirm under questioning 在追问下坐立不安。',
 'squirm 和 wriggle 都能扭动，squirm 更常带不舒服、尴尬；wriggle 更容易让人看见身体扭转、钻过的动作。',
 ('The child began to squirm in the hard chair.','孩子坐在硬椅子上，开始扭来扭去。'),('The question made him squirm with embarrassment.','那个问题让他难堪得坐立不安。'),sources=S('squirm','squirm'))
W('squirms','英 /skwɜːmz/；美 /skwɜːrmz/','扭动、蠕动、难堪不安〔第三人称单数〕；扭动动作〔复数〕',
 '一个孩子在椅子上挪来扭去，或一个人被提到糗事就不自在，用 squirms。难堪用法像把心里的别扭变成身体动作。',
 'squirm + -s，/m/ 后读 /z/；常见动词三单，也可用名词复数说几下扭动。',SQUIRM+[['squirm + -s → squirms','他、她扭动；他、她难堪不安']],
 'squirms in his seat 是在座位上扭，squirms when questioned 是被问时很不自在；能写动作，也能写心理反应。',
 'squirms with embarrassment 难堪得不安；squirms out of reach 扭身躲开。',
 'squirms 比 feels embarrassed 更有身体不安的画面；但比喻语境里无需真的看到人一直扭腰。',
 ('The baby squirms when her brother tries to hold her.','哥哥想抱宝宝时，她就扭来扭去。'),('He squirms whenever anyone mentions that old mistake.','谁一提起那个旧错误，他就浑身不自在。'),sources=S('squirms','squirm'))
W('squirmed','英 /skwɜːmd/；美 /skwɜːrmd/','扭动了；难堪、不舒服得坐立不安了',
 '刚才坐不稳似的挪动身体，或回想当时被问得很不自在，是 squirmed。能写真实扭动，也能把心理难受写得可见。',
 'squirm + 完整 -ed，/m/ 后读 /d/；rm 保留，直接加词尾。',SQUIRM+[['squirm + -ed → squirmed','过去扭动、感到难堪不安']],
 'squirmed in her chair 是在椅子上扭，squirmed under his stare 是被他盯得浑身不自在；介词短语可交代位置或原因。',
 'squirmed with discomfort 不舒服得扭动；squirmed at the memory 想起时难堪不安。',
 'squirmed 强调不安或扭动过程，flinched 更像被惊到时一缩；前者可以持续更久。',
 ('She squirmed in her chair as the meeting dragged on.','会议拖个没完，她在椅子上扭来扭去。'),('He squirmed when the interviewer played the old recording.','采访者播放旧录音时，他难堪得浑身不自在。'),sources=S('squirmed','squirm'))
W('squirming','英 /ˈskwɜːmɪŋ/；美 /ˈskwɜːrmɪŋ/','正在扭动、蠕动；难堪不安的',
 '身体正因不舒服或想挣脱而扭，叫 squirming；被当众追问的人也像坐不稳，心里只想让这一刻赶紧过去。',
 'squirm + 完整 -ing，直接加；rm 后不双写 m，分词可描述动作或难堪状态。',SQUIRM+[['squirm + -ing → squirming','扭动过程；心理上难堪不自在']],
 'a squirming child 是扭来扭去的孩子，leave someone squirming 是使人难堪不安；原因可以是尴尬话题或不舒服环境。',
 'squirming in the seat 在座位上扭动；squirming with embarrassment 难堪得不自在。',
 'squirming 常带不舒服的感觉，wiggling 可以只是轻松晃动；小孩得意晃脚不一定在难堪或想挣脱。',
 ('The squirming toddler refused to sit still.','那个扭来扭去的小孩不肯坐好。'),('The awkward silence left everyone squirming.','那阵尴尬的沉默让大家都浑身不自在。'),sources=S('squirming','squirm'))
HOBBLE=[['中古英语 hoblen 的摇动材料 → hobble','或借、或同源于荷兰语和德语相关词，也有 hop 反复形式的分析'],['不稳地走 → 束腿的相关支线 → 限制、拖住','束腿义可能由旧 hopple 形式变来；现代阻碍比喻像脚被牵住']]
W('hobble','英 /ˈhɒbəl/；美 /ˈhɑːbəl/','蹒跚、跛行；束住牲畜腿；限制、妨碍；束腿绳具',
 '脚不灵便，一步一步艰难挪，是 hobble。把牲畜腿拴住，限制它走远，也叫 hobble；资金不够让项目迈不开步，同样能 hobble it。',
 '中古英语 hoblen 先有摇动义，近源有借德荷材料或联系 hop 的不同分析；束腿义或由旧 hopple 形式变来，不把所有记录压成单线。',HOBBLE,
 'hobble across the room 是艰难挪过房间，hobble a horse 是用绳具束住马腿；hobble progress 是使进展受阻。',
 'hobble along 跛着挪动；a hobble on progress 对进展的束缚。',
 'limp 更突出步态一瘸一拐，hobble 常更有走得艰难、受限制的感觉；现代两者也能描述同一次移动。',
 ('He had to hobble back to the car.','他只好一瘸一拐地挪回车旁。'),('A lack of spare parts could hobble the repair work.','缺少备件可能拖住修理工作。'),sources=S('hobble','hobble'))
W('hobbles','英 /ˈhɒbəlz/；美 /ˈhɑːbəlz/','蹒跚、跛行、限制〔第三人称单数〕；牲畜束腿绳具〔复数〕',
 '人走得不利索，缓慢挪过去，是 hobbles；一个障碍拖住整件事，也像给它脚上套了绳具。绳具本身可用名词复数。',
 'hobble + -s，/l/ 后读 /z/；末尾 e 留着，名词复数与动词三单同形。',HOBBLE+[['hobble + -s → hobbles','他、她艰难挪行；它拖住；多副束腿绳具']],
 'hobbles to the door 是一瘸一拐挪向门，hobbles the work 是阻碍工作；hobbles for horses 是马用束腿绳具。',
 'hobbles on crutches 拄拐艰难走；hobbles further progress 阻碍进一步进展。',
 'hobbles the project 有“让它迈不开步”的比喻感；delays the project 只保证延迟，未必强调能力一直受限。',
 ('He hobbles to the gate with a stick.','他拄着棍子，一瘸一拐挪到大门口。'),('The shortage of equipment hobbles the whole team.','设备短缺拖住了整个团队。'),sources=S('hobbles','hobble'))
W('hobbled','英 /ˈhɒbəld/；美 /ˈhɑːbəld/','蹒跚、跛行了；束住腿了；受限制、被拖住的',
 '刚才艰难挪过去，是 hobbled；项目被缺钱、设备不足困住，像脚上被系住，也可说 was hobbled by something。',
 'hobble 去末尾 e + 完整 -ed → hobbled，/l/ 后读 /d/；基础的双 b 保留。',HOBBLE+[['hobble 去 e + -ed → hobbled','过去受限地走；被束腿、拖住']],
 'hobbled off 是跛着挪走，hobbled by delays 是被不断延误拖住；被动结构让限制因素作 by 后的原因。',
 'hobbled across the yard 艰难挪过院子；hobbled by shortages 受短缺限制。',
 'hobbled 不必表示完全停住：还能挪，还能干，只是能力被明显拖累；stopped 则把停止本身说出来。',
 ('She hobbled across the room to answer the door.','她一瘸一拐地挪过房间去开门。'),('The restoration project was hobbled by a shortage of materials.','修复项目被材料短缺拖住了。'),sources=S('hobbled','hobble'))
W('hobbling','英 /ˈhɒbəlɪŋ/；美 /ˈhɑːbəlɪŋ/','正在蹒跚、跛行；正在限制、拖累',
 '人正一步一步艰难挪，是 hobbling；障碍正使工作迈不开步，也可用同一个词描写受阻过程。',
 'hobble 去末尾 e + 完整 -ing → hobbling；原有 bb 不变，常见发音仍能听到 /bəl/ 一段。',HOBBLE+[['hobble 去 e + -ing → hobbling','艰难走动或限制活动的过程']],
 'hobbling down the path 是沿小路跛行，hobbling the recovery 是拖住恢复进程；一个不及物，一个带被限制的对象。',
 'hobbling towards the bench 跛着挪向长椅；a hobbling gait 蹒跚步态。',
 'hobbling 可说行动困难，也可主动限制某物；看它后面直接跟人、项目，还是跟位置，能区分句子角色。',
 ('We saw him hobbling towards the bench.','我们看见他正一瘸一拐地挪向长椅。'),('Repeated delays were hobbling the restoration work.','一次次延误正拖住修复工作。'),sources=S('hobbling','hobble'))
SHUFFLE=[['中古英语拖步、推移材料或低地德语 → shuffle','可能联系 shove 的旧反复形式，也有独立借入分析'],['小步推移、杂放 → 洗牌、调换顺序、随机播放','几张牌、人事或曲目被换动位置，现代可用同一重排画面理解']]
W('shuffle','/ˈʃʌfəl/','拖着脚走；洗牌、打乱顺序；随手翻动；重排、随机播放',
 '脚不怎么离地，一小步一小步拖着挪，是 shuffle。把牌推来混去、让原来顺序变掉，也叫 shuffle；歌曲随机播放就借这幅重排画面。',
 '可能接中古英语拖步词、shove 的反复动作材料，或借低地德语。现代 shuffle 是整词，-le 的来路不能只凭外形定成一种。',SHUFFLE,
 'shuffle along 是拖步走，shuffle the cards 是洗牌，shuffle the playlist 是打乱播放顺序；shuffle papers 也可说翻弄、挪动纸张。',
 'put the music on shuffle 把音乐设成随机播放；lost in the shuffle 在杂乱安排中被忽略。',
 'shuffle 强调小步挪移或顺序混动；sort 强调按某种规则整理，方向常相反。',
 ('Please shuffle the cards before you deal.','发牌前请先洗牌。'),('We heard someone shuffle along the corridor.','我们听见有人拖着脚沿走廊挪动。'),sources=S('shuffle','shuffle'))
W('shuffles','/ˈʃʌfəlz/','拖步走、洗牌、重排〔第三人称单数〕；拖步、洗牌动作〔复数〕',
 '一个人拖着脚挪、把牌来回混，动词用 shuffles；几次洗牌或拖步小动作，也能当名词复数说。',
 'shuffle + -s，/l/ 后读 /z/；整个基础词后加三单或复数词尾，末尾 e 不去。',SHUFFLE+[['shuffle + -s → shuffles','他、她拖步或洗牌；多次洗牌、拖步']],
 'shuffles the deck 是洗那副牌，shuffles into the room 是拖步进房；give the cards a few shuffles 是给牌洗几遍。',
 'shuffles papers 翻弄纸张；shuffles towards the door 拖步向门口挪。',
 'shuffles the cards 是动词加宾语；a few shuffles 则把一次洗牌当可数动作，词义相连而句子结构不同。',
 ('She shuffles the cards while we find our seats.','我们找座位时，她在洗牌。'),('He shuffles into the kitchen in his slippers.','他穿着拖鞋，拖步挪进厨房。'),sources=S('shuffles','shuffle'))
W('shuffled','/ˈʃʌfəld/','拖步走了；洗过牌、重排了；被打乱顺序的',
 '刚才脚贴着地慢慢挪，用 shuffled；卡牌、曲目已经换了原来的次序，也可说 shuffled。',
 'shuffle 去末尾 e + 完整 -ed → shuffled，/l/ 后读 /d/；原来的双 f 不变。',SHUFFLE+[['shuffle 去 e + -ed → shuffled','过去拖步；已混动、重排']],
 'shuffled to the door 是拖步走到门口，shuffled the papers 是翻动纸张；shuffled the songs 是把歌曲顺序打乱。',
 'shuffled into line 拖步进入队列；a shuffled deck 洗过的牌。',
 'shuffled 的拖步不一定因为跛，可能疲惫、慢吞吞或不愿走；limped 明确写一瘸一拐的步态。',
 ('He shuffled to the window to look outside.','他拖着脚挪到窗边向外看。'),('She shuffled the playlist before the party started.','聚会开始前，她打乱了播放列表的顺序。'),sources=S('shuffled','shuffle'))
W('shuffling','/ˈʃʌfəlɪŋ/','正在拖步、洗牌、重排；拖步声、翻动动作',
 '鞋底贴着地一下一下擦着走，或手里正把牌混来换去，是 shuffling；同样的小幅挪动可以发生在脚、牌或纸张上。',
 'shuffle 去末尾 e + 完整 -ing → shuffling；可作分词，也可把拖步、洗牌当一类动作。',SHUFFLE+[['shuffle 去 e + -ing → shuffling','拖步或混动、调换的过程']],
 'shuffling feet 是拖动的脚或拖步声，shuffling cards 是洗牌；a shuffling gait 是脚抬得很低的步态。',
 'the shuffling of papers 翻动纸张的声音、动作；shuffling along a queue 在队里拖步挪动。',
 'shuffling 强调贴近着推移；staggering 强调身体失去平衡、东倒西歪，脚步不一定贴地。',
 ('We heard the shuffling of feet outside the room.','我们听见房间外有拖步声。'),('She kept shuffling the cards as she talked.','她说话时一直在洗牌。'),sources=S('shuffling','shuffle'))
STAGGER=[['北欧 stakra 等不稳、推撞材料 → 中古英语 stakeren → stagger','较早说走不稳、踉跄；现代 er 不是临时加上的人物后缀'],['失去平衡 → 使人震惊；位置、时间交错安排','震惊像被冲得站不稳；错开则像脚步、排列不在同一条线上']]
W('stagger','英 /ˈstæɡə/；美 /ˈstæɡər/','踉跄、摇晃着走；使震惊；把时间、位置错开；踉跄动作',
 '东西太重，人一步东一步西地勉强走稳，是 stagger。消息让人惊得像站不稳，也能 stagger someone；上班时间分批错开则是另一条安排用法。',
 '经中古英语 stakeren 等接北欧的不稳、推撞材料；后来扩到使人震惊，以及交错排列、错时安排。现代不能拆成 stag 鹿 + -er。',STAGGER,
 'stagger under a load 是负重踉跄，stagger the start times 是把开始时间错开；the cost can stagger you 是费用高得让人震惊。',
 'stagger across the room 踉跄穿过房间；stagger the shifts 错开各班次。',
 'stagger 的动作义重在保持不了平衡，limp 重在一瘸一拐；stagger the hours 则是主动安排，不带走路意思。',
 ('He began to stagger under the weight of the boxes.','箱子太重，他开始踉跄。'),('We can stagger the lunch breaks to keep the desk staffed.','我们可以错开午休时间，让服务台一直有人。'),sources=S('stagger','stagger'))
W('staggers','英 /ˈstæɡəz/；美 /ˈstæɡərz/','踉跄、使震惊、错开安排〔第三人称单数〕；踉跄动作〔复数〕',
 '一个人重心不稳地挪，用 staggers；一个数字让人吃惊，或公司把各组时间分开，也可用它，宾语让不同画面分明。',
 'stagger + -s，读 /z/；动词三单直接接到完整基础词，动作名词也可有同形复数。',STAGGER+[['stagger + -s → staggers','他、她踉跄；它使人震惊或把安排错开']],
 'staggers towards the door 是踉跄走向门，staggers the breaks 是把休息时间错开；a figure that staggers us 是惊人的数字。',
 'staggers under the load 负重踉跄；staggers its opening times 错开开放时间。',
 'staggers 如果直接带 start times 等宾语，常说安排错开；后接 across、towards 等方向，常说人走不稳。',
 ('He staggers backwards when the heavy door swings open.','沉重的门一荡开，他就踉跄着往后退。'),('The factory staggers its lunch breaks.','工厂把午休时间分批错开。'),sources=S('staggers','stagger'))
W('staggered','英 /ˈstæɡəd/；美 /ˈstæɡərd/','踉跄了；震惊的；交错、分批错开的',
 '人刚才晃得站不稳，是 staggered；被消息惊住了，是 was staggered；几组时间不同时开始，则是 staggered times。',
 'stagger + 完整 -ed，读 /d/；可作过去式、过去分词，也形成震惊、错开安排的形容用法。',STAGGER+[['stagger + -ed → staggered','过去踉跄；受到震撼；已被错开']],
 'staggered back 是踉跄退后，staggered by the news 是被消息震惊；staggered hours 是分批错开的工时。',
 'a staggered schedule 错开安排的时间表；staggered rows 交错排列的行。',
 'staggered 常是受到冲击的人感到震惊，staggering 常是使人震惊的数字、消息；错开安排的 staggered 又是另一条义。',
 ('She was staggered by the amount of work involved.','工作量之大让她震惊。'),('We introduced staggered start times for the three groups.','我们把三个小组的开始时间错开了。'),sources=S('staggered','stagger'))
W('staggering','英 /ˈstæɡərɪŋ/；美 /ˈstæɡərɪŋ/','正在踉跄、错开安排；惊人的、令人震惊的',
 '人正晃着身子找平衡，是 staggering；一个数大到让人像被冲得站不稳，也就成了 a staggering number。',
 'stagger + 完整 -ing；分词形容词的“惊人”用法较早已见，不能把它只当今天临时拼成的现在进行。',STAGGER+[['stagger + -ing → staggering','踉跄过程；让人震惊的效果']],
 'staggering across the floor 是正踉跄走过地板，a staggering cost 是惊人的费用；staggering the arrivals 是把到达时间错开。',
 'a staggering amount 惊人的数量；staggering backwards 踉跄退后。',
 'a staggering figure 是那个数字令人吃惊，a staggered reader 是读者被惊住；两词形容的对象、受力方向不同。',
 ('He was staggering under the weight of his backpack.','背包太重，他正踉跄着走。'),('The library holds a staggering number of old maps.','图书馆收藏的旧地图数量惊人。'),sources=S('staggering','stagger'))
LURCH=[['船舶突然侧倾的航海名词 → lurch 的倾晃、猛动动词','早期有 lee-larches 等形式；更远或联系法语放松材料，尚不确定'],['leave in the lurch 的困境名词另分近源','与旧游戏输赢材料有关，不能从船晃一下直接推出这条习语史']]
W('lurch','英 /lɜːtʃ/；美 /lɜːrtʃ/','突然倾晃、猛地移动；踉跄；猛然一晃；〔习语〕困境',
 '公交车突然往前一冲，乘客跟着身子一歪，是 lurch。leave someone in the lurch 则是要紧时刻把人丢下，让对方陷入困境。',
 '倾晃义从较早航海名词发展成动词，更远来源未定；习语困境名词来自另一条旧游戏材料，不能编成“把人留在摇船上”的词源。',LURCH,
 'lurch forward 是猛地向前冲，a sudden lurch 是突然一晃；lurch from crisis to crisis 是跌跌撞撞地从一场危机挪到下一场。',
 'lurch to one side 猛地向一侧歪；leave someone in the lurch 把人撂在困境里。',
 'lurch 常有突然、失控的一下，sway 更能说连续左右摆；a lurch 不保证接下来倒地。',
 ('The bus gave a sudden lurch as it pulled away.','公交车起步时猛地晃了一下。'),('Please do not leave us in the lurch at the last minute.','请别在最后一刻把我们撂下，让我们陷入困境。'),sources=S('lurch','lurch'))
W('lurches','英 /ˈlɜːtʃɪz/；美 /ˈlɜːrtʃɪz/','突然倾晃、猛冲、踉跄〔第三人称单数〕；猛然晃动〔复数〕',
 '船、车或身体突然向一边冲一下，是 lurches；名词复数则像一下一下不平稳的猛晃。',
 'lurch + -es，/tʃ/ 后读 /ɪz/，多一个音节；动词三单和倾晃动作名词复数同形。',LURCH+[['lurch + -es → lurches','它突然倾动；多次猛晃']],
 'lurches forward 是向前猛冲，lurches from side to side 是突然左右倾晃；a series of lurches 是一连串颠晃。',
 'lurches into motion 猛地启动；sudden lurches 突然的猛晃。',
 'lurches 常把几下不平稳动作分出来，glides 则像平顺滑行；同样前进，乘坐和动作感觉完全不同。',
 ('The old lift lurches when it starts moving.','旧电梯启动时会猛晃一下。'),('We felt several sharp lurches as the boat crossed the waves.','船越过浪头时，我们感觉到几下剧烈的倾晃。'),sources=S('lurches','lurch'))
W('lurched','英 /lɜːtʃt/；美 /lɜːrtʃt/','突然倾晃、猛冲了；踉跄移动了',
 '车刚才突然往前一冲，或人身子失衡地歪出一步，是 lurched。它常抓住那一下突然变化。',
 'lurch + 完整 -ed，/tʃ/ 后读 /t/，结尾 /tʃt/；不用另加 /ɪd/ 音节。',LURCH+[['lurch + -ed → lurched','过去猛地移动、突然歪斜']],
 'lurched forward 是猛地向前冲，lurched to the left 是突然左倾；stomach lurched 可比喻胃里因惊惧等翻了一下。',
 'lurched to a halt 颠晃着停下；lurched across the room 踉跄穿过房间。',
 'lurched 更强调突然不稳的一冲，strolled 则是从容散步；两者主要区别在移动方式，不只是速度。',
 ('The train lurched forward as we found our seats.','我们找座位时，火车猛地向前一冲。'),('He lurched sideways when the deck tilted.','甲板倾斜时，他身子猛地向旁边一歪。'),sources=S('lurched','lurch'))
W('lurching','英 /ˈlɜːtʃɪŋ/；美 /ˈlɜːrtʃɪŋ/','正在突然倾晃、颠簸、踉跄；跌跌撞撞的',
 '船一次次歪，车忽快忽慢地冲，身体也跟着失衡，是 lurching；事情从麻烦跌进下一个麻烦，也能借这个不稳的移动讲。',
 'lurch + 完整 -ing，直接加；ch 的 /tʃ/ 保留，过程可以包含连续几下猛晃。',LURCH+[['lurch + -ing → lurching','突然不稳动作持续、反复发生']],
 'lurching from side to side 是猛然左右摇晃，lurching from crisis to crisis 是在一场场危机间跌撞，缺少平顺进展。',
 'a lurching bus 颠晃的公交车；lurching towards the exit 踉跄冲向出口。',
 'lurching 比 swaying 更有突然失衡、颠冲的感觉；swaying 可是音乐中平缓、有节奏的摇摆。',
 ('We held the rail as the boat kept lurching from side to side.','船不停猛地左右倾晃，我们抓住栏杆。'),('The project was lurching from one crisis to the next.','项目正跌跌撞撞地从一场危机挪到下一场。'),sources=S('lurching','lurch'))
SWAY=[['中古英语 sweien，可能来自北欧弯、摆材料 → sway','可能并入英语同族形式；与 swing 的远近关系保留不确定性'],['摇摆、倾向一边；影响、支配等分支','现代可用让人改变方向来理解说服，但不能据此编出每条名词的唯一先后']]
W('sway','/sweɪ/','摇摆、使摇摆；影响、说动；摇摆动作；支配、影响力',
 '树枝随风左右摆，是 sway；一句话让立场往另一边偏，也能 sway someone。hold sway 则像握住方向盘，表示占支配地位。',
 '接中古英语 sweien，可能借北欧语弯、摆材料，与 swing 一系可比较。控制名词义另有欧洲相关用法背景，不能只当现代“说动”动词转出的结果。',SWAY,
 'sway in the breeze 是随微风摇摆，sway an opinion 是影响看法，hold sway 是起支配作用，under the sway of 是受某种力量影响。',
 'sway from side to side 左右摇摆；sway the decision 影响决定。',
 'sway someone 可影响其判断、使其改主意，force someone 则明确强迫；被说动不必有人施加命令。',
 ('The tall grass began to sway in the wind.','高高的草开始随风摇摆。'),('Her clear explanation helped sway the committee.','她清楚的解释帮助说动了委员会。'),sources=S('sway','sway'))
W('sways','/sweɪz/','摇摆、影响、说动〔第三人称单数〕；摇摆动作〔复数〕',
 '一棵树在风里左右摆，叫 sways；一条消息把人的判断带向某边，也可用同形动词。名词可数时是几次摆动。',
 'sway + -s，元音后读 /z/；ay 中的 y 保留，不改成 ies，因为 y 前是元音字母 a。',SWAY+[['sway + -s → sways','它左右摆；它影响人的决定']],
 'sways in the wind 是在风里摆，sways the audience 是影响观众、听众的看法；人物是否直接作宾语能提示用法。',
 'sways gently 轻轻摇摆；sways public opinion 影响公众看法。',
 'sways someone 的影响常朝某个决定、立场偏转；impresses someone 只保证给人深刻印象，未必改变判断。',
 ('The branch sways whenever a bird lands on it.','每逢有鸟落上去，树枝就会摇摆。'),('A strong personal story often sways the audience.','有感染力的亲身经历往往能说动听众。'),sources=S('sways','sway'))
W('swayed','/sweɪd/','摇摆了；影响、说动了；被左右的',
 '树或身体刚才往左右摆，是 swayed；人听了论证改了倾向，是 was swayed。立场像从原位被带向了另一边。',
 'sway + 完整 -ed，元音后读 /d/；ay 的 y 保留，不能写成 swaied。',SWAY+[['sway + -ed → swayed','过去摆动；已经影响或受到影响']],
 'swayed to the music 是随音乐摇摆，swayed by the evidence 是被证据说动；被动用法常接 by 交代影响来源。',
 'easily swayed 容易受影响的；swayed in the breeze 在微风里摇摆。',
 'swayed by evidence 不一定是贬义动摇，也可以是合理改变判断；词本身只说受到影响、偏向某边。',
 ('The crowd swayed to the music.','人群随着音乐摇摆。'),('I was swayed by her practical arguments.','她切合实际的论证说动了我。'),sources=S('swayed','sway'))
W('swaying','/ˈsweɪɪŋ/','正在摇摆；正在影响、说动；摇摆的',
 '身体随音乐轻轻左右移，树梢随风来回摆，是 swaying；文字、演讲也可能正在把人的看法带向某边。',
 'sway + 完整 -ing，直接加；保留 y，/eɪ/ 后再接 /ɪŋ/，不是换成另一个元音拼写。',SWAY+[['sway + -ing → swaying','摆动过程；影响判断的过程']],
 'swaying trees 是摇曳的树，swaying to the rhythm 是随节奏摇摆；swaying voters 是正在影响选民判断。',
 'gently swaying 轻轻摇摆；swaying from side to side 左右摇摆。',
 'swaying 可以平缓且有节奏，lurching 常突然、失控；不是出现摇晃就一律有危险、要跌倒。',
 ('She stood by the stage, swaying to the rhythm.','她站在舞台旁，随着节奏摇摆。'),('We could see the tops of the trees swaying in the wind.','我们能看见树梢正在风中摇动。'),sources=S('swaying','sway'))
TEETER=[['较早 titter 的不稳动作形式 → 近代 teeter','可能接北欧颤动材料；这里不是从轻笑 titter 的意思直接推演'],['上下、左右不稳 → 在边缘将倒未倒','比喻公司、局面等接近坏结果，也像重心卡在危险边缘']]
W('teeter','英 /ˈtiːtə/；美 /ˈtiːtər/','摇摇欲坠；站、走得不稳；在危险边缘徘徊',
 '一摞书叠得太高，晃着像下一秒就掉，是 teeter。企业 teeter on the brink of collapse，也像重心已挪到倒下边缘。',
 '由较早表示不稳动作的 titter 变来，可能联系北欧颤动材料。现代 teeter 是完整动词，末尾 -er 保留在它后续的词形变化中。',TEETER,
 'teeter on the edge 是在边缘摇摇欲坠，teeter on the brink of failure 是濒临失败；也可说穿着不稳的鞋摇晃地走。',
 'teeter on high heels 踩高跟鞋走得不稳；teeter dangerously 危险地摇晃。',
 'sway 可是平稳、有节奏地摆，teeter 通常强调平衡很勉强、仿佛就要倒；不必真的已经跌落。',
 ('The stack of books began to teeter on the narrow shelf.','那摞书在狭窄架子上开始摇摇欲坠。'),('The company seemed to teeter on the brink of failure.','那家公司看起来已在失败边缘摇摇欲坠。'),sources=S('teeter','teeter'))
W('teeters','英 /ˈtiːtəz/；美 /ˈtiːtərz/','摇摇欲坠、站走不稳、处于危险边缘〔第三人称单数〕',
 '一只杯子放在桌边，重心很险、轻轻一碰就要掉，是 teeters；局面好像马上会崩，也能借这种平衡讲。',
 'teeter + -s，读 /z/；直接在完整动词后加三单词尾，原来的 er 不替换。',TEETER+[['teeter + -s → teeters','它勉强维持平衡；它濒临坏结果']],
 'teeters on the edge 是在边缘摇晃，teeters on the brink of collapse 是濒临崩溃；on 后常指出危险边界。',
 'teeters at the top 顶端摇摇欲坠；teeters in high heels 踩高跟鞋走得不稳。',
 'teeters 表示还在勉强撑住，falls 就已经落下；读到 on the brink 时，通常仍是接近某结果。',
 ('The vase teeters on the edge of the crowded shelf.','花瓶在拥挤的架子边缘摇摇欲坠。'),('The old fence teeters whenever the wind picks up.','风一变大，旧围栏就摇摇欲坠。'),sources=S('teeters','teeter'))
W('teetered','英 /ˈtiːtəd/；美 /ˈtiːtərd/','摇摇欲坠了；摇晃着勉强站稳、走了；一度濒临',
 '刚才身子晃着差点失去平衡，或一个方案一度接近失败，是 teetered。它把“差点撑不住”的那段过程说出来。',
 'teeter + 完整 -ed，读 /d/；最后是 /tə/ 或 /tər/ 再加 /d/，不是在 t 后加 /ɪd/，基础词末音决定读法。',TEETER+[['teeter + -ed → teetered','过去勉强平衡；一度在危险边缘']],
 'teetered on the step 是在台阶上摇晃，teetered on the brink of cancellation 是一度接近取消；结果仍要看后文。',
 'teetered for a moment 摇晃了一会儿；teetered on the edge 在边缘摇摇欲坠。',
 'teetered 不必最后跌倒、失败；stumbled 常说绊了一下，而 teetered 更能描写重心来回找平衡。',
 ('He teetered on the step, then grabbed the rail.','他在台阶上晃了晃，随后抓住栏杆。'),('The pile teetered for a moment before it settled.','那一堆东西晃了一阵，随后稳住了。'),sources=S('teetered','teeter'))
W('teetering','英 /ˈtiːtərɪŋ/；美 /ˈtiːtərɪŋ/','正在摇摇欲坠；摇晃不稳的；濒临的',
 '一摞盘子正晃着找平衡，或一件事正处在要失败的关口，是 teetering；最关键是“还没倒，却已不稳”。',
 'teeter + 完整 -ing，直接加；英式在元音开头词尾前也发 r。分词可描述物体或抽象局面的危险状态。',TEETER+[['teeter + -ing → teetering','将倒未倒的过程、处境']],
 'a teetering pile 是摇摇欲坠的一堆东西，teetering on the brink 是在危险边缘；常接 of 再说快发生的坏结果。',
 'teetering on a stool 在凳上晃得不稳；teetering on the edge of failure 濒临失败。',
 'teetering 把不稳和临界感放在一起，leaning 只说倾斜；一面稳固的斜墙可以 leaning，却未必 teetering。',
 ('She steadied the teetering stack of plates.','她扶稳了那摞摇摇欲坠的盘子。'),('The project was teetering on the brink of cancellation.','项目正濒临取消。'),sources=S('teetering','teeter'))

def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfl',ROOTS,WORDS)
 extend_lessons()
