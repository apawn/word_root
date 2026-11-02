"""Block and search: physical shapes, interrupted passage and active looking."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
BL=[['古法语 bloc〔上接日耳曼木块词〕→ 中古英语 blok','木块、树桩、整块'],['现代 block','块、街区；障碍；阻挡、屏蔽等支线']]
def B(f,m):return BL+[[f,m]]
W('block','英 /blɒk/；美 /blɑːk/','块；街区；一栋楼；阻挡、堵塞、屏蔽',
 '一整块东西放在那里，能成为建筑单位，也能把路挡住；后来的很多意思围绕块与挡。',
 '中古英语 blok 经古法语 bloc，后者接日耳曼木块、木料词。街区、楼体、成组事物及阻挡动作逐步发展，不要把现代每个 block 都想成真木头。',BL,
 'a block of wood 木块，a block of flats 一栋公寓楼，two blocks away 隔两个街区，block the road 堵路，block a user 屏蔽用户。',
 'a block of wood；a block of flats；two blocks away；block the road。',
 'block 可块、街区、阻挡；bloc 常指国家、团体结成的集团，是相关借词但现代拼写、常用范围不同。',
 ('A fallen tree was blocking the road.','倒下的树挡住了路。'),('The café is two blocks from the station.','咖啡馆离车站两个街区。'))
W('blockage','英 /ˈblɒkɪdʒ/；美 /ˈblɑːkɪdʒ/','堵塞；堵塞物',
 '本该通畅的管道、通路里卡住了东西；既能说堵住的情况，也能指那处堵塞。',
 'block + -age，形成结果、情况等名词。后缀不是 age 年龄，读音也不是独立 age。',B('block + -age → blockage','受阻、堵塞的状态或堵塞物'),
 'a blockage in the pipe 管道堵塞，clear a blockage 清除堵塞，a drainage blockage 排水堵塞。',
 'a blockage in；clear a blockage；a drainage blockage。',
 'blockage 结果和堵塞处，blocker 执行阻挡的人、工具；blockade 则常是有组织的封锁。',
 ('A blockage in the pipe caused the sink to overflow.','管道堵塞导致水槽溢水。'),('The plumber cleared the blockage.','水管工清除了堵塞。'))
W('blocker','英 /ˈblɒkə/；美 /ˈblɑːkər/','阻挡者；阻碍物；拦截工具',
 '挡在前面的人、东西或软件工具；项目里也可说某个问题卡住了后续进展。',
 'block + -er，中古英语已有对应形式。人物、工具、障碍的具体指向随使用场景专门化。',B('block + -er → blocker','执行阻挡的人、器具；阻碍事项'),
 'an ad blocker 广告拦截工具，a pop-up blocker 弹窗拦截工具，a blocker for the project 项目障碍。',
 'an ad blocker；a pop-up blocker；remove a blocker。',
 'blocker 是阻碍者或工具，blockage 是堵塞状态、堵点；软件 ad blocker 不是广告本身。',
 ('The browser includes a pop-up blocker.','浏览器带有弹窗拦截工具。'),('The missing approval is the main blocker for the project.','缺少批准是项目的主要障碍。'))
W('unblock','英 /ʌnˈblɒk/；美 /ʌnˈblɑːk/','疏通；解除屏蔽、阻挡',
 '原来卡住、拦住了，现在把障碍移走，让水流、人或消息重新过得去。',
 'un- 逆转 + block。可解除实体堵塞，也可解除账户屏蔽等设置，具体结果看对象。',B('un- + block → unblock','解除阻挡、恢复通畅'),
 'unblock a drain 疏通排水管，unblock a contact 取消对联系人的屏蔽，unblock progress 让工作恢复推进。',
 'unblock a drain；unblock a contact；unblock progress。',
 'unblock 解除通路、屏蔽障碍，unlock 解锁；有锁的门和有堵塞的排水管不能都机械用同一个动词。',
 ('They used a tool to unblock the drain.','他们用工具疏通了排水管。'),('You can unblock the contact in the settings.','你可以在设置里取消对这个联系人的屏蔽。'))
W('blocky','英 /ˈblɒki/；美 /ˈblɑːki/','块状、方块感强的；像素块明显的',
 '轮廓不是细细圆圆的，而像一块块方料拼出来；低清图像也会露出一格格像素块。',
 'block + -y。按块的形状描述建筑、字形、图像等，不等于所有对象真的由木块制成。',B('block + -y → blocky','像块、方正厚重；图像呈块状'),
 'a blocky building 方正厚重的楼，blocky letters 方块感字形，a blocky image 像素块明显的图。',
 'a blocky building；blocky letters；a blocky image。',
 'blocky 说外观像块，blocked 说被挡住；a blocky image 不是必然因权限被屏蔽的图。',
 ('The game uses a deliberately blocky visual style.','游戏刻意采用方块感强的视觉风格。'),('The video became blocky when the connection slowed down.','连接变慢后，视频出现了明显的像素块。'))
W('blockade','英 /blɒˈkeɪd/；美 /blɑːˈkeɪd/','封锁；封锁行动；实施封锁',
 '不是偶然卡了一点，而是有组织地堵住港口、道路或物资进出。',
 'block + -ade，形成可能受荷兰语或德语相应封锁词影响，资料对具体类推路径有不同分析。-ade 在这里是名词构形，不要误读成把木块加进饮料。',B('block + -ade；欧陆同族形式影响 → blockade','有组织的阻隔、封锁；后亦作动词'),
 'a naval blockade 海上封锁，lift a blockade 解除封锁，blockade a port 封锁港口。',
 'a naval blockade；lift a blockade；blockade a port。',
 'block 泛指阻挡，blockade 常强调系统、有组织的封锁；blockage 更常是管道等发生堵塞。',
 ('The ships maintained a blockade of the port.','这些船维持着对港口的封锁。'),('Negotiators called for the blockade to be lifted.','谈判代表呼吁解除封锁。'),sources=['https://www.etymonline.com/word/blockade','https://en.wiktionary.org/wiki/blockade#English'])
W('blockbuster','英 /ˈblɒkbʌstə/；美 /ˈblɑːkbʌstər/','轰动、极卖座的作品；大片、畅销大作',
 '一出来就轰动市场，观众、销量都很惊人；电影里常说卖座大片。',
 'block 街区 + buster 摧毁者，原指能摧毁大片街区的重型炸弹，后来转指轰动、成功的作品或产品。不是因售票队绕过街区才造出。',B('block + buster → blockbuster','重型炸弹的名称 → 轰动、极卖座的大作'),
 'a summer blockbuster 夏季卖座大片，a blockbuster novel 畅销小说。常暗示巨大商业成功或相应规模的制作定位。',
 'a summer blockbuster；a blockbuster movie；a blockbuster novel。',
 'blockbuster 强调轰动、卖座等成功形象，masterpiece 强调杰作、艺术价值；两种评价可能重合，但不互相保证。',
 ('The film became an unexpected blockbuster.','这部电影出人意料地大卖。'),('The publisher hoped the novel would be a blockbuster.','出版社希望这本小说成为畅销大作。'),sources=['https://www.etymonline.com/word/blockbuster','https://en.wiktionary.org/wiki/blockbuster#English'])
W('blockchain','英 /ˈblɒktʃeɪn/；美 /ˈblɑːktʃeɪn/','区块链',
 '把一批记录收成一个区块，再按规则与前面的区块相连，形成可核验的记录链。',
 'block 区块 + chain 链，由早期分写的 block chain 等表达固定为一词。这里只讲词和基本结构，不把名称当成所有系统性能的保证。',B('block + chain → blockchain','相连的记录区块 → 区块链技术名称'),
 'a blockchain network 区块链网络，a blockchain record 区块链记录。词首 block 是数据区块，不是网页被屏蔽。',
 'a blockchain network；blockchain records；blockchain technology。',
 'blockchain 是技术、记录结构类别，cryptocurrency 是加密货币；有相关应用，但两词不等同。',
 ('The course explains how records are linked in a blockchain.','课程解释了区块链中的记录如何相连。'),('The team tested a blockchain system for tracking shipments.','团队测试了一个用于追踪货运的区块链系统。'))
W('blockhead','英 /ˈblɒkhed/；美 /ˈblɑːkhed/','笨蛋、木头脑袋〔侮辱用语〕',
 '骂人脑袋像木块一样不开窍，是比较直白的贬人说法。',
 'block 木块 + head 头。借木块僵硬、不灵活的形象称人，并非客观智力评估术语。',B('block + head → blockhead','木块般的脑袋 → 笨蛋的骂人称呼'),
 'call someone a blockhead 骂某人笨蛋；现在常带旧式、戏剧化语气，仍是侮辱。',
 'call someone a blockhead；a complete blockhead；the blockhead in the story。',
 'blockhead 骂人不开窍，blocky head 只是块状头形的描述；不能拿外形词自动推出人格、能力。',
 ('The angry character calls his servant a blockhead.','愤怒的角色骂仆人是个木头脑袋。'),('He felt like a blockhead after missing the obvious clue.','漏掉明显线索后，他觉得自己真笨。'))
R('B3767','整块、街区和阻挡；堵塞、疏通、封锁及固定比喻','BLOCK：一整块；挡在路上就形成阻碍','block → blockage、blocker、unblock、blocky；blockade 组织封锁，blockbuster 保留真实炸弹来源，blockchain 数据链；共有 roadblock、sunblock、woodblock。',
 '别把所有复杂词拆完就死译：blockbuster 的商业成功义有历史转用，blockchain 的 block 是数据区块。',
 'block + -age/-er/-y/-ade；un- + block；block + buster/chain/head；road/sun/wood + block。',
 [['基本形状、阻挡和解除','block · blockage · blocker · unblock · blocky'],['组织阻挡','blockade · roadblock · sunblock'],['固定发展与组合','blockbuster · blockchain · blockhead · woodblock']],
 'block/bloc 区分常用拼写；blockage 堵塞、blockade 封锁；blockbuster 卖座不保证艺术杰作；blockchain 不等于货币。',
 'A fallen block caused a blockage, and workers returned to unblock the road.\n\n一块掉落的材料造成堵塞，工人回来疏通道路。',
 'block blockage blocker unblock blocky blockade roadblock sunblock blockbuster blockchain blockhead woodblock')
SE=[['晚期拉丁 circāre → 古法语 cerchier、盎格鲁法语 sercher','绕行、到处走查 → 寻找'],['中古英语 serchen → search','搜寻、查找、搜查']]
W('search','英 /sɜːtʃ/；美 /sɜːrtʃ/','搜寻、查找；搜查；搜索',
 '不是等答案自己来，而是主动翻、看、查，想把藏着或未知的东西找出来。',
 '经中古英语 serchen，接法语相关形式与晚期拉丁 circāre 绕行、走查，最终联系 circus 圆圈。学习时可想四处找，但不是每次搜索都真绕圈走。',SE,
 'search the room for keys 在房间找钥匙；search for keys 找钥匙。前者直接对象是查的范围，for 后面才是目标。',
 'search for；search the room；in search of；a search engine。',
 'search the bag 搜包，search for the bag 找包；seek 直接接寻找目标常不加 for，不能照一个句型全套。',
 ('We searched the house for the missing keys.','我们在屋里寻找丢失的钥匙。'),('She searched online for a suitable course.','她上网寻找合适的课程。'),sources=['https://www.etymonline.com/word/search','https://en.wiktionary.org/wiki/search#English'])
W('searcher','英 /ˈsɜːtʃə/；美 /ˈsɜːrtʃər/','搜寻者；搜索的人',
 '负责或正在找东西的那个人；强调主动查找，不是搜索结果本身。',
 '现代可对应 search + -er，历史有中古英语 serchour、sercher，接法语 cercheor 等相应人物词。',SE+[['法语人物词及中古英语 serchour、sercher → searcher','寻找、搜查的人；现代对应 search + -er']],
 'rescue searchers 搜救寻找人员，an online searcher 上网查找信息的人。',
 'rescue searchers；an online searcher；the searchers found。',
 'searcher 人，search engine 搜索引擎；search results 搜索结果。结尾 -er 不是结果名词。',
 ('The searchers found footprints beside the river.','搜寻人员在河边发现了脚印。'),('An experienced searcher knows how to narrow the query.','有经验的搜索者知道怎样缩小查询范围。'))
W('searchable','英 /ˈsɜːtʃəbl/；美 /ˈsɜːrtʃəbl/','可搜索、可检索的',
 '内容能被查询、定位；不必一页页靠眼睛慢慢翻。',
 'search + -able，可被搜索、具备检索条件。常用于文档、数据库、网站内容。',SE+[['search + -able → searchable','可以搜索、检索的']],
 'a searchable database 可检索数据库，searchable text 可搜索文本，make the archive searchable 让档案可检索。',
 'a searchable database；searchable text；a searchable archive。',
 'searchable 可检索不等于公开给所有人；publicly accessible 公开可访问是权限问题，两个性质可分开。',
 ('The library created a searchable archive of old newspapers.','图书馆建立了可检索的旧报纸档案。'),('The scanned pages were converted into searchable text.','扫描页面被转换成了可搜索文本。'))
R('B3210','主动四处查找；查的范围与寻找目标分清','SEARCH：主动翻查，寻找未知或藏着的东西','search → searcher → searchable；searchlight 既有精讲共享；重点掌握 search a place for something。',
 '来源的绕行、走查可帮助想象主动寻找；今天网络查询不需要真的绕圈。',
 'search + -er/-able；search + light；search 范围 + for 目标。',
 [['动作、人和可检索性','search · searcher · searchable'],['寻找的工具','searchlight']],
 'search the bag 搜包，search for the bag 找包；searchable 可检索不自动说明公开权限。',
 'The searcher used a searchable archive to search for an old photograph.\n\n查找者用可检索档案寻找一张旧照片。',
 'search searcher searchable searchlight')
if __name__=='__main__':save('continuation_20261030_at',ROOTS,WORDS)
