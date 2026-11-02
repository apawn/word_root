"""Practical adjectives, amounts, group nouns and familiar short expressions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3271':dict(words='brisk brisker briskest'.split(),label='brisk：另源的轻快、有活力；比较等级',note='与 quick 比较快速，不由 quick 派生。brisk 早见苏格兰 bruisk，来源不定，可能联系法语 brusque；不能把猜测远源硬定为直接来路。现代可用于动作轻快、业务活跃和天气清冷。'),
 'B3070':dict(words='curt'.split(),label='curt：缩短、简短 → 短得不客气',note='与 short 较远同接切短材料，但 curt 借拉丁 curtus，short 接古英语日耳曼语线；不是现代 short 随意变几个字母。简短后来带出唐突、不耐烦的语气。'),
 'B3714':dict(words='roster rosters'.split(),label='roster → rosters：烤架格子到名单表格',note='roster 借荷兰 rooster 表、名单，较早是烤架，和 roosten 烤一族相关；格子状烤架到纸上格子名单是常见的可能解释。不是现代英语 roast + -er 烤肉的人。'),
 'B3387':dict(words='loft lofts lofted lofting'.split(),label='loft → lofts、lofted、lofting：高处空间到击球上空',note='loft 接北欧 lopt 空中、上层空间等，英语有阁楼、高空间与后来的高击球动词。英语早期动词也曾表示存放进阁楼，不能说所有动词一开始都只指球类。'),
 'C1196':dict(words='quota quotas'.split(),label='quota → quotas：分到多少份、额度与配额',note='quota 接中古拉丁 quota，较远拉丁 quota pars 多大一份、quotus 第几个等数量词；复数后缀读 /z/。有时是上限，有时是分配量或目标，不把所有 quota 都说成最大限制。'),
 'C0163':dict(words='champ champion champs'.split(),label='champion → champ → champs：冠军的口语短称',note='champ 冠军缩略 champion，较远接拉丁 campus 场地、战场。另有拟声式咀嚼动词 champ，和冠军缩略分开；本轮先学常见人员称呼。'),
 'B3190':dict(words='brigade brigades'.split(),label='brigade：另源的旅、成队群体',note='与 group 比较群体，不由 group 派生。经法语 brigade 接意大利 brigata 队伍、brigare 争斗等材料，较远可能凯尔特或日耳曼语，尚不确定；fire brigade 是消防队。'),
 'B3122':dict(words='champagne champagnes'.split(),label='champagne：旷野词族 → 香槟地名 → 酒名',note='与 field 的现代英语来源分开；较远拉丁 campus 平野 → campania 开阔地 → 法国 Champagne 地名，vin de Champagne 的酒名缩成 champagne。与 champion 同在较远校园、场地词族附近，不是现代冠军饮品才造词。'),
 'A1776':dict(words='warren warrens'.split(),label='warren → warrens：养猎物地到兔穴网络、迷宫',note='与 rabbit 比较栖居空间并补复数，不由 rabbit 派生。warren 经法语 warenne 猎物保护区，远源有围起来的地区、保护等分析；兔子栖地到密集洞穴、房间通道网络。'),
 'B2476':dict(words='heck'.split(),label='hell → heck：语气较轻的替代说法',note='heck 是 hell 的委婉变形；what the heck、a heck of 等保留惊讶、强调的口语功能，不是每次都指地狱这个地方。'),
 'B2544':dict(words='babe babes baby'.split(),label='babe → baby；babe 的昵称、比喻用法',note='babe 接较早 baban 等幼儿称呼、可能拟幼儿语音；baby 历史上是 babe 接小称 -y，不能一律倒讲成 babe 是现代 baby 删 y。babe 后来作亲昵称呼，也有无经验者、吸引人者等口语比喻。'),
}
BRISK=[['苏格兰 bruisk 等 → 英语 brisk','来源不定，可能是法语 brusque 等的变体'],['轻快、有活力 → 生意活跃、天气清冷有劲','brisk + -er、-est 形成现代比较等级']]
LOFT=[['北欧 lopt：空气、天空、上层空间 → 英语 loft','天空与上层房间的更早先后有讨论，不强排一条唯一路线'],['上层、阁楼；存放入阁楼；后来击球到高空','现代用高处、上空的共同关系理解']]
CHAMP=[['拉丁 campus 场地 → 角斗、战斗者名称 → champion','英语 champion 后来常指比赛冠军'],['champion 缩为 champ → champs','冠军、能手的口语人员称呼；咀嚼动词另有来源']]
BRIGADE=[['意大利 briga 争斗 → brigare、brigata 队伍 → 法语 brigade','更远有凯尔特、日耳曼语等不同分析'],['英语 brigade：军中旅；一队从事共同事务的人','现代 fire brigade 是消防队，不要求一定是军队']]
CHAMPAGNE=[['拉丁 campus 平野 → campania 开阔地 → Champagne 地名','法国地区名保留开阔田野的远源'],['vin de Champagne 当地酒 → champagne','地名借给酒；英语复数可数不同种类、不同酒款']]
WARREN=[['法语 warenne 猎物保护区、饲养地 → 英语 warren','较远是围地区还是保护词族等，有不同分析'],['兔子生活区、洞穴网络 → 密集房间、通道的迷宫','比喻沿着很多小空间彼此连通的画面展开']]
BABE=[['baban 等幼儿称呼 → babe','可能拟幼儿易发的 ba 等音节，不按现代词根硬拆'],['babe + 小称 -y → baby；babe 自身继续发展','婴儿 → 亲昵称呼；无经验或吸引人的人等现代口语用法']]
W('brisk','英、美 /brɪsk/','轻快的、敏捷的；生意活跃的；清冷的',
 '迈步快而有精神，是 a brisk walk；顾客来得勤、交易不断，是 brisk business。风吹得清冷提神，也能用 brisk。',
 '早见苏格兰 bruisk 等，来源不定，可能联系法语 brusque 的活泼、强烈等材料。现代词义先抓轻快、有劲，不把可能的借入线写成唯一事实。',BRISK,
 'a brisk pace 是轻快步速；brisk business 是生意兴旺；a brisk wind 是清冷、有劲的风；动作和语气也可显得利落。',
 'a brisk walk；a brisk pace；brisk business；a brisk wind。',
 'quick 主要说快；brisk 常加上精神足、动作有劲的感觉。brisk reply 也可能显得干脆，但不必一定像 curt 那样失礼。',
 ('We went for a brisk walk before breakfast.','早饭前，我们精神十足地快走了一阵。'),('The shop did brisk business during the festival.','节日期间，这家店生意兴旺。'),sources=S('brisk','brisk'))
W('brisker','英 /ˈbrɪskə/；美 /ˈbrɪskɚ/','更轻快、更活跃的；更清冷有劲的',
 '脚下加快又不拖沓，是 a brisker pace；交易比刚才活跃，也能说 brisker business。比较的是活力、速度等程度。',
 'brisk + -er → brisker，词尾 sk 保留直接接比较级后缀，不双写 k。',BRISK+[['brisk + -er → brisker','现代形容词比较级，表更']],
 'a brisker pace 是更轻快的速度；a brisker trade 是更活跃的交易；具体比较哪一面由搭配决定。',
 'a brisker pace；brisker business；a brisker wind。',
 'brisker 的 -er 是比较级；不是“做 brisk 的人”。相同后缀字母要连着词性理解。',
 ('We set off again at a brisker pace.','我们以更轻快的步伐再次出发。'),('The market saw brisker trading after lunch.','午饭后，市场交易更活跃了。'),sources=S('brisker','brisk'))
W('briskest','英、美 /ˈbrɪskɪst/','最轻快、最活跃的；最有劲的',
 '一天当中最热闹、交易最快的一段，可以说 the briskest trading；一组步速里最轻快的一档，也能用 briskest。',
 'brisk + -est → briskest，后缀读 /ɪst/；保留基础词形，不双写 k。',BRISK+[['brisk + -est → briskest','最高级，比较范围内最轻快、最活跃']],
 'the briskest pace 是最轻快的步速；the briskest trade 是最旺的生意。语境要交代和什么时间、地方或对象比较。',
 'the briskest pace；the briskest trade；the briskest business。',
 'briskest 的比较范围常由句子、段落交代；the group、during the day 等能说明和谁、何时相比。',
 ('Sales were briskest just before the holiday.','假期前那阵子销售最活跃。'),('She kept up the briskest pace of the group.','她保持着全组最轻快的步伐。'),sources=S('briskest','brisk'))
W('curt','英 /kɜːt/；美 /kɝt/','简短而不客气的；唐突的',
 '问了一大段，对方只冷冷扔来一个“不行”，这种短得让人感觉被打发的回答，就是 curt。回答短得没有缓和，容易让人感到被敷衍。',
 '借拉丁 curtus 切短、缩短、不完整；较远接切的材料，早期英语也可只说简短，后来形成唐突、不客气的语气。',
 [['拉丁 curtus：切短、缩短 → 英语 curt','更远与 short 的切短材料有亲缘关系，但借入路线不同'],['简短、压缩 → 简短得唐突、不耐烦','现代日常常见于回复、语气、招呼']],
 'a curt reply 是简短冷淡的回复；a curt nod 是生硬点头；be curt with someone 是对某人说话很不客气。',
 'a curt reply；a curt nod；curt with someone。',
 'concise 赞内容简洁；curt 通常嫌语气生硬。相同长度的回复，是否照顾对方感受可能决定用哪个词。',
 ('He gave a curt reply and closed the door.','他冷冷回了一句，就关上门。'),('She apologised for being curt with me earlier.','她为先前对我说话生硬道了歉。'),sources=S('curt','curt'))
W('rosters','英 /ˈrɒstəz/；美 /ˈrɑstɚz/','名单、值勤表〔复数〕；列入名单〔第三人称单数〕',
 '谁在哪天值班、谁在这支队里，一份份排好的名单就是 rosters。它的格子表形象，较远还和烤架的格纹有关。',
 'roster + -s → rosters，后缀读 /z/。roster 借荷兰 rooster 表、名单，早先是烤架；通常认为格纹帮助连接表格义，但不是现代英语 roast + -er。',
 [['荷兰 rooster 烤架 → 格子表、名单 → 英语 roster','格纹到表格是可能的命名桥梁'],['roster + -s → rosters','多份名单、排班表；或列入名单动词单数']],
 'team rosters 是球队名单；duty rosters 是值勤表；staff rosters 是人员、排班名单。名单既可静态列人，也可按时间排任务。',
 'team rosters；duty rosters；staff rosters。',
 'rosters 和 roasters 烘烤者、烘烤设备拼写读音不同；两者较远有烤制词族联系，也不能把现代名单翻成烤炉。',
 ('The manager updated the duty rosters.','经理更新了值勤表。'),('Both clubs published their team rosters.','两家俱乐部都公布了队员名单。'),sources=S('rosters','roster'))
W('lofts','英 /lɒfts/；美 /lɑfts/','阁楼、上层空间〔复数〕；把球高击出去〔第三人称单数〕',
 '房子顶上的几处阁楼，是 lofts；球员把球高高挑起，是 she lofts the ball。高处空间和球飞向上空，用同一条高的关系相连。',
 'loft + -s → lofts，/t/ 后后缀读 /s/；名词接北欧 lopt 上层、天空等旧材料，动词后来也用于高击球。',LOFT+[['loft + -s → lofts','上层空间复数；或高击球的动词单数']],
 'converted lofts 是改建的阁楼空间；city lofts 也可指城市里开阔高挑的住宅空间；lofts the ball 是把球高高打起。',
 'converted lofts；city lofts；lofts the ball。',
 'lofts 在居住语境常是名词，在球员后面接 the ball 常是动词；不要因楼阁意思先学，就漏掉击球。',
 ('Several old lofts have been converted into studios.','几处旧阁楼已改成工作室。'),('She lofts the ball over the defender.','她把球高高挑过防守队员。'),sources=S('lofts','loft'))
W('lofted','英 /ˈlɒftɪd/；美 /ˈlɑftɪd/','高高击起了；被抬高的〔过去式、过去分词〕',
 '球被轻巧地挑到空中，画出一条高弧线，可以说 lofted。高击球是现代常见动作义，房间、床等也能被抬高放到上层。',
 'loft + -ed → lofted，基础末音 /t/ 后后缀读 /ɪd/；动词沿上层、上空关系发展，早期还有存入阁楼等用法。',LOFT+[['loft + -ed → lofted','过去式、过去分词；后缀增加一个音节']],
 'lofted the ball 是把球高挑出去；a lofted pass 是高吊传球；a lofted bed 可是抬高安置的床。',
 'lofted the ball；a lofted pass；a lofted bed。',
 'lofted 说明上抬、高飞的动作或结果；low pass 是低传，动作路线不同。',
 ('He lofted the ball towards the far post.','他把球高高吊向远门柱。'),('The room has a lofted bed above a small desk.','房间里把床架在一张小书桌上方。'),sources=S('lofted','loft'))
W('lofting','英 /ˈlɒftɪŋ/；美 /ˈlɑftɪŋ/','正在把球高击出去；抬高的过程',
 '球从脚边、拍前被向上送出，正在飞向高处，这个动作过程是 lofting。先用上空的路线理解，比死背一种球类术语更直观。',
 'loft + -ing → lofting；基础词尾 ft 保留直接接后缀，不双写 t。',LOFT+[['loft + -ing → lofting','现在分词、动名词；本组先学常见击球、抬高过程']],
 'lofting the ball 是把球高高击起；lofting a pass 是吊高传球；具体运动由上下文确定。',
 'lofting the ball；lofting a pass；lofting over a defender。',
 'lofting 在某些制作行业另有专门术语义，本组先掌握球被送向高空的常见动作，不把行业细节塞进基础理解。',
 ('She practised lofting the ball over a low net.','她练习把球高高打过低网。'),('He created a chance by lofting a pass over the defence.','他用一脚越过防线的高吊传球创造了机会。'),sources=S('lofting','loft'))
W('quotas','英 /ˈkwəʊtəz/；美 /ˈkwoʊtəz/','配额、分配量、限额；目标份额〔复数〕',
 '给每人分一份、给每组定一个量，这些份额就是 quotas。它可能是能用多少，也可能是要完成多少，方向由制度、任务决定。',
 'quota + -s → quotas，元音后后缀读 /z/。quota 接中古拉丁 quota，较远拉丁 quota pars 多大一份、quotus 第几个等数量材料。',
 [['拉丁 quota pars：多大一份 → 中古拉丁 quota → 英语 quota','分到某人的份额、数量'],['quota + -s → quotas','多项配额或分配量；末尾 /təz/']],
 'sales quotas 是销售目标量；production quotas 是生产配额、目标量；storage quotas 是存储限额。不能把所有组合都当成用量上限。',
 'sales quotas；production quotas；storage quotas。',
 'limit 常侧重不能超过的边界；quota 可以是分配量、目标或上限。看 meet a quota 还是 exceed a quota 等搭配更容易判断。',
 ('Each team has different sales quotas.','每个团队有不同的销售目标量。'),('The service assigns storage quotas to individual accounts.','这项服务为各账号分配存储限额。'),sources=S('quotas','quota'))
W('champ','英、美 /tʃæmp/','冠军；能手；〔熟络称呼〕好样的、伙计',
 'champion 太长，口语把它截成 champ。得冠军的人能这样叫；做得好、挺得住的人，也可能被朋友夸一句 champ。',
 'champion → champ，冠军称呼的缩略。champion 较远接法语、晚期拉丁战斗者名，来源于 campus 场地、战场；不是所有 champ 同形动词都由冠军派生。',CHAMP,
 'the world champ 是世界冠军；a chess champ 是国际象棋冠军；like a champ 常夸表现很好、很能扛事。',
 'the world champ；a chess champ；like a champ。',
 'champ at the bit 的 champ 是另条咀嚼、反复咬的动词；其中没有成为冠军的意思。这里先记冠军、夸人的常见称呼。',
 ('She became the club’s youngest chess champ.','她成了俱乐部最年轻的国际象棋冠军。'),('He handled the long journey like a champ.','这趟长途旅行，他应付得很棒。'),sources=S('champ','champ'))
W('champs','英、美 /tʃæmps/','冠军们；能手们〔复数〕',
 '几位冠军、拿过冠军的一队人，可以称 champs。它保留 champion 短称的轻松口吻。',
 'champ + -s → champs，/p/ 后后缀读 /s/；本组人员名词来自 champion，不以同形咀嚼动词解释。',CHAMP+[['champ + -s → champs','多个冠军、能手；末尾 /mps/']],
 'world champs 是世界冠军；defending champs 是卫冕冠军；former champs 是前冠军，具体个人还是队伍由语境决定。',
 'world champs；defending champs；former champs。',
 'champs 也可能是另源咀嚼动词的第三人称单数；赛事名单、champions 的短称语境里通常是人员名词。',
 ('The defending champs won their opening match.','卫冕冠军赢了首场比赛。'),('Several former champs attended the ceremony.','几位前冠军参加了典礼。'),sources=S('champs','champ'))
W('brigade','英 /brɪˈɡeɪd/；美 /brɪˈɡeɪd/','旅〔军事单位〕；队、团体',
 '一队人围着共同任务行动，可以叫 brigade。它有军中“旅”的正式用法，也有日常消防队、某种共同做派的人群用法。',
 '经法语 brigade 接意大利 brigata 队伍、brigare 争斗等，较远来源有凯尔特、日耳曼语等分析，未完全确定。',BRIGADE,
 'an army brigade 是陆军旅；a fire brigade 是消防队；某某 brigade 在口语里也能戏称有共同特征的一伙人。',
 'an army brigade；the fire brigade；a rescue brigade。',
 'brigade 的军队编制大小随国家、时期变化，词义学习先记单位层级；fire brigade 中则是从事消防的队伍，不要求军队身份。',
 ('The brigade moved to a new base.','这个旅转移到了新基地。'),('Someone had already called the fire brigade.','已经有人叫了消防队。'),sources=S('brigade','brigade'))
W('brigades','英、美 /brɪˈɡeɪdz/','旅；队伍、团体〔复数〕',
 '多支承担任务的队伍，或几个军事旅，是 brigades。整个群体单位可以数，一个 brigade 与其中几个人不是同一个层级。',
 'brigade + -s → brigades，基础词已有 e，再加 s；/d/ 后后缀读 /z/，不多一个音节。',BRIGADE+[['brigade + -s → brigades','多个军事单位或其他队伍；末尾 /dz/']],
 'fire brigades 是各支消防队；several brigades 是几个旅；rescue brigades 是救援队。',
 'fire brigades；several brigades；rescue brigades。',
 'brigades 数队伍；members of a brigade 数其中的人。一个集体名词复数，不代表每队只有一个人。',
 ('Fire brigades from nearby towns helped at the scene.','附近城镇的消防队赶到现场帮忙。'),('The history book describes the movements of three brigades.','这本历史书记述了三个旅的调动。'),sources=S('brigades','brigade'))
W('champagne','英、美 /ʃæmˈpeɪn/','香槟酒；香槟色',
 '庆祝时杯里冒着细泡的香槟，英语叫 champagne。名称来自法国地方，不是从“冠军喝的酒”拼出来，虽然它确实常出现在庆祝画面里。',
 '法语 vin de Champagne 香槟地区的酒，缩成 champagne；地区名较远接拉丁 campania 开阔地、campus 平野。地貌词变地名，地名再借给当地酒。',CHAMPAGNE,
 'a glass of champagne 是一杯香槟；a bottle of champagne 是一瓶；champagne colour 也可借酒色指浅金、米金一类颜色。',
 'a glass of champagne；a bottle of champagne；champagne colour。',
 'sparkling wine 是起泡酒的泛称，champagne 则带具体名称、产区背景。词源上的“开阔地”不能直接给出酒的现代制作方式。',
 ('They raised a glass of champagne to celebrate.','他们举起一杯香槟庆祝。'),('The invitation was printed on champagne-coloured paper.','邀请函印在香槟色的纸上。'),sources=S('champagne','champagne'))
W('champagnes','英、美 /ʃæmˈpeɪnz/','不同香槟酒、不同香槟酒款〔复数〕',
 '酒单或品尝活动里，比较不同酒款，可以说 several champagnes。这里数的是种类、款式，不是在把每一滴酒数成一份。',
 'champagne + -s → champagnes，末音 /n/ 后加 /z/。不可数酒液名在谈不同品种、酒款时转为可数复数。',CHAMPAGNE+[['champagne + -s → champagnes','多款、不同种香槟；不是普通酒液必加复数']],
 'different champagnes 是不同款香槟；a selection of champagnes 是多款可选香槟；two glasses of champagne 仍按杯数酒液。',
 'different champagnes；a selection of champagnes；compare champagnes。',
 'two champagnes 在特定点单场景也可能省略杯、份等单位；基础学习先把不同酒款和两杯酒的完整表达分开。',
 ('The menu lists several champagnes by the glass.','菜单列出几款可按杯点的香槟。'),('We compared two champagnes from different producers.','我们比较了两家不同生产者的香槟酒。'),sources=S('champagnes','champagne'))
W('warren','英 /ˈwɒrən/；美 /ˈwɔrən/','兔穴群、兔子栖地；迷宫般的通道、房间',
 '一个洞连另一个洞，兔子在里面穿来穿去，是 a warren。把这幅密集相连的画面搬到老楼，a warren of rooms 就是迷宫般的一堆房间。',
 '经法语 warenne 猎物保护区、饲养地，较远有围起来的地区、保护等不同分析；后来特别联系兔子的栖地、洞穴，再用于密集生活空间。',WARREN,
 'a rabbit warren 是兔穴群、兔子栖地；a warren of rooms 是迷宫般的房间；a warren of narrow streets 是曲折密集的街道网络。',
 'a rabbit warren；a warren of rooms；a warren of narrow streets。',
 'burrow 通常是一条或一处动物洞穴；warren 常把相连的洞穴系统、栖地作为整体。比喻时也突出复杂相连。',
 ('The rabbits disappeared into a warren near the hedge.','兔子钻进了树篱旁的一片洞穴里。'),('The old office was a warren of tiny rooms.','旧办公室是一片迷宫般的小房间。'),sources=S('warren','warren'))
W('warrens','英 /ˈwɒrənz/；美 /ˈwɔrənz/','兔穴群、兔子栖地〔复数〕；迷宫般的通道网络〔复数〕',
 '几处互相独立的兔穴系统，或几片复杂密集的旧街区，可以说 warrens。每一个 warren 内部还可能有许多洞、房间或通道。',
 'warren + -s → warrens，/n/ 后后缀读 /z/；普通名词复数，数多个洞穴系统、空间网络。',WARREN+[['warren + -s → warrens','多处兔穴系统或迷宫般空间']],
 'rabbit warrens 是几处兔子栖地、穴群；warrens of streets 是一片片迷宫般的街道；理解复数时保留整体空间单位。',
 'rabbit warrens；warrens of narrow streets；underground warrens。',
 'warrens 可以是地上房间、街道的比喻，不要求必须有真正的兔子或地下洞穴。',
 ('Several rabbit warrens lay along the bank.','岸边分布着几处兔穴群。'),('The old districts are warrens of narrow streets.','那些老城区里都是迷宫般狭窄曲折的街道。'),sources=S('warrens','warren'))
W('heck','英、美 /hek/','哎呀；究竟、到底〔较温和的口语强调〕',
 'What the heck happened? 像中文“到底发生什么了？”heck 保留一点惊讶、烦躁或强调，但比原来的 hell 语气轻。',
 'hell 的委婉变形 → heck，换了词尾声音而保留口语表达功能；不是每次都在指地狱这个地方。',
 [['hell 的感叹、强调用法 → 委婉变形 heck','减轻原表达的粗烈程度'],['what the heck、a heck of、heck of a 等组合','惊讶、困惑、强调等现代口语用法']],
 'what the heck 是究竟、到底；a heck of a job 是非常费劲或很棒的一项工作，具体褒贬看语境；heck, why not 可是哎，何不呢。',
 'what the heck；a heck of a job；a heck of a lot。',
 'heck 比 hell 温和，但仍偏随意口语。a heck of a lot 强调很多，不适合把 heck 每次都单独译成地狱。',
 ('What the heck is going on here?','这里到底是怎么回事？'),('You have done a heck of a good job.','你干得真是太棒了。'),sources=S('heck','heck'))
W('babe','英、美 /beɪb/','婴儿〔较文学或固定说法〕；宝贝、亲爱的；天真无经验的人；吸引人的人〔口语〕',
 'babe 能是怀里的小婴儿，也能是亲近的人之间一句“宝贝”。容易以为它只是 baby 删字母；历史上 babe 其实更早，baby 反而带了小称尾。',
 '较早 baban 等幼儿称呼缩成 babe，可能拟幼儿语言里的 ba 等音。babe + 小称 -y → baby；babe 自己继续扩展到亲昵称呼、无经验者、吸引人的人等。',BABE,
 'a babe in arms 是尚需抱着的婴儿；babe in the woods 比喻涉世未深；Babe 作称呼常是亲密关系里“宝贝、亲爱的”。',
 'a babe in arms；a babe in the woods；hey, babe。',
 '现代普通婴儿常用 baby，babe 的婴儿义偏文学、固定搭配；把人叫 a babe 也可侧重外貌吸引力，语气可能轻佻，要连关系与语境理解。',
 ('She held a sleeping babe in her arms.','她怀里抱着一个熟睡的婴儿。'),('“Babe, have you seen my keys?” he asked.','“亲爱的，你看到我的钥匙了吗？”他问。'),sources=S('babe','babe'))
W('babes','英、美 /beɪbz/','婴儿们；天真无经验的人们；吸引人的人们〔复数〕',
 '几位涉世未深的新手，可以被比作 babes in the woods；字面文学描写里也能指多个婴儿。复数本身不决定是哪一义。',
 'babe + -s → babes，基础词保留 e，再接 s，/b/ 后后缀读 /z/。不是 baby 的复数，baby 另写 babies。',BABE+[['babe + -s → babes','babe 的复数；baby 的复数是 babies']],
 'babes in arms 是襁褓中的婴儿；babes in the woods 是缺少经验、身处复杂环境的人；口语另有外貌吸引力的人员用法。',
 'babes in arms；babes in the woods；sleeping babes。',
 'babes 与 babies 语体、基础词不同。前者固定搭配、亲昵称呼或外貌口语较突出，后者是现代普通婴儿名称的复数。',
 ('The painting shows mothers holding babes in arms.','画中是母亲们抱着襁褓婴儿的场景。'),('We were babes in the woods when we first entered the industry.','刚进入这个行业时，我们都是不谙世事的新手。'),sources=S('babes','babe'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zir',ROOTS,WORDS)
 extend_lessons()
