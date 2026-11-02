"""Languid, languish, listless and other kinds of low energy."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C0655':dict(words='languid languidly languor languish languishes languished languishing'.split(),label='languere 词群：活力松下来',note='拉丁 languere 虚弱的材料，与 laxus 松的通常作更远的同源比较；不是由现代 lax 加后缀造出。languid、languor、languish 各有法语或拉丁借入路线，不把英语词形顺序强排为借入先后。'),
 'B3067':dict(words='listless listlessly listlessness'.split(),label='listless 的另源词群：没兴致',note='此处 list 是旧 liste 兴致、欲望等材料，接 lystan 喜欢、想要的词族；与清单 list 区分。-less 是缺少兴致，再加 -ly 或 -ness 说方式、状态。'),
 'C0336':dict(words='indolent indolently indolence'.split(),label='indolently：懒洋洋地',note='indolent 的历史内部 in- 否定、dolere 疼痛；早有无痛、不受痛感影响义，后来有安逸、懒散义。不能见到前缀就把现代所有句子都译成无痛。'),
 'C0083':dict(words='inert inertly inertness'.split(),label='inert：不活动、没反应',note='拉丁 iners、inert- 含否定 in- 与 ars 技能，早有无技能、不活动义；经法语或拉丁借入英语，再有化学惰性。'),
 'C0341':dict(words='dormitory dormitories'.split(),label='dormitories：供集体住宿的房间、楼',note='拉丁 dormitorium 睡觉场所，接 dormire 睡；英语 dormitory 后来常指学校宿舍。复数 y 改 i 加 -es。'),
 'C0415':dict(words='dilatory'.split(),label='dilatory：把事情往后搬，迟迟不办',note='经法语、晚期拉丁 dilatorius 接 dilatus，作 differre 拖后、推迟的分词；differre 含 dis- 与 ferre 带、搬。不是现代 dilate 扩张加 -ory 的同一条意思。'),
 'B4057':dict(words='lackluster lacklustre'.split(),label='lacklustre：缺少光彩，到表现平淡',note='英式 lacklustre 与美式 lackluster 对应，lack 缺少与 lustre 光泽组成；不是两个不同强度的形容词。'),
 'A1740':dict(words='lackadaisical lackadaisically'.split(),label='lackadaisical：漫不经心、提不起劲',note='由旧叹词 lackadaisy、lack-a-day，接 alack the day 的感叹材料发展，后义或受 lax 影响。不是 lack 加 daisy 雏菊的字面组合。'),
 'B3446':dict(words='loll lolls lolled lolling'.split(),label='loll：松松地躺靠、垂下',note='和 lounge 比较姿态，不把 loll 当成现代 lounge 缩写。loll 远源未定，可能接中古荷兰语打盹、咕哝材料或模拟摇晃；舌头松垂义后来发展。'),
}
LANG=[['拉丁 languere 虚弱、乏力 → 不同法语、拉丁派生材料','languid、languor、languish 接同一核心，不互相硬派生'],['活力不足 → 没劲、懒洋洋；或久困其中、没有进展','学习画面是像失去支撑，精神和进展都垂下来']]
LIST=[['旧 liste 兴致、喜欢，与 lystan 等词相接','不是清单 list 这一来路'],['liste + -less → listless','缺少兴致、提不起精神，再可说方式或状态']]
INERT=[['拉丁 in- 否定 + ars 技能 → iners、inert-','无技能、不活动等意思，后经法语或拉丁进入英语'],['英语 inert → inertly / inertness','不动、不响应的方式与性质；化学也有惰性义']]
LACKADAISICAL=[['旧感叹 alack the day → lack-a-day → lackadaisy','原有遗憾、哀叹的感情色彩'],['lackadaisical → 漫不经心、缺乏热情','意义或受 lax 松散影响，不是缺少雏菊']]
LOLL=[['中古英语 lollen：闲躺、松松垂下','来源未定，可能接荷兰语材料或拟态'],['舒舒服服靠躺；后来也说舌头松垂','共同画面是松下来，未有力地支撑、收住']]
W('languid','/ˈlæŋɡwɪd/','倦怠无力的；懒洋洋、舒缓的',
 '动作慢下来，手臂像懒得抬高，声音也软下来，是 languid。可以是没力气，也可以是舒服地松下来，语气不一定在批评。',
 '经法语 languide 或直接借拉丁 languidus，接 languere 虚弱。词尾 -id 在拉丁派生中表示性质，不能机械当成现代 languish 截掉 sh 得到。',LANG,
 'a languid wave 懒洋洋地挥手；a languid afternoon 慵懒的午后。',
 'a languid smile；languid movements。',
 'lethargic 常让人感到精力低、反应差，languid 还可有优雅、舒缓的描写感；语气不必一样。',
 ('She greeted us with a languid wave.','她懒洋洋地挥了挥手，向我们打招呼。'),('The music suited the languid summer afternoon.','那音乐很适合慵懒的夏日午后。'),sources=S('languid','languid'))
W('languidly','/ˈlæŋɡwɪdli/','懒洋洋、软绵绵地；无力地',
 '靠在长椅上，手慢慢伸出去，像一点也不急，是 languidly。它把舒缓或乏力的姿态写进动作里。',
 'languid + -ly；形容词变方式副词，完整保留 d。',LANG+[['languid + -ly → languidly','以倦怠、舒缓的方式行动']],
 'stretch languidly 懒洋洋地伸展；smile languidly 慵懒地笑。',
 'lean back languidly；wave languidly。',
 'languidly 不一定是不情愿，reluctantly 才突出心里不愿意；姿态慢与态度拒绝不同。',
 ('He stretched languidly in the hammock.','他在吊床里懒洋洋地伸了伸身子。'),('She leaned back languidly and watched the clouds.','她慵懒地向后靠着，看天上的云。'),sources=S('languidly','languid'))
W('languor','英 /ˈlæŋɡə/；美 /ˈlæŋɡɚ/','倦怠、乏力；慵懒舒缓的状态〔较书面〕',
 '炎热午后，整个人松下来，什么也不想赶，空气都像慢了，是 languor。也能写令人不舒服的乏力，不能只记成优美的懒散。',
 '经古法语 langor 借拉丁 languor、languorem，接 languere 虚弱；英语早有疾病、痛苦义，后来更多说乏力、倦怠。',LANG+[['古法语 langor、拉丁 languor → 英语 languor','早期病弱、痛苦义，到乏力、倦怠等状态']],
 'summer languor 夏日慵懒；a feeling of languor 一阵倦怠。',
 'the languor of a hot afternoon；shake off languor。',
 'languor 是状态名词，languid 是性质形容词；the languor of the afternoon 对应 a languid afternoon。',
 ('A pleasant languor settled over us after lunch.','午饭后，一种舒服的慵懒感笼罩了我们。'),('The heat filled the room with a sense of languor.','炎热让整个房间都有一种倦怠、慵懒的感觉。'),sources=S('languor','languor'))
W('languish','/ˈlæŋɡwɪʃ/','长期困在不利处境；停滞不振；日渐衰弱',
 '申请递上去几个月没人处理，计划放在抽屉里一直没动，都可以 languish。像活力被慢慢耗掉，待着却没有好转、进展。',
 '经古法语 languir 的 languiss- 词干，接通俗拉丁语重建形式 *languire 与拉丁 languere 虚弱。末尾 -ish 不是这里表示有点的现代形容词后缀。',LANG,
 'languish in a drawer 在抽屉里搁置；languish in obscurity 长期默默无闻。',
 'languish in prison 久困狱中；languish at the bottom of the table 长期排名垫底。',
 'remain 可以中性说留下，languish 往往带不利处境、缺少进展、让人惋惜的感觉。',
 ('The proposal may languish in a drawer for months.','那份提案可能会在抽屉里搁上好几个月。'),('Without new investment, the business could languish.','没有新投入，这门生意可能会一直萎靡不振。'),sources=S('languish','languish'))
W('languishes','/ˈlæŋɡwɪʃɪz/','久困其中；停滞不振〔第三人称单数〕',
 '别人已经推进，自己的申请却一直没有消息，是 languishes。不是单纯放着，而是让人觉得卡住、没能发展。',
 'languish + -es，/ʃ/ 后读 /ɪz/；基础动词借法语、拉丁虚弱材料，不能按现代 -ish 近似义拆。',LANG+[['languish + -es → languishes','它一直陷于不振、停滞等状态']],
 'the plan languishes 计划停着不动；languishes at the bottom 排名一直垫底。',
 'languishes in storage；languishes without support。',
 'waits 只说等待，languishes 通常多一层长期受困、没有进展；等片刻公交不宜动辄这样说。',
 ('The application languishes on an unattended desk.','申请一直搁在无人处理的办公桌上。'),('The team languishes near the bottom of the league.','那支队伍长期在联赛末尾徘徊。'),sources=S('languishes','languish'))
W('languished','/ˈlæŋɡwɪʃt/','长期被搁置、困住了；曾萎靡不振',
 '一幅画在仓库里放了多年，一本好书长久没人注意，可以说 languished。语气常是它本有机会，却迟迟没被看见、用上。',
 'languish + 完整 -ed，/ʃ/ 后读 /t/；过去式、过去分词。',LANG+[['languish + -ed → languished','过去长久停滞、被搁置或衰弱']],
 'languished in storage 在库房里长期搁置；languished for years。',
 'languished in obscurity；sales languished 销售曾低迷。',
 'was stored 是被储存，languished in storage 常暗示被冷落、迟迟没派上用场，评价更强。',
 ('The painting languished in storage for decades.','那幅画在仓库里被冷落了几十年。'),('The project languished until a new team took it over.','那个项目一直停滞，直到新团队接手才有起色。'),sources=S('languished','languish'))
W('languishing','/ˈlæŋɡwɪʃɪŋ/','正在长期受困、停滞；衰弱的；含情脉脉的〔较文学〕',
 '一个计划迟迟没人管，是 languishing。文学里 a languishing look 也可写带柔情、相思的眼神，这接旧有因强烈情感而虚弱的意思。',
 'languish + -ing；现代既可写动作过程，也能作形容词。感情义有历史根据，不是所有 -ing 都只表示某刻正在做。',LANG+[['languish + -ing → languishing','停滞、衰弱的过程；也有感伤、柔情的形容词用法']],
 'languishing in obscurity 长期默默无闻；a languishing look 含情的眼神。',
 'a languishing project；languishing near the bottom。',
 'lingering 是留着不散，可以是好香味；languishing 更常是活力、进展不足，不能只因字形相近就混用。',
 ('The scheme is languishing for lack of support.','那项计划因缺少支持，正停滞不前。'),('The actor gave the camera a languishing look.','演员朝镜头投去一个含情脉脉的眼神。'),sources=S('languishing','languish'))
W('listlessly','/ˈlɪstləsli/','没精打采、提不起兴致地',
 '随手翻着书，却什么也看不进去；食物放面前也没兴趣，是 listlessly。动作在做，兴致和精神却没跟上。',
 'listless + -ly；listless 内部是旧 liste 兴致、欲望 + -less，不是因为没有待办清单才没精神。',LIST+[['listless + -ly → listlessly','以提不起精神、兴致的方式行动']],
 'turn pages listlessly 无精打采地翻页；pick at food listlessly。',
 'wander listlessly；stare listlessly out of the window。',
 'listlessly 强调没精神、没兴致，carelessly 强调不细心；没精神地翻书不一定把书弄坏。',
 ('He turned the pages listlessly without reading them.','他没精打采地翻着书页，什么也没读进去。'),('She picked listlessly at her lunch.','她没什么兴致，午饭只随便吃了几口。'),sources=S('listlessly','listless'))
W('listlessness','/ˈlɪstləsnəs/','没精打采、缺少兴致的状态',
 '什么都不太想碰，坐着也提不起精神，这种状态叫 listlessness。它说兴致、活力低，不是说计划没列完整。',
 'listless + -ness；完整保留 -less，再加 -ness 说性质、状态。',LIST+[['listless + -ness → listlessness','把缺乏兴致、活力的状态当作名词谈']],
 'a feeling of listlessness 一阵没精神；shake off listlessness。',
 'summer listlessness；a mood of listlessness。',
 'boredom 更偏觉得事情无聊，listlessness 是整个人提不起精神；无聊可能让人坐立不安，也可能引出没劲。',
 ('The long, hot afternoon brought a feeling of listlessness.','漫长炎热的午后让人提不起精神。'),('A change of scene helped break the group’s listlessness.','换了个环境，大家总算不再那么没精打采。'),sources=S('listlessness','listless'))
W('indolently','/ˈɪndələntli/','懒洋洋、安于闲散地〔较正式〕',
 '靠着不想动，明明不急着干什么，也不愿费心，能写作 indolently。较书面，常有一层安逸、懒散的评价。',
 'indolent + -ly；基础词借法语或拉丁 indolent-，历史内部是否定 in- 与 dolere 疼痛。现代懒散义不是每句都译成不疼。',
 [['拉丁 in- 否定 + dolere 疼痛的相关材料 → indolent-','较早有不受痛感影响、无痛义'],['安逸、懒散义 → indolent + -ly','现代日常叙述中说懒洋洋地行动']],
 'lie indolently 懒洋洋地躺着；stretch indolently。',
 'recline indolently in a chair；indolently watch the clouds。',
 'indolently 往往有懒散、爱安逸的描写，painlessly 才直接说无痛地；词源旧义不能代替现代搭配。',
 ('He lay indolently in the hammock.','他懒洋洋地躺在吊床里。'),('She stretched indolently before reaching for her book.','她懒洋洋地伸了伸身子，才去拿书。'),sources=S('indolently','indolent'))
W('inertly','英 /ɪˈnɜːtli/；美 /ɪˈnɝtli/','一动不动地；毫无反应地',
 '东西放下后就那么待着，人也不作回应，可以写 inertly。像没有自己的启动和响应，不只是移动速度慢。',
 'inert + -ly；基础词接拉丁 iners、inert-，有不活动、没能力响应等意思。',INERT+[['inert + -ly → inertly','以不动、无反应的方式存在']],
 'lie inertly 静静地躺着不动；sit inertly 毫无反应地坐着。',
 'rest inertly on the ground；remain inertly in place。',
 'inertly 强调不动、不响应，quietly 只说安静；一个人安静地工作时仍很活跃。',
 ('The fallen branch lay inertly across the path.','落下的树枝横在小路上，一动不动。'),('The puppet’s arms hung inertly at its sides.','木偶的双臂垂在两侧，一点也没动。'),sources=S('inertly','inert'))
W('inertness','英 /ɪˈnɜːtnəs/；美 /ɪˈnɝtnəs/','不活动、无反应的性质；惰性',
 '推不动、叫不应的静滞感，或材料不容易和周围物质起反应的性质，可以叫 inertness。具体是行动还是化学，要看对象。',
 'inert + -ness；把不活动、不响应这种性质变成名词。词源内部 in- 否定与 ars 技能，不是现代英语加了一个否定前缀就能机械译全文。',INERT+[['inert + -ness → inertness','不活动、低反应性的性质']],
 'chemical inertness 化学惰性；the inertness of the committee 委员会的不作为。',
 'relative inertness 相对不活泼；a feeling of inertness。',
 'inertia 在物理上有惯性的专门意思，inertness 常说不活泼、无反应；运动中的物体也有惯性，并不必须静止。',
 ('The material was chosen for its chemical inertness.','选这种材料，是看中它的化学惰性。'),('The committee’s inertness frustrated everyone waiting for a decision.','委员会迟迟不行动，让所有等决定的人都很失望。'),sources=S('inertness','inert'))
W('dormitories','英 /ˈdɔːmɪtriz/；美 /ˈdɔrməˌtɔriz/','宿舍、宿舍楼〔复数〕；集体寝室',
 '几幢供学生住的宿舍楼，是 dormitories；旅舍里几间多人共住的大寝室，也可以这样叫。它指睡觉、居住的场所，不是住的人。',
 'dormitory 的 y 改 i，加 -es → dormitories；拉丁 dormitorium 是睡觉的场所，接 dormire 睡。现代常见学校宿舍义。',
 [['拉丁 dormire 睡 → dormitorium 睡觉场所 → 英语 dormitory','较早见于修道院等集体住宿场景，后来用于学校'],['dormitory → dormitories','y 改 i 加 -es，表示多个寝室或宿舍楼']],
 'student dormitories 学生宿舍；shared dormitories 多人寝室。',
 'university dormitories；rooms and dormitories in a hostel。',
 'dormitories 是场所，residents 是住户；宿舍可以很多，住户数量另算。',
 ('The university built two new dormitories near the library.','大学在图书馆附近新建了两幢宿舍楼。'),('The hostel has private rooms as well as shared dormitories.','旅舍既有独立客房，也有多人寝室。'),sources=S('dormitories','dormitory'))
W('dilatory','英 /ˈdɪlətəri/；美 /ˈdɪləˌtɔri/','拖拉、迟缓的；意在拖延的〔正式〕',
 '该回信迟迟不回，是 dilatory；一再提小问题，只为让决定拖下去，是 dilatory tactics。前者慢，后者可能故意制造慢。',
 '经法语、晚期拉丁 dilatorius，接 dilatus，作为 differre 拖后、推迟的分词；内部有 dis- 分开、移开与 ferre 带、搬。',
 [['拉丁 dis- + ferre → differre 推迟','把事情往后带，是历史内部可理解的方向'],['dilatus → dilator、dilatorius → 英语 dilatory','拖着不做，或专门造成拖延']],
 'dilatory tactics 拖延战术；dilatory in replying 回答拖拉。',
 'a dilatory response；dilatory behaviour。',
 'slow 可以中性说慢，dilatory 通常嫌迟缓、拖延；slow and careful 不自动等于故意拖着。',
 ('He was dilatory in answering the letter.','他迟迟没有回那封信。'),('The chair accused them of using dilatory tactics.','主持人指责他们在耍拖延战术。'),sources=S('dilatory','dilatory'))
W('lacklustre','英 /ˈlæklʌstə/；美 /ˈlæklʌstɚ/','缺少光彩的；表现平淡、提不起劲的〔英式拼写〕',
 '演出没有亮点，球队踢得没精神，可以说 lacklustre。像表面没光泽，借来写表现也没能闪一下。',
 'lack 缺少 + lustre 光泽；美式常拼 lackluster。早有眼睛缺少光彩的用法，后来常评价表现不出色。',
 [['lack + lustre → lacklustre','缺少光泽、亮度，早可形容眼睛'],['光彩不足 → 演出、表现平淡','英式 lacklustre 与美式 lackluster 是拼写对应']],
 'a lacklustre performance 平淡无力的表现；lacklustre sales 平平的销量。',
 'a lacklustre campaign；a lacklustre response。',
 'lacklustre 常说表现没亮点，lackadaisical 更偏做事态度不上心；有人很努力，结果仍可能平淡。',
 ('The team gave a lacklustre performance.','球队踢得平淡无力。'),('Sales remained lacklustre despite the new advertising campaign.','虽然做了新一轮广告，销量仍然平平。'),sources=S('lacklustre','lackluster'))
W('lackadaisical','/ˌlækəˈdeɪzɪkəl/','漫不经心、懒懒散散、提不起热情的',
 '别人认真忙着，他随便应付，像怎么都无所谓，是 lackadaisical。常批评态度散漫、没有应有的投入。',
 '接旧叹词 lackadaisy，后者由 lack-a-day、alack the day 的遗憾感叹材料变化而来；现代意义或受 lax 松散影响。不是 lack 加 daisy 雏菊。',LACKADAISICAL,
 'a lackadaisical attitude 漫不经心的态度；a lackadaisical approach。',
 'lackadaisical about preparation；lackadaisical effort。',
 'relaxed 可以是放松但仍认真，lackadaisical 通常嫌人不够上心；轻松和敷衍不同。',
 ('His lackadaisical attitude frustrated the rest of the team.','他漫不经心的态度让其他队员很恼火。'),('The report criticised the department’s lackadaisical approach to preparation.','报告批评了该部门准备工作敷衍、散漫。'),sources=S('lackadaisical','lackadaisical'))
W('lackadaisically','/ˌlækəˈdeɪzɪkli/','漫不经心、懒懒散散地',
 '话听了像没听，任务随便碰两下就算了，是 lackadaisically。重点是态度没投入、没热情，不只是身体动作慢。',
 'lackadaisical + -ly；拼写在 -cal 后加 -ly，常读 /ɪkli/，不用把末尾每个字母都硬读成一个音节。',LACKADAISICAL+[['lackadaisical + -ly → lackadaisically','以不上心、没热情的方式行动']],
 'work lackadaisically 做事散漫；respond lackadaisically 漫不经心地回应。',
 'prepare lackadaisically；wave lackadaisically。',
 'slowly 只说速度，lackadaisically 评价投入；仔细核对所以慢，和懒得核对所以散漫不同。',
 ('He waved lackadaisically without looking up.','他头也没抬，漫不经心地挥了挥手。'),('They prepared lackadaisically and were surprised by the difficult questions.','他们准备得敷敷衍衍，遇到难题才吃了一惊。'),sources=S('lackadaisically','lackadaisical'))
W('loll','英 /lɒl/；美 /lɑl/','懒洋洋地躺靠；松松地垂下、伸出',
 '人没骨头似的靠在沙发上，是 loll；狗的舌头松松伸在嘴外，也能 loll。共同画面是松下来，不绷着、不收紧。',
 '来源未定，可能接中古荷兰语 lollen 打盹、咕哝等材料，或模拟摇晃。英语早有闲躺、松垂，舌头的专门用法后来发展。',LOLL,
 'loll on the sofa 懒洋洋地靠在沙发上；a tongue lolls out 舌头松垂在嘴外。',
 'loll about 闲躺；loll back in a chair。',
 'loll 强调松散、懒洋洋的姿态，sit 只说坐；坐得笔直不一定是 loll。',
 ('We had time to loll on the sofa before dinner.','晚饭前，我们有时间在沙发上懒洋洋地靠一会儿。'),('The dog let its tongue loll out of its mouth.','狗让舌头松松地垂在嘴外。'),sources=S('loll','loll'))
W('lolls','英 /lɒlz/；美 /lɑlz/','懒洋洋地躺靠；松松垂下〔第三人称单数〕',
 '猫斜躺在椅子上，是 lolls；狗舌头伸着、松松垂在一边，也可以 lolls。要看主语是整个身体还是某个部位。',
 'loll + -s，读 /z/；原有双 l 保留。基础词的远源未定，不因为末尾像缩写就改成网络用语。',LOLL+[['loll + -s → lolls','他、它懒靠，或某部位松垂']],
 'lolls in a chair 懒靠在椅子里；the tongue lolls out。',
 'lolls on the grass；lolls back against the cushions。',
 'lolls 是动词，网络缩写 LOL 通常表示大笑等反应；这里按句法和拼写认词。',
 ('He lolls on the sofa while everyone else packs.','别人都在收拾，他却懒洋洋地靠在沙发上。'),('The dog’s tongue lolls to one side.','狗的舌头松松地垂向一边。'),sources=S('lolls','loll'))
W('lolled','英 /lɒld/；美 /lɑld/','懒洋洋地躺靠了；松松地垂下了',
 '刚才在草地上东倒西歪地躺着，或头没支撑似的歪在一边，能写 lolled。重点是松软、散开的姿态。',
 'loll + 完整 -ed，读 /d/；词干本已有双 l，不另外再添一个。',LOLL+[['loll + -ed → lolled','过去懒靠、松垂']],
 'lolled on the grass 懒懒地躺在草地；head lolled to one side。',
 'lolled back in his chair；lolled about all afternoon。',
 'lolled 写松懈的身体姿态，leaned 可以只是靠着；为了看清东西主动前倾，也能 leaned，却不一定 lolled。',
 ('They lolled on the grass after the picnic.','野餐后，他们懒懒地躺在草地上。'),('The sleeping child’s head lolled to one side.','睡着的孩子头松松地歪向一边。'),sources=S('lolled','loll'))
W('lolling','英 /ˈlɒlɪŋ/；美 /ˈlɑlɪŋ/','正在懒洋洋地躺靠；松垂着的',
 '人在椅子里松松地摊着，是 lolling；狗跑完后舌头垂在外面，也能说 tongue lolling。动作画面比休息两字更具体。',
 'loll + -ing；已有双 l 保留，形成过程或描述姿态的分词。',LOLL+[['loll + -ing → lolling','松松地靠躺、垂着的过程或姿态']],
 'lolling on the sofa；with its tongue lolling out 舌头松垂在外。',
 'lolling in the shade；lolling back in a chair。',
 'lolling 不必睡着，dozing 已是打盹；一边懒靠一边聊天也可以 lolling。',
 ('He was lolling in an armchair, listening to music.','他懒洋洋地靠在扶手椅里听音乐。'),('The dog came back with its tongue lolling out.','狗跑回来时，舌头松松地垂在嘴外。'),sources=S('lolling','loll'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhn',ROOTS,WORDS)
 extend_lessons()
