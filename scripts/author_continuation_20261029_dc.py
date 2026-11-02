"""Shot and baby: shooting, images, outcomes and childcare words."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
SH=[['古英语 sċeot → 中古英语 schot → shot','发射、射出的东西；与 shoot 历史相关'],['现代 shot 的固定用法','一次射击、投射 → 拍摄、尝试等；也是 shoot 的过去式、过去分词']]
W('shot','英 /ʃɒt/；美 /ʃɑːt/','射击；投篮、射门；照片、镜头；尝试；针剂；少量烈酒',
 '常把一次短促的动作或一份结果当成一项来数：射一发、拍一张、试一次；具体是哪种，看对象。',
 '名词接古英语 sċeot 等，与 shoot 词族相关；动词形式 shot 是 shoot 的过去式、过去分词。不同固定量词义经过各自发展，不把酒、针剂都编成真正射出子弹。',SH,
 'take a shot 拍照、射门或尝试，靠场景定；a flu shot 一针流感疫苗，a shot of espresso 一份浓缩咖啡，a shot of whisky 一小杯威士忌；give it a shot 试试。',
 'give it a shot；a close-up shot；take a shot；a shot of espresso。',
 'shoot 是动作原形，shot 可是名词或过去形式；My phone is shot 口语还可说手机坏掉、不能用了，不是每次真的中弹。',
 ('Give it a shot; you may enjoy it.','试试看，你也许会喜欢。'),('The photographer took a wide shot of the room.','摄影师拍了一张房间的广角画面。'))
W('snapshot','英 /ˈsnæpʃɒt/；美 /ˈsnæpʃɑːt/','快照；某一时刻的概况、状态记录',
 '迅速抓住眼前一瞬间；数据报告也能只呈现某一刻的截面，而不是完整过程。',
 'snap 快速动作 + shot 拍摄、射击；历史有快速、不细瞄的射击用法，再用于随手照片及状态记录。不是所有 snapshot 都只是一张图像文件。',C('snap 快速动作','shot 拍摄、一次发射','snapshot','快拍 → 某时刻的简要记录'),
 'a holiday snapshot 假期随手照，a snapshot of the economy 经济某时点概况；系统 snapshot 可指可供保存、恢复等用途的状态记录，具体内容依工具。',
 'take a snapshot；a snapshot of；a system snapshot。',
 'snapshot 常强调一瞬间的样子，trend 趋势要跨时间观察；一个 snapshot 不足以自动说明长期变化方向。',
 ('She showed me a few snapshots from the trip.','她给我看了几张旅行随手照。'),('The report provides a snapshot of local employment.','报告给出了当地就业情况的一个时点概况。'))
W('screenshot','英 /ˈskriːnʃɒt/；美 /ˈskriːnʃɑːt/','屏幕截图；截取屏幕画面',
 '把屏幕此刻显示的全部或一部分内容，保存成一张静止图。',
 'screen 屏幕 + shot 拍摄的画面，形成数字截图名词，也可作动词。不是用相机对着屏幕拍才算。',C('screen 屏幕','shot 一张画面','screenshot','屏幕内容的静态截取图'),
 'take a screenshot 截图，a screenshot of the error 错误界面截图；可以截全屏，也可以只截一个窗口、区域。',
 'take a screenshot；save a screenshot；a screenshot of the message。',
 'screenshot 静态截图，screen recording 屏幕录制通常包含时间过程；snapshot 范围更宽，还能指系统状态。',
 ('Please take a screenshot of the error message.','请把错误信息截个图。'),('She saved a screenshot of the timetable.','她保存了一张时刻表截图。'))
W('gunshot','英 /ˈɡʌnʃɒt/；美 /ˈɡʌnʃɑːt/','枪声；枪击、开枪',
 '一次开枪的动作，或听到的那声响；修饰伤口时又说明由枪击造成。',
 'gun 枪 + shot 射击，复合为枪击、枪声名词。与 shotgun 交换前后顺序，中心词也随之改变。',C('gun 枪','shot 射击','gunshot','开枪动作、枪声及相关性质'),
 'hear a gunshot 听到枪声，a gunshot wound 枪伤；故事、报道中依所修饰对象判断。',
 'hear gunshots；a distant gunshot；a gunshot wound。',
 'gunshot 枪击、枪声，shotgun 是一种枪；gunshot 是事件、声音，不是那件武器本身。',
 ('A distant gunshot broke the silence in the film.','电影中，远处一声枪响打破了沉默。'),('The witness said she had heard two gunshots.','目击者说她听见了两声枪响。'))
W('shotgun','英 /ˈʃɒtɡʌn/；美 /ˈʃɑːtɡʌn/','霰弹枪；副驾驶座〔美式口语搭配〕',
 '是一种以发射霰弹等为人熟知的枪械类别；ride shotgun 在现代口语里常只是坐副驾驶。',
 'shot 霰弹、小弹丸 + gun 枪，复合为枪械名称。ride shotgun 有旧日护卫坐在车夫旁的历史背景，后转作副驾驶位置；并不表示现代乘客必须带枪。',C('shot 小弹丸、霰弹','gun 枪','shotgun','枪械类别 → ride shotgun 的座位称呼'),
 'a shotgun in a historical display 历史展品中的霰弹枪；ride shotgun 坐副驾驶，call shotgun 口语抢先说自己要坐副驾驶。',
 'a shotgun；ride shotgun；call shotgun。',
 'shotgun 武器名，gunshot 枪声、枪击；ride shotgun 通常不是正在开枪，先看是不是乘车口语。',
 ('The museum displayed an old shotgun.','博物馆展出了一支旧霰弹枪。'),('I’ll drive, and you can ride shotgun.','我来开车，你可以坐副驾驶。'))
W('buckshot','英 /ˈbʌkʃɒt/；美 /ˈbʌkʃɑːt/','较大颗粒的霰弹',
 'shot 还可以指一群小弹丸；buckshot 是其中颗粒较大的类别名称。',
 'buck 雄鹿等相关动物称谓 + shot 弹丸，命名有狩猎用途背景。是固定弹药名，不是被鹿踢出来的一次射门。',C('buck 雄鹿相关动物名','shot 弹丸','buckshot','以较大颗粒为特点的霰弹类别'),
 'buckshot in a historical collection 历史收藏中的霰弹；通常作材料、集合式不可数名词。',
 'buckshot；a description of buckshot；buckshot in a museum display。',
 'buckshot 是弹丸类别，shotgun 是枪械；不能把弹药和武器当同一个物体。',
 ('The label identified the old pellets as buckshot.','标签把这些旧弹丸标为较大颗粒的霰弹。'),('The historian explained the word “buckshot” in the letter.','历史学家解释了信中 buckshot 这个词。'))
W('slingshot','英 /ˈslɪŋʃɒt/；美 /ˈslɪŋʃɑːt/','弹弓；像弹射一样快速移动',
 '用拉紧后回弹的器具把小物体弹出去；动词借这种突然被送出去的速度感。',
 'sling 抛投、投石器相关词 + shot 发射，复合为弹弓名称；动词有借势迅速冲出等用法。',C('sling 抛投、投石器相关词','shot 发射','slingshot','弹弓 → 弹射般迅速移动的比喻'),
 'a slingshot in an illustration 插图中的弹弓；slingshot ahead 迅速冲到前面。太空文章的 gravitational slingshot 另有引力助推专门含义。',
 'a slingshot；slingshot ahead；a slingshot effect。',
 'slingshot 是弹弓，sling 更早可指投石索等不同器具；不要把所有抛投器都当同一结构。',
 ('The drawing shows a character holding a slingshot.','画里的人物拿着弹弓。'),('The cyclist slingshotted ahead as the road opened up.','道路变开阔时，那位骑行者一下冲到了前面。'))
W('earshot','英 /ˈɪəʃɒt/；美 /ˈɪrʃɑːt/','听得见的距离、范围',
 '声音传到耳朵还能听清，才算在这个范围里；不需要真的向耳朵发射任何东西。',
 'ear 耳朵 + shot，后者用射程、所及范围的引申，形成听力所及范围名词。',C('ear 耳朵','shot 所及范围的旧引申','earshot','声音能被听见的距离范围'),
 'within earshot 在听得见的范围内，out of earshot 到了听不见处；范围会随声音、环境、听者而变。',
 'within earshot；out of earshot；stay within earshot。',
 'earshot 听觉范围，eyesight 视力、视线相关能力；out of earshot 不等于 out of sight 看不见。',
 ('Wait until they are out of earshot.','等他们走到听不见的地方再说。'),('The children stayed within earshot of the campsite.','孩子们待在营地喊话能听见的范围内。'))
W('bloodshot','英 /ˈblʌdʃɒt/；美 /ˈblʌdʃɑːt/','眼睛布满血丝的',
 '眼白上显出红红的血丝，看起来发红；这不是描述眼睛中了枪。',
 'blood 血 + shoot 的旧过去分词 shotten，早期 bloodshotten 后缩短成 bloodshot。可用血丝布满的画面帮助理解，不是名词枪击。',[['blood + 旧分词 shotten → bloodshotten','血丝布满的旧形式'],['bloodshotten → bloodshot','缩短形式：眼睛显出红血丝的']],
 'bloodshot eyes 布满血丝的眼睛；常用于叙述外观，原因还需上下文，不能仅凭这个词判断具体疾病。',
 'bloodshot eyes；look bloodshot；tired, bloodshot eyes。',
 'bloodshot 说眼白血丝外观，a black eye 眼周瘀青是另一表达；red eyes 范围又更宽。',
 ('His eyes were bloodshot after the overnight journey.','通宵旅行后，他眼里布满血丝。'),('The actor’s makeup made his eyes look bloodshot.','演员的妆容让他的眼睛显得布满血丝。'))
W('upshot','英 /ˈʌpʃɒt/；美 /ˈʌpʃɑːt/','最终结果；结局',
 '前面折腾了很多步骤，最后归结到什么结果；常用于把复杂经过收拢成一句结论。',
 'up- + shot，历史常追到射箭比赛最后一箭的用法，再发展最终结果义。现代不能只按 up 向上译成朝天射一枪。',
 [['up- + shot；射箭比赛最后一箭的旧用法','决定结果的一次射击'],['现代 upshot','事情最终归结的结果']],
 'the upshot of the discussion 讨论结果，The upshot is that... 最后的结果是……；不一定是好结果。',
 'the upshot is that；the upshot of；the final upshot。',
 'upshot 结果，upset 扰乱、难过、爆冷等是另一词；upshot 本身不说明结果令人高兴还是失望。',
 ('The upshot is that we need another week.','结果就是，我们还需要一周。'),('What was the upshot of the meeting?','会议最后得出了什么结果？'),sources=['https://en.wiktionary.org/wiki/upshot#English','https://www.etymonline.com/word/upshot'])
R('B2976','射击、投射；照片、尝试与各种短促一项','SHOT：一次发射，再到一次拍摄、尝试和固定量','先读 shot 基础，再读 snapshot、screenshot；gunshot 是枪声、事件，shotgun 是武器，不能换顺序仍当同词。',
 'shot 名词接古英语，与 shoot 词族相关，也是 shoot 的过去式、过去分词。earshot 取所及范围，upshot 取最后结果；各义保留自己的历史分支。',
 'shot → snapshot、screenshot、headshot；gunshot、shotgun、buckshot 按事件、武器、弹丸分；earshot、bloodshot、upshot 是固定词。',
 [['基础、拍摄及图像','shot · snapshot · screenshot · headshot'],['枪声、器具和弹丸','gunshot · shotgun · buckshot · slingshot'],['听距、外观与结果','earshot · bloodshot · upshot'],['已学人物口语','hotshot']],
 'gunshot 不是 shotgun；earshot 不是眼睛；bloodshot 不是中枪；upshot 是结果，不必好。',
 'The upshot of the discussion was a request for a clearer screenshot.\n\n讨论最后的结果，是要求提供一张更清楚的截图。',
 'shot snapshot screenshot headshot gunshot shotgun buckshot slingshot earshot bloodshot upshot hotshot')
BA=[['中古英语 babe → baby、babie','婴儿；-y、-ie 亲昵、指小形式'],['现代 baby','婴儿；幼小的；娇惯、像婴儿般照顾的比喻']]
W('baby','/ˈbeɪbi/','婴儿；幼崽；宝贝；过分照顾',
 '最小、最需要照顾的孩子；也能叫幼小动物、最小成员，或亲昵地称宝贝。',
 '中古英语 baby、babie，来自 babe 的亲昵、指小形式；更早常被联系婴儿发声，具体起点不强定。动词 baby 是把人当小婴儿那样照顾。',BA,
 'a newborn baby 新生儿，a baby elephant 小象；the baby of the family 家中最小成员；Don’t baby me 别把我当小孩处处照顾。',
 'a newborn baby；a baby animal；the baby of the family；baby someone。',
 'baby 通常比 child 年龄更小，但 the baby of the family 可能已经成年；baby 作亲昵称呼也不说明对方真是婴儿。',
 ('The baby fell asleep in the car.','婴儿在车里睡着了。'),('Please don’t baby me; I can do this myself.','请别把我当小孩哄着照顾，我自己能做。'))
W('babysitter','英 /ˈbeɪbisɪtə/；美 /ˈbeɪbisɪtər/','临时照看孩子的人',
 '父母出门或忙时，替他们看一会儿孩子的人；孩子不一定还是婴儿。',
 'baby 孩子 + sitter 留守照看者。sit 的待着、看护用法与这里的角色有关，不表示整场只能坐着不动。这个人物词也与后来 babysit 逆构形成有关。',C('baby 孩子','sitter 留守照看者','babysitter','临时照看孩子的人'),
 'hire a babysitter 请临时保姆、看护者，a regular babysitter 常来帮忙照看的人员；可以有偿，也可以亲友帮助。',
 'hire a babysitter；find a babysitter；a regular babysitter。',
 'babysitter 偏临时照看，nanny 通常有更持续的照料职责；实际安排各异，不按名称假定同样工时或资格。',
 ('We need a babysitter for Saturday evening.','周六晚上我们需要有人临时照看孩子。'),('The babysitter read the children a story.','临时看护者给孩子们读了个故事。'))
W('babysit','/ˈbeɪbisɪt/','临时照看孩子；一直盯着照料〔比喻〕',
 '别人暂时顾不上孩子，你接手看护；说设备、同事时可夸张表示总得有人盯着。',
 '现代材料可认 baby + sit，词源资料也按 babysitter 去掉 -er 逆构解释。较短形式不必历史更早；变化 babysat、babysat，跟 sit—sat 一样。',BA+[['baby + sitter → babysitter；由人物词逆构 babysit','临时照看者 → 临时照看孩子']],
 'babysit for a neighbour 替邻居看孩子，babysit the children 照看孩子；babysit a slow machine 抱怨需要一直守着机器。',
 'babysit for；babysit the children；offer to babysit。',
 'babysit 是做事，babysitter 是人；不必仅限 baby 婴儿，也可照顾大一些的儿童。',
 ('Can you babysit for us on Friday?','周五你能帮我们看一下孩子吗？'),('He babysat his niece while her parents were out.','侄女父母外出时，他帮忙照看了她。'))
W('babysitting','/ˈbeɪbisɪtɪŋ/','临时照看孩子；代看孩子的工作',
 '把看一会儿孩子这件事当成一项安排、活动或工作来讲。',
 'baby + sitting 的动作名词，也与 babysit + -ing 的现代词族对应；双写 sit 的 t。历史记录不能仅因较长就断定一定晚于较短动词。',BA+[['baby + sitting；与 babysit 的 -ing 形式对应','照看孩子的活动、工作']],
 'do some babysitting 帮忙或兼职看孩子，a babysitting job 临时看护工作；通常用不可数活动名词。',
 'do some babysitting；a babysitting job；babysitting arrangements。',
 'babysitting 是活动，babysitter 是从事者，babysit 是动词；I do babysitting 不等于 I am a babysitting。',
 ('She earns extra money from babysitting.','她靠临时看孩子赚些额外收入。'),('We arranged babysitting before booking the tickets.','我们订票前先安排了代看孩子的人。'))
R('B2544','婴儿；幼小、亲昵与临时看护','BABY：幼小、需照顾，和看护动作分开','baby 可以是婴儿、小动物或亲昵称呼；babysitter、babysit、babysitting 再分人员、动作、活动。',
 'baby 是 babe 的历史亲昵形式。babysit 与 babysitter 有逆构关系，阅读仍可按人物和动词对应理解；不要因为 baby 在前就把照看对象只限新生儿。',
 'baby → babysitter；babysitter 逆构 babysit，与 babysitting 成一组；crybaby 是已学固定人物比喻。',
 [['基础及临时看护','baby · babysitter · babysit · babysitting'],['抱怨式人物比喻','crybaby']],
 'babysitter 人，babysit 动作，babysitting 活动；sit 在这里不是坐着不动；baby 亲昵称呼不说明年龄。',
 'The babysitter offered to babysit again, so our babysitting arrangements were settled.\n\n临时看护者愿意再来帮忙，代看孩子的安排就定下了。',
 'baby babysitter babysit babysitting crybaby')
for item in WORDS:
    if item['word']=='bloodshot':item['sources'].append('https://www.etymonline.com/word/bloodshot')
    if item['word']=='shotgun':item['sources'].append('https://www.etymonline.com/word/shotgun')
if __name__=='__main__':save('continuation_20261029_dc',ROOTS,WORDS)
