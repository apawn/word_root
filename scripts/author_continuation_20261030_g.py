"""Card and sign: cards, card metaphors and close signing extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['希腊 chartes 纸、纸草 → 拉丁 charta → 法语 carte','书写材料、纸片'],['中古英语 carde → card','纸牌、卡片 → 证件、节目单与电子卡等']]
def H(f,m):return C+[[f,m]]
W('card','英 /kɑːd/；美 /kɑːrd/','卡片；纸牌；银行卡、证件卡；节目单',
 '先是一小片承载信息的卡，后来材料可以是塑料、电子数据；具体是哪种卡由场景决定。',
 '经法语 carte 上接拉丁 charta、希腊纸张词，与 chart 同族异形。梳理纤维的 card 动词另有历史，不把梳棉说成拿银行卡刷棉花。',C,
 'a birthday card 生日卡，a bank card 银行卡，play cards 打牌，pay by card 刷卡付款；the fight card 是拳赛等的比赛名单。',
 'a birthday card；pay by card；play cards；an identity card。',
 'card 银行卡不必都是 credit card 信用卡；debit card 借记卡也属于 bank card。',
 ('She sent me a birthday card.','她给我寄了一张生日卡。'),('Can I pay by card?','我能刷卡付款吗？'))
W('carded','英 /ˈkɑːdɪd/；美 /ˈkɑːrdɪd/','被查证件的；被出示处罚牌的；另有梳理纤维义',
 '美式买酒等场景是被要求出示年龄证件；比赛里可能是裁判给了黄牌、红牌。',
 'card + -ed，接查证件、出牌处罚的动词义。纺织中 carded wool 梳理过的羊毛走另一梳纤维词源，不混入纸卡故事。',H('card + -ed → carded','核对证件、出牌处罚的过去形式'),
 'get carded 被查年龄证件，be carded for a foul 因犯规吃牌；具体处罚还看是哪项运动。',
 'get carded；be carded for；carded at the entrance。',
 'carded 不总是被刷卡付款；The player was carded 多半说吃牌，The customer was carded 可能说查证件。',
 ('He still gets carded when buying wine.','他买葡萄酒时仍会被要求出示年龄证件。'),('The player was carded for a late tackle.','球员因铲球过迟被出牌处罚。'))
W('cardholder','英 /ˈkɑːdhəʊldə/；美 /ˈkɑːrdhoʊldər/','持卡人；卡套、卡夹',
 '可以是谁拥有这张卡，也可以是哪件东西装着它；holder 既指人，也指收纳物。',
 'card + holder，后部 hold + -er。两种名词义分别取持有人和承装器具。',H('card + holder → cardholder','持有卡的人；装卡的物件'),
 'the cardholder’s name 持卡人姓名，a leather cardholder 皮卡包；先看是否在表单、商品描述里。',
 'the cardholder’s name；a leather cardholder；cardholder information。',
 'cardholder 不一定是信用卡持卡人，也可能其他卡；a cardholder 商品则不表示在卖一个人。',
 ('Please enter the cardholder’s name exactly as shown.','请按卡面原样填写持卡人姓名。'),('She keeps her travel cards in a small cardholder.','她把交通卡放在小卡夹里。'))
W('flashcard','英 /ˈflæʃkɑːd/；美 /ˈflæʃkɑːrd/','学习卡；抽认卡',
 '一面提示问题，另一面给答案，短时间拿出来认、回想；纸质和手机里的都可以叫它。',
 'flash 快速出示、闪现 + card，按快速展示提示的学习用途组合，不是存照片的 flash memory card。',H('flash + card → flashcard','快速出示的学习卡 → 抽认卡'),
 'vocabulary flashcards 单词卡，make flashcards 制作抽认卡，review flashcards 复习卡片。',
 'vocabulary flashcards；make flashcards；review flashcards。',
 'flashcard 学习工具，memory card 存储卡；两者都可能电子化，但用途完全不同。',
 ('She made flashcards for the new vocabulary.','她为新单词制作了学习卡。'),('Each flashcard has a question on one side and an answer on the other.','每张卡一面是问题，另一面是答案。'))
W('scorecard','英 /ˈskɔːkɑːd/；美 /ˈskɔːrkɑːrd/','记分卡；评价记录表',
 '把各项得分写在一张表上，最后看谁表现如何；也能用来评估项目、机构。',
 'score 分数 + card，实体记分卡扩展为系统化表现记录，不一定真是一小片硬卡。',H('score + card → scorecard','记录分数的卡 → 记分、评价表'),
 'a golf scorecard 高尔夫记分卡，a performance scorecard 绩效记录表。',
 'a golf scorecard；a performance scorecard；update the scorecard。',
 'scorecard 记录表，scoreboard 展示比分的板；前者可有细分指标，不只是一个大比分。',
 ('He checked his scorecard after the final hole.','打完最后一洞，他核对记分卡。'),('The report uses a scorecard to compare the projects.','报告用评价记录表比较项目。'))
W('wildcard','英 /ˈwaɪldkɑːd/；美 /ˈwaɪldkɑːrd/','通配符；外卡参赛资格；难预测的因素',
 '牌局里可灵活代表别的牌，计算机里就借来代表一类字符；比赛外卡与难预测的人又是不同用法。',
 'wild 灵活、不固定 + card 牌，最初牌类表达发展出代表不固定对象、特殊准入或不确定因素的用法。也常写 wild card。',H('wild + card → wildcard','不固定牌值 → 通配、特殊资格、不确定因素'),
 'a wildcard character 通配符，a wildcard entry 外卡参赛，a political wildcard 政治中的不确定因素。',
 'a wildcard character；a wildcard entry；a wildcard in the race。',
 'wildcard 体育外卡是特殊入围方式，不是保证赢；通配符匹配规则也随软件不同，不能默认任何符号通吃所有位置。',
 ('The search tool accepts a wildcard at the end of a word.','搜索工具允许在词尾使用通配符。'),('She entered the tournament as a wildcard.','她凭外卡资格参加了锦标赛。'))
W('discard','动词英 /dɪsˈkɑːd/、美 /dɪsˈkɑːrd/；名词常前重音','丢弃；弃牌；弃掉的东西',
 '手里有一张不想留的牌，出掉；再借来讲扔掉不要的物品、做法或想法。',
 'dis- 移除 + card，接弃牌动作扩展为舍弃。现代很多宾语不再是卡片。',H('dis- + card → discard','弃牌 → 丢弃、抛开'),
 'discard old papers 丢旧纸，discard an idea 放弃想法；名词 discards 可说弃物。',
 'discard old papers；discard an idea；discarded materials。',
 'discard 丢弃不等于必然回收 recycle；discard a theory 是不再采用它，不是拿剪刀剪论文。',
 ('Discard the damaged packaging.','丢掉破损包装。'),('The team discarded the first design and started again.','团队弃用了第一个设计，重新开始。'))
W('undercard','英 /ˈʌndəkɑːd/；美 /ˈʌndərkɑːrd/','主赛前的垫场比赛；该部分参赛者',
 '一晚比赛节目里，主角登场前还有一些比赛，合起来叫 undercard。',
 'under- 次要、位于下方 + card 比赛名单、节目单。接卡片的节目安排义，不是桌子底下的牌。',H('under- + card → undercard','主赛下方的节目安排 → 垫场赛'),
 'fight on the undercard 参加垫场赛，an undercard bout 一场垫场比赛；拳击报道尤其常见。',
 'on the undercard；an undercard bout；the main event and undercard。',
 'undercard 垫场赛，underdog 不被看好的竞争者；垫场运动员不自动实力弱到不可能获胜。',
 ('The young boxer fought on the undercard.','年轻拳击手参加了垫场赛。'),('The evening included three undercard bouts before the main event.','当晚主赛前有三场垫场比赛。'))
R('B2932','卡片、证件、记分与比赛名单','CARD：承载信息的小片，延伸出多种功能','从 card、carded、cardholder 读卡与人，再看学习、记分、通配；discard 弃牌，undercard 比赛节目。',
 '纸片词经法语接希腊拉丁书写材料，与 chart 同族；梳纤维的 card 另源不硬混。',
 'card → carded、cardholder；flash/score/wild + card；dis- + card；under- + card；共享 cardboard、postcard。',
 [['基本卡与持有者','card · carded · cardholder'],['学习、记分与通配','flashcard · scorecard · wildcard'],['弃牌、节目与已有纸制品','discard · undercard · cardboard · postcard']],
 'cardholder 可人可物；flashcard 不是存储卡；undercard 垫场不同于 underdog 弱势；carded wool 纺织义另源。',
 'The cardholder used a flashcard to remember the new word.\n\n持卡人用一张学习卡记住了新词。',
 'card carded cardholder flashcard scorecard wildcard discard undercard cardboard postcard')
SI=[['拉丁 signum 标记 → 法语 signe、signer → sign','标志、作记号；签名'],['现代 sign 派生','签字主体与共同签署']]
W('signee','/saɪˈniː/','签约者；被签下的人',
 '在体育、艺人经纪报道中，常说刚被球队、公司签下的那个人。',
 'sign + -ee，现代形成签约关系人物名。-ee 在此常偏被签约的一方，不把所有签字者都一律称 signee。',SI+[['sign + -ee → signee','签约关系中的人物 → 被签下的人']],
 'a new signee 新签约者，a recent signee 最近签下的人；实际角色由合同、报道对象决定。',
 'a new signee；a recent signee；the club’s latest signee。',
 'signer 中性签字者，signee 常见被球队等签下的人；signatory 正式签署方是另一常用称谓。',
 ('The club introduced its latest signee.','俱乐部介绍了最新签下的球员。'),('The label’s new signee released her first single.','唱片公司新签的歌手发布了第一支单曲。'))
W('cosign','英 /ˌkəʊˈsaɪn/；美 /ˌkoʊˈsaɪn/','共同签署；联署；贷款语境作共同签字担保',
 '不是只自己签，而是与别人一同在文件上签字；贷款语境还可能承担相应偿付责任。',
 'co- 共同 + sign 签署，也常写 co-sign。发音以 /saɪn/ 结尾，不是数学 cosine 余弦。',SI+[['co- + sign → cosign','一起签字 → 联署、共同签署']],
 'cosign a letter 联署信件，cosign a loan 在贷款上共同签字；具体责任依文件和制度，不从一个前缀推断。',
 'cosign a letter；cosign an agreement；cosign a loan。',
 'cosign 与 witness 见证签字角色不同；签字见证者不自动成为共同借款、担保责任人。',
 ('Three residents agreed to cosign the letter.','三名居民同意联署这封信。'),('Her parent was asked to cosign the agreement.','她的家长被要求在协议上共同签字。'))
R('B3869','标记、签字与签约人物','SIGN：以记号确认；SIGNEE 与 COSIGN 各看角色','基本 sign、signer 已精讲，新增 signee 被签约人物、cosign 共同签字，相关路标词共享归看。',
 '经法语接拉丁标记词。-ee 不一定能靠被动受事一条规则解释所有英语词，在 signee 中看签约角色。',
 'sign → signer、signee、signage；co- + sign → cosign；sign + post、board。',
 [['基本词与签字、签约角色','sign · signer · signee · cosign'],['已有标识与路标','signage · signpost · signboard']],
 'signee 常指被签下的球员、艺人；cosign 不等于 witness；cosine 余弦是另词。',
 'The new signee signed the agreement at the club.\n\n新签约球员在俱乐部签了协议。',
 'sign signer signee cosign signage signpost signboard')
if __name__=='__main__':save('continuation_20261030_g',ROOTS,WORDS)
