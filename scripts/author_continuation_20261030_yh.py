"""Everyday clothing, including the older sources of sock, glove and trousers."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2910':dict(words=['shirt','shirts'],label='shirt → shirts：衬衫与复数',note='本族古英语衣服词延续；与 skirt 的历史联系不等于现代可以互换。'),
 'B2912':dict(words=['shoe','shoes'],label='shoe → shoes：鞋与复数',note='古英语鞋名延续，现代 shoe 作为一个整体学习。'),
 'A1776':dict(words=['sock','socks','glove','gloves','trousers'],label='服饰中的 -s：袜子、手套与裤子的复数',note='sock、glove 各有自己的来源；trousers 是通常按复数使用的裤子名称，不能只按去掉 s 猜历史。'),
 'B2951':dict(words=['coat','coats'],label='coat → coats：外套与覆盖的一层',note='衣物名扩展到覆盖物、涂层，名词也发展成涂覆动词。'),
 'B3722':dict(words=['jacket','jackets'],label='jacket → jackets：短外套与外护套',note='法语衣服名称的小称借入英语，后用于书等物体的外保护层。'),
 'B3655':dict(words=['hat','hats'],label='hat → hats：帽子与担任的角色',note='古英语帽名延续；角色比喻来自戴不同帽子代表不同身份。'),
 'B2942':dict(words=['bag','bags'],label='bag → bags：袋与装袋、取得',note='北欧相关袋子词借入；英语又由名词发展出动词。'),
 'B3508':dict(words=['pocket','pockets'],label='pocket → pockets：小袋与放进口袋',note='古法语小袋名称借入，衣袋、局部小区域和收进自己手里的动词义各有扩展。'),
}
W('shirts','英 /ʃɜːts/；美 /ʃɜːrts/','衬衫〔shirt 的复数〕',
 '挂着、叠着的一件件衬衫，就是 shirts。先把它当作具体衣物，再留意前面的词说明材质、样式或用途。',
 'shirt + -s，/t/ 后读 /s/。shirt 延续古英语 scyrte，经中古英语形式发展；它与 skirt 的较早历史有关，英语中的两词后来走向不同衣物。',
 [['古英语 scyrte → 中古英语 → shirt','贴身穿的衣服 → 衬衫'],['shirt + -s → shirts','多件衬衫']],
 'cotton shirts 棉衬衫；short sleeved shirts 短袖衬衫；iron the shirts 熨衬衫。',
 'shirts hanging in the wardrobe；two clean shirts。','a shirt 数一件；a pair of shirts 是把两件凑成一对，普通数两件直接说 two shirts。shirt 的复数无需增加音节。',
 ('She folded the clean shirts and put them away.','她把洗干净的衬衫叠好收了起来。'),('He packed two shirts for the weekend trip.','他为周末旅行装了两件衬衫。'),sources=['https://en.wiktionary.org/wiki/shirts#English','https://en.wiktionary.org/wiki/shirt#English'])
W('shoes','/ʃuːz/','鞋〔shoe 的复数〕；给马钉蹄铁〔第三人称单数〕',
 '包住脚、让脚踩在地上的一双鞋，是 shoes；马脚上保护蹄子的铁件，也沿用 shoe 这个名称。',
 'shoe + -s，元音后读 /z/。shoe 延续古英语 scōh，经过中古英语 sho 等形式；蹄铁义及钉蹄铁动词属于鞋与护脚作用的扩展，更深来源不定。',
 [['古英语 scōh → 中古英语 sho 等 → shoe','鞋；保护脚或蹄的器物'],['shoe + -s → shoes','多只鞋；单数主语给马钉蹄铁']],
 'running shoes 跑鞋；leather shoes 皮鞋；a pair of shoes 一双鞋；take off your shoes 脱鞋。',
 'shoes by the door；shoes that fit well。','two shoes 是两只鞋，a pair of shoes 通常是一双。shoe 的过去式、过去分词可用 shod，较常见于给马钉蹄铁等语境。',
 ('Please leave your shoes by the door.','请把鞋放在门边。'),('These shoes are comfortable enough for a long walk.','这双鞋很舒服，适合走较长的路。'),sources=['https://en.wiktionary.org/wiki/shoes#English','https://en.wiktionary.org/wiki/shoe#English'])
W('sock','英 /sɒk/；美 /sɑːk/','短袜；袜子',
 '套在脚上、通常穿在鞋里面的那层柔软织物，是 sock。它的老名字最初却指一种轻便鞋，后来转用于袜子。',
 '现代把 sock 整体记。拉丁 soccus 轻便鞋、拖鞋借入古英语为 socc，再经中古英语 sok 发展为 sock；拉丁词更早可能与希腊相关鞋名相连，远源未定。',
 [['拉丁 soccus → 古英语 socc','轻便鞋、拖鞋'],['中古英语 sok → sock','名称转用于包脚的袜子']],
 'a cotton sock 一只棉袜；a hole in a sock 袜子上的洞；one sock missing 少了一只袜子。',
 'a sock under the bed；the heel of a sock。','sock 是一只；一双是 a pair of socks。这里先掌握衣物义；常见复数 socks 接在后面。',
 ('I found a sock under the bed.','我在床底下找到一只袜子。'),('There is a small hole in this sock.','这只袜子上有个小洞。'),sources=['https://www.etymonline.com/word/sock','https://en.wiktionary.org/wiki/sock#English'])
W('socks','英 /sɒks/；美 /sɑːks/','袜子〔sock 的复数〕',
 '一只只包住脚的织物，是 socks；通常左右脚各穿一只，所以生活里很常直接见到复数。',
 'sock + -s，/k/ 后读 /s/。单词底层继承古英语 socc，较早是拉丁 soccus 轻便鞋的借词；现代复数按普通规则形成。',
 [['拉丁 soccus → 古英语 socc → sock','轻便鞋名 → 袜子'],['sock + -s → socks','多只袜子；常按双使用']],
 'wool socks 羊毛袜；clean socks 干净袜子；a pair of socks 一双袜子；matching socks 配对的袜子。',
 'put on your socks；socks in the drawer。','a pair of socks 是一双；two pairs of socks 是两双。socks 本身数的是袜子，不直接告诉你总共有几双。',
 ('She put on thick socks before going outside.','出门前她穿上了厚袜子。'),('I bought three pairs of socks.','我买了三双袜子。'),sources=['https://en.wiktionary.org/wiki/socks#English','https://www.etymonline.com/word/sock'])
W('glove','/ɡlʌv/','手套',
 '把手包住、让手指分别伸进去的保护套，是 glove。保暖手套、工作手套、拳击手套，靠前面的词说明用途。',
 'glove 继承古英语 glōf。更早常重建为日耳曼语 *galofo，可能含集合前缀与手、手掌的旧词；这种分析带有不确定性，现代不拆成 g + love。',
 [['较早日耳曼语手部覆盖物词 → 古英语 glōf','包住手的器具；更早构成有推测'],['古英语 glōf → glove','手套；继而用于各类专门手套']],
 'a leather glove 一只皮手套；a boxing glove 一只拳击手套；fit like a glove 非常合身。',
 'a glove on the floor；a glove that protects the hand。','love 和 glove 拼写相近，glove 的构词历史却接手套旧词。fit like a glove 抓的是紧贴、合适的画面，也能说衣服以外的东西很适合。',
 ('He took off one glove to use his phone.','他脱下一只手套来用手机。'),('The new jacket fits like a glove.','这件新夹克穿着特别合身。'),sources=['https://www.etymonline.com/word/glove','https://en.wiktionary.org/wiki/glove#English'])
W('gloves','/ɡlʌvz/','手套〔glove 的复数〕',
 '给两只手各套上保护层，就是戴 gloves 的日常画面；复数也可泛指几只、几副手套。',
 'glove + -s，浊音 /v/ 后读 /z/。glove 继承古英语 glōf；更早可能连接手、手掌的日耳曼语旧词，现代词尾 e 不单独发音。',
 [['古英语 glōf → glove','手部覆盖物 → 手套'],['glove + -s → gloves','多只手套；常成副使用']],
 'wear gloves 戴手套；rubber gloves 橡胶手套；gardening gloves 园艺手套；a pair of gloves 一副手套。',
 'gloves for working outdoors；gloves in a coat pocket。','gloves 的 v 保留 /v/，与部分以 f 结尾名词的变形不是同一条规则。一副用 a pair，一般说戴手套用 wear gloves。',
 ('She wears gloves when working in the garden.','她在花园里干活时戴手套。'),('His gloves were still wet from the snow.','他的手套还被雪弄得湿湿的。'),sources=['https://en.wiktionary.org/wiki/gloves#English','https://www.etymonline.com/word/glove'])
W('trousers','英 /ˈtraʊzəz/；美 /ˈtraʊzərz/','裤子；长裤',
 '腰部连在一起、下面分成两条裤腿的衣物，是 trousers。英语日常把这个衣物名称按复数使用，一条裤子也说 a pair of trousers。',
 '来自盖尔语或中古爱尔兰语 triubhas 的裤子名称，借入英语有 trouse、trouzes、trossers 等旧形式，后为 trousers。第二个 r 的出现不完全清楚，可能受 drawers 等复数衣物词影响；更远来源不定。',
 [['盖尔语／中古爱尔兰语 triubhas → 英语 trouse 等','一种贴身裤子名称借入'],['较早复数形式 → trousers','形成今天通常按复数使用的裤子词']],
 'a pair of trousers 一条裤子；black trousers 黑裤子；trouser legs 裤腿；try on trousers 试穿裤子。',
 'These trousers are too long；two pairs of trousers。','trousers 通常接 are；a pair of trousers 的主语核心是 pair，可接 is。英式 trousers 常对应美式 pants；英式 pants 还常说内裤，按地区与语境判断。',
 ('These trousers are too long for me.','这条裤子对我来说太长了。'),('She bought a pair of trousers for work.','她买了一条上班穿的裤子。'),sources=['https://www.etymonline.com/word/trousers','https://en.wiktionary.org/wiki/trousers#English'])
W('coats','英 /kəʊts/；美 /koʊts/','外套；涂层〔复数〕；涂覆〔第三人称单数〕',
 '穿在身体外面的一层是 coats 的外套义；刷在墙外面的一层漆，也能叫 a coat。共同画面是包在外面的一层。',
 'coat + -s，/t/ 后读 /s/。coat 经古法语 cote、cotte 的衣物名称借入，较早有日耳曼语背景；英语再扩展到覆盖层与给表面涂覆。',
 [['古法语 cote、cotte → coat','衣服、外衣'],['覆盖层义及名词转动词；coat + -s → coats','多件外套、多层涂料；单数主语涂覆']],
 'winter coats 冬季外套；two coats of paint 两层漆；coats the surface 覆盖表面。',
 'coats hanging by the door；apply two coats。','two coats of paint 数两层涂刷形成的覆盖层。coats the metal with oil 中 coats 是动词，with 后接涂在上面的材料。',
 ('Their coats were hanging beside the entrance.','他们的外套挂在入口旁边。'),('The door needs two coats of paint.','这扇门需要刷两层漆。'),sources=['https://en.wiktionary.org/wiki/coats#English','https://en.wiktionary.org/wiki/coat#English'])
W('jackets','/ˈdʒækɪts/','夹克、短外套；外护套〔复数〕',
 '衣服外面的一件较短外套，是 jacket；包在书等物体外面的保护层，也借用这个外衣画面。',
 'jacket + -s，/t/ 后读 /s/。jacket 经法语 jaquet、jacquet 等衣物小称借入，基底 jaque 是一种衣服名称，较早来源有争议；不把它讲成确定的人名故事。',
 [['法语 jaque 及其小称 → jacket','衣服名称、小外衣 → 短外套'],['jacket + -s → jackets；外衣比喻扩展','多件夹克；书等物体的护套']],
 'leather jackets 皮夹克；rain jackets 防雨外套；book jackets 书的护封；life jackets 救生衣。',
 'jackets on the hooks；remove the book jackets。','jacket 常说较短的外套，coat 常用于较厚、较长的外衣，但实际分类会重叠。book jacket 是书外可取下的护封，别只按人体衣服理解。',
 ('They left their jackets on the backs of the chairs.','他们把夹克搭在了椅背上。'),('The designer created jackets for three new books.','这位设计师为三本新书设计了护封。'),sources=['https://en.wiktionary.org/wiki/jackets#English','https://en.wiktionary.org/wiki/jacket#English'])
W('hats','/hæts/','帽子；担任的角色〔复数、比喻〕',
 '戴在头上的一顶顶帽子，是 hats；换一顶帽子好像换一个身份，于是 wear many hats 可以说一个人身兼数职。',
 'hat + -s，/t/ 后读 /s/。hat 延续古英语 hætt 的帽子名称；表示身份、职责的用法由不同帽子标示不同角色的画面扩展。',
 [['古英语 hætt → hat','帽子'],['hat + -s → hats；身份比喻','多顶帽子；一个人承担的不同角色']],
 'sun hats 遮阳帽；wool hats 毛线帽；wear several hats 身兼数职；take off your hats 脱帽。',
 'hats on display；wears many hats at work。','wears many hats 常是在说职责范围：同一个人同时做几种工作。普通 hats 数帽子，角色义要靠 wear 等搭配与工作语境判断。',
 ('The children hung their hats beside the door.','孩子们把帽子挂在门旁。'),('In this small company, she wears many hats.','在这家小公司里，她身兼数职。'),sources=['https://en.wiktionary.org/wiki/hats#English','https://en.wiktionary.org/wiki/hat#English'])
W('bags','/bæɡz/','袋、包〔复数〕；装袋；抢先得到〔第三人称单数〕',
 '可以把东西拢在一起、提着走的袋或包，是 bags；由这个器物名，英语又有把东西装袋、把好东西拿到手的动词用法。',
 'bag + -s，/ɡ/ 后读 /z/。bag 来自中古英语 bagge，通常联系古诺尔斯语 baggi 的袋子词，更远来源未定；动词由名词发展。',
 [['古诺尔斯语 baggi 等 → 中古英语 bagge → bag','袋子、包'],['名词转动词；bag + -s → bags','多个包；单数主语装袋、拿到手']],
 'shopping bags 购物袋；school bags 书包；bags the groceries 把食品杂货装袋；bags a seat 抢先占到座位〔口语〕。',
 'bags at the checkout；carry the bags upstairs。','bags 可以指不同样式的包，具体看前面修饰词。bags a seat 的口语画面是先把位置拿到手；旅行时泛说行李常用不可数 luggage。',
 ('Could you help me carry these bags upstairs?','你能帮我把这些包提到楼上吗？'),('He bags the groceries while I pay.','我付款时，他把买的东西装进袋子。'),sources=['https://en.wiktionary.org/wiki/bags#English','https://en.wiktionary.org/wiki/bag#English'])
W('pockets','英 /ˈpɒkɪts/；美 /ˈpɑːkɪts/','口袋；局部的小片区域〔复数〕；放进口袋、收进自己手里〔第三人称单数〕',
 '缝在衣服上的小袋是 pockets；较大范围里面一小块集中存在的区域，也像藏在里面的小口袋。',
 'pocket + -s，/t/ 后读 /s/。pocket 经古法语或盎格鲁法语 poquet、poket 的小袋名称借入，接 poque、poke 袋子与小称词尾；现代口袋义又发展出放入口袋的动词。',
 [['法语袋子词 + 小称 → poquet、poket → pocket','小袋 → 衣服口袋'],['pocket + -s → pockets；空间及动词扩展','多个口袋、小片区域；单数主语收进口袋']],
 'coat pockets 外套口袋；empty your pockets 掏空口袋；pockets of fog 局部雾区；pockets the change 把找零装进口袋。',
 'deep pockets；pockets of warm air。','deep pockets 字面可说口袋深，比喻常说财力雄厚。pockets of something 强调局部分散地存在，像大范围里藏着几小块。',
 ('She checked all her pockets for the key.','她把所有口袋都找了一遍，想找到钥匙。'),('Pockets of fog remained in the valley.','山谷里局部地方仍有雾。'),sources=['https://en.wiktionary.org/wiki/pockets#English','https://en.wiktionary.org/wiki/pocket#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yh',ROOTS,WORDS)
 extend_lessons()
