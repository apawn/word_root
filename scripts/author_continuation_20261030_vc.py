"""Daybreak, ruin, paired clothes, hammer names and chocolate."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2422':dict(words=['day','dawn','dawning'],label='dawn：天开始亮，想法也开始明白',note='dawn 接古英语成日、天亮词族，现代短动词经历了由较长动作名词缩短或逆构的历史；dawning 现代也可重新认 dawn + -ing。'),
 'A1760':dict(words=['ruin','ruined'],label='ruin 到 ruined：坍塌、毁坏与受损结果',note='ruin 来自拉丁 ruina 倒塌，经法语等材料发展，ruined 是规则 -ed 形式；情绪化夸张与真实建筑损毁按对象分清。'),
 'A1776':dict(words=['ruin','ruins','pants'],label='常用复数的分工：ruins 废墟与 pants 衣物',note='ruins 是 ruin 的复数并常指建筑遗迹；pants 是 pantaloons 的缩短，衣物义保留复数结构，一条用 a pair of pants。'),
 'C0756':dict(words=['mallet','maul','mall'],label='更早击碎、研磨材料中的锤与购物中心旧名',note='拉丁 malleus 锤与 molere 研磨有更远词族联系；mallet、maul 接锤、重击，mall 购物中心名则经古球槌游戏、林荫道之名辗转发展，不是现代从研磨直接造词。'),
 'A1699':dict(words=['chocolate','chocolaty'],label='chocolate 与 chocolaty：食物到味道性质',note='chocolate 经西班牙语借入，更早中美洲来源有不同细节分析；chocolaty 是现代 -y 性质词，也有 chocolatey 拼写。'),
}
W('dawn','英 /dɔːn/；美 /dɔːn/ 或 /dɑːn/','黎明；开端；天亮；逐渐明白〔dawn on〕',
 '黑夜不是一下变成白昼，而是先透出第一点光。想法在头脑中慢慢亮起来，也能说 dawn on someone。',
 '接古英语 dagian 成为白天、天亮及 dagung 等动作名词，和 day 同族；中古英语较短动词由较长形式缩短或逆构，后又有现代名词黎明。抽象开端、逐渐明白义后来发展。',
 [['古英语日、天亮词族 → 中古英语较短形式','日子开始；天开始亮'],['英语 dawn 的名词、抽象扩展','黎明；新事物开端；想法逐渐明白']],
 'at dawn 黎明时；the dawn of a new era 新时代的开端；It dawned on me that ... 我逐渐明白……；the day dawned 天亮了。',
 'before dawn；dawn on someone。','dawn on 的主语常是想法、事实或 it：It dawned on me ...；不能按中文我明白了直接把我放到 I dawned ... 的主语位置。',
 ('We left the house at dawn.','我们在黎明时离开了家。'),('It slowly dawned on me that I had the wrong address.','我慢慢才意识到，自己拿错了地址。'),sources=['https://www.etymonline.com/word/dawn','https://en.wiktionary.org/wiki/dawn#English'])
W('dawning','英 /ˈdɔːnɪŋ/；美 /ˈdɔːnɪŋ/ 或 /ˈdɑːnɪŋ/','开始出现的；逐渐形成的领悟；黎明、开端',
 '眼前还没完全亮，但已经能看出一点轮廓。a dawning realization 是一个认识正慢慢浮现。',
 '现代可认 dawn + -ing。历史上相关较长天亮名词早于现代短名词 dawn，不能只按今天短词再加后缀的外形重写全部先后。',
 [['较早天亮动作名词与 dawn 的缩短历史','天开始亮；较长、较短形式的交错发展'],['现代 dawning 的常用分词、名词用法','正在开始；领悟刚形成；开端']],
 'a dawning realization 逐渐浮现的认识；dawning awareness 渐渐形成的意识；the dawning of a new age 新时代的开端。',
 'a dawning understanding；a dawning suspicion。','dawning 常强调刚开始出现，不表示已经全部明白。a dawning suspicion 是渐起的怀疑，complete understanding 才是充分理解。',
 ('A dawning realization made her stop talking.','一个逐渐浮现的认识让她停下了话头。'),('The exhibition explores the dawning of the industrial age.','展览探讨工业时代的开端。'),sources=['https://www.etymonline.com/word/dawn','https://en.wiktionary.org/wiki/dawning#English'])
W('ruin','/ˈruːɪn/','毁坏、毁灭；使糟掉；衰败；废墟、残垣',
 '本来能用、能维持的东西塌了、坏到失去原样，是 ruin；雨没把野餐打碎，却能让原来的安排全泡汤。',
 '接拉丁 ruina 坍塌，来自 ruere 猛然倒下、坍塌，英语也受法语 ruine、ruiner 影响。实物倒塌再扩展到生活、计划、名誉等被严重破坏。',
 [['拉丁 ruere → ruina','猛烈倒下 → 坍塌、崩坏'],['英语 ruin，含法语相关词影响','废弃损毁状态；使事物失去价值、作用或原样']],
 'ruin a plan 毁掉计划；ruin a shirt 弄坏衣服；fall into ruin 日渐荒废；the ruins of a castle 城堡遗迹；financial ruin 经济上彻底垮掉。',
 'ruin the surprise；a ruined building。','ruin 通常比普通 damage 强，常说严重坏掉或安排全受影响；日常也可夸张：You ruined the surprise 是惊喜被提前揭破，不是真实物品一定损毁。',
 ('The rain ruined our picnic.','雨把我们的野餐全搅了。'),('The old house had fallen into ruin.','老房子已经荒废破败了。'),sources=['https://www.etymonline.com/word/ruin','https://en.wiktionary.org/wiki/ruin#English'])
W('ruined','/ˈruːɪnd/','毁坏的、破败的；搞砸了；ruin 的过去式、过去分词',
 '衣服再穿不成原样，城堡只剩断墙，或计划被完全打乱，都可说 ruined。它把注意力放在受到破坏后的结果。',
 'ruin + -ed，结尾读 /d/；继承倒塌、毁坏的词族。分词形容词常描述建筑受损或事物严重受破坏的状态。',
 [['ruin','严重破坏；使失去原有状态、作用'],['ruin + -ed → ruined','曾毁坏；处于受损、破败状态']],
 'a ruined castle 破败城堡；a ruined shirt 弄坏的衬衫；a ruined holiday 被毁掉的假期；financially ruined 经济上垮掉的。',
 'the ruined walls；the meal was ruined。','ruined 描述受损结果；ruins 常作名词说遗迹、废墟。a ruined castle 与 the ruins of a castle 都可以描述破败城堡，但句子结构不同。',
 ('We walked past the walls of a ruined castle.','我们走过一座破败城堡的城墙。'),('The shirt was ruined by a large ink stain.','一大块墨渍把衬衫毁了。'),sources=['https://www.etymonline.com/word/ruin','https://en.wiktionary.org/wiki/ruined#English'])
W('ruins','/ˈruːɪnz/','废墟、遗迹；ruin 的复数；另为动词第三人称单数',
 '建筑原来的整体不在了，留下断墙、石柱、地基等残余。看这些存留下来的部分，常用 the ruins。',
 'ruin + -s；建筑残余义在拉丁复数与英语历史中都可见。英语后来在考古、旅游语境里常用 ruins，不必表示刚刚发生灾难。',
 [['拉丁 ruina、ruinae 与英语 ruin','倒塌、破坏；残留部分'],['ruin + -s → ruins','常用复数遗迹、废墟；也可为动词形式']],
 'ancient ruins 古代遗迹；the ruins of a temple 寺庙遗迹；lie in ruins 成为废墟；explore the ruins 探访遗迹。',
 'the castle ruins；a town in ruins。','The ruins are ... 里 ruins 是复数名词；The stain ruins the shirt 里 ruins 是单数主语后的动词。不要只凭结尾 s 判断都是复数。',
 ('The path leads to the ruins of an old temple.','小路通向一座旧庙的遗迹。'),('Much of the town lay in ruins.','镇上的大片区域成了废墟。'),sources=['https://www.etymonline.com/word/ruin','https://en.wiktionary.org/wiki/ruins#English'])
W('pants','/pænts/','长裤〔尤其美式〕；内裤〔尤其英式〕；喘气〔另源动词形式〕',
 '美式说一条外穿长裤常用 pants，英式日常说 pants 却常在说内裤。同样穿在身上，地区用法会让画面完全变样。',
 '衣物义是 pantaloons 的缩短，较早联系意大利喜剧人物 Pantalone 及其服装名称。复数结构保留下来；动词 pant 喘气的第三人称 pants 是另一来源。',
 [['人物、服装名 Pantalone → pantaloons','人物穿着相关的裤装名称，式样后来变化'],['缩短 pants','裤子等衣物；另有喘气动词的同形形式']],
 'a pair of pants 一条裤子或一条内裤，依地区；put on your pants 穿上裤子；short pants 短裤，常见美式；The dog pants 狗喘气，另源动词。',
 'These pants are ...；a pair of pants is ...。','衣物义通常用复数结构，数一条用 a pair of pants。跨地区求清楚，trousers 通常更明确地说外穿长裤，underpants 明确说内裤。',
 ('These pants are too long for me.','这条裤子我穿太长了。'),('She bought two pairs of pants for work.','她买了两条上班穿的长裤。'),sources=['https://www.etymonline.com/word/pants','https://en.wiktionary.org/wiki/pants#English'])
W('mallet','/ˈmælɪt/','木槌、橡胶槌等槌状工具',
 '拿一把头部较大的槌敲击，让力量落到表面，mallet 常是木头、橡胶等材料的槌。工具名称抓住击打这一点。',
 '经法语 maillet 小槌，接 mail 与小称材料，更早拉丁 malleus 锤。malleus 与 molere 研磨有更远的击碎、研磨词族联系，不来自英语 bad 的 mal-。',
 [['拉丁 malleus → 法语 mail／maillet','锤 → 小槌、小称工具名'],['英语 mallet','木槌、橡胶槌等；某些运动用槌']],
 'a wooden mallet 木槌；a rubber mallet 橡胶槌；a croquet mallet 槌球用槌；tap with a mallet 用槌轻敲。',
 'a mallet head；a small mallet。','mallet 常与一般 metal hammer 区分工具头的材料、形状、用途，但不是每把 mallet 都木制。maillet 中的小称历史也不规定现代实物必须很小。',
 ('He used a rubber mallet to fit the parts together.','他用橡胶槌把零件装合。'),('The players carried their croquet mallets onto the lawn.','球员拿着槌球球槌走上草坪。'),sources=['https://www.etymonline.com/word/mallet','https://en.wiktionary.org/wiki/mallet#English'])
W('maul','英 /mɔːl/；美 /mɔːl/ 或 /mɑːl/','撕咬重伤、粗暴伤害；狠狠批评；重槌',
 '老意思是拿重槌击打，后来重点转成受了严重、粗暴的伤害。动物把人咬伤、抓伤，或评论者猛烈抨击，都可见 maul。',
 '名词经法语锤相关形式接拉丁 malleus；动词由重击发展到严重伤害、粗暴对待。与 mallet 同族，但现代 maul 作动词不要求手里真有一把槌。',
 [['拉丁 malleus → 法语／英语重槌词','重槌；用重物击打'],['英语 maul 动词的扩展','严重伤害、粗暴对待；严厉批评']],
 'be mauled by an animal 被动物严重咬伤、抓伤；be mauled by critics 遭评论者猛烈抨击；a heavy maul 重槌。',
 'a dog mauling；a film mauled by reviewers。','maul 通常比 touch、scratch 强得多，强调严重或粗暴伤害。新闻写 mauled 不宜轻轻译成被摸了一下；评论语境则是比喻猛烈批评。',
 ('The report described an incident in which a dog mauled a passer-by.','报告描述了一起狗严重咬伤路人的事件。'),('The film was mauled by several reviewers.','这部电影遭到几位评论者的猛烈抨击。'),sources=['https://www.etymonline.com/word/mallet','https://en.wiktionary.org/wiki/maul#English'])
W('mall','英 /mɔːl/；美 /mɔːl/ 或 /mɑːl/','大型购物中心；步行林荫道、宽阔步道〔部分用法〕',
 '今天常是人步行、两边有商店的一片购物空间。老名字却先指一条供球槌游戏使用、后来供人散步的道。',
 '现代步道义由伦敦 The Mall 的名称推广，较早那里与 pall-mall 球槌游戏相连。游戏名经法语、意大利语含球与槌的材料，槌接拉丁 malleus；再由步行空间发展出购物中心义。',
 [['旧球槌游戏名 → The Mall 步道名','以球槌游戏关联的场地、林荫步道'],['mall 步行空间 → shopping mall','供人步行的空间 → 集中商店的购物中心']],
 'a shopping mall 购物中心；meet at the mall 在购物中心见面；an outdoor mall 室外购物步行区；London’s The Mall 另有专名读法 /mæl/。',
 'a mall entrance；shops in the mall。','mall 在现代购物语境不是锤子；联系锤的意义要经过旧游戏名、场地名几步，不能把遥远词源直接当现代释义。shopping centre 与 shopping mall 常有重叠。',
 ('We met at the entrance to the mall.','我们在购物中心入口见了面。'),('The mall has a cinema as well as shops.','购物中心除了商店还有电影院。'),sources=['https://www.etymonline.com/word/mall','https://en.wiktionary.org/wiki/mall#English'])
W('chocolate','英 /ˈtʃɒklət/；美 /ˈtʃɑːklət/','巧克力；巧克力糖；巧克力饮品；巧克力色',
 '可可经过加工成一块巧克力，是材料、食品；数一颗小巧克力糖，是 a chocolate。它不只指货架上的一整板甜食。',
 '经西班牙语 chocolate 借入，较早联系中美洲语言中的可可饮品名称，通常联系纳瓦特尔语。更深拆分有不同分析，不把常见苦水故事当唯一确定解释。英语先有饮品义，再有固体食品、糖果、颜色等。',
 [['中美洲饮品名称 → 西班牙语 chocolate','可可相关饮品；更早构词细节有不同说法'],['英语 chocolate 的用途扩展','饮品 → 固体食品、单颗糖果、颜色']],
 'a bar of chocolate 一板巧克力；hot chocolate 热巧克力饮品；a box of chocolates 一盒巧克力糖；dark chocolate 黑巧克力；chocolate brown 巧克力棕。',
 'melt chocolate；a chocolate cake。','chocolate 当材料、食品统称常不可数；chocolates 可数时常是多颗巧克力糖。cocoa 常说可可粉、可可饮品，cacao 常接可可原料、植物等语境，具体商品命名可有重叠。',
 ('Melt the chocolate gently before adding it to the mixture.','把巧克力温和地融化后再加入混合物。'),('She gave us a box of chocolates.','她送给我们一盒巧克力糖。'),sources=['https://www.etymonline.com/word/chocolate','https://en.wiktionary.org/wiki/chocolate#English'])
W('chocolaty','英 /ˈtʃɒkləti/；美 /ˈtʃɑːkləti/','有巧克力味、香气、口感等性质的',
 '吃一口、闻一下，就让人想到浓浓巧克力，叫 chocolaty。它在描写感觉，不是只给原料单换一个词形。',
 'chocolate 去词末 e 加 -y，形成具有巧克力性质的形容词；也有保留 e 的 chocolatey 拼写。两者常表达同一种味道、香气等性质。',
 [['chocolate','巧克力材料、味道等'],['chocolate + -y → chocolaty／chocolatey','具有巧克力般的味道、香气等']],
 'a rich chocolaty flavour 浓郁巧克力味；a chocolaty aroma 巧克力般香气；chocolaty brownies 巧克力味浓的布朗尼。',
 'a deeply chocolaty cake；a chocolaty taste。','chocolate cake 是食品类别、配料关系的常见说法；chocolaty cake 更突出吃起来有浓巧克力感觉。感觉描述本身不能单独证明某种具体原料含量。',
 ('The cake has a rich, chocolaty flavour.','蛋糕有浓郁的巧克力味。'),('The coffee had a pleasantly chocolaty aroma.','咖啡带着宜人的巧克力般香气。'),sources=['https://www.etymonline.com/word/chocolate','https://en.wiktionary.org/wiki/chocolaty#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vc',ROOTS,WORDS)
 extend_lessons()
