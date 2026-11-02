"""Snow: visible compounds, weather, travel and a few common metaphors."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['古英语 snāw → 中古英语 snaw、snow → snow','雪；本族继承词'],['中古英语 snouen 等 → 现代动词 snow','下雪；现代动词形式接名词发展']]
def SH(f,m):return S[:1]+[[f,m]]
W('snow','英 /snəʊ/；美 /snoʊ/','雪；下雪',
 '从空中飘下、落地积成白层的雪。英语名词和动词同形：snow on the road 是路上的雪，It is snowing 是正在下雪。',
 '名词继承古英语 snāw，经中古英语变成 snow。现代动词接中古英语基于雪名词的形式发展，不能把名词、动词当完全同一次借词。',S,
 'heavy snow 大雪，fresh snow 新雪，It snows 下雪，be snowed in 被雪困住。snow 常不可数，the winter snows 可说多场降雪、大片积雪。',
 'heavy snow；fresh snow；It is snowing；be snowed in。',
 'snow 雪，sleet、hail 是不同天气现象；snowy 是有雪、多雪的形容词，snowing 是下雪动作正在发生。',
 ('Fresh snow covered the road.','新雪覆盖了道路。'),('It started to snow just after midnight.','刚过午夜就开始下雪。'))
W('snowy','英 /ˈsnəʊi/；美 /ˈsnoʊi/','有雪的、多雪的；雪白的',
 '眼前这地方、这一天带着雪的特点；也能借雪的白描写头发、羽毛等。',
 '古英语 snāwiġ → 中古英语 snowy 等 → snowy；现代对应 snow + -y。不是昨天才在英语里临时拼成的新形容词。',SH('古英语 snāwiġ → snowy；现代对应 snow + -y','有雪、多雪、像雪一样白'),
 'a snowy morning 下雪的早晨，snowy mountains 雪山，snowy hair 雪白头发。',
 'a snowy morning；snowy mountains；snowy hair。',
 'snowy 描写有雪或雪白，snowing 说正在下雪；山顶 snowy 时，天空也可能很晴朗。',
 ('We woke up to a snowy morning.','我们醒来时，外面是个白雪覆盖的早晨。'),('The snowy peaks glowed in the evening light.','雪峰在傍晚的光线中发亮。'))
W('snowflake','英 /ˈsnəʊfleɪk/；美 /ˈsnoʊfleɪk/','雪花；过分敏感的人〔讥称〕',
 '雪以一片片的形态落下，flake 就是薄片。讥称人物时，则带觉得对方太容易受伤、太把自己当特殊的评价。',
 'snow + flake 薄片。人物俚义是后来的比喻，带说话者的态度，不是对某类人的客观诊断。',SH('snow + flake → snowflake','一片雪花；后来有讥称人物的用法'),
 'a falling snowflake 飘落的雪花，catch snowflakes 接雪花；人物 snowflake 常含贬义，阅读时认出语气。',
 'a falling snowflake；catch snowflakes；snowflake patterns。',
 'snowflake 一片雪花，snowfall 一场降雪、降雪量；把人叫 snowflake 是评价，不是中性的敏感者名称。',
 ('A snowflake landed on her sleeve.','一片雪花落在她袖子上。'),('The article criticized the habit of calling people snowflakes.','文章批评了动不动就把人讥称为 snowflakes 的习惯。'))
W('snowball','英 /ˈsnəʊbɔːl/；美 /ˈsnoʊbɔːl/','雪球；像滚雪球一样增大',
 '小雪团滚着粘上更多雪，越滚越大；费用、麻烦、关注度不断带来新的增长，也叫 snowball。',
 '中古英语已有 snoweball 等，snow + ball。动词及 snowball effect 借雪球增长的形象，不必真有雪。',SH('snow + ball → snowball','雪球 → 比喻越积越大、发展加快'),
 'throw a snowball 扔雪球，a snowball effect 滚雪球效应，costs snowball 费用不断膨胀，snowball into a crisis 演变扩大为危机。',
 'throw a snowball；a snowball effect；costs snowball；snowball into。',
 'snowball 强调小事牵出更多、越积越大，不保证永远是坏事；support can snowball 支持也可迅速扩大。',
 ('The children threw snowballs at each other.','孩子们互相扔雪球。'),('A small delay snowballed into a major problem.','一点小延误滚雪球般发展成了大问题。'))
W('snowman','英 /ˈsnəʊmæn/；美 /ˈsnoʊmæn/','雪人',
 '用雪堆成像人的形状，眼睛、鼻子等可以再放上去；名字说材料和造型。',
 'snow + man 人，复数 snowmen。这里 man 是人形的命名材料，不是保证里面有个真正的人。',SH('snow + man → snowman','用雪做的人形'),
 'build a snowman 堆雪人，a melting snowman 正在融化的雪人，two snowmen 两个雪人。',
 'build a snowman；a melting snowman；two snowmen。',
 'snowman 雪人，snowball 雪球；做雪人可以用雪球堆，但两个词不是同一形状名称。',
 ('We built a snowman in the garden.','我们在花园里堆了个雪人。'),('The snowman began to melt in the afternoon sun.','雪人在午后的阳光下开始融化。'))
W('snowstorm','英 /ˈsnəʊstɔːm/；美 /ˈsnoʊstɔːrm/','暴风雪、猛烈降雪的天气',
 'storm 指强烈风暴天气，前面的 snow 说明主要伴随雪；比平静飘几片雪更猛烈。',
 'snow + storm，早有分写、连写等形式，现代采用合写词头。',SH('snow + storm → snowstorm','伴随强烈降雪的风暴天气'),
 'a heavy snowstorm 强暴风雪，caught in a snowstorm 遭遇暴风雪，after the snowstorm 暴风雪后。',
 'a heavy snowstorm；caught in a snowstorm；after the snowstorm。',
 'snowfall 说降雪事件或量，snowstorm 强调猛烈天气；blizzard 在气象语境有更具体条件，不能从日常近义直接推相同标准。',
 ('The flight was delayed by a snowstorm.','航班因暴风雪延误。'),('They stayed indoors during the snowstorm.','暴风雪期间，他们待在室内。'))
W('snowmobile','英 /ˈsnəʊməbiːl/；美 /ˈsnoʊməbiːl/','机动雪地车',
 '专门在雪地上行进的小型机动车，通常前面滑板导向、下面履带推进。',
 'snow + -mobile，后一个成分接可移动、车辆命名的用法。这里 mobile 不指移动电话。',SH('snow + -mobile → snowmobile','用于雪地行驶的机动车'),
 'ride a snowmobile 骑雪地车，a snowmobile trail 雪地车路线，a snowmobile tour 雪地车游览。',
 'ride a snowmobile；a snowmobile trail；a snowmobile tour。',
 'snowmobile 机动车，sled/sledge 雪橇可无发动机；snowplow 主要功能是清雪，不能仅因在雪上开就当同一种车。',
 ('They reached the cabin by snowmobile.','他们乘雪地车到了小屋。'),('A snowmobile trail runs through the forest.','一条雪地车路线穿过森林。'))
W('snowshoe','英 /ˈsnəʊʃuː/；美 /ˈsnoʊʃuː/','雪鞋、雪地行走用的宽底装具；穿雪鞋行走',
 '把脚下接触面积放大，走松软雪地时不那么容易深陷；是鞋外的宽装具，不只是厚一点的靴子。',
 'snow + shoe，按雪地用途命名，后来也作使用雪鞋行走的动词。',SH('snow + shoe → snowshoe','雪地宽底装具；使用它行走'),
 'a pair of snowshoes 一副雪鞋，go snowshoeing 穿雪鞋徒步，snowshoe through the woods 穿雪鞋走树林。',
 'a pair of snowshoes；go snowshoeing；snowshoe through the woods。',
 'snowshoe 增大接地面以便走雪地，ski 滑雪板更长、常用于滑行；snow boot 是防寒靴，不等于雪鞋装具。',
 ('We rented snowshoes for the walk.','我们为这次徒步租了雪鞋。'),('They snowshoed through the quiet forest.','他们穿着雪鞋走过安静的森林。'))
W('snowmelt','英 /ˈsnəʊmelt/；美 /ˈsnoʊmelt/','融雪；雪融化形成的水',
 '冬天积下的雪暖起来变成水，既可以说这个过程，也可以说流进河里的融雪水。',
 'snow + melt 融化，合成过程、产物名称。不是把 snow 名词直接加过去式。',SH('snow + melt → snowmelt','雪的融化；融雪水'),
 'spring snowmelt 春季融雪，water from snowmelt 融雪形成的水，snowmelt feeds the river 融雪水补给河流。',
 'spring snowmelt；water from snowmelt；snowmelt runoff。',
 'snowfall 雪落下来，snowmelt 雪化开；snowpack 是积雪层，融化后可成为 snowmelt。',
 ('Spring snowmelt feeds the river.','春季融雪水补给着这条河。'),('The stream was swollen with snowmelt.','小溪因融雪水而水量大增。'))
W('snowbird','英 /ˈsnəʊbɜːd/；美 /ˈsnoʊbɜːrd/','冬季常见的某些鸟；迁往温暖地区过冬的人〔北美口语〕',
 '鸟义与冬季、雪地出现的习性有关，不是所有白鸟的统称；人物义像候鸟一样，天冷就去暖和地方过冬。',
 'snow + bird。旧有冬季鸟名，后来人物比喻常用于北美季节性避寒居住者。并不把此词当唯一鸟种的全球标准名。',SH('snow + bird → snowbird','冬季鸟称；比喻季节性迁居避寒的人'),
 'Canadian snowbirds 到温暖地区过冬的加拿大居民，snowbirds return north 避寒者春暖后北返。',
 'Canadian snowbirds；snowbirds return north；winter snowbirds。',
 '人物 snowbird 常指每年季节性移动，不等于 immigrant 移民永久迁居；也不是每个向南旅行的游客都固定叫 snowbird。',
 ('The town welcomes snowbirds every winter.','这个小镇每年冬天都迎来避寒居住的人。'),('Many snowbirds return north in the spring.','许多避寒者春天返回北方。'))
W('snowplow','英 /ˈsnəʊplaʊ/；美 /ˈsnoʊplaʊ/','铲雪车、除雪犁',
 '像犁把泥土翻开那样，把路面的雪推到旁边，让道路露出来；可以说铲雪部件，也可以说装它的车。',
 'snow + plow 犁；英式常拼 snowplough，含义相同，不另立讲解。',SH('snow + plow → snowplow','推开道路积雪的装置或车辆'),
 'a snowplow cleared the road 铲雪车清路，a snowplow driver 铲雪车司机，wait for the snowplow 等铲雪车。',
 'a snowplow driver；clear the road；wait for the snowplow。',
 'snowplow 推、铲雪，snowmobile 载人在雪地行进；plow/plough 是拼写差别，不是两种完全不同原理。',
 ('A snowplow cleared the main road before dawn.','天亮前，铲雪车清理了主路。'),('The snowplow left a ridge of snow beside the driveway.','铲雪车在车道旁留下了一道雪堆。'))
W('snowbound','英 /ˈsnəʊbaʊnd/；美 /ˈsnoʊbaʊnd/','被雪困住、被积雪封闭的',
 '雪厚到走不了、出不去，地方或人仿佛被雪绑住；不是往雪地开去的目的地方向。',
 'snow + -bound，-bound 在此接受限制、被困的含义，对照 bind 的束缚意象；不与 London-bound 那种驶往方向义混。',SH('snow + -bound → snowbound','被雪限制住、困住'),
 'a snowbound village 被雪封住的村庄，snowbound travellers 被雪困住的旅客，remain snowbound 仍被雪困住。',
 'a snowbound village；snowbound travellers；remain snowbound。',
 'snowy 只是有雪，snowbound 已强调雪造成阻隔；snowbound 不是一定被埋在雪下面。',
 ('The snowbound village received supplies by helicopter.','被雪封住的村庄靠直升机收到补给。'),('We spent two snowbound days in the cabin.','我们被雪困在小屋里待了两天。'))
W('snowdrop','英 /ˈsnəʊdrɒp/；美 /ˈsnoʊdrɑːp/','雪花莲〔一种早开的小白花〕',
 '低垂的小白花像一滴白色水珠，常在冬末、早春出现；名字是形象联想，不是从天上掉下来的雪滴。',
 'snow + drop，形成花名 Galanthus 的常用称呼。白、下垂形状有助记忆，不把这一形象补成某个确证的首次命名故事。',SH('snow + drop → snowdrop','白色低垂、较早开花的植物名称'),
 'snowdrops in the garden 花园里的雪花莲，snowdrops appear 雪花莲出现、开放，a clump of snowdrops 一丛雪花莲。',
 'snowdrops in the garden；a clump of snowdrops；snowdrops appear。',
 'snowdrop 花名，snowflake 日常先说雪花；植物俗名还可能另有同名，认植物看属名与语境。',
 ('Snowdrops appeared beside the garden wall.','花园墙边开出了雪花莲。'),('The first snowdrops were a welcome sign of spring.','最早开放的雪花莲带来了让人欣喜的春意。'),
 sources=['https://en.wiktionary.org/wiki/snowdrop#English','https://www.etymonline.com/word/snowdrop','https://www.rhs.org.uk/plants/snowdrops/growing-guide'])
R('B3118','雪的状态、形状、天气、出行与比喻','SNOW：先看飘落和积成白层，再看它怎样阻路、融化、被做成物件','snow → snowy；snowflake、snowball、snowman 从片、球、人形展开；天气、交通、融雪分组；植物与迁居人物另列。',
 'snowball 的增大、snowbound 的被困都有直观动作。snowdrop 是花，snowbird 可是避寒者，不把所有复合词机械译为雪加后项。',
 '古英语 snāw → snow；snowy 保留 snāwiġ 老形；snow + flake/ball/man/storm/mobile/shoe/melt/bird/plow；snow + -bound。',
 [['基础、性质与形状','snow · snowy · snowflake · snowball · snowman'],['天气、积雪与融水','snowstorm · snowpack · snowmelt'],['雪地活动与受阻','snowboard · snowmobile · snowshoe · snowplow · snowbound'],['植物和人物比喻','snowdrop · snowbird']],
 'snowy 不一定正在 snowing；snowball 可比喻增长；snowbound 已受阻，非仅有雪；snowmobile/snowplow 功能不同；snowdrop 花，snowbird 有人物义。',
 'The snowbound village waited for the snowplow while the children built a snowman.\n\n村庄被雪封住，大家等铲雪车来，孩子们则在堆雪人。','snow snowy snowflake snowball snowman snowstorm snowpack snowmelt snowboard snowmobile snowshoe snowplow snowbound snowdrop snowbird')
ROOTS[-1]['exclude']['snows']='snow 的规则复数或动词第三人称，已在 snow 条内说明，不另立重复词头。'
if __name__=='__main__':save('continuation_20261030_de',ROOTS,WORDS)
