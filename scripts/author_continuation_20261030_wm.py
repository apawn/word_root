"""Faces, mouths, body parts and familiar metaphorical uses."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B4351':dict(words=['face','faces'],label='face → faces：脸、表面；面对',note='face 经法语接拉丁 facies，faces 在 /s/ 后增加 /ɪz/；与 facere 的更深关系不当作确定派生。'),
 'B2767':dict(words=['mouth','mouths'],label='mouth → mouths：嘴、开口；用口形说',note='嘴的名词复数常见 /maʊðz/，另有清音变体；动词 mouths 通常读 /maʊðz/，保留名词、动词的读音差别。'),
 'B2766':dict(words=['nose','noses'],label='nose → noses：鼻子、前端；探查',note='nose 已有 e，加 s，词尾增加 /ɪz/；接古英语 nosu，不把末尾 -se 当独立后缀。'),
 'B2772':dict(words=['neck','necks'],label='neck → necks：脖颈与细长连接处',note='neck 继承古英语 hnecca，旧词首 h 消失；necks 的词尾读 /s/。'),
 'B2898':dict(words=['back','backs'],label='back → backs：背部；背面；支持',note='back 名词接古英语 bæc；名词多处背面与动词支持的现代用法同写 backs。'),
 'B3061':dict(words=['heart','hearts'],label='heart → hearts：心脏、内心；红心牌',note='heart 接古英语 heorte，内心、勇气等比喻较早已有；hearts 也用于扑克牌的红心花色。'),
}
W('faces','/ˈfeɪsɪz/','脸、面孔；表面、面；面对、朝向〔face 的第三人称单数〕',
 '人的脸是 face，物体朝外的一面也叫 face；动词则把正面转向某处，或直接面对一个问题。',
 'face 已有 e，加 s；/s/ 后读 /ɪz/。face 经法语接拉丁 facies 外观、面貌，动词由名词发展；与 facere 的更深联系不能当确定父子关系。',
 [['拉丁 facies → 法语 face → 英语 face','外观、面貌 → 脸、表面'],['face 名词、动词 + -s → faces','多个面孔、表面；单数主语面对、朝向']],
 'familiar faces 熟悉的面孔；make faces 做鬼脸；the faces of a cube 立方体各面；faces south 朝南；faces a problem 面临问题。',
 'new faces；faces the garden。','The room faces south 中 faces 是朝向的动词；six faces 中是六个面。make faces 常是做鬼脸，face a difficulty 则是面对困难，注意各自搭配。',
 ('I recognised a few familiar faces in the crowd.','我在人群里认出了几张熟悉的面孔。'),('The kitchen window faces the garden.','厨房窗户朝着花园。'),sources=['https://en.wiktionary.org/wiki/faces#English','https://en.wiktionary.org/wiki/face#English'])
W('mouths','常见 /maʊðz/；名词复数也有 /maʊθs/ 等变体','嘴；河口、洞口等开口；用口形说、空口重复等〔动词形式〕',
 '嘴是进出食物、发声的开口；河流汇出去的地方、洞的入口，也借用嘴这个形状。动词 mouths 常说只动嘴唇把话做出来。',
 'mouth + -s。单数名词常为 /maʊθ/，常见复数变浊音为 /maʊðz/；也有清音复数变体。动词 mouths 通常读 /maʊðz/。词基继承古英语 mūþ，动词由名词发展。',
 [['古英语 mūþ → mouth','嘴；按开口形状扩展为河口、洞口等'],['mouth 名词、动词 + -s → mouths','多个嘴、开口；单数主语用口形说等']],
 'mouths to feed 需要养活的人口；river mouths 河口；the mouths of caves 洞口；mouths the words 用嘴唇做出词的口形；mouths off 顶嘴、放肆说话。',
 'open mouths；mouths a silent warning。','嘴的复数常有 /θ/ 到 /ð/ 的变化，但不把它当所有 th 的统一规则：months 仍常读 /mʌnθs/。mouth 动词也不必表示真的发出了声音。',
 ('The children covered their mouths to keep from laughing.','孩子们捂着嘴，不让自己笑出声。'),('Across the room, she mouths my name and points to the door.','在房间另一头，她用口形叫我的名字，又指了指门。'),('The map marks the mouths of several rivers.','地图标出了几条河流的河口。'),sources=['https://en.wiktionary.org/wiki/mouths#English','https://www.merriam-webster.com/dictionary/mouth'])
W('noses','英 /ˈnəʊzɪz/；美 /ˈnoʊzɪz/','鼻子；机头、船首等前端；探查、用鼻子推碰等〔动词形式〕',
 '脸上向前突出的鼻子，给飞机、船等向前突出的部分提供了形状比喻。动词 nose 则常带用鼻子探、往前探的感觉。',
 'nose 已有 e，加 s；原词结尾 /z/ 后增加 /ɪz/。nose 继承古英语 nosu，现代动词从相应名词发展。',
 [['古英语 nosu → nose','鼻子；形状、位置延伸到机头、船首等'],['nose 名词、动词 + -s → noses','多个鼻子、前端；单数主语探查等']],
 'red noses 红鼻子；wipe their noses 擦鼻子；the noses of planes 飞机机头；noses around ... 在……四处探看；noses the door open 用鼻子把门拱开。',
 'cold noses；noses around the garden。','noses 的结尾增加一个 /ɪz/ 音节，因为 nose 已以 /z/ 收尾；names 末尾 /m/ 后只加 /z/。同写加 s，发音不按字母外观一刀切。',
 ('The children came in with cold hands and red noses.','孩子们进屋时手冰凉，鼻子红红的。'),('The dog noses the door open and comes inside.','狗用鼻子拱开门，走了进来。'),sources=['https://en.wiktionary.org/wiki/noses#English','https://en.wiktionary.org/wiki/nose#English'])
W('necks','/neks/','脖子、颈部；瓶颈等细长部分；neck 的复数',
 '连接头和身体的细长部位是 neck；瓶子、乐器等从主体伸出的细长部分，也可以借这个形状叫 neck。',
 'neck + -s，/k/ 后读 /s/。继承古英语 hnecca，经中古英语 nekke 等到 neck；旧词首 h 在现代不再发音。',
 [['古英语 hnecca → 中古英语 nekke → neck','颈、脖子；延伸到器物细长连接处'],['neck + -s → necks','多个脖颈或相似形状部位']],
 'long necks 长脖子；bottle necks 瓶颈；the necks of guitars 吉他的琴颈；crane their necks 伸长脖子看。',
 'scarves around their necks；narrow necks。','neck 是连接头和身体的整个颈部，throat 常说前面的咽喉区域或内部通道。衣领周围系围巾，通常说 around the neck。',
 ('The birds stretched their necks towards the food.','鸟儿伸长脖子朝向食物。'),('These bottles have narrow necks and wide bases.','这些瓶子颈部细，底部宽。'),sources=['https://en.wiktionary.org/wiki/necks#English','https://en.wiktionary.org/wiki/neck#English'])
W('backs','/bæks/','背部、后背；背面、椅背等；支持、倒车等〔动词形式〕',
 '人的背在身后，椅子托住后背的部分也叫 back。站到某人身后给支持，是动词 back 很直观的理解方式。',
 'back + -s，/k/ 后读 /s/。名词接古英语 bæc，经中古英语 bak 等延续；现代支持、倒退等动词用法与相应位置、动作相连。',
 [['古英语 bæc → 中古英语 bak → back','背部、后面；后来有支持等动词用法'],['back 名词、动词 + -s → backs','多个背部、背面；单数主语支持、倒退等']],
 'the backs of chairs 椅背；the backs of envelopes 信封背面；backs a proposal 支持提案；backs up files 备份文件；backs out 退出、反悔。',
 'backs the team；backs the car into the garage。','backs a plan 是支持计划，backs up a claim 常是拿出证据支持说法。backs up files 则是备份文件，具体意思要看宾语和 up 等小词。',
 ('The chairs have high backs and soft seats.','这些椅子的靠背高，座垫软。'),('The manager backs the plan to extend the opening hours.','经理支持延长营业时间的计划。'),sources=['https://en.wiktionary.org/wiki/backs#English','https://en.wiktionary.org/wiki/back#English'])
W('hearts','英 /hɑːts/；美 /hɑːrts/','心脏；内心、感情、勇气；红心、红桃花色等；heart 的复数',
 '身体里的心脏是 heart，人们也用它谈内心、感情和勇气。hearts 可以是多个人的心，也可以是纸牌上的红心符号。',
 'heart + -s，/t/ 后读 /s/。heart 继承古英语 heorte，较早已有内心、勇气等比喻；红心花色按符号形状命名。',
 [['古英语 heorte → heart','心脏；内心、感情等较早已有的比喻'],['heart + -s → hearts','多颗心、多人内心；纸牌的红心花色等']],
 'their hearts sank 他们心里一沉；win people’s hearts 赢得人心；in our hearts 在我们心里；the queen of hearts 红心皇后。Hearts 也可作相关纸牌游戏名称。',
 'kind hearts；the ace of hearts。','hearts 说身体器官、感情或纸牌花色，靠场景判断。heart 的 ea 在这里不读 /iː/；learn by heart 是背熟的固定搭配，通常不用复数。',
 ('Their hearts sank when they saw the closed gate.','看到大门关着，他们心里一沉。'),('She put the queen of hearts on the table.','她把红心皇后放在桌上。'),sources=['https://en.wiktionary.org/wiki/hearts#English','https://en.wiktionary.org/wiki/heart#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wm',ROOTS,WORDS)
 extend_lessons()
