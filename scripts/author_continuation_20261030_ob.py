"""Swallowing, ordinal -eth, several historical -el forms and backpacking."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()

Sw=[['古英语 swelgan → 中古英语 swolwen → swallow 吞下','嘴里的东西经过喉咙进入体内'],['古英语 swealwe → 中古英语 swalwe 等 → swallow 燕子','鸟名与吞咽动词是不同近源路线']]
W('swallow','英 /ˈswɒləʊ/；美 /ˈswɑːloʊ/','吞下；信以为真、忍下；燕子',
 'swallow water 是吞水；swallow a story 是不加质疑地接受说法；swallow your pride 是把自尊先忍下。a swallow 却可以是一只燕子，接另一条鸟名历史。',
 '吞咽义承古英语 swelgan，经中古英语 swolwen 到 swallow，并发展吸收、接受、抑制情感等比喻。鸟名承古英语 swealwe，经另一组中古英语形式延续，不由燕子吞食动作确定派生。',Sw,
 'swallow a mouthful 吞下一口；hard to swallow 难以下咽、难以接受；swallow your pride 放下自尊；a flying swallow 飞翔的燕子。',
 'hard to swallow；swallow your pride。',
 'swallow 与 chew 咀嚼是不同动作；鸟名与吞咽动词同形，具体先看句法、对象。',
 ('She swallowed the last mouthful of water.','她咽下最后一口水。'),('His explanation was hard to swallow.','他的解释让人难以相信。'))
R('B3047','吞入、接受与鸟名分源，燕尾形状另接鸟名','SWALLOW：动词往里吞，鸟名看燕子','swallow 的吞咽、接受支与燕子支分开；swallowtail 按燕尾形状命名。',
 '比喻的说法、骄傲像东西一样被吞下，容易形象理解。鸟的名称另有旧词，不能因为它吃飞虫就当作动词转名词的确定历史。',
 'swelgan → swolwen → 吞 swallow；swealwe → swalwe 等 → 鸟 swallow；鸟名 + tail。',
 [['吞咽、接受与同形鸟名','swallow'],['借燕尾形状命名','swallowtail']],
 'swallow 是吞，chew 是嚼；swallowtail 的 tail 指形状，不是吞掉尾巴。',
 'A swallow flew past while he swallowed the last sip of water.\n\n一只燕子飞过，他咽下最后一口水。','swallow swallowtail')

Or=[['古英语、英语中古阶段的整十序数形式','二十等基数名与序数词尾在历史中类推整合'],['现代 -ty → -tieth','twenty → twentieth 等；表示次序，也能表示等分中的一份']]
W('twentieth','/ˈtwentiəθ/','第二十；二十分之一',
 'twenty 是有二十个，twentieth 是排到第二十位。把整体平分二十份，a twentieth 又是一份，也就是二十分之一。',
 '承古英语 twentigotha、中古英语 twentithe 等，现代形式经类推更清楚地接 twenty。拼写 twenty 的 y 改 i + -eth → twentieth。',Or,
 'the twentieth century 二十世纪；her twentieth birthday 她的二十岁生日；one twentieth 二十分之一；缩写 20th。',
 'the twentieth century；one twentieth。',
 'twentieth 第二十与 twelfth 第十二不同；twenty 基数通常数数量，twentieth 常标次序。',
 ('She celebrated her twentieth birthday with friends.','她和朋友庆祝二十岁生日。'),('One twentieth of the class chose that option.','全班二十分之一的人选了那个选项。'))
W('thirtieth','英 /ˈθɜːtiəθ/；美 /ˈθɜːrtiəθ/','第三十；三十分之一',
 '三十个位置排成一列，最后那一位是 the thirtieth。它把 thirty 的数量换成名次；分数用法再看三十等分中的一份。',
 '承古英语 thritigotha 等及中古英语序数形式，现代类推对应 thirty。y 改 i + -eth → thirtieth，末尾读 /iəθ/。',Or,
 'the thirtieth page 第三十页；a thirtieth anniversary 三十周年；缩写 30th。',
 'the thirtieth page；the thirtieth anniversary。',
 'thirteenth 第十三与 thirtieth 第三十的结尾、重音不同；thirty 与 thirteen 的区别延续到序数词。',
 ('The answer appears on the thirtieth page.','答案在第三十页。'),('They marked the thirtieth anniversary of the project.','他们纪念项目三十周年。'))
W('fortieth','英 /ˈfɔːtiəθ/；美 /ˈfɔːrtiəθ/','第四十；四十分之一',
 'forty 的四十变成排位，就是 fortieth 第四十。最容易漏的是拼写：这里沿用 forty，没有把 four 里的 u 补回来。',
 '承中古英语 fourtithe 等，现代对应 forty 的类推形式。forty 的 y 改 i + -eth → fortieth，标准现代拼写无 u。',Or,
 'the fortieth floor 第四十层；a fortieth birthday 四十岁生日；缩写 40th。',
 'the fortieth floor；a fortieth birthday。',
 'fortieth 第四十，不写成 fourtieth；fourteenth 才是第十四。',
 ('The restaurant is on the fortieth floor.','餐厅位于第四十层。'),('We gathered for her fortieth birthday.','我们聚在一起庆祝她四十岁生日。'))
W('fiftieth','/ˈfɪftiəθ/','第五十；五十分之一',
 '五十周年、第五十页、排到第五十位，都用 fiftieth。后面的 /iəθ/ 让它与表示第十五的 fifteenth 分开。',
 '承中古英语 fiftithe、fyftith 等，现代对应 fifty。y 改 i + -eth → fiftieth，是整十序数的共同类推模式。',Or,
 'a fiftieth anniversary 五十周年；the fiftieth page 第五十页；缩写 50th。',
 'a fiftieth anniversary；the fiftieth page。',
 'fiftieth 第五十与 fifteenth 第十五不能只看前面的 fif-；词尾决定关键差别。',
 ('The museum celebrated its fiftieth anniversary.','博物馆庆祝成立五十周年。'),('The clue was hidden on the fiftieth page.','线索藏在第五十页。'))
W('sixtieth','/ˈsɪkstiəθ/','第六十；六十分之一',
 'sixty 数六十，sixtieth 把其中一位标为第六十。一分钟的六十等分里，一份就是 a sixtieth of a minute。',
 '承中古英语 sixtithe 等，现代 sixty 的 y 改 i + -eth → sixtieth。基数、序数对应在英语历史中经过类推整合。',Or,
 'a sixtieth birthday 六十岁生日；one sixtieth 六十分之一；缩写 60th。',
 'a sixtieth birthday；one sixtieth。',
 'sixteenth 是第十六，sixtieth 是第六十；读清后半不要只靠开头 six- 猜数值。',
 ('They planned a dinner for his sixtieth birthday.','他们安排晚餐为他庆祝六十岁生日。'),('A second is one sixtieth of a minute.','一秒是一分钟的六十分之一。'))
W('seventieth','/ˈsevəntiəθ/','第七十；七十分之一',
 'seventy 的七十换成序列位置，是 seventieth。后缀不改变七十这个基数参照，而是让它回答“第几个”。',
 '承中古英语 seventithe 等，现代 seventy 的 y 改 i + -eth → seventieth。与其他整十序数共享类推形成的拼写、读音关系。',Or,
 'a seventieth birthday 七十岁生日；the seventieth entry 第七十个条目；缩写 70th。',
 'a seventieth birthday；the seventieth entry。',
 'seventeenth 第十七与 seventieth 第七十不同；序数后缀不能只写成 seventy 加一个 s。',
 ('The family gathered for her seventieth birthday.','家人齐聚一堂庆祝她七十岁生日。'),('The seventieth entry was the last one on the list.','第七十个条目是清单的最后一项。'))
R('A1718','整十基数的序数、等分份额，拼写沿历史类推固定','-ETH：数量变成排位，整十分之一也借序数命名','twentieth、thirtieth、fortieth、fiftieth、sixtieth、seventieth 按 20 到 70 的数值顺序复习。',
 '排位回答第几个，数量回答有多少；a twentieth of 则回答二十等分里的一份。共同拼写是 -ty 变 -tieth，但各自还保留英语历史词形。',
 '旧序数形式经类推 → 现代 twenty、thirty 等对应形式；y 改 i 接 -eth；缩写 20th、30th、40th、50th、60th、70th。',
 [['按数值读整十序数','twentieth · thirtieth · fortieth · fiftieth · sixtieth · seventieth']],
 'thirteenth／thirtieth、fifteenth／fiftieth 等要读清；fortieth 沿用 forty，无 u。',
 'She read the twentieth, thirtieth and fortieth entries, then checked the fiftieth.\n\n她读了第二十、第三十、第四十个条目，再检查第五十个。','twentieth thirtieth fortieth fiftieth sixtieth seventieth')

El=[['英语及相关日耳曼语言的旧 -el、-le 等名词、动词构词','有工具、小称、反复动作等不同历史材料'],['部分整词借入或仅结尾相似','不能把所有现代 -el 都解释成同一个小称后缀']]
W('swivel','/ˈswɪvəl/','转环、旋转接头；绕轴转动',
 '椅子底座有轴，上半部能转向另一个方向，是 swivel。工具名是允许相连部件转动的接头，动作名则是围着支点转。',
 '承中古英语 swyvel、swivel，接古英语 swifan 转动的派生材料，带旧工具后缀 -el。名词的旋转连接用途又形成相应动词。',El[:1]+[['swifan 转动的派生 → swyvel → swivel','能转的接头 → 绕支点转动']],
 'a swivel chair 转椅；a swivel joint 旋转接头；swivel round 转过身、转向。',
 'a swivel chair；a swivel joint。',
 'swivel 常突出绕固定轴、支点改变方向；whirl 则常更突出快速旋转。',
 ('She swivelled her chair to face the screen.','她转动椅子面对屏幕。'),('The lamp is mounted on a swivel joint.','灯装在旋转接头上。'))
W('whirl','英 /wɜːl/；美 /wɜːrl/','快速旋转；纷乱、接连不断的活动；试一试',
 '树叶被风带着打转，是 whirl；一周事情转个不停，是 a whirl of activity。give it a whirl 则是“试着来一回”的固定口语。',
 '承中古英语 whirlen 及相关名词，联系古英语旋转词的派生、北欧同族形式等，具体影响路线有讨论。较早形式较长，带反复动作、名词构词材料，后来收缩成 whirl。',El[:1]+[['旧旋转词派生、北欧同族形式 → whirlen、whirl','转来转去 → 忙乱活动、一次尝试']],
 'whirl around 迅速打转；a whirl of activity 忙碌活动一片；give it a whirl 试试。',
 'whirl around；a whirl of activity；give it a whirl。',
 'whirl 的现代结尾已不是完整 -el 字母，历史构词材料不等于今天还能随意分出独立单词。',
 ('Leaves whirled around the courtyard.','树叶在院子里打转。'),('I had never tried pottery, but I decided to give it a whirl.','我没做过陶艺，但决定试一试。'))
W('gavel','/ˈɡævəl/','法槌、议事槌、拍卖槌',
 '会议主持人敲一下让大家安静，拍卖师落槌确认成交，这把小木槌就是 gavel。用声音标示程序节点，是它最直观的用途。',
 '木槌常用义来源未定，有与石工工具名称、组织用语等相联系的不同解释。旧的赋税同形词来自古英语 gafol、give 词族，不能直接把它的 give + -el 分析移给现代木槌义。',El[:1]+[['木槌 gavel 的近源未定；不同于古英语赋税同形词','用于议事、拍卖等的信号小槌']],
 'bang a gavel 敲槌；bring down the gavel 落槌；the auctioneer’s gavel 拍卖槌。',
 'bang a gavel；bring down the gavel。',
 'gavel 按具体议事器具认，不等于所有 hammer 锤子；使用传统也随机构、地区不同。',
 ('The chair struck the gavel to restore order.','主持人敲槌维持秩序。'),('The auction ended with a tap of the gavel.','拍卖在轻轻一声落槌中结束。'),sources=['https://en.wiktionary.org/wiki/gavel#English','https://www.etymonline.com/word/gavel'])
W('morel','/məˈrel/','羊肚菌',
 '菌盖表面一格格凹坑，像蜂窝，也让中文联想到羊肚，是 morel 的外观线索。英语名称有自己的借词历史，不是 more 更多加一个 l。',
 '借法语 morille，上接德语 morhel、morchel 等更早根类、菌类名称，涉及较古老的小称构词。英语是整词借入，不是现代以 more 为基础新造。',El[:1]+[['日耳曼根类、菌类名称及小称形式 → 法语 morille → morel','蜂窝状凹坑菌盖的羊肚菌']],
 'a morel mushroom 一朵羊肚菌；morel sauce 羊肚菌酱；dried morels 干羊肚菌。',
 'morel mushrooms；dried morels。',
 'morel 与 moral 道德的拼写、读音不同；这里是菌类名称，外观描写不替代物种鉴定。',
 ('The menu listed pasta with morel sauce.','菜单上列着羊肚菌酱意面。'),('The photograph showed the pitted cap of a morel.','照片展示了一朵羊肚菌满是凹坑的菌盖。'))
W('hovel','英 /ˈhɒvəl/；美 /ˈhʌvəl/','破屋、陋屋；简陋棚屋',
 '不是温馨小屋的中性称呼，而是很简陋、破败、住起来条件差的 hovel。故事用这个词，通常也在评价环境。',
 '见中古英语 hovel、hovil 等，早期涉及有顶通道、棚屋，后来用于简陋人居小屋。最早来源未定，把它确定拆成古英语 hof 房屋 + 小称后缀的说法有争议。',El[:1]+[['中古英语 hovel 等，有顶空间、棚屋 → hovel 陋屋','较后带贫陋、破败的人居评价，最远起源未定']],
 'a miserable hovel 破陋小屋；a damp hovel 潮湿陋屋。',
 'a miserable hovel；a damp hovel。',
 'hut 可中性说棚屋，hovel 通常更贬，突出简陋、肮脏、破败等条件差。',
 ('The novel begins in a damp little hovel.','小说从一间潮湿陋屋写起。'),('He described the neglected cottage as a hovel.','他把那间失修小屋形容成破屋。'),sources=['https://en.wiktionary.org/wiki/hovel#English','https://www.etymonline.com/word/hovel'])
W('cudgel','/ˈkʌdʒəl/','短粗棍棒；用棍棒打；竭力思索',
 '短而粗、常有较大一头的棍棒，是 cudgel。cudgel your brains 则像在敲自己的脑袋让它想起来，实际是绞尽脑汁的比喻。',
 '承古英语 cycgel，经中古英语 kuggel 等到 cudgel。较早可能涉及膨大、弯曲材料及工具、小称构词，细节有不同分析；名词再转打、竭力思索的动词。',El[:1]+[['cycgel → kuggel 等 → cudgel','棍棒 → 棍击、绞尽脑汁的比喻']],
 'a wooden cudgel 木棍棒；cudgel one’s brains 绞尽脑汁；take up the cudgels for 为……出面辩护。',
 'cudgel one’s brains；take up the cudgels for。',
 'cudgel one’s brains 是比喻，不是真的伤害脑袋；take up the cudgels for 常指言语辩护。',
 ('The museum displayed a wooden cudgel.','博物馆展出一根木棍棒。'),('I cudgelled my brains but could not remember the name.','我绞尽脑汁，也想不起那个名字。'),sources=['https://en.wiktionary.org/wiki/cudgel#English','https://www.etymonline.com/word/cudgel'])
R('A1952','旧工具、小称等后缀与同形结尾汇集，逐词看历史','-EL：有时是旧工具、小称材料，有时只是相似字尾','shovel、swivel 可看旧工具构词；morel、sorrel 等有外语小称路线；gavel、hovel 的常用义不能靠同一后缀包办。',
 '历史构词不等于今天按字母砍开。whirl 的旧形式更长，gavel 木槌与旧赋税同形词分开，hovel 的最早来源也有争议。每个词的实体画面与已知近源更可靠。',
 '日耳曼旧 -el、-le 等与法语小称等材料并非一条现代规则；各词另有缩合、借入、来源未定的情况。',
 [['旧工具、动作与形态名称','shovel · swivel · whirl · cudgel'],['外语小称、旧名借入','morel · sorrel · lapel · lintel'],['仅按常用实义和已知历史对照','gavel · hovel']],
 'gavel 木槌起源未定，不照搬赋税义的 give 构词；hovel 也不确定由房屋词加小称造出。',
 'The visitor swivelled the chair and compared a gavel, a shovel and a cudgel in the display.\n\n参观者转过椅子，对比展柜里的小槌、铲子和棍棒。','shovel swivel whirl cudgel morel sorrel lapel lintel gavel hovel')

Bp=[['back 背 + pack 包 → backpack','背在身上的包，名词也作背包旅行动词'],['backpack + -ing、-er','背包旅行活动；背包旅行者']]
W('backpacking','英 /ˈbækpækɪŋ/；美 /ˈbækpækɪŋ/','背包旅行；携装备徒步露营',
 '把主要行李背在身上，在不同地方走、住，是 backpacking。户外文章常指背装备徒步过夜，城市旅行文章又常指轻装、预算较低的旅行方式。',
 'backpack + -ing，组合活动名。backpack 先由 back + pack 名称形成，也作携背包旅行的动词，两种旅行传统共享背包这个核心物件。',Bp,
 'go backpacking 去背包旅行；a backpacking trip 背包旅程；backpacking equipment 徒步背包装备。',
 'go backpacking；a backpacking trip。',
 'backpacking 不等于每个戴双肩包的通勤动作；通常已经进入旅行、徒步等活动语境。',
 ('They went backpacking through several small towns.','他们背包旅行，经过几个小镇。'),('The article compares equipment for backpacking and day hiking.','文章比较过夜背包徒步与当日徒步所用装备。'))
W('backpacker','英 /ˈbækpækə/；美 /ˈbækpækər/','背包旅行者、背包客',
 'backpacking 是旅行方式，backpacker 是采用这种方式的人。实际可能走山路，也可能在城市间坐车住旅舍，不由一个词保证完全同样的预算、路线。',
 'backpack + -er → backpacker，动作执行者名称。由携带背包的旅行活动发展为常见旅客类型名称，个别地区还可转指服务背包客的旅舍。',Bp[:1]+[['backpack + -er → backpacker','携背包旅行的人，后有相关旅舍转指']],
 'a group of backpackers 一群背包客；a backpacker hostel 背包客旅舍。',
 'a group of backpackers；a backpacker hostel。',
 'backpacker 的重点是旅行方式；tourist 更广泛，不必因为都旅游就认为身份完全一样。',
 ('Several backpackers were waiting at the bus stop.','几位背包客在公交站等车。'),('The hostel welcomed backpackers from many countries.','旅舍接待来自许多国家的背包客。'))
R('B4203','背上的行李成为旅行方式，再命名参与者','BACKPACK：包背在身上，人就能带着行李移动','backpack → backpacking、backpacker，物件、活动、人物依次看。',
 '实体背包提供共同画面，户外露营与城市经济旅行各有传统。装备、行程决定具体活动，不把一个词当作所有人都相同的旅行方案。',
 'back + pack → backpack；-ing 活动，-er 参与者。',
 [['背包、旅行活动与背包客','backpack · backpacking · backpacker']],
 '背着包通勤不一定是 backpacking；backpacker 是活动角色，backpack 是物件。',
 'The backpacker packed her backpack before the backpacking trip.\n\n背包客在背包旅程前收拾好背包。','backpack backpacking backpacker')

if __name__=='__main__':save('continuation_20261030_ob',ROOTS,WORDS)
