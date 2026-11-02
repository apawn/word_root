"""Size and test, two familiar bases with less obvious histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['古法语 assise 的缩短形式 sise、cise → 中古英语 sise','规定、限度；规定的量'],['英语 size','数量、规格 → 大小、尺寸；按尺寸调整']]
W('size','/saɪz/','大小；尺寸、尺码；按大小分类、调整',
 '不只问大不大，还能问这东西占多大空间、该选哪个规格。',
 '尺寸义经古法语 assise 的缩短形式入英语，早期与规定的量、规格有关，后来泛指大小。另有绘画、造纸的施胶材料义，来源关系不明，不强串到尺寸义里。',S,
 'the size of the room 房间大小，What size? 什么尺码，size ten 十号尺码；size up 还可说打量、判断一个人或局面。',
 'the size of；What size?；in different sizes；size up。',
 'size 大小，shape 形状；两个箱子可以 the same size but different shapes。size 也不只长度，衣服尺码可能综合多项尺寸。',
 ('What size shoes do you wear?','你穿多大码的鞋？'),('The boxes are the same size but different shapes.','这些箱子大小相同，但形状不同。'))
W('sized','/saɪzd/','某种大小的；按尺寸处理的',
 '通常等前面告诉你多大：medium-sized 是中等大小，不是只知道一个孤立的有大小。',
 'size + -ed，保留 e 后加 d，形成动词过去形式或形容词；末尾读 /zd/。在复合修饰语中常接大小说明。',S+[['size + -ed → sized','具有某种大小；已按尺寸处理']],
 'a medium-sized bag 中号包，similarly sized rooms 大小相近的房间；修饰语中的连字符是正常书写，不等于再单列一个新词。',
 'medium-sized；similarly sized；differently sized。',
 'size 是大小名词或动词，sized 常是已处理或带尺寸性质的形式；不要把 sized 单独当“大”的同义词。',
 ('They booked two similarly sized rooms.','他们订了两间大小相近的房间。'),('A medium-sized bag should be enough for the trip.','一个中号包应该就够这趟旅行用了。'))
W('sizable','/ˈsaɪzəbəl/','相当大的；可观的',
 '不是普通地有尺寸，而是大到值得专门提一句：可观的一笔钱、数量或差距。',
 'size + -able，常规写 sizable，也见 sizeable。这里成词后的固定义是相当大，不能机械译成能被定尺寸。',S+[['size + -able → sizable','具有显著大小 → 相当大的']],
 'a sizable sum 一笔可观金额，a sizable crowd 相当多的人；可修饰抽象差距、比例。',
 'a sizable sum；a sizable crowd；a sizable difference。',
 'sizable 强调规模可观，sized 常需前文交代具体大小；a sizable company 与 a medium-sized company 重点不同。',
 ('They received a sizable donation.','他们收到了一笔可观的捐款。'),('There is a sizable gap between the two estimates.','两项估算之间有相当大的差距。'))
W('oversize','英 /ˈəʊvəsaɪz/；美 /ˈoʊvərsaɪz/','超常尺寸的；特大号的',
 '比通常的标准、用途或比例更大；可以是需要特殊运输，也可以是有意设计的宽大款式。',
 'over- 超出 + size 大小，组合成超出通常尺寸的形容词，也有相关动词用法。oversized 是很常见的另一形容词形式。',S+[['over- + size → oversize','超出通常尺寸 → 特大、超大']],
 'oversize luggage 超尺寸行李，an oversize coat 宽大外套；具体超出什么标准由场景确定。',
 'oversize luggage；an oversize load；an oversize coat。',
 'oversize 不一定是买错尺码，服装可能有意宽大；overweight 说重量超标，两个标准不同。',
 ('The airline charges extra for oversize luggage.','航空公司对超尺寸行李另行收费。'),('He wore an oversize coat over his suit.','他在西装外穿了一件宽大的外套。'))
W('outsize','英 /ˈaʊtsaɪz/；美 /ˈaʊtsaɪz/','特大的；超常规模的',
 '大到跑到普通规格之外；也能说影响、作用比通常预期更大。',
 'out- 超出 + size，形成超常尺寸的表达。outsize 和 outsized 都可见，现代还常修饰抽象影响。',S+[['out- + size → outsize','超出正常规格 → 特大、超常']],
 'an outsize suitcase 特大手提箱，an outsize influence 异常大的影响；不是只说位置在尺寸外面。',
 'an outsize suitcase；an outsize role；an outsize influence。',
 'outsize 与 oversize 在具体大小上有重合；outsize influence 更突出影响超过通常比例，不是衣服尺码。',
 ('The small country has an outsize influence on the industry.','这个小国对该行业有着超出其规模的影响力。'),('An outsize suitcase blocked the narrow passage.','一只特大手提箱堵住了狭窄通道。'))
W('resize','/ˌriːˈsaɪz/','调整大小、尺寸',
 '把原有尺寸改成需要的尺寸，既可以缩小，也可以放大。',
 're- 重新 + size 按大小处理，现代常见于图片、窗口和物件尺寸调整；re- 不限定调整的方向。',S+[['re- + size → resize','重新设定尺寸 → 调整大小']],
 'resize an image 调整图片大小，resize a window 调整窗口大小，resize a ring 改戒指尺寸。',
 'resize an image；resize a window；resize a ring。',
 'resize 改大小，crop 裁掉边缘；两者都可能改变图像尺寸，但做的动作不同。',
 ('Resize the image before uploading it.','上传前先调整图片大小。'),('You can resize the window by dragging its corner.','你可以拖动窗口一角来调整它的大小。'))
W('downsize','/ˈdaʊnsaɪz/','缩减规模；裁员；搬入较小住房',
 '把现在的一整套规模往小里收：公司缩减人员，家庭也可能从大房子搬到小房子。',
 'down- 向下、减少 + size。现代常用于组织、产品和住房规模调整，意义由具体对象决定。',S+[['down- + size → downsize','把规模往小里改 → 缩减规模']],
 'downsize the workforce 缩减员工规模，downsize to a smaller home 换住较小房子；公司语境可能委婉指裁员。',
 'downsize the workforce；downsize the business；downsize to a flat。',
 'resize 只说明改尺寸，downsize 明确变小；downsize 公司不一定等于公司关闭。',
 ('The company plans to downsize its workforce.','公司计划缩减员工规模。'),('They decided to downsize to a smaller flat.','他们决定换住一套较小的公寓。'))
R('B3189','大小、规格与调整规模','SIZE：问它有多大、该用哪个规格','先看 size，再把 sized 的具体尺寸和 sizable 的相当大分开；最后按超出、重设、缩减看前缀变化。',
 'size 的大小义先接规定的量与规格，才成为现代通用大小词。施胶材料同形义另行保留来源不确定，不硬凑。',
 'size → sized、sizable；over-、out- 超出 → oversize、outsize；re- 重设 → resize；down- 缩减 → downsize；共享 supersize。',
 [['核心与性质','size · sized · sizable'],['超出通常尺寸','oversize · outsize · supersize'],['调整方向','resize · downsize']],
 'sizable 相当大，sized 常由修饰语交代多大；resize 不限定放大缩小，downsize 才说明缩小。',
 'We resized the image without changing the size of the page.\n\n我们调整了图片大小，没有改变页面尺寸。',
 'size sized sizable oversize outsize supersize resize downsize')
T=[['拉丁 testum → 古法语 test、teste','陶制容器；检验金属所用的器皿'],['英语 test','金属检验 → 检查品质、能力与结果']]
W('test','/test/','测试；检验；考试；考验',
 '不是光看一眼，而是给它一个问题、条件或操作，看看实际表现怎么样。',
 '借法语词上接拉丁 testum 陶器，历史英语有金属检验用容器义，后从检验金属扩展为一般检验。别与 testify 作证只按相似字母混在一起。',T,
 'take a test 参加考试，test a product 测产品，put something to the test 实际考验；a test result 是测试结果，不自动是合格结果。',
 'take a test；pass a test；test a theory；put to the test。',
 'test 范围很广，exam 常指正式考试；一次 test 也不一定证明所有环境下都可靠。',
 ('We tested the new system before the launch.','上线前，我们测试了新系统。'),('The long journey put their patience to the test.','漫长的旅程考验了他们的耐心。'))
W('tester','英 /ˈtestə/；美 /ˈtestər/','测试人员；测试器；试用样品',
 '可能是负责测试的人，也可能是用来测量的工具；商店里让顾客先试一试的样品也这样叫。',
 '测试义是 test + -er，构成人、工具等名词。历史上同形 tester 另有床顶罩等名词，来源不同；本页只讲常用测试分支。',T+[['test + -er → tester','执行测试的人、器具；供试用的样品']],
 'a software tester 软件测试员，a battery tester 电池测试器，a perfume tester 香水试用装。',
 'a software tester；a battery tester；a perfume tester。',
 '-er 不只表示人；The tester needs a battery 中 tester 很可能是工具，要用句意判断。',
 ('The tester found a bug in the payment screen.','测试人员在付款页面发现了一个漏洞。'),('The shop keeps perfume testers beside the display.','商店把香水试用装放在陈列架旁。'))
W('retest','动词 /ˌriːˈtest/；名词 /ˈriːtest/','重新测试；复试、补测',
 '已经测过，再测一遍；可能因为原结果有疑问，也可能想确认改动后的情况。',
 're- 再次 + test。动词和名词都常见，一些读法中动词重音偏后、名词偏前，实际口音可有变化。',T+[['re- + test → retest','再次测试 → 复测；复测这件事']],
 'retest a sample 复测样品，request a retest 要求复测，take a retest 参加补测。再次测不自动表示第一次一定失败。',
 'retest a sample；request a retest；a driving retest。',
 'retest 强调再测，review 可以只是复查已有资料；没有实际重做测试时不必说 retest。',
 ('The laboratory will retest the sample tomorrow.','实验室明天将重新检测样品。'),('He requested a retest after questioning the result.','他质疑结果后要求复测。'))
W('testable','/ˈtestəbəl/','可检验的；可测试的',
 '能想出办法，用观察或实验去检查它，而不是永远只能凭感觉争论。',
 'test + -able 可被、能，构成可测试的形容词。这个能力描述只说存在检验办法，不预先给出真假结论。',T+[['test + -able → testable','能够被检验的']],
 'a testable hypothesis 可检验假设，a testable prediction 可检验预测，testable code 易于开展测试的代码。',
 'a testable hypothesis；a testable claim；testable code。',
 'testable 能检验，tested 已经检验；testable hypothesis 不等于已证实的理论。',
 ('The team turned the idea into a testable hypothesis.','团队把这个想法变成了可检验的假设。'),('The design makes each component separately testable.','这种设计使每个组件都能单独测试。'))
R('B3237','从金属检验到考试与测试','TEST：给一个条件，看实际表现','先看 test 这个动作，再读谁来测、重新测和能不能测；已有 pretest、testbed 一起归在本族。',
 '检验义的历史接陶制器皿与金属检验，不是从考试纸张凭空生出。现代 test 能检验知识、产品、假设或耐心。',
 'test → tester、testable；re- 再 → retest；pre- 预先 → pretest；test + bed → testbed。',
 [['核心、执行者与可检验性','test · tester · testable'],['先后与环境','pretest · retest · testbed']],
 'testable 不是已证实，retest 不是只复看旧报告；tester 可指人，也可指仪器、试用品。',
 'The tester will retest the system after the update.\n\n更新后，测试人员将重新测试系统。',
 'test tester testable pretest retest testbed')
if __name__=='__main__':save('continuation_20261029_dq',ROOTS,WORDS)
