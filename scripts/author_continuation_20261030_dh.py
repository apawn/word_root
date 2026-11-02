"""Moon: light, visible phases, precious stones and the changing honeymoon."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
M=[['古英语 mōna → 中古英语 mone → moon','月亮；与 month 的月周期词族相关'],['月亮的形象扩展','月光、月周期；其他行星的天然卫星']]
def MH(f,m):return M[:1]+[[f,m]]
W('moon','/muːn/','月亮；〔其他行星的〕天然卫星',
 '夜空里由缺到圆、再变缺的月亮，过去也帮人记时间；看到别的行星绕着类似的天然卫星，也借叫 moons。',
 '古英语 mōna 经中古英语 mone 继承而来，与 month 同属月亮、月周期的老词族；更远与计量的词根联系常被提出，不把现代 moon 拆成 mo + on。',M,
 'the moon 月亮，a full moon 满月，a crescent moon 弯月，Jupiter’s moons 木星的卫星，over the moon 非常高兴，once in a blue moon 极少。',
 'the moon；a full moon；over the moon；once in a blue moon。',
 'the moon 通常是地球的月亮，a moon 可以是某颗行星的天然卫星；moon 不等于所有人造 satellite 卫星。',
 ('The full moon rose above the trees.','满月升到了树梢上方。'),('She was over the moon about the good news.','听到好消息，她高兴极了。'))
W('moonlight','/ˈmuːnlaɪt/','月光；业余兼职〔动词〕',
 '夜里月光铺在路上、水上；作动词则常说已有一份主业，还在下班后另外干一份活。',
 'moon + light 光，名词中古英语已有对应组合。现代兼职动词与 moonlighter 下班后另做工作的人相接，借月下、夜间工作的形象，不保证所有兼职都在晚上。',
 MH('中古英语 moon 与 light 的对应组合 → moonlight；moonlighter → 兼职动词 moonlight','月光；后来借夜间另一份工作说兼职'),
 'in the moonlight 在月光下，moonlight on the water 水面月光，moonlight as a musician 业余兼做乐手，moonlight at another job 另外兼职。',
 'in the moonlight；moonlight on the water；moonlight as；moonlight at。',
 'moonlight 名词常不可数，moonbeam 可数一束；moonlight 兼职多暗示主业之外的工作，不等于所有 part-time job 兼职岗位。',
 ('The garden looked peaceful in the moonlight.','花园在月光下显得很宁静。'),('He works as a teacher and moonlights as a musician.','他的本职是教师，业余兼做乐手。'),
 sources=['https://en.wiktionary.org/wiki/moonlight#English','https://www.etymonline.com/word/moonlight'])
W('moonlit','/ˈmuːnlɪt/','月光照亮的',
 '不是有灯架在路边，而是月光落下来，照出小路、水面等景物。',
 'moon + lit，lit 是 light 照亮的过去分词；组合后表示被月光照着，不是 moon 自己的过去式。',MH('moon + lit〔light 的分词〕→ moonlit','被月光照亮的'),
 'a moonlit night 月夜，a moonlit path 月光照着的小路，a moonlit sea 月光下的海面。',
 'a moonlit night；a moonlit path；a moonlit sea。',
 'moonlit 被月光照亮，moonless 没有可见月亮；moonlit 不意味着亮得像白天。',
 ('They walked along a moonlit path.','他们沿着月光照亮的小路走。'),('The moonlit sea looked silver.','月光下的海面泛着银色。'))
W('moonless','/ˈmuːnləs/','没有月亮可见的、无月光的',
 '抬头没看到月亮，周围也没有月光照着。说眼前夜色，不是在宣布地球失去了月球。',
 'moon + -less 没有，形成夜色、天空状态的形容词。',MH('moon + -less → moonless','无可见月亮、无月光的'),
 'a moonless night 无月之夜，a moonless sky 没有月亮可见的夜空，dark and moonless 漆黑无月的。',
 'a moonless night；a moonless sky；dark and moonless。',
 'moonless 说月亮或月光不可见，starless 说无星；没有月光的晴夜仍可以有许多星星。',
 ('They set out on a moonless night.','他们在一个无月之夜出发。'),('Stars filled the moonless sky.','没有月亮的夜空里布满了星星。'))
W('moonbeam','/ˈmuːnbiːm/','一束月光',
 '光从窗缝、树叶间斜斜落进来，好像一条淡亮的线；beam 指一束光。',
 'moon + beam 光束，合成可数的月光束。beam 也有梁的义项，在这里不说月亮上架木梁。',MH('moon + beam → moonbeam','一束从月亮方向照来的光'),
 'a moonbeam through the window 穿窗月光，pale moonbeams 淡淡的月光束，in a moonbeam 在一束月光里。',
 'a pale moonbeam；moonbeams through the window；in a moonbeam。',
 'moonbeam 可数、强调一束，moonlight 常不可数说月光整体；光束名不是一颗新的小月亮。',
 ('A moonbeam fell across the floor.','一束月光斜落在地板上。'),('Pale moonbeams shone through the branches.','淡淡的月光从树枝间照下来。'))
W('moonshine','/ˈmuːnʃaɪn/','月光〔较文学〕；私酿烈酒；空话、胡说〔较旧〕',
 '字面是月光；说酒时，接的是躲在夜色里秘密生产、运输的形象，不是酒里放进了月亮。',
 '中古英语已有 mone schyne 等，由 moon + shine。酒义与夜间隐蔽活动相连，早期也涉及走私酒，不强定只有美国山里酿酒的单一路线。空话义是另一比喻扩展。',
 MH('moon + shine → moonshine；后有酒与空话等比喻','月光 → 夜色掩护下的酒；虚浮无实之说'),
 'a jar of moonshine 一罐私酿烈酒，the history of moonshine 私酿酒史，in the moonshine 在月光里〔文学〕。现代酒义较常见。',
 'a jar of moonshine；the history of moonshine；in the moonshine。',
 'moonshine 酒义与 moonlight 月光、兼职义不互换；今天商品名可能借用旧私酒名称，名字本身不证明某瓶酒违法。',
 ('The museum displayed old equipment once used to make moonshine.','博物馆展出了过去用于酿私酒的旧设备。'),('The lake gleamed in the moonshine.','湖面在月光中闪亮。'),
 sources=['https://en.wiktionary.org/wiki/moonshine#English','https://www.etymonline.com/word/moonshine'])
W('moonstone','英 /ˈmuːnstəʊn/；美 /ˈmuːnstoʊn/','月光石〔宝石名〕',
 '转个角度，石面像有一层柔和光雾游动，让人联想到月光；不是通常所说从月球带回的岩石。',
 'moon + stone 石头，借柔和光泽命名宝石。常见月光石属于长石类；具体品种与商业名称可能有细分，不从名字认定化学成分只有一种。',MH('moon + stone → moonstone','让人联想到月光光泽的宝石'),
 'a moonstone ring 月光石戒指，a moonstone pendant 月光石吊坠，the sheen of moonstone 月光石的柔光。',
 'a moonstone ring；a moonstone pendant；the sheen of moonstone。',
 'moonstone 宝石俗名，moon rock 月球岩石；柔和光泽与月亮意象相关，不意味着石头本身像灯一样不断发光。',
 ('She wore a moonstone pendant.','她戴着一枚月光石吊坠。'),('The moonstone showed a soft glow as she turned it.','她转动那块月光石时，石面浮现出柔和的光泽。'),
 sources=['https://en.wiktionary.org/wiki/moonstone#English','https://www.gia.edu/moonstone-description'])
W('honeymoon','/ˈhʌnimuːn/','蜜月、蜜月旅行；关系初期的融洽时期',
 '新婚时甜甜的一段日子，后来也专指新婚旅行；新领导、新合作刚开始受到欢迎，也可借说蜜月期。',
 '早期 hony moone，由 honey 甜蜜 + moon 月、月周期。月可以联系一段时间，也有甜蜜像月相会变化的旧解释；不是确定来自新人连续喝一个月蜂蜜酒的故事。旅行义较后形成。',
 MH('honey + moon → hony moone → honeymoon','新婚甜蜜时期 → 蜜月旅行；更广的初期融洽'),
 'go on honeymoon 去度蜜月，a honeymoon period 蜜月期，honeymoon in Italy 在意大利度蜜月，the honeymoon is over 蜜月结束、最初融洽期过去。',
 'go on honeymoon；a honeymoon period；the honeymoon is over。',
 'honeymoon 最初可指时期，不必实际旅行；后来的比喻也不说明双方结婚。honey 和 moon 是并列材料，不是 honey 演变成 moon。',
 ('They went to Greece for their honeymoon.','他们去希腊度蜜月。'),('The new manager’s honeymoon period did not last long.','新经理上任后的蜜月期没有持续很久。'),
 sources=['https://en.wiktionary.org/wiki/honeymoon#English','https://www.etymonline.com/word/honeymoon'])
R('B2638','月亮、月光与月周期的比喻','MOON：夜空里周期变化的月亮，也给光、时间和情绪借形象','moon 为基础；moonlit、moonless 说夜色；moonbeam、moonshine、moonstone 说光或借光命名；moonrise 复用；honeymoon 接甜蜜时期。',
 '月光石不是月球岩石，私酒不是月亮的液体，蜜月先有时期再有旅行义。形象帮助记忆，但不编成每个词都已证实的传说。',
 '古英语 mōna → moon；moon + lit/-less/beam/shine/stone/rise；honey + moon → honeymoon。',
 [['基础与可见状态','moon · moonlight · moonlit · moonless'],['月光、升起与物品命名','moonbeam · moonshine · moonstone · moonrise'],['甜蜜时期比喻','honeymoon']],
 'moonbeam 一束、moonlight 整体；moonstone 非 moon rock；moonshine 现代常酒义；honeymoon 不一定旅行，蜜酒故事不作定论。',
 'On their honeymoon, they walked beside a moonlit lake.\n\n蜜月期间，他们在月光照亮的湖边散步。','moon moonlight moonlit moonless moonbeam moonshine moonstone moonrise honeymoon')
if __name__=='__main__':save('continuation_20261030_dh',ROOTS,WORDS)
