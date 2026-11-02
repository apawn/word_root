"""Staying stuck, sudden impacts, smells, shrinking, sweeping and tears."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2990':dict(words=['stick','stuck'],label='stick 与 stuck：粘住、卡住',note='stick → stuck → stuck；stuck 作形容词常说无法移动、无法推进，be stuck on 也有着迷、偏爱等搭配义。'),
 'B2993':dict(words=['strike','struck'],label='strike 与 struck：击中与突然想到',note='strike → struck → struck；stricken 在特定形容词、分词搭配中仍存在，不能当所有 struck 的任意替换。'),
 'B2991':dict(words=['sting','stung'],label='sting 与 stung：刺痛',note='sting → stung → stung；旧过去式曾有 stang 等，后来过去式和分词统一为 stung。'),
 'A1699':dict(words=['stink','stank','stunk','stinky','stench'],label='stink 与 stinky：臭味及难闻的',note='stink 旧时可说发出任何气味，后来难闻义占主导；stinky 是现代 stink + -y。stench 是同族的旧名词，不能硬当成现代规则后缀派生。'),
 'B2508':dict(words=['shrink','shrank','shrunk'],label='shrink：尺寸缩小与畏缩',note='shrink → shrank → shrunk 是常见组合；shrunk 也可见过去式。衣物变小、身体后缩、畏缩回避各有实际搭配。'),
 'B2996':dict(words=['sweep','swept'],label='sweep 与 swept：一片扫过',note='sweep → swept → swept；sweep 的具体早期形式路径有不同解释，不把现代形式硬画成唯一音变路线。'),
 'A1741':dict(words=['weep','wept','weeping'],label='weep 与 weeping：流泪、垂枝',note='weep → wept → wept；weeping 可表流泪，也用于枝条下垂的树名。树枝形状的比喻与真实流泪要分开。'),
 'B2438':dict(words=['leap','leapt','leaped'],label='leap 的两种常用过去形式',note='leapt 与 leaped 都用；leapt 常读 /lept/，leaped 常读 /liːpt/。过去式、过去分词选用存在地区和个人习惯差别。'),
}
W('stuck','/stʌk/','粘住、卡住的；陷住、难以推进的；stick 的过去式、过去分词',
 '抽屉拉不开、车陷在泥里、一道题想不下去：都有被固定在原处、推进不了的感觉。',
 'stick 动词接古英语 stician 等刺入、保持固定的词族材料，现代过去式、分词固定常用 stuck。粘住、卡住的结果又成为常见形容词。',
 [['较早 stick 的刺入、固定词族','使固定；保持附着'],['现代 stick → stuck → stuck','粘住；卡住、陷住的状态']],
 'stuck a note on the fridge 把便条贴到冰箱上；be stuck in traffic 堵在路上；get stuck on a question 卡在一道题上；be stuck with something 只好面对某物。',
 'stuck in the mud；stuck for ideas。','I stuck it on 是我把它贴上了；it is stuck on 是它附着在上面。stuck 的过去时间还是当前状态，要看整句结构。',
 ('The drawer is stuck, and I can’t open it.','抽屉卡住了，我打不开。'),('We got stuck in traffic on the way home.','回家的路上我们堵在了车流中。'),sources=['https://www.etymonline.com/word/stick','https://en.wiktionary.org/wiki/stuck#English'])
W('struck','/strʌk/','击中了；突然想到；留下印象；strike 的常用过去式、过去分词',
 '球击中窗户，是实物撞上去；一个念头突然击中脑子，就是 it struck me。不同搭配把击中转到身体、感觉或想法。',
 'strike 接古英语 strican 抚过、擦过、移动等，后来发展出打击、碰撞义。struck 是这条旧动词词族在后续英语中形成的现代常用过去形式。',
 [['古英语 strican 词族 → 后来的打击义','擦过、移动；发展为击打等'],['现代 strike → struck → struck','击中；思想或印象突然触动']],
 'struck the wall 击中墙；it struck me that 突然想到；struck a deal 达成协议；struck a match 划着火柴；struck a balance 找到平衡。',
 'was struck by the beauty；struck me as unusual。','struck me as odd 是让我觉得奇怪；it struck me that 是我突然想到。stricken 常用于受某种打击的形容词搭配，不必处处替换 struck。',
 ('The ball struck the window.','球击中了窗户。'),('It struck me that we had met before.','我突然想起我们以前见过。'),sources=['https://www.etymonline.com/word/strike','https://en.wiktionary.org/wiki/struck#English'])
W('stung','/stʌŋ/','蜇了、刺痛了；刺伤感情；sting 的过去式、过去分词',
 '蜜蜂一蜇，疼得尖锐；一句刻薄话也像扎了一下，让人心里刺痛。',
 'sting 接古英语 stingan 刺、扎，旧过去式有 stang，分词 stungen 等；后来过去形式统一成 stung。词尾 -ng 是词干的一部分。',
 [['古英语 stingan、stang、stungen 等','刺、扎及旧变位'],['现代 sting → stung → stung','蜇伤、刺痛；感情受刺痛']],
 'was stung by a bee 被蜜蜂蜇了；the smoke stung her eyes 烟熏得她眼睛刺痛；stung by criticism 被批评刺痛。',
 'stung on the hand；deeply stung by the remark。','stung 的痛感常是尖锐的一下；hurt 用法更广。眼睛被烟熏得刺痛也能 stung，不要求真的有针刺入。',
 ('A bee stung him on the hand.','一只蜜蜂蜇了他的手。'),('Her careless remark stung him more than she realized.','她那句随口的话比她以为的更伤他的心。'),sources=['https://www.etymonline.com/word/sting','https://en.wiktionary.org/wiki/stung#English'])
W('stink','/stɪŋk/','发臭；口语：很糟、很不擅长；臭味',
 '气味冲鼻子，让人想把窗户打开，是 stink。口语把这种让人受不了的感觉拿来评价事情：This stinks，真糟。',
 '接古英语 stincan，早期可说散发各种气味，难闻义也很早存在，后来占主导。现代负面评价等用法接难闻、令人不快的分支。',
 [['古英语 stincan','散发气味；原先不限于臭味'],['现代 stink → stank／stunk → stunk','发臭；负面评价、表现很差']],
 'the bin stinks 垃圾桶很臭；stink of smoke 一股烟味；stink at tennis 网球打得很差；raise a stink 大声抗议、闹起来。',
 'stink up the room；This really stinks。','smell 可以中性地说气味，stink 通常已经带明显负面评价。stink at 是不擅长某事的口语，说人时语气会很直接。',
 ('The bin stinks; we should take it outside.','垃圾桶很臭，我们该把它拿到外面去。'),('I enjoy the game, even though I stink at it.','虽然我玩得很差，但还是喜欢这个游戏。'),sources=['https://www.etymonline.com/word/stink','https://en.wiktionary.org/wiki/stink#English'])
W('stank','/stæŋk/','发臭了、有难闻气味；stink 的过去式之一',
 '回忆某处当时的味道：屋里一股烟味，袜子臭得厉害。stank 负责把发臭放到过去。',
 'stink 接古英语 stincan，旧过去式 stanc 等与现代 stank 相承。现代过去式可见 stank，也可见 stunk；过去分词常用 stunk。',
 [['古英语 stincan、stanc 等','散发气味及旧过去形式'],['现代 stank','stink 的过去式之一']],
 'stank of smoke 当时一股烟味；stank of fish 有鱼腥味；stank after the game 比赛后很臭。of 后通常点明臭味来源或特征。',
 'the room stank；stank terribly。','stank 是 /æ/，stunk 是 /ʌ/。现代确有变体，学习时先记 stink → stank → stunk 这一常见组。',
 ('The room stank of cigarette smoke.','房间里一股难闻的香烟味。'),('His socks stank after the long walk.','走了很长的路后，他的袜子很臭。'),sources=['https://www.etymonline.com/word/stink','https://en.wiktionary.org/wiki/stank#English'])
W('stunk','/stʌŋk/','发过臭、很糟；stink 的过去分词，也可作过去式',
 '气味已经难闻了一阵子，或回头说某次表现糟糕，都可能遇到 stunk。',
 '接 stink 的旧分词材料，古英语有 stuncen 等。现代 stunk 常作过去分词，也用于一般过去；变化中保留了旧分词的元音。',
 [['古英语 stincan、stuncen 等','发出气味与相应分词'],['现代 stunk','常用过去分词；也见过去式']],
 'has stunk for days 臭了好几天；the place stunk 那地方当时很臭；the performance stunk 那场表现实在很差，属口语负面评价。',
 'have stunk of something；stunk up the kitchen。','stunk 作过去式是实际存在的变体；完成结构通常 has stunk。stank 与 stunk 常用过去形式有差异，按整句时态和实际搭配理解。',
 ('The cupboard has stunk of damp wood for weeks.','橱柜已经有好几周都带着一股难闻的潮木头味。'),('The fish stunk up the whole kitchen.','那条鱼把整个厨房弄得臭烘烘的。'),sources=['https://www.etymonline.com/word/stink','https://en.wiktionary.org/wiki/stunk#English'])
W('stinky','/ˈstɪŋki/','臭烘烘的；有难闻气味的',
 '闻起来让人皱鼻子的袜子、垃圾桶，可以直白地叫 stinky。语气比正式描述更日常。',
 'stink 发臭 + 形容词后缀 -y，表示有这种气味、特征。继承臭味分支，不给 -y 另编一段历史含义。',
 [['stink','发臭、臭味'],['stink + -y → stinky','带臭味的；日常形容词']],
 'stinky socks 臭袜子；a stinky bin 臭垃圾桶；stinky cheese 气味很重的奶酪，喜好可以因人而异。',
 'a stinky smell；something stinky。','stinky 明确说气味难闻；smelly 也常说不好闻。fragrant、scented 往往往香味方向走，不能都翻成同一种有气味。',
 ('He left his stinky shoes outside the door.','他把臭烘烘的鞋留在门外。'),('We opened the windows to air out the stinky room.','我们打开窗户，给那间臭烘烘的房间换气。'),sources=['https://en.wiktionary.org/wiki/stinky#English'])
W('stench','/stentʃ/','浓烈的臭味、恶臭',
 '不是凑近才勉强闻到，而是一股难闻的味道迎面扑来。stench 常比普通 smell 更强、更负面。',
 '接古英语 stenc、stync 等气味名词，与 stink 属旧词族。旧词也能指一般气味、香气，现代恶臭义固定下来；不能把 -ench 当现代通用名词后缀。',
 [['古英语 stenc、stync 等；与 stink 同族','气味、散出的味道'],['现代 stench','强烈难闻的气味']],
 'the stench of rotten food 腐烂食物的恶臭；an awful stench 难闻的恶臭；the stench filled the room 臭味充满房间。',
 'a strong stench；the stench from the drain。','stench 是名词，stink 可作动词也可作名词。a faint smell 只是淡淡的气味；a terrible stench 已经给出很强的负面感受。',
 ('A terrible stench came from the old drain.','旧排水口传来一股恶臭。'),('The stench of rotten food filled the kitchen.','腐烂食物的臭味充满了厨房。'),sources=['https://www.etymonline.com/word/stench','https://en.wiktionary.org/wiki/stench#English'])
W('shrank','/ʃræŋk/','缩小了；退缩了；shrink 的常见过去式',
 '毛衣洗完小了一圈，人害怕时往后缩，也都有往里收、往回缩的画面。',
 'shrink 接古英语 scrincan 收缩、萎缩，旧过去式 scranc、分词 scruncen 等。现代常记 shrink、shrank、shrunk。',
 [['古英语 scrincan、scranc 等','身体收缩、萎缩及其过去形式'],['现代 shrank','尺寸缩小；身体或心理退缩']],
 'the sweater shrank 毛衣缩水了；the crowd shrank 人群变少；shrank back 后退、畏缩；shrank from responsibility 畏惧承担责任。',
 'shrank in the wash；shrank to half its size。','shrank 是常见过去式，shrunk 也会用于过去式。shrink from 常接不愿面对的事情，画面是往后退。',
 ('My sweater shrank in the wash.','我的毛衣洗缩水了。'),('The child shrank back when the dog barked.','狗叫时，孩子吓得往后缩。'),sources=['https://www.etymonline.com/word/shrink','https://en.wiktionary.org/wiki/shrank#English'])
W('shrunk','/ʃrʌŋk/','已缩小、缩水；shrink 的过去分词，也可作过去式',
 '原来的大小留在记忆里，眼前已经小了一圈。has shrunk 常让人注意到这种缩小后的结果。',
 '接 shrink 的旧分词材料，古英语有 scruncen 等；现代 shrunk 常作过去分词，也见作过去式。形容词还常用 shrunken。',
 [['古英语 scrincan、scruncen 等','收缩与相应分词'],['现代 shrunk；相关形容词 shrunken','已经缩小、收缩的结果']],
 'has shrunk 已缩小；the shirt has shrunk 衬衫缩水了；the budget has shrunk 预算减少了。',
 'shrunk considerably；shrunk over the years。','has shrunk 与 a shrunken sweater 结构不同。shrunken 常放在名词前形容缩小的状态，shrunk 常接在完成结构中。',
 ('The shirt has shrunk, so it no longer fits.','衬衫缩水了，已经不合身。'),('The number of visitors has shrunk this year.','今年的访客人数减少了。'),sources=['https://www.etymonline.com/word/shrink','https://en.wiktionary.org/wiki/shrunk#English'])
W('swept','/swept/','扫了、席卷了；迅速掠过；sweep 的过去式、过去分词',
 '扫帚一带，灰尘被推走；风、浪、人群也能像一大片力量扫过来。swept 不必真的拿着扫帚。',
 'sweep 在中古英语有 swepen 等形式，与更早 swope、古英语 swapan 或斯堪的纳维亚相关材料的具体路径有不同解释。现代 sweep、swept、swept 已固定。',
 [['中古英语 swepen 等扫动词；早期路径有不同解释','扫除；后来也说迅速而有力地通过'],['现代 sweep → swept → swept','扫过、扫走、席卷']],
 'swept the floor 扫了地；swept away the leaves 扫走叶子；swept across the country 席卷全国；swept to victory 大获全胜。',
 'swept through the room；swept off one’s feet。','sweep /swiːp/ 与 swept /swept/ 的元音不同。was swept away 可说真被水冲走，也可说情感上被深深打动，要看对象与场景。',
 ('She swept the kitchen floor after dinner.','晚饭后，她扫了厨房地板。'),('A strong wind swept the leaves across the yard.','一阵大风把树叶卷过院子。'),sources=['https://www.etymonline.com/word/sweep','https://en.wiktionary.org/wiki/swept#English'])
W('weep','/wiːp/','哭泣、流泪；哀悼；缓缓渗出',
 '眼泪一滴滴落下来，常带悲伤，也可以喜极而泣。weep 比日常 cry 更偏重流泪这一面。',
 '接古英语 wepan，旧有流泪、哭诉、哀悼等义；较早是强变化词族，现代常用过去式、过去分词 wept。渗出液体的比喻也很早出现。',
 [['古英语 wepan 等哭泣词族','流泪、哀悼、哭诉'],['现代 weep → wept → wept','流泪；有时比喻缓缓渗液']],
 'weep with joy 喜极而泣；weep for someone 为某人流泪；weep over a loss 因失去而哭泣。说墙面 weep 时可指渗出湿气。',
 'weep quietly；weep bitterly。','cry 可以泛指哭，也可以喊；weep 主要落在流泪、悲泣。sob 则把抽噎、一顿一顿的哭声突出出来。',
 ('She began to weep when she read the letter.','读到那封信时，她开始流泪。'),('He wept with relief when he heard the good news.','听到好消息时，他如释重负地哭了。'),sources=['https://www.etymonline.com/word/weep','https://en.wiktionary.org/wiki/weep#English'])
W('wept','/wept/','哭了、流泪了；weep 的过去式、过去分词',
 '事情已经触动人，眼泪落过。wept 可以接悲伤，也可以接团聚、放心后的激动。',
 '接 weep 的旧哭泣词族；古英语有强变化 weop、wopen 等，后来的英语改用 wept 这套形式。现代结尾 t 不意味着它从古至今只有同一变位规则。',
 [['古英语 wepan、weop、wopen 等','流泪及旧变位'],['后起 wept → 现代 weep、wept、wept','现代常用过去式、过去分词']],
 'wept quietly 静静流泪；wept for joy 高兴得哭了；had wept all night 曾哭了一整夜。',
 'wept over the letter；wept with relief。','weep /wiːp/ 与 wept /wept/ 的元音不同。wept 常比 cried 稍有书面、叙述色彩，具体悲喜由搭配决定。',
 ('She wept quietly on the train home.','回家的火车上，她静静地流泪。'),('They wept with joy when they were reunited.','重聚时，他们喜极而泣。'),sources=['https://www.etymonline.com/word/weep','https://en.wiktionary.org/wiki/wept#English'])
W('weeping','/ˈwiːpɪŋ/','哭泣、流泪；垂枝的；weep 的 -ing 形式',
 '人低头流泪；柳树枝条向下垂，看起来也像低头哭泣。weeping willow 的名字借了这种姿态。',
 'weep + -ing；作为流泪的分词、名词有很长历史。后来用于枝条弯垂的树木名称，形成形状比喻。',
 [['weep + -ing → weeping','哭泣、正在流泪；伴有眼泪的'],['形状比喻 → weeping willow 等','枝条下垂，姿态像低头流泪']],
 'was weeping 正在哭泣；a weeping child 哭泣的孩子；a weeping willow 垂柳；weeping branches 下垂的枝条。',
 'quiet weeping；branches of a weeping willow。','weeping willow 用低垂姿态给树形命名。普通 weeping 是否表进行时，要看 was、is 等整句结构。',
 ('She heard a child weeping in the next room.','她听见隔壁房间有个孩子在哭。'),('A weeping willow shaded the edge of the pond.','一棵垂柳为池塘边遮着阴。'),sources=['https://www.etymonline.com/word/weep','https://en.wiktionary.org/wiki/weeping#English'])
W('leapt','/lept/，也有 /liːpt/ 等变体','跳了、跃过了；猛增了；leap 的过去式、过去分词之一',
 '身体一下跃起来，越过小溪；价格一下跳到更高处，也能用 leapt。',
 'leap 接古英语 hleapan 的跳跃词族，旧时有强变化；现代 leapt 与 leaped 并存，都是常用过去式、过去分词，地区偏好有差别。',
 [['古英语 hleapan 等跳跃词族','离地跃起、跳过'],['现代 leaped／leapt','两种常用过去式、过去分词']],
 'leapt over the stream 跃过小溪；leapt to his feet 一下站起来；leapt at the chance 急忙抓住机会；prices leapt 价格猛涨。',
 'leapt forward；leapt into the air。','leapt 常读 /lept/，leaped 常读 /liːpt/，也有变体。leap at a chance 是抓住机会，不要逐字译成朝机会跳过去。',
 ('The dog leapt over the narrow stream.','狗跃过了狭窄的小溪。'),('She leapt at the chance to join the expedition.','她立刻抓住了参加考察的机会。'),sources=['https://www.etymonline.com/word/leap','https://en.wiktionary.org/wiki/leapt#English'])
W('leaped','/liːpt/，也有 /lept/ 等变体','跳了、跃过了；leap 的过去式、过去分词之一',
 '双脚用力，一下跃起来，或一下抓住机会，过去都能用 leaped。它与 leapt 是同一个动词的两种常用写法。',
 '现代 leap + -ed；leap 承接古英语 hleapan 的跳跃词族。较早词族有强变化，现代规则形式 leaped 与 leapt 并行。',
 [['古英语 hleapan → leap','跳、跃起、越过'],['现代 leap + -ed → leaped','规则过去式、过去分词；与 leapt 并用']],
 'leaped over a wall 跃过墙；leaped out of bed 一下跳下床；leaped at an offer 急忙接受提议；the number leaped 数字猛增。',
 'leaped into the water；has leaped forward。','leaped 中 -ed 常读 /t/，全词一个音节。leaped 与 leapt 没有跳高和跳远之类的词义分工，地区和个人习惯会影响选择。',
 ('The cat leaped onto the windowsill.','猫跳上了窗台。'),('He leaped out of bed when he heard the alarm.','听到闹钟响，他一下从床上跳起来。'),sources=['https://www.etymonline.com/word/leap','https://en.wiktionary.org/wiki/leaped#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ud',ROOTS,WORDS)
 extend_lessons()
