"""Milk: parallel inherited noun/verb, milk-like appearances and dairy compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
M=[['古英语 meolc、meoluc → 中古英语 milk 等 → milk〔名词〕','奶、乳'],['古英语 melcan → 中古英语 milken → milk〔动词〕','挤奶；与名词同族，现代词形相同'],['现代外形与动作比喻','乳白液体、颜色；尽量榨取关注、利益等']]
def MH(f,m):return M[:1]+[[f,m]]
W('milk','/mɪlk/','奶、乳；挤奶；榨取、充分利用〔比喻〕',
 '名词说奶，动词说把奶挤出来；一段经历被反复拿来博同情、求关注，也能像不断挤取那样说 milk。',
 '奶名词继承古英语 meolc 等，挤奶动词继承 melcan，经中古英语两路到同形 milk。植物饮品、乳白液体借形态用途称 milk，不是所有奶字食品都来自同一动物。',M,
 'a glass of milk 一杯奶，milk a cow 挤牛奶，oat milk 燕麦饮品，milk an opportunity 尽量利用机会，cry over spilt milk 为不可挽回的事懊悔。',
 'a glass of milk；milk a cow；oat milk；cry over spilt milk。',
 'milk 名词常不可数，a milk 可在点单口语中代指一份；milk 比喻榨取常带过度利用语气，看具体宾语。',
 ('She added a little milk to her tea.','她往茶里加了一点奶。'),('The comedian milked the joke for every laugh he could get.','喜剧演员把那个笑话反复发挥，尽可能多逗出些笑声。'))
W('milky','/ˈmɪlki/','含奶多的；乳白的、像奶的',
 '咖啡里奶放得多，可以是 milky；一片白雾、浑白玻璃像奶，也能这样形容，未必真掺了奶。',
 '中古英语 mylky、melky 等已有相应形容词，现代对应 milk + -y；更早相应形的重建分析不必当作有原文记录的词形。',MH('中古英语 mylky、melky → milky；对应 milk + -y','奶多的；像奶一样白、浑白的'),
 'milky coffee 奶多的咖啡，milky water 浑白水体，a milky sky 乳白天色，the Milky Way 银河。',
 'milky coffee；a milky sky；milky glass；the Milky Way。',
 'milky 颜色、外观不证明成分有奶；the Milky Way 是白带般银河的名称，不是字面牛奶铺成的路。',
 ('She likes her coffee sweet and milky.','她喜欢咖啡甜一点、奶多一点。'),('A milky haze covered the hills.','乳白色薄雾笼罩着山丘。'))
W('milking','/ˈmɪlkɪŋ/','挤奶、挤奶过程；正在挤取',
 '把 milk 挤奶的动作作为一项工作、过程来讲；milking machine 就是用于这项工序的机器。',
 'milk + -ing，中古英语 milkinge 等已有动作名词。也可随动词的榨取比喻使用，不能每次看到 -ing 就一定在说此刻奶牛正挤奶。',M[:2]+[['milk + -ing → milking','挤奶过程；相应分词']],
 'morning milking 早晨挤奶，a milking machine 挤奶机，a milking parlour 挤奶厅。',
 'morning milking；a milking machine；a milking parlour。',
 'milk 奶或挤奶动词，milking 强调过程；milkshake 奶昔是饮品，不是挤奶动作的另一个 -ing。',
 ('Morning milking began before sunrise.','早晨挤奶在日出前开始。'),('The farm installed a new milking machine.','农场安装了一台新挤奶机。'))
W('milkshake','/ˈmɪlkʃeɪk/','奶昔',
 '把奶与调味、常见还有冰淇淋等摇匀、搅打，成为浓滑饮品。名字说奶加摇动，不是奶被吓得发抖。',
 'milk + shake 摇、搅动，现代复合饮品名。不同地方、年代配方不同，不把冰淇淋当所有 milkshake 必有的唯一标准。',MH('milk + shake → milkshake','摇匀、搅打制成的含奶饮品'),
 'a strawberry milkshake 草莓奶昔，a chocolate milkshake 巧克力奶昔，order a milkshake 点奶昔。',
 'a strawberry milkshake；a chocolate milkshake；order a milkshake。',
 'milkshake 奶昔，smoothie 常由水果等搅打而成、未必含奶；名称和配方范围有重叠，不能只看是否用搅拌机就完全等同。',
 ('He ordered a chocolate milkshake.','他点了一杯巧克力奶昔。'),('The café serves milkshakes in tall glasses.','咖啡馆用高玻璃杯装奶昔。'))
W('buttermilk','英 /ˈbʌtəmɪlk/；美 /ˈbʌtərmɪlk/','酪乳、白脱牛奶〔乳制品名〕',
 '传统上是做黄油后留下的液体；现代商店常见的则是培养发酵得到的酸味乳品。不是把一块黄油直接丢进奶里就完成词义。',
 'butter 黄油 + milk，中古英语已有相应组合。名称来自与制黄油过程的关系，后来也用于培养酸乳类产品，旧工序与现代商品用法分开。',MH('butter + milk → buttermilk','制黄油留下的乳液 → 培养酸乳等用法'),
 'buttermilk pancakes 酪乳煎饼，a carton of buttermilk 一盒酪乳，cultured buttermilk 培养发酵酪乳。',
 'buttermilk pancakes；a carton of buttermilk；cultured buttermilk。',
 'buttermilk 名称不表示一定比普通奶含更多黄油；butter 黄油与 buttermilk 是相关过程中的不同乳品，不可只按材料字面互换。',
 ('The recipe calls for buttermilk.','食谱需要酪乳。'),('She bought a carton of cultured buttermilk.','她买了一盒培养发酵酪乳。'),
 sources=['https://en.wiktionary.org/wiki/buttermilk#English','https://www.etymonline.com/word/buttermilk'])
W('milkman','/ˈmɪlkmən/','送奶工〔传统称呼〕',
 '把奶送到住户门前的人；man 是人物材料，不是把牛奶做成人形。',
 'milk + man，按配送的产品命名职业。复数 milkmen；不同地区、时代的配送制度可不同，词本身不保证只送玻璃瓶奶。',MH('milk + man → milkman','送奶的人'),
 'the milkman’s round 送奶路线，the local milkman 当地送奶工，leave a note for the milkman 留字条给送奶工。',
 'the local milkman；the milkman’s round；leave a note for the milkman。',
 'milkman 配送，dairy farmer 奶农、生产方；一人可能兼做，但送到门口的人不一定亲自养牛。',
 ('The milkman left two bottles by the door.','送奶工在门边放了两瓶奶。'),('She left a note for the milkman.','她给送奶工留了张字条。'))
W('milkweed','/ˈmɪlkwiːd/','乳草、马利筋类植物〔常用名〕',
 '汁液乳白、像奶，所以植物名称里借用 milk；weed 是草本植物、杂草的命名材料，不代表每位园丁都嫌弃它。',
 'milk 乳白形象 + weed 草，历史上曾用于多种有乳状汁液的植物，现代常指马利筋属等相应植物。不是奶农专用的饲草这个意思。',MH('milk + weed → milkweed','汁液像奶的植物名称'),
 'milkweed plants 乳草植株，milkweed seeds 乳草种子，a patch of milkweed 一片乳草。',
 'milkweed plants；milkweed seeds；a patch of milkweed。',
 'milkweed 按汁液形象命名，milking 是挤奶动作；植物俗名有范围差别，认具体物种看完整名称。',
 ('Milkweed grew along the fence.','篱笆旁长着乳草。'),('The packet contained milkweed seeds.','小包里装着乳草种子。'),
 sources=['https://en.wiktionary.org/wiki/milkweed#English','https://www.etymonline.com/word/milkweed'])
R('B3241','奶、挤奶与乳白形象的扩展','MILK：能被挤出的乳液，后来也借给颜色、汁液和反复榨取','milk → milky、milking；milkshake、buttermilk 是饮品乳品，milkman 是配送人物，milkweed 取乳白汁液形象。',
 '奶名词与挤奶动词是同族不同旧形式，现代同形。buttermilk 不等于往牛奶加黄油，milkweed 不会产动物乳。',
 'meolc 等 → milk 名词，melcan → milk 动词；milk + -y/-ing；milk + shake/man/weed；butter + milk。',
 [['基础、性质与过程','milk · milky · milking'],['乳品、配送与植物','milkshake · buttermilk · milkman · milkweed']],
 'milky 外观不保证含奶；milkshake 配方非唯一；buttermilk 旧工序与现代培养产品分；milkweed 是植物俗名。',
 'The milkman delivered milk, and she used some to make a milkshake.\n\n送奶工送来牛奶，她用其中一些做了奶昔。','milk milky milking milkshake buttermilk milkman milkweed')
if __name__=='__main__':save('continuation_20261030_ea',ROOTS,WORDS)
