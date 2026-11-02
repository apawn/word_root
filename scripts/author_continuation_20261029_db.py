"""Song and pass: action, creator, sound, crossing and authentication words."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
SO=[['古英语 sang → 中古英语 song、sang','歌唱、歌曲，与 sing 历史同族'],['英语 song','歌曲、歌唱声；某些固定比喻']]
W('song','英 /sɒŋ/；美 /sɔːŋ/，亦 /sɑːŋ/','歌曲；歌唱；鸣唱声',
 '通常把旋律和可唱的词组织成一首作品；鸟儿唱出的声音也能说 song。',
 '接古英语 sang，经中古英语 song 等延续，与 sing 唱歌是历史相关形式。不是现代英语任意把 sing 的 i 换成 o 都能造名词的规则。',SO,
 'sing a song 唱一首歌，write a song 写歌；bird song 鸟鸣。for a song 固定说花很便宜的价钱，不是用一首歌直接付款。',
 'sing a song；write a song；a love song；for a song。',
 'song 通常是一首可唱作品，music 是音乐上位词；instrumental music 器乐不必称 song，但日常有时会把音乐曲目宽泛叫 song。',
 ('She sang a song she had written herself.','她唱了一首自己写的歌。'),('We heard the song of a bird outside the window.','我们听见窗外鸟儿的鸣唱。'))
W('songwriter','英 /ˈsɒŋraɪtə/；美 /ˈsɔːŋraɪtər/','歌曲创作者；词曲作者',
 '负责把一首歌写出来的人：可能写旋律、歌词，也可能与别人分工。',
 'song 歌 + writer 作者。歌曲由歌词和音乐等部分组成，songwriter 的具体贡献按作品、署名情况，不强定人人必须独写全部。',C('song 歌曲','writer 作者','songwriter','创作歌曲的人'),
 'a singer-songwriter 创作型歌手，a team of songwriters 歌曲创作团队；连字符组合可在搭配中理解，当前不另开标题。',
 'a talented songwriter；a team of songwriters；a songwriter’s work。',
 'songwriter 写歌，singer 唱歌；同一个人可以两者都是，但演唱一首歌不自动拥有其创作署名。',
 ('The songwriter worked with a singer on the new album.','词曲作者与一位歌手合作制作新专辑。'),('She is best known as a songwriter.','她最为人熟知的身份是歌曲创作者。'))
W('songwriting','英 /ˈsɒŋraɪtɪŋ/；美 /ˈsɔːŋraɪtɪŋ/','歌曲创作；写歌',
 '把歌词、旋律等逐步构思成一首歌的工作，而不是台上唱完一次。',
 'song 歌曲 + writing 写作、创作，动作名词通常不可数。与 songwriter 人物词并排看，writer 与 writing 分别说人和活动。',C('song 歌曲','writing 创作活动','songwriting','歌曲的创作过程、技艺'),
 'songwriting skills 写歌能力，a songwriting workshop 歌曲创作工作坊；不只手写到纸上，现代也可在电脑里完成。',
 'songwriting skills；a songwriting workshop；the songwriting process。',
 'songwriting 创作，singing 演唱，recording 录制；可能相互配合，但不是同一动作。',
 ('He attends a weekly songwriting workshop.','他每周参加一次歌曲创作工作坊。'),('Her songwriting draws on memories of her hometown.','她写歌时会借用家乡记忆。'))
W('songbird','英 /ˈsɒŋbɜːd/；美 /ˈsɔːŋbɜːrd/','鸣禽；善鸣的鸟',
 '名字把重点放在鸟会唱、善于鸣叫，而不是会写歌词。',
 'song 鸣唱 + bird 鸟，形成鸣禽、善鸣鸟的名称。自然分类中 songbirds 有更具体的范围，不能只按人觉得好听就随意给所有鸟归类。',C('song 鸣唱','bird 鸟','songbird','按鸣唱特点称呼的鸟类'),
 'a garden songbird 花园里的鸣禽，songbird populations 鸣禽种群；文学、比喻里范围有时较宽。',
 'a songbird；garden songbirds；songbird populations。',
 'songbird 是鸟，birdsong 是鸟发出的鸣唱；前后顺序决定中心是鸟还是声音。',
 ('A small songbird perched on the fence.','一只小鸣禽栖在围栏上。'),('The study follows changes in local songbird populations.','研究追踪当地鸣禽种群的变化。'))
W('birdsong','英 /ˈbɜːdsɒŋ/；美 /ˈbɜːrdsɔːŋ/','鸟鸣声；鸟的鸣唱',
 '清早树林里传来一片鸟叫的旋律，把这一类声音整体叫 birdsong。',
 'bird 鸟 + song 鸣唱，中心是 song 声音，通常作不可数名词。不是倒过来就仍说一只鸟。',C('bird 鸟','song 鸣唱','birdsong','鸟发出的鸣唱声'),
 'wake to birdsong 在鸟鸣中醒来，a recording of birdsong 鸟鸣录音；也可泛说鸟儿的歌唱现象。',
 'the sound of birdsong；wake to birdsong；record birdsong。',
 'birdsong 声音，songbird 鸟；one songbird 一只鸣禽，some birdsong 一阵鸟鸣。',
 ('We woke to birdsong outside the tent.','我们伴着帐篷外的鸟鸣醒来。'),('The recording captures the dawn birdsong.','录音记录了黎明时的鸟鸣。'))
R('B2749','歌曲、歌唱声；创作与鸟鸣','SONG：一首歌，或歌唱的声音','songwriter 是人，songwriting 是创作活动；songbird 是鸟，birdsong 是声音，用顺序抓住复合词中心。',
 'song 由古英语 sang 延续，与 sing 历史同族。先看作品，再看创作者与过程，最后按鸟及鸣唱声成对记。',
 'song → songwriter、songwriting、songbook；song + bird → songbird，bird + song → birdsong；evensong 是已学固定词。',
 [['歌曲、创作与歌本','song · songwriter · songwriting · songbook'],['鸟及鸣唱声','songbird · birdsong'],['固定宗教用语','evensong']],
 'songwriter 不一定是演唱者；songwriting 不等于 recording；songbird 与 birdsong 换顺序换对象。',
 'The songwriter listened to birdsong before starting a new song.\n\n歌曲创作者开始写新歌前，听了一会儿鸟鸣。',
 'song songwriter songwriting songbook songbird birdsong evensong')
PA=[['法语 passer → 英语 pass；更远接拉丁步子、通行词族','跨过、通过'],['现代 pass 词族','经过、及格、传递；通行许可及通行设施']]
W('overpass','英 /ˈəʊvəpɑːs/；美 /ˈoʊvərpæs/','跨线桥；高架跨越通道',
 '一条路从上面跨过另一条路、铁路等，让两股交通不用在同一平面相交。',
 'over- 在上、越过 + pass 通行，名词为上方跨越的通道。另有较少见动词义，本轮主学交通设施名词。',C('over- 在上、越过','pass 通行','overpass','从上方跨越其他线路的通道'),
 'a pedestrian overpass 人行天桥，a highway overpass 公路跨线桥；不是所有 elevated road 高架道路都只是一处交叉跨线桥。',
 'a pedestrian overpass；a highway overpass；cross the overpass。',
 'overpass 从上面跨过，underpass 从下面穿过；同一交叉设施也可从不同线路观察来描述。',
 ('We crossed the railway on a pedestrian overpass.','我们通过人行天桥跨过铁路。'),('The bus passed beneath the overpass.','公交车从跨线桥下驶过。'))
W('underpass','英 /ˈʌndəpɑːs/；美 /ˈʌndərpæs/','下穿通道；地下通道',
 '不从车流前横穿，而是从道路、铁路等下面穿过去。',
 'under- 在下 + pass 通行，形成下方穿越通道名称。可能供行人、车辆使用，不只人行地下道。',C('under- 在下','pass 通行','underpass','从道路、铁路等下方穿越的通道'),
 'a pedestrian underpass 人行地下通道，a road underpass 道路下穿通道；具体深度、长度依设施。',
 'a pedestrian underpass；walk through an underpass；a road underpass。',
 'underpass 突出穿过上方其他线路，tunnel 隧道范围更广，可穿山、地底或水下；二者会有重叠。',
 ('The underpass connects the two sides of the busy road.','地下通道连接繁忙道路的两侧。'),('Cyclists used the underpass to avoid the junction.','骑行者通过下穿通道避开路口。'))
W('passcode','英 /ˈpɑːskəʊd/；美 /ˈpæskoʊd/','通行码；解锁码',
 '输入约定的一串代码，门禁或设备才放行、解锁。',
 'pass 通过、获准 + code 代码，形成认证或访问用代码名称。常见数字代码，但名称不保证只能使用数字。',C('pass 获准通过','code 代码','passcode','用于放行、解锁的代码'),
 'enter a passcode 输入解锁码，a device passcode 设备解锁码；具体格式由系统规定。',
 'enter a passcode；set a passcode；a device passcode。',
 'passcode 与 password 实际产品命名有交叠；passphrase 特别强调以短语式较长内容组成，不能仅凭名称断言哪种绝对更安全。',
 ('Enter your passcode to unlock the device.','请输入解锁码以解锁设备。'),('The app asked her to set a new passcode.','应用要求她设置新的通行码。'))
W('passphrase','英 /ˈpɑːsfreɪz/；美 /ˈpæsfreɪz/','口令短语；密码短语',
 '把口令设计成一串词或短语式内容，而不只想到一个短单词。',
 'pass 获准通过 + phrase 短语，形成以短语式内容构成的口令名称。可以包含多个词、字符，具体是否允许空格由系统决定。',C('pass 获准通过','phrase 短语','passphrase','短语式构成的认证口令'),
 'enter a passphrase 输入口令短语，a backup passphrase 备份相关口令；它仍可能作为广义 password 使用。',
 'enter a passphrase；choose a passphrase；a long passphrase。',
 'passphrase 特别说口令形式，password 是更宽泛的密码称谓；phrase 在这里不是日常说一句话就能跳过认证。',
 ('The program asks for a passphrase before opening the file.','程序打开文件前要求输入口令短语。'),('She chose a passphrase that she could remember.','她选择了一条自己能记住的口令短语。'))
R('B3143','通过、经过、传递；通行物与认证','PASS：从这一边通过到另一边','pass 本身有经过、传递、及格等固定用法；交通设施分上下通行，认证用词分口令、代码和短语。',
 'pass 经法语接通行、步子词族。overpass、underpass 用位置修饰通道；password、passcode、passphrase 用材料或形式修饰通行凭据。',
 'pass → passing、passerby、passable、impassable；bypass 绕过；overpass 在上、underpass 在下；password、passcode、passphrase 并排辨析。',
 [['通过的基础及人物、性质','pass · passing · passerby · passable · impassable'],['绕过和上下通行','bypass · overpass · underpass'],['通行凭据、记录及认证','passport · passbook · password · passcode · passphrase']],
 'overpass 上跨，underpass 下穿；password、passcode 命名范围交叠；passphrase 说短语式口令，不自动保证强度。',
 'The passerby used the overpass rather than crossing the busy road.\n\n路人走了天桥，没有直接横穿繁忙道路。',
 'pass passing passerby passable impassable bypass overpass underpass passport passbook password passcode passphrase')
if __name__=='__main__':save('continuation_20261029_db',ROOTS,WORDS)
