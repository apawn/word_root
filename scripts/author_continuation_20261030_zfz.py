"""Rummaging, ransacking, digging into details and sifting evidence."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2701':dict(words='room rummage rummages rummaged rummaging'.split(),label='rummage：从船舱货物安排到翻找',note='rummage 常解释为法语 arrumage 一路的缩短，较远可能联系 room 的空间词族；另有直接 room 加 -age 的分析，不把路线统一成唯一确定的现代拼造。'),
 'B2966':dict(words='seek ransack ransacks ransacked ransacking'.split(),label='ransack：旧北欧语的搜屋材料',note='接北欧 rann 房屋加 saka 搜查的组合，后半与 seek 所属的寻找材料相关；现代常说翻箱倒柜、洗劫，不把 sack 袋子当确定原始后半。'),
 'B2845':dict(words='dig delve delves delved delving'.split(),label='delve 与 dig 的挖掘、深查对照',note='delve 承古英语 delfan，dig 是另一组旧挖掘材料；这里并列近义动作，不说二者是现代同一词根直接派生。delve 的旧强变化后来转为常见规则 delved。'),
 'A1760':dict(words='sift sifts sifted sifting sieve sieves sieved sieving'.split(),label='sift、sieve 的筛选动作与现代过去词尾',note='sift 承古英语 siftan，sieve 名词承 sife，二者有旧词族联系；现代 sieve 动词由器具名转用。sifted 读 /ɪd/，sieved 读 /d/。'),
 'B4517':dict(words='scrutiny scrutinize scrutinizes scrutinized scrutinizing scrutinise scrutinises scrutinised scrutinising'.split(),label='scrutiny 到 scrutinize、scrutinise 的仔细审查',note='scrutiny 去末 y 加 -ize、-ise 构成动词；两套拼写的现代词形并排。更早拉丁 scrutari 的搜查词源有废物中翻找、刮切等不同分析，不选一个编成确定画面。'),
 'C1131':dict(words='probe probes probed probing'.split(),label='probe：探查器具与深入追问',note='名词接中世纪拉丁 proba 检查，远接 probare 测试；动词既有名词转用也有拉丁词影响。英语动词抽象调查记录早于其具体用探针检查的用法，不把所有动词义倒排成先物后喻。'),
 'C1379':dict(words='inspect inspects inspected inspecting'.split(),label='inspect：把目光投向内部细查',note='拉丁 in- 加 specere 形成 inspicere，其 inspect- 词干借入英语；现代 inspected、inspecting 是英语词尾扩展。'),
}
RUMMAGE=[['法语 arrumage 安排船舱货物等 → 英语 rummage 名词','较远可能联系日耳曼空间、room 词族；也有直接由 room 加 -age 的分析'],['安排货物 → 翻动货物、仔细翻找','现代常是把一堆东西拨开、翻来翻去寻找；别把早期整理义和现在弄乱的画面硬说成完全一样']]
W('rummage','/ˈrʌmɪdʒ/','翻找；翻来翻去搜寻；一次翻找',
 '钥匙在包里，可不知压在哪层，只好把里面东西拨来拨去地找，这叫 rummage。能让人看见手在一堆东西里翻动。',
 '常解释为法语 arrumage 的缩短，原与船舱货物安排相关，较远可能接 room 空间词族；更早路线仍有不同分析。',RUMMAGE,
 'rummage through a bag 翻包寻找；rummage around in a drawer 在抽屉里翻找；have a rummage 翻找一番。',
 'rummage for the keys 翻找钥匙；a rummage sale 旧物义卖，名称有早期货物出售背景。',
 'search 比较一般，rummage 特别让人看到把杂物翻动的动作，不只是输入一个搜索词。',
 ('I had to rummage through my bag to find the keys.','我只好把包翻了一遍，才找到钥匙。'),('Have a rummage in the drawer; there may be a spare cable.','在抽屉里翻翻，也许有一根备用线。'),sources=S('rummage','rummage'))
W('rummages','/ˈrʌmɪdʒɪz/','翻找〔第三人称单数〕；几次翻找〔复数〕',
 '他一到门口就把口袋翻来翻去找钥匙，这个经常发生的动作可以写 rummages；几次翻找也同形。',
 'rummage + -s，/dʒ/ 后词尾读 /ɪz/；动词三单与名词复数同形。',RUMMAGE+[['rummage + -s → rummages','他、她翻动东西寻找；多次翻找']],
 'rummages in his pockets 在口袋里翻找；rummages through old boxes 翻找旧箱子。',
 'rummages around for a pen；rummages through the cupboard。',
 'rummages for 后接想找的东西，rummages through 后接翻找的范围：for a pen、through a bag。',
 ('He rummages in his pockets whenever the phone rings.','电话一响，他就翻口袋找手机。'),('She rummages through old boxes looking for family photos.','她翻着旧箱子，寻找家人的照片。'),sources=S('rummages','rummage'))
W('rummaged','/ˈrʌmɪdʒd/','翻找了；把东西翻来翻去搜寻了',
 '刚才把抽屉、旧盒子翻了一阵，东西一件件挪开，想找出某个目标，这叫 rummaged。',
 'rummage 去 e 加完整 -ed，词尾读 /d/；/dʒd/ 连发，和三单 rummages 的 /dʒɪz/ 区别开。',RUMMAGE+[['rummage → rummaged','过去翻动一堆东西寻找']],
 'rummaged through the papers 翻找那堆纸；rummaged in a drawer 在抽屉里翻找。',
 'rummaged around for a torch；rummaged through the attic。',
 'rummaged 不保证已经找到；要表达找到，可另接 and found 或 to find 的结果场景。',
 ('We rummaged through the cupboard for a torch.','我们在柜子里翻找手电筒。'),('She rummaged in her bag and found the receipt.','她在包里翻了一阵，找到了收据。'),sources=S('rummaged','rummage'))
W('rummaging','/ˈrʌmɪdʒɪŋ/','正在翻找；翻动搜寻的过程',
 '抽屉开着，手把里面东西挪到这边、拨到那边，人还在找，这个进行中的画面叫 rummaging。',
 'rummage 去 e 加 -ing，保留基础 /dʒ/；-ing 把整个翻找动作放进进行中的场景。',RUMMAGE+[['rummage → rummaging','翻动杂物寻找正在进行']],
 'rummaging through a suitcase 翻行李箱；rummaging around in the kitchen 在厨房里四处翻找。',
 'caught someone rummaging 撞见某人在翻找；spent an hour rummaging。',
 'rummaging 通常有触手拨弄的实体画面；searching online 只是网上检索，通常不带翻动物件的动作。',
 ('I found him rummaging through a pile of old letters.','我发现他正在一堆旧信里翻找。'),('We spent an hour rummaging in the attic.','我们在阁楼里翻找了一个小时。'),sources=S('rummaging','rummage'))
RANSACK=[['北欧 rann 房屋 + saka 搜查 → rannsaka 等 → ransack','后半与 seek 的寻找材料相关；现代末尾可能受 sack 洗劫影响'],['彻底搜查、劫掠 → 翻箱倒柜、洗劫一空','现代常让人看到东西被翻得乱七八糟；也可夸张说自己翻遍各处']]
W('ransack','/ˈrænsæk/','翻箱倒柜地搜查；洗劫',
 '抽屉全拉开，柜子翻遍，东西散在地上，这种彻底而可能粗暴的翻找叫 ransack。盗贼洗劫房子也常用它。',
 '接旧北欧语房屋 rann 加搜查 saka 的组合，后半与 seek 词族相连；现代 sack 拼写可能受洗劫词影响，构词关系需回到北欧语的房屋加搜查材料理解。',RANSACK,
 'ransack a house 洗劫、翻遍房子；ransack the drawers 把抽屉翻个遍；ransack the archives 夸张说翻遍档案。',
 'ransack the room；ransack the cupboards for a key。',
 'rummage 常写一阵翻找，ransack 更强烈，容易带彻底翻遍、弄乱甚至洗劫的结果。',
 ('The thieves began to ransack the empty house.','盗贼开始洗劫那栋空房子。'),('We had to ransack every drawer to find the old photograph.','我们翻遍了每个抽屉，才找到那张老照片。'),sources=S('ransack','ransack'))
W('ransacks','/ˈrænsæks/','翻箱倒柜搜查、洗劫〔第三人称单数〕',
 '他找一件小东西，却把柜子、抽屉都翻开，弄得像整个地方都被搜过一遍，动词用 ransacks。',
 'ransack + -s，/k/ 后读 /s/；基础词是北欧搜屋材料一路借入的。',RANSACK+[['ransack + -s → ransacks','他、她彻底翻找或洗劫某处']],
 'ransacks the kitchen 翻遍厨房；ransacks the house for a document 把家里翻个遍找文件。',
 'ransacks every cupboard；ransacks a shop。',
 'ransacks 通常接被翻找、洗劫的地方；要找的目标常另用 for 接出来。',
 ('He ransacks the kitchen whenever he cannot find a snack.','他一找不到零食，就把厨房翻个底朝天。'),('In the story, a gang ransacks the abandoned shop.','故事里，一伙人洗劫了那家废弃商店。'),sources=S('ransacks','ransack'))
W('ransacked','/ˈrænsækt/','翻箱倒柜搜查了；遭洗劫的；被翻乱了的',
 '回家一看，柜门开着、抽屉倒空，东西全乱了，可以说 the house was ransacked。也能说自己为了找东西把房间翻遍了。',
 'ransack + 完整 -ed，/k/ 后词尾读 /t/；主动过去式、被动或结果状态都可出现。',RANSACK+[['ransack + -ed → ransacked','过去彻底翻找、洗劫；也写被翻乱的结果']],
 'a ransacked room 被翻得乱七八糟的房间；ransacked the house for the papers 为找文件翻遍屋子。',
 'returned to find the flat ransacked；ransacked every drawer。',
 'ransacked 比 untidy 更能暗示翻找、洗劫造成的乱；普通乱放物品不一定要用这个词。',
 ('We came home to find the flat ransacked.','我们回家发现公寓被翻得乱七八糟。'),('I ransacked every cupboard for the missing charger.','为了找丢失的充电器，我翻遍了每个柜子。'),sources=S('ransacked','ransack'))
W('ransacking','/ˈrænsækɪŋ/','正在翻箱倒柜搜查、洗劫；彻底翻找的过程',
 '东西还在被一件件翻出来，抽屉还在被拉开，整个房间正被搜个遍，这段过程叫 ransacking。',
 'ransack + -ing，保留末尾 k；既能作进行形式，也可把翻遍、洗劫当作活动名词。',RANSACK+[['ransack + -ing → ransacking','彻底翻找、洗劫正在进行或作为一件事']],
 'ransacking the house 翻遍、洗劫屋子；caught someone ransacking a drawer 撞见某人翻箱倒柜。',
 'the ransacking of the office；ransacking cupboards for food。',
 'searching 更中性，ransacking 常给人强烈、彻底翻动的画面；写认真整理资料时不必随便加这种破坏感。',
 ('I found him ransacking the cupboard for biscuits.','我发现他正把柜子翻个底朝天找饼干。'),('The film shows thieves ransacking an empty office.','电影里，盗贼正在洗劫一间空办公室。'),sources=S('ransacking','ransack'))
DELVE=[['古英语 delfan：用铲等挖掘 → 中古英语 delven → delve','原是强变化动词，后来逐渐出现规则词尾形式'],['挖土往深处去 → 深入查究、翻查材料','现代常见 delve into，像把资料、问题一层层往下挖']]
W('delve','/delv/','深入探究；翻查；挖掘',
 '表面答案还不够，于是继续翻资料、问细节，像把土一铲铲挖开，叫 delve。今天常在深入查究的句子里见到。',
 '承古英语 delfan 挖掘；现代 delve into 的抽象用法由往里挖的动作帮助理解。dig 是另一组旧词，不是 delve 的现代缩短。',DELVE,
 'delve into the records 深入翻查记录；delve into a problem 深入探究问题；delve into a bag 伸进包里翻找。',
 'delve deeper；delve into the past。',
 'look into 可以一般地调查一下，delve into 更容易突出继续往深处查、翻出更多层次。',
 ('We need to delve deeper into the cause of the problem.','我们需要更深入地查清问题原因。'),('She likes to delve into old family records.','她喜欢深入翻查旧家族记录。'),sources=S('delve','delve'))
W('delves','/delvz/','深入探究、翻查〔第三人称单数〕',
 '文章没有停在表面介绍，而是继续往细节、原因里钻，可以说 it delves into the subject。',
 'delve + -s，/v/ 后词尾读 /z/，结尾 /lvz/；不另添 /ɪz/。',DELVE+[['delve + -s → delves','他、她、它往细节、深层资料里查究']],
 'delves into the history 深入探究历史；delves into the reasons 深究原因。',
 'a chapter that delves into the evidence；delves below the surface。',
 'delves 主要说探究的深入程度，summarizes 则把内容收拢成摘要；同一篇文章可以前面深查、后面概括。',
 ('The book delves into the history of the city’s markets.','这本书深入探究了这座城市集市的历史。'),('The final chapter delves deeper into the evidence.','最后一章更深入地分析了证据。'),sources=S('delves','delve'))
W('delved','/delvd/','深入探究、翻查了；挖掘了',
 '过去为了弄清楚一件事，翻开旧档案、继续往前追查，像把埋着的信息挖出来，就用 delved。',
 'delve 去 e 加完整 -ed，词尾读 /d/；古英语曾有强变化，现代常用 delved 是后来规则化的形式。',DELVE+[['delve → delved','现代规则过去式，写过去深入翻查、探究']],
 'delved into the archives 深入翻查档案；delved into her bag 伸进包里翻找。',
 'delved into the details；delved deeper。',
 'delved into her bag 是具体的伸手翻找，delved into her past 是查究过去；看 into 后面是什么，确定画面。',
 ('We delved into the archives to find the original plan.','我们深入翻查档案，寻找最初的方案。'),('She delved into her bag and pulled out a notebook.','她伸进包里翻了翻，拿出一本笔记本。'),sources=S('delved','delve'))
W('delving','/ˈdelvɪŋ/','正在深入探究、翻查；挖掘',
 '问题还在一层层被打开，资料还在往更深处翻，这种持续深入的过程叫 delving。',
 'delve 去 e 加 -ing，/v/ 保留；into 常引出正在深入的资料、话题或空间。',DELVE+[['delve → delving','把继续深入翻查的过程放到眼前']],
 'delving into the records 深入翻查记录；delving into a mystery 探究谜团；delving through old boxes 翻查旧箱子。',
 'spend time delving into the past；delving beneath the surface。',
 'delving 强调挖进去的过程，不保证最后能得出结论；a discovery 才是某项实际发现。',
 ('She spent the afternoon delving into old newspapers.','她花了一个下午深入翻查旧报纸。'),('We are delving into why the first attempt failed.','我们正在深入探究第一次尝试为何失败。'),sources=S('delving','delve'))
SIFT=[['古英语 siftan → 中古英语 siften → sift','让细小部分通过筛孔，与 sieve 的旧筛具名词同族'],['筛面粉、细料 → 仔细翻看、筛选资料','像筛子一样，逐项检查，留下或挑出需要的内容；抽象用法已有很长历史']]
W('sift','/sɪft/','筛；仔细筛查、翻检',
 '面粉过筛，细粉落下，大块留下；看几百页材料时也一项项过一遍、挑出需要的，这就叫 sift。',
 '承古英语 siftan，与 sieve 筛子属于旧词族；它们是历史上相关的不同形式，现代分别保留。',SIFT,
 'sift the flour 筛面粉；sift through the evidence 仔细筛查证据；sift out the irrelevant parts 筛掉无关部分。',
 'sift through applications 筛查申请；sift fact from fiction 分清事实与虚构。',
 'sift 强调从一堆内容里逐项检查、分出所需；skim 是快速浏览，通常没这么细。',
 ('Sift the flour into a large bowl.','把面粉筛进大碗里。'),('We need time to sift through all the applications.','我们需要时间仔细筛查所有申请。'),sources=S('sift','sift'))
W('sifts','/sɪfts/','筛、仔细筛查〔第三人称单数〕',
 '程序一条条看记录，编辑一份份挑材料，像用筛子过东西，动词可用 sifts。',
 'sift + -s，词尾读 /s/，基础 /ft/ 保留，结尾 /fts/；现代三单按规则加词尾。',SIFT+[['sift + -s → sifts','他、她、它逐项筛选或让东西过筛']],
 'sifts through reports 仔细筛查报告；sifts flour 筛面粉；sifts out unwanted entries 筛掉不需要的条目。',
 'sifts the evidence；sifts through the pile。',
 'sifts through 后面通常是待翻检的一堆材料；sifts out 后面通常是被分出、剔除的部分。',
 ('The editor sifts through dozens of submissions each week.','编辑每周都会仔细筛看几十份投稿。'),('She sifts the flour before adding it to the mixture.','她把面粉加入混合物前，会先筛一遍。'),sources=S('sifts','sift'))
W('sifted','/ˈsɪftɪd/','筛过了；仔细筛查了；筛过的',
 '面粉已经过了筛，变得细匀，叫 sifted flour；那一堆材料已经仔细看过、挑过，也可以说 sifted through。',
 'sift + 完整 -ed，基础以 /t/ 结尾，词尾读 /ɪd/；不是去掉 t 再造过去式。',SIFT+[['sift + -ed → sifted','过去筛选；或已经过筛的结果']],
 'sifted flour 筛过的面粉；sifted through the records 仔细翻查过记录。',
 'sifted the evidence；sifted out the duplicates 筛掉了重复项。',
 'sifted through 不保证已找到答案，只说仔细翻查过；要表达筛出了什么，再接 out 或说明结果。',
 ('Add the sifted flour a little at a time.','把筛过的面粉一点点加进去。'),('We sifted through the records for a clue.','我们仔细翻查记录，寻找线索。'),sources=S('sifted','sift'))
W('sifting','/ˈsɪftɪŋ/','正在筛、筛查；筛选过程',
 '筛子还在晃，或材料正一项项被翻过、分开，这段过程就是 sifting。',
 'sift + -ing；既可组成进行式，也可把筛查作为一个过程来讨论。',SIFT+[['sift + -ing → sifting','过筛、逐项筛查正在进行；也作过程名词']],
 'sifting flour 筛面粉；sifting through emails 仔细翻找邮件；the sifting of evidence 证据筛查。',
 'spend hours sifting；careful sifting 仔细筛选。',
 'sifting 是筛查过程，sorting 更一般地说分类、排列；可以先筛出相关材料，再按时间排序。',
 ('She was sifting flour while I prepared the tin.','我准备烤模时，她正在筛面粉。'),('He spent hours sifting through old emails.','他花了几个小时仔细翻找旧邮件。'),sources=S('sifting','sift'))
SIEVE=[['古英语 sife → 中古英语 sive → sieve','有网孔的筛具，与 sift 的过筛动词有旧词族联系'],['筛具名词 → 动词 sieve','从器具转为用器具过筛，现代还能把不断漏掉东西的状态比作筛子']]
W('sieve','/sɪv/','筛子；过滤器；筛、过滤',
 '一张细网装在框里，小的从孔里过，大的留在上面，这就是 a sieve；拿它筛东西，动词也叫 sieve。',
 '名词承古英语 sife，动词后来由名词转用；现代 ie 组合在这里读 /ɪ/，末尾读 /v/。',SIEVE,
 'a fine sieve 细筛；sieve the flour 筛面粉；a memory like a sieve 是记性差，像筛孔一样把事情漏走。',
 'put through a sieve 过筛；sieve out the lumps 筛掉结块。',
 'sieve 常能直接指手里的筛具，sift 通常是过筛、筛查的动作；两个词能在筛面粉场景相遇。',
 ('Pour the mixture through a fine sieve.','把混合物倒过细筛过滤。'),('Sieve the flour before you add the eggs.','加鸡蛋前，先把面粉筛一遍。'),sources=S('sieve','sieve'))
W('sieves','/sɪvz/','筛子、过滤器〔复数〕；筛、过滤〔第三人称单数〕',
 '几只网孔大小不同的筛子是 sieves；她每次都把面粉过筛，动词也写 sieves。',
 'sieve + -s，/v/ 后词尾读 /z/；读 /sɪvz/，不因拼写 ie 就念成长 /iː/。',SIEVE+[['sieve + -s → sieves','多个筛具；它、他、她筛、过滤']],
 'fine sieves 细筛；sieves the sauce 把酱汁过筛；a set of sieves 一套筛具。',
 'sieves of different sizes；sieves the dry ingredients。',
 'sieves 作工具名词是几只筛子，sifts 作动词是筛；读句子时先看前面是不是 a set of、she 等结构。',
 ('The laboratory uses sieves with different mesh sizes.','实验室使用网孔大小不同的筛具。'),('She sieves the sauce to remove the seeds.','她把酱汁过筛，滤掉籽。'),sources=S('sieves','sieve'))
W('sieved','/sɪvd/','筛过、过滤了；已经过筛的',
 '酱汁从细网里过去，籽留在外面；面粉过完筛，这个已发生、已有结果的状态叫 sieved。',
 'sieve 去不发音 e 加完整 -ed，词尾读 /d/，结尾 /vd/；与 sifted 的两音节形式区分。',SIEVE+[['sieve → sieved','过去过筛；也形容已过滤的材料']],
 'sieved flour 过筛面粉；sieved tomatoes 筛滤过的番茄；sieved the mixture 把混合物筛过了。',
 'finely sieved 筛得细的；sieved through a fine mesh。',
 'sieved 强调用筛具处理；strained 也可泛说过滤液体，所用工具未必和筛面粉完全相同。',
 ('She sieved the flour into the bowl.','她把面粉筛进了碗里。'),('We sieved the sauce to remove the last few seeds.','我们把酱汁过筛，滤掉最后几颗籽。'),sources=S('sieved','sieve'))
W('sieving','/ˈsɪvɪŋ/','正在过筛、过滤；筛分过程',
 '东西正穿过网孔，粗细、大小被分开，这个进行中的动作或处理过程叫 sieving。',
 'sieve 去 e 加 -ing；保留 /v/，基础只有一个音节，接词尾后成为 /ˈsɪvɪŋ/。',SIEVE+[['sieve → sieving','用筛具分离材料正在进行；也作过程名词']],
 'sieving flour 筛面粉；sieving sand 筛沙；particle size analysis by sieving 用筛分分析颗粒大小。',
 'the sieving process；sieving out small stones。',
 'sieving 指过筛这个过程，a sieve 才是器具；表达需要一个筛子，不能把动作名词直接当工具名。',
 ('He was sieving sand to remove the small stones.','他正在筛沙，筛去小石子。'),('Sieving the flour helps break up lumps.','给面粉过筛有助于打散结块。'),sources=S('sieving','sieve'))
SCRUTINY=[['拉丁 scrutari 搜查 → scrutinium → scrutiny','远源有在废物中翻找、刮切等不同分析，具体路线不硬定'],['scrutiny 去 y 加 -ize → scrutinize；-ise 拼写为 scrutinise','由仔细审查的名词形成动词；两套现代拼写对应相同动作']]
W('scrutinizes','英 /ˈskruːtənaɪzɪz/；美 /ˈskruːtənaɪzɪz/','细查、仔细审视〔第三人称单数；-ize 拼写〕',
 '文件上每个数字都不轻放过，脸上的一点表情也认真看，这种把细节盯紧的检查叫 scrutinizes。',
 'scrutinize + -s，基础 /z/ 后词尾读 /ɪz/；更前面是 scrutiny 去 y 加 -ize。',SCRUTINY+[['scrutinize + -s → scrutinizes','他、她仔细查看细节、审查内容']],
 'scrutinizes the figures 细查数字；scrutinizes every detail 审视每个细节；scrutinises 是另一拼写。',
 'scrutinizes a face；scrutinizes the evidence。',
 'looks at 可以只是看一眼，scrutinizes 通常暗示持续注意细部、试图发现问题或弄清含义。',
 ('She scrutinizes every figure before approving the report.','批准报告前，她会细查每个数字。'),('He scrutinizes my face as if searching for a clue.','他仔细打量我的脸，像在寻找线索。'),sources=S('scrutinizes','scrutinize'))
W('scrutinized','/ˈskruːtənaɪzd/','细查、仔细审视了〔-ize 拼写〕',
 '刚才把细节放到眼前，一处处认真核对过，叫 scrutinized；也能说方案被人这样审查过。',
 'scrutinize 去 e 加完整 -ed，/z/ 后词尾读 /d/，结尾 /zd/；另一拼写 scrutinised 同读。',SCRUTINY+[['scrutinize → scrutinized','过去仔细审查；或作为被审查的形式']],
 'scrutinized the document 细查了文件；closely scrutinized 受到仔细审视。',
 'scrutinized the evidence；scrutinized for errors 为找错误而细查。',
 'scrutinized 说明检查很细，不保证一定找到错误；检查的力度与发现的结果要分开。',
 ('We scrutinized the photographs for any sign of damage.','我们仔细查看照片，寻找损坏迹象。'),('The proposal was scrutinized by several reviewers.','这项提案经过几位评审者仔细审查。'),sources=S('scrutinized','scrutinize'))
W('scrutinizing','/ˈskruːtənaɪzɪŋ/','正在细查、审视；仔细打量的〔-ize 拼写〕',
 '目光还停在细节上，数字、表情正被一点点检查，叫 scrutinizing；也能描述一种细细打量的眼神。',
 'scrutinize 去 e 加 -ing；对应 -ise 拼写是 scrutinising，两者用法和读音相同。',SCRUTINY+[['scrutinize → scrutinizing','仔细审查正在进行；也修饰目光等']],
 'scrutinizing the accounts 细查账目；a scrutinizing look 一种仔细打量的目光。',
 'spend hours scrutinizing；scrutinizing every line。',
 'scrutinizing 强调细看、细查；probing 更容易让人想到追问、探入内部，二者有时会同时用于同一次调查。',
 ('She was scrutinizing the map through a magnifying glass.','她正透过放大镜仔细查看地图。'),('He gave the damaged box a scrutinizing look.','他仔细打量了一下那个破损的箱子。'),sources=S('scrutinizing','scrutinize'))
W('scrutinises','/ˈskruːtənaɪzɪz/','细查、仔细审视〔第三人称单数；-ise 拼写〕',
 '一行一行地看，细微差别也不放过，动词可以写 scrutinises。它跟 scrutinizes 做的是同一件事。',
 'scrutinise + -s，词尾读 /ɪz/；-ise 常见于英式拼写，英式也可按所采用的规范使用 -ize。',SCRUTINY+[['scrutinise + -s → scrutinises','-ise 拼写下的动词三单']],
 'scrutinises the details 细查细节；scrutinises the evidence 审查证据；选择拼写时全文保持一致。',
 'scrutinises each application；scrutinises a new plan。',
 'scrutinises 与 scrutinizes 没有“一个更严格”的词义差别；力度由 closely、carefully 等和语境补充。',
 ('The panel scrutinises each application before making a decision.','小组会细查每份申请，再作决定。'),('She scrutinises the tiny print on the label.','她仔细看着标签上的小字。'),sources=S('scrutinises','scrutinize'))
W('scrutinised','/ˈskruːtənaɪzd/','细查、仔细审视了〔-ise 拼写〕',
 '那份记录已经一项项对过、认真看过，过去或被动句里可以用 scrutinised。重点是查得细。',
 'scrutinise 去 e 加完整 -ed，词尾读 /d/；与 scrutinized 同义、同读，保留各自 s、z 拼写。',SCRUTINY+[['scrutinise → scrutinised','-ise 形式的过去式、过去分词']],
 'scrutinised the report 细查了报告；was scrutinised 受到审查；carefully scrutinised 仔细审查过的。',
 'scrutinised every detail；scrutinised under good light。',
 'scrutinised 不等于 approved：仔细审查以后，可能通过，也可能驳回；动词本身不包办结论。',
 ('The report was scrutinised before publication.','报告发表前经过了仔细审查。'),('He scrutinised the old photograph for a familiar face.','他仔细看那张旧照片，寻找熟悉的面孔。'),sources=S('scrutinised','scrutinize'))
W('scrutinising','/ˈskruːtənaɪzɪŋ/','正在细查、审视；仔细打量的〔-ise 拼写〕',
 '眼睛还在仔细扫过每处细节，人还在审视、核对，叫 scrutinising；这个词也能修饰细察的眼神。',
 'scrutinise 去 e 加 -ing；先看基础动词的 -ise，再看外层 -ing，就能把动词形成与动作形式分清。',SCRUTINY+[['scrutinise → scrutinising','-ise 拼写下的进行形式、修饰形式']],
 'scrutinising the documents 正在细查文件；a scrutinising gaze 仔细审视的目光。',
 'scrutinising the small print；scrutinising each frame of the film。',
 'scrutinising 和 scrutinizing 用法相同，选择哪套拼写不影响审查对象、动作阶段。',
 ('The team is scrutinising the records for inconsistencies.','小组正在细查记录，寻找不一致之处。'),('She gave me a long, scrutinising look.','她仔仔细细地打量了我好一会儿。'),sources=S('scrutinising','scrutinize'))
PROBE=[['中世纪拉丁 proba 检查 → 英语 probe 名词','远接拉丁 probare 测试，早期名词可指探查器具、检查'],['probe 动词：深入调查，后也用探查器具检查','动词受名词和拉丁词影响；英语抽象动词记录较早，不倒排全部词义']]
W('probes','英 /prəʊbz/；美 /proʊbz/','探针、探测器、调查〔复数〕；探查、深入追问〔第三人称单数〕',
 '器具伸进去测里面，是 probes 的工具画面；问题一层层问，试着查出内情，动词也用 probes。太空探测器同样往未知处探。',
 'probe + -s，/b/ 后读 /z/；名词复数与动词三单同形。基础经拉丁检查、测试材料发展。',PROBE+[['probe + -s → probes','多个探查工具、调查；它、他、她深入探查']],
 'space probes 太空探测器；temperature probes 温度探针；probes the reasons 深入查究原因。',
 'probes beneath the surface；probes into the matter。',
 'probes 可能是器具或动作，先找句子的主语和谓语；two probes 是两个探测器，she probes 则是她在探查。',
 ('The mission uses two probes to study the planet.','这次任务用两个探测器研究那颗行星。'),('The interviewer probes the reasons behind each decision.','采访者深入追问每项决定背后的原因。'),sources=S('probes','probe'))
W('probed','英 /prəʊbd/；美 /proʊbd/','探查、深入调查了；追问了',
 '没有停在表面答案，而是继续试探、追问，想知道里面发生了什么，过去这种动作叫 probed。',
 'probe 去 e 加完整 -ed，词尾读 /d/，结尾 /bd/；不另加 /ɪd/ 音节。',PROBE+[['probe → probed','过去向深处调查、试探或探查']],
 'probed the cause 深入调查原因；probed for weak points 试探弱点；probed with questions 用问题追问。',
 'probed the gap with a stick；probed the issue further。',
 'probed 可以实际把工具伸进去，也可抽象追问；不要看见它就一律翻成用探针进行检查。',
 ('He probed the narrow gap with a stick.','他用木棍探了探那道窄缝。'),('The interviewer probed further when the answer was unclear.','答案不清楚时，采访者又进一步追问。'),sources=S('probed','probe'))
W('probing','英 /ˈprəʊbɪŋ/；美 /ˈproʊbɪŋ/','正在探查、深入调查；刨根问底的、洞察性的',
 '问题没有只问表面情况，而是一步步问到原因、矛盾处，这叫 probing questions；工具往里面探的过程也叫 probing。',
 'probe 去 e 加 -ing；可作动作形式，也作形容词，描述问得深、观察得透的特点。',PROBE+[['probe → probing','探查正在进行；也形容深入追问、观察']],
 'probing questions 深入追问的问题；a probing interview 追问得很深入的访谈；probing into the cause 查究原因。',
 'a probing look 试探、探究的目光；further probing 进一步探查。',
 'probing 强调往深处探，rude 强调失礼；问得深可能让人不舒服，但两个词评价的维度不同。',
 ('She asked several probing questions about the plan.','她就这个方案提出了几个刨根问底的问题。'),('The team is probing why the system stopped unexpectedly.','小组正在深入调查系统为什么意外停止。'),sources=S('probing','probe'))
INSPECT=[['拉丁 in- 向里 + specere 看 → inspicere','看进去、观察；inspectus 是相应过去分词形式'],['拉丁 inspect- 词干 → 英语 inspect','把对象看仔细、检查状态，现代再接英语规则词尾']]
W('inspects','/ɪnˈspekts/','检查、仔细查看〔第三人称单数〕',
 '不是路过看一眼，而是把物件各处看清，确认有没有问题，用 inspects。可以是机器、房屋，也可以是衣服上的破口。',
 'inspect + -s，/t/ 后词尾读 /s/；更前面是拉丁 in- + specere 一路，不是现代英语把独立词 spect 拼上去。',INSPECT+[['inspect + -s → inspects','他、她按检查目的仔细查看']],
 'inspects the equipment 检查设备；inspects the goods 检验货物；inspects the room 查看房间状态。',
 'inspects every item；inspects for damage 检查是否损坏。',
 'inspects 通常带检查对象状态的目的；admires 则是欣赏，即使都在认真看，意图也不同。',
 ('The mechanic inspects the brakes before every trip.','每次出车前，机械师都会检查刹车。'),('She inspects each piece of fruit for bruises.','她逐个查看水果有没有碰伤。'),sources=S('inspects','inspect'))
W('inspected','/ɪnˈspektɪd/','检查、仔细查看了；受过检查的',
 '机器已经看过一遍、状态已核对，或房间经过查看，可以说 inspected。这个词本身只说检查过，没保证一定合格。',
 'inspect + 完整 -ed，基础以 /t/ 结尾，词尾读 /ɪd/；拉丁词干借入后，现代过去式在英语里规则形成。',INSPECT+[['inspect + -ed → inspected','过去检查；也构成已经被检查的状态']],
 'inspected the roof 检查过屋顶；was inspected 受到检查；carefully inspected 仔细检查过的。',
 'inspected for damage；inspected before use。',
 'inspected 是检查过程发生过，approved 才是获准、通过；检查后的结论需要另说。',
 ('We inspected the roof after the storm.','暴风雨后，我们检查了屋顶。'),('Each parcel was inspected before it left the warehouse.','每个包裹出仓前都经过了检查。'),sources=S('inspected','inspect'))
W('inspecting','/ɪnˈspektɪŋ/','正在检查、仔细查看',
 '人正把注意力放到物件细节上，逐处看状态、找问题，这段进行中的检查就是 inspecting。',
 'inspect + -ing，基础 /kt/ 保留；与 inspected 的 /ɪd/ 词尾分清，时间作用不同。',INSPECT+[['inspect + -ing → inspecting','检查动作正在进行；也可把检查当作活动']],
 'inspecting the engine 检查发动机；inspecting the damage 查看损坏情况；inspecting a property 查看房屋状况。',
 'spend time inspecting；someone inspecting the equipment。',
 'inspecting 注重看、查状态；repairing 是动手修理。检查可能找出需要修理的地方，但两步不混成同一个动作。',
 ('The mechanic is inspecting the engine.','机械师正在检查发动机。'),('We spent the morning inspecting the old house.','我们整个上午都在仔细查看那栋老房子的状况。'),sources=S('inspecting','inspect'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfz',ROOTS,WORDS)
 extend_lessons()
