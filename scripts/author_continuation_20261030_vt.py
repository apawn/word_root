"""Loaves, calves, scarves and fantasy plurals, with distinct origins."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3665':dict(words=['loaf','loaves','lord'],label='loaf／loaves 与 lord：面包和旧家庭称呼',note='loaf 承接古英语 hlaf 面包，lord 的旧组合含面包、守护材料；loaf 闲逛的动词另由 loafer 逆构，不能全串成面包义。'),
 'A1776':dict(words=['calf','calves','scarf','scarves'],label='calf → calves，scarf → scarves：常见 ves 复数',note='calf 的动物与小腿义近源不同；scarves 是围巾复数，另有可接受的 scarfs；现代复数规则不证明底词同源。'),
 'B3940':dict(words=['dwarf','dwarfs','dwarves'],label='dwarf → dwarfs／dwarves：两种名词复数与动词',note='两种名词复数都有词典记录，dwarves 尤其常见于奇幻文学；dwarfs 还可说使某物相形见小。'),
 'B3228':dict(words=['elf','elves','elvish'],label='elf → elves：精灵的复数',note='elf 承接古英语、日耳曼语神话名，普通复数 elves；不同作品塑造的精灵形象不同。'),
}
W('loaf','英 /ləʊf/；美 /loʊf/','一条、一整个成形面包；成条、成块的食物；闲逛、混日子〔另一动词来源〕',
 '烤成一个完整形状、尚未切成一片片的面包，是 a loaf。bread 当材料、食物说，loaf 帮你把成形的一整个数出来。',
 '面包名接古英语 hlaf，属日耳曼语旧面包词族。闲逛的动词 loaf 较晚从 loafer 逆构而来，loafer 更早来源不定，两个同形词分开记来源。',
 [['古英语 hlaf → loaf 名词','成形的一整个面包；也指类似形状的食物'],['另一路：loafer → loaf 动词','闲混的人 → 闲逛、无所事事']],
 'a loaf of bread 一条面包；a sliced loaf 一条切片面包；a loaf tin 面包烤模；loaf around 闲荡。名词复数 loaves。',
 'a freshly baked loaf；loaf about all afternoon。','a slice of bread 是一片，a loaf of bread 是完整一条。loaf around 的动词与面包名近源不同；不能靠同拼写把历史强接在一起。',
 ('I bought a fresh loaf of bread from the bakery.','我从面包店买了一条新鲜面包。'),('We spent the afternoon loafing around the house.','我们整个下午都在家里闲着。'),sources=['https://www.etymonline.com/word/loaf','https://en.wiktionary.org/wiki/loaf#English'])
W('loaves','英 /ləʊvz/；美 /loʊvz/','整条、整个成形面包〔loaf 的复数〕',
 '一条面包叫 a loaf，两条、三条就是 loaves。说的是成形的整份，不是切下来的几片。',
 'loaf 名词的 f 改成 ves，词尾读 /vz/。保留古英语面包名的词族，现代作可数单位，把通常不可数的 bread 数成整条。',
 [['古英语面包词 → loaf','一整个成形面包'],['loaf 的 f → ves → loaves','不止一条面包']],
 'two loaves of bread 两条面包；fresh loaves 新烤面包；bake several loaves 烤几条面包；small loaves 小面包条。',
 'a row of loaves；three loaves。','two breads 在普通购物里通常不如 two loaves of bread 明确；若谈不同面包种类，breads 才另有相应可数用法。',
 ('The baker took six loaves out of the oven.','面包师从烤箱里取出六条面包。'),('We need two loaves of bread for the picnic.','这次野餐需要两条面包。'),sources=['https://www.etymonline.com/word/loaf','https://en.wiktionary.org/wiki/loaves#English'])
W('calf','英 /kɑːf/；美 /kæf/','小牛；某些大型动物的幼崽；小腿肚',
 '农场里跟着母牛的小牛是 calf；人体膝盖下方、腿后侧鼓起的肌肉部位也叫 calf。先把这两个常见意思分别记住。',
 '动物义接古英语 cealf；小腿义借古诺尔斯语 kalfi，较早来源不明。两路是否更远同源有不同分析，不能据今天同形就把小腿说成小牛变来的。',
 [['古英语 cealf → calf','小牛；后来也用于某些大型动物幼崽'],['古诺尔斯语 kalfi → calf','小腿后侧丰满的部位；与动物名的更远关系未定']],
 'a newborn calf 新生小牛；a whale calf 幼鲸；a calf muscle 小腿肌肉；the back of the calf 小腿肚后侧。复数 calves，l 常不发音。',
 'a cow and her calf；a calf muscle。','thigh 是膝盖以上的大腿，calf 是膝盖以下后侧的小腿肚。动物义不能只限于牛，也能用于鲸、象等相应幼崽。',
 ('The calf stayed close to its mother.','小牛紧跟在母牛身旁。'),('The diagram labels the calf muscles in the lower leg.','示意图标出了小腿后侧的肌肉。'),sources=['https://www.etymonline.com/word/calf','https://www.merriam-webster.com/dictionary/calf','https://en.wiktionary.org/wiki/calf#English'])
W('calves','英 /kɑːvz/；美 /kævz/','小牛、某些大型动物幼崽〔复数〕；小腿肚〔复数〕',
 '草地上是几头小牛，或人有两侧小腿肚，都可能用 calves。判断在说动物还是身体，要看周围搭配。',
 'calf 的常见名词复数把 f 改成 ves，结尾读 /vz/，l 仍不发音。动物义接古英语，小腿义经北欧语借入；它们共享现代复数写法。',
 [['calf 的动物义、部位义','近源不同的两个常用同形名词'],['calf 的 f → ves → calves','多个幼崽或小腿肚']],
 'newborn calves 新生小牛；elephant calves 幼象；the muscles in your calves 小腿肚的肌肉；strong calves 结实的小腿肚。',
 'a field of calves；both calves。','现代常用 calves；词典在特定义项、用法中也记录 calfs，学习这里的日常动物、小腿用法先记 calves。',
 ('Several calves were resting in the field.','几头小牛正在田里休息。'),('The trousers were tight around his calves.','这条裤子在他小腿肚的位置很紧。'),sources=['https://www.etymonline.com/word/calf','https://www.merriam-webster.com/dictionary/calf','https://en.wiktionary.org/wiki/calves#English'])
W('scarf','英 /skɑːf/；美 /skɑːrf/','围巾、披肩、头巾；狼吞虎咽地吃〔scarf down，另一路用法〕',
 '一条布围在脖子上保暖，也可披在肩上或包住头部，常叫 scarf。日常另会听到 scarf down a sandwich，意思是很快吃掉三明治。',
 '衣物名通常联系古北法语 escarpe 等带子、肩带词，更早有不同分析；快速吃的动词较晚，可能是 scoff 等口语词的变化，来源也有不确定处。',
 [['法语相关带子、肩带名称 → scarf','布带、披巾 → 常见围巾、头巾等'],['另一条较晚口语动词线 → scarf down','快速、大口吃下']],
 'a woollen scarf 羊毛围巾；a silk scarf 丝巾；wrap a scarf around your neck 在脖子上围围巾；scarf down lunch 很快吃完午餐。',
 'a warm scarf；a scarf over her hair。','围巾复数 scarves、scarfs 都有实际使用。快速吃的动词第三人称通常 scarfs，如 He scarfs down lunch，不套用名词 scarves。',
 ('She wrapped a soft scarf around her neck.','她在脖子上围了一条柔软的围巾。'),('He scarfed down a sandwich before leaving.','出门前，他匆匆吃掉了一个三明治。'),sources=['https://www.etymonline.com/word/scarf','https://www.merriam-webster.com/dictionary/scarf','https://en.wiktionary.org/wiki/scarf#English'])
W('scarves','英 /skɑːvz/；美 /skɑːrvz/','围巾、丝巾、披巾、头巾〔复数〕',
 '店里摆着好几条围巾，或几个人都系着丝巾，通常会说 scarves。它是 scarf 很常见的复数形式。',
 'scarf 的 f 改成 ves，结尾读 /vz/。较早也常写 scarfs，后来 scarves 按其他 f／ves 名词的形式逐渐流行；现代两种复数都可见。',
 [['scarf','经法语等材料进入的衣物名'],['scarf → scarves／scarfs','两种有记录的名词复数，scarves 常见']],
 'woollen scarves 羊毛围巾；silk scarves 丝巾；colourful scarves 彩色围巾；winter scarves 冬季围巾。',
 'a collection of scarves；scarves and hats。','scarves 侧重名词复数；若是 scarf down 的动词第三人称，通常写 scarfs。围巾的材质、形状不固定，按 woollen、silk 等修饰语进一步理解。',
 ('The shop sells scarves in many different colours.','这家店卖各种颜色的围巾。'),('They took off their scarves when they came indoors.','他们进屋后摘下了围巾。'),sources=['https://www.etymonline.com/word/scarf','https://www.merriam-webster.com/dictionary/scarf','https://en.wiktionary.org/wiki/scarves#English'])
W('dwarves','英 /dwɔːvz/；美 /dwɔːrvz/','矮人等〔dwarf 的一种名词复数，奇幻故事中常见〕',
 '奇幻故事里，一群擅长打造器物或居于山中的矮人，常写 dwarves。具体种族形象由作品设定，复数形式本身只说明不止一个。',
 'dwarf 的 f 改成 ves，形成 dwarves；普通复数 dwarfs 也有长期使用。dwarves 在传奇族群用法中由托尔金推广，不能说所有场合都只能写这个形式。',
 [['古英语 dweorg 等 → dwarf','日耳曼语矮人、矮小者的名称'],['dwarf → dwarves／dwarfs','两种名词复数；dwarves 在现代奇幻写作中常见']],
 'a company of dwarves 一队矮人；elves and dwarves 精灵与矮人；the dwarves in the story 故事中的矮人。',
 'a kingdom of dwarves；a tale about dwarves。','dwarves 是名词复数；dwarfs 既能作名词复数，也能是动词第三人称。dwarves 本身不承担那个使显得矮小的动词形式。',
 ('The dwarves built a hall beneath the mountain.','矮人在山下修建了一座大厅。'),('The story describes an alliance between elves and dwarves.','故事描写了精灵与矮人之间的联盟。'),sources=['https://www.etymonline.com/word/dwarf','https://www.merriam-webster.com/dictionary/dwarf','https://en.wiktionary.org/wiki/dwarves#English'])
W('dwarfs','英 /dwɔːfs/；美 /dwɔːrfs/','矮人、矮小者或物等〔dwarf 的复数〕；使相形见小〔dwarf 的第三人称单数〕',
 '名词时，它可以说故事里的多个矮人，或天文学里的矮星。动词时，旁边的新楼太大，把旧楼衬得很小，也用 dwarfs。',
 '名词 dwarf 直接加 -s，或动词 dwarf 加第三人称 -s，两者同写 dwarfs。名词接古英语旧名，动词从相对矮小的性质转成使显小等用法。',
 [['dwarf → dwarfs','规则名词复数，也用于矮星等名称'],['dwarf 动词 + -s → dwarfs','单数主语使另一物相形见小']],
 'red dwarfs 红矮星；the seven dwarfs 七个小矮人；dwarfs the old building 把旧楼衬得很小；dwarfs earlier efforts 使此前努力相形见绌。',
 'white dwarfs；dwarfs everything nearby。','The tower dwarfs the houses 中 dwarfs 是动词，意思是塔楼相比之下显得特别大。名词 dwarfs、dwarves 都有词典记录，不把前者一概判为错误。',
 ('The book has a chapter about red dwarfs.','书里有一章介绍红矮星。'),('The new tower dwarfs the older buildings around it.','新塔楼把周围的旧建筑衬得很小。'),sources=['https://www.merriam-webster.com/dictionary/dwarf','https://www.etymonline.com/word/dwarf','https://en.wiktionary.org/wiki/dwarfs#English'])
W('elves','/elvz/','精灵、小精灵〔elf 的复数〕',
 '童话、民间传说或奇幻小说里，一个是 an elf，一群则是 elves。它们可能被写得小巧顽皮，也可能高大优雅，形象不由这个复数词固定。',
 '现代 elf 的 f 改成 ves。词族接古英语 elf、aelf 及相应复数材料，属于日耳曼语传说名称；更远与白色词根相连只是一种分析。',
 [['古英语及日耳曼语 elf 词族','传说中的精灵、超自然角色'],['现代 elf → elves','普通名词复数；词尾读 /vz/']],
 'woodland elves 森林精灵；a group of elves 一群精灵；elves in a fairy tale 童话中的小精灵；elven／elvish languages 精灵语言〔作品用语等〕。',
 'stories about elves；elves and fairies。','elves 是复数名词；elvish、elven 常作相关形容词。不同作品、传统对 elf 的设定有差别，不用某一部电影的外形去限定所有用法。',
 ('The children read a story about elves in a forest.','孩子们读了一篇森林精灵的故事。'),('In this novel, the elves speak a language of their own.','在这部小说里，精灵说一种自己的语言。'),sources=['https://www.etymonline.com/word/elf','https://en.wiktionary.org/wiki/elves#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vt',ROOTS,WORDS)
 extend_lessons()
