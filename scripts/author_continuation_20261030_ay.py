"""Dream and fan: familiar images without invented source stories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
DR=[['中古英语 dream、dreem；与北欧 draumr 等同族形式相关','睡梦；古英语 drēam 的快乐、音乐义与现代词如何衔接仍有争议'],['现代 dream','睡梦、想象；理想愿望；理想般美好的东西']]
def D(f,m):return DR+[[f,m]]
W('dream','/driːm/','梦；梦想、理想；做梦、向往',
 '睡着时脑里有画面，醒着也能把希望的生活在脑中先过一遍；两种都叫 dream。',
 '现代睡梦义见中古英语，与北欧同族词关系密切。古英语同形词 drēam 多记快乐、音乐，二者关系有争议，不要编成听音乐睡着才产生做梦义。',DR,
 'have a dream 做梦，dream about/of 梦到、梦想，a dream job 理想工作，dream up a plan 想出计划。过去、分词可 dreamed 或 dreamt。',
 'have a dream；dream about；a dream job；dream up。',
 'dream 梦或愿望，nightmare 噩梦、可怕经历；dream of doing 可向往，wouldn’t dream of doing 则常说绝不会考虑那样做。',
 ('I had a strange dream last night.','昨晚我做了个奇怪的梦。'),('She dreams of opening a small café.','她梦想开一家小咖啡馆。'),sources=['https://www.etymonline.com/word/dream','https://en.wiktionary.org/wiki/dream#English'])
W('dreamt','/dremt/','dream 的过去式、过去分词之一',
 '昨天梦到了、曾经梦想过，换的是时间和语法位置，基本意思仍接 dream。',
 'dream 的 -t 过去形式，现代拼写词中有 amt 连写，但读 /dremt/。dreamed 也是标准形式，dreamt 在英式等语境较常见。',D('dream → dreamed／dreamt','规则与 -t 两种过去式、过去分词'),
 'I dreamt that ... 我梦见……，had dreamt of 曾梦想……。不要因为末尾没 -ed 就当成另一个独立词根。',
 'dreamt that；dreamt about；had dreamt of。',
 'dreamt /dremt/ 与 dreamed /driːmd/ 读音不同，但都可标准；dreamed up 想出也接同一个动词。',
 ('I dreamt that I was flying above the sea.','我梦见自己在海面上飞。'),('She had dreamt of this journey for years.','这趟旅行她梦想了好多年。'))
W('dreamer','英 /ˈdriːmə/；美 /ˈdriːmər/','做梦的人；有梦想的人；空想家',
 '同一个想象丰富的人，可以被夸有理想，也可以被嫌不够实际；语气和上下文决定。',
 'dream + -er，中古英语已有对应人物形式。睡梦者和理想、空想者都接 dream 的不同义。',D('dream + -er → dreamer','做梦者；有梦想或爱空想的人'),
 'a practical dreamer 有梦想又肯实干的人，an idle dreamer 空想家。',
 'a practical dreamer；an idle dreamer；a young dreamer。',
 'dreamer 不必然贬义，visionary 常强调有远见，fantasist 更可能说沉溺幻想、编想；别只按中文梦想家一律替换。',
 ('She is a dreamer who also knows how to get things done.','她有梦想，也知道怎样把事情做成。'),('The story begins with a young dreamer leaving home.','故事从一个怀揣梦想的年轻人离家写起。'))
W('dreamy','/ˈdriːmi/','恍惚、爱做白日梦的；梦幻、令人心醉的',
 '人像神游别处，景色像梦里一样柔和美好；都是现实感变淡的感觉。',
 'dream + -y。既可描写人的出神状态，也可评价环境、声音等梦幻宜人。',D('dream + -y → dreamy','像在梦中的；梦幻、令人心醉的'),
 'a dreamy expression 出神的表情，a dreamy atmosphere 梦幻氛围，dreamy music 梦幻音乐。',
 'a dreamy expression；a dreamy atmosphere；dreamy music。',
 'dreamy 常有柔和、恍惚或迷人感觉，dreamlike 泛说像梦，可能美也可能怪；不是所有梦幻场景都快乐。',
 ('He had a dreamy expression during the lesson.','上课时，他一脸神游的表情。'),('Soft lighting gave the room a dreamy atmosphere.','柔和灯光让房间有一种梦幻氛围。'))
W('dreamlike','/ˈdriːmlaɪk/','如梦的；梦一般不真实的',
 '熟悉的东西组合得不太真实，像醒着走进了梦；不必然都是美梦。',
 'dream + -like，后部直接表示像……。按感觉相似命名，不要求真在睡眠中。',D('dream + -like → dreamlike','像梦中的、不太真实的'),
 'a dreamlike scene 如梦场景，a dreamlike quality 如梦特质，a dreamlike sequence 电影的梦境般片段。',
 'a dreamlike scene；a dreamlike quality；a dreamlike sequence。',
 'dreamlike 像梦，dream 理想的修饰用法可说 a dream job；a dreamlike job 不等于通常的理想工作。',
 ('The empty streets had a dreamlike quality.','空荡街道有一种如梦般不真实的感觉。'),('The film ends with a dreamlike sequence.','影片以一段如梦的场景结束。'))
W('dreamland','/ˈdriːmlænd/','梦乡；幻想中的世界',
 '把做梦、幻想想成一个人可以进入的地方；睡着是去了梦乡，脱离实际也可像活在梦里。',
 'dream + land 地方、世界。land 在这里多为想象场所，不需要真有一块土地。',D('dream + land → dreamland','睡梦、幻想所在的想象世界'),
 'drift off to dreamland 渐渐进入梦乡，live in dreamland 活在幻想中。',
 'drift off to dreamland；in dreamland；live in dreamland。',
 'dreamland 多为梦乡或脱离现实的想象处境，dreamscape 特别着眼梦中呈现的景象。',
 ('The child soon drifted off to dreamland.','孩子很快进入了梦乡。'),('Anyone expecting the job to be effortless is living in dreamland.','指望这工作毫不费力的人，是活在幻想里。'))
W('dreamscape','/ˈdriːmskeɪp/','梦中景象；梦境般的画面、世界',
 '把梦里的街道、山川、房间等整个画面看成一片景观。',
 'dream + -scape，后部由 landscape 等类推为景观、场景。不是 dream + escape 逃走。',D('dream + -scape → dreamscape','梦中的景观；梦境般画面'),
 'a surreal dreamscape 超现实梦境，a shifting dreamscape 不断变换的梦中景象。文学、艺术评论常见。',
 'a surreal dreamscape；a shifting dreamscape；a painted dreamscape。',
 'dreamscape 具体画面、世界布局，dreamland 梦乡或幻想世界；二者可重合，但着眼点不同。',
 ('The artist painted a dreamscape of floating islands.','画家画了一片漂浮岛屿组成的梦境。'),('The story moves through a constantly changing dreamscape.','故事在不断变化的梦中世界里展开。'))
W('dreamcatcher','英 /ˈdriːmkætʃə/；美 /ˈdriːmkætʃər/','捕梦网',
 '圆环里编着网，常配羽毛等装饰；名字把过滤坏梦的传统观念说成捕捉梦。',
 'dream + catcher 捕捉者、器具，名称联系奥吉布瓦等原住民传统中的相关物件和信念；后来广泛作为装饰出现。不是所有原住民文化的统一习俗。',D('dream + catcher → dreamcatcher','与传统梦境观念相关的网状物件名称'),
 'a handmade dreamcatcher 手工捕梦网，hang a dreamcatcher 悬挂捕梦网。这里描述传统信念，不声称能实际控制睡梦。',
 'a handmade dreamcatcher；hang a dreamcatcher；a dreamcatcher above the bed。',
 'dreamcatcher 是物件名称，dreamer 是做梦或有梦想的人；catcher 也能用于工具，并非总是人。',
 ('A handmade dreamcatcher hung above the bed.','床头上方挂着一个手工捕梦网。'),('The display explains the cultural background of the dreamcatcher.','展陈解释了捕梦网的文化背景。'))
W('dreamboat','英 /ˈdriːmbəʊt/；美 /ˈdriːmboʊt/','梦中情人；迷人的人〔口语，略显旧式〕',
 '喜欢得像从理想里走出来的人；常夸男性很有魅力，语气带玩笑、浪漫色彩。',
 'dream + boat，可能联系承载梦想、爱情的船的比喻及旧流行歌曲。具体人物义形成不只凭两个词就能完全还原，保留可能性。',D('dream + boat → dreamboat','梦想之舟的比喻 → 很迷人的理想对象'),
 'a real dreamboat 真是个梦中情人。现在常带轻松、戏谑或复古口吻。',
 'a real dreamboat；call someone a dreamboat；a teenage dreamboat。',
 'dreamboat 迷人的人，不是所有梦到的船；dreamer 说有梦、爱想的人，不保证长得迷人。',
 ('In the old film, everyone calls the singer a dreamboat.','老电影里，大家都说那位歌手是梦中情人。'),('She jokingly described the actor as a dreamboat.','她开玩笑地称那个演员为梦中情人。'))
R('B2850','睡梦、想象和理想；梦幻场景与人物分组','DREAM：脑中的画面；也承载现实还没实现的向往','dream → dreamt、dreamer、dreamy、dreamlike；梦中地方和画面一起读，再讲文化物件、迷人对象；daydream、dreamworld 共享。',
 '古英语快乐、音乐的同形词与现代睡梦词如何衔接仍有争议，从可靠中古英语睡梦用法讲起。',
 'dream → dreamt/dreamed；dream + -er/-y/-like；dream + land/world/catcher/boat；dream + -scape；day + dream。',
 [['基本词、变化和人物','dream · dreamt · dreamer'],['状态和类梦特征','dreamy · dreamlike · daydream'],['梦中地方、画面和物件','dreamland · dreamworld · dreamscape · dreamcatcher'],['理想对象的俚语','dreamboat']],
 'dreamt/dreamed 都标准；dreamy 未必等于 dreamlike 所有用法；dreamcatcher 文化物件与信念分清；dreamboat 人物俚语。',
 'The dreamer dreamt of a strange dreamscape and painted it the next day.\n\n这个爱做梦的人梦见奇异景象，第二天把它画了下来。',
 'dream dreamt dreamer dreamy dreamlike daydream dreamland dreamworld dreamscape dreamcatcher dreamboat')
FA=[['拉丁 vannus → 古英语 fann → fan','扬谷器具 → 扇子、风扇；送风、扇动'],['另源 fanatic → fan〔缩略〕','狂热爱好者 → 迷、粉丝；起初常见于美国体育语境']]
W('fan','/fæn/','风扇、扇子；扇动；迷、粉丝〔另源〕',
 '风扇把空气扇起来，粉丝把热情投向喜欢的对象；这两路现代同形，却不能编成同一个来源。',
 '扇具义接古英语 fann，远接拉丁 vannus 扬谷器具；爱好者义通常由 fanatic 缩略，可能也有相关爱好者表达影响。两条历史分开。',FA,
 'an electric fan 电风扇，fan the flames 扇旺火焰、煽动情绪，a football fan 球迷，I’m a fan of ... 我很喜欢……。',
 'an electric fan；fan the flames；a football fan；a fan of。',
 'fan 粉丝常是中性热爱者，fanatic 往往有过度狂热意味；不能因为历史缩略关系就把所有粉丝说成极端狂热者。',
 ('She switched on the fan to cool the room.','她打开风扇，让房间凉快些。'),('I’m a big fan of her writing.','我非常喜欢她写的东西。'),sources=['https://www.etymonline.com/word/fan','https://en.wiktionary.org/wiki/fan#English'])
W('fandom','/ˈfændəm/','粉丝群体；粉丝文化、圈子；作为粉丝的状态',
 '不只一个人喜欢，而是围绕作品、人物、运动形成共同讨论、创作、相聚的圈子。',
 'fan 粉丝 + -dom，后缀可表领域、群体、状态。这里接爱好者 fan，不接风扇。',FA[1:]+[['fan + -dom → fandom','粉丝群体、所形成的圈子和文化']],
 'the fandom of a series 某剧粉丝群体，join a fandom 进入粉丝圈，fandom culture 粉丝文化。',
 'join a fandom；fandom culture；an active fandom。',
 'fan 是单个爱好者，fandom 群体、领域；fan club 是有一定组织形式的粉丝俱乐部，fandom 可以更松散。',
 ('The series has an active online fandom.','这部剧有活跃的网络粉丝群体。'),('She discovered fan art through the fandom.','她通过粉丝圈接触到了同人画作。'))
W('turbofan','英 /ˈtɜːbəʊfæn/；美 /ˈtɜːrboʊfæn/','涡轮风扇发动机；涡扇发动机',
 '发动机带动前部大风扇，一部分空气走外侧通道；飞机发动机名称里常见这个词。',
 'turbo- 涡轮相关 + fan 风扇。这里接送风设备义，不是某种特别热情的粉丝。',FA[:1]+[['turbo- + fan → turbofan','以涡轮驱动风扇的发动机类别']],
 'a turbofan engine 涡扇发动机，a modern turbofan 现代涡扇发动机。先认识类别，不靠词形推算全部机械性能。',
 'a turbofan engine；a modern turbofan；turbofan-powered aircraft。',
 'turbofan 风扇发动机，turbojet 涡喷发动机是相关但不同类别；fan 前部来源看设备，不看粉丝。',
 ('The aircraft uses two turbofan engines.','这架飞机使用两台涡扇发动机。'),('The museum displays a cutaway model of a turbofan.','博物馆展示了一台涡扇发动机的剖面模型。'))
R('B3356','扇具与爱好者两条来源；设备和粉丝扩展分组','FAN：风扇、粉丝同形，来源分开','fan 先明确两源；fandom、fanboy 等接粉丝支线，turbofan 接风扇支线；已有同族词共享。',
 '扇动和热情都能帮助想象，但不是风扇吹得热就变粉丝。爱好者义有 fanatic 缩略来源，现代语气通常更中性。',
 '拉丁 vannus → fann → fan；另源 fanatic → fan；fan + -dom/boy/girl/art/site；super- + fan；turbo- + fan。',
 [['基本词的两条来源','fan'],['爱好者与文化','fandom · fanboy · fangirl · fanart · fansite · superfan'],['设备','turbofan']],
 'fan 中性粉丝不等于 fanatic 的过度狂热；fandom 圈子不必正式俱乐部；turbofan 接风扇义。',
 'The aircraft fan enjoyed studying the turbofan display.\n\n这位飞机迷很喜欢研究涡扇发动机展品。',
 'fan fandom fanboy fangirl fanart fansite superfan turbofan')
if __name__=='__main__':save('continuation_20261030_ay',ROOTS,WORDS)
