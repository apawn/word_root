"""Cooking actions and common condiments, with literal-to-figurative links."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3557':dict(words='stew stews stewed stewing'.split(),label='stew：热、蒸汽与慢炖；另有焦虑比喻',note='stew 经法语 estuver 等热浴、焖炖材料借入，更远来源不确定；和 stove 的旧暖房、浴室义可能有关，但不能断定现代 stew 直接从 stove 删字母。炖菜名词、焦虑比喻各有用法发展。'),
 'B2996':dict(words='whisk whisks whisked whisking'.split(),label='whisk：快速扫动 → 搅打、迅速带走',note='与 sweep 比较动作，并非 sweep 派生。whisk 的名动词分别接北欧语草束、扫动和快速动作等材料；搅打工具与迅速移动由扫动关系连起来，不一律由现代打蛋器造出所有动词义。'),
 'B3769':dict(words='knead kneads kneaded kneading'.split(),label='knead：反复揉压面团',note='和 dough 比较厨房动作，不是 dough 派生。knead 接古英语 cnedan、日耳曼语揉压一族；早期 k、n 都发音，现代标准英语 k 不发音。现代过去式已常规化为 kneaded。'),
 'B3317':dict(words='chop chops chopped chopping'.split(),label='chop → chops、chopping：砍切与排骨块',note='砍切 chop 远源不完全确定，可能有法语和日耳曼语材料；名词一击、切下块到肉排。另有交易、来回改变一支接古英语 ceapian，不把所有 chop and change 硬归刀切。'),
 'C0147':dict(words='simmer simmers simmered simmering'.split(),label='simmer：小火咕嘟；情绪暗涌',note='与 boil 比较加热状态，不从拉丁 bullire 派生。simmer 接早期 simperen、simber 等，可能拟液体轻嘶声；现代比喻情绪压在里面、未爆发，simmer down 则逐渐平静。'),
 'B3714':dict(words='roast roasts roasted roasting'.split(),label='roast → roasts：烤制、烤肉；调侃嘲弄',note='roast 经法语 rostir 接法兰克等日耳曼烤架、烤制材料；后来的玩笑 roast 借烤的形象说拿某人打趣。roasts 可为名词复数或动词单数。'),
 'C1247':dict(words='ketchup mayonnaise'.split(),label='ketchup、mayonnaise：另源的常见酱料名',note='与 sauce 比较调味酱，并非都由拉丁 sal 盐派生。ketchup 的亚洲来源细节有争论，旧配方也不全是番茄；mayonnaise 借法语，Mahon 地名故事不宜当定论。'),
 'B3543':dict(words='chickpea chickpeas'.split(),label='chickpea：旧豆名 + pea，不是小鸡种的豆',note='chick- 接古法语 chiche、拉丁 cicer 豆名，经民间词源变形接近 chick；后部接 pease、pea 的重分析。整个词虽像 chick + pea，历史上不是以小鸡直接命名。'),
}
STEW=[['古法语 estuver 热浴、焖炖等 → 英语 stew 动词及相关名词','较远来源不确定，和 stove 暖房等旧义的联系也有讨论'],['慢炖 → 炖菜；闷在里面 → 烦闷、焦虑等比喻','现代先用锅里慢炖的画面理解，不把所有义项排成唯一时间线']]
WHISK=[['北欧语草束、擦扫、快速动作等材料 → 英语 whisk 名动词','名词和动词各有较早借入背景'],['迅速扫动 → 搅打食物及工具；迅速带走','现代打蛋器是同族的一项，不是所有动词义的唯一起点']]
KNEAD=[['日耳曼语揉压词族 → 古英语 cnedan → knead','古英语 k、n 对应音都发，现代标准发音只留 /n/'],['反复揉压软材料，如面团、黏土','古英语曾是强变化，现代常用规则 kneaded、kneading']]
CHOP=[['英语 chop：迅速一击地切、砍','较远来源不定，可能联系法语等材料'],['一砍 → 切下一块 → 肉排；动词继续用于切碎','交易、来回改变的 chop 另接 ceapian，不强并为同一刀切来源']]
SIMMER=[['早期 simperen、simber 等 → simmer','可能拟液体轻轻嘶响，不和傻笑 simper 硬定同源'],['液体轻轻咕嘟 → 情绪压在里面、持续暗涌','simmer down 再借由滚沸转小火的画面说平静下来']]
W('stew','英 /stjuː/；美 /stuː/','炖、焖；炖菜；焦虑、烦闷',
 '锅里放少量液体，让肉和蔬菜慢慢炖，是 stew；炖出来的一锅浓厚菜肴，也叫 a stew。心事闷在里面反复熬，也能借这个动作说烦闷。',
 '经古法语 estuver 热浴、焖炖等及相关名词形式，较远来源未定。暖房、蒸汽、慢煮是旧语境中的联系，现代菜名与焦虑用法各有发展。',STEW,
 'beef stew 是炖牛肉；stew the apples 是把苹果炖软；stew over a problem 是为问题闷着烦恼。',
 'beef stew；stew fruit；stew over a problem。',
 'soup 通常汤液更多；stew 通常食材块更突出、较浓稠，实际菜肴仍有重叠。stew 作动词不只限肉类。',
 ('We had beef stew with bread for dinner.','晚饭我们吃了炖牛肉配面包。'),('There is no point letting yourself stew over one awkward remark.','没必要为了那一句尴尬的话反复烦心。'),sources=S('stew','stew'))
W('stews','英 /stjuːz/；美 /stuːz/','炖菜〔复数〕；炖、闷着烦〔第三人称单数〕',
 '菜单上几种炖菜，是 stews；he stews over it 则是他为这事闷着烦。锅里的慢炖和心里的慢熬，可以用同一画面连接。',
 'stew + -s → stews，元音后后缀读 /z/；名词复数和动词第三人称单数同形。',STEW+[['stew + -s → stews','多个炖菜；或单数主语在炖、烦恼']],
 'hearty stews 是扎实丰盛的炖菜；she stews fruit 是她炖水果；he stews over a decision 是他为决定烦心。',
 'vegetable stews；hearty stews；stews over a decision。',
 'stews 若接在 he、she 后常是谓语，前面有 several 则常是菜名复数；句法比单看 s 更可靠。',
 ('The book includes recipes for soups and stews.','书里有汤和炖菜的做法。'),('He stews over every small mistake.','他每犯一点小错都会闷着烦很久。'),sources=S('stews','stew'))
W('stewed','英 /stjuːd/；美 /stuːd/','炖过、炖软的；炖了、烦闷过〔过去式、过去分词〕',
 '苹果放锅里慢慢煮软，是 stewed apples。-ed 把动作落到已经处理过的食物状态上。',
 'stew + -ed → stewed，基础词以元音结束，后缀读 /d/；过去分词常修饰食物。',STEW+[['stew + -ed → stewed','过去式、过去分词；也描述炖过的状态']],
 'stewed fruit 是炖水果；stewed apples 是炖苹果；stewed over a problem 也可说当时为问题烦心。',
 'stewed fruit；stewed apples；stewed over the decision。',
 'stewed 描述经慢炖、焖煮的处理；raw 是生的，roasted 是烤过的，区别落在烹饪动作上。',
 ('We served stewed apples with yoghurt.','我们端上炖苹果配酸奶。'),('She stewed over the comment all evening.','她整个晚上都为那句评论闷闷不乐。'),sources=S('stewed','stew'))
W('stewing','英 /ˈstjuːɪŋ/；美 /ˈstuɪŋ/','正在炖；适合炖的；闷着烦恼',
 '锅里的菜正在慢慢炖，是 stewing；人一直闷着想一件不痛快的事，也像在心里反复熬它。',
 'stew + -ing → stewing，直接接后缀；可表示过程，也在 stewing beef 里说明适合炖的用途。',STEW+[['stew + -ing → stewing','分词、动名词；也可表示食材用途']],
 'stewing beef 是适合慢炖的牛肉，不要求买来时已经炖好；be stewing over 是正为某事烦闷。',
 'stewing beef；stewing fruit；stewing over a problem。',
 'stewing beef 与 stewed beef 不同：前者说明用途，后者常说明已经做过的状态。',
 ('The apples were stewing gently on the stove.','苹果在炉上轻轻咕嘟着。'),('She spent the evening stewing over the argument.','她一晚上都在为那场争论烦心。'),sources=S('stewing','stew'))
W('whisk','英、美 /wɪsk/','快速搅打；迅速带走、扫动；打蛋器',
 '手腕快速转动，把鸡蛋打散，是 whisk；车一到就把人迅速接走，也是 whisk。共同画面是轻快、迅速地扫动。',
 '名词可能接古诺尔斯 visk 草束、扫具，动词另有北欧语擦扫、快速动作背景；不是所有意思都先从今天的打蛋器派生。后来工具名专用于搅打鸡蛋、奶油等。',WHISK,
 'whisk the eggs 是快速打散鸡蛋；whisk someone away 是迅速带走；a wire whisk 是金属丝打蛋器。',
 'whisk the eggs；a wire whisk；whisk someone away。',
 'stir 是搅拌，whisk 通常突出快速打散、打入空气等动作；词首 wh 在常见标准读音里读 /w/。',
 ('Whisk the eggs in a large bowl.','在大碗里把鸡蛋打散。'),('A car arrived to whisk the guests away.','一辆车驶来，把客人们迅速接走。'),sources=S('whisk','whisk'))
W('whisks','英、美 /wɪsks/','搅打、迅速带走〔第三人称单数〕；打蛋器〔复数〕',
 '她迅速打蛋，是 she whisks the eggs；抽屉里几把打蛋器，则是 whisks。动作和工具名一起记。',
 'whisk + -s → whisks，/k/ 后后缀读 /s/，末尾 /sks/；也可形成可数工具名的复数。',WHISK+[['whisk + -s → whisks','单数主语的动作；或多个打蛋器']],
 'electric whisks 是电动打蛋器；she whisks 是她搅打；the lift whisks visitors up 是电梯迅速把游客送上去。',
 'electric whisks；whisks the eggs；whisks visitors upstairs。',
 'whisks 后缀不读成 /ɪz/；基础末音 /k/ 直接接 /s/，即使前面还有 /s/。',
 ('She whisks the eggs while the pan warms up.','锅加热时，她把鸡蛋打散。'),('The shop sells bowls, spatulas and whisks.','这家店卖碗、锅铲和打蛋器。'),sources=S('whisks','whisk'))
W('whisked','英、美 /wɪskt/','快速搅打了；迅速带走了〔过去式、过去分词〕',
 '鸡蛋刚被打散，或人一转眼被带走，都能用 whisked。过去动作里仍保留那股轻快、迅速的感觉。',
 'whisk + -ed → whisked，/k/ 是清音，-ed 读 /t/；末尾 /skt/ 连在一起，不另加 /ɪd/。',WHISK+[['whisk + -ed → whisked','过去式、过去分词；后缀 /t/']],
 'whisked the cream 是搅打了奶油；was whisked away 是被迅速带走；was whisked upstairs 是被迅速送上楼。',
 'whisked the eggs；whisked away；whisked upstairs。',
 'taken away 只说被带走；whisked away 还描写动作很快，往往几乎没有停留。',
 ('She whisked the cream until it thickened.','她把奶油搅打到变稠。'),('The guests were whisked upstairs in a private lift.','客人们乘专用电梯迅速被送到了楼上。'),sources=S('whisked','whisk'))
W('whisking','英、美 /ˈwɪskɪŋ/','正在搅打；迅速带走的过程',
 '一边慢慢倒液体，一边手腕不停快速打散，可以说 whisking continuously。动作连续，就不容易把它只理解成一个静态工具名。',
 'whisk + -ing → whisking，直接接后缀，不双写 k；动词的搅打、迅速移动两类用法都能形成分词。',WHISK+[['whisk + -ing → whisking','现在分词、动名词，描写搅打或迅速移动过程']],
 'keep whisking 是继续搅打；while whisking 是搅打的同时；whisking someone away 是迅速把人带走。',
 'keep whisking；whisking continuously；whisking visitors away。',
 'whisking 的动作通常比 gently stirring 更快、更有打散的感觉；选词要跟实际烹饪动作对应。',
 ('Add the milk slowly, whisking continuously.','慢慢加牛奶，同时不停搅打。'),('She was still whisking the eggs when the timer rang.','计时器响时，她还在打鸡蛋。'),sources=S('whisking','whisk'))
W('knead','英、美 /niːd/','揉、揉压；揉面',
 '把面团按下去、折回来，再按，再折，这样反复揉压就是 knead。重点是软材料在手下受压、变得均匀，不只是搅两下。',
 '接古英语 cnedan，日耳曼语揉压词族；早期词首对应的 k、n 都发音，现代标准英语 k 已不发音。现代常用规则过去式 kneaded。',KNEAD,
 'knead dough 是揉面；knead clay 是揉黏土。动词也可用于类似的按揉动作，具体宾语说明材料。',
 'knead the dough；knead clay；knead until smooth。',
 'knead 与 need 需要同音 /niːd/，拼写和来源不同。mix 是混合，knead 还突出反复用力揉压。',
 ('Knead the dough until it feels smooth.','把面团揉到手感光滑。'),('She began to knead a lump of clay.','她开始揉一团黏土。'),sources=S('knead','knead'))
W('kneads','英、美 /niːdz/','揉、揉压〔第三人称单数〕',
 '他每天揉一团面，是 he kneads the dough。手掌来回施压，动作规律地重复。',
 'knead + -s → kneads，基础末音 /d/ 后的后缀读 /z/；词首 k 仍不发音。',KNEAD+[['knead + -s → kneads','第三人称单数；读 /niːdz/']],
 'a baker kneads dough 是面包师揉面；a machine kneads dough 是机器揉面；主体可以是人，也可以是工具。',
 'kneads the dough；kneads clay；a machine kneads。',
 'kneads 与 needs 同音；前者是揉，后者是需要。The baker kneads，the baker needs flour，靠句意与拼写区别。',
 ('The baker kneads the dough by hand.','面包师用手揉面。'),('This machine mixes and kneads the dough for us.','这台机器替我们混合原料并揉面。'),sources=S('kneads','knead'))
W('kneaded','英、美 /ˈniːdɪd/','揉过了；揉好的〔过去式、过去分词〕',
 '面团已经揉好，是 kneaded dough；说她刚才揉了面，则是 she kneaded the dough。过去动作与完成状态用同一个形式。',
 'knead + -ed → kneaded；基础末音 /d/ 后，-ed 读 /ɪd/，增加一个音节。古英语旧强变化不再作为现代常用形式保留。',KNEAD+[['knead + -ed → kneaded','规则过去式、过去分词；/d/ 后加 /ɪd/']],
 'freshly kneaded dough 是刚揉好的面团；kneaded the clay 是揉过黏土；had kneaded 说此前已经揉过。',
 'freshly kneaded dough；kneaded by hand；kneaded the clay。',
 'kneaded 与 needed 同音 /ˈniːdɪd/；拼写看得出是在揉材料，还是需要某物。',
 ('She kneaded the dough for several minutes.','她揉了几分钟面。'),('The freshly kneaded dough rested in a covered bowl.','刚揉好的面团放在盖好的碗里醒着。'),sources=S('kneaded','knead'))
W('kneading','英、美 /ˈniːdɪŋ/','揉压、揉面；正在揉',
 '手掌不停把面团按开、折回，这整个反复操作的过程是 kneading。-ing 把一次动作展开成持续过程，也能作为行为名称。',
 'knead + -ing → kneading；词尾直接接 -ing，词首 k 不发音。读 /ˈniːdɪŋ/。',KNEAD+[['knead + -ing → kneading','现在分词、动名词；揉压过程']],
 'be kneading dough 是正在揉面；after kneading 是揉过之后；kneading by hand 是手工揉面。',
 'kneading dough；after kneading；kneading by hand。',
 'kneading 与 needing 同音。前者可描述面包制作步骤，后者常接所需对象，意思与来源不同。',
 ('He was kneading dough at the kitchen table.','他正在厨房桌边揉面。'),('After kneading, she shaped the dough into a ball.','揉好后，她把面团整成了球形。'),sources=S('kneading','knead'))
W('chops','英 /tʃɒps/；美 /tʃɑps/','砍、切碎〔第三人称单数〕；肉排〔复数〕；〔口语〕本领',
 '厨师一下下切菜，是 chops；端上两块带骨肉排，也叫 chops。名词先从“切下的一块”理解，再接到菜单里的肉排。',
 'chop + -s → chops，/p/ 后后缀读 /s/。砍切动词形成切下一块等名词；口语还有技艺、本领用法，不能都按实际拿刀解释。',CHOP+[['chop + -s → chops','动词单数；肉排等名词复数；现代另有本领俗语用法']],
 'pork chops 是猪排；she chops onions 是她切洋葱；musical chops 是演奏本领。技能用法先作为现代口语义记，不编造唯一动作起源。',
 'pork chops；lamb chops；chops onions；musical chops。',
 'chop and change 反复变来变去，另接早期交易词线；肉排的 chops 则与砍切那一支联系。',
 ('She chops the onions while I prepare the sauce.','我准备酱汁时，她切洋葱。'),('We ordered pork chops with vegetables.','我们点了猪排配蔬菜。'),sources=S('chops','chop'))
W('chopping','英 /ˈtʃɒpɪŋ/；美 /ˈtʃɑpɪŋ/','正在切碎、砍；砍切动作',
 '菜刀反复落下，把洋葱切成小块，是 chopping。与切出整齐薄片不同，这里先抓一下下砍切、分成小块的动作。',
 'chop 双写末尾 p + -ing → chopping；单音节基础词的短元音后只有一个辅音字母 p，接元音开头后缀时双写。',CHOP+[['chop 双写 p + -ing → chopping','现在分词、动名词；保持基础短元音拼写关系']],
 'chopping onions 是切洋葱；a chopping board 是切菜板；chopping wood 是劈木头，动作和材料一起决定译法。',
 'chopping onions；a chopping board；chopping wood。',
 'slice 通常突出切成片；chop 常突出一下下砍切、切成块。chopping board 说明用途，板子自己没有正在切。',
 ('He was chopping vegetables for dinner.','他正在切蔬菜准备晚饭。'),('Put the onion on a chopping board.','把洋葱放在切菜板上。'),sources=S('chopping','chop'))
W('simmers','英 /ˈsɪməz/；美 /ˈsɪmɚz/','小火慢煮；情绪暗涌〔第三人称单数〕',
 '锅里轻轻冒小泡，是 simmers；怒气压着没有爆发，也像锅里一直咕嘟着，仍能说 simmers。',
 'simmer + -s → simmers，后缀 /z/。simmer 接早期 simperen、simber 等液体轻嘶声材料，可能带拟声背景。',SIMMER+[['simmer + -s → simmers','第三人称单数；实体液体、抽象情绪均可作主语']],
 'the sauce simmers 是酱汁在小火煮；resentment simmers 是不满暗中积着。with 后可接 anger 等说明情绪。',
 'the sauce simmers；resentment simmers；simmers with anger。',
 'boils 常呈大泡翻滚的状态；simmers 通常温和地咕嘟。比喻里 simmer 也突出尚未完全爆发的情绪。',
 ('The sauce simmers while we cook the pasta.','我们煮意面时，酱汁在小火咕嘟着。'),('Resentment simmers beneath their polite conversation.','他们客客气气地交谈，底下却暗藏不满。'),sources=S('simmers','simmer'))
W('simmered','英 /ˈsɪməd/；美 /ˈsɪmɚd/','小火煮过；暗中积着〔过去式、过去分词〕',
 '汤在锅里轻轻咕嘟了一阵，是 simmered；矛盾表面平静、底下一直没散，也可以说 simmered。',
 'simmer + -ed → simmered，后缀读 /d/。现代规则过去形式承接液体小火煮与情绪暗涌两类用法。',SIMMER+[['simmer + -ed → simmered','过去式、过去分词；后缀 /d/']],
 'simmered the sauce 是把酱汁小火煮过；anger simmered 是怒气一直暗中积着；simmered down 是慢慢平静下来。',
 'simmered the sauce；anger simmered；simmered down。',
 'simmered down 平静下来与 simmered with anger 怒气暗涌，方向看似不同，区别在 down 与 with 的搭配。',
 ('She simmered the soup for another ten minutes.','她把汤又小火煮了十分钟。'),('The disagreement simmered for weeks before anyone spoke openly.','分歧暗中积了好几个星期，才有人公开说出来。'),sources=S('simmered','simmer'))
W('roasts','英 /rəʊsts/；美 /roʊsts/','烤、烘焙；拿人打趣〔第三人称单数〕；烤肉、调侃活动〔复数〕',
 '她烤蔬菜，是 she roasts vegetables；周日吃的几顿烤肉大餐，也能说 Sunday roasts。口语拿人“放在火上烤”，又借给了调侃。',
 'roast + -s → roasts，末尾 /t/ 后读 /s/。roast 经古法语 rostir 接日耳曼语烤架、烤制材料，烤肉名词和调侃用法后来扩展。',
 [['日耳曼语烤架、烤制材料 → 法语 rostir → 英语 roast','干热烹饪 → 烤肉；又喻拿人开玩笑'],['roast + -s → roasts','名词复数或动词第三人称单数；词尾 /sts/']],
 'roasts vegetables 是烤蔬菜；Sunday roasts 是周日烤肉餐；roasts a friend 是拿朋友打趣。语气和关系决定玩笑是否被接受。',
 'Sunday roasts；roasts vegetables；roasts coffee beans。',
 'roast 与 boil、stew 的加热方式不同；a roast 在餐饮里不是泛指任何煮熟的肉。',
 ('She roasts the vegetables with garlic.','她用大蒜一起烤蔬菜。'),('The pub is famous for its Sunday roasts.','这家酒馆以周日烤肉餐出名。'),sources=S('roasts','roast'))
W('ketchup','英、美 /ˈketʃəp/','番茄酱〔常见现代义〕；某些其他调味酱',
 '薯条旁那团酸甜的红酱，今天通常就是 ketchup。但名字早年管过不止一种酱，蘑菇酱、鱼类调味酱等也出现在它的历史里。',
 '通常联系亚洲酱料名称，常见分析经过马来语并联系闽南等汉语酱汁词；也有其他远源说法，具体传播路线未完全确定。英语早期有 catchup、catsup 等拼写。',
 [['亚洲酱料名称 → 英语 ketchup、catchup、catsup 等','较远来源和借入路线有争论，早期配方并不统一'],['英语中的多种调味酱 → tomato ketchup 广泛流行','现代无修饰 ketchup 通常指番茄酱']],
 'tomato ketchup 明说番茄酱；a bottle of ketchup 是一瓶酱。作食材名通常不可数，数量靠 bottle、spoonful 等。',
 'tomato ketchup；a bottle of ketchup；fries with ketchup。',
 'ketchup 常是酸甜调味番茄酱；tomato sauce 的范围因地区和菜式更宽，意面酱未必就是 ketchup。',
 ('Would you like ketchup with your fries?','薯条要配番茄酱吗？'),('She put a bottle of ketchup on the table.','她把一瓶番茄酱放到桌上。'),sources=S('ketchup','ketchup'))
W('mayonnaise','英 /ˌmeɪəˈneɪz/；美 /ˈmeɪəneɪz/','蛋黄酱；美乃滋',
 '三明治里那种绵稠、浅色的酱，常叫 mayonnaise。现代典型做法把油与蛋黄等打成均匀酱体，口语常缩成 mayo。',
 '借法语 mayonnaise；更早命名来由有争论。联系 Mahon 地名、庆祝战役的故事很流行，但词形记录与传说时间并不吻合到足以确证。',
 [['法语 mayonnaise：旧菜式、调味酱用语 → 英语 mayonnaise','确切命名来源有争论，Mahon 地名说不能当成定论'],['配方、酱体在历史中变化 → 现代常见蛋黄酱','英语口语再缩为 mayo']],
 'a spoonful of mayonnaise 是一勺蛋黄酱；tuna mayonnaise 是金枪鱼拌蛋黄酱相关做法。名词通常按酱料不可数使用。',
 'a spoonful of mayonnaise；tuna mayonnaise；mayonnaise dressing。',
 'mayonnaise 与 mustard 芥末酱、ketchup 番茄酱是不同调味料；现代读音英美重音可不同，不按拼写逐个元音全读。',
 ('Mix the tuna with a little mayonnaise.','把金枪鱼和少量蛋黄酱拌在一起。'),('Would you like mayonnaise in your sandwich?','你的三明治里要加蛋黄酱吗？'),sources=S('mayonnaise','mayonnaise'))
W('chickpea','英、美 /ˈtʃɪkpiː/','鹰嘴豆',
 '煮熟后小小一粒、常呈浅黄色，能打成鹰嘴豆泥的豆子，是 chickpea。英文看着像“小鸡 + 豌豆”，历史却是旧豆名被听熟、写熟后的结果。',
 'chick- 接古法语 chiche、拉丁 cicer 的豆名，早期英语有 chich、chich-pease；后来受 chick 拼写影响。pease 又重分析成 pea，形成现代 chickpea。',
 [['拉丁 cicer 豆名 → 法语 chiche → 英语 chich 等','旧豆名的词形后来被民间词源拉近 chick'],['chich-pease 等 → chickpea','后部经历 pease、pea 的重新分析，不是由小鸡直接命名']],
 'a chickpea 数一粒；chickpea flour 是鹰嘴豆粉。常见食物 hummus 的原料之一就是 chickpeas。',
 'a chickpea；chickpea flour；chickpea curry。',
 '中文鹰嘴豆的形状命名和英语 chickpea 的历史不必完全对应；不同语言能用不同方式给同一食物起名。',
 ('A chickpea rolled off the chopping board.','一粒鹰嘴豆从切菜板上滚了下来。'),('The flatbread is made with chickpea flour.','这种薄饼用鹰嘴豆粉制作。'),sources=S('chickpea','chickpea'))
W('chickpeas','英、美 /ˈtʃɪkpiːz/','鹰嘴豆〔复数〕',
 '一罐鹰嘴豆，是 a tin of chickpeas。多数做菜场景会用很多粒，所以比起单数，食谱里常看见这个复数。',
 'chickpea + -s → chickpeas，元音 /iː/ 后接 /z/。复数加在整个名词末尾，不改前面的旧豆名材料。',
 [['拉丁 cicer → 法语 chiche → 英语 chich-pease、chickpea','豆名、拼写和 pease 的重分析共同塑成现代词'],['chickpea + -s → chickpeas','一粒到多粒，词尾 /piːz/']],
 'cooked chickpeas 是熟鹰嘴豆；a tin of chickpeas 是一罐；roasted chickpeas 是烤鹰嘴豆。',
 'cooked chickpeas；a tin of chickpeas；roasted chickpeas。',
 'chickpeas 是多粒豆；chickpea flour 用单数名词作材料修饰语，不因面粉来自许多粒就必须写 chickpeas flour。',
 ('Drain the chickpeas before adding them to the salad.','把鹰嘴豆沥干，再加进沙拉。'),('She blended cooked chickpeas into a smooth paste.','她把熟鹰嘴豆打成细腻的泥。'),sources=S('chickpeas','chickpea'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zil',ROOTS,WORDS)
 extend_lessons()
