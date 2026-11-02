"""Bow and bends: pronunciation branches, elbow, bout and oxbow."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['古英语 boga → 中古英语 bowe → bow〔弓等〕','弯曲、弓形的物件'],['古英语 būgan → 中古英语 bouen → bow〔躬身〕','弯曲身体、低头'],['船头 bow 经北欧、低地日耳曼语相关词路径','船体前端；与弯曲词族有关，直接传入路线另看']]
W('bow','弓、蝴蝶结：英 /bəʊ/、美 /boʊ/；鞠躬、船头：/baʊ/','弓、琴弓、蝴蝶结；鞠躬；船头',
 '弓是弯着蓄力的，蝴蝶结是带子绕出的圈，鞠躬是身体弯下去。船头也属相关老词路径，但现代读音分两组，不能只记一种。',
 '弓接古英语 boga，躬身动词接 būgan，两条都属弯曲的日耳曼词族。船头借入有北欧、低地日耳曼语相关形式，不能画成现代弓名词必先变成所有其他 bow。',B,
 'a bow and arrow 弓箭，tie a bow 打蝴蝶结，a violin bow 小提琴弓；take a bow 鞠躬谢幕，at the bow 在船头。',
 'a bow and arrow；tie a bow；a violin bow；take a bow；at the bow。',
 '弓与结读 /bəʊ, boʊ/，鞠躬与船头读 /baʊ/。bow out 退出、不再参与；不是每个 bow 都是同一个现代词义随意转用。',
 ('She tied the ribbon into a bow.','她把丝带打成蝴蝶结。'),('The actors took a bow after the performance.','演出后，演员们鞠躬谢幕。'),('He stood at the bow of the boat.','他站在船头。'),
 sources=['https://en.wiktionary.org/wiki/bow#English','https://www.etymonline.com/word/bow'])
W('bowtie','英 /bəʊˈtaɪ/；美 /ˈboʊtaɪ/','领结、蝴蝶领结',
 '领口那条打成左右两个圈、像蝴蝶形的短领带。这里 bow 是结，不是低头的动作。',
 'bow 蝴蝶结 + tie 领带、系结，合成衣饰名。也见分写 bow tie，这里用合写词头。',B[:1]+[['bow + tie → bowtie','打成蝴蝶形的领结']],
 'wear a bowtie 戴领结，a black bowtie 黑领结，tie a bowtie 打领结。',
 'wear a bowtie；a black bowtie；tie a bowtie。',
 'bowtie 领结，necktie 日常常指长领带；前项 /bəʊ, boʊ/，不按鞠躬 /baʊ/ 读。',
 ('He wore a black bowtie to the concert.','他戴着黑领结去听音乐会。'),('She helped him tie his bowtie.','她帮他打好领结。'))
W('bowman','英 /ˈbəʊmən/；美 /ˈboʊmən/','弓箭手〔常见于历史叙述〕',
 '使用弓的人，名字直接把器具和人物合在一起；复数 bowmen 的后半变 men。',
 '中古英语已有 boweman、bouman 等，对应 bow 弓 + man 人。这里主要讲弓箭手，船上岗位的同形用法按船头读音另辨。',B[:1]+[['bow + man → 中古英语 boweman 等 → bowman','持弓、用弓的人']],
 'a skilled bowman 熟练的弓箭手，medieval bowmen 中世纪弓箭手，a line of bowmen 一排弓箭手。',
 'a skilled bowman；medieval bowmen；a line of bowmen。',
 'bowman 与 archer 义近，archer 日常较常见；bowman 说弓箭手时用弓的读音，不是鞠躬的人。',
 ('The story follows a young bowman.','故事讲述了一位年轻弓箭手的经历。'),('A line of bowmen stood along the wall.','一排弓箭手站在城墙边。'))
W('elbow','英 /ˈelbəʊ/；美 /ˈelboʊ/','肘、胳膊肘；用肘挤、推',
 '前臂与上臂相接、能弯起来的地方；在人群中用这块凸出的肘挤开路，elbow 便能作动词。',
 '古英语 elboga、elnboga，经中古英语 elbowe；原来前项接前臂的旧词，后项是 bow 弯曲。现代 el- 不再是一个随处能接的肘前缀。',
 [['古英语 elboga、elnboga → 中古英语 elbowe → elbow','前臂的弯曲处 → 肘'],['现代 elbow〔动词〕','用肘挤、推开位置']],
 'bend your elbow 弯肘，rest on your elbows 用肘撑着，elbow your way through 挤着穿过；管道 elbow 也可说弯头。',
 'bend your elbow；rest on your elbows；elbow your way through。',
 'elbow 肘，wrist 手腕；elbow room 字面能伸肘的空间，再比喻活动、施展余地。',
 ('He rested his elbows on the table.','他把双肘支在桌上。'),('She elbowed her way through the crowd.','她用肘挤着穿过人群。'))
W('oxbow','英 /ˈɒksbəʊ/；美 /ˈɑːksboʊ/','牛轭的弯曲部分；U 形河曲；牛轭湖〔相关表达〕',
 '旧时套在牛颈周围的弯件像一个 U；河道绕出类似大弯，或弯道与主河道分离后留下湖，也借这形状命名。',
 'ox 牛 + bow 弯曲物，先看轭的形状，再看河曲、oxbow lake 的地理比喻。不是牛使用的弓箭。',B[:1]+[['ox + bow → oxbow','牛轭弯件 → 形似的河曲等']],
 'an oxbow lake 牛轭湖，a river oxbow 河流的大弯，an old oxbow 旧河曲。',
 'an oxbow lake；a river oxbow；an old oxbow。',
 'oxbow lake 常由曲流裁弯取直后遗留，不是所有 U 形湖都凭外观就能判成相同成因；名字先给形状线索。',
 ('The old river bend became an oxbow lake.','那处旧河湾后来成了一座牛轭湖。'),('Birds gathered around the oxbow lake.','鸟儿聚在牛轭湖周围。'),
 sources=['https://en.wiktionary.org/wiki/oxbow#English','https://www.etymonline.com/word/oxbow','https://eros.usgs.gov/earthshots/oxbow-lakes'])
W('bout','/baʊt/','一场〔拳击等〕比赛；一阵、一段发作',
 '不是一直持续下去，而是一次集中发生的比赛、活动或不适：a bout of coughing 就是一阵咳嗽。',
 '中古英语 bout、bught 等接弯、回转的旧词，可能有未见记录的古英语中间形。意思由绕行、一次循环发展到一轮活动、比赛或一阵发作；与 bow 的弯曲词族相关，不是现代 bow 随便换字母。',
 [['中古英语 bught、bout 等〔弯、回转〕→ bout','一轮、一次循环'],['活动轮次 → 比赛、疾病等一阵','集中发生的一段']],
 'a boxing bout 一场拳击赛，a bout of coughing 一阵咳嗽，a bout of flu 一次流感发作。',
 'a boxing bout；a bout of；a bout of coughing。',
 'a boxing bout 往往整场比赛，不等于 round 单回合；口语 ’bout 还可以是 about 的省略，与这条比赛名词路线分开。',
 ('The boxer won the bout on points.','拳手凭点数赢得了这场比赛。'),('A bout of coughing interrupted the speech.','一阵咳嗽打断了讲话。'),
 sources=['https://en.wiktionary.org/wiki/bout#English','https://www.etymonline.com/word/bout'])
R('B3293','弯曲的物件、动作、身体部位与轮次','BOW：看见弯，再分 /bəʊ, boʊ/ 与 /baʊ/ 两组读音','bow 为入口；bowtie、bowman、crossbow、longbow 接结与弓；elbow、rainbow、oxbow 接弯形；bout 接绕行到一轮的历史。',
 '弓、鞠躬、船头在更远词族上相关，直接传入路径不同。bower 凉亭、住处另从古英语 būr，不能因字母相像混进弓。',
 '古英语 boga 弓、būgan 弯分别接现代 bow；ell 类前臂词 + bow → elbow；ox + bow；bout 有旧弯、回转的中间路线。',
 [['弓、结与人物器具','bow · bowtie · bowman · crossbow · longbow'],['身体、天空与河道的弯','elbow · rainbow · oxbow'],['轮次与发作','bout']],
 '弓结 /boʊ/，鞠躬船头 /baʊ/；bout 比赛非单回合；bower 来源另看；oxbow 湖不只凭 U 形外观确定成因。',
 'He bent his elbow and adjusted his bowtie before taking a bow.\n\n他弯起胳膊整理领结，然后鞠躬谢幕。','bow bowtie bowman crossbow longbow elbow rainbow oxbow bout')
ROOTS[-1]['exclude']['bower']='常见住处、凉亭义接古英语 būr，不是 bow 弓或鞠躬的直接派生。'
if __name__=='__main__':save('continuation_20261030_dj',ROOTS,WORDS)
