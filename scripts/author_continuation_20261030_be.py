"""Beach, hall and smith: landscapes, shared buildings and skilled trades."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
BE=[['中古英语 bache 等相关形式 → beach','岸边、沙砾滩等；更早来源有不同分析'],['现代 beach','沙、砾石等组成的岸滩；使船上滩、搁浅']]
def B(f,m):return BE+[[f,m]]
W('beach','/biːtʃ/','海滩、湖岸沙砾滩；使船上滩、搁浅',
 '水边铺着沙或小石子的那片可站、可走的岸滩；动词就是让船停上这片滩。',
 '接中古英语相关岸、沙砾滩形式，更早有溪流、岸边或砾石等不同分析，不把某条不确定远源说成唯一。动词由上滩场景形成。',BE,
 'a sandy beach 沙滩，a pebble beach 砾石滩，walk along the beach 沿海滩走，beach a boat 把船拉上滩。',
 'a sandy beach；a pebble beach；on the beach；beach a boat。',
 'beach 岸滩可有沙也可有石，不是所有 coast 海岸线都能躺着晒太阳。海边湖边都可能有 beach。',
 ('We walked along the beach after breakfast.','早饭后，我们沿海滩散步。'),('They beached the small boat before the storm.','风暴来临前，他们把小船拉上了滩。'),sources=['https://www.etymonline.com/word/beach','https://en.wiktionary.org/wiki/beach#English'])
W('beachy','/ˈbiːtʃi/','海滩般的；有海边休闲感觉的',
 '沙色、松弛、轻快，带点海边度假的感觉；可以说装饰、衣着或发型。',
 'beach + -y，表示海滩相关、像海滩。没有要求对象真摆在海边，如 beachy décor 也可在内陆家里。',B('beach + -y → beachy','海滩相关；借指海边休闲风格'),
 'a beachy atmosphere 海边般休闲氛围，beachy décor 海滩风装饰，beachy waves 自然松散波浪发。',
 'a beachy atmosphere；beachy décor；beachy waves。',
 'beachy 偏性质、风格，beachfront 明确临海滩位置；一间 beachy café 未必真的就在海滩边。',
 ('The café has a relaxed, beachy atmosphere.','咖啡馆带着海边般的轻松氛围。'),('She chose light colours for a beachy look.','她选浅色，营造海滩休闲风。'))
W('beachhead','/ˈbiːtʃhed/','滩头阵地；立足点〔比喻〕',
 '先在岸边站稳一小块，后续才有地方向里面展开；商业比喻也取先拿下立足点。',
 'beach 滩 + head 前端、突出位置，先作军事登陆相关名称，后引申建立后续行动基础的地点、位置。',B('beach + head → beachhead','登陆后建立的滩头位置 → 后续扩展的立足点'),
 'establish a beachhead 建立滩头阵地、立足点，a market beachhead 市场初步立足点。',
 'establish a beachhead；secure a beachhead；a market beachhead。',
 'beachhead 说先站稳、便于后续推进的阵地，不等于整条 beach 的最前端都自动是军事阵地。',
 ('The troops established a beachhead before moving inland.','部队建立滩头阵地后，才向内陆推进。'),('The small office gave the company a beachhead in the new market.','这间小办公室给公司在新市场提供了初步立足点。'))
W('beachwear','英 /ˈbiːtʃweə/；美 /ˈbiːtʃwer/','海滩服装；沙滩穿着用品',
 '为去海边穿的泳装、罩衫、短裤等这一类衣着；按使用场景归成一组。',
 'beach + wear 衣着、穿着用品。wear 在这里是名词性成分，不是磨损海滩。',B('beach + wear → beachwear','海滩场景穿着的服装类别'),
 'summer beachwear 夏季沙滩服装，a beachwear collection 海滩服装系列。通常不可数。',
 'summer beachwear；a beachwear collection；casual beachwear。',
 'beachwear 海滩衣着范围较宽，swimwear 专用于游泳的衣物；去海滩穿的罩衫未必适合直接下水游。',
 ('The shop sells swimwear and other beachwear.','店里出售泳装和其他海滩服装。'),('The collection includes light summer beachwear.','系列包括轻薄的夏季海滩服装。'))
R('B3361','沙砾岸滩；休闲风格、登陆立足点与场景服装','BEACH：水边沙石铺成的岸滩','beach → beachy，再 beachhead、beachwear；beachfront、beachside 已有共享，按位置分组。',
 '更早来源有不同分析，从可靠岸滩义讲。海滩不必全是细沙，也不必处处可游泳。',
 'beach + -y/head/wear/front/side。',
 [['基本岸滩和风格','beach · beachy'],['位置、阵地和用途','beachfront · beachside · beachhead · beachwear']],
 'beach 沙或砾滩、coast 海岸；beachy 风格不等于 beachfront 位置；beachwear 比 swimwear 范围宽。',
 'The beachside shop sells beachwear in a relaxed, beachy setting.\n\n海滩旁的店在轻松的海滨风环境里出售沙滩服装。',
 'beach beachy beachfront beachside beachhead beachwear')
HA=[['古英语 heall → 中古英语 halle → hall','大厅、居所、重要建筑等'],['现代 hall','大厅、会堂；门厅、走廊；公共机构建筑等']]
W('hall','英 /hɔːl/；美 /hɔːl/〔部分口音 /hɑːl/〕','大厅；会堂、礼堂；门厅、走廊；公共建筑',
 '人进出、聚集或通过的一大片室内空间；在不同房子里，可能是门口过道，也可能是整座礼堂。',
 '继承古英语 heall，旧时可指重要大厅、居所等。后随建筑用途分出会堂、入口、走道等义，不要求每个 hall 都很豪华。',HA,
 'the entrance hall 门厅，a concert hall 音乐厅，the town hall 市政厅，down the hall 沿走廊。',
 'the entrance hall；a concert hall；the town hall；down the hall。',
 'hall 可大型聚会空间，也可过道；hallway 更直接说明走廊、通道，room 房间通常按独立使用空间称呼。',
 ('Please leave your shoes in the hall.','请把鞋留在门厅。'),('The concert will take place in the main hall.','音乐会将在主礼堂举行。'))
W('guildhall','英 /ˈɡɪldhɔːl/；美 /ˈɡɪldhɔːl/','行会会馆；历史上的市政会馆',
 '商人、工匠结成行会后，用来开会、办事的公共建筑；有些城市的历史会馆也承担市政用途。',
 'guild 行会 + hall 会堂。先认组织和建筑两个成分，不是 gold 黄金 + hall。',HA+[['guild + hall → guildhall','行会聚会、办事建筑；一些城市有市政用途']],
 'the old guildhall 老行会会馆，a medieval guildhall 中世纪行会会馆。首字母大写时可能是具体建筑名。',
 'the old guildhall；a medieval guildhall；visit the guildhall。',
 'guildhall 说明行会、历史市政建筑，town hall 泛指市政厅；名称有时重叠，不能所有现代市政厅都默认叫 guildhall。',
 ('The old guildhall now houses a small museum.','老行会会馆如今设有一间小博物馆。'),('The tour includes a visit to the medieval guildhall.','参观行程包括一座中世纪行会会馆。'))
R('B3954','人聚集、通行的室内空间与公共建筑','HALL：会聚的大空间，也可门厅、走廊','hall → guildhall；hallway、hallmark、dancehall 既有共享，分别讲通道、检验印记历史与舞厅。',
 '旧重要大厅词延续，现代范围从家中门厅到音乐厅。hallmark 的印记历史已有单词讲解，不重新由走廊硬猜。',
 'hall + way/mark；guild/dance + hall。',
 [['基本空间和走道','hall · hallway'],['组织、活动和历史用法','guildhall · dancehall · hallmark']],
 'hall 大厅或过道靠建筑语境；guildhall 行会馆不是黄金大厅；hallmark 是固定历史支线。',
 'Visitors walked through the hall of the old guildhall.\n\n访客穿过老行会会馆的大厅。',
 'hall hallway guildhall dancehall hallmark')
SM=[['古英语 smiþ → 中古英语 smith → smith','工匠，尤其金属加工工匠；更远来源有不同分析'],['现代 smith','金属匠人；按材料、产品命名的职业；文字技艺等比喻']]
def S(f,m):return SM+[[f,m]]
W('smith','/smɪθ/','金属匠人；铁匠等职业成分；锻造〔动词，较少用〕',
 '把材料加工成有用、精巧物件的人；职业前面加材料或产品，就能看出他主要做什么。',
 '继承古英语 smiþ。常被拿来与 smite 击打联系，但现代研究对远源并不一致，不把锤击这个直观画面当唯一词源结论。',SM,
 'a skilled smith 熟练金属匠，a village smith 乡村铁匠。Smith 也是常见姓，不能据姓直接推断现代职业。',
 'a skilled smith；a village smith；work as a smith。',
 'smith 金属工匠这个通称，blacksmith 铁匠、goldsmith 金匠按材料分；wordsmith 则把锻造技艺借到文字。',
 ('The village smith repaired the metal gate.','乡村铁匠修好了金属门。'),('The museum demonstrates how a smith shapes hot metal.','博物馆演示金属匠怎样给热金属塑形。'),sources=['https://www.etymonline.com/word/smith','https://en.wiktionary.org/wiki/smith#English'])
W('locksmith','英 /ˈlɒksmɪθ/；美 /ˈlɑːksmɪθ/','锁匠',
 '专门做锁、修锁、配钥匙、处理锁具问题的手艺人；前面直接说明产品。',
 'lock 锁 + smith 工匠，中古英语已有 loksmith。不是把头发 lock 烫成某种样子的发型师。',S('lock + smith → locksmith','制作、修理锁具的工匠'),
 'call a locksmith 叫锁匠，a local locksmith 当地锁匠，a locksmith’s shop 锁匠铺。',
 'call a locksmith；a local locksmith；a locksmith’s shop。',
 'locksmith 做锁具相关工作，blacksmith 铁匠工作范围更广；也不等于所有修门的 carpenter 木匠。',
 ('We called a locksmith after losing the keys.','丢钥匙后，我们叫了锁匠。'),('The locksmith repaired the old lock.','锁匠修好了旧锁。'))
W('silversmith','英 /ˈsɪlvəsmɪθ/；美 /ˈsɪlvərsmɪθ/','银匠',
 '把银做成器皿、首饰等物件的工匠，按主要材料命名。',
 'silver 银 + smith 工匠，有古英语 seolforsmiþ 等旧同族形式。不是现代先有英语 silver 才临时加后缀的新职业。',SM[:1]+[['古英语 seolforsmiþ → silversmith','银加工匠人；现代对应 silver + smith']],
 'a skilled silversmith 熟练银匠，a silversmith’s workshop 银匠作坊。',
 'a skilled silversmith；a silversmith’s workshop；silverware by a silversmith。',
 'silversmith 银匠，goldsmith 金匠，jeweller 珠宝匠、珠宝商范围更宽；银匠也可制作杯盘而不仅是首饰。',
 ('The silversmith made a small silver bowl.','银匠做了一个小银碗。'),('The exhibition features work by local silversmiths.','展览展出了当地银匠的作品。'))
R('B3480','加工金属的手艺人；材料、产品与技艺比喻','SMITH：把材料做成物件的匠人','smith 基础词后，按已有 blacksmith、goldsmith 与新增 silversmith 分材料；locksmith、gunsmith 分产品，wordsmith 接文字比喻。',
 '工匠画面直观，远源却不要强定锤击一说。冷门箭匠、地区性复合职业暂略。',
 'black/gold/silver/lock/gun/word + smith；部分组合有古英语旧形式。',
 [['通称和材料','smith · blacksmith · goldsmith · silversmith'],['产品及技艺比喻','locksmith · gunsmith · wordsmith']],
 'Smith 姓不说明当代职业；silversmith 可做杯盘不只首饰；smith 远源与 smite 不能一概定为同词。',
 'The locksmith and the silversmith use different tools for their trades.\n\n锁匠和银匠用不同工具从事各自的手艺。',
 'smith blacksmith goldsmith silversmith locksmith gunsmith wordsmith')
if __name__=='__main__':save('continuation_20261030_be',ROOTS,WORDS)
