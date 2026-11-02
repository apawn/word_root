"""Common reading forms: things, quantities, wording, terms and others."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2939':dict(words=['thing','things'],label='thing → things：东西、事情与情况',note='thing 从古英语议事、事务等意思扩展到事物；How are things? 常问近况。'),
 'B2423':dict(words=['hour','hours'],label='hour → hours：小时、长时间与开放时段',note='hours 的 h 仍不发音；a few hours 是时长，opening hours 是开放时段。'),
 'C0568':dict(words=['hour','hours'],label='hora 词族的英语 hour／hours',note='hour 经法语、拉丁词族接到希腊 hora 一段时间、时节；复数延续现代小时单位等用法。'),
 'B2431':dict(words=['name','names','nickname'],label='name → names：名称与命名、点名',note='names 同时可作名词复数与动词第三人称，name names 是说出具体人名。'),
 'C0842':dict(words=['number','numbers'],label='number → numbers：数字、数量、编号',note='number 名词、动词经相关法语借入路线接拉丁 numerus；numbers 既可说数字、数额，也可说编号、数量达到。'),
 'B2413':dict(words=['word','words'],label='word → words：单词、措辞与口头交锋',note='words 可为多个词，也可在 have words 中说争执；word 动词的第三人称还能说如何措辞。'),
 'B3285':dict(words=['way','ways'],label='way → ways：道路、方法与习惯',note='道路与行事方式的联系很早已存在，复数既可说多条路，也可说多种方法、习惯。'),
 'C1495':dict(words=['term','terms'],label='term → terms：期限、术语、条件与关系',note='term 从边界、尽头发展出期限，以及界定概念、条件等义；on good terms 是关系良好。'),
 'C1211':dict(words=['rule','rules'],label='rule → rules：准则、统治与排除',note='rule 接拉丁 regula 直尺、准则；复数规则与单数主语的管辖、判断动作同写 rules。'),
 'C1404':dict(words=['state','states'],label='state → states：状态、政治单位与陈述',note='state 接拉丁 status 所处状态，后有国家、州与陈述动词等分支；states 在句中可能是名词或动词。'),
 'B2676':dict(words=['other','others'],label='other → others：其他的与其他人、物',note='others 可以自己代替复数人、物，不再在后面直接添同一个被省略的名词；另有 the others 特指其余。'),
}
W('things','/θɪŋz/','东西、事物；事情、情况；thing 的复数',
 '看得见的物件、要处理的事情、最近过得怎样，都能用 things。它很宽，具体意思要靠场景来补。',
 'thing + -s，/ŋ/ 后读 /z/，不另读一个 /ɡ/。thing 接古英语 þing 议事、事务等材料，逐渐扩展为具体、抽象事物。',
 [['古英语 þing → thing','议事、事务 → 事物、东西'],['thing + -s → things','多个事物；也可概括近况、待办事情']],
 'pack your things 收拾物品；things to do 要做的事；How are things? 最近怎样？；all things considered 综合考虑各方面。',
 'a few things；put things in order。','things 很宽泛，物件可按需要改成 items，事情可具体说 tasks、issues。How are things? 是问近况，回答可概括生活、工作情况。',
 ('I have a few things to finish before lunch.','午饭前我有几件事要完成。'),('How are things at your new job?','你新工作的情况怎么样？'),sources=['https://en.wiktionary.org/wiki/things#English','https://en.wiktionary.org/wiki/thing#English'])
W('hours','英 /ˈaʊəz/；美 /ˈaʊərz/','小时〔复数〕；很长时间；工作、开放等时段',
 'a few hours 是几小时；opening hours 是哪段时间开放；I waited for hours 往往在强调等了很久。',
 'hour + -s，h 不发音，结尾读 /z/。hour 经法语、拉丁 hora 接希腊 hora 时间、时节词族，现代以六十分钟的小时义为核心。',
 [['希腊、拉丁、法语时间词 → hour','时节、一段时间 → 小时单位'],['hour + -s → hours','多个小时；常指工作、开放时段等']],
 'two hours 两小时；working hours 工作时间；opening hours 营业、开放时间；office hours 办公、答疑时间等；for hours 长达好几个小时。',
 'a few hours later；outside normal hours。','half an hour 是半小时，two and a half hours 是两个半小时。hours 的首音是元音，沿用 hour 不发 h 的读法。',
 ('The journey took almost four hours.','这段旅程花了差不多四小时。'),('Please check the museum’s opening hours before you visit.','参观前请查看博物馆的开放时间。'),sources=['https://en.wiktionary.org/wiki/hours#English','https://en.wiktionary.org/wiki/hour#English'])
W('names','/neɪmz/','名字、名称〔复数〕；命名、点名、任命〔name 的第三人称单数〕',
 '名单上的名字是 names；公告把某人明确点出来，或宣布某人担任某职，name 也能作动词，单数主语后写 names。',
 'name 已有 e，直接加 s，/m/ 后读 /z/。name 接古英语 nama、noma 等名称词及相关命名动词，名词、动词形式现代相同。',
 [['古英语名称、命名词 → name','名字、称呼；给出名称'],['name + -s → names','多个名字；单数主语说出名字、命名等']],
 'first names 名；family names 姓；place names 地名；name names 说出具体人名；names a winner 指定、宣布获胜者。',
 'a list of names；remember people’s names。','names 是复数；name’s 可是单数所有格，也可能是 name is 的缩写，靠句子判断。name names 的第二个 names 是名词复数。',
 ('I am better at remembering faces than names.','我记脸比记名字更在行。'),('The final paragraph names the people who helped.','最后一段列出了提供帮助的人。'),sources=['https://en.wiktionary.org/wiki/names#English','https://en.wiktionary.org/wiki/name#English'])
W('numbers','英 /ˈnʌmbəz/；美 /ˈnʌmbərz/','数字、数目、数量；编号、期号；曲目、节目；编号、总数达到〔动词形式〕',
 '数字用来数多少，也用来给车、门、杂志或节目排顺序，因此 numbers 能说数字本身、数量，也能说按编号排出的项目。',
 'number + -s，词尾读 /z/。名词经法语 nombre 接拉丁 numerus 数，动词也有相关法语借入支线；编号、数目与按编号列出的项目形成不同现代义项。',
 [['拉丁 numerus → 法语相关形式 → number','数、数目；编号、计算'],['number + -s → numbers','多个数字、编号项目；单数主语编号或数量达到']],
 'large numbers of people 大量人；phone numbers 电话号码；the latest numbers 最新数据、数目；musical numbers 音乐节目、曲目；numbers two hundred 总数为两百。',
 'in large numbers；the numbers on the page。','a number of 后常接复数名词，表示一些、许多；the number of 强调数目本身。numbers 的具体义由统计、通讯、演出等语境决定。',
 ('Write the numbers in the correct order.','把这些数字按正确顺序写出来。'),('The club now numbers over a hundred members.','这个俱乐部现在有一百多位成员。'),('The show includes three musical numbers.','这场演出包括三个音乐节目。'),sources=['https://en.wiktionary.org/wiki/numbers#English','https://en.wiktionary.org/wiki/number#English'])
W('words','英 /wɜːdz/；美 /wɜːrdz/','单词；话语、措辞；歌词；措辞、表述〔word 的第三人称单数〕',
 '一个个词连成话；words 可以说词本身，也可以概括说出口或写下来的内容。怎样把同一个意思说出来，是措辞。',
 'word + -s，/d/ 后读 /z/。word 继承古英语同形词，言语、承诺、表达内容等义较早就有；动词 word 是用词语表述。',
 [['古英语 word → word','词、言语、表达内容'],['word 名词、动词 + -s → words','多个词、话语、歌词；单数主语安排措辞']],
 'in other words 换句话说；the words of a song 歌词；a few kind words 几句好话；have words with someone 与某人争执；words the request carefully 谨慎措辞提出请求。',
 'choose your words；put it into words。','have a word with someone 常是跟某人谈几句，have words with someone 则常有争执的意思。a 的有无和固定搭配一起影响含义。',
 ('I know the tune, but I cannot remember the words.','我记得曲调，却想不起歌词。'),('She words the request carefully so that everyone understands it.','她仔细斟酌请求的措辞，让每个人都能理解。'),sources=['https://en.wiktionary.org/wiki/words#English','https://en.wiktionary.org/wiki/word#English'])
W('ways','/weɪz/','方法、方式；道路、方向；习惯、作风；way 的复数',
 '到目的地可以走不同的路，解决问题也可以走不同的路。ways 把实际路线和做事方法用同一个画面串起来。',
 'way + -s，元音后读 /z/。way 接古英语 weg 道路、路线、行事方式等词；道路到方式的联系很早存在，现代复数按语境数路线、办法、习惯。',
 [['古英语 weg → way','路、路线；行事方式'],['way + -s → ways','多条路线、多种方法或习惯']],
 'different ways 不同方法；ways to improve 改进办法；ways of working 工作方式；in many ways 在许多方面；change your ways 改变行事习惯。',
 'two ways of doing it；in some ways。','a way to do 与 a way of doing 都可表示做事方式。in many ways 是在许多方面，by the way 另是顺便说一句的固定结构。',
 ('There are several ways to solve this problem.','这个问题有几种解决办法。'),('In many ways, the smaller office works better for us.','从许多方面看，小办公室反而更适合我们。'),sources=['https://en.wiktionary.org/wiki/ways#English','https://en.wiktionary.org/wiki/way#English'])
W('terms','英 /tɜːmz/；美 /tɜːrmz/','术语；期限、任期、学期；条件、条款；关系；term 的复数等',
 '先用边界、界定来想：时间可以划出一段任期，概念可以用一个术语界定，合作也可以定下双方接受的条件。',
 'term + -s，词尾读 /z/。term 经法语 terme 接拉丁 terminus 边界、尽头，期限、术语、条件等用法沿不同语境发展；现代 terms 还出现在关系、表达方式等固定搭配中。',
 [['拉丁 terminus → 法语 terme → term','边界、尽头 → 期限；界定的概念与条件'],['term + -s → terms','多个期限、术语、条件等；固定搭配另看']],
 'technical terms 技术术语；school terms 学期；terms and conditions 条件、条款；on good terms 关系良好；in simple terms 用简单的话；in terms of ... 从……方面来说。',
 'come to terms with ...；explain in ordinary terms。','in terms of 常引出衡量角度；in simple terms 说用简单措辞。come to terms with 常说逐渐接受、适应某事实，不能逐字只译成来到条件。',
 ('The guide explains the technical terms in simple language.','指南用简单语言解释了技术术语。'),('The two neighbours are on good terms.','这两位邻居关系很好。'),sources=['https://en.wiktionary.org/wiki/terms#English','https://en.wiktionary.org/wiki/term#English'])
W('rules','/ruːlz/','规则、准则〔复数〕；统治、管辖、裁定等〔rule 的第三人称单数〕',
 '指导大家怎样做的一条条标准是 rules。rule 作动词则可以说掌控、裁定；rules out 常是把某种可能排除。',
 'rule + -s，/l/ 后读 /z/。名词经法语接拉丁 regula 直尺、准则；动词经相关法语、拉丁规范动词传入，两条借入路径相连而不完全相同。',
 [['拉丁 regula、regulare → 法语 → rule','直尺、准则；规范、管理'],['rule 名词、动词 + -s → rules','多个准则；单数主语管辖、裁定等']],
 'follow the rules 遵守规则；rules of a game 游戏规则；rules out a possibility 排除一种可能；rules in favour of ... 作出有利于……的裁决。',
 'clear rules；rules out that option。','rules 作名词时是一条条标准，作动词时要看后面的对象和小词。rule out 的排除义是整组搭配，不把 out 直接当作走出去。',
 ('The rules are simple and easy to remember.','规则很简单，也容易记。'),('The room’s small size rules out a large table.','房间太小，放大桌子的方案行不通。'),sources=['https://en.wiktionary.org/wiki/rules#English','https://en.wiktionary.org/wiki/rule#English'])
W('states','/steɪts/','状态；国家、州等政治单位〔复数〕；陈述、说明〔state 的第三人称单数〕',
 '物体处在什么样子，是 state；一套有组织的政治单位也发展出 state 的名称。动词 state 则是把内容明确说出来。',
 'state 已有 e，加 s，词尾 /t/ 后读 /s/。state 经法语、拉丁 status 所处状态、地位等材料进入英语，状态、政治单位和正式说明是不同现代分支。',
 [['拉丁 status → 法语 → state','所处状态、地位；后来有政治单位与陈述义'],['state 名词、动词 + -s → states','多个状态、政治单位；单数主语陈述']],
 'different states 不同状态、州等；solid and liquid states 固态和液态；member states 成员国；states that ... 说明……；clearly states 明确写明。',
 'the states in the region；states the purpose。','states 后接 that 从句时常是说明、写明的动词。名词 states 的状态、国家、州要根据材料、国际组织、行政区等语境判断。',
 ('The notice states that the doors close at six.','告示写明，门六点关闭。'),('The report compares several states in the region.','报告比较了该地区的几个州。'),sources=['https://en.wiktionary.org/wiki/states#English','https://en.wiktionary.org/wiki/state#English'])
W('others','英 /ˈʌðəz/；美 /ˈʌðərz/','其他人、其他事物；其余的人或物〔the others〕',
 '先有一部分，再把剩下或另外的部分指给对方看，others 可以直接代替这些人、东西，不必重复名词。',
 'other + -s，形成代指复数人、物的形式。other 接古英语 ōþer，较早也有第二的意思；现代 others 按上下文指另外的人、物。',
 [['古英语 ōþer → other','另一个、别的；较早也可说第二'],['other + -s → others','代替复数人、物；the others 常指特定其余部分']],
 'help others 帮助别人；some ... others ... 有些……另一些……；the others 其余的那些；others’ opinions 别人的意见。',
 'learn from others；some prefer tea, others coffee。','保留名词时用 other people、other students；others 已代替复数名词。some others 可以是不特定的另外一些，the others 常是已知范围内余下的那些。',
 ('Some people preferred walking; others took the bus.','有些人喜欢步行，另一些人坐了公交车。'),('I have read two of the letters; the others are still unopened.','这些信我读了两封，其余的还没拆。'),sources=['https://en.wiktionary.org/wiki/others#English','https://en.wiktionary.org/wiki/other#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vz',ROOTS,WORDS)
 extend_lessons()
