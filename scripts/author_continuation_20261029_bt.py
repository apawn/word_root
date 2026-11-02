"""Hot and cold: temperature and conventional metaphors."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
H=[['古英语 hāt → 中古英语 hot / hoot','热的'],['英语 hot','温度高；辣；热门；激烈；口语还可说性感或赃物']]
W('hot','英 /hɒt/；美 /hɑːt/','热的；辣的；热门的；激烈的；性感的；赃物的',
 '热是身体最直接的感受；人们借这种强烈刺激说辣、抢手、激烈等不同事情。',
 '继承古英语 hāt，经中古英语发展为 hot。现代多个比喻义各有使用习惯，不能碰到 hot 都只译热，也不要假装它们在同一时期一起出现。',H,
 'hot soup 是温度高，hot curry 往往指辛辣；a hot topic 是热门话题，a hot temper 是易怒脾气。hot goods 可指赃物，hot 单说人可表示性感，语气口语。',
 'hot weather；spicy hot food；a hot topic；hot off the press；hot goods。',
 'hot 的辣与 warm 的温暖不同；a hot deal 可能是吸引人的交易，但不能只凭 hot 判定价格或真实性。',
 ('Be careful: the bowl is still hot.','小心，碗还很烫。'),('The new café has become a hot topic in the neighbourhood.','新咖啡馆成了街区里的热门话题。'),('This curry is too hot for me.','这道咖喱对我来说太辣了。'))
W('hotness','英 /ˈhɒtnəs/；美 /ˈhɑːtnəs/','热；辣；热门或性感的程度',
 '把多热、多辣，或某种热门、性感的感觉拿出来当作性质来谈。',
 'hot + -ness，把形容词性质名词化。具体含义继承当前语境中的 hot，不总是物理温度。',H+[['hot → hotness','热、辣等性质 → 相应的程度或状态']],
 'the hotness of a pepper 辣椒的辣度；the hotness of the room 房间的热。形容人时可能是很口语的性感、吸引力，语体不同。',
 'the hotness of the sauce；judge the hotness；the hotness of the day。',
 '温度场景常直接用 heat 或 temperature；hotness 是可用的性质名词，却不是所有 heat 都应替换成它。',
 ('The label gives a rough guide to the sauce’s hotness.','标签粗略说明了这款酱的辣度。'),('We were surprised by the hotness of the room.','房间里热得出乎我们的意料。'))
W('hotly','英 /ˈhɒtli/；美 /ˈhɑːtli/','激烈地；强烈地；紧紧地',
 '说话、争夺或追赶都带着很高的强度，像热度上来了。',
 'hot + -ly，副词用法保留热的强烈、激烈比喻；常与争论、否认、竞争等动作搭配。',H+[['hot → hotly','热、激烈的 → 激烈地、紧迫地']],
 'hotly debated 争论激烈，hotly contested 竞争激烈；hotly pursued 被紧紧追赶。不是主要用来说明东西温度很热的通用副词。',
 'hotly debated；hotly disputed；hotly contested；hotly pursued。',
 'The soup is hot 是汤很热，不用 is hotly。hotly 多修饰动作或分词，尤其是争论、争夺的强度。',
 ('The proposal was hotly debated at the meeting.','这项提议在会上引发激烈讨论。'),('The final place in the team was hotly contested.','队里最后一个名额竞争得很激烈。'))
W('hotline','英 /ˈhɒtlaɪn/；美 /ˈhɑːtlaɪn/','热线；专用快速联系渠道',
 '一条随时能较快接通、专门处理某类事情的联系线。',
 'hot 强调紧急、即时或活跃 + line 通信线路。电话线路是基本背景，后来名称也用于特定服务的联系渠道。',C('hot 紧急、即时联系的意象','line 通信线路','hotline','专用快速联系渠道'),
 'a customer hotline 客服热线；a reporting hotline 举报热线。是否全天开放、是否收费，要看具体服务，词本身没有保证。',
 'a customer service hotline；call the hotline；set up a hotline。',
 'hotline 不是热得发烫的电线；helpline 强调提供帮助，hotline 强调专用联系通道，两者可能重合。',
 ('The company set up a hotline for questions about the recall.','公司设立了一条热线，解答关于召回的问题。'),('The leaflet lists the festival’s information hotline.','传单列出了艺术节的信息咨询热线。'))
W('hotbed','英 /ˈhɒtbed/；美 /ˈhɑːtbed/','温床；某种活动滋长的环境、中心',
 '先是让植物更容易长起来的暖床，再借说让某种现象特别容易滋长的地方。',
 'hot 热 + bed 苗床。由有助植物生长的暖苗床，引申为促使思想、活动等密集滋长的环境。',C('hot 暖热','bed 苗床','hotbed','暖苗床 → 活动、思想滋长之地'),
 'a hotbed of innovation 创新活跃之地；a hotbed of corruption 腐败滋生地。中文温床常偏负面，英语 hotbed 也可用于积极事物。',
 'a hotbed of activity；a hotbed of innovation；a hotbed of unrest。',
 'hotbed 不必是床，更不必是坏事；看 of 后面长出的是什么。',
 ('The small city became a hotbed of independent music.','这座小城成了独立音乐活跃之地。'),('The abandoned site was described as a hotbed of illegal dumping.','那处废弃场地被描述为非法倾倒垃圾的滋生地。'))
W('hotshot','英 /ˈhɒtʃɒt/；美 /ˈhɑːtʃɑːt/','能人；高手；自命不凡的厉害人物',
 '在人群里很抢眼、很有本事的人；说话人也可能嫌他太爱显摆。',
 'hot + shot 的固定复合词。旧有炽热弹丸等用法，后来形成厉害、成功的人这一口语称呼；具体语义桥梁不必硬编为一条必然故事。',C('hot 热、突出等意象','shot 的旧弹丸等用法','hotshot','固定口语称呼：高手、能人'),
 'a hotshot lawyer 厉害的律师；a young hotshot 年轻能手，也可能带讽刺。可作名词，也可放在职业名词前。',
 'a hotshot designer；a young hotshot；think one is a hotshot。',
 'hotshot 可赞也可讽刺，要听语气；hothead 是容易发火的人，不保证有本事。',
 ('They hired a hotshot designer to lead the new project.','他们请了一位设计高手带领新项目。'),('He acts like a hotshot, but rarely listens to the rest of the team.','他摆出一副能人架势，却很少听团队其他人的意见。'))
W('hottie','英 /ˈhɒti/；美 /ˈhɑːti/','性感迷人的人；口语称呼',
 '把 hot 形容人的性感、吸引力，直接变成对人的称呼。',
 'hot 性感的 + 非正式称呼后缀 -ie，双写 t 形成 hottie。不是把所有很热的人都这样称呼。',H+[['hot + -ie → hottie','性感、有吸引力的 → 相应的人物称呼']],
 'a movie hottie 影视里的性感人物，口语、娱乐文字可见。它着重外貌、性感吸引力，较随便，不是普通的漂亮或尊敬称呼。',
 'a movie hottie；describe someone as a hottie。',
 'hottie 比 attractive person 更随便，且更强调性感；不能只因为某人出汗、觉得热就用 hottie。',
 ('The magazine described the adult actor as a rising screen hottie.','杂志把那位成年演员称作冉冉上升的银幕性感明星。'),('In the comedy, she jokingly calls her husband a hottie.','喜剧中，她开玩笑地称丈夫是个性感帅哥。'))
R('B2672','热；辣；热门；激烈','HOT：身体上的热，借给强烈刺激和活跃状态','温度高是起点；辣、热门、激烈都是现代常见约定用法，不是遇到每个词都能自由替换。',
 'hot 接古英语 hāt。派生 hotness、hotly 后，先按语境确定说温度、辣度，还是情绪与竞争。',
 'hot → hotness、hotly；hotline 是联系线；hotbed、hothouse 是生长环境；hotshot、hothead、hottie 各说不同人的特征；再看 hotfix、superhot。',
 [['性质与程度','hot · hotness · hotly'],['联系与生长环境','hotline · hotbed · hothouse'],['人物称呼','hotshot · hothead · hottie'],['其他现代组合','hotfix · superhot']],
 'hotshot 能人，hothead 易怒者，hottie 性感的人；hotly 常说激烈地，不直接替换 hot 温度高。',
 'The hotshot’s proposal became a hot topic and was hotly debated.\n\n那位能人的提议成了热门话题，引发激烈讨论。',
 'hot hotness hotly hotline hotbed hothouse hotshot hothead hottie hotfix superhot')
CO=[['古英语 cald、ċeald → 中古英语 cold','冷的；名词也有对应寒冷形式'],['英语 cold','温度低；冷淡；感冒；缺少事先接触或准备的']]
W('cold','英 /kəʊld/；美 /koʊld/','冷的；冷淡的；寒冷；感冒；未经预热、准备的',
 '身体缺少温暖，人的态度也可以缺少温情；陌生联系、突然面对任务则借用没有预热的感觉。',
 '继承古英语 cald、ċeald 等形式，经中古英语发展。寒冷的环境与感冒曾在传统观念中联系，形成疾病名称；这不是在证明着凉就是全部病因。',CO,
 'I’m cold 是我觉得冷；I have a cold 是我感冒了。a cold welcome 冷淡的欢迎；a cold call 是事先没有联系基础的推销等电话。cold food 也可只是凉食，不等于变质。',
 'cold weather；have a cold；catch a cold；a cold reception；a cold call。',
 'cold 作形容词与 a cold 名词分清；cool 较凉，有时舒服，cold 常比它更冷。cold call 不看打电话那天温度。',
 ('I’m cold; could you close the window?','我觉得冷，能关上窗吗？'),('She stayed home because she had a cold.','她感冒了，所以待在家里。'),('His suggestion received a cold reception.','他的建议受到冷淡对待。'),sources=['https://en.wiktionary.org/wiki/cold#English','https://dictionary.cambridge.org/dictionary/english/cold'])
W('coldly','英 /ˈkəʊldli/；美 /ˈkoʊldli/','冷淡地；冷酷地',
 '说话、目光、态度里没有给人暖意。',
 'cold + -ly；对应冷淡、缺少感情的形容词用法，形容人怎样回应或行动。',CO+[['cold → coldly','冷淡的 → 冷淡地']],
 'reply coldly 冷冷地回答；look at someone coldly 冷淡地看某人。常在讲人际态度，不是食物被冰箱降温的通用说法。',
 'reply coldly；smile coldly；stare coldly at someone。',
 'coldly 可以说明表面态度冷淡，却不证明说话人内心一定毫无感情；calmly 平静地也不一定冷漠。',
 ('“That is your decision,” he said coldly.','“那是你自己的决定。”他冷冷地说。'),('She looked at him coldly and closed the door.','她冷淡地看了他一眼，关上了门。'))
W('coldness','英 /ˈkəʊldnəs/；美 /ˈkoʊldnəs/','寒冷；冷淡、冷漠',
 '可以是水、空气的冷，也可以是接触一个人时感到的疏远。',
 'cold + -ness，把温度低或态度冷的性质名词化；具体是哪种冷，由修饰对象决定。',CO+[['cold → coldness','冷的、冷淡的 → 寒冷、冷淡这种性质']],
 'the coldness of the water 水的冰冷；the coldness of her reply 她答复中的冷淡。the cold 也常直接说寒冷天气，不必处处换成 coldness。',
 'the coldness of the air；a certain coldness；emotional coldness。',
 'coldness 可说人际缺少温情；coolness 除凉爽外，还可能是沉着、镇定，不一定带相同负面感觉。',
 ('The coldness of the water took my breath away for a moment.','水冰冷得让我一时倒吸一口气。'),('I was surprised by the coldness of his reply.','他答复中的冷淡让我吃了一惊。'))
R('B2671','冷；冷淡；另有感冒名词义','COLD：温度不暖，态度也可不暖','身体觉得冷与人际感觉冷分开看；感冒是固定名词用法，不能仅凭词名倒推全部病因。',
 'cold 接古英语 cald、ċeald。coldly、coldness 继续从冷淡或低温的具体语境理解，不必每次都解释成天气。',
 'cold → coldly、coldness；cold call、cold reception 等短语在基础词中看。',
 [['温度、态度及固定名词义','cold'],['态度方式与性质','coldly · coldness']],
 'I’m cold 我觉得冷；I have a cold 我感冒了。calmly 平静地不必等于 coldly 冷淡地。',
 'The coldness of the room was easier to bear than the coldness of his welcome.\n\n比起他欢迎时的冷淡，房间里的寒冷反而更容易忍受。',
 'cold coldly coldness')
if __name__ == '__main__':save('continuation_20261029_bt',ROOTS,WORDS)
