"""Everyday missed bases and suffix families: harassment, void, cottage, massage."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1833':dict(words=['harass','harassment'],label='harass → harassment：反复烦扰这一行为',note='harass 借法语，更早来源有争议；harassment 是英语内加 -ment 的名词。'),
 'A1760':dict(words=['harass','harassment'],label='harass 词族补读 harassment',note='harassment 与已有 harassed、harassing 放在同一词族理解；其名词后缀是 -ment。'),
 'C1597':dict(words=['void','voided'],label='vacant／void：空着、空缺与失去效力',note='void 经法语 voide 等接拉丁 vocīvus，关联 vacāre 空着；动词空出、使失效也有较早法语来源。'),
 'A1933':dict(words=['cottage','cottages','massage','massages','massaged','massaging'],label='-age 的借词分支：小屋与揉按过程',note='cottage 经旧法语小屋词与 -age 的组合借入；massage 借法语 masser + -age。massage 的词尾通常读 /ɑːʒ/，与多数英语 -age 派生词不同；masser 更早来源有争论。'),
}
W('harassment','英 /ˈhærəsmənt/；美常见 /həˈræsmənt/，也有 /ˈhærəsmənt/','骚扰；反复烦扰、施压的行为',
 '让一个人不断被纠缠、攻击或烦扰，难以安稳下来，这种行为就是 harassment。常突出反复侵扰、施压带来的困扰感。',
 'harass + -ment，把骚扰的动作变成名词。harass 借法语 harasser 使疲惫、烦扰，更早来源未定；名词 harassment 是英语中的后续派生。',
 [['法语 harasser → 英语 harass','使疲惫、反复烦扰'],['harass + -ment → harassment','骚扰行为；遭受侵扰的状态']],
 'online harassment 网络骚扰；workplace harassment 工作场所骚扰；complaints of harassment 关于骚扰的投诉。',
 'report harassment；a policy on harassment。','harassment 通常不可数，描述一件具体事件可说 an incident of harassment。harass 是动作，harassed 可说受到侵扰的人或状态；名词 -ment 把行为本身拿出来讨论。',
 ('The company explained its policy on workplace harassment.','公司说明了处理工作场所骚扰的政策。'),('She described the repeated messages as harassment.','她把那些反复发来的信息称为骚扰。'),sources=['https://en.wiktionary.org/wiki/harassment#English','https://www.etymonline.com/word/harassment'])
W('void','/vɔɪd/','空的、缺少的；空隙、空缺；无效的；使失效',
 '本来可以有东西的位置空着，是 void；一个人离开后留下的空落，也可以是 a void。用到规则、文件上，则像是把它的效力清空。',
 '形容词经法语 voide、viude 等接拉丁 vocīvus 空着的，与 vacāre 空着同族；名词有空处、空缺义。动词另经法语 voider、vuider 清空的路线借入，后来常用于使失效。',
 [['拉丁空着词族 → 法语 voide 等 → void 形容词、名词','空的 → 空处、缺口、缺少感'],['法语 voider／vuider → void 动词','清空 → 使失去效力']],
 'fill a void 填补空缺；null and void 无效；void of meaning 毫无意义；void a ticket 使票作废。',
 'a void in her life；declare something void。','a void 可以是空间缺口，也可以是心理上的缺失；void 作形容词说无效，void 作动词说使失效。devoid of 常见于完全缺乏某物的表达，与 void 同族。',
 ('His departure left a void in the team.','他的离开给团队留下了空缺。'),('The clerk marked the damaged ticket as void.','工作人员把那张损坏的票标成无效。'),sources=['https://en.wiktionary.org/wiki/void#English','https://www.etymonline.com/word/void'])
W('voided','/ˈvɔɪdɪd/','已经使失效、作废；清空、排出过〔具体语境〕',
 '让原来的一张票、一项记录失去效力，这个动作做完了，就是 voided；东西被清空、排出的旧义也仍见于特定语境。',
 'void + -ed，词基以 /d/ 结尾，因此增加 /ɪd/，成为两个音节。动词 void 接法语 voider、vuider 清空词族，与形容词空的相连。',
 [['法语清空词族 → 英语 void 动词','清空 → 使失去效力等'],['void + -ed → voided','已经作废、清空；被作废的']],
 'a voided ticket 已作废的票；voided the transaction 使那笔交易作废；was voided 被作废。',
 'marked as voided；a voided receipt。','voided 说使其失效的动作已发生，empty 常只描述里面没有东西。这里 -ed 在 /d/ 后多出一个音节，和 emailed、appealed 的 /d/ 词尾读法不同。',
 ('The duplicate ticket was voided before it could be used.','那张重复票在使用前就被作废了。'),('She kept the voided receipt with the other records.','她把那张作废收据和其他记录放在一起保存。'),sources=['https://en.wiktionary.org/wiki/voided#English','https://en.wiktionary.org/wiki/void#English'])
W('cottage','英 /ˈkɒtɪdʒ/；美 /ˈkɑːtɪdʒ/','乡间小屋；小住宅',
 '一栋不大、可以独立住人的乡间房子，就是 cottage。早期常指简朴的小屋，今天也可以是舒适的乡间住宅、度假屋。',
 '经古法语 cote 小屋与盎格鲁法语 -age 的组合借入，早期可能包括附属小屋的整片产权。cote 较早可能来自古诺尔斯语 kot，与古英语 cot 小屋同族；不要把现代“婴儿床”cot 的印度语来源混为一谈。',
 [['小屋词族 → 古法语 cote + -age → cottage','小屋及相关住所、附属物'],['英语 cottage 的用法发展','简朴住处 → 乡间小住宅、度假小屋']],
 'a country cottage 乡间小屋；a holiday cottage 度假小屋；cottage industry 家庭作坊式产业；cottage cheese 茅屋奶酪、一种软质凝乳奶酪。',
 'a cottage by the lake；a stone cottage。','cottage 常带小住宅、乡间住所的感觉，不一定是木屋，也不保证简陋。cabin 常让人想到较简单的木屋、舱室，两词场景有重合，来源不同。',
 ('They rented a small cottage beside the lake.','他们在湖边租了一栋小屋。'),('A narrow path led from the cottage to the garden.','一条窄路从小屋通向花园。'),sources=['https://en.wiktionary.org/wiki/cottage#English','https://www.etymonline.com/word/cottage','https://www.etymonline.com/word/cot'])
W('cottages','英 /ˈkɒtɪdʒɪz/；美 /ˈkɑːtɪdʒɪz/','乡间小屋、小住宅〔cottage 的复数〕',
 '一排排、一栋栋不大的乡间住宅，就是 cottages；它们可以简朴，也可以是如今的度假住处。',
 'cottage + -s，原词末尾 /dʒ/ 后增加 /ɪz/，拼写为 cottages。cottage 经法语小屋词与 -age 的组合借入，现代复数按英语规则形成。',
 [['法语 cote + -age → 英语 cottage','小屋、住所 → 乡间小住宅'],['cottage + -s → cottages','多栋小屋；发音增加 /ɪz/']],
 'stone cottages 石头小屋；holiday cottages 度假小屋；a row of cottages 一排小屋。',
 'cottages near the coast；cottages surrounded by trees。','cottages 的 /ɪz/ 是复数词尾；单数 cottage 最后 /ɪdʒ/ 属于原词。小屋可以由石、砖、木建成，具体材料要看修饰词。',
 ('A row of stone cottages stood beside the village green.','村中的草地旁立着一排石头小屋。'),('The old farm buildings have been turned into holiday cottages.','那些旧农场建筑已改成了度假小屋。'),sources=['https://en.wiktionary.org/wiki/cottages#English','https://en.wiktionary.org/wiki/cottage#English'])
W('massage','英 /ˈmæsɑːʒ/；美 /məˈsɑːʒ/','按摩、揉按；揉按身体；修饰、操弄〔数据等，引申〕',
 '用手压、揉，让某个部位得到揉按，是 massage；把数据来回调整、让呈现更好看，也会借用“揉弄”的感觉，通常含批评意味。',
 '借法语 massage，由 masser 揉按与 -age 构成，英语后来也作动词。masser 更早来源有争论，阿拉伯语触摸词族与葡萄牙语揉面词族等都有分析；不能写成已确定的一条路线。',
 [['法语 masser + -age → massage 名词','揉按这一过程；更早来源未定'],['英语借入 massage，并作动词','按摩；后来引申为调整、操弄数据等']],
 'a shoulder massage 肩部按摩；massage the hands 揉按双手；massage the figures 修饰、操弄数字。',
 'a gentle massage；massage someone’s shoulders。','massage 常见词尾读 /ɑːʒ/，保留法语借词特点；message 信息、消息则通常读 /ˈmesɪdʒ/。两词拼写相近，意思和发音都不同。',
 ('He asked for a gentle shoulder massage.','他请人轻轻按摩一下肩膀。'),('The report accused the company of massaging the figures.','报告指责那家公司修饰了数据。'),sources=['https://en.wiktionary.org/wiki/massage#English','https://www.etymonline.com/word/massage'])
W('massages','英 /ˈmæsɑːʒɪz/；美 /məˈsɑːʒɪz/','按摩〔复数〕；揉按、按摩〔第三人称单数〕',
 '一次次按摩可以数成 massages；某个人用手揉按身体，也可以用动词 massages。',
 'massage + -s，原词末尾 /ʒ/ 后增加 /ɪz/，写成 massages。massage 是法语借词，含 masser 与 -age；英语复数和第三人称按普通规则变化。',
 [['法语揉按词族 → 英语 massage 名词、动词','揉按、按摩'],['massage + -s → massages','多次按摩；单数主语揉按']],
 'shoulder massages 肩部按摩；offers massages 提供按摩服务；massages her hands 揉按她的双手。',
 'short massages；massages his temples。','massages 的词尾是 /ʒɪz/；messages 消息则是 /dʒɪz/。前面重音、元音也不同，按 massage 和 message 两个基本词分别认。',
 ('The hotel offers short shoulder massages by appointment.','酒店提供需要预约的短时肩部按摩。'),('She massages her hands while waiting for the kettle to boil.','等水壶烧开时，她揉按着自己的双手。'),sources=['https://en.wiktionary.org/wiki/massages#English','https://en.wiktionary.org/wiki/massage#English'])
W('massaged','英 /ˈmæsɑːʒd/；美 /məˈsɑːʒd/','按摩过、揉按过；修饰、调整过〔数据等〕',
 '揉按这个动作已经做过，是 massaged；说数字被“揉弄过”，往往暗示为了好看而调整了呈现。',
 'massage 末尾已有 e，加 -d → massaged。原词以 /ʒ/ 结尾，过去词尾读 /d/，不另增 /ɪd/ 音节。法语名词借入英语后，动词按规则形成过去式。',
 [['法语 massage → 英语名词、动词','揉按、按摩；数据调整的引申'],['massage 去 e + -ed → massaged','揉按过；被调整、修饰过']],
 'massaged his shoulders 按摩过他的肩膀；massaged the numbers 修饰了数字；carefully massaged wording 经过巧妙调整的措辞。',
 'gently massaged；had been massaged。','massaged 的 /ʒd/ 连起来读；voided 则在 /d/ 后增加 /ɪd/。数据、措辞语境的 massaged 常带刻意调整的意味，并不只是在说身体动作。',
 ('She gently massaged his shoulders for a minute.','她轻轻按摩了他的肩膀一会儿。'),('The figures had been massaged to make the results look better.','这些数字经过了修饰，好让结果看起来更好。'),sources=['https://en.wiktionary.org/wiki/massaged#English','https://en.wiktionary.org/wiki/massage#English'])
W('massaging','英 /ˈmæsɑːʒɪŋ/；美 /məˈsɑːʒɪŋ/','正在按摩、揉按；修饰、操弄〔数据等〕；massage 的 -ing 形式',
 '把揉按当作持续的动作，就是 massaging；用于数据时，则把调整、修饰的过程形象地说成揉弄。',
 'massage 去掉末尾不发音 e，再加 -ing → massaging，保留 /ʒ/。词基由法语 masser + -age 的名词借入英语，再有动词和规则形式。',
 [['法语 massage → 英语 massage 名词、动词','揉按、按摩 → 另有修饰数据等引申'],['massage 去 e + -ing → massaging','进行中的揉按、调整']],
 'massaging the shoulders 揉按肩膀；massaging the figures 修饰数据；spend time massaging 花时间揉按、调整。',
 'gently massaging；accused of massaging the numbers。','massaging 和 messaging 正在发信息是不同词；前者来自 massage /ɑːʒ/ 词族，后者来自 message /ɪdʒ/ 词族。先认基本词，再读扩展形式。',
 ('He was massaging his hands as he listened.','他一边听，一边揉按自己的双手。'),('The article questions whether the team was massaging the figures.','文章质疑该团队是否在修饰数据。'),sources=['https://en.wiktionary.org/wiki/massaging#English','https://en.wiktionary.org/wiki/massage#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xq',ROOTS,WORDS)
 extend_lessons()
