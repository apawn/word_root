"""Fear and brown: simple bases before close extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
FE=[['古英语 fær；相关动词 færan','突然的危险、灾祸；使恐惧'],['中古及现代 fear','对危险的恐惧；害怕、担忧']]
def FH(f,m):return FE+[[f,m]]
W('fear','英 /fɪə/；美 /fɪr/','恐惧、害怕；担忧',
 '觉得坏事可能来、自己可能受伤，心里先紧起来；历史上的词先指突然袭来的危险。',
 '名词接古英语 fær 突发危险、灾祸，后来重心转到人的害怕感受；相关旧动词有使恐惧义，现代常用为感到害怕。',FE,
 'fear of heights 恐高，fear for someone’s safety 担心某人安全，I fear that 恐怕、担心。fear 可名词也可动词。',
 'fear of；fear for；fear that；for fear of。',
 'fear 较直接说害怕或担心，awe 敬畏常混有惊叹、敬意；感到 fear 不要求危险已证实存在。',
 ('She overcame her fear of speaking in public.','她克服了当众讲话的恐惧。'),('They feared that the road might be blocked.','他们担心道路可能堵住了。'),sources=['https://www.etymonline.com/word/fear','https://en.wiktionary.org/wiki/fear#English'])
W('feared','英 /fɪəd/；美 /fɪrd/','令人畏惧的；被担心的；fear 的过去式、分词',
 '重点常在别人怕它：一个让对手畏惧的人，或大家一直担心会来的坏结果。',
 'fear + -ed，保留中古英语对应词形。过去分词作形容词时常有被他人畏惧、担忧的方向。',FH('fear + -ed → feared','曾害怕；被别人畏惧或担心的'),
 'a feared opponent 令人畏惧的对手，the feared delay 一直担心的延误，feared by others 为别人所畏惧。',
 'a feared opponent；the feared outcome；be feared by。',
 'a feared player 常是别人怕他，a fearful player 常是他自己害怕；不能只看都含 fear 就译成胆小。',
 ('She became a feared opponent on the tennis court.','她成为网球场上令人畏惧的对手。'),('The feared delay never happened.','大家担心的延误没有发生。'))
W('fearful','英 /ˈfɪəfl/；美 /ˈfɪrfl/','害怕、担忧的；可怕的；很厉害的〔部分搭配〕',
 '人心里装满害怕，是 fearful；另一些搭配却说事情吓人、程度很大，需要看它修饰谁。',
 'fear + -ful，中古英语已有造成恐惧和满怀恐惧等义。-ful 不能保证所有词都只有装满这种感受一条解释。',FH('fear + -ful → fearful','满怀恐惧；令人恐惧；加强程度'),
 'fearful of failure 害怕失败，fearful that 担心，a fearful noise 可说非常吓人或很大的噪声。',
 'fearful of；fearful that；a fearful expression；a fearful noise。',
 'fearful 常描述害怕者，但保留可怕义；fearsome 更稳定地说引起畏惧。用补语 of/that 时方向通常更清楚。',
 ('The children were fearful of entering the dark room.','孩子们害怕进入黑屋。'),('There was a fearful crash as the tree fell.','树倒下时发出一声吓人的巨响。'))
W('fearless','英 /ˈfɪələs/；美 /ˈfɪrləs/','无畏的；大胆的',
 '危险或压力在面前，仍然不畏缩；也可能是在夸一个人的勇气。',
 'fear + -less，没有恐惧、表现无畏。通常评价行动或性格，不必字面证明这个人从来没有任何恐惧。',FH('fear + -less → fearless','不畏惧 → 无畏、大胆'),
 'a fearless reporter 无畏的记者，fearless criticism 大胆批评，a fearless approach 大胆做法。',
 'a fearless reporter；fearless criticism；a fearless approach。',
 'fearless 夸勇气，reckless 鲁莽批评不顾风险；两者都敢做，但评价重点不同。',
 ('She is known as a fearless investigative reporter.','她以无畏的调查记者形象闻名。'),('The performance showed a fearless approach to experimentation.','表演展现了大胆实验的态度。'))
W('fearsome','英 /ˈfɪəsəm/；美 /ˈfɪrsəm/','可怕的；令人畏惧的；实力骇人的',
 '看起来、听起来或实际强得让别人心里发怵，害怕感在别人那边。',
 'fear + -some，-some 在这里表示引起某感受、具有某性质。与 fearful 重合但用法着眼点不同。',FH('fear + -some → fearsome','引起畏惧 → 可怕、强得让人发怵'),
 'a fearsome beast 可怕野兽，a fearsome opponent 强大得令人畏惧的对手，a fearsome reputation 令人敬畏的名声。',
 'a fearsome beast；a fearsome opponent；a fearsome reputation。',
 'fearsome 描述引起害怕的对象，不通常表示这个对象自己胆小；也可带对实力的佩服。',
 ('The team faces a fearsome opponent in the final.','球队决赛将面对一个令人畏惧的强大对手。'),('The story describes a fearsome creature living in the cave.','故事描写了一只住在洞穴里的可怕生物。'))
R('B3102','危险、害怕与让别人畏惧','FEAR：先看谁怕谁；后缀改变感受方向','fear → feared、fearful、fearless、fearsome 紧挨着，用人和对手的关系辨别。',
 '旧名词先指突发危险，后来侧重恐惧感受。旧动词也有使恐惧义，所以不能把现代所有后缀词都只归成自己害怕。',
 'fear + -ed/-ful/-less/-some。',
 [['感受与被畏惧','fear · feared'],['害怕、无畏与引起畏惧','fearful · fearless · fearsome']],
 'feared 常别人怕它；fearful 常自己怕但也可吓人；fearless 无畏，fearsome 令别人畏惧。',
 'The fearless player faced a fearsome opponent without showing fear.\n\n无畏的选手面对强大对手，没有流露恐惧。',
 'fear feared fearful fearless fearsome')
BR=[['古英语 brūn → 中古英语 broun','深色、棕褐色'],['现代 brown','棕色；使食物表面变褐；按颜色命名甜点、石材']]
W('brown','/braʊn/','棕色、褐色的；使煎烤成褐色',
 '巧克力、树皮一类的棕褐色；烹饪里让食物表面上色，也用 brown。',
 '继承古英语 brūn，经中古英语 broun 延续。动词由颜色状态说明变成、使变成褐色。',BR,
 'brown eyes 棕色眼睛，brown sugar 红糖、棕色糖，brown the onions 把洋葱炒至上色。具体食品名称不只按字面颜色翻译。',
 'brown eyes；brown sugar；brown bread；brown the onions。',
 'brown the food 是让表面上色，不一定烤糊；burn 才直接说烧焦。brown bread 的具体配方还得看标签。',
 ('She has dark brown eyes.','她有深棕色眼睛。'),('Brown the onions before adding the tomatoes.','先把洋葱炒上色，再加番茄。'))
W('brownish','/ˈbraʊnɪʃ/','略带棕色的；偏褐色的',
 '不是纯粹认定棕色，而是看着有一点棕，或者颜色接近它。',
 'brown + -ish，-ish 表有点、近似。描述颜色时软化界线，不要求精确色值。',BR+[['brown + -ish → brownish','带一点棕褐色、近似棕色']],
 'a brownish stain 偏褐色污迹，brownish water 泛褐色的水，a brownish shade 偏棕色调。',
 'a brownish stain；brownish water；a brownish shade。',
 'brownish 接近棕色，dark brown 是深棕，两者不按同一标准分类；偏棕不保证深。',
 ('The leaves had turned a brownish colour.','叶子已变成偏褐色。'),('A brownish stain remained on the paper.','纸上留着一块偏褐色污迹。'))
W('brownie','/ˈbraʊni/','布朗尼巧克力点心；家务小精灵〔民间故事〕',
 '菜单上通常是颜色深褐、口感浓厚的小块巧克力点心；老故事里还有帮做家务的小精灵。',
 'brown + 小称 -ie。精灵义较早见于苏格兰民间用语，甜点义后来出现；不能把点心画成小精灵变出来的。',BR+[['brown + -ie → brownie','棕色小精灵旧称；另发展出褐色巧克力点心名']],
 'a chocolate brownie 巧克力布朗尼，a tray of brownies 一盘布朗尼。Brownie 大写在其他专名中另有用法。',
 'a chocolate brownie；a tray of brownies；bake brownies。',
 'brownie 点心与 brownish 偏棕色不是同一后缀；-ie 小称形成名词，-ish 描述相近性质。',
 ('She baked a tray of chocolate brownies.','她烤了一盘巧克力布朗尼。'),('Would you like a brownie with your coffee?','喝咖啡时要来块布朗尼吗？'),sources=['https://www.etymonline.com/word/brownie','https://en.wiktionary.org/wiki/brownie#English'])
W('brownstone','英 /ˈbraʊnstəʊn/；美 /ˈbraʊnstoʊn/','褐砂岩；褐砂岩外墙住宅',
 '先是一种褐色建筑石材，再把用这种石材做门脸的房子也这样叫。',
 'brown + stone 石头，先按颜色说材料；美式、尤其纽约住宅描写里，转指有这类外墙的排屋。',BR+[['brown + stone → brownstone','褐色砂岩 → 以这种石材饰面的住宅']],
 'a brownstone facade 褐砂岩立面，a Brooklyn brownstone 布鲁克林褐砂岩排屋。房子内部不必全由同一种石头构成。',
 'a brownstone facade；a row of brownstones；a Brooklyn brownstone。',
 'brownstone 可材料也可房屋；不是所有棕色房子都符合这种建筑用法。',
 ('They rented an apartment in an old brownstone.','他们在一栋老褐砂岩排屋里租了公寓。'),('The street is lined with brownstones.','街道两边排列着褐砂岩排屋。'))
R('B2420','棕褐色、近似色与按颜色命名','BROWN：颜色；BROWNISH：偏棕；BROWNIE：点心名','先 brown、brownish，再 brownie 与 brownstone；brownfield 的已开发地块义共享旧精讲。',
 '古英语深色词成为现代棕褐色名，动词说明上色。点心、石材住宅、开发地块各有固定命名历史。',
 'brown + -ish/-ie；brown + stone/field。',
 [['颜色与程度','brown · brownish'],['点心、石材与地块','brownie · brownstone · brownfield']],
 'brown 食物上色不一定烧焦；brownie 两个历史用法不画成前后变形；brownstone 不仅说颜色。',
 'They served brownies in the café beneath the brownstone apartments.\n\n褐砂岩公寓楼下的咖啡馆供应布朗尼点心。',
 'brown brownish brownie brownstone brownfield')
if __name__=='__main__':save('continuation_20261030_ac',ROOTS,WORDS)
