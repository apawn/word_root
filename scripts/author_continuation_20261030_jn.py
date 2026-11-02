"""Infection, wrap and size comparisons."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
I=[['拉丁 in- 向内 + facere 的相关形式 → inficere','浸入、染色；沾染、污染'],['拉丁 īnfectiō 经法语等 → infection','污染、感染；现代也借用于计算机感染']]
W('infection','/ɪnˈfekʃən/','感染；感染性疾病；计算机受感染的状态',
 '不是表面碰了一下，而是感染性因素进入宿主、建立相应过程。电脑被恶意程序侵入也借这个感染的画面。',
 '经古法语 infection、infeccion 等接晚期拉丁 īnfectiō、inficere。更早有浸染、沾染的意义；现代对应 infect + -ion，不是 in- 否定 + fiction 小说。',I,
 'a bacterial infection 细菌感染，prevent infection 预防感染，a computer infection 计算机感染。infection 可说过程，也能可数说一次、某种感染。',
 'a bacterial infection；prevent infection；a computer infection。',
 'infection 感染与 inflammation 炎症不同：前者说感染过程，后者说机体反应，不能只因中文相近便互换。',
 ('The textbook distinguishes bacterial and viral infections.','教材区分了细菌感染和病毒感染。'),('The scan found signs of infection on the computer.','扫描发现了电脑受感染的迹象。'))
W('disinfection','/ˌdɪsɪnˈfekʃən/','消毒',
 '不是说已经没有 infection 这个状态，而是说采取处理，破坏、去除许多致病微生物。它是过程名称。',
 '现代可对应 dis- 去除、反转 + infection，亦联系 disinfect 消毒的名词形式和法语相应命名。dis- 在这里引入去除污染、感染因素的处理关系。',I+[['dis-／disinfect 的相应名词 → disinfection','针对微生物污染的消毒过程']],
 'surface disinfection 表面消毒，cleaning and disinfection 清洁与消毒，a disinfection procedure 消毒程序。具体处理类别、效果由方法与条件决定。',
 'surface disinfection；cleaning and disinfection；a disinfection procedure。',
 'disinfection 不等于 sterilization 灭菌；消毒不保证杀灭所有微生物形态，如某些芽孢。cleaning 清洁也不自动与消毒同义。',
 ('The training explains the difference between cleaning and disinfection.','培训解释了清洁和消毒的区别。'),('The report describes the surface disinfection procedure.','报告描述了表面消毒程序。'),sources=['https://en.wiktionary.org/wiki/disinfection#English','https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/glossary.html'])
R('B4371','沾染、感染的历史联系，以及去除感染因素的处理名词','INFECTION：感染过程；DISINFECTION：消毒处理','infection → disinfection，后者不是单纯没有感染，而是处理过程。',
 '旧染色、污染的概念发展到感染。现代术语还需区分感染、炎症、清洁、消毒与灭菌，不能只靠一个前缀概括全部。',
 '拉丁 inficere、īnfectiō 经法语进入英语；现代与 infect + -ion 对应；dis- 连接去除、反转。',
 [['感染与消毒过程','infection · disinfection']],
 'infection 不等于 inflammation；disinfection 不等于 sterilization。',
 'The chapter discusses infection and explains the purpose of disinfection.\n\n这一章讨论感染，并说明消毒的目的。','infection disinfection')
W0=[['中古英语 wrappen、wrappe','包、折叠；更早来源未完全确定'],['现代 wrap','用材料包围；包裹物、食物卷；收尾与文本换行等扩展']]
W('wrap','/ræp/','包、裹；包装材料、披肩、食物卷；收尾；文本换行',
 '用一层柔软材料围住东西，是 wrap 的核心画面。食物被饼包起来成卷；工作全部收拢结束，又有 wrap up 收尾。',
 '中古英语 wrappen、wrappe 等已存在，远源有日耳曼语相关分析但未定。开头 w 在现代常用读音中不发音；不要与 rap 说唱混为一词。',W0,
 'wrap a gift 包礼物，wrap a scarf around your neck 把围巾绕在脖子上，a chicken wrap 鸡肉卷，wrap up a meeting 结束会议。word wrap 是排版中的自动换行。',
 'wrap a gift；wrap around；wrap up；word wrap。',
 'wrap 强调围包，pack 更广地说打包、装好。That’s a wrap! 常表示拍摄、工作完成，并不要求真出现包装纸。',
 ('She wrapped the gift in blue paper.','她用蓝纸包好了礼物。'),('Let’s wrap up the meeting in five minutes.','我们五分钟后结束会议吧。'))
W('wrapping','/ˈræpɪŋ/','包装材料；包裹的动作；文本换行',
 'wrapping paper 是包东西的纸，the wrapping 可以说外面的包装。电脑里的 text wrapping 则关注文字怎样折到下一行。',
 'wrap + -ing，双写 p；中古英语已有 wrappinge 等。既可说包的过程，又可命名包裹材料，另外继承文本 wrap 的排版义。',W0+[['wrap + -ing → wrapping','包装过程、材料；换行过程']],
 'wrapping paper 包装纸，remove the wrapping 拆掉包装，text wrapping 文本换行。wrapping 作材料总称常不可数，也可在具体语境说某层包装。',
 'wrapping paper；remove the wrapping；text wrapping。',
 'wrapping 不只是一种进行时。包装纸通常叫 wrapping paper，别把 paper 当成动作本身。',
 ('The children saved the colourful wrapping paper.','孩子们留下了彩色包装纸。'),('The editor supports automatic text wrapping.','这个编辑器支持文本自动换行。'))
W('wrapper','英 /ˈræpə/；美 /ˈræpər/','包装纸、外包层；包装者或包装器；软件封装层',
 '糖果外面那一层是 wrapper。软件里，在一个已有功能外面套一层较方便的接口，也借包一层这个画面。',
 'wrap + -er，双写 p；中古英语已有 wrappere。-er 可命名执行者、器具，也可指包在外面的材料；不是每次都指人。',W0+[['wrap + -er → wrapper','包装者、外包层；软件的接口封装层']],
 'a sweet wrapper 糖果包装纸，remove the wrapper 去掉外包装，a wrapper around a library 围绕程序库的封装层。技术用法不代表每个 wrapper 都增加同样程度的功能。',
 'a sweet wrapper；remove the wrapper；a software wrapper。',
 'wrapper 与 rapper 同音不同源；wrapping 常泛说材料或过程，a wrapper 更常指一件、一个包覆层。',
 ('He put the empty wrapper in the bin.','他把空包装纸扔进垃圾桶。'),('The module provides a simple wrapper around the existing library.','这个模块给现有程序库套了一层简单接口。'))
W('unwrap','/ʌnˈræp/','拆开包装；展开、去除包覆',
 '先前包起来，现在把外层打开，让里面的东西露出来，就是 unwrap。',
 'un- 反转动作 + wrap；中古英语已有 unwrappen。这里 un- 不是简单表示不包，而是把已经包好的状态解开。',W0+[['un- + wrap → unwrap','拆开、解除包覆']],
 'unwrap a present 拆礼物，unwrap the parcel 打开包裹。技术里也可借给解除某层封装、展开某种表示，具体对象要另看。',
 'unwrap a present；unwrap the parcel。',
 'unwrap 不必撕坏外层，tear 撕破强调材料分裂；unwrapped 有时是已经拆开，有时依语境是未包裹，需看整句。',
 ('The child carefully unwrapped the present.','孩子小心地拆开了礼物。'),('She unwrapped the sandwich before eating.','她吃三明治前先打开了包装。'))
W('wraparound','/ˈræpəraʊnd/','包裹式的、环绕式的；环绕覆盖物、围裹衣物',
 '不是只挡正面，而是往两侧或周围延伸，像包住一圈，这就是 wraparound。常见于墨镜、露台、衣服等设计。',
 'wrap + around，动作和方向组合后固定作形容词、名词。不同设计借同一环绕关系，不必真的每件都完整绕满一圈。',W0+[['wrap + around → wraparound','向侧面、周围延伸，围裹的设计']],
 'wraparound sunglasses 包覆式太阳镜，a wraparound porch 环绕式门廊，a wraparound skirt 围裹裙。',
 'wraparound sunglasses；a wraparound porch；a wraparound skirt。',
 'wrap around 分开常是动作短语，wraparound 连写常修饰设计或命名物件。不是所有 wraparound 都在说文本换行。',
 ('He wore wraparound sunglasses on the ride.','骑行时他戴着包覆式太阳镜。'),('The house has a wraparound porch.','这所房子有环绕式门廊。'))
R('B3904','围包、包裹材料，以及收尾、换行和软件封装等扩展','WRAP：用一层东西围住；扩展看收拢、换行或接口外层','wrap → wrapping、wrapper；unwrap 解开；wraparound 按环绕的设计命名。',
 '材料包围物件是最直观的起点。不同领域会借一部分关系形成固定用法，不必把每次 wrap 都翻成包装纸。',
 '中古英语 wrappen → wrap；w 不发音；-ing、-er 前双写 p，un- 反转动作，around 表方向。',
 [['动作、材料与包覆层','wrap · wrapping · wrapper'],['解开与环绕设计','unwrap · wraparound']],
 'wrapper 与 rapper 同音；wrap up 工作是收尾，word wrap 是文本换行。',
 'She unwrapped the gift and folded the wrapper for reuse.\n\n她拆开礼物，把外包装折好准备再用。','wrap wrapping wrapper unwrap wraparound')
S=[['size 尺寸 + -ed → sized','具有某种尺寸的'],['over-／under- + sized','大于或小于通常、预期、适合的尺寸']]
W('oversized','美 /ˌoʊvərˈsaɪzd/；英也常见 /ˈəʊvəsaɪzd/','过大的；特大号的；宽大版型的',
 '不是只说它大，而是比同类通常尺寸、某个用途需要的尺寸更大。衣服也可能故意做得宽松，这时不一定是买错号。',
 'over- 超过 + sized 有某种尺寸的。size 去末尾 e 加 -ed 成 sized，读 /saɪzd/，没有额外 /ɪd/。',S,
 'an oversized sweater 宽大毛衣，oversized luggage 超常规尺寸行李，an oversized logo 过大或醒目的标志。具体比较基准随对象而定。',
 'an oversized sweater；oversized luggage；an oversized logo。',
 'oversized 可能是设计风格，也可能是不合适；large 只说大，不必超出通常尺寸。词本身不保证褒贬。',
 ('She wore an oversized sweater with jeans.','她穿着宽大毛衣和牛仔裤。'),('The oversized box would not fit through the doorway.','箱子太大，过不了门口。'),sources=['https://en.wiktionary.org/wiki/oversized#English','https://www.merriam-webster.com/dictionary/oversized'])
W('undersized','英 /ˌʌndəˈsaɪzd/；美 /ˌʌndərˈsaɪzd/','尺寸不足的；比通常、预期小的',
 '东西本身未必极小，只是放到这个用途、同类标准旁边显得不够大。undersized pump 就是对任务而言偏小、能力不足的泵。',
 'under- 低于标准、要求 + sized。不是在某个大小的下方；-ed 在 /z/ 后读 /d/。',S,
 'an undersized container 偏小容器，undersized equipment 规格偏小的设备，undersized for a position 对某位置的通常体格而言偏小。比较要带着对象和用途看。',
 'an undersized container；undersized equipment；undersized for。',
 'small 可是合适的小号；undersized 更常暗示低于通常或所需。和 underused 使用不足是不同关系。',
 ('The undersized container could not hold all the tools.','容器偏小，装不下全部工具。'),('The engineer replaced the undersized pump.','工程师换掉了规格不足的泵。'),sources=['https://en.wiktionary.org/wiki/undersized#English','https://www.merriam-webster.com/dictionary/undersized'])
R('B4471','具有某种尺寸，以及超过、不足、居中等尺寸比较','SIZED：尺寸要有比较基准，前半告诉你怎样比','sized → oversized、undersized；midsized 处在同类中间，supersized 强调特大。',
 '大、小不一定是不合适。oversized 可能是有意设计，undersized 则常带相对要求偏小的意思。',
 'size + -ed → sized；over- 超过、under- 不足、mid- 居中，super- 加强尺寸。',
 [['尺寸性质与比较','sized · oversized · undersized · midsized · supersized']],
 'sized 读 /saɪzd/；oversized 与 large 不完全一样，undersized 也不是 underused。',
 'The first container was undersized, while the replacement was unnecessarily oversized.\n\n第一个容器偏小，换来的那个却又大得没必要。','sized oversized undersized midsized supersized')
if __name__=='__main__':save('continuation_20261030_jn',ROOTS,WORDS)
