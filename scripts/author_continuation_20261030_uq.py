"""Time, frequency, substitution, sufficiency and fear."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1696':dict(words=['soon','sooner','soonest'],label='soon 的比较与最高程度',note='soon → sooner → soonest，-est 也可接时间副词；现代常见 as soon as possible、the sooner the better 等表达。'),
 'B2507':dict(words=['often','oftentimes','time'],label='often 与 oftentimes：反复发生的次数',note='often 承接旧 oft 经后续延长形成；oftentimes 加入 time 等材料并保留旧副词 s，现代与 often 意思基本相同。'),
 'B4476':dict(words=['stead','instead','steady'],label='stead 位置与 instead 替代',note='stead 接古英语 stede 位置、稳定等词，steady 接 stead + -y；instead 接 in stead 在某人的位置上这一旧短语。'),
 'C0247':dict(words=['enough'],label='远层同源比较：古英语 ge- 保留在 enough',note='enough 接古英语 genog，ge- 为旧加强、集合等前缀，与拉丁 com- 有更远的同源关系。enough 本身是日耳曼语继承词，不是从拉丁 com- 在现代英语直接变来；第二部分有达到、取得的旧材料。'),
 'B3887':dict(words=['terrify','terrified','terrifying'],label='terrify 的双方：被吓到与让人害怕',note='terrified 常说体验恐惧的人，terrifying 常说引起恐惧的事物、经历；两者分别接 -ed、-ing。'),
 'A1741':dict(words=['target','targeting'],label='targeting：把动作对准对象',note='target + -ing，现代说针对、面向、选定对象；词本身不保证已经达到目标。'),
}
W('soon','/suːn/','很快、不久；早',
 '从眼下看过去，不必等太久，事情就会发生。soon 先管时间间隔短，不等于动作本身做得快。',
 '接古英语 sona 立即、马上，经中古英语 sone 等发展；后来语义放宽成短时间内、不久。现代比较 sooner、最高程度 soonest。',
 [['古英语 sona → 中古英语 sone','立即、直接'],['现代 soon → sooner → soonest','不久；更早；最早']],
 'see you soon 很快再见；as soon as possible 尽快；too soon 太早；soon after 不久之后；soon enough 够快、迟早会到，按语境看。',
 'coming soon；get well soon。','soon 说过多久发生，quickly 常说动作做得快。I’ll reply soon 是不久会回复，不等于打字速度一定快。',
 ('I will send you the details soon.','我很快会把细节发给你。'),('We arrived too soon, and the doors were still locked.','我们到得太早，门还锁着。'),sources=['https://www.etymonline.com/word/soon','https://en.wiktionary.org/wiki/soon#English'])
W('sooner','英 /ˈsuːnə/；美 /ˈsuːnər/','更早、更快；soon 的比较级',
 '原来预计周五，现在周三就办好：发生时间往前移了，就是 sooner。它比较等待多久、何时发生。',
 'soon + 比较级 -er，继承旧很快、立即的时间词。这里 -er 表程度比较，不是执行动作的人。',
 [['soon','很快、不久；早'],['soon + -er → sooner','时间上更早、等待更短']],
 'sooner than expected 比预计早；the sooner the better 越早越好；sooner or later 迟早；I’d sooner stay 更愿意留下，较带口语或特定风格。',
 'a little sooner；much sooner。','sooner 不必形容移动速度。The parcel arrived sooner 比较到达时间，arrived faster 在不同语境可能比较运输速度。',
 ('The repairs were finished sooner than expected.','维修比预计更早完成了。'),('If you can come sooner, that would help.','如果你能早点来，会有帮助。'),sources=['https://www.etymonline.com/word/soon','https://en.wiktionary.org/wiki/sooner#English'])
W('soonest','/ˈsuːnɪst/','最早、最快；soon 的最高级',
 '几个可能时间摆在面前，挑能最早发生的那个，就是 soonest。at the soonest 又把它当作最早边界。',
 'soon + 最高级 -est，形成时间副词的最高程度。现代既可比较谁最早回来，也可说 at the soonest 最早也要某时。',
 [['soon → sooner','不久 → 更早'],['soon + -est → soonest','最早、等待时间最短']],
 'at the soonest 最早；who can arrive soonest 谁能最早到；the soonest possible date 尽可能早的日期。',
 'Monday at the soonest；return soonest。','next week at the soonest 是最早下周，可能更晚；不要把它译成最晚下周。日常尽快也常说 as soon as possible。',
 ('The package will arrive on Friday at the soonest.','包裹最早星期五到。'),('We asked who could return soonest.','我们询问谁能最早回来。'),sources=['https://www.etymonline.com/word/soon','https://en.wiktionary.org/wiki/soonest#English'])
W('often','英 /ˈɒfən/ 或 /ˈɒftən/；美 /ˈɔːfən/、/ˈɑːfən/ 等，亦有读 /t/ 形式','经常、常常',
 '不是只发生一回，而是在一段时间里反复发生。often 看的是频率高，不规定每次持续多久。',
 '由旧 oft 常常延长形成，古英语已有 oft；中古英语 often 形式可能受 selden 等词类推影响，后来取代普通用法中的 oft。字母 t 读或不读都有实际使用。',
 [['古英语 oft → 中古英语扩展 often','多次、反复发生'],['现代 often','经常；读音有保留或不读 t 的形式']],
 'often visit 经常拜访；not often 不常；how often 多久一次、频率多高；more often 更经常；very often 很经常。',
 'quite often；as often as possible。','often 常位于普通动词前、be 后：I often go；She is often late。t 发或不发都可见，不必靠这个差别判断词义或是否标准。',
 ('We often walk to the park after dinner.','晚饭后我们常步行去公园。'),('How often do you visit your grandparents?','你多久去看一次祖父母？'),sources=['https://www.etymonline.com/word/often','https://en.wiktionary.org/wiki/often#English'])
W('oftentimes','英 /ˈɒfəntaɪmz/；美 /ˈɔːfəntaɪmz/ 或 /ˈɑːfəntaɪmz/ 等','常常、往往〔与 often 基本同义〕',
 '把许多次这样的情况放在一起看，说往往如此。oftentimes 比 often 长，却不自动表示频率更高。',
 'often 与 time 的较早短语结合，后来合写；末尾 s 承接旧副词材料。中古英语已有相应写法，现代尤其在美式使用中可见。',
 [['较早 often + time 等时间表达','许多时候、反复发生'],['合写 oftentimes；保留旧副词 -s','常常、往往']],
 'oftentimes people ... 人们往往……；oftentimes overlooked 经常被忽略；oftentimes difficult 往往很难。',
 'oftentimes the case；oftentimes forgotten。','oftentimes 与 often 意思基本相同，普通简洁表达 often 通常就够。词更长不代表次数一定更多，也不等于 sometimes 有时。',
 ('Oftentimes, the simplest explanation is the best one.','往往最简单的解释就是最好的。'),('Small improvements are oftentimes overlooked.','小幅改进常常被忽略。'),sources=['https://www.etymonline.com/word/oftentimes','https://en.wiktionary.org/wiki/oftentimes#English'])
W('stead','/sted/','位置、地位；多见于代替、起作用等固定表达',
 '一个人原来站着、承担事情的位置，可以让另一个人顶上。in her stead 就是在她的位置上、代她做。',
 '接古英语 stede、steode 位置、稳定、站立等，属于 stand 的古老同源材料。现代独立说 place 更普遍，stead 主要保留在固定表达和复合词中。',
 [['古英语 stede、steode','位置；站立、稳定'],['现代固定表达中的 stead','某人的位置；作用、益处']],
 'in someone’s stead 代替某人，稍正式；stand someone in good stead 对某人以后大有帮助；instead 接 in stead 合写。',
 'act in her stead；experience will stand you in good stead。','stead 在日常并不随处替换 place；主要记固定表达。steady 稳定的与 stead 同族，所抓的线索是站稳、固定在位置上。',
 ('Her deputy attended the meeting in her stead.','她的副手代她参加了会议。'),('The experience will stand you in good stead later.','这段经历以后会对你大有帮助。'),sources=['https://www.etymonline.com/word/stead','https://en.wiktionary.org/wiki/stead#English'])
W('instead','/ɪnˈsted/','改为、代替、反而',
 '本来想把 A 放进这个位置，后来用 B 顶上去。instead 把注意力放在替换后的选择上。',
 '由中古英语 in stede 等短语缩合，in 在……位置上，stead 是某人的位置。原来在某人的位置上，逐渐成为代替的固定副词。',
 [['in + stead；较早 in stede','在某人、某物的位置上'],['合写 instead','替代、改用另一选择']],
 'do this instead 改做这个；instead of tea 用来代替茶；instead of going 改为不去或以别的活动替代去。of 后可接名词、代词、-ing。',
 'choose something else instead；instead of waiting。','instead 可独立：We walked instead。明确说代替什么，用 instead of：We walked instead of taking the bus。不要把 instead 后直接硬接普通名词。',
 ('We had tea instead of coffee.','我们没喝咖啡，改喝了茶。'),('I was too tired to cook, so we ordered food instead.','我累得不想做饭，于是我们改叫了外卖。'),sources=['https://www.etymonline.com/word/instead','https://en.wiktionary.org/wiki/instead#English'])
W('enough','/ɪˈnʌf/','足够的；足够地；够了',
 '需求是一条线，现有的数量或能力已经够到它：enough。I’ve had enough 还可把忍耐也当成一个已经满了的容量。',
 '接古英语 genog 足够，旧 ge- 为加强、集合等前缀，与拉丁 com- 有更远同源关系；后部接达到、取得的旧材料。经中古英语变化形成 enough，现代 gh 在这里读 /f/。',
 [['古英语 genog 等日耳曼语材料','旧前缀 ge- + 达到、取得相关材料；数量够用'],['现代 enough','足够数量、足够程度；忍耐已够的表达']],
 'enough time 足够时间；warm enough 够暖；enough to share 足够分享；have had enough 受够了。名词前放 enough，形容词、副词后放 enough。',
 'good enough；old enough to do something；that’s enough。','enough money 中 enough 在名词前；tall enough 中在形容词后。它表示达到所需，不等于越多越好；too much 反而说超过合适范围。',
 ('We have enough food for everyone.','我们的食物够所有人吃。'),('The room is warm enough without the heater.','不用暖气，房间也够暖。'),sources=['https://www.etymonline.com/word/enough','https://en.wiktionary.org/wiki/enough#English'])
W('terrified','/ˈterɪfaɪd/','非常害怕的；被吓坏了；terrify 的过去式、过去分词',
 '恐惧落到这个人身上，已经吓得厉害。terrified of heights 说怕高怕得很，不只是觉得不舒服。',
 'terrify 词末 y 变 i 加 -ed；-ed 读 /d/。继承拉丁使害怕词族，分词形容词常描述感到恐惧的一方。',
 [['拉丁惊吓词族 → terrify','使人强烈害怕'],['terrify + -ed → terrified','使害怕的过去；被吓到的状态']],
 'terrified of something 非常怕某物；terrified to do 不敢去做；terrified that 担心某事发生而极害怕；absolutely terrified 怕极了。',
 'a terrified child；look terrified。','terrified 多说体验恐惧的人或动物；terrifying 多说造成恐惧的东西。The film was terrifying；the audience was terrified。',
 ('She is terrified of heights.','她非常怕高。'),('The loud crash left the dog terrified.','那声巨响把狗吓坏了。'),sources=['https://www.etymonline.com/word/terrify','https://en.wiktionary.org/wiki/terrified#English'])
W('terrifying','/ˈterɪfaɪɪŋ/','吓人的、令人非常害怕的；terrify 的 -ing 形式',
 '事情本身把恐惧带给别人：一次险遇、一段突然的声音，都可能是 terrifying。它从造成恐惧这一方来描写。',
 'terrify 保留词末 y 加 -ing，形成分词及常用形容词；与 terrified 的 y 变 i 加 -ed 区别记。',
 [['terrify','使人强烈害怕'],['terrify + -ing → terrifying','正在使害怕；具有吓人作用的']],
 'a terrifying experience 可怕经历；a terrifying noise 吓人声响；a terrifying thought 可怕念头；absolutely terrifying 极其吓人。',
 'find something terrifying；a terrifying moment。','terrifying 不是这个东西自己在害怕，而是它引起恐惧。词形说明作用方向，terrified 说明受到影响后的感受。',
 ('It was a terrifying experience, but everyone returned safely.','那是一次吓人的经历，但所有人都安全回来了。'),('The thought of losing the records was terrifying.','一想到记录可能丢失，就让人非常害怕。'),sources=['https://www.etymonline.com/word/terrify','https://en.wiktionary.org/wiki/terrifying#English'])
W('targeting','英 /ˈtɑːɡɪtɪŋ/；美 /ˈtɑːrɡɪtɪŋ/','针对、面向、选定目标；target 的 -ing 形式',
 '先圈定希望影响的对象，再把帮助、信息或资源对准它。targeting 抓住这个选定并朝向的过程。',
 'target + -ing；现代接靶子、目标名词转成的针对动词。较早小盾历史已留在 base target 中，今天按针对哪个对象理解。',
 [['target 的目标义 → 动词 target','把某人某物选定为目标'],['target + -ing → targeting','针对的动作、过程或方法']],
 'targeting a specific audience 面向特定受众；targeting resources at a problem 把资源集中到某问题；better targeting 更精准地选定对象。',
 'a targeting strategy；targeting new readers。','targeting 说选定、面向对象，reaching 说触达；选中了对象，不等于信息一定已被所有目标人群看见。',
 ('The campaign is targeting new readers.','那项宣传活动面向新读者。'),('Better targeting helped the programme reach families who needed support.','更准确地确定对象，帮助那项计划触达了需要支持的家庭。'),sources=['https://www.etymonline.com/word/target','https://en.wiktionary.org/wiki/targeting#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_uq',ROOTS,WORDS)
 extend_lessons()
