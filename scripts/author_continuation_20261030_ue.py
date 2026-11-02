"""Two overlooked old English elements and common plural forms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2656':dict(words=['child','children'],label='child 与 children：复数上又加了复数',note='children 承接旧复数 cildru、childer 等材料，再添另一复数词尾，形成保留到今天的双重复数；现代不能继续再加 s。'),
 'B2585':dict(words=['woman','women'],label='woman 与 women 的读音变化',note='woman /ˈwʊmən/；women /ˈwɪmɪn/。两个音节都要听，不能只按字面把 woman 的尾字母换一下。'),
 'B2763':dict(words=['tooth','teeth'],label='tooth 与 teeth：旧复数留下的变元音',note='tooth → teeth 是旧 i 变音的遗迹；更早词尾影响前面的元音，词尾后来不见了，元音差别留下。'),
 'B2770':dict(words=['foot','feet'],label='foot 与 feet：脚和英尺',note='foot → feet 保留旧 i 变音。数值后说 several feet；数词加单位在名词前作复合修饰时常用单数 foot。'),
 'B2592':dict(words=['mouse','mice'],label='mouse 与 mice：旧复数及鼠标',note='mouse → mice 也是旧 i 变音后经过后续语音变化的结果。电脑鼠标的复数 mice、mouses 都可见。'),
 'B2777':dict(words=['goose','geese'],label='goose 与 geese：鹅的复数',note='goose → geese 保留旧 i 变音；它是这个词的历史形式，不能推广成所有 oo 都要变 ee。'),
}
R('B3246','不、没有；旧否定成分留下的常用词','NE：给时间、数量、事物加一个否定',
 '时间上没有一次，是 never；数量上一个也没有，是 none；努力最后什么也没留下，可说 come to naught。',
 '古英语 ne 是常见否定词。它与其他材料结合形成一批现代熟词；今天 ne 本身通常不独立使用，重点学仍在生活中出现的后代。',
 'never 接 ne + æfre〔任何时候〕；none 接 ne + an〔一个〕。naught、nought 接 na + wiht〔任何事物、东西〕的旧复合及其音变。no 的旧副词来源可接 ne + a〔曾、总〕，限定词 no 又与 none 的后续发展相连，不能给所有 no 只画一条现代拆分。',
 [['一般否定与时间','no · not · never'],['数量与事物','none · nothing'],['归零与一无所获','naught · nought'],['同族词义转变','naughty']],
 'none 要按所指对象决定搭配，不能由古词源“not one”就认定现代永远只能接单数。naughty 从旧时无用、恶劣的词族发展，现代说孩子时常弱化为淘气。',
 'None of the keys worked, and all our efforts came to naught.\n\n所有钥匙都打不开，我们的一番努力全白费了。',
 'no not never none nothing naught nought naughty')
R('A1961','旧 to- 的分开义；另源 to 与时间、方向的结合','TO-：同样拼写，先分清两条历史',
 '今天、今晚、明天，原来像“在这一天、在这夜里、在次日早晨”的短语；词用久了，写成了一个词。',
 '旧英语还有另一个表示分开、毁裂的 to-，许多相关动词已消失或很古旧。today、tonight、tomorrow、together 接的是介词 to 与后词结合的另一来源；学习时把仍常用的这一组讲清。',
 '时间、方向材料 to + day／night／旧 morgen〔早晨〕；together 接 to + gædere〔聚在一起〕。这里的 to 可有在、于、向等旧用法，不能一律翻成现代“去做”。表示分裂的旧 to- 与这组不是一个词源。',
 [['当下与随后时间','today · tonight · tomorrow'],['聚到一处','together']],
 'tonight 表示今晚，tomorrow 表示明天。旧分裂前缀 to- 不宜拿来解释这些常用时间词。',
 'We will stay together tonight and leave tomorrow.\n\n我们今晚待在一起，明天离开。',
 'today tonight tomorrow together')
W('naught','英 /nɔːt/；美 /nɔːt/ 或 /nɑːt/','无、毫无；固定表达中：白费、一无所获',
 '花了许多力气，最后什么也没留下：all came to naught。它常把一番努力归到零。',
 '接古英语 nawiht 等，旧结构相当于 no + thing：na 否定，wiht 指事物。音节逐渐缩短，经过中古英语形成 naught；数字零等义也由什么都没有发展。',
 [['古英语 na + wiht → nawiht 等','没有任何东西'],['中古英语相关形式 → naught','无；零；努力白费的固定表达']],
 'come to naught 最终落空；all for naught 全白费了；set at naught 把某物看得毫无价值，较书面。日常直接说没有，通常用 nothing 更自然。',
 'efforts came to naught；it was all for naught。','naught 与 nought 同族、常同音；nought 在英式读零时更常见，naught 更常出现在书面、修辞的白费表达，分工并非绝对。',
 ('Months of planning came to naught when the event was cancelled.','活动取消，几个月的筹划都落了空。'),('They worried that all their work had been for naught.','他们担心所有工作都白费了。'),sources=['https://www.etymonline.com/word/naught','https://en.wiktionary.org/wiki/naught#English'])
W('nought','英 /nɔːt/；美 /nɔːt/ 或 /nɑːt/','零〔尤其英式〕；无、一无所获',
 '小数点前一个零，英式可读 nought point five。它背后的老画面就是一个东西也没有。',
 '接古英语 nowiht、nawiht 等否定加事物的复合，与 naught 同族。不同拼写有长期历史；零的读法和一无所获的固定表达后来并行。',
 [['古英语 nowiht／nawiht 等','没有东西、什么也没有'],['现代 nought','数字零；come to nought 等固定表达']],
 'nought point five 0.5；noughts and crosses 英式井字棋游戏名；come to nought 最终落空。美式普通读零常用 zero。',
 'nought point two；all came to nought。','nought 的 gh 在常见现代读音中不发音。nought 和 naught 拼写不同而同源，不能按字母数断定一个是另一个加了后缀。',
 ('The display read nought point five.','显示屏上显示零点五。'),('The children played noughts and crosses on a sheet of paper.','孩子们在一张纸上玩井字棋。'),sources=['https://www.etymonline.com/word/nought','https://en.wiktionary.org/wiki/nought#English'])
W('tonight','/təˈnaɪt/','今晚；在今晚',
 '把时间指针落在今天接下来的夜里，或此刻正在过的这一夜。tonight 不是每个夜晚，而是这一个晚上。',
 '接古英语 toniht，to 在旧时间表达中相当于在、于，niht 是夜晚。历史上经历分写、加连字符和合写，现代通常写一个词 tonight。',
 [['古英语 to + niht → toniht','在当前或即将到来的夜里'],['后来分写、连写等 → 现代 tonight','今晚；用作副词或时间名词']],
 'see you tonight 今晚见；tonight’s meeting 今晚的会议；stay here tonight 今晚住这里；late tonight 今晚较晚时候。',
 'tonight at eight；by tonight。','普通时间副词直接说 tonight，不说 on tonight。this evening 与 tonight 常有重叠，具体晚间边界依场景，不必硬划统一几点钟。',
 ('Are you free tonight?','你今晚有空吗？'),('Tonight’s concert starts at eight.','今晚的音乐会八点开始。'),sources=['https://www.etymonline.com/word/tonight','https://en.wiktionary.org/wiki/tonight#English'])
W('children','/ˈtʃɪldrən/','孩子们；子女；child 的复数',
 '不止一个孩子，用 children；说某人的 children，也可以说已经成年的子女，重点是亲子关系。',
 'child 接古英语 cild。旧复数后来出现 cildru、childer 等形式，中古英语又加复数词尾 -en，形成 children，常被称为双重复数。现代只把它当固定复数用。',
 [['古英语 cild → 旧复数 cildru、childer 等','孩子及其旧复数形式'],['再加复数 -en → children','旧复数上再添词尾，成为现代固定形式']],
 'young children 年幼的孩子；adult children 成年子女；children’s books 儿童读物。所有格写 children’s，已有复数含义。',
 'two children；her three children；the children are playing。','child → children；不能再写 childrens。children’s 的 ’s 标所有关系，不是再标一次普通复数。',
 ('The children are playing in the garden.','孩子们正在花园里玩。'),('Both of her children now live abroad.','她的两个子女现在都住在国外。'),sources=['https://www.etymonline.com/word/children','https://en.wiktionary.org/wiki/children#English'])
W('women','/ˈwɪmɪn/','女性、女人；woman 的复数',
 '一位女性是 a woman，多位女性是 women。写法只改一个字母，读音却要把两个音节一起换到熟悉的声音。',
 'woman 接古英语 wifman 等，历史结构为表示女性的 wif 加表示人的 man；旧复数有 wifmen、wimmen 等。women 保留较早的首音节元音材料，现代与 woman 的读音分开。',
 [['古英语 wifman；旧复数 wifmen、wimmen 等','女性；相关复数形式'],['现代 woman／women','单数 /ˈwʊmən/；复数 /ˈwɪmɪn/']],
 'two women 两位女性；women’s clothing 女装；women doctors 女性医生，作为性别限定时会见前后名词都用复数。',
 'women in science；a group of women。','woman 第一音节常 /wʊ/，women 常 /wɪ/；不要把复数也照单数读。women’s 是所有格，women 已经是复数。',
 ('Three women were waiting by the entrance.','三位女性在入口旁等候。'),('The exhibition celebrates women in science.','展览致敬科学领域的女性。'),sources=['https://www.etymonline.com/word/women','https://en.wiktionary.org/wiki/women#English'])
W('teeth','/tiːθ/','牙齿〔复数〕；齿状部件；tooth 的复数',
 '嘴里一颗颗牙是 teeth；锯子上一排能咬进木头的小尖齿，也借这个形状和作用来命名。',
 'tooth 接古英语 toð，复数 teð 等。更早的复数词尾影响词干元音，词尾后来消失，元音差异留下，这叫 i 变音；现代并非临时把 oo 换成 ee 的新规则。',
 [['较早词尾引起 i 变音 → 古英语 toð／teð','单复数通过词干元音区分'],['现代 tooth → teeth','牙齿复数；引申为工具上的齿']],
 'brush your teeth 刷牙；clench your teeth 咬紧牙关；the teeth of a saw 锯齿；by the skin of one’s teeth 勉强、险些没成功。',
 'front teeth；a gap between the teeth。','teeth 末尾是清音 /θ/，舌尖靠近或轻置上下齿间送气。teethe 长牙是相关动词，末尾常读浊音 /ð/。',
 ('She brushed her teeth before bed.','她睡前刷了牙。'),('The teeth of the old saw were badly worn.','那把旧锯子的锯齿磨损得很厉害。'),sources=['https://www.etymonline.com/word/tooth','https://en.wiktionary.org/wiki/teeth#English'])
W('feet','/fiːt/','脚〔复数〕；英尺〔复数〕；foot 的复数',
 '两只脚站在地上，是 feet；量一堵墙有多高，也可以用英尺。单位名称借了脚这一旧尺度。',
 'foot 接古英语 fot，复数元音差别承接旧 i 变音：更早的词尾曾改变前面的元音，后来词尾消失。长度单位 foot 在古英语中已有，历史长度并非始终相同。',
 [['古英语 foot 词族的旧单复数元音区别','脚；也用作长度单位'],['现代 foot → feet','脚的复数；英尺的复数']],
 'my feet hurt 我的脚疼；six feet tall 六英尺高；on your feet 站着；get back on your feet 恢复站稳，也可比喻恢复生活、经济状态。',
 'two feet away；stand on both feet。','The wall is six feet high 用复数 feet；a six-foot wall 作名词前的复合修饰，用单数 foot。on foot 徒步是固定单数搭配。',
 ('My feet were tired after the long walk.','走了那么远，我的脚都累了。'),('The wall is about six feet high.','那堵墙大约六英尺高。'),sources=['https://www.etymonline.com/word/foot','https://en.wiktionary.org/wiki/feet#English'])
W('mice','/maɪs/','老鼠〔复数〕；鼠标〔复数之一〕',
 '一只小老鼠是 a mouse，一群是 mice。电脑里那种手握着移动的小装置后来也叫 mouse，所以它的复数也会遇到 mice。',
 'mouse 接古英语 mus，旧复数 mys 已有元音差别，属 i 变音；后续语音变化形成现代 /maʊs/ 与 /maɪs/。电脑装置名称借自外形联想。',
 [['古英语 mus／mys 等','老鼠单复数的旧元音区别'],['现代 mouse／mice；再借用于电脑装置','老鼠；鼠标及其复数']],
 'field mice 田鼠；a pair of mice 两只老鼠；wireless mice 无线鼠标。电脑鼠标的复数 mouses 也有使用，动物复数通常 mice。',
 'mice in the cupboard；computer mice。','mice 不再加普通复数 s。mouse 的动词过去式是 moused，不能用 mice 当成捉老鼠的过去式。',
 ('We found mice in the garden shed.','我们在花园棚屋里发现了老鼠。'),('The office ordered ten wireless mice.','办公室订购了十个无线鼠标。'),sources=['https://www.etymonline.com/word/mouse','https://en.wiktionary.org/wiki/mice#English'])
W('geese','/ɡiːs/','鹅〔复数〕；goose 的复数',
 '一只鹅是 a goose，一群鹅走向池塘就是 geese。这个词先把整群鸟装进一个复数形式。',
 'goose 接古英语 gos 等，复数 geese 的元音变化来自旧 i 变音。它与 foot／feet、tooth／teeth 类似，都是旧词尾消失后留下的词干差别。',
 [['古英语 gos 等及旧复数变化','鹅；单复数的元音区分'],['现代 goose → geese','现代固定复数形式']],
 'a flock of geese 一群鹅；wild geese 雁、野鹅，具体鸟种依语境；geese on the pond 池塘里的鹅。',
 'two geese；geese flying overhead。','goose /ɡuːs/，geese /ɡiːs/。这是特定旧词的形式，不能把 moose 等其他 oo 词也类推成 meese。',
 ('A flock of geese landed on the lake.','一群鹅降落在湖面上。'),('Two geese walked slowly across the path.','两只鹅慢慢走过小路。'),sources=['https://www.etymonline.com/word/goose','https://en.wiktionary.org/wiki/geese#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ue',ROOTS,WORDS)
 extend_lessons()
