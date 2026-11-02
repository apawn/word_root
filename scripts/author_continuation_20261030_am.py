"""Sweet and wild: familiar meanings, old forms and useful extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
SW=[['古英语 swēte → 中古英语 swete → sweet','甜；感官愉悦、令人喜爱等义也很早'],['现代 sweet','味甜、声香悦人、待人贴心；也作赞叹']]
def S(f,m):return SW+[[f,m]]
W('sweet','/swiːt/','甜的；芳香、悦耳的；贴心的；糖果〔英式常用复数〕',
 '先想到入口的甜，再想到让鼻子、耳朵、心里舒服的感觉：声音好听、举动贴心，都能说 sweet。',
 '继承古英语 swēte。古英语已经有味觉之外的愉悦、亲切等义，所以这是一组很老的联系，不必编成英语里某天才从糖变成好人。',SW,
 'sweet tea 甜茶，a sweet voice 悦耳嗓音，That’s sweet of you. 你真贴心。Sweet! 口语中也可赞叹太棒了。',
 'sweet tea；a sweet voice；sweet of you；a bag of sweets。',
 'sweet 甜、贴心；suite 套房、组曲常与它同音，但来源不同。sweets 在英式英语常指糖果。',
 ('The tea is a little too sweet for me.','这茶对我来说有点太甜了。'),('It was sweet of you to remember my birthday.','你还记得我的生日，真贴心。'),sources=['https://www.etymonline.com/word/sweet','https://en.wiktionary.org/wiki/sweet#English'])
W('sweeten','/ˈswiːtən/','使变甜；让条件更诱人；使更愉快',
 '杯里加糖是让味道更甜；谈条件时再添点好处，就是让对方更愿意接受。',
 'sweet + -en，使成为某种状态。字面加甜和改善条件都围绕 sweet 的愉悦、好接受的含义。',S('sweet + -en → sweeten','使变甜 → 增添吸引力、改善条件'),
 'sweeten the tea 给茶加甜，sweeten the deal 给交易加码、改善条件；不必然暗示非法好处。',
 'sweeten the tea；sweeten the deal；sweeten the offer。',
 'sweet 状态甜，sweeten 让它变甜；sweeten the deal 重点是条件更好，并非每笔交易都和食物有关。',
 ('She sweetened her tea with honey.','她往茶里加蜂蜜调甜。'),('The company sweetened the deal by offering free delivery.','公司提供免费送货，让交易条件更诱人。'))
W('sweetness','/ˈswiːtnəs/','甜味、甜度；温柔亲切',
 '把甜这个特点单独拿出来说：可以尝得到，也可以从人的语气和举动里感觉到。',
 'sweet + -ness，古英语已有 swētnes 等对应形式。后缀把性质变成名词，不是某一种甜食的名称。',S('古英语 swētnes → sweetness','甜的性质；令人愉悦、温柔亲切'),
 'the sweetness of the fruit 水果的甜味，a touch of sweetness 一点甜味，the sweetness of her voice 嗓音的柔美。',
 'the sweetness of；a touch of sweetness；natural sweetness。',
 'sweetness 甜味或亲切这个性质，sweets 常是糖果这些东西；两个名词不能照词尾机械互换。',
 ('The fruit has a gentle natural sweetness.','这种水果自带柔和的甜味。'),('There was a sweetness in the way he spoke to the child.','他对孩子说话时透着温柔。'))
W('sweetly','/ˈswiːtli/','悦耳地；温柔、亲切地',
 '笑容柔和、声音好听、说话温柔，都是一个动作带着 sweet 的感觉。',
 'sweet + -ly，接古英语 swētlīce 等同族副词。不是所有语境都指食物有多甜。',S('古英语 swētlīce → sweetly','以悦人、温柔的方式'),
 'smile sweetly 甜甜地笑，sing sweetly 唱得悦耳，speak sweetly 温柔地说话。',
 'smile sweetly；sing sweetly；speak sweetly。',
 'sweetly 修饰笑、唱、说等动作；sweetness 是性质名词。She smiled sweetly 不需要改成 smiled sweetness。',
 ('The child smiled sweetly at her grandfather.','孩子冲爷爷甜甜地笑了。'),('A bird was singing sweetly outside the window.','窗外有只鸟在婉转地唱。'))
W('sweetie','/ˈswiːti/','亲爱的；可爱、讨人喜欢的人；糖果〔英式〕',
 '把一个让你喜欢、疼爱的人叫作小甜心；常用于孩子、伴侣，也可夸一个人真好。',
 'sweet + 亲昵小称 -ie。这个词历史上也用于甜食、糖果；今日人称和食物义要靠语境分清。',S('sweet + -ie → sweetie','亲昵的小称；甜食或讨人喜爱的人'),
 'Hi, sweetie. 亲爱的，你好。She’s a sweetie. 她是个很可爱、很好的人。对不熟悉的人这样称呼可能显得过分亲昵。',
 'Hi, sweetie；be a sweetie；a bag of sweeties。',
 'sweetie 是亲昵称呼，不等于正式称赞一个人的专业能力；sweetheart 也是常见亲昵名词，可接着对照。',
 ('Come here, sweetie, and put your coat on.','亲爱的，过来把外套穿上。'),('He brought a small bag of sweeties for the children.','他给孩子们带了一小袋糖果。'))
W('bittersweet','英 /ˈbɪtəswiːt/；美 /ˈbɪtərswiːt/','苦甜交织的；喜忧参半的',
 '高兴是真的，舍不得、难过也是真的；两种感觉同时在，不是先苦完才轮到甜。',
 'bitter 苦 + sweet 甜，中古英语已有对应组合。混合味道的形象也用于情绪；植物名称等较少用义先略。',S('bitter + sweet → bittersweet','苦甜相混 → 喜悦与伤感同时存在'),
 'a bittersweet memory 苦乐交织的回忆，a bittersweet farewell 喜悦与不舍交织的告别。',
 'a bittersweet memory；a bittersweet farewell；a bittersweet ending。',
 'bittersweet 不是单纯 bitter 难受，也不是只剩 sweet 快乐；常见情境是毕业、离别、成功却失去某些东西。',
 ('Graduation was a bittersweet moment for the friends.','毕业对这群朋友来说是喜悦又不舍的时刻。'),('The film has a bittersweet ending.','影片的结尾让人又欣慰又伤感。'))
R('B2813','甜、悦人、贴心；味觉与情感共用的愉悦感','SWEET：入口甜，听着、闻着、相处着也舒服','sweet 的味觉、感官、待人三路先抓住；sweeten 是改变，sweetness 是性质，sweetly 是方式，sweetie 是亲昵称呼。',
 '古英语已有不止味甜的用法。用甜的感受帮助理解，别把学习联想写成未经证实的历史时间线。',
 'sweet + -en/-ness/-ly/-ie；bitter + sweet；sweet + heart。',
 [['基本感受与变化','sweet · sweeten · sweetness · sweetly'],['人和亲昵关系','sweetie · sweetheart'],['两种感受交织','bittersweet']],
 'sweet/suite 同音不同源；sweetness 性质、sweets 糖果；sweeten the deal 是改善条件；bittersweet 喜忧并存。',
 'The sweetie smiled sweetly, but the farewell still felt bittersweet.\n\n这个可爱的人甜甜地笑着，但告别仍让人喜忧交织。',
 'sweet sweeten sweetness sweetly sweetie sweetheart bittersweet')
WI=[['古英语 wilde → 中古英语 wilde → wild','未驯服、未耕种、天然生长的'],['现代 wild','野生、荒野的；失控、狂热；缺少根据的']]
def V(f,m):return WI+[[f,m]]
W('wild','/waɪld/','野生的；未驯服的；狂乱、热烈的；离谱、无根据的',
 '先抓住没被人驯服、管住的状态：动物在野外，天气猛烈，想法放得很开，都能接上。',
 '继承古英语 wilde。更远来源有争议，本文从可靠古英语节点讲起；不能把所有现代意思都说成危险。',WI,
 'wild animals 野生动物，wild flowers 野花，go wild 兴奋得不得了，a wild guess 没什么根据的猜测。',
 'wild animals；go wild；a wild guess；wild weather。',
 'wild 野生并不必然凶猛；a wild rabbit 也可温和。wild guess 缺少依据，educated guess 则根据已有信息推测。',
 ('We saw wild rabbits near the path.','我们在小路附近看到了野兔。'),('That number is just a wild guess.','那个数字只是随便猜的。'),sources=['https://www.etymonline.com/word/wild','https://en.wiktionary.org/wiki/wild#English'])
W('wildly','/ˈwaɪldli/','失控、狂乱地；极其；差异极大地',
 '动作像管不住一样大起大落；程度也可以放大到非常、极其。',
 'wild + -ly。既可描述激烈动作，也可加强程度，不能每次都硬译成野生地。',V('wild + -ly → wildly','狂乱地；程度极大或波动很大'),
 'wave wildly 拼命挥动，wildly successful 极其成功，estimates vary wildly 各估计差得很远。',
 'wave wildly；wildly successful；vary wildly。',
 'wildly /waɪldli/ 狂乱、极其；widely /waɪdli/ 广泛。widely known 广为人知不等于 wildly known。',
 ('He waved wildly to attract their attention.','他拼命挥手，想引起他们注意。'),('The app became wildly popular in a few months.','几个月内，这款应用就变得极其受欢迎。'))
W('wildness','/ˈwaɪldnəs/','野性；荒野气息；狂放、失控的性质',
 '说的是那股没被驯服、没被修整的劲儿，可以属于景色，也可以属于性情。',
 'wild + -ness，把 wild 的性质名词化。不是直接给一片荒野取地名。',V('wild + -ness → wildness','未驯服、天然或狂放的性质'),
 'the wildness of the landscape 景色的荒野气息，a sense of wildness 野性、天然感。',
 'the wildness of；a sense of wildness；preserve its wildness。',
 'wildness 说性质，wilderness 通常说大片荒野这个地方；They entered the wilderness 不能只换成 wildness。',
 ('The painting captures the wildness of the sea.','这幅画抓住了大海狂放不羁的气势。'),('She loved the wildness of the mountain landscape.','她喜欢山地景色未经雕琢的野趣。'))
W('wilderness','英 /ˈwɪldənəs/；美 /ˈwɪldərnəs/','荒野；大片未开垦自然地带；失势状态〔比喻〕',
 '走进去，人的道路、房屋渐渐没了，四周主要由自然占据；重点是一大片地方。',
 '中古英语 wildernes 等形式，历史上与古英语 wilddēor 野生动物及同族形式相关，末尾有 -ness；中间具体路径有不同分析。旧 dēor 泛指兽，不只今天的鹿，别硬造现代 -erness 后缀。',
 [['古英语 wilddēor 及同族形式','wild 野的 + dēor 兽、动物'],['中古英语 wildernes → wilderness','野兽出没、未经开垦的地方；中间构形有不同分析'],['现代 wilderness','大片荒野；比喻远离权力、影响的处境']],
 'a vast wilderness 广阔荒野，a wilderness area 荒野地区，years in the political wilderness 政治上失势的那些年。',
 'a vast wilderness；a wilderness area；the political wilderness。',
 'wilderness 荒野地方，wildness 野性、荒野感。这里的历史动物成分不要只理解为鹿生活的地方。',
 ('They spent a week exploring the wilderness.','他们花了一周探索荒野。'),('The party returned to power after years in the political wilderness.','这个政党在多年失势后重新执政。'))
W('wildflower','英 /ˈwaɪldˌflaʊə/；美 /ˈwaɪldˌflaʊər/','野花；自然生长的开花植物',
 '没人专门栽在花坛里，也自己在田边、草地开起来的花。',
 'wild 野生 + flower 花，直接按自然生长状态命名。名称本身不说明它是否稀有、是否受保护。',V('wild + flower → wildflower','自然生长的花、开花植物'),
 'a field of wildflowers 一片野花，a wildflower meadow 野花草地，wildflower seeds 野花种子。',
 'a field of wildflowers；a wildflower meadow；wildflower seeds。',
 'wildflower 野花，weed 杂草按人在某处是否想让它长来称呼；同一植物在不同地方可能得到不同称呼。',
 ('Wildflowers grew along the railway.','铁路沿线长着野花。'),('The meadow was covered with colourful wildflowers.','草地上开满了五颜六色的野花。'))
W('wildcat','/ˈwaɪldkæt/','野猫；未经正式授权、擅自发动的〔如罢工〕',
 '动物义很好懂；在行动里，wildcat 抓住的是没按既定组织和程序发动的劲头。',
 'wild + cat，中古英语已有野猫词。后来有冒险、投机等比喻支线，再用于未经正式工会授权等行动；不要把动物直接编成某次罢工的唯一故事。',V('wild + cat → wildcat','野猫；后有冒险、擅自行动等比喻'),
 'a wildcat species 一种野猫，a wildcat strike 未经正式工会授权的罢工。这个词本身不直接判定行动是否合法。',
 'a wildcat species；a wildcat strike；wildcat action。',
 'wildcat 可指自然野生猫类；feral cat 常指家猫后代或家猫在野外生活，二者并非每个场景都等同。',
 ('The camera recorded a wildcat moving through the forest.','摄像机拍到一只野猫穿过森林。'),('Workers staged a wildcat strike after the announcement.','公告发布后，工人发动了一场未经正式工会授权的罢工。'),sources=['https://www.etymonline.com/word/wildcat','https://en.wiktionary.org/wiki/wildcat#English'])
R('B3953','野生、未驯服；从自然状态到狂放和缺少约束','WILD：没人驯服、没人管住的状态','wild → wildly、wildness；wilderness 单讲地方和旧动物成分，wildflower、wildcat 再接用途。既有 wildlife、wildfire、wildcard 共享。',
 '先用野生、天然的画面理解，再按动作失控、程度极高等固定用法延伸；更远来源不强行确定。',
 'wild + -ly/-ness；wilderness 有旧 wilddēor 等历史；wild + flower/cat/life/fire/card。',
 [['性质、方式与地方','wild · wildly · wildness · wilderness'],['野生植物与动物','wildflower · wildcat · wildlife'],['火势与规则比喻','wildfire · wildcard']],
 'wildly 狂乱、极其与 widely 广泛分清；wildness 性质、wilderness 地方；wildcat strike 说明组织授权情况。',
 'Wildflowers filled the valley, preserving a sense of wildness.\n\n山谷开满野花，保留着一种天然野趣。',
 'wild wildly wildness wilderness wildflower wildcat wildlife wildfire wildcard')
if __name__=='__main__':save('continuation_20261030_am',ROOTS,WORDS)
