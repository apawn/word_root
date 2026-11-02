"""Skin: body covering, removed skins, materials and fixed cultural uses."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
SK=[['古诺尔斯语 skinn → 古、中古英语相关形式 → skin','动物皮；后来也通用于人体皮肤'],['现代 skin','皮肤、皮、表层；动词可剥皮或擦破皮']]
def S(f,m):return SK+[[f,m]]
W('skin','/skɪn/','皮肤；动物皮；外皮、表层；剥皮、擦破皮',
 '身体外面包着的一层；水果外皮、汤面薄膜、软件换外观，也能借外层的画面理解。',
 '接古诺尔斯语 skinn，经旧英语、中古英语形式进入今天的 skin。原先动物皮的联系很强，后来通用于人的皮肤；动词按动作可去皮、擦破。',SK,
 'dry skin 干燥皮肤，banana skin 香蕉皮，skin a tomato 给番茄去皮，skin your knee 擦破膝盖。',
 'dry skin；banana skin；skin a tomato；get under someone’s skin。',
 'skin 通常说外皮，flesh 说皮下肉质；hide 名词常说大型动物皮；动词 hide 是躲藏，两用法要分清，更远都与覆盖观念有关。',
 ('The cold air made my skin feel dry.','冷空气让我的皮肤觉得干。'),('She fell and skinned her knee.','她摔了一跤，擦破了膝盖。'),sources=['https://www.etymonline.com/word/skin','https://en.wiktionary.org/wiki/skin#English'])
W('skinny','/ˈskɪni/','很瘦的；紧身的〔服装〕；内幕消息〔the skinny〕',
 '人瘦得像只剩皮包着骨头；衣服则紧贴瘦窄轮廓。口语 the skinny 另指内情。',
 'skin + -y，中古英语已有像皮的同族形容词，瘦义可能联系 skin and bones。消息义的具体动机不完全确定，不把皮薄等联想冒充来源。',S('skin + -y → skinny','像皮、瘦；后有紧身服装及内情俚义'),
 'a skinny cat 很瘦的猫，skinny jeans 紧身牛仔裤，give me the skinny 告诉我内情。称人 skinny 有时带嫌太瘦的评价。',
 'skinny jeans；a skinny cat；the skinny on。',
 'slim 常赞身形苗条，skinny 更容易说太瘦；thin 较宽泛。the skinny 是固定俚语，不是那层皮本身。',
 ('The kitten looked skinny when we first found it.','刚发现那只小猫时，它瘦瘦的。'),('She wore skinny jeans and a loose jacket.','她穿着紧身牛仔裤和宽松夹克。'))
W('skinned','/skɪnd/','去皮的；擦破皮的；有某种皮肤的〔组合中〕',
 '厨房里是皮被剥掉了，摔跤后是皮擦破了；组合形容词里也可说有怎样的皮肤。',
 '两种结构要分开：动词 skin + -ed 是去皮、擦皮的分词；名词 skin + -ed 可表示有某种皮肤，常带前面的修饰成分。',SK+[['skin〔动词〕+ -ed','被去皮、擦破皮'],['skin〔名词〕+ -ed〔有……的〕','组合中描述所具有的皮肤性质']],
 'skinned tomatoes 去皮番茄，a skinned knee 擦破皮的膝盖；描述肤色、皮肤厚薄时常在组合形容词中出现。',
 'skinned tomatoes；a skinned knee；peeled and skinned ingredients。',
 'skinned 可能已去皮，skinless 直接说无皮；带皮性质的 -skinned 组合又是另一构词结构。',
 ('Add the skinned tomatoes to the pan.','把去皮番茄放进锅里。'),('He showed me his skinned knee after the fall.','摔倒后，他给我看擦破皮的膝盖。'))
W('skinless','/ˈskɪnləs/','无皮的；去皮的',
 '说食材上没有外皮，购买或处理后的状态就能直接这样描述。',
 'skin + -less，中古英语已有相应组合。后缀表示没有，不解释到底是天生没有还是后来去掉，靠对象和语境。',S('skin + -less → skinless','没有皮、去掉皮的'),
 'skinless chicken 去皮鸡肉，skinless fillets 去皮鱼片。',
 'skinless chicken；skinless fillets；boneless and skinless。',
 'skinless 无皮，boneless 无骨；boneless meat 不自动意味着皮也去了。',
 ('The recipe uses skinless chicken breasts.','这道菜用去皮鸡胸肉。'),('She bought two skinless fish fillets.','她买了两片去皮鱼柳。'))
W('skintight','/ˈskɪntaɪt/','紧贴身体的；紧身的',
 '衣服像另一层皮一样贴着身体，几乎没留宽松空间。',
 'skin + tight 紧的，组合说明紧到贴皮的程度。不表示衣服材质真是皮革。',S('skin + tight → skintight','紧到贴合皮肤、身体轮廓'),
 'a skintight suit 紧身衣，skintight leggings 紧身打底裤。',
 'a skintight suit；skintight leggings；skintight clothing。',
 'skintight 说贴身程度，skinny 服装常说窄瘦剪裁；leather 说皮革材料，和是否贴身是不同维度。',
 ('The dancer wore a skintight costume.','舞者穿着紧身表演服。'),('The fabric stretches to give a skintight fit.','这种面料能伸展，穿上后紧贴身体。'))
W('foreskin','英 /ˈfɔːskɪn/；美 /ˈfɔːrskɪn/','包皮〔通常指覆盖阴茎头的皮褶〕',
 '身体部位名称：覆盖在阴茎头外面、能够活动的皮肤褶层。',
 'fore- 前部 + skin 皮肤，英语身体部位词，与拉丁对应名称有仿译联系。不要照字面误认为额头皮肤。',S('fore- + skin → foreskin','位于前端的覆盖皮褶 → 固定解剖名称'),
 'the foreskin 包皮，the inner foreskin 包皮内侧。先认识身体部位词，具体医学问题另看专业语境。',
 'the foreskin；the inner foreskin；a description of the foreskin。',
 'foreskin 是固定部位，forehead 才是额头；两个 fore- 都与前有关，但不能据此互换。',
 ('The diagram labels the foreskin and the other structures.','示意图标出了包皮及其他结构。'),('The textbook describes the foreskin as a fold of skin.','教材把包皮描述为一层皮肤褶。'))
W('sheepskin','/ˈʃiːpskɪn/','绵羊皮、羊皮毛',
 '羊的皮作为材料，常连着羊毛，用于外套、地垫、衬里等。',
 'sheep 绵羊 + skin。按动物来源命名，不保证每件商品都保留毛，也不把所有山羊皮叫 sheepskin。',S('sheep + skin → sheepskin','绵羊皮及其制品材料'),
 'a sheepskin coat 羊皮毛外套，a sheepskin rug 羊皮毛地垫，sheepskin lining 羊皮毛衬里。',
 'a sheepskin coat；a sheepskin rug；sheepskin lining。',
 'sheepskin 特指绵羊皮，lambskin 更强调羔羊；wool 是羊毛，不是带皮整块材料的同义词。',
 ('A sheepskin rug lay beside the bed.','床边铺着一张羊皮毛地垫。'),('The boots have a warm sheepskin lining.','这双靴子有暖和的羊皮毛衬里。'))
W('lambskin','/ˈlæmskɪn/','羔羊皮；羔羊皮革',
 '用小羊皮做的柔软皮革；前部说明动物年龄、来源。',
 'lamb 羔羊 + skin。lamb 的 b 不发音，组合中通常也不额外读出 b。',S('lamb + skin → lambskin','羔羊皮、相应皮革材料'),
 'lambskin gloves 羔羊皮手套，a lambskin jacket 羔羊皮夹克。',
 'lambskin gloves；a lambskin jacket；soft lambskin。',
 'lambskin 羔羊皮，calfskin 小牛皮；同属按动物来源命名的皮料，不能只见 soft 就混为一类。',
 ('The gloves are made from soft lambskin.','手套由柔软的羔羊皮制成。'),('She tried on a black lambskin jacket.','她试穿了一件黑色羔羊皮夹克。'))
W('calfskin','英 /ˈkɑːfskɪn/；美 /ˈkæfskɪn/','小牛皮；小牛皮革',
 '做皮鞋、手袋、装帧等的小牛皮料；不是人的小腿皮肤这个普通组合。',
 'calf 小牛 + skin。calf 另有小腿义，但这个固定材料词通常接小牛；l 在常见读音中不发音。',S('calf〔小牛〕+ skin → calfskin','小牛皮及相应皮革'),
 'calfskin shoes 小牛皮鞋，a calfskin bag 小牛皮包，calfskin binding 小牛皮装帧。',
 'calfskin shoes；a calfskin bag；calfskin binding。',
 'calfskin 材料名取小牛义，calf muscle 小腿肌肉取另一义；词基多义要靠整个组合判断。',
 ('The book has a dark calfskin binding.','这本书用深色小牛皮装帧。'),('The label says the shoes are made of calfskin.','标签上说这双鞋由小牛皮制成。'))
W('snakeskin','/ˈsneɪkskɪn/','蛇皮；蛇皮纹材料',
 '蛇身上的那层皮，也可借称带蛇皮花纹的材料或外观。',
 'snake 蛇 + skin，按动物来源和外观命名。商品里蛇皮纹未必表示天然蛇皮，要看材质说明。',S('snake + skin → snakeskin','蛇皮；借指蛇皮纹理、材料外观'),
 'a snakeskin pattern 蛇皮纹，snakeskin boots 蛇皮或蛇皮纹靴，shed snakeskin 蛇蜕皮。',
 'a snakeskin pattern；snakeskin boots；shed snakeskin。',
 'snakeskin 可能实际蛇皮或纹理描述；snakeskin pattern 只明确花纹，不由名称保证天然皮料。',
 ('The bag has a snakeskin pattern.','这个包有蛇皮纹。'),('We found a dry piece of snakeskin near the wall.','我们在墙边发现了一块干蛇蜕皮。'))
W('skinhead','/ˈskɪnhed/','剃光、剃极短头发的人；光头族成员',
 '头发剃得露出头皮，是名字最直观的来源；还可以是特定青年亚文化的称呼。',
 'skin + head，借露头皮的外观命名。20世纪英国的亚文化名称后来也用于不同群体，不能把所有 skinheads 一概等同某个政治派别。',S('skin + head → skinhead','头皮外露的短发、剃发外观 → 人及亚文化名称'),
 'a skinhead in the photograph 照片里的光头青年，skinhead culture 光头族文化。应按具体年代、地区、团体理解。',
 'skinhead culture；a skinhead in the photograph；the history of skinheads。',
 'bald 可因自然脱发或剃发而无发，skinhead 常含剃发造型或亚文化信息；不是所有 bald men 都是 skinheads。',
 ('The documentary explores the history of skinhead culture.','纪录片探讨光头族文化的历史。'),('The photograph shows a skinhead wearing heavy boots.','照片上一个剃极短头发的青年穿着厚重靴子。'),sources=['https://www.etymonline.com/word/skinhead','https://en.wiktionary.org/wiki/skinhead#English'])
R('B3347','身体外层与皮料；去皮、无皮和紧身分开','SKIN：包在外面的皮；动词有时把它去掉或擦破','skin → skinny、skinned、skinless；skintight 贴身；foreskin 固定部位；几种常见皮料按动物一起读，skincare、bearskin 共享。',
 '外层画面很稳定，但动词去皮和名词有皮的 -ed 结构不能混。极冷门皮料、职业词先略；历史贬称不在本页扩展。',
 'skin + -y/-ed/-less；skin + tight/head；fore- + skin；sheep/lamb/calf/snake/bear + skin；skin + care。',
 [['基本皮肤和处理','skin · skinny · skinned · skinless · skincare'],['贴身、部位与外观称呼','skintight · foreskin · skinhead'],['按来源命名的材料','sheepskin · lambskin · calfskin · snakeskin · bearskin']],
 'skinny 很瘦不等于 slim 的褒义；skinless 去皮、skinned 依结构分义；calfskin 小牛不是小腿；skinhead 不等于所有秃头。',
 'The shop sells calfskin shoes and gloves made from lambskin.\n\n店里出售小牛皮鞋和羔羊皮手套。',
 'skin skinny skinned skinless skincare skintight foreskin skinhead sheepskin lambskin calfskin snakeskin bearskin')
if __name__=='__main__':save('continuation_20261030_as',ROOTS,WORDS)
