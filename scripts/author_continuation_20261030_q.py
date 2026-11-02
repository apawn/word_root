"""Got and gone: familiar forms with useful modern extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
GE=[['古诺尔斯语 geta → 中古英语 geten → get','得到、取得'],['get → got／gotten','保留不规则过去式与分词形式']]
W('got','英 /ɡɒt/；美 /ɡɑːt/','get 的过去式、过去分词；有、必须〔固定构式〕',
 '昨天拿到了、刚弄明白了，都可以用 got；但 I’ve got 还常只是说我现在有。',
 'get 的不规则词形，经中古英语形式发展。get 借古诺尔斯语；have got 与 have got to 在英语使用中形成固定表达。',GE,
 'I got your message 收到消息，I’ve got a question 我有个问题，I’ve got to go 我得走。Got it! 常表示懂了、记住了。',
 'got a message；have got；have got to；Got it!。',
 'I got a car 常说弄到一辆车，I’ve got a car 常说现在有车；过去时间看整句，不因 got 就把所有 have got 都译成过去有。',
 ('I got your message this morning.','我今天早上收到你的消息了。'),('I have got to leave before six.','我必须在六点前离开。'))
W('gotten','英 /ˈɡɒtn/；美 /ˈɡɑːtən/','get 的过去分词〔尤美式〕；得到的',
 '强调事情已经发生了变化：拿到了、变好了、学会了；美式常保留这个带 -en 的分词。',
 '接 get 的历史分词形式；现代美式常用 gotten 表获得、变得等，英式通常用 got。不是 got 另加一个表示让它变成的动词后缀。',GE+[['历史分词 → gotten','美式保留常见分词形式，具体分布与 got 有别']],
 'has gotten better 已变好，have gotten a job 已找到工作。美式 have got 表有、have got to 表必须时，不能简单全换 gotten。',
 'has gotten better；have gotten a job；has gotten used to。',
 'has got a car 常说拥有；has gotten a car 美式常强调弄到车。两者在实际语境还要看 get 所接的补语。',
 ('The weather has gotten much colder.','天气冷了很多。'),('She has gotten used to the new schedule.','她已经习惯了新作息。'))
W('gotcha','英 /ˈɡɒtʃə/；美 /ˈɡɑːtʃə/','懂了；抓到你了；陷阱、容易踩的坑〔口语〕',
 '听懂对方时说“明白”；抓住对方破绽时说“逮到你了”。名词又可指让人措手不及的小坑。',
 'got you 连读的口语拼写，/t/ 与后面 /j/ 相接可形成 /tʃ/。you 的弱化在这里写成 -cha，不是普遍词根后缀。',GE+[['got you 连读 → gotcha','抓住你、听懂你 → 口语应答及陷阱名词']],
 'Gotcha! 可以应答明白或开玩笑揭穿。a gotcha in the instructions 是说明里容易忽略、导致出错的点，技术讨论里也常见。',
 'Gotcha!；a common gotcha；watch out for this gotcha。',
 'gotcha 语气很口语，正式说明可用 hidden problem、pitfall。对方说 Gotcha 要听语境，可能理解了，也可能在捉弄。',
 ('“Turn left at the bridge.” “Gotcha.”','“到桥那里左转。”“明白。”'),('There is one gotcha: the file name is case-sensitive.','有一个容易踩的坑：文件名区分大小写。'))
R('B2869','得到、理解与口语连读','GOT：先看原动词 GET，再分 got 与 gotten','get 已精讲共享，got → gotten → gotcha 相邻，避免把词形变化当新词根。',
 'get 是斯堪的纳维亚借词，got/gotten 保留历史变化。固定 have got 的现代含义需按整个结构讲。',
 'get → got／gotten；got + you 连读 → gotcha。',
 [['原形与不规则形式','get · got · gotten'],['连读与现代口语','gotcha']],
 'have got 现在有，have got to 必须；gotten 尤美式获、变分词；gotcha 多种语气。',
 'I’ve got your message, and I’ve gotten used to the new plan.\n\n我收到你的消息了，也已经习惯了新计划。',
 'get got gotten gotcha')
GO=[['古英语 gān、ġegān → 中古英语 gon → gone','走、已经走了的分词'],['现代 gone','已经离开 → 没了、过去了、用完了']]
W('gone','英 /ɡɒn/；美 /ɡɔːn/ 或 /ɡɑːn/','go 的过去分词；离开的；没了的、用完的',
 '人已经走出门，蛋糕已经被吃完，机会已经过去：都抓住原来在、现在不在。',
 '接 go 的历史过去分词，经古英语、中古英语延续。go—went—gone 中 went 是另一个动词历史词形被借来用，不把它硬按 go 加尾巴解释。',GO,
 'has gone home 已经回家，The milk is gone 牛奶没了，gone days 不是常规搭配，通常说 days gone by。',
 'has gone home；all gone；long gone；days gone by。',
 'has gone to 通常强调去了尚未回来，has been to 通常强调去过的经历；仅用 gone 不等于所有场景的死亡。',
 ('By the time we arrived, the guests had gone.','我们到时，客人已经走了。'),('There is no bread left—it is all gone.','面包一点不剩，全没了。'))
W('ago','英 /əˈɡəʊ/；美 /əˈɡoʊ/','以前；距现在若干时间前',
 '从现在往回数：三天前，就是有三天已经走过去了。',
 '来自中古英语 agon 已过去的缩短形式，原是旧动词 agon 的分词，上接古英语 āgān 走开、过去。与 go/gone 同族，不是现代 gone 随便删掉末尾。',
 [['古英语 āgān → 中古英语 agon〔旧动词〕','走开、过去'],['其分词 agon → ago','已过去 → 距现在一段时间前']],
 'three days ago 三天前，long ago 很久以前；通常放时间长度后，从说话的现在往回数。',
 'two years ago；a moment ago；long ago。',
 'ago 通常以现在为参照，before 可以以过去某个时间为参照。I met her two days ago 通常用一般过去时。',
 ('I sent the email ten minutes ago.','我十分钟前发了邮件。'),('The bridge was built more than a century ago.','这座桥建于一个多世纪以前。'),sources=['https://www.etymonline.com/word/ago','https://en.wiktionary.org/wiki/ago#English'])
W('bygone','英 /ˈbaɪɡɒn/；美 /ˈbaɪɡɔːn/ 或 /ˈbaɪɡɑːn/','过去的、往昔的；过去的事〔常复数〕',
 '时间已经从身边走过去，留下一个回头看的旧时代。',
 'by 经过 + gone，连接 go by 过去、流逝的画面。名词 bygones 常用于不再计较旧事的表达。',GO+[['by + gone → bygone','已经流逝 → 往昔的、过去的事']],
 'a bygone era 过去的时代，bygone days 往日；let bygones be bygones 过去的事就让它过去，常用于结束旧怨。',
 'a bygone era；bygone days；let bygones be bygones。',
 'bygone 常带回顾旧时代的色彩，previous 只是顺序上的之前；bygone 不是某件东西被买走。',
 ('The old station is a reminder of a bygone era.','旧车站让人想起一个过去的时代。'),('They agreed to let bygones be bygones and work together again.','他们同意不再计较旧事，重新合作。'))
W('goner','英 /ˈɡɒnə/；美 /ˈɡɔːnər/ 或 /ˈɡɑːnər/','完了的人或东西；无望挽救者〔口语〕',
 '已经没救、撑不住了，口语夸张地说“这下完了”。可以说人，也可以说坏掉的机器。',
 'gone + -er，形成处于完了状态的人或物的名词。不是所有 -er 都只表示主动做事者。',GO+[['gone + -er → goner','已经完了 → 无望挽救的人或物']],
 'be a goner 基本完了，I thought I was a goner 我以为自己完蛋了。常带夸张，不必都理解成真的死亡。',
 'be a goner；think someone is a goner；a complete goner。',
 'gone 可直接作状态补语，goner 是可数名词：The phone is a goner。正式技术报告宜具体说明故障。',
 ('After the fall, I thought my phone was a goner.','手机摔下去后，我以为它彻底报废了。'),('When the huge wave hit, he thought he was a goner.','巨浪袭来时，他以为自己完了。'))
R('B2870','走了、没了与时间过去','GONE：原来在，现在已经离开或过去','go 已有精讲，接 gone；时间分支 ago、bygone，再看口语 goner。',
 'gone 是 go 的旧分词。ago 来自旧动词的分词缩短，bygone 接已经过去的画面，goner 是完了者的口语命名。',
 'go → went／gone；旧 āgān → agon 分词 → ago；by + gone；gone + -er。',
 [['原动词与离开状态','go · gone'],['过去时间与时代','ago · bygone'],['口语完了者','goner']],
 'gone to 去而未返、been to 去过常有差别；ago 通常参照现在；goner 可比喻坏掉的物件。',
 'The old machines are gone, but photographs preserve that bygone era.\n\n旧机器已经不在了，照片却留住了那个过去的时代。',
 'go gone ago bygone goner')
if __name__=='__main__':save('continuation_20261030_q',ROOTS,WORDS)
