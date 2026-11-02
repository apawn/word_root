"""Listen, share, store and relation: linked forms with distinct uses."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
LI=[['古英语 hlysnan 等 → 中古英语 listenen、listnen','留神听、听取'],['英语 listen','主动把注意力放在声音或他人表达上']]
W('listen','/ˈlɪsən/','听；留心听；听取意见',
 '声音不只是进了耳朵，你还把注意力放过去，想弄明白对方在说什么。',
 '接古英语 hlysnan 等听的词族，经中古英语形式演变。现代 t 不发音；不能按 list 清单 + en 拆成制作列表。',LI,
 'listen to music 听音乐，listen to advice 听取建议；Listen! 单独提醒人留神。listen for a sound 等待、留意某种声音。',
 'listen to；listen for；listen carefully；listen up。',
 'listen 常强调主动注意，hear 听见；后接对象通常 listen to the teacher，不说 listen the teacher。',
 ('Please listen to the instructions carefully.','请仔细听说明。'),('She listened for footsteps outside the door.','她留意着门外是否有脚步声。'))
W('listener','英 /ˈlɪsənə/；美 /ˈlɪsənər/','听者；听众；善于倾听的人',
 '把注意力给说话、音乐或节目的人；说 good listener，还在夸他肯听懂别人的感受。',
 'listen + -er，形成听者人物词；t 同样不发音。不是仅有耳朵就自动被叫 a good listener。',LI+[['listen + -er → listener','留神听 → 听者、听众']],
 'radio listeners 广播听众，a good listener 善于倾听的人；listeners to a podcast 播客听众。',
 'a good listener；radio listeners；regular listeners。',
 'listener 听的人，speaker 说话、演讲者；audience 可以是看、听演出的整群观众，范围依场景。',
 ('The programme invites questions from listeners.','节目欢迎听众提问。'),('She is a patient and thoughtful listener.','她是个耐心、体贴的倾听者。'))
W('listening','/ˈlɪsnɪŋ/，亦 /ˈlɪsənɪŋ/','倾听；听力理解；正在听的',
 '听这个活动可以训练，也可以是愿意给别人一点注意力；语言课上又常专说听力。',
 'listen + -ing，与较早分词、动作名词形式对应；中间不另加 t 的发音。',LI+[['listen + -ing → listening','听的活动、形式 → 语言听力等用法']],
 'listening skills 听力、倾听技能，a listening test 听力测试；a listening ear 愿意倾听、支持别人的态度。',
 'listening skills；listening comprehension；a listening test；a listening ear。',
 'listening 主动听、听力理解，hearing 也可说听觉能力、听证会等；听力考试常用 listening test，不能机械全换 hearing。',
 ('The course includes reading and listening practice.','课程包含阅读和听力练习。'),('Sometimes people simply need a listening ear.','有时人们只是需要有人愿意倾听。'))
W('listenable','/ˈlɪsənəbəl/','悦耳、听得下去的；可收听的',
 '不只声音大到听得见，还常评价这音乐或节目听起来舒服、能吸引人继续听。',
 'listen + -able 可……的，形成可听、适合听的评价形容词；实际常比字面可被听到多一层可听性评价。',LI+[['listen + -able → listenable','可听 → 适合收听、听得舒服的']],
 'a listenable album 听起来不错的专辑，highly listenable radio 颇有可听性的广播内容；不一定夸成杰作。',
 'a listenable album；highly listenable；an easily listenable recording。',
 'listenable 常说听感、可听性，audible 说能否听见；声音 audible 仍可能吵得完全不 listenable。',
 ('The songs are simple but very listenable.','这些歌简单，却很好听。'),('The clean recording makes the old interview more listenable.','清晰的录音让这段旧采访更容易听下去。'))
R('B2741','留神听、听众、倾听与可听性','LISTEN：把注意力给声音，而非只听见','listen 动作，listener 听的人，listening 活动和听力，listenable 再说内容听起来怎么样。',
 'listen 来自古英语听的词族，与 list 清单分开。t 不发音，衍生词也延续；listen to 是最常见接对象结构。',
 'listen → listener、listening、listenable。',
 [['动作、人物、活动及性质','listen · listener · listening · listenable']],
 'listen to，不是 listen someone；hear 听见、listen 留心听；listenable 不只 audible 听得见。',
 'The regular listener found the new programme easy to listen to.\n\n这位固定听众觉得新节目听起来很轻松。',
 'listen listener listening listenable')
SH=[['古英语 sċearu → 中古英语 schare → share','切分、分出的部分，与 shear 等词族相关'],['英语 share','一份、股份；分享、共同使用、共同承担']]
W('share','英 /ʃeə/；美 /ʃer/','一份；股份；分享、共用、分担',
 '一整块分出你的一份；也可以把手里的东西拿来一起用，把责任拿来一起担。',
 '名词接古英语 sċearu 切分、部分，与剪切词族相关；现代动作有分给、共同拥有使用等，不等于每次都真的切成几块。',SH,
 'share a room 合住一间房，share an idea 分享想法，share the cost 分担费用；a share of the cake 蛋糕一份，company shares 公司股份。',
 'share with；share the cost；a share of；have something in common。',
 'share 信息不一定让原持有者失去它；share a burden 分担负担，也不是所有 share 都是金融股票。',
 ('Can I share the table with you?','我可以和你共用这张桌子吗？'),('Everyone should do their share of the work.','每个人都应完成自己那一份工作。'))
W('shareable','英 /ˈʃeərəbəl/；美 /ˈʃerəbəl/','可分享的；适合传播、共用的',
 '能交给别人一起看、一起用；内容平台里还常夸它容易让人想转发。',
 'share + -able，通常保留 e，形成可分享性质词；另有 sharable 拼写。不是一旦可分享，就代表拥有转发任何内容的许可。',SH+[['share + -able → shareable','分享 → 可分享、适于传播的']],
 'shareable content 适合分享传播的内容，a shareable link 可分享链接；shareable portions 可供多人分享的份量。',
 'shareable content；a shareable link；a shareable document。',
 'shareable 能、适合分享，shared 已分享、共同使用；a shared folder 共享文件夹不是在赞它很有传播力。',
 ('The app creates a shareable link to the album.','应用会生成一个可分享的相册链接。'),('The café serves small, shareable dishes.','咖啡馆供应适合大家分着吃的小份菜。'))
W('shareholder','英 /ˈʃeəhəʊldə/；美 /ˈʃerhoʊldər/','股东',
 '把公司股权看成分出的份额，持有这些份额的人或机构就是股东。',
 'share 股份 + holder 持有者，后半来自 hold + -er。不是只要常分享东西，就算公司股东。',C('share 股份','holder 持有者','shareholder','持有公司股份的人或机构'),
 'a major shareholder 大股东，a shareholders’ meeting 股东大会；shareholders 可以是个人，也可以是其他机构。',
 'a major shareholder；a minority shareholder；a shareholders’ meeting。',
 'shareholder 股东，stakeholder 利益相关方范围更广，员工、客户等也可能是 stakeholder，但未必持有股份。',
 ('The company sent the report to its shareholders.','公司把报告发给了股东。'),('A major shareholder asked questions at the meeting.','一位大股东在会上提出了问题。'))
W('shareholding','英 /ˈʃeəhəʊldɪŋ/；美 /ˈʃerhoʊldɪŋ/','持股；所持股份、股权份额',
 '不说谁这个人，而说他在公司里拿着多少股、怎样一块权益。',
 'share 股份 + holding 持有、所持份额，形成持股活动和股权份额名词。',C('share 股份','holding 持有、所持份额','shareholding','持股或持有的股权份额'),
 'a minority shareholding 少数股权，a shareholding in a company 在某公司的持股；可以按数量、比例描述。',
 'a minority shareholding；a controlling shareholding；a shareholding in。',
 'shareholder 是持有人，shareholding 是所持股权；a person has a shareholding，而不是这个人本身就是一块 shareholding。',
 ('She has a small shareholding in the company.','她在这家公司持有少量股份。'),('The report lists the group’s shareholdings.','报告列出了该集团的持股情况。'))
W('shareware','英 /ˈʃeəweə/；美 /ˈʃerwer/','共享试用软件；通常试用后付费的软件',
 '可以先分发、试用，让人试过再决定是否继续使用、购买；共享不等于永远免费。',
 'share 分享 + -ware 软件类构词部分，形成特定软件分发模式名称。不是把程序的所有权平均分给每位用户。',SH+[['share + -ware → shareware','可分发、试用的软件模式']],
 'a shareware program 共享试用软件，download shareware 下载试用软件；试用期限、限制、付费条件依具体许可。',
 'shareware software；a shareware program；shareware distribution。',
 'shareware 不等于 freeware 免费软件，也不等于 free/open-source software 自由、开源软件；免费试用与源码、修改权是不同维度。',
 ('The archive includes several old shareware programs.','档案里收录了几款旧共享试用软件。'),('The shareware version lets users try the basic features.','共享试用版允许用户先体验基本功能。'))
W('rideshare','英 /ˈraɪdʃeə/；美 /ˈraɪdʃer/','合乘；拼车；网约出行服务〔依语境〕',
 '原来把一段车程与别人共用，现代某些地区也用这个词说平台匹配司机、乘客的服务。',
 'ride 乘车行程 + share 分享、共用。传统合乘画面与现代平台服务名称有联系，但一单 rideshare 不保证车里一定同时拼着多个陌生乘客。',C('ride 乘车行程','share 分享、共用','rideshare','合乘、拼车 → 某些语境的网约出行服务'),
 'a rideshare service 合乘或网约出行服务，arrange a rideshare 安排合乘；具体是否拼车，看服务选项、地区习惯。',
 'a rideshare service；a rideshare app；arrange a rideshare。',
 'rideshare 名称不保证每程都多人拼车；carpool 更直接强调多人共同乘车，常为通勤。',
 ('They arranged a rideshare to the festival.','他们安排了合乘去参加节庆。'),('The airport has a pickup area for rideshare services.','机场设有网约出行服务上车区。'))
R('B3341','一份、股份；分享、共用与分担','SHARE：分出一份，也可把东西放在一起共用','分蛋糕是一份，分担费用是责任共担，股份是公司权益份额；数字分享又不必让原物消失。',
 'share 接古英语分切、份额词族。先看基础和可分享性，再把股东、持股成组；shareware、rideshare 是固定分发、出行模式名称。',
 'share → shareable；shareholder 人物 → shareholding 份额；shareware 软件模式，rideshare 车程服务。',
 [['份额、分享及可分享性','share · shareable'],['股东和持股','shareholder · shareholding'],['软件与车程模式','shareware · rideshare']],
 'shareholder 不等于所有 stakeholder；shareware 不一定免费；rideshare 不保证多人拼同一辆车。',
 'The shareholders shared the cost of creating a shareable report.\n\n股东们分担了制作可分享报告的费用。',
 'share shareable shareholder shareholding shareware rideshare')
ST=[['拉丁 instaurāre → 法语 estorer、estor 等 → 英语 store','建立、配备 → 储备物资、供应'],['现代 store','存放、储存；储备；售卖商品的商店']]
W('store','英 /stɔː/；美 /stɔːr/','商店；储备；储存、存放',
 '先把东西放好留待使用；存着供应的货物又联系卖货的店。今天动词存和名词店都很常见。',
 '经法语旧形式接拉丁 instaurāre 建立、配备词族，先有供应、储备等历史。restore 有相关拉丁重建词族背景，但不是现代 re- 再 + store 把文件再存一次。',ST,
 'store food 储存食物，store data 保存数据；a grocery store 食品杂货店，stores 复数也可说物资储备；what’s in store for us 等着我们的会是什么。',
 'store data；a department store；in store for；a store of knowledge。',
 'store 商店在美式很常见，英式也用但日常小店常说 shop；store information 存信息，restore information 从备份等恢复信息。',
 ('We store the tools in a locked cupboard.','我们把工具存放在上锁柜子里。'),('Nobody knew what the future had in store for them.','没人知道未来有什么在等着他们。'),sources=['https://en.wiktionary.org/wiki/store#English','https://www.etymonline.com/word/store'])
W('storage','英 /ˈstɔːrɪdʒ/；美 /ˈstɔːrɪdʒ/','储存；存储空间、容量',
 '把东西存下来的过程，或能让这些东西待着的空间；衣物、粮食、数据都能谈 storage。',
 'store 去 e + -age，形成储存、仓储及空间名词。不是 store 商店的年龄。',ST+[['store + -age → storage','储存 → 存放过程、空间、容量']],
 'storage space 储物空间，data storage 数据存储，in storage 存放保管中；a storage unit 可说租用储物单元或某类存储单元。',
 'storage space；data storage；put in storage；storage capacity。',
 'storage 存储通常不可数；a store 是商店或一份储备。computer storage 长期保存数据的功能，与工作内存 memory 的用途不同，日常产品用词仍要看规格。',
 ('The flat has very little storage space.','这套公寓储物空间很少。'),('The files are kept in secure storage.','文件被妥善存放保管。'))
W('storekeeper','英 /ˈstɔːkiːpə/；美 /ˈstɔːrkiːpər/','店主、店铺管理员；库管员',
 '负责照看这家店、这批物资的人；先看 store 在场景里是商店还是储备。',
 'store 商店、物资储备 + keeper 看管者。keep 在这里是管理、保管，不是把整家商店藏到口袋里。',C('store 商店、物资储备','keeper 看管者','storekeeper','店铺或库存物资的管理者'),
 'a village storekeeper 村店经营者，a warehouse storekeeper 仓库保管员；具体工作不一定同时拥有店铺所有权。',
 'a village storekeeper；a warehouse storekeeper；the storekeeper’s records。',
 'storekeeper 管理商店、库存，shopkeeper 更直接指经营商店者；两者有交叠，但仓库岗位不能一律翻店老板。',
 ('The storekeeper ordered more rice before the holiday.','店铺经营者在节日前多订了一些米。'),('The storekeeper checked the inventory records.','库管员核查了库存记录。'))
W('drugstore','英 /ˈdrʌɡstɔː/；美 /ˈdrʌɡstɔːr/','药店；兼售日用品的药妆、药品商店〔尤美〕',
 '核心与卖药有关，但美国街头这种店也常卖日用品、洗护等，不只一个配药窗口。',
 'drug 药品 + store 商店，形成商业场所名。drug 既可药品也可毒品，不能看到前半就把普通药店当成非法场所。',C('drug 药品','store 商店','drugstore','销售药品并常兼售日用品的店'),
 'the local drugstore 当地药店；buy shampoo at a drugstore 在药店买洗发水。是否有处方药、具体服务，看实际店铺。',
 'a local drugstore；a corner drugstore；drugstore products。',
 'drugstore 常说整家药品兼日用品商店，pharmacy 更强调药房、配药业务；范围在不同地区、机构里有交叠。',
 ('She bought toothpaste at the drugstore.','她在药店买了牙膏。'),('There is a drugstore near the station.','车站附近有一家药店。'))
R('B3861','储存、储备、商店；空间与看管者','STORE：留着供使用，再看储备与商店','store food 是存食物，a food store 是食品店；storage 说储存过程、空间，storekeeper 看管物资或店铺。',
 'store 经法语接拉丁配备、建立词族。restore 的旧拉丁重建背景另看历史，不能只按英语重新存入解释恢复。',
 'store → storage、storekeeper；drugstore、bookstore、webstore 按所售物和媒介；storehouse、storeroom 看存放建筑、房间。',
 [['储存、空间及管理','store · storage · storekeeper'],['不同商店及店面','drugstore · bookstore · superstore · webstore · storefront'],['仓储地点','storehouse · storeroom'],['历史相关、现代非直接拆分','restore']],
 'store 存，restore 恢复；storage 不通常说一间商店；drugstore 不把 drug 只认成毒品。',
 'The storekeeper stored the boxes in the storeroom to save space in the store.\n\n店铺管理员把箱子放进储物间，腾出店内空间。',
 'store storage storekeeper drugstore bookstore superstore webstore storefront storehouse storeroom restore')
RE=[['拉丁 referre → relātus、relātiō → 法语 relacion → 英语 relation','带回、报告、联系相关对象等历史词族'],['现代 relation 词族','事物联系；亲属、关系及其性质']]
W('relation','/rɪˈleɪʃən/','关系；联系；亲属；叙述〔较正式〕',
 '两件事怎样对得上、怎样相互影响，是一种 relation；说 a relation，又可能是一位亲戚。',
 '经法语接拉丁 relātiō，来自 referre 的 relātus 词干。现代可认 relate 与 -ion 的对应，但历史 lat- 与 fer- 是不规则词干关系，不按字母随意替换。',RE,
 'the relation between A and B A 与 B 的关系，in relation to 关于、相对于；a distant relation 远亲。international relations 国际关系常用复数。',
 'the relation between；in relation to；a distant relation；international relations。',
 'relation 可具体指一位亲属，relationship 常说联系、相处关系；a distant relation 远亲，不是一个很远的恋爱关系。',
 ('The report examines the relation between sleep and memory.','报告考察睡眠与记忆的关系。'),('He is a distant relation of mine.','他是我的一位远亲。'))
W('relationship','/rɪˈleɪʃənʃɪp/','关系；相处关系；恋爱关系；联系',
 '不只是两点之间的一根线，还可以说人们怎样长期相处、维持联系。',
 'relation + -ship，形成关系、相处状态名词。ship 是抽象状态、关系后缀，不是关系之船这一真实词源。',RE+[['relation + -ship → relationship','联系、关系 → 具体相处关系、关联状态']],
 'a relationship with someone 与某人的关系，a close relationship 密切关系；be in a relationship 在恋爱中，但 relationship 不都指情侣关系。',
 'a relationship with；a close relationship；build a relationship；the relationship between。',
 'relationship 可人际，也可事物联系；a relation 可是亲戚本人，a relationship 通常不是一位亲戚。',
 ('She has a good relationship with her neighbours.','她和邻居关系很好。'),('The study looks at the relationship between exercise and sleep.','研究考察运动与睡眠之间的联系。'))
W('relational','/rɪˈleɪʃənəl/','关系的；与关系有关的；关系模型的',
 '把重点放在事物、人之间怎样联系；数据库里则是一个专门模型名，不只是泛泛说数据彼此有关系。',
 'relation + -al 相关形容词。relational database 的 relation 取数学关系的专门含义，常以表来表示，不是把数据库当人际关系网。',RE+[['relation + -al → relational','关系 → 关系方面的；专门关系模型的']],
 'relational skills 人际关系技能，a relational database 关系数据库；两个场景同词但专业程度不同。',
 'relational skills；relational data；a relational database。',
 'relational database 不是所有互相连接的数据都自动属于它；relationship 仍是名词，不能写 a relationship database 来替代正式术语。',
 ('The workshop focuses on relational skills in team leadership.','工作坊重点训练团队领导中的人际关系技能。'),('The application stores customer records in a relational database.','应用把客户记录存入关系数据库。'),sources=['https://en.wiktionary.org/wiki/relational#English','https://www.ibm.com/think/topics/relational-databases'])
R('B3911','事物联系、亲属；相处关系及相关性质','RELATION：怎样联系，或因什么关系连在一起','relation 可说联系，也可指亲戚本人；relationship 常说相处、关联状态；relational 是关系方面的形容词。',
 'relation 经法语接拉丁 relātiō，与 referre、relātus 历史相关。现代分清名词与形容词，比把所有中文关系都同词替换更有用。',
 'relation → relationship、relational；-ship 说关系状态，-al 说相关性质。',
 [['关系、相处和性质','relation · relationship · relational']],
 'a relation 可以是一位亲戚；relationship 不只恋爱；relational database 有专门数学关系模型背景。',
 'The article explains the relationship between social experience and relational skills.\n\n文章解释了社会经历与人际关系技能之间的联系。',
 'relation relationship relational')
for item in WORDS:
    if item['word']=='shareware':item['sources'].append('https://www.gnu.org/philosophy/categories.html#shareware')
    if item['word']=='rideshare':item['sources'].append('https://www.oxfordlearnersdictionaries.com/definition/english/ride-share_2')
if __name__=='__main__':save('continuation_20261029_dj',ROOTS,WORDS)
