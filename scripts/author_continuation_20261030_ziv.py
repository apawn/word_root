"""Everyday tree names, fruits and the imitative cluck family."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3504':dict(words='cluck clucks clucked clucking'.split(),label='cluck → clucks、clucked、clucking：母鸡的咯咯声',note='与 hen 对照声音，不由 hen 派生。cluck 接古英语 cloccian，通常认为是拟声词；动词啼叫很古老，名词一声咯咯随动词形成，现代也比喻人发出关心、不赞同的咂舌声。'),
 'B2615':dict(words='elm elms fir firs spruce spruces'.split(),label='elm、fir、spruce：并排辨认的树名，各有来源',note='本支按树名比较，不由现代 tree 派生。elm 接古英语，fir 多认为经北欧语进入；spruce 则有普鲁士地名、进口木材的命名背景。三者不是彼此变形。'),
 'B3731':dict(words='birch birches'.split(),label='birch → birches：亮白树皮与桦树',note='birch 经古英语 beorc、berc，上溯亮、白的古老词族，有树皮颜色的背景；birches 在 /tʃ/ 后接 /ɪz/。'),
 'C0027':dict(words='acorn acorns'.split(),label='acorn：可能相关的田野果实旧词',note='acorn 接古英语 æcern，早期泛指林木果实，后来缩窄为橡实。常被认为与 acre、田野的古老词族有关，但不能当作现代 oak + corn 的直拼。'),
 'B3448':dict(words='holly hollies'.split(),label='holly：用叶缘刺来记的冬青名',note='与 leaf 比较叶片特征，不由 leaf 派生。holly 接古英语 holegn、holen 等，远源可能联系刺、扎；现代 y 是历史形式的一部分，复数 hollies 按规则改写。'),
 'C0317':dict(words='dandelion dandelions'.split(),label='dandelion → dandelions：狮子的牙齿',note='dandelion 接古法语 dent de lion 狮子的牙齿，背后有拉丁 dens leonis；锯齿状叶缘像牙齿，指的不是白色绒球。'),
 'B2557':dict(words='thistle thistles'.split(),label='thistle：蓟，带刺的草本植物',note='与 plant 比较植物种类，不由 plant 派生。thistle 经古英语 þistel，远源不确定，可能接刺、扎的古老材料；现代发音中 t 不单独读出。'),
 'B3136':dict(words='chestnut chestnuts hazelnut hazelnuts'.split(),label='chestnuts、hazelnuts：栗子与榛子的复数',note='chestnut 的前部是经法语、拉丁语传下的栗子旧名，后来又加 nut；hazelnut 则是古老的 hazel 榛树 + nut 果实复合，不能把 chestnut 前部当现代箱子 chest。'),
}
CLUCK=[['古英语 cloccian：发出母鸡叫声','通常认为是模仿咯咯声的拟声构词'],['英语 cluck 动词 → cluck 一声咯咯的名词','现代还能描述人咂舌、关切或不赞同的声音']]
ELM=[['古英语 elm ← 重建日耳曼语 *elmaz','与拉丁 ulmus 等有同族关系'],['elm 榆树 → elms','更远可能联系红、棕颜色的古老词根，但不是定论']]
FIR=[['现代 fir 通常认为经古诺斯语、古丹麦语的树名借入','古英语也有同族形式，不能把近代借词和所有祖先混成一条直线'],['更远重建的词族有橡树、树林等旧义 → 北方针叶树名称','现代 fir 常指冷杉，也见于范围不同的传统植物俗名']]
SPRUCE=[['普鲁士地名的中古英语形式 Spruce → 进口物产、木材名称','树名 spruce 与普鲁士木材贸易背景有关'],['进口皮革、服饰名称又与 spruce 整洁漂亮的形容词相连','spruce 动词打扮、收拾整齐来自形容词，常接 up']]
BIRCH=[['古英语 beorc、berc ← 重建日耳曼语 *berkjon','更远接亮、白的词族，命名通常联系浅色树皮'],['birch 桦树 → birches','现代名词在 /tʃ/ 后接复数 /ɪz/']]
ACORN=[['古英语 æcern：林木坚果、果实 → 中古英语 akorn 等','常被认为与 acre、田野的古老词族相关'],['泛称林木果实 → 主要指橡实；拼写受 oak、corn 联想影响','现代 acorn 不是实际由英语 oak + corn 直接拼出']]
HOLLY=[['古英语 holegn、holen → 中古英语 holin 等 → holly','更远可能联系刺、扎，与部分冬青刺状叶缘相应'],['holly 冬青 → hollies','现代词末 y 不单独拆作小称后缀；复数依拼写规则变化']]
THISTLE=[['古英语 þistel ← 重建日耳曼语 *thistilaz','更远来源不明，可能与刺、扎材料有关'],['中古英语 thistel → thistle → thistles','词名传承；现代 t 不单独发音']]
W('cluck','英、美 /klʌk/','〔母鸡〕咯咯叫；咂舌；咯咯声',
 '母鸡“咯、咯”地叫，英语用 cluck。人听见不赞同的事，发出咂舌声，也能借这个声音词来写。',
 '接古英语 cloccian，通常认为是拟声词；先有古老动词，后来也用 cluck 指一声叫声。这里靠声音形象理解，不靠硬拆字母。',CLUCK,
 'hens cluck 是母鸡咯咯叫；a soft cluck 是轻轻一声；cluck in disapproval 是不赞同地咂舌。',
 'hens cluck；a soft cluck；cluck in disapproval。',
 'cluck 常让人想到母鸡咯咯声，crow 常说公鸡打鸣；两个都是声音词，但声音、典型动物不同。',
 ('The hens began to cluck when she opened the gate.','她打开门时，母鸡开始咯咯叫。'),('He gave a little cluck of disapproval.','他轻轻咂了一下舌，表示不赞同。'),sources=S('cluck','cluck'))
W('clucks','英、美 /klʌks/','咯咯叫；咂舌；咯咯声〔复数〕',
 '一只母鸡在叫，可以说 the hen clucks；一阵里几声咯咯声，也能用名词 clucks。',
 'cluck + -s → clucks，/k/ 后读 /s/。可作第三人称单数动词，也可作声音名词复数。',CLUCK+[['cluck + -s → clucks','词尾 /ks/，区分声音名词与动作动词']],
 'the hen clucks 是母鸡叫；soft clucks 是轻柔的咯咯声；clucks her tongue 是咂舌。',
 'the hen clucks；soft clucks；clucks her tongue。',
 'clucks 带短促的声音感；crows 通常是另一类拉长、响亮的啼叫，不直接替换。',
 ('The hen clucks softly beside her chicks.','母鸡在小鸡旁边轻轻咯咯叫。'),('Soft clucks came from the chicken house.','鸡舍里传出轻轻的咯咯声。'),sources=S('clucks','cluck'))
W('clucked','英、美 /klʌkt/','咯咯叫了；咂舌了',
 '听到一件不太赞成的事，人轻轻咂一下舌，可以写 clucked；母鸡刚才的叫声也用它。',
 'cluck + -ed → clucked，/k/ 后后缀读 /t/；保留原 ck，直接加完整的 -ed。',CLUCK+[['cluck + -ed → clucked','规则过去式、过去分词；末尾 /kt/']],
 'clucked softly 是轻轻叫；clucked her tongue 是咂了咂舌；clucked in disapproval 是咂舌表示不赞同。',
 'clucked softly；clucked her tongue；clucked in disapproval。',
 '人物描写中的 clucked 常是在写声音与态度，不是在把人直接叫作母鸡。',
 ('The hen clucked and led her chicks away.','母鸡咯咯叫着，领小鸡走开了。'),('She clucked her tongue at the muddy footprints.','看到泥脚印，她不赞同地咂了咂舌。'),sources=S('clucked','cluck'))
W('clucking','英、美 /ˈklʌkɪŋ/','咯咯叫；咂舌；关切地唠叨',
 '母鸡在身边一阵阵咯咯叫，是 clucking；描写人围着谁关切地念叨，也能借这种声音和姿态。',
 'cluck + -ing → clucking，直接接 -ing；既可作进行式中的分词，也可把叫声动作当名词来谈。',CLUCK+[['cluck + -ing → clucking','叫声的进行、动作名称，以及人物态度描写']],
 'hens clucking 是母鸡在叫；clucking in disapproval 是不赞同地咂舌；clucking over someone 可带围着关心、念叨的语气。',
 'hens clucking；clucking her tongue；clucking in disapproval。',
 '用来写人的 clucking 可能带作者一点调侃；描述普通关心，用 caring、asking after 等更中性。',
 ('We could hear the hens clucking outside.','我们能听见外面母鸡咯咯叫。'),('She was clucking her tongue at the mess.','看着一片狼藉，她正在咂舌。'),sources=S('clucking','cluck'))
W('elm','英、美 /elm/','榆树；榆木',
 '一棵伸展着大树冠的榆树，是 an elm。它是沿用很久的树名，不需要找现代英语里的小零件硬凑。',
 '古英语 elm 接古日耳曼语树名，与拉丁 ulmus 等有同族关系；更远可能联系红、棕颜色，但不能把猜测说成确定的命名故事。',ELM,
 'an old elm 是老榆树；elm wood 是榆木；an elm tree 把 tree 补出来也很自然。',
 'an elm tree；an old elm；elm wood。',
 'elm 是榆树，oak 是橡树，birch 是桦树；都可以修饰 wood，但指不同树种的木材。',
 ('An old elm shaded the village square.','一棵老榆树为村庄广场遮阴。'),('The bench was made of elm.','这张长凳是榆木做的。'),sources=S('elm','elm'))
W('elms','英、美 /elmz/','榆树〔复数〕',
 '路两边是一排排榆树，就可以说 rows of elms。末尾的 l、m 都留在发音里。',
 'elm + -s → elms，/m/ 后读 /z/，结尾是 /lmz/；直接加 s。',ELM+[['elm + -s → elms','多棵榆树，读 /elmz/']],
 'a row of elms 是一排榆树；tall elms 是高大的榆树；old elms 是老榆树。',
 'a row of elms；tall elms；old elms。',
 'elm wood 说木材时常按材料不可数；elms 是把树一棵棵来数。',
 ('Tall elms lined the road.','高大的榆树排列在道路两旁。'),('The park has several old elms.','公园里有几棵老榆树。'),sources=S('elms','elm'))
W('birches','英 /ˈbɜːtʃɪz/；美 /ˈbɝtʃɪz/','桦树〔复数〕',
 '几棵细高、树皮浅亮的桦树，是 birches。亮白树皮也能帮你记住这个名字的古老来历。',
 'birch + -es → birches，/tʃ/ 后读 /ɪz/；树名经古英语传下，更远接亮、白的古老词族。',BIRCH,
 'silver birches 常说白桦类树；young birches 是幼桦；a stand of birches 是一片桦树林。',
 'silver birches；young birches；a stand of birches。',
 '这里先学树名复数；birch 也有用桦条抽打的动词义，那是树枝被用作工具后产生的用法。',
 ('Silver birches grew beside the lake.','湖边长着白桦树。'),('We planted three young birches in the garden.','我们在花园里种了三棵小桦树。'),sources=S('birches','birch'))
W('fir','英 /fɜː/；美 /fɝ/','冷杉；冷杉木；某些针叶树的俗名',
 '针状叶、常绿的 fir，常见中文对应是冷杉。先认树，再留意传统植物名称不总按现代分类划分。',
 '现代词通常认为经古诺斯语、古丹麦语树名借入；更远的词族曾有橡树、树林等意义。不同地区树名转用，不能理解成某棵橡树真的变成了冷杉。',FIR,
 'a fir tree 是一棵冷杉；fir branches 是冷杉枝；fir wood 是冷杉木。',
 'a fir tree；fir branches；fir wood。',
 'fir、pine、spruce 通常分别说冷杉、松、云杉；传统俗名有交叉，具体树种还要看完整名称。fir 和 fur 毛皮同音。',
 ('A tall fir stood beside the cabin.','小屋旁立着一棵高大的冷杉。'),('We decorated the room with fir branches.','我们用冷杉枝装饰了房间。'),sources=S('fir','fir'))
W('firs','英 /fɜːz/；美 /fɝz/','冷杉〔复数〕',
 '山坡上一片常绿冷杉，便可以说 firs。复数的 s 接在原来长元音或卷舌元音之后。',
 'fir + -s → firs，后缀读 /z/；这里数树的棵数，树名的历史借词关系不变。',FIR+[['fir + -s → firs','多棵冷杉的规则复数']],
 'tall firs 是高大的冷杉；a row of firs 是一排冷杉；firs on the hillside 是山坡上的冷杉。',
 'tall firs；a row of firs；dark firs。',
 'firs 和 furs 发音相同；前者是树，后者可能是毛皮，靠句意区分。',
 ('Tall firs covered the hillside.','高大的冷杉覆盖了山坡。'),('The path winds between dark firs.','小路在深色的冷杉之间蜿蜒。'),sources=S('firs','fir'))
W('spruce','英、美 /spruːs/','云杉；整洁漂亮的；收拾、打扮整齐〔常接 up〕',
 'a spruce 是一棵云杉；spruce up a room 则是把房间收拾漂亮。它们背后都有旧时普鲁士物产名称的线索。',
 'Spruce 曾是普鲁士地名的英语形式，与进口木材相连，后来用于树名；整洁漂亮的形容词通常联系进口皮革、时兴服饰，动词再来自形容词。',SPRUCE,
 'a spruce tree 是云杉；look spruce 是看着整洁精神；spruce up the room 是把房间收拾漂亮。',
 'a spruce tree；look spruce；spruce up the house。',
 '“打扮整齐”不是先把房间变成云杉树；两支用法要回到物产名称、衣着的不同发展去理解。',
 ('A spruce grew at the edge of the wood.','树林边长着一棵云杉。'),('We need to spruce up the guest room.','我们得把客房收拾漂亮些。'),('He looked very spruce in his new jacket.','他穿着新夹克，看上去十分整洁精神。'),sources=S('spruce','spruce'))
W('spruces','英、美 /ˈspruːsɪz/','云杉〔复数〕；收拾、打扮整齐',
 '一排云杉是 spruces；she spruces up the room 则说她把房间收拾漂亮。看句中位置区分树名和动作。',
 'spruce + -s → spruces；原词末尾已有 e，只添 s。基础末音 /s/ 后后缀读 /ɪz/，不读成 /spruːsz/。',SPRUCE+[['spruce + -s → spruces','树名复数、动词第三人称单数，读 /ˈspruːsɪz/']],
 'blue spruces 是蓝云杉；tall spruces 是高云杉；spruces up the office 是收拾办公室。',
 'tall spruces；blue spruces；spruces up the room。',
 '拼写只加 s，读音却多一个音节；判断词尾读法要看 /s/，不能只看有没有写 -es。',
 ('Tall spruces sheltered the house from the wind.','高大的云杉为房子挡风。'),('She always spruces up the room before guests arrive.','客人来之前，她总会把房间收拾漂亮。'),sources=S('spruces','spruce'))
W('acorn','英 /ˈeɪkɔːn/；美 /ˈeɪkɔrn/','橡实、橡子',
 '橡树结出的带小帽子的果实，就是 an acorn。小帽子是记外形的画面，名字本身经历过更古老的变化。',
 '古英语 æcern 早期范围比今天大，可说林木坚果、果实；后来主要指橡实。常被认为与 acre、田野的古老词族有关，现代拼写又受 oak、corn 联想影响。',ACORN,
 'an acorn 是一颗橡实；an acorn cup 是橡实杯状的壳斗；an oak grown from an acorn 是由橡实长成的橡树。',
 'an acorn；an acorn cup；grow from an acorn。',
 'acorn 不是现代英语 a + corn 一粒玉米；它早在现代 corn 用法之前就是一个整体传下的词。',
 ('An acorn fell onto the path.','一颗橡实落在小路上。'),('The child planted an acorn in a pot.','孩子把一颗橡实种进了花盆。'),sources=S('acorn','acorn'))
W('acorns','英 /ˈeɪkɔːnz/；美 /ˈeɪkɔrnz/','橡实、橡子〔复数〕',
 '秋天橡树下的一颗颗小果实，是 acorns。用复数时，画面是许多颗，而不是木材。',
 'acorn + -s → acorns，/n/ 后读 /z/；直接加 s，整词的历史来源与单数相同。',ACORN+[['acorn + -s → acorns','多颗橡实的规则复数']],
 'collect acorns 是捡橡实；fallen acorns 是落下的橡实；a handful of acorns 是一把橡实。',
 'collect acorns；fallen acorns；a handful of acorns。',
 'oak 是树名，acorns 是它的果实；同一植物的部位、产物可以各有自己的词源。',
 ('The children collected acorns under the oak.','孩子们在橡树下捡橡实。'),('Squirrels carried acorns across the garden.','松鼠叼着橡实穿过花园。'),sources=S('acorns','acorn'))
W('holly','英 /ˈhɒli/；美 /ˈhɑli/','冬青；冬青枝叶',
 '圣诞装饰里常见的绿叶、红果冬青，是 holly。典型叶缘的小刺，也能帮你记住它可能的古老命名背景。',
 '经古英语 holegn、holen 等形式，后来缩短、变化成 holly；更远可能接刺、扎的词族。部分种类的带刺叶缘提供直观联想，现代不把所有冬青都只凭红果定义。',HOLLY,
 'a holly tree 是冬青树；holly leaves 是冬青叶；a sprig of holly 是一小枝冬青。',
 'holly leaves；holly berries；a sprig of holly。',
 'holly 是植物名，holy 是神圣的；一个常读 /ˈhɒli/、/ˈhɑli/，另一个读 /ˈhəʊli/、/ˈhoʊli/，元音不同。',
 ('A holly grew beside the front gate.','前门旁长着一株冬青。'),('She tucked a sprig of holly into the wreath.','她往花环里插了一小枝冬青。'),sources=S('holly','holly'))
W('hollies','英 /ˈhɒliz/；美 /ˈhɑliz/','冬青〔多株、多种的复数〕',
 '花园里几株冬青，或苗圃展示几种冬青，都能用 hollies。它是在数植株、种类。',
 'holly 词末辅音字母 l + y，变 y 为 i + -es → hollies；原 /i/ 保留，再接 /z/。',HOLLY+[['holly 变 y 为 i + -es → hollies','按植株、种类计数的复数']],
 'evergreen hollies 是常绿冬青；young hollies 是幼株冬青；several hollies 是几株或几种冬青。',
 'young hollies；evergreen hollies；several hollies。',
 'holly 作枝叶材料时常不可数；three hollies 通常数三株，不能直接当作三片叶子。',
 ('Several hollies grow along the fence.','栅栏旁长着几株冬青。'),('The nursery sells hollies in different sizes.','苗圃出售不同大小的冬青植株。'),sources=S('hollies','holly'))
W('dandelions','英、美 /ˈdændɪlaɪənz/','蒲公英〔复数〕',
 '草坪上的黄色花，后来变成白色绒球，是 dandelions。名字里的“狮子牙齿”，看的是叶缘的锯齿。',
 'dandelion 借古法语 dent de lion 狮子的牙齿，背后有拉丁 dens leonis；英语再加 -s → dandelions，词尾 /z/。',
 [['拉丁 dens leonis 狮子的牙齿 → 古法语 dent de lion','比的是叶缘像牙齿的形状'],['法语词组压缩、借入英语 dandelion → dandelions','加 -s 形成现代英语复数']],
 'yellow dandelions 是开黄花的蒲公英；dandelions in the lawn 是草坪里的蒲公英。',
 'yellow dandelions；dandelions in the lawn；pick dandelions。',
 '名称的牙齿指锯齿叶缘；白色绒球是另一个生长阶段，不能拿绒毛解释 dent 的牙齿义。',
 ('Yellow dandelions dotted the lawn.','草坪上点缀着黄色蒲公英花。'),('The children blew the seeds off the dandelions.','孩子们把蒲公英的种子吹散了。'),sources=S('dandelions','dandelion'))
W('thistle','英、美 /ˈθɪsəl/','蓟；带刺的蓟类植物',
 '带刺的茎叶、常见紫色花头，能帮你认 thistle。它也是苏格兰标志里常见的植物。',
 '古英语 þistel，接日耳曼语的古老植物名；更远不确定，可能联系刺、扎的材料。现代词里的 t 不单独读出，末尾读 /səl/。',THISTLE,
 'a purple thistle 是开紫花的蓟；a thistle flower 是蓟花；a thistle emblem 是蓟图案标志。',
 'a purple thistle；a thistle flower；a thistle emblem。',
 'thistle 是植物名；thorn 是刺，两者可以放在同一幅带刺的画面里记，却不是现代同一个词。',
 ('A purple thistle grew beside the path.','路边长着一株开紫花的蓟。'),('The badge shows a thistle surrounded by leaves.','徽章上画着一朵被叶子环绕的蓟花。'),sources=S('thistle','thistle'))
W('thistles','英、美 /ˈθɪsəlz/','蓟〔复数〕',
 '田边一丛丛带刺的蓟，可以说 thistles。别因为写着 t，就把中间多读一个 /t/。',
 'thistle + -s → thistles；原 /əl/ 后加 /z/，不另加 /ɪz/，写法只加 s。',THISTLE+[['thistle + -s → thistles','多株蓟，词尾 /əlz/']],
 'purple thistles 是开紫花的蓟；a patch of thistles 是一片蓟；thistles by the fence 是栅栏旁的蓟。',
 'purple thistles；a patch of thistles；remove thistles。',
 'thistles、nettles 都可能让人想到不好碰的植物；前者的典型画面是刺，后者常说接触后的刺痛感。',
 ('Thistles grew along the edge of the field.','田边长着蓟。'),('We cleared a patch of thistles beside the fence.','我们清理了栅栏旁的一片蓟。'),sources=S('thistles','thistle'))
W('chestnuts','英 /ˈtʃesnʌts/；美 /ˈtʃɛsnʌts/','栗子；栗树〔复数〕',
 '街边烤得热乎乎的一颗颗栗子，是 chestnuts；上下文谈树，也可以指多棵栗树。',
 'chestnut 的前部来自中古英语栗子旧名，向前接法语、拉丁 castanea、希腊 kastaneia，后来又补 nut；加 -s → chestnuts。常见读音中前部 t 不单独发音。',
 [['希腊 kastaneia → 拉丁 castanea → 法语与中古英语栗子旧名','更远来源有争议，不把相关地名故事当定论'],['旧栗子名称 + nut → chestnut → chestnuts','现代以 nut 为中心构复数，末尾 /ts/']],
 'roasted chestnuts 是烤栗子；a bag of chestnuts 是一袋栗子；old chestnuts 依上下文也能说老栗树，或借喻反复讲的老故事。',
 'roasted chestnuts；a bag of chestnuts；chestnuts in the park。',
 'chestnuts 不由现代 chest 箱子、胸部 + nuts 新造；horse chestnuts 是另一种完整俗名，不把名称重合当作食材相同。',
 ('We bought a bag of roasted chestnuts.','我们买了一袋烤栗子。'),('Old chestnuts shaded the park entrance.','老栗树为公园入口遮阴。'),sources=S('chestnuts','chestnut'))
W('hazelnuts','英、美 /ˈheɪzəlnʌts/','榛子〔复数〕',
 '巧克力里那些香脆的榛子，是 hazelnuts。这个名字拆开就很直接：榛树结的坚果。',
 'hazel 榛树 + nut 坚果 → hazelnut，古英语已有 hæselhnutu 这一复合；现代加 -s → hazelnuts，末尾 /ts/。',
 [['古英语 hæsel 榛树 + hnutu 坚果 → hæselhnutu','复合词历史很老，并非现代食品营销新造'],['英语 hazel + nut → hazelnut → hazelnuts','加复数 -s，按果实一颗颗计数']],
 'roasted hazelnuts 是烤榛子；chopped hazelnuts 是切碎的榛子；chocolate with hazelnuts 是含榛子的巧克力。',
 'roasted hazelnuts；chopped hazelnuts；a handful of hazelnuts。',
 'hazel 可说榛树，也有眼睛颜色用法；hazelnuts 通常直接说果实，不是把眼睛颜色当作一种坚果。',
 ('The chocolate contains whole hazelnuts.','这款巧克力含有整颗榛子。'),('She sprinkled chopped hazelnuts over the cake.','她把切碎的榛子撒在蛋糕上。'),sources=S('hazelnuts','hazelnut'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ziv',ROOTS,WORDS)
 extend_lessons()
