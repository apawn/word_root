"""Holding fast, settling a result, twitching and repetitive hand movements."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A2238':dict(words='jiggle jiggles jiggled jiggling'.split(),label='jiggle 的反复小晃动与现代变化',note='jig 的抖、跳材料加旧 -le 形成 jiggle，也可能受 jog 影响；现代去不发音 e 后加完整 -ed、-ing。'),
 'A1760':dict(words='cling clings clung clinging clench clinch clinches clinched clinching tweak twitch twitches twitched twitching twang twangs twanged twanging strum strums strummed strumming fidget fidgets fidgeted fidgeting fiddle fiddles fiddled fiddling jiggle jiggles jiggled jiggling'.split(),label='贴紧、锁定、抽动、弹扫和手上小动作',note='clung 是 cling 的不规则过去式、分词，不带 -ed；clinched、twitched 的词尾读 /t/，twanged、strummed、fiddled 读 /d/，fidgeted 读 /ɪd/。'),
}
CLING=[['古英语 clingan → cling','牢靠贴住、黏附，也有凝结、萎缩旧义'],['贴紧不放 → 抱住人、坚持希望或旧观念','现代可把身体、衣物和心里执着都放在“不愿脱开”的画面里理解']]
W('cling','/klɪŋ/','紧抓、抱紧；黏附、贴紧；依恋、坚持不放',
 '孩子抱着大人不松手，湿衣贴在身上，心里抓着一点希望不肯丢，都像 cling：贴住、拉不开。',
 '承古英语 clingan 的牢靠贴住、凝结等材料；现代 cling → clung，不靠加 -ed 变过去式。clench 是相关旧使动词的一支。',CLING,
 'cling to a rail 是紧抓栏杆，cling to hope 是抱住希望；clothes cling 是衣服贴身，cling to someone 也可说情感上依赖。',
 'cling together 紧靠在一起；cling to an old idea 固守旧观念。',
 'cling 常带紧、不愿松开的感觉，hold 更中性；孩子 cling to a parent，常比普通牵手更有依赖、怕分开的画面。',
 ('The wet shirt began to cling to his back.','湿衬衫开始紧贴他的背。'),('They continued to cling to the hope of finding the dog.','他们仍抱着找到狗的希望不放。'),sources=S('cling','cling'))
W('clings','/klɪŋz/','紧抓、黏附、依恋、坚持不放〔第三人称单数〕',
 '一件湿衣紧贴身体，或一个人总抓住旧想法，用 clings。东西、人、观念都能呈现紧贴不放的状态。',
 'cling + -s，/ŋ/ 后读 /z/，结尾 /ŋz/；现代三单规则加 s，过去式则另为 clung。',CLING+[['cling + -s → clings','它贴紧；他、她坚持、依附']],
 'clings to the wall 是贴住墙，clings to her hand 是紧抓她的手，clings to the belief 是坚持那个看法；常用 to 接对象。',
 'clings tightly 紧紧贴住；mud clings to shoes 泥黏在鞋上。',
 'clings to an idea 不一定赞成或贬低该想法，只强调抓得紧；说 outmoded ideas 才把旧、过时的评价加出来。',
 ('Mud clings to the soles of my shoes.','泥黏在我的鞋底。'),('She clings to the belief that things can improve.','她始终坚信事情能够好转。'),sources=S('clings','cling'))
W('clung','/klʌŋ/','紧抓、黏附、抱紧了；坚持、依恋着〔过去式、过去分词〕',
 '刚才孩子紧抱着、湿叶贴着地，或人一直没放掉希望，是 clung。换成过去，贴紧不放的画面仍一样。',
 'cling → clung，元音由 /ɪ/ 变 /ʌ/；现代过去式、过去分词同形，是旧强变化材料延续后的不规则形式。',CLING+[['cling → clung','过去或完成时紧贴、抱住、坚持']],
 'clung to the rope 是紧抓绳子，had clung to hope 是此前一直抱住希望；没有词尾 -ed。',
 'clung together 紧抱在一起；clung to the wall 贴在墙上。',
 'clung 通常接 to 再接对象，clutched 可直接接宾语；clung to the rail 与 clutched the rail 都能说紧抓，句型不同。',
 ('The child clung to her father\'s hand.','孩子紧紧抓着爸爸的手。'),('Wet leaves clung to the pavement.','湿叶贴在路面上。'),sources=S('clung','cling'))
W('clinging','/ˈklɪŋɪŋ/','正在紧抓、贴紧、依恋；贴身的、黏着的',
 '人正抱着不放，或布正贴住身体，是 clinging；衣服作 clinging 时像紧贴轮廓，情感里则可能过分依赖。',
 'cling + 完整 -ing，直接加；ng 保留 /ŋ/，后接元音也不凭空加一个 /ɡ/。',CLING+[['cling + -ing → clinging','紧贴、抱持的过程或性质']],
 'clinging to a rope 是正紧抓绳，clinging clothes 是紧贴身体的衣服；clinging to the past 是放不下过去。',
 'clinging together 紧紧靠在一起；a clinging child 黏着大人的孩子。',
 'clinging 可以是布料或手的实际贴紧，也可以是心理不肯放手；是否令人不适取决于具体对象，词形本身不只一种评价。',
 ('He stood clinging to the rail with both hands.','他站着，双手紧紧抓着栏杆。'),('She was still clinging to the hope that he would return.','她仍抱着他会回来的希望不放。'),sources=S('clinging','cling'))
CLINCH=[['clench 的变体 → clinch 的紧固动作','较早把钉尖敲弯，使钉子固定、不易拔出'],['锁牢 → 敲定、锁定；拳击中近身抱住','现代胜局、协议像最后一锤固定住；缠抱另沿紧固身体动作发展']]
W('clinch','/klɪntʃ/','敲定、锁定、赢得；近身缠抱；紧固',
 '比分还没稳，最后一球让胜负基本定了，是 clinch the win；谈判最后一项同意下来，是 clinch the deal。像把钉尖敲弯，结果锁牢了。',
 '原是 clench 的变体，较早指把已打入的钉尖弯折、敲牢；决定性解决的比喻从这种固定动作发展，拳击紧抱又有相应动作支。',CLINCH,
 'clinch a deal 是敲定交易，clinch victory 是锁定胜利；in a clinch 可说拳击中近身抱在一起。',
 'clinch the title 锁定冠军；clinch the argument 为论点作决定性证明。',
 'clinch 强调最后把结果定住，pursue 只是追求；还在争取冠军是 pursue，拿到决定性结果才更像 clinch。',
 ('The final goal helped them clinch the victory.','最后那个进球帮助他们锁定胜利。'),('The boxers became locked in a clinch.','两名拳击手近身缠抱在一起。'),sources=S('clinch','clinch'))
W('clinches','/ˈklɪntʃɪz/','敲定、锁定、紧固〔第三人称单数〕；缠抱、紧固处〔复数〕',
 '一个证据把争论最后定下来，或一球让胜局落定，用 clinches；拳击中的几次紧抱则是名词复数。',
 'clinch + -es，/tʃ/ 后读 /ɪz/；动词三单与缠抱、紧固名词复数同形。',CLINCH+[['clinch + -es → clinches','它把结果定住；几次缠抱']],
 'clinches the argument 是为论点作决定性证明，clinches a place 是锁定一个名额；break up clinches 是分开近身缠抱。',
 'clinches the deal 敲定交易；repeated clinches 反复的近身缠抱。',
 'clinches a title 是拿到足以确定冠军的结果，defends a title 是争取卫冕、保卫头衔；后者不自动保证这次也获胜。',
 ('This final piece of evidence clinches the argument.','最后这条证据把论点彻底坐实了。'),('The referee separated the boxers after several clinches.','几次近身缠抱之后，裁判把拳击手分开。'),sources=S('clinches','clinch'))
W('clinched','/klɪntʃt/','敲定、锁定、赢得了；缠抱、紧固了',
 '刚才的一步让结果不再悬着，是 clinched；一个名额、一场胜利、一个协议终于落定，都能带这种最后锁牢的感觉。',
 'clinch + 完整 -ed，/tʃ/ 后读 /t/，结尾 /ntʃt/；现代规则过去式、分词。',CLINCH+[['clinch + -ed → clinched','结果已定住；过去缠抱、锁牢']],
 'clinched the championship 是锁定冠军，clinched the deal 是敲定交易，clinched a place in the final 是锁定决赛名额。',
 'clinched victory 锁定胜利；clinched the argument 决定性证明论点。',
 'clinched 常说有一个关键动作、证据让结果确定，improved 只说变好；比分领先一点不自动等于已 clinched victory。',
 ('Their last win clinched a place in the final.','最后那场胜利让他们锁定了决赛名额。'),('The extra evidence clinched the argument.','补充证据把论点彻底坐实了。'),sources=S('clinched','clinch'))
W('clinching','/ˈklɪntʃɪŋ/','正在敲定、锁定、紧固、缠抱；起决定作用的',
 '事情正被最后一锤定住，是 clinching；a clinching argument 像那枚最后锁住的钉子，让对方难再反驳。',
 'clinch + 完整 -ing，直接加；分词可描述敲定过程，也可修饰起决定作用的证据、论证等。',CLINCH+[['clinch + -ing → clinching','锁定过程；有决定性作用的性质']],
 'clinching the title 是正锁定冠军，a clinching piece of evidence 是决定性证据；拳击 clinching 又是近身缠抱。',
 'a clinching argument 决定性论据；clinching the deal 敲定交易。',
 'clinching 的决定性用法说明足以把结果落定，helpful 只是有帮助；有用的信息还可能不是最后定论。',
 ('She supplied the clinching piece of evidence.','她提供了那条决定性证据。'),('The team celebrated clinching a place in the final.','球队庆祝锁定了决赛名额。'),sources=S('clinching','clinch'))
TWITCH=[['古英语 twiccian → 中古英语 twicchen → twitch','拔、急扯、抓住，和 tweak 的相关材料可比较'],['急扯小动作 → 肌肉短促抽动；相关名词','现代常是眼皮、嘴角、耳朵忽然微动，不一定持续抖']]
W('twitch','/twɪtʃ/','抽动、颤动、急促拉动；抽动一下',
 '眼皮忽然跳一下，猫耳朵迅速动一下，是 twitch。像一个局部被短促拉了下，动作很快就过去。',
 '承古英语 twiccian 的拔、急扯材料，经中古英语 twicchen；较早主动拉扯，后来也说肌肉自己短促收动。',TWITCH,
 'an eye twitch 是眼皮抽动，ears twitch 是耳朵快动；twitch the curtain aside 是把帘子急促拉开一点。',
 'a slight twitch 轻微一抽；twitch at the corner of the mouth 嘴角动一下。',
 'twitch 常是一个部位短促一抽，tremble 更能说持续发抖；一只耳朵 twitch 不等于整只动物一直在抖。',
 ('I saw the cat\'s ear twitch.','我看见猫的耳朵快动了一下。'),('A slight twitch at the corner of his mouth suggested a smile.','他的嘴角轻轻一动，像要笑出来。'),sources=S('twitch','twitch'))
W('twitches','/ˈtwɪtʃɪz/','抽动、颤动、急拉〔第三人称单数〕；短促抽动〔复数〕',
 '一只耳朵或嘴角一下快动，叫 twitches；接连几个小抽动也可看作一下一下的名词复数。',
 'twitch + -es，/tʃ/ 后读 /ɪz/；动词三单和局部抽动名词复数同形。',TWITCH+[['twitch + -es → twitches','它短促微动；几下抽动']],
 'his eyelid twitches 是他眼皮跳，a few twitches 是几下抽动；主语经常直接是身体局部。',
 'twitches suddenly 忽然抽一下；tiny twitches 细微抽动。',
 'twitches 描写动作，不单凭它判断身体、情绪的原因；猫耳朵因声音动一下，也能用 twitches。',
 ('The rabbit\'s nose twitches as it sniffs.','兔子嗅闻时，鼻子一动一动。'),('We noticed a few small twitches in his fingers.','我们注意到他的手指轻轻抽了几下。'),sources=S('twitches','twitch'))
W('twitched','/twɪtʃt/','抽动、快动、急拉了一下',
 '刚才嘴角轻轻一跳，猫尾巴尖突然动了一下，是 twitched。它常把叙述缩到很小、很快的一次动作。',
 'twitch + 完整 -ed，/tʃ/ 后读 /t/，结尾 /tʃt/；基础短元音不改，整词不增 /ɪd/ 音节。',TWITCH+[['twitch + -ed → twitched','过去局部短促抽动或急拉']],
 'his mouth twitched 是他嘴角动了动，twitched the curtain aside 是急拉开帘子一点；后者是主动动作。',
 'twitched once 抽了一下；ears twitched 耳朵动了动。',
 'twitched 不必是大幅动作，jerked 常更显突然一拉、一顿；描述微小表情时 twitched 更能留住细节。',
 ('His mouth twitched as he tried not to laugh.','他忍着笑，嘴角动了动。'),('The cat\'s ears twitched at the sound.','听到声音，猫的耳朵快动了一下。'),sources=S('twitched','twitch'))
W('twitching','/ˈtwɪtʃɪŋ/','正在抽动、颤动、急促微动；抽动行为',
 '眼皮正跳，猫尾巴尖正一下下抽动，是 twitching；一个过程可以由连续几次很快的小动作构成。',
 'twitch + 完整 -ing，直接加；分词、动作名词同形，ch 仍读 /tʃ/。',TWITCH+[['twitch + -ing → twitching','短促微动连续发生的过程']],
 'a twitching tail 是抽动的尾巴，twitching at the mouth 是嘴角微动；look at the twitching ears 是看那快动的耳朵。',
 'twitching slightly 轻轻抽动；stop twitching 停止抽动。',
 'twitching 由短促的小抽构成，swaying 常是平缓来回摆；猫尾巴可以轻摆，也可以突然一下一下抽动，镜头不同。',
 ('The cat sat with the tip of its tail twitching.','猫坐着，尾巴尖一下一下抽动。'),('She noticed her eyelid twitching as she read.','看书时，她发现眼皮在跳。'),sources=S('twitching','twitch'))
TWANG=[['十六世纪 twang 的拟声材料','绷紧弦被拨后发出锐利、带余振的响声；动词记录也很早'],['弦嗡响 → 带鼻音的声音、某种口音特色','声音像拉紧的弦响，并不表示所有地方口音都粗俗、好笑']]
W('twang','/twæŋ/','弦的嗡响、铮响；带鼻音的腔调、口音特色；拨得嗡响',
 '绷紧的弦拉开再放，发出带余振的嗡声，是 twang。某些人的腔调带明显鼻音，也像弦声，叫 a twang。',
 '十六世纪出现的拟声词，模仿弓弦、琴弦等锐利振动声；后来扩到鼻音及地方腔调。名词、动词记录都较早，不按今天先讲哪个来定词史。',TWANG,
 'the twang of a string 是弦的一声嗡响，speak with a twang 是说话带某种鼻音腔调；twang the strings 是把弦拨响。',
 'a distinctive twang 独特腔调；a guitar twang 吉他的嗡响。',
 'twang 既可说声音，也可说让弦发这种声音的动作；strum 更具体说扫过弦，twang 更关注弦响出来的音色。',
 ('The string sprang back with a twang.','弦嗡地弹了回去。'),('She spoke with a faint regional twang.','她说话带着一点当地特有的鼻音腔调。'),sources=S('twang','twang'))
W('twangs','/twæŋz/','拨得嗡响、发出弦响〔第三人称单数〕；弦响、腔调〔复数〕',
 '一根弦被拉开弹回，嗡地响，是 twangs；接连几下弦声，也能当名词复数来听。',
 'twang + -s，/ŋ/ 后读 /z/；三单与声音、腔调名词复数同形，不额外加 /ɡ/。',TWANG+[['twang + -s → twangs','它嗡地响；几下弦响或几种腔调']],
 'the string twangs 是弦嗡响，twangs the string 是把弦拨响；a few twangs 是几下带弹振的响声。',
 'twangs sharply 锐利地响；the twangs of a banjo 班卓琴的几声铮响。',
 'twangs 是某类带弦振感的响，rings 更宽，可以是钟、电话或金属；并不是所有响声都带 twang 的音色。',
 ('The string twangs when he lets it go.','他一松手，弦就嗡地响。'),('A few sharp twangs came from the banjo.','班卓琴传来几声清亮的铮响。'),sources=S('twangs','twang'))
W('twanged','/twæŋd/','嗡地响了；把弦拨响了',
 '刚才一根紧弦被拨、弹回，响得有余振，是 twanged；可以是弦自己作主语，也可以人把弦拨响。',
 'twang + 完整 -ed，/ŋ/ 后读 /d/，结尾 /ŋd/；基础 ng 不需另加 /ɡ/。',TWANG+[['twang + -ed → twanged','过去发出弦振声或拨弦']],
 'the string twanged 是弦嗡地响了，twanged the guitar strings 是拨响吉他弦；以发出的声音质感为重点。',
 'twanged loudly 大声铮响；twanged a note 拨出一个带弦响的音。',
 'twanged 常能让读者“听见”紧弦的音色，plucked 更关注手指拉开再放的动作；同一次弹弦可从两方面说。',
 ('The bowstring twanged as it sprang back.','弓弦弹回时嗡地响了。'),('He twanged the lowest guitar string.','他把吉他最低的那根弦拨得嗡响。'),sources=S('twanged','twang'))
W('twanging','/ˈtwæŋɪŋ/','正在拨响、发出弦响；带弦振感的声音',
 '紧弦正一声声嗡响，或手正反复拨出这种声音，是 twanging；可以把动作和音色一起画出来。',
 'twang + 完整 -ing，直接加；ng 表示 /ŋ/，后接元音仍不多出 /ɡ/。',TWANG+[['twang + -ing → twanging','弦振响声、拨响的过程']],
 'twanging guitar strings 是嗡响的吉他弦或正在拨吉他弦，a twanging sound 是带绷弦余振的声音；看句型分角色。',
 'twanging on a banjo 拨响班卓琴；a twanging note 带弦振感的音。',
 'twanging 注重弦响音色，strumming 注重手怎样扫过弦；同样的吉他声，可以选择不同镜头描述。',
 ('He sat twanging the strings of his guitar.','他坐着，把吉他弦拨得嗡嗡响。'),('We heard a sharp twanging sound as the wire sprang back.','金属丝弹回时，我们听见一声锐利的嗡响。'),sources=S('twanging','twang'))
STRUM=[['十八世纪 strum 的弹弦词','可能模仿手指掠过琴弦的声音，较早有弹得不熟练的贬意'],['随手弹奏 → 现代扫弦、轻松弹弦','现代可中性说弹奏方式，不一律暗示演奏差']]
W('strum','/strʌm/','扫弦、弹拨弦乐器；扫弦一下、弹奏声',
 '手指或拨片一下扫过几根吉他弦，发出一个和弦，是 strum。像手横着从一排绷紧的细线上刷过去。',
 '十八世纪的弹弦词，可能拟声；早期有笨拙、随便弹奏的贬意，现代已可中性描述扫弦、休闲弹奏。',STRUM,
 'strum a guitar 是扫着弹吉他，strum a chord 是扫出一个和弦；a gentle strum 是轻轻一下扫弦或它的声音。',
 'strum along 跟着轻松弹；strum softly 轻轻扫弦。',
 'strum 常是一次扫过几根弦，pluck 可用手指单独拉放一根；两种手法都能演奏得很好，不用旧贬义评价今天的技术。',
 ('She began to strum a few chords on the guitar.','她开始在吉他上扫出几个和弦。'),('A gentle strum broke the silence.','轻轻一声扫弦打破了安静。'),sources=S('strum','strum'))
W('strums','/strʌmz/','扫弦、弹弦乐器〔第三人称单数〕；扫弦动作、声响〔复数〕',
 '一个人手扫过琴弦，用 strums；几下扫弦也能数作 strums，像一下一下把和弦刷出来。',
 'strum + -s，/m/ 后读 /z/；动词三单与扫弦名词复数同形，原来的单 m 不双写。',STRUM+[['strum + -s → strums','他、她扫弦；几下弹扫']],
 'strums the guitar 是扫弹吉他，strums a chord 是扫出和弦；a few quiet strums 是几下轻轻扫弦。',
 'strums along with the song 跟着歌扫弦；slow strums 缓慢的几下扫弦。',
 'strums 更具体讲弦上手法，plays 可以泛说演奏；plays the guitar 可能扫弦，也可能逐根拨。',
 ('He strums the guitar while his sister sings.','姐姐唱歌时，他扫弹吉他伴奏。'),('A few quiet strums were enough to set the rhythm.','轻轻扫了几下弦，节奏就带起来了。'),sources=S('strums','strum'))
W('strummed','/strʌmd/','扫弦、弹拨了',
 '刚才手扫过琴弦，奏出一串和弦，是 strummed；画面是整只手或拨片有节奏地掠过几根弦。',
 'strum 双写 m + 完整 -ed → strummed，/m/ 后读 /d/；短元音重读单音节按规则双写。',STRUM+[['strum 双写 m + -ed → strummed','过去扫弹琴弦']],
 'strummed the guitar 是扫弹了吉他，strummed a few chords 是扫出几个和弦；可认真弹，也可随手弹。',
 'strummed softly 轻轻扫弦；strummed along 跟着弹了。',
 'strummed 不自动说弹得好坏，只交代弹奏手法；off-key 等词才会另外评价音准。',
 ('She strummed a few chords while waiting for the others.','等其他人时，她扫出了几个和弦。'),('He strummed his guitar beside the campfire.','他在篝火旁扫弹吉他。'),sources=S('strummed','strum'))
W('strumming','/ˈstrʌmɪŋ/','正在扫弦、弹拨；扫弦手法、动作',
 '手正一下下横过弦，给歌带出节奏，是 strumming；也能把这种手法当一项技能来练。',
 'strum 双写 m + 完整 -ing → strumming；分词和动作名词同形，双写不多发一遍 /m/。',STRUM+[['strum 双写 m + -ing → strumming','扫弦过程；可练习的手法']],
 'strumming patterns 是扫弦节奏型，strumming a guitar 是正在扫弹吉他；gentle strumming 是轻柔的扫弦。',
 'practise strumming 练扫弦；strumming along 跟着扫弹。',
 'strumming 把焦点放在扫弦动作，twanging 更突出响出的弦振音色；不是两个词都只译成弹吉他就够了。',
 ('We could hear her strumming in the next room.','我们能听见她在隔壁扫弦。'),('He practised a new strumming pattern.','他练习一种新的扫弦节奏型。'),sources=S('strumming','strum'))
FIDGET=[['较早 fidge 的不安移动材料 → fidget','更远可能联系中古英语 fiken，一层层早期路线仍有不确定部分'],['不安、不断小动 → 手脚动个不停；坐不住的人','现代可写紧张、无聊时的小动作，不需每次解释为大幅移动']]
W('fidget','/ˈfɪdʒɪt/','坐立不安、手脚动个不停；摆弄；坐不住的人、小动作',
 '等得无聊，一会儿动脚、一会儿摸袖口，是 fidget。整个人未必走开，只是身体总有一点小动作停不住。',
 '联系较早 fidge 的不安移动词，更远或接中古英语 fiken；现代 fidget 是完整词，结尾不是 get 得到，也不按小称 -et 硬拆。',FIDGET,
 'fidget in a chair 是在椅子上动来动去，fidget with a pen 是不断摆弄笔；a fidget 可说总坐不住的人。',
 'stop fidgeting 别动来动去；a nervous fidget 紧张的小动作或不安的人。',
 'fidget 强调小动作多、坐不住，walk about 是走来走去；不离开椅子也可以一直 fidget。',
 ('I tend to fidget when I have to wait too long.','等得太久时，我容易手脚动个不停。'),('She was a terrible fidget during long meetings.','开长会时，她总是动来动去，坐不住。'),sources=S('fidget','fidget'))
W('fidgets','/ˈfɪdʒɪts/','手脚动个不停、摆弄〔第三人称单数〕；不安小动作、坐不住的人〔复数〕',
 '一个人等着时总动脚、摸东西，用 fidgets；the fidgets 又像一阵坐不住、浑身要动的不安。',
 'fidget + -s，/t/ 后读 /s/，结尾 /ts/；动词三单与人物、动作名词复数同形。',FIDGET+[['fidget + -s → fidgets','他、她动来动去；不安小动作或多人']],
 'fidgets with her keys 是总摆弄钥匙，fidgets in his seat 是在座位上不停动；have the fidgets 是有些坐立不安。',
 'fidgets nervously 紧张地动来动去；gets the fidgets 开始坐不住。',
 'fidgets with a key 是手上反复摆弄，tweaks a setting 是为改善效果而微调；小动作可能看起来像，却未必都在调整。',
 ('He fidgets with his keys while he waits.','他等着时不停摆弄钥匙。'),('She always gets the fidgets during long announcements.','通知讲得一长，她就总坐不住。'),sources=S('fidgets','fidget'))
W('fidgeted','/ˈfɪdʒɪtɪd/','坐立不安、动来动去了；不断摆弄了',
 '刚才人没走远，却一直动脚、扯袖口或转笔，是 fidgeted。像身体在替无聊、紧张找一点出口。',
 'fidget + 完整 -ed，/t/ 后读 /ɪd/，多一个音节；末音节不重读，不双写 t。',FIDGET+[['fidget + -ed → fidgeted','过去反复作不安小动作']],
 'fidgeted in his seat 是在座位上动来动去，fidgeted with the ribbon 是反复摆弄丝带；with 后交代手碰的东西。',
 'fidgeted nervously 紧张地小动；fidgeted through the meeting 开会期间一直坐不住。',
 'fidgeted 可以来自无聊、兴奋或紧张，panicked 则明确是惊慌；小动作不自动说明人已慌乱。',
 ('He fidgeted in his chair throughout the long talk.','长篇讲话期间，他在椅子上一直动来动去。'),('She fidgeted with the ribbon on the gift.','她不停摆弄礼物上的丝带。'),sources=S('fidgeted','fidget'))
W('fidgeting','/ˈfɪdʒɪtɪŋ/','正在手脚动个不停、坐立不安、摆弄；不安小动作',
 '脚在地上来回点，手又去转笔、扯衣角，整个人始终没完全静下来，是 fidgeting。动的是小地方，不必整个身体乱跑。',
 'fidget + 完整 -ing，直接加；末音节不重读，保留一个 t。分词和动作名词都可说不断小动。',FIDGET+[['fidget + -ing → fidgeting','反复小动的过程、行为']],
 'fidgeting with a pen 是不停摆弄笔，stop fidgeting 是别再动来动去；fidgeting in the seat 是坐在位子上不安地动。',
 'constant fidgeting 不停的小动作；nervous fidgeting 紧张时的小动作。',
 'fidgeting 说动作频繁、难安静，twitching 常是一个局部短促抽动；主动转笔是 fidgeting，不是笔自己抽了一下。',
 ('She was fidgeting with the zip of her jacket.','她正不停摆弄外套拉链。'),('His constant fidgeting made the chair creak.','他一直动来动去，把椅子弄得吱吱响。'),sources=S('fidgeting','fidget'))
FIDDLE=[['古英语 fiðele 一类乐器名 → 中古英语 fedele、fydyll → fiddle','日耳曼同族乐器词较早，和拉丁 vitula 的关系、借入方向有争议'],['乐器名 → 拉琴动词 → 手上摆弄等用法','现代还可说胡乱改动、做手脚；不靠一个传闻包办具体词史']]
W('fiddle','/ˈfɪdəl/','小提琴〔俗称〕；拉小提琴；摆弄、瞎调；做手脚、作弊',
 'fiddle 可以亲切地叫小提琴，尤其民间音乐场景；fiddle with a pen 又像手指没闲着，来回摆弄。fiddle the figures 则是对数字做手脚。',
 '乐器名承古英语 fiðele 等，远源未定；和拉丁 vitula 的关系有不同方向分析。拉琴动词由乐器名来，手上摆弄是后来发展的常用支。',FIDDLE,
 'play the fiddle 是拉小提琴，fiddle with the controls 是摆弄控制器，fiddle the accounts 是做假账；fit as a fiddle 是非常健康、状态很好。',
 'stop fiddling with it 别再摆弄它；a fiddle tune 小提琴曲。',
 'fiddle 与 violin 常可指同一种现代乐器，前者更口语、常见民间演奏场景；不是 fiddle 一定廉价或演奏技术差。',
 ('She plays the fiddle at local dances.','她在当地舞会上拉小提琴。'),('Please do not fiddle with the controls.','请别乱动那些控制器。'),sources=S('fiddle','fiddle'))
W('fiddles','/ˈfɪdəlz/','拉琴、摆弄、做手脚〔第三人称单数〕；小提琴、骗局〔复数〕',
 '一个人手里不停转笔，或在控制器上随手调，用 fiddles；几把小提琴也叫 fiddles，词性和搭配会把意思分开。',
 'fiddle + -s，/l/ 后读 /z/；动词三单与乐器、欺诈行为等名词复数同形，末尾 e 保留。',FIDDLE+[['fiddle + -s → fiddles','他、她拉琴、摆弄；多把小提琴或多次欺诈']],
 'fiddles with a pen 是不停摆弄笔，fiddles the figures 是对数字做手脚；two fiddles 是两把小提琴。',
 'fiddles with the dial 乱调旋钮；traditional fiddles 民间音乐中的小提琴。',
 'fiddles with settings 可能显得没必要地动来动去，tweaks settings 更容易是有目的微调；语气和目的感不同。',
 ('He fiddles with his pen while he thinks.','他思考时不停摆弄笔。'),('The band uses two fiddles and a guitar.','乐队用两把小提琴和一把吉他。'),sources=S('fiddles','fiddle'))
W('fiddled','/ˈfɪdəld/','拉琴、摆弄、乱调了；做手脚、造假了',
 '刚才手没闲着，一直弄拉链、旋钮，是 fiddled with；如果是 fiddled the accounts，就变成在账目上做手脚的负面用法。',
 'fiddle 去末尾 e + 完整 -ed → fiddled，/l/ 后读 /d/；原有双 d 保留。',FIDDLE+[['fiddle 去 e + -ed → fiddled','过去拉琴、摆弄或弄虚作假']],
 'fiddled with the zip 是摆弄拉链，fiddled with the settings 是调来调去；fiddled the figures 是篡改数字。',
 'fiddled around 胡乱忙活；fiddled the accounts 做假账。',
 'fiddled 如果直接带 figures、accounts 等宾语，常说做假；with 后接小物件，常只是摆弄，不能一律译成诈骗。',
 ('She fiddled with the zip while she waited.','她等着时不停摆弄拉链。'),('He admitted that he had fiddled the figures.','他承认自己对数字做了手脚。'),sources=S('fiddled','fiddle'))
W('fiddling','/ˈfɪdəlɪŋ/','正在拉琴、摆弄、乱调、做手脚；拉琴演奏；琐碎的',
 '手指正来回摸笔、调小旋钮，是 fiddling；如果对象是琴，就是拉小提琴。fiddling details 又像小得让人反复摆弄的琐事。',
 'fiddle 去末尾 e + 完整 -ing → fiddling；可作动作名词、分词，也固定出琐小、不重要的形容用法。',FIDDLE+[['fiddle 去 e + -ing → fiddling','拉琴、摆弄过程；琐碎性质']],
 'fiddling with keys 是摆弄钥匙，folk fiddling 是民间小提琴演奏；fiddling the books 是在账本上做假。',
 'stop fiddling around 别再瞎忙活；fiddling little details 琐小细节。',
 'fiddling with a pen 是手在摆弄物件，fidgeting 更宽，动脚、挪屁股也包括；两者可描述同一个人的不同小动作。',
 ('He was fiddling with his keys during the announcement.','通知播放时，他一直摆弄钥匙。'),('We listened to some lively folk fiddling.','我们听了一段活泼的民间小提琴演奏。'),sources=S('fiddling','fiddle'))
JIGGLE=[['jig 的抖、跳、来回动材料 + -le → jiggle','旧尾可带小幅、反复意味，也可能受 jog 影响'],['轻晃整词 → 现代物体自己动、用手小幅晃动','既能说果冻颤，也能说晃把手让它松一点']]
W('jiggles','/ˈdʒɪɡəlz/','轻晃、轻摇〔第三人称单数〕；几下小晃动〔复数〕',
 '一碗果冻随桌面轻震而颤，是 jiggles；手抓住把手轻轻晃几下，也可以说 he jiggles the handle。',
 'jiggle + -s，/l/ 后读 /z/；动词三单与小晃动名词复数同形，基础 jig 接旧反复动作 -le。',JIGGLE+[['jiggle + -s → jiggles','它轻颤；他、她轻摇；几下小晃动']],
 'jiggles the handle 是轻晃把手，the jelly jiggles 是果冻颤动；a few jiggles 是几下小晃动。',
 'jiggles up and down 上下轻颤；jiggles it loose 轻晃使它松动。',
 'jiggles 常小幅反复，shakes 可从轻到猛；写轻轻活动卡住的把手，jiggles 会把小动作说得更具体。',
 ('The jelly jiggles when I move the plate.','我一动盘子，果冻就轻颤。'),('He jiggles the handle until the door opens.','他轻晃把手，直到门打开。'),sources=S('jiggles','jiggle'))
W('jiggled','/ˈdʒɪɡəld/','轻晃、轻摇、颤动了',
 '刚才把卡住的把手小幅来回动了动，或果冻晃了几下，是 jiggled。动作常是试探地晃，不是一把猛拽。',
 'jiggle 去末尾 e + 完整 -ed → jiggled，/l/ 后读 /d/；基础双 g 保留。',JIGGLE+[['jiggle 去 e + -ed → jiggled','过去轻晃或颤动']],
 'jiggled the key 是晃了晃钥匙，jiggled the handle 是轻摇把手；jiggled it loose 是晃松它。',
 'jiggled gently 轻轻摇了；jiggled up and down 上下颤动。',
 'jiggled 与 yanked 可都试图把东西弄开，前者小晃，后者猛拉；动作力度不是一句“弄了弄”能交代完。',
 ('She jiggled the key until the lock turned.','她轻轻晃动钥匙，直到锁转开。'),('The bowl of jelly jiggled as he set it down.','他放下碗时，碗里的果冻颤了颤。'),sources=S('jiggled','jiggle'))
W('jiggling','/ˈdʒɪɡəlɪŋ/','正在轻晃、轻摇、颤动；小幅反复晃动',
 '手正来回小幅晃着东西，或一团柔软物体正抖来抖去，是 jiggling。镜头关注一连串细小、不太用力的来回动。',
 'jiggle 去末尾 e + 完整 -ing → jiggling；基础 gg 保留，-ing 讲小晃动正在展开。',JIGGLE+[['jiggle 去 e + -ing → jiggling','反复轻晃的过程']],
 'jiggling the handle 是轻晃把手，jiggling a baby on a knee 是让宝宝在膝上轻轻颠动；具体对象决定场景。',
 'jiggling up and down 上下轻颤；keep jiggling 继续轻晃。',
 'jiggling 可以是主动小幅摇，也可以是东西自己颤；fidgeting 则更关注人坐不住、总有小动作，未必在摇某个东西。',
 ('He opened the stuck drawer by jiggling the handle.','他轻晃把手，把卡住的抽屉打开了。'),('The jelly was still jiggling after the plate stopped moving.','盘子不动后，果冻还在轻颤。'),sources=S('jiggling','jiggle'))

def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfr',ROOTS,WORDS)
 extend_lessons()
