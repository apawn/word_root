"""Frequently encountered extended nouns: relationships, requirements, capabilities."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3911':dict(words=['relationship','relationships'],label='relation → relationship → relationships：联系与相处',note='-ship 表状态、关系；relationship 包括人际关系及事物关联。'),
 'C1189':dict(words=['requirement','requirements'],label='require → requirement → requirements：需要满足的条件',note='require 加 -ment 形成所需事项，再有可数复数。'),
 'C1072':dict(words=['application','applications'],label='apply／application → applications：应用与申请',note='贴到对象上、把力量用上，连接到实际应用、申请及软件。'),
 'A1675':dict(words=['opportunity','opportunities','ability','abilities','community','communities'],label='-ity 词族的常见复数：机会、能力与群体',note='这些名词各有借入历史；词尾 y 变 ies 是现代复数规则，不表示它们都由英语现成形容词新造。'),
 'C1397':dict(words=['responsibility','responsibilities'],label='responsible → responsibility → responsibilities：需要交代的职责',note='从回应、作答，理解应该对什么事负责。'),
 'C0168':dict(words=['capability','capabilities'],label='capable → capability → capabilities：能承接并完成的事',note='-able 变为 -ability，再以 -ies 构成复数；容纳、胜任的词族保持联系。'),
 'C0401':dict(words=['facility','facilities'],label='facile／facility → facilities：让事情容易做的条件',note='由容易、便利发展到使活动能开展的设备、设施。'),
 'C0917':dict(words=['organization','organizations'],label='organ／organization → organizations：各部分协作的整体',note='工具、器官词族与各部分组织成整体相连；现代复数常指机构。'),
 'C0097':dict(words=['authority','authorities'],label='authority → authorities：职权、专家与主管机构',note='权威名词承拉丁 auctōritās；复数的主管当局和权威专家按语境分辨。'),
}
W('relationships','/rɪˈleɪʃənʃɪps/','关系；相处关系；事物间的关联〔复数〕',
 '两个对象怎样联系、怎样相处，这一组组联系就是 relationships：可以是朋友，也可以是温度与生长速度。',
 'relation + -ship → relationship，再加 -s，/p/ 后读 /s/。relation 经法语接拉丁 relātiō，与 referre、relātus 同族；-ship 是状态、关系后缀。',
 [['拉丁关系词族 → 法语 → 英语 relation','关联、关系'],['relation + -ship → relationship；再加 -s','相处、关联的状态 → 多种关系']],
 'build relationships 建立关系；working relationships 工作关系；relationships between variables 变量之间的关系；family relationships 家庭关系。',
 'maintain good relationships；understand the relationships。','relationships 既有人的相处，也有客观关联。in a relationship 在特定人际语境常表示有恋爱关系；一般的 working relationships 则是工作上的相处。',
 ('She builds good relationships with everyone on the team.','她与团队里的每个人都相处得很好。'),('The chart shows the relationships between light, temperature and plant growth.','这张图展示了光照、温度与植物生长之间的关系。'),sources=['https://en.wiktionary.org/wiki/relationships#English','https://en.wiktionary.org/wiki/relationship#English'])
W('requirements','/rɪˈkwaɪəmənts/〔美音保留 /r/：/rɪˈkwaɪərmənts/〕','要求；必要条件；实际所需〔requirement 的复数〕',
 '想让一件事做成，必须具备或满足的一条条条件，就是 requirements。它既可以是规定，也可以是事情本身需要什么。',
 'require + -ment → requirement，再加 -s，/t/ 后读 /s/。require 经法语接拉丁 requīrere，re- 与 quaerere 寻找、询问组成寻求、提出需要的词族。',
 [['拉丁 requīrere → 法语相关形式 → 英语 require','寻求、请求 → 需要、要求'],['require + -ment → requirement；再加 -s','必须满足的条件 → 多项要求']],
 'meet the requirements 满足要求；entry requirements 入学、入场条件；water requirements 用水需求；system requirements 系统运行要求。',
 'minimum requirements；requirements for the role。','requirements 可来自规章，也可来自实际需要。meet a requirement 是满足要求；make a request 是提出请求，request 通常保留请求别人做事的语气。',
 ('The course lists its entry requirements on the first page.','课程在第一页列出了入学条件。'),('We need to understand the plants’ water requirements.','我们需要了解这些植物的用水需求。'),sources=['https://en.wiktionary.org/wiki/requirements#English','https://en.wiktionary.org/wiki/requirement#English'])
W('applications','英 /ˌæplɪˈkeɪʃənz/；美 /ˌæpləˈkeɪʃənz/','应用、用途；申请；应用软件；施用〔复数〕',
 '把方法真正用到对象上，是 applications 的应用分支；把请求正式提交出去，是申请；替你完成具体任务的程序，也叫 applications。',
 'application + -s，/n/ 后读 /z/。名词经法语接拉丁 applicātiō，来自 applicāre，由 ad- 向、到与 plicāre 折叠、使相接相连；现代与 apply 对应，但不是英语先有 apply 再临时造出所有 application 用法。',
 [['拉丁 applicāre、applicātiō → 法语 → application','使贴到、施用、投入 → 应用、申请等'],['application + -s → applications','多种应用；多份申请；多个应用程序']],
 'practical applications 实际应用；job applications 求职申请；software applications 应用软件；applications of paint 多次涂漆。',
 'review the applications；applications in everyday life。','在招聘、入学语境，applications 常是申请；在设备里常是应用程序；applications of a theory 则是理论的应用。app 是 application 的常见缩写。',
 ('The discovery has several practical applications.','这项发现有好几种实际用途。'),('The school received more applications than it expected.','学校收到的申请比预想的多。'),sources=['https://en.wiktionary.org/wiki/applications#English','https://en.wiktionary.org/wiki/application#English'])
W('opportunities','英 /ˌɒpəˈtjuːnətiz/；美 /ˌɑːpərˈtuːnətiz/','机会；有利时机；可做某事的条件〔复数〕',
 '有一扇门在合适的时候打开，让你能做成一件事，这样的时机、条件就是 opportunities。门是帮助理解的比喻。',
 'opportunity 的 y 变为 -ies。词基经法语接拉丁 opportūnitās，来自 opportūnus 合适、有利；较早通常联系 ob 向与 portus 港口，常以有利于入港的条件解释合适、及时的画面。',
 [['拉丁 opportūnus → opportūnitās → 法语 → opportunity','合适、有利 → 有利时机、机会'],['opportunity 变 y 为 ies → opportunities','多次机会、可利用的有利条件']],
 'opportunities to learn 学习机会；job opportunities 工作机会；equal opportunities 平等机会；opportunities for improvement 改进的空间、机会。',
 'create new opportunities；make the most of opportunities。','opportunity 常强调可以利用的有利条件；chance 也能表示可能性，如 a chance of rain。opportunities to do 和 opportunities for something 都常用。',
 ('The project gives students opportunities to work with local artists.','这个项目给学生提供了与当地艺术家合作的机会。'),('We looked for opportunities to improve the design.','我们寻找可以改进设计的地方和机会。'),sources=['https://en.wiktionary.org/wiki/opportunities#English','https://en.wiktionary.org/wiki/opportunity#English','https://www.etymonline.com/word/opportune','https://en.wiktionary.org/wiki/opportunus#Latin'])
W('responsibilities','英 /rɪˌspɒnsəˈbɪlətiz/；美 /rɪˌspɑːnsəˈbɪlətiz/','职责；责任；需要照顾、完成的事务〔复数〕',
 '哪些事情轮到你照顾、做好，出了问题需要你交代，这些就是 responsibilities。',
 'responsible + -ity → responsibility，再变 y 为 -ies。-ible 与 -ibility 对应，重音在 -bil-。responsible 经法语接拉丁 respondēre 回答、回应，较早联系 spondēre 郑重承诺。responsibility 这一步形成于英语。',
 [['拉丁回应、承诺词族 → 法语 → responsible','能作答、应交代 → 负责的'],['responsible → responsibility → responsibilities','责任 → 分得开的各项职责']],
 'family responsibilities 家庭责任；daily responsibilities 日常职责；take on responsibilities 承担职责；share responsibilities 分担责任。',
 'carry out your responsibilities；responsibilities at work。','responsibilities 常指具体分工、照顾事项；responsibility 也可不可数地说负责状态、归责，如 take responsibility for a mistake。职责可以分担，具体归责仍看上下文。',
 ('Her new responsibilities include training the volunteers.','她的新职责包括培训志愿者。'),('They share the responsibilities of caring for their father.','他们分担照顾父亲的责任。'),sources=['https://en.wiktionary.org/wiki/responsibilities#English','https://en.wiktionary.org/wiki/responsibility#English'])
W('capabilities','/ˌkeɪpəˈbɪlətiz/','能力；功能；能够做到的事情〔capability 的复数〕',
 '一个人、一台设备或一个系统到底能完成哪些事，这些能做到的本领、功能就是 capabilities。',
 'capable + -ity → capability，-able 对应 -ability，再变 y 为 -ies。capable 经法语接晚期拉丁 capābilis，较早联系 capere 拿住、容纳，由装得下、承接得住发展到能胜任。',
 [['拉丁 capere、capābilis → 法语 → capable','拿住、容纳 → 能容纳、能胜任'],['capable → capability → capabilities','有能力 → 一项项能力、功能']],
 'technical capabilities 技术能力；the camera’s capabilities 相机的功能；expand our capabilities 扩展能力；beyond its capabilities 超出它的能力范围。',
 'a range of capabilities；develop new capabilities。','skills 常说练出来的具体技能；capabilities 更广，可以概括人、组织、设备能做到什么。设备的 capabilities 也常直译为功能、性能范围。',
 ('The guide explains the camera’s main capabilities.','这份指南解释了相机的主要功能。'),('The project helped the team develop new capabilities.','这个项目帮助团队培养了新的能力。'),sources=['https://en.wiktionary.org/wiki/capabilities#English','https://en.wiktionary.org/wiki/capability#English'])
W('facilities','/fəˈsɪlətiz/','设施；设备及便利条件；特定用途场所〔复数〕',
 '能让一项活动方便开展的场地、设备和条件，就是 facilities：泳池、洗手间、实验设备都可算在里面。',
 'facility 的 y 变为 -ies。facility 经法语 facilité 接拉丁 facilitās 容易、便利，来自 facilis 容易做的，联系 facere 做。便利条件后来具体化为设施、场所。',
 [['拉丁 facere → facilis、facilitās → 法语 → facility','做 → 容易做、便利'],['facility → facilities','便利条件 → 供活动开展的设施、场所']],
 'sports facilities 体育设施；research facilities 研究设施；washing facilities 洗漱设施；facilities for children 儿童活动设施。',
 'improve the facilities；modern facilities。','facilities 常把一整套便利条件合起来说，不只是单件机器；equipment 通常不可数，更侧重设备。a facility 可说某个具体机构、场所，facility 也另有熟练、轻松做事的能力义。',
 ('The campsite has basic washing facilities.','营地有基本的洗漱设施。'),('The new building includes sports facilities for local residents.','新大楼设有供当地居民使用的体育设施。'),sources=['https://en.wiktionary.org/wiki/facilities#English','https://en.wiktionary.org/wiki/facility#English','https://www.etymonline.com/word/facility'])
W('abilities','/əˈbɪlətiz/','能力；本领；才干〔ability 的复数〕',
 '一个人在不同方面能做好什么，这一项项本领就是 abilities；范围可以包括学会的技能和较广的思考、表达能力。',
 'ability 的 y 变为 -ies。ability 经古法语 ableté 接拉丁 habilitās，与 habilis 合用、有能力的相连，更早联系 habēre 拿着、拥有。现代与 able 对应，但名词有自己的借入历史。',
 [['拉丁 habēre、habilis、habilitās → 古法语 ableté → ability','拿取、合用 → 能力'],['ability 变 y 为 ies → abilities','不同方面的能力、本领']],
 'different abilities 不同能力；reading abilities 阅读能力；natural abilities 天赋能力；develop your abilities 发展能力。',
 'people with a wide range of abilities；confidence in her abilities。','ability 可以说做某事的能力，如 the ability to explain；abilities 适合并列多方面的本领。able to do 是形容词结构，ability to do 是名词结构。',
 ('The activity allows children of different abilities to work together.','这项活动让能力各不相同的孩子能够一起合作。'),('She became more confident in her abilities.','她对自己的能力变得更有信心了。'),sources=['https://en.wiktionary.org/wiki/abilities#English','https://en.wiktionary.org/wiki/ability#English'])
W('organizations','英 /ˌɔːɡənaɪˈzeɪʃənz/；美 /ˌɔːrɡənəˈzeɪʃənz/','组织；机构；团体〔复数〕',
 '把人和各自职责安排好，使大家能一起做成事，这样形成的一个个团体，就是 organizations。',
 'organization + -s，/n/ 后读 /z/。organization 接中世纪拉丁 organizātiō 及法语相关路线，较早 organum 来自希腊 órganon 工具、器官；各部分组成发挥作用的整体，发展到机构义。英式也常拼 organisations。',
 [['希腊 órganon → 拉丁 organum、organizāre、organizātiō → organization','工具、发挥功能的部分 → 有结构的整体'],['organization + -s → organizations','一套套组织起来的机构、团体']],
 'local organizations 当地组织；charitable organizations 慈善机构；international organizations 国际组织；voluntary organizations 志愿团体。',
 'work with several organizations；organizations of different sizes。','organization 可表示组织安排这一过程或能力，如 good organization；organizations 这种复数更常说具体机构。organ 的工具、器官背景，能帮助记住各部分发挥功能、相互配合的整体画面。',
 ('Several local organizations helped prepare the festival.','几个当地组织协助筹备了节庆活动。'),('The library works with organizations across the town.','图书馆与镇上的多家机构合作。'),sources=['https://en.wiktionary.org/wiki/organizations#English','https://en.wiktionary.org/wiki/organization#English','https://www.etymonline.com/word/organization'])
W('communities','英 /kəˈmjuːnətiz/；美 /kəˈmjuːnətiz/','社区；群体；有共同联系的人群〔复数〕',
 '住在同一片地方，或因共同兴趣、身份而联系起来的人，形成一个个 communities。共同联系比地理围墙更重要。',
 'community 的 y 变为 -ies。community 经古法语 comunité、communité 接拉丁 commūnitās，来自 commūnis 共同的、共享的；不是 communication 的缩写。',
 [['拉丁 commūnis → commūnitās → 法语 → community','共同、共享 → 共同关系、群体'],['community 变 y 为 ies → communities','不同地方社区；不同共同身份、兴趣群体']],
 'local communities 当地社区；rural communities 乡村社区；online communities 网络社群；fishing communities 渔业社区、以捕鱼为生的群体。',
 'bring communities together；serve different communities。','community 可按居住地形成，也可按共同兴趣、工作、文化联系形成。communities 指人群或社会联系，neighbourhoods 通常更强调居住区域，两个词有重合。',
 ('The programme connects schools in different rural communities.','这个项目把不同乡村社区的学校联系起来。'),('Online communities allow people to share their interest in rare books.','网络社群让人们能够交流对珍本书的兴趣。'),sources=['https://en.wiktionary.org/wiki/communities#English','https://en.wiktionary.org/wiki/community#English','https://www.etymonline.com/word/community'])
W('authorities','英 /ɔːˈθɒrətiz/；美 /əˈθɔːrətiz/','主管当局、有关部门；权威人士、权威资料〔复数〕',
 '有权负责处理一件事的部门，可以统称 authorities；对某个领域说得上话、值得信赖的专家，也可以叫 authorities。职权与专业可信度要分开看。',
 'authority 的 y 变为 -ies。authority 经古法语 autorité 接拉丁 auctōritās，来自 auctor 发起者、担保者，远接 augēre 使增长；字母 h 后来进入英语拼写，并形成现代 /θ/ 读音。',
 [['拉丁 auctor、auctōritās → 古法语 autorité → authority','发起者、担保者 → 影响力、权威、职权'],['authority 变 y 为 ies → authorities','主管机构；多个权威专家、来源']],
 'local authorities 当地主管部门；the relevant authorities 有关部门；leading authorities on birds 鸟类研究的权威专家；consult the authorities 查阅权威资料。',
 'inform the authorities；recognized authorities in the field。','the authorities 常统称有正式管辖、管理职责的部门；an authority on something 则常是某领域的专家。authority 说权力、授权本身时通常不可数，如 act without authority。',
 ('The local authorities repaired the damaged bridge.','当地主管部门修复了受损的桥。'),('The book draws on the work of several leading authorities on birds.','这本书参考了几位鸟类权威专家的研究成果。'),sources=['https://en.wiktionary.org/wiki/authorities#English','https://en.wiktionary.org/wiki/authority#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xm',ROOTS,WORDS)
 extend_lessons()
