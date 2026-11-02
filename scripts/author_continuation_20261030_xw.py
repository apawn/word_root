"""Common past actions: joining, entering, picking and launching."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0625':dict(words=['join','joined'],label='join → joined：接到一起与加入',note='拉丁接合词族经法语进入英语；加入团体与把两件东西连接共享接在一起的画面。'),
 'B4162':dict(words=['enter','entered'],label='enter → entered：进入、录入与参加',note='走到里面的词族，扩展到信息、活动、阶段。'),
 'B3757':dict(words=['pick','picked'],label='pick → picked：挑取、摘取与各种 pick up',note='挑、啄、刺的旧词族，更远来源不强作定论；常用小词决定具体动作。'),
 'B3633':dict(words=['drop','dropped'],label='drop → dropped：落下、降低与放弃',note='滴、落下的早期词族，现代扩展到放下物品、减少、停止某事。'),
 'B3964':dict(words=['fill','filled'],label='fill → filled：装满、填上与充满感受',note='与 full 同族的使满动词，英语过去形式只加 ed，不再多写 l。'),
 'B3105':dict(words=['pull','pulled'],label='pull → pulled：拉近、拉开与拔出',note='继承古英语拉、拔词族，方向由 out、away 等补明。'),
 'C0496':dict(words=['notice','noticed'],label='notice → noticed：进入注意范围',note='知悉、知道词族的名词在英语中发展为察觉动词。'),
 'B3279':dict(words=['launch','launched'],label='launch → launched：投出、下水与推出',note='这里是投掷、向前送出的动词词族；船只名称 launch 另有借词路线。'),
 'B4205':dict(words=['improve','improved'],label='improve → improved：使更好与变好',note='收益、善加利用的早期词义发展为提高质量；不是现代 im 加 prove 的否定组合。'),
 'C1439':dict(words=['destroy','destroyed'],label='destroy → destroyed：拆掉、毁坏',note='de- 撤去与 struere 建造相连，形成拆毁、使失去作用的词族。'),
}
W('joined','/dʒɔɪnd/','连接了；加入了；与……一道行动；join 的过去式和过去分词',
 '把原先分开的两边接到一起，是 joined；自己接进一个团体、队伍或活动，也就是加入。',
 'join + -ed，/n/ 后读 /d/。join 经古法语 joindre 接拉丁 iungere 接合、联合，分词形 iūnctus 留在其他同族词里；joined 是英语规则过去形式。',
 [['拉丁 iungere → 古法语 joindre → 英语 join','接合、联合'],['join + -ed → joined','已连接、已加入；被接起来的']],
 'joined the team 加入团队；joined the queue 排进队伍；joined us for lunch 与我们一起吃午饭；joined A to B 把 A 接到 B。',
 'joined together；has joined the group。','joined a club 可直接接组织；joined in an activity 常强调参与活动。joined us for dinner 是和我们一起吃饭，不表示加入一个正式组织。',
 ('She joined us for lunch after the meeting.','会议后，她和我们一起吃了午饭。'),('The two pieces were joined with a narrow strip of wood.','这两块东西用一根窄木条连接起来。'),sources=['https://en.wiktionary.org/wiki/joined#English','https://en.wiktionary.org/wiki/join#English'])
W('entered','英 /ˈentəd/；美 /ˈentərd/','进入了；录入了；参加了；enter 的过去式和过去分词',
 '从外面来到里面，是 entered；把资料放进系统、把自己报进比赛，也沿这个进入的画面理解。',
 'enter + -ed，词尾读 /d/。enter 经古法语 entrer 接拉丁 intrāre 进入，关联 intrā 在里面的词族。英音常不读 r，美音保留。',
 [['拉丁 intrā、intrāre → 法语 entrer → enter','里面 → 走进去'],['enter + -ed → entered','进入、录入、参加已发生']],
 'entered the room 进入房间；entered the data 录入数据；entered a competition 报名参加比赛；entered a new stage 进入新阶段。',
 'had entered；entered into the record。','entered the room 通常直接接地点；entered into an agreement 常说达成、订立协议。entered the information into the system 交代信息被录入哪里。',
 ('She entered the room quietly.','她轻轻地走进了房间。'),('He entered the measurements into a spreadsheet.','他把测量数据录入了电子表格。'),sources=['https://en.wiktionary.org/wiki/entered#English','https://en.wiktionary.org/wiki/enter#English'])
W('picked','/pɪkt/','挑选、摘取过；捡起、接走、学会等〔picked up〕',
 '从一堆中挑出一个、从枝头摘下一个，是 picked；后面加 up，动作就常变成拿起来、接人，或顺带学会一些东西。',
 'pick + -ed，/k/ 后读 /t/。pick 接较早英语挑、啄、刺的词族，与邻近日耳曼语材料相关，更远来源不定；直接加 -ed，保留 ck。',
 [['较早英语挑、啄、刺词族 → pick','从中挑出、摘取'],['pick + -ed → picked；picked up 等结构','过去挑、摘；拾起、接走、学到等']],
 'picked a colour 选了颜色；picked apples 摘苹果；picked up the bag 提起包；picked up a language 学会一些语言。',
 'carefully picked；picked someone up at the station。','picked a name 是选了名字；picked up a name 则可能是获得外号、听到一个名字等，需看句子。pick up 的常见意思用宾语、场景分辨，比硬背一个“捡起”更实用。',
 ('She picked a few apples from the tree.','她从树上摘了几个苹果。'),('He picked up some Italian while working in the café.','他在咖啡馆工作时学会了一些意大利语。'),sources=['https://en.wiktionary.org/wiki/picked#English','https://en.wiktionary.org/wiki/pick#English'])
W('dropped','英 /drɒpt/；美 /drɑːpt/','掉下、放下了；下降了；停止、放弃了；drop 的过去式和过去分词',
 '东西从手里落下，是 dropped；数字往下落也能这样说。把一项活动从原有安排里放下，则有停止、放弃的感觉。',
 'drop 末尾 p 双写后加 -ed → dropped，词尾读 /t/。drop 继承古英语 dropa 一滴及相关滴落动词，经中古英语延续，再扩展到下降、放下、退出等。',
 [['古英语滴、滴落词族 → 中古英语 → drop','一滴、落下 → 下降、放下等'],['drop 双写 p + -ed → dropped','过去掉落、下降、放弃']],
 'dropped the cup 掉了杯子；the temperature dropped 气温下降了；dropped the subject 不再谈那个话题；dropped out of the course 退出课程。',
 'dropped sharply；dropped someone off at the station。','dropped the bag 可能是松手让包掉下，也可能按语境说放下；fell 主要说物体自己落下。dropped someone off 则是把人送到某处下车。',
 ('The temperature dropped quickly after sunset.','日落后，气温很快降了下来。'),('She dropped me off outside the library.','她把我送到图书馆外，让我在那里下车。'),sources=['https://en.wiktionary.org/wiki/dropped#English','https://en.wiktionary.org/wiki/drop#English'])
W('filled','/fɪld/','装满、填补了；充满；fill 的过去式和过去分词',
 '让空的地方有了内容，是 filled；洞被填好、杯子装满、房间充满音乐，都共享从空到有的感觉。',
 'fill + -ed，/l/ 后读 /d/，原来已经是 ll，不再加一个 l。fill 继承古英语 fyllan，使满，与 full 满同族。',
 [['古英语 fyllan → fill；与 full 同族','使满、装满、补足'],['fill + -ed → filled','装满、填过；充满某物的']],
 'filled the bottle 装满瓶子；filled the gap 填补空缺；filled in the form 填好了表格；filled with light 充满光。',
 'a room filled with music；filled to the top。','filled with 说明里面充满什么；filled in a form 和 filled out a form 都可表示填表，地区使用习惯有差异。full 是形容词，filled 更能看出填入、装入后的状态。',
 ('She filled the bottle with water before leaving.','离开前，她把瓶子装满了水。'),('The room was filled with the sound of laughter.','房间里充满了笑声。'),sources=['https://en.wiktionary.org/wiki/filled#English','https://en.wiktionary.org/wiki/fill#English'])
W('pulled','/pʊld/','拉、拔、拖过；pull 的过去式和过去分词',
 '抓住东西朝自己或某个方向带，是 pulled；拔出钉子、拉开门、把椅子拉近，都可沿着这个动作理解。',
 'pull + -ed，/l/ 后读 /d/，原词已写 ll。pull 继承古英语 pullian，经中古英语 pullen 延续，更远来源不确定。',
 [['古英语 pullian → 中古英语 pullen → pull','拉、拔、扯'],['pull + -ed → pulled','过去拉动、拔出、拖动']],
 'pulled the door 拉门；pulled out a nail 拔出钉子；pulled up a chair 拉来一把椅子；pulled away 驶离、离开。',
 'pulled gently；pulled the curtains closed。','pull 以拉的方式带动，push 以推的方式带动。pulled up 可说车停下，也可说拉来椅子，具体对象、场景决定方向和结果。',
 ('She pulled the chair closer to the table.','她把椅子拉得更靠近桌子。'),('The train pulled away from the platform.','火车驶离了站台。'),sources=['https://en.wiktionary.org/wiki/pulled#English','https://en.wiktionary.org/wiki/pull#English'])
W('noticed','英 /ˈnəʊtɪst/；美 /ˈnoʊtɪst/','注意到；察觉了；notice 的过去式和过去分词',
 '原来没有进入注意范围的小细节，现在被看见、听见、察觉到了，就是 noticed。',
 'notice 末尾已有 e，加 -d，原词以 /s/ 结尾，词尾读 /t/。notice 名词经法语接拉丁 notitia 知悉、知识，关联 noscere 知道；英语后来由名词发展出察觉动词。',
 [['拉丁知悉词族 → 法语 notice → 英语 notice 名词、动词','知悉 → 注意、告知；察觉'],['notice 去 e + -ed → noticed','过去注意到、察觉到']],
 'noticed a change 注意到变化；noticed that ... 注意到……；noticed someone leaving 注意到某人正在离开；went unnoticed 没被注意到〔相关形式〕。',
 'suddenly noticed；had not noticed before。','noticed someone do 常把动作作为一件事来察觉；noticed someone doing 常突出当时正在进行的动作。noticed that 后接完整情况，说明发现了什么。',
 ('I noticed a small crack near the window.','我注意到窗边有一道小裂缝。'),('She noticed that the room had become quiet.','她察觉到房间里安静下来了。'),sources=['https://en.wiktionary.org/wiki/noticed#English','https://en.wiktionary.org/wiki/notice#English'])
W('launched','英 /lɔːntʃt/；美 /lɔːntʃt, lɑːntʃt/','发射了；使船下水；推出、开展了；launch 的过去式和过去分词',
 '把东西向前送出，让它真正动起来，是 launched 的画面：船下水、火箭发射，或新项目正式推出。',
 'launch + -ed，/tʃ/ 后词尾读 /t/，结尾是 /ntʃt/，不多添 /ɪd/。动词经法语 lancher、lancier 等接拉丁 lanceāre 投矛，来自 lancea 矛。',
 [['拉丁 lancea、lanceāre → 法语 → launch 动词','矛、投掷 → 向前送出、使起步'],['launch + -ed → launched','发射过、下水了；推出、展开']],
 'launched a rocket 发射火箭；launched a boat 使船下水；launched a product 推出产品；launched a campaign 开展活动。',
 'successfully launched；a newly launched service。','launched 常强调正式开始、向外推出。launched a website 说网站上线推出，built a website 则说建成网站，关注的阶段不同。',
 ('The team launched a new website for the museum.','团队为博物馆推出了一个新网站。'),('They launched the small boat from the beach.','他们从海滩上把小船推下了水。'),sources=['https://en.wiktionary.org/wiki/launched#English','https://en.wiktionary.org/wiki/launch#English'])
W('improved','/ɪmˈpruːvd/','改进、提高了；改善了；改良的',
 '比原来更好、更能达到目的，是 improved 的共同意思；人可以改进方法，状态也可以自己变好。',
 'improve 末尾已有 e，加 -d，/v/ 后读 /d/。improve 接盎格鲁法语 emprouwer 等，使产生收益、善加利用的意义发展为使更好；后来拼写受 prove 等影响。',
 [['盎格鲁法语收益、善加利用词族 → improve','让它有收益、用得好 → 改善'],['improve 去 e + -ed → improved','已经变好；改进后的']],
 'improved the design 改进了设计；skills improved 技能提高了；an improved version 改进版；much improved 好多了。',
 'has improved greatly；improved over time。','improved something 说使某物更好；something improved 说某物变好了。improved 作形容词可修饰新版、方法，比较的是过去状态或某个基准。',
 ('The new layout improved the flow of people through the building.','新的布局让楼内人员通行更顺畅了。'),('Her pronunciation improved with regular practice.','经过经常练习，她的发音进步了。'),sources=['https://en.wiktionary.org/wiki/improved#English','https://en.wiktionary.org/wiki/improve#English'])
W('destroyed','/dɪˈstrɔɪd/','摧毁、毁坏了；使严重失去作用；destroy 的过去式和过去分词',
 '搭好的东西被拆坏、破坏到难以继续存在或使用，就是 destroyed；希望、计划等也能被比喻成遭到摧毁。',
 'destroy + -ed，y 前是元音 o，直接保留 y，加 ed，词尾读 /d/。destroy 经古法语等接拉丁 dēstruere，de- 拆下、撤去与 struere 建造相连。',
 [['拉丁 de- + struere → dēstruere → 法语、英语 destroy','把搭好的东西拆掉 → 毁坏、摧毁'],['destroy + -ed → destroyed','过去摧毁；被毁坏的']],
 'destroyed the bridge 摧毁了桥；destroyed by fire 被火烧毁；destroyed their hopes 摧毁了希望；a destroyed building 被毁坏的建筑。',
 'completely destroyed；nearly destroyed。','destroy 通常比 damage 损坏程度更重，强调正常功能、结构或存在基础遭到破坏。destroyed an argument 可以比喻彻底驳倒论点，语气较强。',
 ('The fire destroyed the old warehouse.','大火烧毁了那座旧仓库。'),('The discovery destroyed their hopes of finishing that day.','这一发现打破了他们当天完成的希望。'),sources=['https://en.wiktionary.org/wiki/destroyed#English','https://en.wiktionary.org/wiki/destroy#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xw',ROOTS,WORDS)
 extend_lessons()
