"""Common states: agreement, completion, requirement, permission, absence and existence."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0503':dict(words=['agree','agreed'],label='agreed：双方已接受同一安排',note='agree 经法语 a gré 等接拉丁令人满意、乐意的词族；agreed 是过去、分词及表示一致接受的修饰语。'),
 'C0425':dict(words=['finish','finished'],label='finished：走到终点与做完的状态',note='finish 接拉丁 finis 边界、终点词族；finished 分别可说完成的产品、结束工作及处境完了。'),
 'C1189':dict(words=['require','required'],label='required：被规定需要的',note='require 经法语接拉丁 requirere 寻求、要求；required 用于过去、被动与必需性质，不能把语法被动都当过去时间。'),
 'B3592':dict(words=['allow','allowed'],label='allowed：获准与被留出的限度',note='allow 历史合流了法语认可、赞许及分配相关词；allowed 可说获准做某事，或安排中留出的量。'),
 'B4236':dict(words=['miss','missing'],label='missing：该在却不在',note='miss 承接古英语 missan 未达到、错过；missing 常表示人或物不在预期位置，与 missed 被错过、被想念作对比。'),
 'B3283':dict(words=['own','owned'],label='owned：属于某人、由某人拥有',note='own 的拥有动词接自己的这一性质词，owned 为过去、分词；口语击败义另由掌控、占优势发展。'),
 'B3965':dict(words=['exist','existing'],label='existing：现在已经有的',note='exist 经法语接拉丁 exsistere 出现、存在；existing 作形容词说已经存在的客户、规则、设施等。'),
}
W('agreed','/əˈɡriːd/','商定的、一致接受的；同意了；agree 的过去式、过去分词',
 '你说可以，我也接受，事情就有了共同确定的版本。the agreed price 是谈妥的价钱。',
 'agree + -d，结尾读 /d/。agree 经法语 agreer、a gré 乐意地、满意地，上接拉丁 gratum 令人满意的等材料；双方认可发展为达成一致。',
 [['法语 agreer、a gré → agree','接受、感到满意 → 意见相合'],['agree 去 e + -ed → agreed','过去表示同意；已经一致接受的']],
 'the agreed time 商定的时间；an agreed plan 一致接受的方案；as agreed 按照约定；Agreed! 同意、就这么办。',
 'an agreed price；We are agreed on this point。','I agreed 是我过去表示了同意；We are agreed 是我们目前意见一致。不要写成 I am agree；agree 本身是动词。',
 ('We met at the agreed time.','我们在约定的时间见了面。'),('“Let’s start with the easy part.” “Agreed.”','“先从容易的部分开始吧。”“同意。”'))
W('finished','/ˈfɪnɪʃt/','完成的、做完了的；结束了、完了；finish 的过去式、过去分词',
 '一路做到终点，剩下的工作已经没有了。a finished product 是做好了的成品；I’m finished 具体是做完还是完蛋，要听上下文。',
 'finish + -ed，/ʃ/ 后结尾读 /t/。finish 经法语 finir 等接拉丁 finire 划定边界、结束，上接 finis 边界、终点；完成与结束的范围不断扩大。',
 [['拉丁 finis → finire → finish','边界、终点 → 使结束、完成'],['finish + -ed → finished','做完的；已结束的状态']],
 'a finished product 成品；be finished with something 用完、处理完某物；Are you finished? 你做完了吗；finished goods 制成品。',
 'the finished article；finished with the scissors。','I’m finished with the report 通常说报告处理完了。If they find out, I’m finished 则是事情败露我就完了，语气依情境判断。',
 ('The finished product looks very different from the first sketch.','成品与最初的草图看起来很不一样。'),('Are you finished with the scissors?','剪刀你用完了吗？'))
W('required','/rɪˈkwaɪəd/；美亦 /rɪˈkwaɪrd/','必需的、按规定要有的；被要求；require 的过去式、过去分词',
 '有些材料可交可不交，有些少了就达不到要求。required 把后者标出来：这一项需要有。',
 'require + -d，结尾 /d/。require 经古法语接拉丁 requirere 寻求、询问、要求，含 re- 与 quaerere 寻找的材料；现代分词常作要求、必需的形容词。',
 [['拉丁 requirere → 法语 → require','寻找、要求得到'],['require 去 e + -ed → required','被要求；满足条件所必需的']],
 'required reading 必读材料；a required field 必填项；required skills 必需技能；be required to do 被要求做；if required 如有需要。',
 'the required documents；the minimum age required。','required 表明确要求，recommended 通常只是建议。You are required to sign 是当前规定你要签字，不因出现 -ed 就变成过去的要求。',
 ('Please complete all required fields.','请填写所有必填项。'),('Students are required to bring their own notebooks.','学生须自带笔记本。'))
W('allowed','/əˈlaʊd/','被允许的、获准的；留出的；allow 的过去式、过去分词',
 '本来有一道规则的门，现在规则说你可以过去：be allowed to do，就是获准做。',
 'allow + -ed，结尾读 /d/。allow 经中古英语、法语，历史合流认可、赞许及分配的不同来源；现代常见许可与留出资源两条用法。',
 [['法语认可与分配相关动词 → allow','认可、允许；分配、留出'],['allow + -ed → allowed','曾允许；获准；被留出的']],
 'be allowed to enter 获准进入；Pets are not allowed 不许带宠物；the time allowed 留出的时间；allowed expenses 认可的费用，具体看制度语境。',
 'allowed to leave；within the time allowed。','allowed 与 aloud 读音相同。allowed 说许可，aloud 说出声：read aloud 大声读。许可结构用 be allowed to do，不用 be allowed doing 表同一关系。',
 ('Visitors are allowed to take photographs here.','参观者可以在这里拍照。'),('We completed the task within the time allowed.','我们在规定时间内完成了任务。'))
W('missing','/ˈmɪsɪŋ/','不见的、缺失的；想念、错过着〔miss 的 -ing 形式〕',
 '桌上本应有三把钥匙，现在只看见两把，另一把就是 missing。关键是该有的位置空了，不一定已经知道它去了哪里。',
 'miss + -ing；miss 接古英语 missan 未中、未达到、错过的词。分词形容词发展为不在预期位置、找不到或缺少；作动词时也接想念义。',
 [['古英语 missan → miss','没有达到、错过；后来也有想念'],['miss + -ing → missing','应在而不在；正在想念或错过等']],
 'a missing page 缺失的一页；go missing 不见、失踪；something is missing 缺了点东西；I’m missing you 我正在想你。',
 'missing information；a missing piece。','a missing child 是失踪的孩子；a missed call 是未接来电。I’m missing you 表我想你；You are missing 表你不见了，主语与结构改变了意思。',
 ('One page is missing from this book.','这本书缺了一页。'),('I found the missing key under the sofa.','我在沙发底下找到了不见的钥匙。'),('I’m missing our evening walks.','我很想念我们傍晚一起散步的时光。'))
W('owned','英 /əʊnd/；美 /oʊnd/','拥有了；由……拥有的；own 的过去式、过去分词',
 '东西确实属于某一方，owned 把这个归属关系说出来。a locally owned shop 就是本地人拥有的店。',
 'own + -ed，结尾读 /d/。own 的性质词接古英语 agen 自己的，与拥有、取得的古老动词词族相连；英语 own 再发展出拥有、承认的动词用法。',
 [['古英语 agen → own','自己的；与古老拥有词族相连'],['动词 own + -ed → owned','拥有过；由某人拥有；口语也说压倒性击败']],
 'privately owned 私人拥有的；family owned 家族拥有的；owned by someone 归某人所有；I owned a bicycle 我过去有一辆自行车。',
 'a locally owned café；wholly owned。','owned 表归属，不保证所有者亲自管理。be owned by 和 be managed by 分别回答归谁、由谁管理；游戏口语 got owned 另说被彻底击败。',
 ('The café is owned by two sisters.','这家咖啡馆归两姐妹所有。'),('He owned the bicycle for nearly ten years.','那辆自行车他拥有了将近十年。'))
W('existing','/ɪɡˈzɪstɪŋ/','现有的、已经存在的；exist 的 -ing 形式',
 '还没增加新东西，眼下手里本来就有的那一部分，是 existing。existing customers 就是已有客户。',
 'exist + -ing；exist 经法语 exister 接拉丁 exsistere 出现、存在，含 ex- 向外与 sistere 站定、使站住等材料。现代 existing 常作形容词。',
 [['拉丁 exsistere → 法语 exister → exist','出现、存在'],['exist + -ing → existing','已经存在的；现有的']],
 'existing customers 老客户、现有客户；existing buildings 现有建筑；existing rules 现行规则；existing equipment 已有设备。',
 'make use of existing resources；the existing system。','existing 常把已经有的与准备新加的对照；existent 更偏存在与否的性质描述，日常说已有客户通常选 existing customers。',
 ('We can use the existing equipment for the experiment.','我们可以用现有设备做实验。'),('The new service is also available to existing customers.','现有客户也可以使用这项新服务。'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ut',ROOTS,WORDS)
 extend_lessons()
