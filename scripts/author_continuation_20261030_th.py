"""Common participial adjectives and everyday hovering/howling vocabulary."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1741':dict(words=['frighten','frightening','flatter','flattering','linger','lingering','dazzle','dazzling','kneel','kneeling','uplift','uplifting','overflow','overflowing','howl','howling','whopping','hover','hovering'],label='声音、感受与持续状态的常见扩展',note='frightening、flattering、dazzling、uplifting 常说带来某种感受的事物；lingering 常说迟迟不消失；howling、whopping 又有口语程度评价。'),
 'A1760':dict(words=['guide','misguided','batter','battered','repress','repressed'],label='被误导、受损与被压住的状态',note='misguided 接 misguide + -ed；repressed 接 repress + -ed。battered 的受损义接击打动词，裹面糊义则接面糊名词的相应构词。'),
 'A1697':dict(words=['hover','hovering'],label='同形的旧动词反复材料：hover',note='hover 的旧 -er 是反复、持续动作材料，与表示人物的 -er 不同；可追溯中古英语 hoveren 与 hoven 逗留、悬浮的关系。'),
}
W('frightening','/ˈfraɪtənɪŋ/','令人害怕的；frighten 的 -ing 形式',
 '声音、经历或想象让人心里一紧，它本身就可以叫 frightening。说的是引起害怕的那个东西。',
 'frighten 使害怕 + -ing，形成分词和形容词；frighten 又接 fright 恐惧及动词化材料。',
 [['fright → frighten','恐惧 → 使害怕'],['frighten + -ing → frightening','正在使人害怕；具有这种效果的']],
 'a frightening experience 可怕经历；a frightening noise 吓人的声响；find something frightening 觉得某事可怕。',
 'a frightening thought；frighteningly close。','frightened 常说人感到害怕，frightening 常说事物令人害怕。The child is frightened 与 The noise is frightening 主角不同。',
 ('The sudden noise was frightening.','突如其来的声响很吓人。'),('Getting lost in the dark was a frightening experience.','在黑暗中迷路是一次可怕的经历。'))
W('flattering','英 /ˈflætərɪŋ/；美 /ˈflætərɪŋ/','赞美、讨好的；衬得人好看的',
 '好听的话让人觉得被夸了；合适的衣服、角度也能把人显得更好看，像替人把优点亮出来。',
 'flatter 奉承、使人满意 + -ing，形成分词形容词。由赞美、给人好印象，扩展到衣着、图像衬得好看。',
 [['flatter 的赞美、讨好用法','让人对自己有好印象'],['flattering 的形容词发展','赞美的；外观上显得更好的']],
 'flattering remarks 赞美、讨好的话；a flattering photo 显得人好看的照片；a flattering dress 衬人的裙子。是否带虚假讨好意味要看语境。',
 'a flattering comparison；flattering lighting。','flattering 是带来好印象的；flattered 常是人感到受宠若惊。a flattering photo 说视觉效果衬人，flattered 则描述人心理上的感受。',
 ('That colour is very flattering on you.','那个颜色很衬你。'),('She smiled at the flattering comment.','听到那句赞美，她笑了。'))
W('lingering','英 /ˈlɪŋɡərɪŋ/；美 /ˈlɪŋɡərɪŋ/','迟迟不散的、持续未消的；逗留、拖延',
 '人已经走了，香味还在；事情结束了，疑问还留着。lingering 抓住比预想留得更久、不肯散的感觉。',
 'linger 逗留、迟迟不去 + -ing；linger 的较早词族接延长、拖久等材料。分词形容词把延留变成持续存在的性质。',
 [['linger 的逗留、延长词义','不很快离开或结束'],['linger + -ing → lingering','仍逗留；某种感觉、状态迟迟不散']],
 'a lingering smell 挥之不去的气味；lingering doubts 仍未消除的疑虑；lingering by the door 在门边逗留。',
 'a lingering memory；a lingering feeling。','lasting 可中性说持久；lingering 常更突出本应或可能结束、却仍留下的感觉。美好记忆也可以 lingering，未必负面。',
 ('There was a lingering smell of coffee in the room.','房间里仍留着咖啡香。'),('She had lingering doubts about the explanation.','她对那个解释仍存疑虑。'))
W('misguided','/ˌmɪsˈɡaɪdɪd/','判断错误的、受误导的；出于错误想法的',
 '可能是想帮忙，但方向、前提或判断弄错了。misguided 常批评思路走偏，不一定在说动机恶意。',
 'misguide 误导 + -ed；mis- 给错误方向，guide 给引导。过去分词再用于形容人、信念或做法受到错误认识影响。',
 [['mis- + guide → misguide','引到错误方向、误导'],['misguide + -ed → misguided','被误导的；基于错误判断的']],
 'a misguided attempt 方向错误的尝试；a misguided belief 错误信念；well-meaning but misguided 出于好意却判断失当。',
 'a misguided policy；a misguided idea。','misguided 不直接等于 malicious 恶意的。它常保留出发点或许好、但认识与做法不对这一层区别。',
 ('It was a misguided attempt to help.','那是一次出于帮助却方向不对的尝试。'),('He acted on the misguided belief that nobody would notice.','他误以为没人会注意，于是采取了行动。'))
W('battered','英 /ˈbætəd/；美 /ˈbætərd/','受损、破旧的；被殴打的；裹面糊的',
 '旧箱子被撞得伤痕累累，是 battered；菜单上的 battered fish 却是在说鱼外面裹了面糊。先看名词、场景。',
 '受损义接 batter 反复击打 + -ed；食品义接 batter 面糊与覆盖某物的形容词材料。batter 的相关词族更早都与击打、搅打等有联系，但现代词性和构成分开。',
 [['batter 击打动词 + -ed','被反复敲击、撞坏 → 破旧、受伤的'],['batter 面糊名词的相应形容词','外面裹着面糊的']],
 'a battered suitcase 破旧的手提箱；battered furniture 伤痕累累的家具；battered fish 裹面糊的鱼。形容人时还可能说受殴打，要按语境认真选义。',
 'a battered old car；battered fish and chips。','食品里的 battered 不表示把鱼打坏；这是面糊名词参与的构词。旧物 battered 则常借反复受撞的画面形容损伤。',
 ('He carried a battered suitcase.','他提着一只破旧的手提箱。'),('The menu includes battered fish with chips.','菜单上有裹面糊的炸鱼配薯条。'),sources=['https://en.wiktionary.org/wiki/battered#English'])
W('dazzling','/ˈdæzlɪŋ/','耀眼的、令人目眩的；精彩夺目的',
 '光太亮，一下晃了眼；表演、才华太出色，也像亮得把人震住。',
 'dazzle 使眼花、使赞叹 + -ing；形成分词和形容词。具体强光的反应，转为对精彩表现的赞叹。',
 [['dazzle 的晃眼、使惊叹用法','强光刺激；精彩表现震住人'],['dazzle + -ing → dazzling','具有耀眼、令人赞叹的效果']],
 'dazzling sunlight 耀眼阳光；a dazzling performance 精彩夺目的表演；a dazzling display of skill 令人惊叹的技艺展示。',
 'a dazzling smile；dazzling colours。','dazzling 强调事物造成的效果；dazzled 常说人已经被晃到眼、被震住。比喻用法不要求真的存在强光。',
 ('The dazzling sunlight made her shield her eyes.','耀眼的阳光让她抬手遮住眼睛。'),('The dancers gave a dazzling performance.','舞者们献上了一场精彩夺目的表演。'))
W('kneeling','/ˈniːlɪŋ/','跪着、下跪；kneel 的 -ing 形式',
 '把膝盖落到地上，身体由膝部支撑。kneeling 说这项动作或所处姿势。',
 'kneel + -ing；kneel 与 knee 膝的日耳曼词族相连。开头 k 在现代常见读音里不发音。',
 [['knee 膝与 kneel 下跪的相邻词族','身体以膝部接触支撑面'],['kneel + -ing → kneeling','正在下跪；处在跪姿']],
 'kneeling on the floor 跪在地板上；a kneeling position 跪姿；kneeling beside a chair 跪在椅子旁。姿势也常作为修饰语。',
 'kneeling down；a kneeling figure。','kneeling 跪着与 sitting 坐着不同，主要支撑、接触方式不同。具体用途可以是找东西、工作、礼仪，不由姿势词单独决定。',
 ('He was kneeling on the floor, looking for the key.','他正跪在地上找钥匙。'),('The sculpture shows a kneeling figure.','雕塑表现了一个跪着的人物。'))
W('uplifting','/ʌpˈlɪftɪŋ/','振奋人心的、令人鼓舞的；提升',
 '本来心情低落，看完、听完某件事，精神像被往上托起来。uplifting 常形容这种积极情绪效果。',
 'uplift 提起、提升 + -ing；up 向上 + lift 抬起的物理结构，较自然地比喻成精神受到鼓舞。',
 [['up + lift → uplift','向上抬起；再说精神提升'],['uplift + -ing → uplifting','令人振奋、受到鼓舞的']],
 'an uplifting story 鼓舞人的故事；uplifting music 振奋的音乐；an uplifting experience 振奋人心的经历。',
 'an uplifting message；find something uplifting。','uplifting 多强调带来积极精神感受；exciting 强调兴奋、刺激，不一定使人精神上得到鼓舞。',
 ('The film tells an uplifting story about friendship.','电影讲了一个鼓舞人心的友谊故事。'),('She found the music deeply uplifting.','她觉得那段音乐让人精神大振。'))
W('repressed','/rɪˈprest/','被压抑、压制的；不易表露情感的',
 '情绪、愿望被往回按，没让它表现出来；也可以说某种活动被压制。核心是力量被压住。',
 'repress 压抑、抑制 + -ed；repress 的词族接拉丁 reprimere 按回、约束，含 re- 回与 premere 压。',
 [['拉丁按回、压住词族 → repress','阻止表现、限制活动'],['repress + -ed → repressed','已受压制；情绪不轻易显露的']],
 'repressed anger 被压住的愤怒；repressed feelings 被抑制的感情；a repressed person 较不容易表露情感的人。',
 'repressed emotion；a repressed desire。','repressed 不等于没有感受，而是描述表达、显露受抑制。depressed 是另一个词，不能只因中文都可能带压就互换。',
 ('His voice revealed years of repressed anger.','他的声音流露出多年压抑的愤怒。'),('The novel explores the character’s repressed feelings.','小说探讨了人物压抑的感情。'))
W('overflowing','英 /ˌəʊvəˈfləʊɪŋ/；美 /ˌoʊvərˈfloʊɪŋ/','满溢、溢出的；充满、洋溢着的',
 '容器装满后，水从边上流出来。再把画面借给人群、感情：多到像装不下。',
 'overflow 溢出 + -ing；over- 越过、超过 + flow 流，组合成超过边界而流出。抽象用法把容量画面延伸到感受、数量。',
 [['over- + flow → overflow','流过容器边界、溢出'],['overflow + -ing → overflowing','正在溢出；满到装不下般的']],
 'an overflowing sink 溢水的洗涤池；overflowing with joy 满心欢喜；overflowing with people 人多得满满当当。with 后接充满的内容。',
 'overflowing bins；a heart overflowing with gratitude。','full 可以只说装满；overflowing 更突出已到边界、甚至越出来的量感。比喻里也可能是积极情绪。',
 ('The sink was overflowing with water.','洗涤池里的水满得溢了出来。'),('She was overflowing with excitement.','她满心兴奋。'))
W('howl','/haʊl/','嚎叫、长号；风呼啸；大声哭喊或大笑；嚎叫声',
 '狼拖长嗓子嗷地叫，风在窗外长长呼啸，人也能大声笑、哭。抓住延长、响亮的一阵声音。',
 '经中古英语 howlen、houlen 等延续，联系较早日耳曼长号词族，通常认为有拟声性质；不强定更远唯一来源。',
 [['较早长号、嚎叫的拟声词族','拖长的响亮声音'],['现代 howl 的多类声源','动物嚎、人喊笑、风呼啸；相应声音名词']],
 'a wolf howls 狼嚎；the wind howls 风呼啸；howl with laughter 放声大笑；a howl of pain 一声痛叫。名词、动词都常见。',
 'hear a howl；howl at the moon。','howl 不是所有动物叫声的统称，常突出长、响的声音。howl with laughter 明确是大笑，不要机械译成哭嚎。',
 ('We heard wolves howling in the distance.','我们听见远处有狼在嚎叫。'),('The joke made everyone howl with laughter.','那个笑话让大家放声大笑。'))
W('howling','/ˈhaʊlɪŋ/','嚎叫、呼啸的；极大的〔部分口语搭配〕',
 '风、狼的长叫声持续着，是 howling；howling success 则是口语里的巨大成功，取强烈、引人注意的程度感。',
 'howl + -ing，较早英语已有相应动作名词。后来的口语形容词还用于强调程度，而不一定真的发出声音。',
 [['howl 嚎叫、呼啸 + -ing','发声过程、持续的声音性质'],['部分口语程度搭配','强烈、极大 → a howling success 等']],
 'howling wind 呼啸的风；howling wolves 嚎叫的狼；a howling success 巨大成功。具体声音与程度评价按搭配分开。',
 'hear howling；a howling wind。','howling success 不要求成功本身在喊叫，这是固定的夸张形容词用法。普通 howling wind 则直接说声音。',
 ('The howling wind kept us awake.','呼啸的风让我们无法入睡。'),('The school concert was a howling success.','学校音乐会大获成功。'))
W('whopping','英 /ˈwɒpɪŋ/；美 /ˈwɑːpɪŋ/','巨大的、惊人的〔口语，常加强数字〕',
 '数字比预想大一大截，说出来要特意加重语气。a whopping seven hundred pages 就是足足七百页，重点在惊讶。',
 'whop 重击、猛打的动词 + -ing，形成夸张的大、惊人等形容词。现代常作为口语程度评价，原动词本身较少见。',
 [['whop + -ing','重击、强烈动作的相应形式'],['口语形容词 whopping','异常大、数量大得惊人']],
 'a whopping number 惊人的数量；a whopping seven hundred pages 足足七百页。数字前的 a whopping 即使后面是复数量词也常出现。',
 'a whopping amount；a whopping ninety per cent。','whopping 比 large 更口语、更有惊讶感。它是在评价数量很大，不是精确的计量单位。',
 ('The report ran to a whopping seven hundred pages.','报告竟然长达七百页。'),('The bag weighed a whopping eighteen kilos.','那个包重达十八公斤。'),sources=['https://en.wiktionary.org/wiki/whopping#English'])
W('hover','英 /ˈhɒvə/；美 /ˈhʌvər/','悬停；在附近徘徊、守候；鼠标指针停留',
 '直升机待在空中同一处，鼠标停在图标上，人又在门边迟迟不走。都像在某个位置附近停留、微微活动。',
 '经中古英语 hoveren，接较早 hoven 悬浮、逗留等及旧反复动作材料 -er。更远来源分析不一；这个 -er 不是做某事的人。',
 [['较早 hoven + 反复动作材料 → hoveren','悬浮、来回微动、逗留'],['现代 hover 的场景扩展','空中悬停；附近守候；指针停留']],
 'hover above the ground 在地面上方悬停；hover near the door 在门边徘徊；hover over an icon 把鼠标悬停在图标上。',
 'a helicopter hovers；hover over a button。','hover 常保持在某处或附近；fly 只说飞行，不一定停在一处。电脑 hover 是把空间停留的画面用于指针。',
 ('The helicopter hovered above the field.','直升机在田野上方悬停。'),('Hover over the icon to see a short description.','把鼠标悬停在图标上，就能看到简短说明。'),sources=['https://www.etymonline.com/word/hover','https://en.wiktionary.org/wiki/hover#English'])
W('hovering','英 /ˈhɒvərɪŋ/；美 /ˈhʌvərɪŋ/','悬停、徘徊、守候；hover 的 -ing 形式',
 '保持在某个位置附近不离开。可以是飞行器，也可以是一个总在旁边转、让人感觉被盯着的人。',
 'hover + -ing；由悬停、逗留的动词进入分词和状态描写。不同对象保留附近停留这一核心。',
 [['hover 的悬浮、逗留词义 + -ing','持续维持附近位置'],['hovering 的具体与人物描写','正在悬停；在附近徘徊、过分守候']],
 'a hovering helicopter 悬停的直升机；hovering by the entrance 在入口边徘徊；hovering over someone 总在某人旁边转、盯着。',
 'hovering above the water；hovering nearby。','hovering over a person 可能带让对方不自在的照管、监督意味；hovering over an icon 则通常是中性的电脑动作。',
 ('A bird was hovering above the water.','一只鸟在水面上方悬停。'),('He kept hovering by the door, unsure whether to leave.','他一直在门边徘徊，不确定该不该走。'))
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_th',ROOTS,WORDS)
    extend_lessons()
