"""Evaluation, desired outcomes and permission in ordinary usage."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C1379':dict(words=['respect','respected'],label='respect → respected：看重一个人的能力、品行',note='拉丁回看、留意的词族，发展为认真看待与尊敬；respected 侧重受到尊敬的地位。'),
 'C1602':dict(words=['value','valued'],label='value → valued：觉得值得，因而珍视',note='拉丁 valere 强健、有价值，经法语价值词进入英语；valued 可以说被珍视，也可以在估价结构中说被估为某价。'),
 'C1122':dict(words=['appreciate','appreciated'],label='appreciate → appreciated：认识价值并表达认可',note='由拉丁定价、价值词族扩大为珍视、感激与充分认识；appreciated 说受到相应评价。'),
 'B3541':dict(words=['desire','desired'],label='desire → desired：想要得到的结果',note='desire 接法语和拉丁 desiderare 渴望；更深与星辰有关的解释有争议，精讲不把故事当定论。'),
 'C0707':dict(words=['recommend','recommended'],label='recommend → recommended：提出值得采用的选择',note='较早有托付、称许的词义，发展为推荐、建议；re- 在这里不必理解为再推荐一遍。'),
 'C0751':dict(words=['permit','permitted','permission'],label='permit → permitted：允许通过、允许做',note='per- 通过 + 拉丁 mittere 放行、送出；分词双写 t，表示得到允许。'),
 'C0097':dict(words=['authorize','authorized'],label='authorize → authorized：正式赋予权限',note='authority、authorize 接拉丁 auctor 负责人、权威等词族；authorized 说有授权，常用于人员、渠道和操作。'),
}
W('respected','/rɪˈspektɪd/','受尊敬的、受敬重的；respect 的过去式、过去分词',
 '一个人的能力、判断或品行让大家愿意认真听他说话、郑重看待他，就可以说 he is respected。它突出别人对他的敬重。',
 'respect + -ed，/t/ 后读 /ɪd/。respect 接拉丁 re- 回、specere 看形成的 respicere 回看、留意词族，再发展为看重、尊敬。',
 [['拉丁回看、留意词族 → respect','注意、认真看待 → 敬重'],['respect + -ed → respected','受到尊敬；过去尊重了某人、某事']],
 'a respected teacher 受敬重的老师；a respected expert 受尊敬的专家；respected for honesty 因诚实受敬重；widely respected 广受尊敬。',
 'a highly respected colleague；be respected by others。','respected 是受尊敬，respectful 是表现得尊重别人，respectable 常说体面、值得尊重。名气很大不必然等于受敬重。',
 ('She is widely respected for her fairness.','她因处事公正而广受尊敬。'),('He became a respected voice in the local community.','他成了当地社区中一位意见受到敬重的人。'),sources=['https://www.etymonline.com/word/respect','https://en.wiktionary.org/wiki/respected#English'])
W('valued','/ˈvæljuːd/','被珍视、受重视的；被估价为……的；value 的过去式、过去分词',
 '你的付出被看见，意见有人认真听，团队会让你感到 valued。换到估价场景，valued at 则说这件东西被估成多少钱。',
 'value 去末尾 e，加完整 -ed，词尾读 /d/。value 经法语 valoir、value 接拉丁 valere 强健、有价值；动词发展出估价和看重两种常见作用。',
 [['拉丁 valere → 法语价值词 → value','有力量、有价值 → 价值、估价、重视'],['value 去 e + -ed → valued','被珍视；被估为某价']],
 'a valued friend 珍视的朋友；a valued member 受重视的成员；feel valued 感到被重视；be valued at ... 被估价为……。',
 'a highly valued skill；make someone feel valued。','valued 强调有人珍视或已作估价，valuable 强调本身有价值。a valued old letter 可能不值钱，但对主人很珍贵。',
 ('A simple thank you can make people feel valued.','一句简单的谢谢，就能让人感到被重视。'),('The painting was valued at two thousand dollars.','这幅画被估价为两千美元。'),sources=['https://www.etymonline.com/word/value','https://en.wiktionary.org/wiki/valued#English'])
W('appreciated','/əˈpriːʃieɪtɪd/','受到感激、认可、欣赏的；appreciate 的过去式、过去分词',
 '你帮忙做的事，对方知道有用、也领你的情，便可以说 Your help is appreciated。核心是这份价值被人看见。',
 'appreciate 去 e 加 -ed，词尾读 /ɪd/。接晚期拉丁 appretiare 定价，由 ad- 与 pretium 价格组成；看出、评定价值，扩大为珍视、感激、充分认识。',
 [['拉丁 ad- + pretium → appretiare','给出价格、评定价值'],['appreciate → appreciated','欣赏、感激 → 得到认可或感激；也可说过去已认识到']],
 'Your help is greatly appreciated 非常感谢你的帮助；feel appreciated 感到付出得到认可；a much appreciated gesture 令人十分感激的举动。',
 'I really appreciated ...；be deeply appreciated。','I appreciated the difficulty 是我当时充分认识到了困难。appreciate 也可指价值上涨，判断 appreciated 的具体含义要看主语和上下文。',
 ('Your patience is greatly appreciated.','非常感谢你的耐心。'),('I appreciated how much work had gone into the project.','我充分认识到了这个项目投入了多少工作。'),sources=['https://www.etymonline.com/word/appreciate','https://en.wiktionary.org/wiki/appreciated#English'])
W('desired','英 /dɪˈzaɪəd/；美 /dɪˈzaɪərd/','想要的、期望得到的；desire 的过去式、过去分词',
 '你先在心里定了一个想达到的状态，desired result 就是那个期望的结果。它说愿望指向哪里，不保证结果已经发生。',
 'desire 去末尾 e，加完整 -ed。经古法语 desirrer 接拉丁 desiderare 渴望、期待；更早与 sidus 星辰的联系有不同解释，不能据此断言 desire 就是向星星许愿。',
 [['拉丁 desiderare → 法语 → desire','渴望、期待某物'],['desire 去 e + -ed → desired','曾想要；所希望得到的']],
 'the desired result 期望的结果；the desired effect 预期效果；the desired temperature 所需温度；leave much to be desired 有很多不尽如人意之处。',
 'achieve the desired outcome；if desired。','desired 是被想要的，desirable 是值得想要、理想的。leave a lot to be desired 的画面是还有许多想得到的东西没有得到，常用来表达不满意。',
 ('Adjust the lamp to the desired height.','把灯调到所需高度。'),('The room was clean, but the service left a lot to be desired.','房间很干净，但服务有很多不尽如人意的地方。'),sources=['https://www.etymonline.com/word/desire','https://en.wiktionary.org/wiki/desired#English'])
W('recommended','/ˌrekəˈmendɪd/','被推荐的、建议采用的；recommend 的过去式、过去分词',
 '有人替你比较过选择，觉得这一本书、这条路线或这个做法值得考虑，于是把它推荐给你。recommended 就从被推荐这一面描述它。',
 'recommend + -ed，/d/ 后读 /ɪd/。经中古拉丁 recommendare 接 commendare 托付、称许；这里 re- 可能加强意义，不能一概解作再来一次。',
 [['拉丁 commendare → recommendare → recommend','托付、称许 → 推荐、建议'],['recommend + -ed → recommended','已经推荐；建议采用的']],
 'a recommended book 推荐读物；the recommended route 建议路线；highly recommended 非常推荐；recommended by a friend 朋友推荐的。',
 'recommended reading；the recommended method。','recommended 表示建议采用，不等于 required 必须。recommended that 后可接动词原形或 should 加原形：recommended that we leave／should leave。',
 ('This is the route recommended by the visitor centre.','这是游客中心推荐的路线。'),('The teacher recommended that we read the introduction first.','老师建议我们先读引言。'),sources=['https://www.etymonline.com/word/recommend','https://en.wiktionary.org/wiki/recommended#English'])
W('permitted','/pəˈmɪtɪd/〔美 r 发音〕','被允许的、获准的；permit 的过去式、过去分词',
 '原本有一道限制，但规则或有权决定的人允许你通过、允许你做，这时就是 permitted。它说有没有许可。',
 'permit 最后一节重读，双写 t 加 -ed。拉丁 per- 通过 + mittere 放行、送出 → permittere 放行、允许，经法语及拉丁来源进入英语。',
 [['拉丁 per- + mittere → permittere','让通过、放行 → 允许'],['permit 双写 t + -ed → permitted','允许了；得到许可']],
 'be permitted to enter 获准进入；Photography is permitted 允许拍照；the maximum permitted size 允许的最大尺寸；not permitted 不被允许。',
 'permitted by the rules；only permitted in this area。','be permitted to do 后接动词原形；permit doing 和 permit someone to do 是常见主动结构。名词 permit 是许可证，通常重读前面，过去动词仍重读后面。',
 ('Visitors are permitted to take photographs in this room.','参观者可以在这个房间拍照。'),('We checked the maximum permitted size before packing.','打包前，我们核对了允许的最大尺寸。'),sources=['https://www.etymonline.com/word/permit','https://en.wiktionary.org/wiki/permitted#English'])
W('authorized','英 /ˈɔːθəraɪzd/；美 /ˈɔːθəraɪzd/〔r 发音〕','获授权的、正式批准的；authorize 的过去式、过去分词',
 '有人有权决定，并明确把做这件事的权限交给你。authorized 就是拿到了这份正式许可或授权。',
 'authorize 去 e 加 -ed，词尾读 /d/。经法语 autoriser 与中古拉丁 auctorizare 接 auctor 负责人、权威等词；更早与 augere 增加相关，现代重点是赋予权限。',
 [['拉丁 auctor → 法语、拉丁授权动词 → authorize','负责、提供权威的人 → 正式赋予权限'],['authorize + -ed → authorized','已正式批准；持有相应权限']],
 'authorized staff 授权工作人员；an authorized dealer 授权经销商；be authorized to sign 获授权签字；authorized access 获准访问。',
 'an authorized representative；formally authorized。','permitted 泛指允许，authorized 更突出由有权者正式授予权限。authorized 的结尾属于过去、分词形式；英式也常写 authorised。',
 ('Only authorized staff can open this cabinet.','只有获授权的工作人员可以打开这个柜子。'),('She was authorized to sign the documents on behalf of the team.','她获授权代表团队签署文件。'),sources=['https://www.etymonline.com/word/authorize','https://en.wiktionary.org/wiki/authorized#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vj',ROOTS,WORDS)
 extend_lessons()
