"""Common expression and narrative forms, with noun/verb distinctions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0713':dict(words=['mean','meant'],label='mean → meant：表示与本来打算',note='meant 接表示、打算的动词 mean；平均的、刻薄的 mean 有不同历史。'),
 'B2746':dict(words=['talk','talks','talked'],label='talk → talks → talked：谈话、商谈与谈过',note='talks 的谈判义可由多方正式谈话理解。'),
 'B2745':dict(words=['think','thinks'],label='think → thinks：想、认为与考虑',note='思考过程、判断意见和考虑对象的连接方式不同。'),
 'B2583':dict(words=['write','writes'],label='write → writes：写下与写信',note='古英语刻划的动作发展到留下文字、创作。'),
 'B2879':dict(words=['hold','holds'],label='hold → holds：抓住、容纳与持续有效',note='从把东西稳住，理解保持位置、装得下及说法成立。'),
 'B3100':dict(words=['arrive','arrived','arriving'],label='arrive → arrived → arriving：到达与正在到来',note='到岸的历史画面扩展到一般到达；-ing 形式去末尾不发音 e。'),
 'C0503':dict(words=['agree','agrees'],label='agree → agrees：意见相合与同意请求',note='同意某人、同意内容和答应做事使用不同连接方式。'),
 'C1635':dict(words=['provide','provides'],label='provide → provides：事先考虑到并备好所需',note='借词背后有向前看、预先照顾的历史，现代常用义是提供。'),
 'C1487':dict(words=['continue','continues'],label='continue → continues：让事情接着进行',note='保持连在一起的早期词族，发展为时间上连续不断。'),
 'B3326':dict(words=['movie','movies'],label='movie → movies：活动影像与电影',note='moving picture 的缩短及 -ie 形成 movie，再加 s 为 movies。'),
 'A1862':dict(words=['character','characters'],label='character → characters：特点、人物与文字符号',note='刻出的印记、区别标记，发展出事物特征与可辨认人物等义。'),
 'B4061':dict(words=['lot','lots'],label='lot → lots：份额、批次与许多',note='抽签与分得的份额相连，后来有批、地块及固定数量表达。'),
}
W('meant','/ment/','表示、意味着；本来打算、意在；mean 的过去式和过去分词',
 '回头解释一句话想表达什么、一个人当时打算做什么，常用 meant；结果带来了什么，也能说 meant。',
 'mean 的不规则过去式、过去分词，元音由 /iː/ 变为 /e/，结尾为 /t/。这个动词接古英语 mǣnan 的意指、打算；“平均的”和“刻薄的”mean 属于其他历史来源。',
 [['古英语 mǣnan → 中古英语 menen → mean','意指、打算'],['mean 的过去式、过去分词 → meant','过去表示、打算；事情所意味着的']],
 'meant to call 本来打算打电话；meant well 本意是好的；meant a lot 意义很大；was meant for you 原本是给你的。',
 'what she meant；never meant to hurt anyone。','meant to do 看本来打算做什么；meant doing 看某事意味着必须做什么。I meant to wait 是本打算等，It meant waiting 是这就意味着得等。',
 ('I meant to call you, but I left my phone at home.','我本来打算给你打电话，但把手机落在家里了。'),('Missing the bus meant walking the last two kilometres.','没赶上巴士，就意味着最后两公里得走过去。'),sources=['https://en.wiktionary.org/wiki/meant#English','https://en.wiktionary.org/wiki/mean#English'])
W('talks','英 /tɔːks/；美 /tɔːks, tɑːks/','说话、交谈；谈话、演讲；正式商谈、谈判〔复数〕',
 '嘴里把想法说出来，是动词 talks；一场场谈话、分享，或为解决问题而进行的多轮商谈，是名词 talks。',
 'talk + -s，/k/ 后读 /s/，常见标准读音中 l 不单独发音。talk 接中古英语 talken、talkien，较早关联讲述、叙说词族；不能把 tell + k 当现代构词规则。',
 [['中古英语 talken、talkien 等 → talk','说、谈话'],['talk + -s → talks','单数主语交谈；多场谈话、商谈']],
 'talks about work 谈工作；talks to a neighbour 和邻居说话；peace talks 和谈；gives talks 作演讲。',
 'talks with the team；a series of talks。','名词 talks 说谈判时，常表示双方或多方正式商谈；单数 a talk 常说一次谈话或演讲。talk to、talk with 都能表达与人说话，语境决定互动侧重。',
 ('She talks to her sister on the phone every evening.','她每天晚上和姐姐通电话。'),('The two teams held talks about sharing the building.','两个团队就共用这栋楼进行了商谈。'),sources=['https://en.wiktionary.org/wiki/talks#English','https://en.wiktionary.org/wiki/talk#English'])
W('talked','英 /tɔːkt/；美 /tɔːkt, tɑːkt/','交谈过；谈到过；说服过；talk 的过去式和过去分词',
 '谈话已经发生过，是 talked；后面再接 about、into、out of 等，可以交代谈了什么、把人说动去做什么。',
 'talk + -ed，原词以 /k/ 结尾，过去词尾读 /t/，不增加音节。talk 的历史接中古英语 talken、talkien 的说话词族。',
 [['中古英语 talken、talkien 等 → talk','谈话、说'],['talk + -ed → talked','谈过、说过；相应说服结构的过去形式']],
 'talked about the plan 谈过计划；talked for hours 聊了几小时；talked me into joining 说服我加入；talked him out of leaving 劝他别走。',
 'have talked before；talked things through。','talked me into doing 是把我说动去做；talked me out of doing 是把我劝得不去做。talked to me 本身只交代跟我说过话。',
 ('We talked about the trip over lunch.','我们吃午饭时聊了那次旅行。'),('She talked me into trying the new route.','她说服我试试那条新路线。'),sources=['https://en.wiktionary.org/wiki/talked#English','https://en.wiktionary.org/wiki/talk#English'])
W('thinks','/θɪŋks/','想；认为；考虑；think 的第三人称单数',
 '脑子围着一件事转、形成一个判断，就是 thinks。后面接的内容会告诉你：是在思考，还是已经有了看法。',
 'think + -s，/k/ 后词尾读 /s/。think 主要接古英语 þencan 的思考义，中古英语又与相关的 þyncan 显得一系发生形式汇合；现代过去式是 thought。',
 [['古英语 þencan 等 → 中古英语相关形式 → think','思考；认为'],['think + -s → thinks','单数主语想、认为、考虑']],
 'thinks about the problem 考虑问题；thinks of a solution 想出办法；thinks it is useful 认为它有用；thinks highly of her 对她评价很高。',
 'thinks carefully；thinks before speaking。','think about 常表示把注意力放在某事上考虑；think of 在想起、想到办法等语境常见，两者也有重合。thinks that ... 后面直接接一个判断。',
 ('She thinks the second design is easier to use.','她认为第二个设计更容易使用。'),('He always thinks carefully before making a promise.','他作出承诺前总会认真考虑。'),sources=['https://en.wiktionary.org/wiki/thinks#English','https://en.wiktionary.org/wiki/think#English'])
W('writes','/raɪts/','写；写信；创作；write 的第三人称单数',
 '把话、想法留下可读的痕迹，就是 writes；写几行字、写信、写整本书都沿用这个动作。',
 'write + -s，/t/ 后读 /s/，开头 w 不发音。write 继承古英语 wrītan，早与刻划、划出痕迹有关，经中古英语 writen 延续。',
 [['古英语 wrītan → 中古英语 writen → write','刻划、留下文字 → 写作'],['write + -s → writes','单数主语写、创作或写信']],
 'writes stories 写故事；writes to a friend 给朋友写信；writes down the number 记下号码；writes for a magazine 为杂志撰稿。',
 'writes clearly；writes in a notebook。','writes /raɪts/ 与 rights 权利、rites 仪式同音。writes down 强调把信息记下来，writes back 强调回复来信、消息。',
 ('She writes down every new word in a small notebook.','她把每个生词都记在一个小笔记本里。'),('He writes short stories about life in the village.','他写关于乡村生活的短篇小说。'),sources=['https://en.wiktionary.org/wiki/writes#English','https://en.wiktionary.org/wiki/write#English'])
W('holds','英 /həʊldz/；美 /hoʊldz/','拿着、保持；容纳；举行；成立、有效；握持处〔复数〕',
 '把东西稳稳留在原处，是 holds；把人或物装得下、让某种状态维持住，也可以借这个画面理解。',
 'hold + -s，/d/ 后读 /z/。主要动词继承古英语 healdan，经中古英语 holden；过去式和分词是 held。船的货舱名词 hold 有与 hole 相关的不同历史，遇到 cargo holds 应另认来源。',
 [['古英语 healdan → hold','握住、维持；容纳等'],['hold + -s → holds','单数主语拿、保持、装得下；握持处等复数']],
 'holds the door open 扶着门让它开着；holds fifty people 能容纳五十人；holds a meeting 开会；the rule still holds 这条规则仍成立。',
 'holds her attention；holds the record。','holds water 字面是盛得住水，常比喻说法经得起推敲。攀岩的 handholds、holds 则是可以抓握、踩踏的位置；具体名词义由场景判断。',
 ('The small theatre holds about a hundred people.','这家小剧院能容纳大约一百人。'),('The same explanation still holds in this case.','在这种情况下，同一个解释仍然成立。'),sources=['https://en.wiktionary.org/wiki/holds#English','https://en.wiktionary.org/wiki/hold#English'])
W('arrived','/əˈraɪvd/','已经到达；已经出现、来到；arrive 的过去式和过去分词',
 '人走完一段路来到目的地，或者等待的时刻终于到了，都可以说 arrived。',
 'arrive 去末尾 e，加完整 -ed → arrived，词尾读 /d/。arrive 经法语 ariver 接“到岸”的历史词族，较早拉丁形式常重建为 *arrīpāre，由 ad- 向与 rīpa 岸构成。星号表示重建形式。',
 [['较早拉丁到岸词族 → 法语 ariver → arrive','到岸 → 一般到达'],['arrive 去 e + -ed → arrived','到达已发生；已经来到']],
 'arrived at the station 到了车站；arrived in town 到了镇上；the parcel has arrived 包裹到了；the moment has arrived 时刻已经到来。',
 'arrived safely；has finally arrived。','arrive at 常接站点、建筑等具体到达点，arrive in 常接城市、国家等区域；arrive home、arrive here 通常直接连接。arrive at a conclusion 是经过思考得出结论。',
 ('We arrived at the station just before noon.','我们在快到中午时到达了车站。'),('The moment we had been waiting for had finally arrived.','我们一直等待的时刻终于到了。'),sources=['https://en.wiktionary.org/wiki/arrived#English','https://en.wiktionary.org/wiki/arrive#English'])
W('arriving','/əˈraɪvɪŋ/','正在到达；即将到来；arrive 的 -ing 形式',
 '把注意力放到抵达这一过程或将到的安排上，就是 arriving；既能说正在进站，也能说按安排明天抵达。',
 'arrive 去掉末尾不发音 e，再加 -ing → arriving。词基经法语接早期到岸词族，现代已经扩展到各种交通、人物、事物的到达。',
 [['到岸词族 → 法语 ariver → 英语 arrive','到岸 → 到达目的地'],['arrive 去 e + -ing → arriving','到达过程；按安排即将到来']],
 'arriving passengers 抵达的旅客；arriving late 迟到；arriving tomorrow 明天到；on arriving 一到达。',
 'the next train arriving；thanks for arriving early。','is arriving tomorrow 可以用现在进行结构说安排好的将来。on arriving 后可接 at 或 in，再交代地点；这里 arriving 把到达当作一件事来表达。',
 ('The next train is arriving at platform two.','下一班列车正在驶入二号站台。'),('On arriving home, she put the flowers in water.','一到家，她就把花放进水里。'),sources=['https://en.wiktionary.org/wiki/arriving#English','https://en.wiktionary.org/wiki/arrive#English'])
W('agrees','/əˈɡriːz/','同意；意见一致；相符；agree 的第三人称单数',
 '两边的想法合得上，或者一方接受了提议，就是 agrees；数字、描述对得上，也能用这个词。',
 'agree + -s，元音后读 /z/。agree 经古法语 agreer，与 a gré 合心意相关，远接拉丁 grātum 的令人满意、可喜等义。',
 [['拉丁 grātum → 古法语 a gré、agreer → agree','合心意 → 同意、相合'],['agree + -s → agrees','单数主语同意；与另一方相符']],
 'agrees with me 同意我的看法；agrees to help 答应帮忙；agrees to the change 接受变化；agrees with the record 与记录相符。',
 'everyone agrees；agrees on the date。','agree with someone 表示意见相同；agree to a proposal 表示接受提议；agree on a date 表示就日期达成一致。agrees with 在数字、描述语境也可以说相符合。',
 ('She agrees with your explanation.','她同意你的解释。'),('The number on the box agrees with the number on the receipt.','盒子上的号码与收据上的号码一致。'),sources=['https://en.wiktionary.org/wiki/agrees#English','https://en.wiktionary.org/wiki/agree#English'])
W('provides','/prəˈvaɪdz/','提供；使具备；规定；provide 的第三人称单数',
 '把别人需要的东西准备、拿出来，让对方能够使用，就是 provides。正式文件也可以把可做什么、须满足什么事先规定好。',
 'provide + -s，/d/ 后读 /z/。provide 借拉丁 prōvidēre，历史是 prō- 向前与 vidēre 看，先有预见、预先照顾的联系，再发展到备好所需、提供。',
 [['拉丁 prō- + vidēre → prōvidēre → provide','向前看 → 预先照顾、备好'],['provide + -s → provides','单数主语提供；正式条文规定']],
 'provides information 提供信息；provides food for guests 为客人提供食物；provides someone with a map 给某人提供地图；provides that ... 规定……。',
 'provides a clear view；provides for future needs。','provide someone with something 与 provide something for someone 都常用。provides that 在法律、正式条文中可表示规定；provided that 另可作“只要、如果”理解。',
 ('The library provides a quiet place to study.','图书馆提供了一个安静的学习场所。'),('The guide provides visitors with a map of the gardens.','向导给游客提供了一张花园地图。'),sources=['https://en.wiktionary.org/wiki/provides#English','https://en.wiktionary.org/wiki/provide#English'])
W('continues','/kənˈtɪnjuːz/','继续；持续；接着延伸；continue 的第三人称单数',
 '前面的事情还没断，接着往下发生，就是 continues；一条路继续延伸，也可以这样说。',
 'continue + -s，元音后读 /z/。continue 经古法语 continuer 接拉丁 continuāre，与 continuus 连在一起的相关，更早联系 continēre 保持在一起。',
 [['拉丁连续词族 → 古法语 continuer → continue','保持相连 → 持续、继续'],['continue + -s → continues','单数主语接着进行、延伸']],
 'continues to grow 继续增长；continues working 继续工作；the road continues 路继续延伸；the story continues 故事仍在继续。',
 'continues for several hours；continues into the next room。','continues to do 与 continues doing 都常表示继续做。continues 后不接对象时，主语本身就是持续的事情；接 road、line 等主语可说空间延伸。',
 ('The path continues beyond the last house.','小路过了最后一所房子还继续向前延伸。'),('She continues to practise even after the lesson ends.','下课后，她仍继续练习。'),sources=['https://en.wiktionary.org/wiki/continues#English','https://en.wiktionary.org/wiki/continue#English'])
W('movies','/ˈmuːviz/','电影；电影业、电影放映场所〔特定表达〕；movie 的复数',
 '一幅幅会动的画面组成电影；一部部电影就是 movies，go to the movies 则是日常说去看电影。',
 'movie + -s，元音后读 /z/，末尾写 ie，不变成 ies。movie 由 moving picture 中的 moving 缩短并加昵称式 -ie 形成，起初在美式英语中常见。',
 [['moving picture','会动的影像 → 电影'],['moving 缩短 + -ie → movie；movie + -s → movies','一部电影 → 多部电影；看电影的相关表达']],
 'watch movies 看电影；silent movies 无声电影；go to the movies 去看电影；in the movies 在电影业、在电影中。',
 'a collection of old movies；movies based on novels。','movie 与 film 都可说电影，使用习惯随地区、语境变化。movies 的词尾原本是 ie 加 s；studies 则是 study 把 y 变 i 后加 es。',
 ('We watched two old movies on the rainy afternoon.','下雨的那个下午，我们看了两部老电影。'),('Would you like to go to the movies after dinner?','晚饭后你想去看电影吗？'),sources=['https://en.wiktionary.org/wiki/movies#English','https://en.wiktionary.org/wiki/movie#English'])
W('characters','英 /ˈkærəktəz/；美 /ˈkærəktərz/','人物、角色；字符；性格、特质〔复数〕',
 '能让一个人、一件事显出自己特点的印记，是理解 character 的起点；故事里有特点的人物、书写中可辨认的符号，都在这个词里。',
 'character + -s，读 /z/。character 经法语、拉丁语接希腊 kharaktḗr 刻印工具、印记，关联 kharássein 刻写；标记引出特征、个性、符号等多条意义。',
 [['希腊刻写词族 → 拉丁、法语 → character','刻出的印记 → 区别特征、文字标记等'],['character + -s → characters','多个人物、多个字符或不同特质']],
 'main characters 主要人物；Chinese characters 汉字；special characters 特殊字符；people of different characters 性格各异的人。',
 'create memorable characters；a password of twelve characters。','characters 可以是 letters 字母、digits 数字或其他符号的总称。故事人物不必是人类，动物、幻想生物也可成为 characters。性格这个整体概念常用单数或不可数结构。',
 ('The story has only three main characters.','这个故事只有三个主要人物。'),('The name must contain fewer than twenty characters.','名称必须少于二十个字符。'),sources=['https://en.wiktionary.org/wiki/characters#English','https://en.wiktionary.org/wiki/character#English'])
W('lots','英 /lɒts/；美 /lɑːts/','许多〔lots of〕；批次、份额、地块；签〔复数〕',
 '原来用抽签分配份额，分出来的一份、一个批次是 lot；后来 lots of 成为很常见的“许多”表达。',
 'lot + -s，/t/ 后读 /s/。lot 继承古英语 hlot 的签、抽签、份额等义；抽签决定份额与分配结果相连，后来有批次、地块及数量表达。',
 [['古英语 hlot → lot','签、抽签 → 份额、批次等'],['lot + -s → lots；lots of','多份、多批、地块；许多']],
 'lots of people 许多人；lots of time 许多时间；parking lots 停车场；draw lots 抽签；auction lots 拍卖批次。',
 'thanks a lot／thanks lots〔后者较口语〕；sell in separate lots。','lots of 可接可数复数或不可数名词：lots of books、lots of water。动词随后面的主要对象：Lots of people are here，Lots of time is needed。',
 ('We have lots of time before the train leaves.','离火车发车还早，我们时间很充裕。'),('The furniture was sold in separate lots.','这些家具分成不同批次出售。'),sources=['https://en.wiktionary.org/wiki/lots#English','https://en.wiktionary.org/wiki/lot#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xk',ROOTS,WORDS)
 extend_lessons()
