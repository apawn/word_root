"""Common claims, categories, ideas, notes and source material."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0156':dict(words=['claim','claims'],label='claim → claims：声称、主张与索取',note='claim 经法语接拉丁 clāmāre 呼喊、宣称词族，名词和动词有平行借入路线。'),
 'B2455':dict(words=['star','stars'],label='star → stars：星星、明星与主演',note='star 继承古英语 steorra；星形标记、名人和主演等现代分支分别看。'),
 'C1569':dict(words=['type','types'],label='type → types：印记、样式到种类',note='type 接希腊 typos 敲出的印记、样式，经拉丁借入；动词打字由印字的材料发展。'),
 'C0055':dict(words=['animal','animals'],label='animal → animals：有生命、气息的到动物',note='animal 接拉丁 anima 生命、气息与 animalis 有生命的词族，英语经法语和拉丁借入。'),
 'C0117':dict(words=['benefit','benefits'],label='benefit → benefits：做好事、带来好处',note='benefit 经法语做好事、好处词族传入，后受拉丁 bene- 拼写影响；好处与福利等现代用法按场景分辨。'),
 'C0596':dict(words=['idea','ideas'],label='idea → ideas：看见的形状到心中的想法',note='idea 经拉丁接希腊 idea 形状、样式，相关 idein 看；英语由哲学用法扩展为普通想法。'),
 'C0829':dict(words=['note','notes'],label='note → notes：留下标记、记下的内容',note='note 接拉丁 nota、notare 的标记词族，名词与动词有相关借入路线；与 noscere 的更深关系不当确定事实。'),
 'B2749':dict(words=['song','songs'],label='sing／song → songs：歌唱与一首首歌',note='song 继承古英语 sang，与 sing 有历史元音变化关系；现代复数直接加 s。'),
 'C1459':dict(words=['source','sources'],label='source → sources：涌起处到来源',note='source 经法语 sourse、sourdre 接拉丁 surgere 涌起；来源名词与寻求货源的动词用法分开看。'),
 'C1026':dict(words=['photograph','photo','photos'],label='photograph → photo → photos：光构词与较晚缩略',note='photo 是 photograph 的后起缩短，photos 直接加 s；词尾 o 不自动要求复数加 es。'),
}
W('claims','/kleɪmz/','声称、主张；索赔、索取要求、权益主张；声称、要求〔claim 的第三人称单数〕',
 '把一个说法或要求明确提出来，是 claim。claims 可以是几项待查的说法，也可以是在要求某种权益、补偿。',
 'claim + -s，/m/ 后读 /z/。经古法语 clamer 动词、claime 名词等接拉丁 clāmāre 呼喊、宣称，两种词性有相关平行借入线。',
 [['拉丁 clāmāre → 法语 clamer／claime → claim','呼喊、宣称 → 主张、提出要求'],['claim 名词、动词 + -s → claims','多个说法、要求；单数主语声称、索取']],
 'claims about ... 关于……的说法；claims to know 声称知道；insurance claims 保险索赔；claims a prize 领取、要求得到奖品。',
 'check the claims；claims that ...。','claims that ... 先表示有人这样说，作者可能暂不认可，也可能只是标记信息来源；不由 claim 这个词本身证明说法为真。a claim 还可指要求，而不只是一句话。',
 ('The article checks several claims made in the advertisement.','文章核查了广告里的几个说法。'),('He claims to have seen the original painting.','他声称见过那幅画的原作。'),sources=['https://en.wiktionary.org/wiki/claims#English','https://en.wiktionary.org/wiki/claim#English'])
W('stars','英 /stɑːz/；美 /stɑːrz/','星星；星形标记；明星、主角；由……主演、担任主演〔动词形式〕',
 '夜空里亮眼的星，给舞台上引人注目的人提供了明星这个比喻。星形符号也被用来评分或作标记。',
 'star + -s，词尾 /z/。star 继承古英语 steorra、中古英语 sterre，与其他印欧星名有更远同源关系；名人、标记、主演等为不同现代分支。',
 [['古英语 steorra → 中古英语 sterre → star','星；后来有明星、星形标记等'],['star 名词、动词 + -s → stars','多颗星、多个明星；单数主语主演、以某人为主演']],
 'film stars 电影明星；five stars 五星；stars in a film 在片中主演；the film stars ... 这部片由……主演。',
 'stars in the sky；stars a young actor。','She stars in the film 是她主演这部片；The film stars her 是电影由她主演。动词可以换叙述起点，人物和作品的位置不同。',
 ('The stars became visible after the clouds cleared.','云散后，星星露了出来。'),('The film stars a young actor from the local theatre.','这部电影由当地剧院的一位年轻演员主演。'),sources=['https://en.wiktionary.org/wiki/stars#English','https://en.wiktionary.org/wiki/star#English'])
W('types','/taɪps/','类型、种类；字模、字体等；打字〔type 的第三人称单数〕',
 '给事物按共同样式分组，就有不同 types；文字印成什么样式，也和 type 的印记历史相关。动词则说按键输入文字。',
 'type 已有 e，加 s，/p/ 后读 /s/。希腊 typos 是敲出的印记、样式，经拉丁 typus 借入英语；打字义沿印字、字体等使用史发展。',
 [['希腊 typos → 拉丁 typus → 英语 type','敲出的印记、样式 → 类型、字模等'],['type 名词、动词 + -s → types','多个类别、字体等；单数主语打字']],
 'different types 不同种类；types of plants 植物种类；types a message 输入消息；types quickly 打字快。',
 'several types of ...；types the address。','three types of chair 常说三种椅子，three chairs 是三把椅子。types 作动词时强调输入文字，writes 也能说更广的写作、手写等。',
 ('The guide describes three types of woodland.','指南介绍了三种林地。'),('She types the address carefully before sending the message.','发送消息前，她仔细输入地址。'),sources=['https://en.wiktionary.org/wiki/types#English','https://en.wiktionary.org/wiki/type#English'])
W('animals','/ˈænɪməlz/','动物；animal 的复数',
 '猫、兔、鸟、鱼等都能是 animals。这个词把许多不同动物放在一个大类别里，具体是哪种再用名称补出来。',
 'animal + -s，/l/ 后读 /z/。拉丁 anima 生命、气息 → animalis 有生命的 → animal 动物，经法语及拉丁借入英语。',
 [['拉丁 anima → animalis → animal','生命、气息 → 有生命的 → 动物名词'],['法语、拉丁借入英语 animal；再加 -s → animals','多个动物']],
 'wild animals 野生动物；farm animals 农场动物；domestic animals 家养动物；animals in the forest 森林里的动物。',
 'care for animals；different kinds of animals。','日常 people and animals 常把人和其他动物分开说；在更广的生物分类语境里，人也属于动物。具体阅读要看这个词采用哪种语境范围。',
 ('The farm keeps several kinds of animals.','这家农场养着几种动物。'),('We watched the wild animals from a distance.','我们隔着一段距离观察野生动物。'),sources=['https://en.wiktionary.org/wiki/animals#English','https://en.wiktionary.org/wiki/animal#English'])
W('benefits','/ˈbenɪfɪts/','好处、益处；福利、津贴；使受益、受益〔benefit 的第三人称单数〕',
 '一件事给人带来什么好处，是 benefits；工作或制度安排里提供的福利，也用这个词。作动词时，可说某人得到了好处或使别人得到好处。',
 'benefit + -s，/t/ 后读 /s/。经古法语 benfet、bienfait 好处及 bienfaire 做好事等相关材料传入，拼写后来受拉丁 bene- 好的影响；faire 远接 facere 做。',
 [['拉丁做好事相关材料 → 法语 bienfait／benfet 等 → benefit','做好事、好处；后有现代福利等用法'],['benefit 名词、动词 + -s → benefits','多项益处、福利；单数主语受益或使受益']],
 'the benefits of reading 阅读的益处；employee benefits 员工福利；benefits from ... 从……受益；benefits everyone 使大家受益。',
 'practical benefits；benefits the community。','The change benefits the team 是改变使团队受益；The team benefits from the change 是团队从改变中受益。主语和 from 一起交代谁得到好处。',
 ('The guide explains the benefits of keeping clear records.','指南说明了保存清晰记录的好处。'),('The whole team benefits from sharing what they learn.','分享所学，让整个团队受益。'),sources=['https://en.wiktionary.org/wiki/benefits#English','https://en.wiktionary.org/wiki/benefit#English'])
W('ideas','英 /aɪˈdɪəz/；美 /aɪˈdiːəz/','想法、点子；概念、理念；idea 的复数',
 '脑中浮出的做法、对事情的理解，是 ideas。像在心里先有一个样子，再拿出来讨论，正好能帮助理解它的看见、形状词源背景。',
 'idea + -s，元音后读 /z/。经拉丁 idea 接希腊 idea 形状、样式、类型，与 idein 看相关；英语早期哲学理念义后来扩大为一般想法。',
 [['希腊 idea／idein → 拉丁 idea → 英语 idea','形状、看见；哲学中的理念等'],['idea + -s → ideas','多个想法、点子、概念']],
 'new ideas 新点子；ideas for a project 项目的构想；exchange ideas 交流想法；have no ideas 一时没有点子。',
 'share ideas；ideas about the future。','I have no idea 常是我不知道，单数固定结构很常见；I have no ideas 常是没点子、想不出办法。数的变化会把重点从知道与否移到有没有构想。',
 ('We shared ideas for making the room more useful.','我们交流了怎样让这个房间更好用的想法。'),('The notebook is full of ideas for future stories.','笔记本里写满了以后创作故事的点子。'),sources=['https://en.wiktionary.org/wiki/ideas#English','https://en.wiktionary.org/wiki/idea#English'])
W('notes','英 /nəʊts/；美 /noʊts/','笔记、便条；音符、语气等；纸币〔部分语境〕；注意到、指出〔动词形式〕',
 '把信息留下一个记号，是 notes：纸上能记笔记，乐谱里能标音符，简短留言能写便条。动词 note 则把值得注意的事标出来、说出来。',
 'note 已有 e，加 s，/t/ 后读 /s/。名词经法语 note 并有早期英语借词背景，接拉丁 nota 标记；动词经法语 noter 接 notare。更深与 noscere 的关系有异议，不强作确定同源。',
 [['拉丁 nota／notare → 法语 note／noter 等 → note','标记；记下、指出'],['note 名词、动词 + -s → notes','多个笔记、音符、便条等；单数主语注意到、指出']],
 'take notes 记笔记；leave notes 留便条；musical notes 音符；banknotes／notes 纸币；notes that ... 指出……。',
 'notes from the meeting；notes on the page。','notes 是为了留住信息的记录，a full report 通常更成篇、系统。notes that ... 中 notes 是动词，后面跟要提醒读者注意的内容。',
 ('I took notes during the talk and reviewed them later.','我听讲时记了笔记，后来又复习了一遍。'),('The guide notes that the entrance closes at five.','指南提醒，入口五点关闭。'),sources=['https://en.wiktionary.org/wiki/notes#English','https://en.wiktionary.org/wiki/note#English'])
W('songs','英 /sɒŋz/；美 /sɔːŋz, sɑːŋz/','歌、歌曲；song 的复数',
 '能唱出来的一首首作品是 songs，通常有曲调，也常有歌词。它把唱歌动作形成的作品数成一首一首。',
 'song + -s，/ŋ/ 后读 /z/，不另添 /ɡ/。song 继承古英语 sang，与 sing 有历史关系；现代不能把元音换位当作随意造词规则。',
 [['古英语 sang → 中古英语 song → song','歌，与 sing 的历史词族相连'],['song + -s → songs','多首歌']],
 'folk songs 民歌；love songs 情歌；sing songs 唱歌；write songs 创作歌曲；songs from a film 电影里的歌曲。',
 'three songs；the words of the songs。','songs 通常可数，music 作音乐总称通常不可数。three songs 是三首歌，some music 是一些音乐；纯器乐作品也常用 pieces、tracks 等按场景称呼。',
 ('We learned two new songs for the concert.','我们为音乐会学了两首新歌。'),('The album includes songs written over several years.','这张专辑收录了几年间创作的歌曲。'),sources=['https://en.wiktionary.org/wiki/songs#English','https://en.wiktionary.org/wiki/song#English'])
W('sources','英 /ˈsɔːsɪz/；美 /ˈsɔːrsɪz/','来源、源头；消息来源、资料出处；寻找货源〔动词形式〕',
 '水从哪里涌出来，信息、材料从哪里来，都可以问 sources。作动词时，则是去找到能供货、提供材料的地方。',
 'source 已有 e，加 s，/s/ 后增加 /ɪz/。古法语 sourse 来自 sourdre 涌起的相关形式，上接拉丁 surgere；寻找货源的英语动词由名词后起发展。',
 [['拉丁 surgere → 法语 sourdre／sourse → source','涌起、源头 → 材料、信息等来源'],['source 名词、动词 + -s → sources','多个来源；单数主语寻找、取得货源']],
 'sources of information 信息来源；historical sources 史料；water sources 水源；sources materials locally 从当地寻找材料供应。',
 'check the sources；sources for the claim。','sources 主要问从哪里来，resources 主要问能用什么。一本书可以是某说法的 source，也可以作为教学 resource，角度不同。',
 ('The article lists its sources at the end.','文章在末尾列出了资料来源。'),('The workshop sources most of its wood locally.','作坊的大部分木材都从当地采购。'),sources=['https://en.wiktionary.org/wiki/sources#English','https://en.wiktionary.org/wiki/source#English'])
W('photos','英 /ˈfəʊtəʊz/；美 /ˈfoʊtoʊz/','照片；photo 的复数',
 '照相机或手机拍下来的一张张影像，就是 photos。日常比 photographs 更短、更口语，但说的通常是同一类东西。',
 'photo + -s，直接加 s，不写 photoes。photo 是 photograph 的后起截短；更早 photograph 用 photo- 光与 -graph 写、记录的希腊材料造词。',
 [['希腊光、记录词的组合材料 → photograph','用光记录的照片名称'],['photograph 缩短 → photo；再加 -s → photos','较短日常名称 → 多张照片']],
 'take photos 拍照；family photos 家庭照片；photos of the trip 旅行照片；share photos 分享照片。',
 'a few photos；photos on the phone。','photos 是照片，pictures 范围更广，也能指画、插图等。以 o 结尾的名词复数不一律加 es：photos、radios，加 s；tomatoes、potatoes 则常加 es。',
 ('I saved the photos in a folder named after the trip.','我把照片保存在一个按这次旅行命名的文件夹里。'),('These photos show the room before it was repaired.','这些照片拍的是房间修缮前的样子。'),sources=['https://en.wiktionary.org/wiki/photos#English','https://en.wiktionary.org/wiki/photo#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xa',ROOTS,WORDS)
 extend_lessons()
