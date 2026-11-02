"""Long cries, heated complaints, fitting language and vivid impressions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1741':dict(words=['rant','ranting','wail','wailing','strike','striking'],label='ranting、wailing、striking：动作与固定形容词',note='ranting 强调激烈地抱怨或咆哮；wailing 强调拖长的哭号声；striking 既可作 strike 的分词，也有引人注目的常用形容词义。'),
 'A1740':dict(words=['apt','aptly','affectionate','affectionately','striking','strikingly','shocking','shockingly'],label='形容词先抓准，再读 -ly 的方式或程度',note='aptly 恰当地；affectionately 亲昵地；strikingly 显著地、格外地；shockingly 令人震惊地。先理解形容词的画面，副词再说明动作方式或程度。'),
 'B2522':dict(words=['industrialize','industrialized','industrialization'],label='工业化的动作、状态和过程',note='industrialize 使工业化；industrialized 工业化了的；industrialization 工业化过程。industrialized 是分词形容词，也可作过去式，不能仅看到 -ed 就认定句子在讲过去。'),
}
W('rant','英 /rænt/，部分英音 /rɑːnt/；美 /rænt/','激烈地长篇抱怨、咆哮；一通激烈言论',
 '本来只要说个不满，却越说越大声、越说越长，旁人很难插话。rant 常带说话者情绪很冲、言辞过头的评价。',
 '借自荷兰语 randten、ranten 等胡乱高谈、狂言词，英语早期也有喧闹欢乐等义；更早来源不明。现代主要落在高声、激烈地说一大通。',
 [['荷兰语 randten／ranten → 英语 rant','胡乱高谈、喧闹；来源更早不定'],['现代 rant 动词、名词','激烈长篇抱怨；一通情绪化言论']],
 'rant about the service 对服务大发牢骚；rant at someone 冲某人咆哮；go on a rant 大发一通议论；rant and rave 大喊大叫、暴跳如雷。',
 'a long rant；rant on about something。','complain 可是平静地提出不满；rant 把声量、情绪或言辞过火突出出来。把别人的话叫 a rant，本身常带批评。',
 ('He went on a long rant about the delayed train.','他对列车延误大发了一通牢骚。'),('She ranted about the poor service for several minutes.','她激烈地抱怨了几分钟服务太差。'),sources=['https://www.etymonline.com/word/rant','https://en.wiktionary.org/wiki/rant#English'])
W('ranting','/ˈræntɪŋ/，也有 /ˈrɑːntɪŋ/ 等读法','激烈咆哮、长篇抱怨；rant 的 -ing 形式',
 '话一大串地冲出来，夹着怒气、夸张或指责。ranting 让人想到正在喋喋不休地发火，而不是从容陈述。',
 'rant + -ing，接从荷兰语借入的喧闹、激烈高谈词。可作进行结构中的分词，也作动作名词或名词前的描述。',
 [['rant','激烈地说、抱怨；早期有喧闹词义'],['rant + -ing → ranting','咆哮、激烈抱怨这一动作']],
 'was ranting about the bill 正在对账单大发牢骚；stop ranting 别再咆哮；a ranting speaker 激烈叫嚷的发言者。',
 'ranting and raving；listen to someone’s ranting。','ranting 在评价别人讲话时通常不中性；reporting 只是报告，arguing 是争辩，两者不自动有 ranting 的过火感。',
 ('He was ranting about the price of the repair.','他正在对维修价格大发牢骚。'),('The recording captured several minutes of angry ranting.','录音录下了几分钟愤怒的咆哮。'),sources=['https://www.etymonline.com/word/rant','https://en.wiktionary.org/wiki/ranting#English'])
W('wail','/weɪl/','哭号、哀号；发出尖长声；哭号声',
 '哭声不是一声短促的抽噎，而是拉长、响亮地拖出去。警笛和风也能借这种声音叫 wail。',
 '经中古英语 weilen 等，接古诺斯 væla 哀叹，来自表示悲苦、哀叹的 væ。后来既描写人的哭号，也描写类似的长鸣。',
 [['古诺斯 væ、væla → 中古英语相关形式','悲苦的喊声、哀叹'],['现代 wail','高声哭号；警笛等拖长的声音']],
 'wail with grief 悲痛地哭号；the wail of a siren 警笛的长鸣；wail about something 哭着或大声抱怨某事。',
 'let out a wail；a distant wail。','weep 更侧重流泪，sob 更突出抽噎，wail 更突出响亮、拖长的声音。声音来源也可不是人。',
 ('A siren wailed in the distance.','远处警笛长鸣。'),('The child let out a loud wail when the balloon burst.','气球爆裂时，孩子放声哭了起来。'),sources=['https://www.etymonline.com/word/wail','https://en.wiktionary.org/wiki/wail#English'])
W('wailing','/ˈweɪlɪŋ/','哭号、哀号；长鸣；wail 的 -ing 形式',
 '声音拉得长，尖而响，一阵接一阵。wailing sirens 把警笛描写得像在高声哀号。',
 'wail + -ing，接古诺斯哀叹、哭号词族。现代可说人正在哭号，也可说警笛、乐器等的长鸣声。',
 [['wail','长声哭号、哀叹；类似声音'],['wail + -ing → wailing','哭号动作；长鸣的声音特征']],
 'a wailing baby 放声哭的婴儿；wailing sirens 长鸣的警笛；the wailing of the wind 风的呼号。',
 'wailing with grief；hear someone wailing。','wailing 不只说情绪，也可描述声音本身。a wailing siren 是按声形作比喻，理解成尖长的鸣响即可。',
 ('Wailing sirens broke the silence.','长鸣的警笛打破了寂静。'),('She could hear a baby wailing upstairs.','她能听见楼上有个婴儿在放声哭。'),sources=['https://www.etymonline.com/word/wail','https://en.wiktionary.org/wiki/wailing#English'])
W('apt','/æpt/','恰当贴切的；聪敏、学得快的；容易、往往会的',
 '一句比喻恰好贴住眼前情况，是 apt。be apt to 又说某事容易照这个方向发生，像总有这种倾向。',
 '经法语 ate、apte 或直接借自拉丁 aptus 合适、适配的；更早接连接、贴合的旧动词材料。英语适合与倾向两支都较早存在。',
 [['拉丁 aptus → 法语／英语 apt','贴合、适合、具备所需性质'],['现代常用搭配','贴切的；学得快的；倾向于、容易']],
 'an apt description 贴切描述；an apt pupil 聪明好学的学生；be apt to forget 容易忘；an apt comparison 恰当比喻。',
 'an apt choice of words；apt to change。','apt to do 是容易、往往会，不一定是有能力。an apt description 说描述贴切，an able person 则说人有能力，不能只按一个中文词换。',
 ('That is an apt description of the problem.','那是对这个问题的贴切描述。'),('The weather here is apt to change suddenly.','这里的天气容易突然变化。'),sources=['https://www.etymonline.com/word/apt','https://en.wiktionary.org/wiki/apt#English'])
W('aptly','/ˈæptli/','恰当地、贴切地',
 '名字正好点中特点，评论正好说到要害，都可以加 aptly：说得贴、选得准。',
 'apt + -ly，-ly 形成方式副词；接 apt 的合适、贴合分支。早期也有其他用法，现代重点是方式恰当。',
 [['apt；接拉丁 aptus 合适、贴合','恰当、适合'],['apt + -ly → aptly','以贴切、合适的方式']],
 'aptly named 名副其实地命名；aptly described 贴切地描述；aptly put 说得恰到好处；aptly illustrates 恰好说明。',
 'an aptly chosen word；aptly sums up。','aptly 强调恰当，accurately 强调准确。一个描述可以事实准确却没抓住重点；aptly 往往还赞它贴合场景。',
 ('The café was aptly named The Meeting Place.','那家咖啡馆取名“相聚之地”，很是贴切。'),('Her remark aptly summed up the mood in the room.','她的话贴切地概括了屋内的气氛。'),sources=['https://www.etymonline.com/word/aptly','https://en.wiktionary.org/wiki/aptly#English'])
W('affectionately','/əˈfekʃənətli/','亲昵地、满怀爱意地',
 '叫名字时语气软下来，拍肩、拥抱时带着亲近喜欢。affectionately 把这种有感情的方式添到动作上。',
 'affectionate + -ly；affectionate 由 affection 加 -ate 等材料形成，承接法语、拉丁情感、倾向的词族。现代取喜爱、亲近这一分支。',
 [['拉丁／法语情感词族 → affection → affectionate','情感、喜爱 → 充满爱意的'],['affectionate + -ly → affectionately','以亲昵、带喜爱感的方式']],
 'smile affectionately 亲昵地微笑；speak affectionately of someone 满怀感情地谈某人；affectionately known as 被大家亲切地叫作。',
 'pat someone affectionately；remember someone affectionately。','affectionately 可以用于家人、朋友、宠物，不限于爱情。romantically 更明确朝恋爱、浪漫关系的方向。',
 ('She smiled affectionately at her grandson.','她满怀爱意地朝孙子微笑。'),('The old bus was affectionately known as Big Red.','大家亲切地把那辆旧公交车叫作“大红”。'),sources=['https://www.etymonline.com/word/affectionate','https://en.wiktionary.org/wiki/affectionately#English'])
W('striking','/ˈstraɪkɪŋ/','引人注目的、显著的；击打、罢工等；strike 的 -ing 形式',
 '有个特点一下撞进视线，让人难以忽略，就是 striking。a striking contrast 是差别非常醒目。',
 'strike 去词末 e 加 -ing；动作分词后来在留下鲜明印象这一动词分支上形成常用形容词。strike 的击打、罢工等其他分支也保留相应 -ing 用法。',
 [['strike + -ing','击打等动作分词；也接罢工分支'],['留下鲜明印象的分支 → 形容词 striking','突出的、引人注目的']],
 'a striking difference 显著差别；a striking resemblance 惊人相似；a striking image 令人印象深的画面；striking workers 罢工工人。',
 'a striking contrast；striking features。','striking 的形容词常表示吸引注意，struck 是过去式、过去分词，不能只按中文都含打击就换用。a striking difference 的 difference 不在作击打动作。',
 ('There is a striking contrast between the two rooms.','两个房间形成了鲜明对比。'),('The report includes interviews with striking workers.','报告收录了对罢工工人的采访。'),sources=['https://www.etymonline.com/word/striking','https://en.wiktionary.org/wiki/striking#English'])
W('strikingly','/ˈstraɪkɪŋli/','显著地、格外地、惹人注目地',
 '相似不只是有一点，而是像到让人一下注意；不同也可以明显得一眼看出来。strikingly 把程度推到醒目这一层。',
 'striking 引人注目的 + -ly，形成方式、程度副词；承接 strike 留下鲜明印象这一分支，经形容词再派生。',
 [['strike → striking','留下印象 → 引人注目的'],['striking + -ly → strikingly','达到让人注意的明显程度']],
 'strikingly similar 惊人地相似；strikingly different 明显不同；strikingly beautiful 美得引人注目；strikingly clear 格外清楚。',
 'look strikingly alike；a strikingly modern design。','strikingly 可同时修饰相似和不同，不等于某个固定方向的变化。它强调程度醒目，读完后面的形容词才知道具体特点。',
 ('The two buildings are strikingly similar.','两栋建筑惊人地相似。'),('Her approach was strikingly different from ours.','她的方法与我们的明显不同。'),sources=['https://www.etymonline.com/word/striking','https://en.wiktionary.org/wiki/strikingly#English'])
W('shockingly','英 /ˈʃɒkɪŋli/；美 /ˈʃɑːkɪŋli/','令人震惊地；糟糕到令人吃惊地；出人意料地〔加强语气〕',
 '一看价格，心里猛地一震：怎么会这么贵。shockingly 把程度说到令人吃惊，有时也夸张地强调出乎意料。',
 'shocking + -ly；shocking 接 shock 使震惊的分词形容词，较早有令人反感、惊骇等义。现代副词常修饰很高、很低、很坏或夸张的好。',
 [['shock → shocking','冲击、震惊 → 令人震惊、反感的'],['shocking + -ly → shockingly','以令人震惊的方式；达到惊人程度']],
 'shockingly expensive 贵得惊人；shockingly low 低得惊人；behave shockingly 行为糟糕；shockingly good 好得出乎意料，口语夸张。',
 'shockingly bad；a shockingly small amount。','shocking 多形容造成震惊的事物，shocked 多说感到震惊的人。shockingly 修饰程度，不等于 shockedly 那样直接描写某人受惊的样子。',
 ('The repairs were shockingly expensive.','维修费高得惊人。'),('For such a tiny speaker, the sound was shockingly good.','音箱这么小，音质却好得出乎意料。'),sources=['https://www.etymonline.com/word/shocking','https://en.wiktionary.org/wiki/shockingly#English'])
W('industrialized','/ɪnˈdʌstriəlaɪzd/','工业化的；已实现工业化；industrialize 的过去式、过去分词',
 '生产越来越依靠工厂、机器和大规模流程，一片地区或一种生产方式变成 industrialized。作形容词时看的是形成的状态。',
 'industrial + -ize → industrialize，再加 -ed 得 industrialized；工业化动词可能参照法语 industrialiser 形成。industrial 更早经法语、拉丁勤劳、劳动词族，现代专门朝制造业发展。',
 [['industrial + -ize → industrialize','使具有工业性质、发展大规模工业'],['industrialize + -ed → industrialized','已工业化的；相应过去动作']],
 'an industrialized region 工业化地区；industrialized production 工业化生产；became industrialized 实现了工业化。英式也常写 industrialised。',
 'highly industrialized；an industrialized economy。','industrialized 表状态或过去形式，industrialization 表过程名词。The region is industrialized 用 is 描述现在状态，不因词末 -ed 就自动是过去时。',
 ('The region became industrialized during the nineteenth century.','该地区在十九世纪实现了工业化。'),('The book compares agricultural and industrialized economies.','那本书比较农业型经济与工业化经济。'),sources=['https://www.etymonline.com/word/industrialize','https://en.wiktionary.org/wiki/industrialized#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ul',ROOTS,WORDS)
 extend_lessons()
