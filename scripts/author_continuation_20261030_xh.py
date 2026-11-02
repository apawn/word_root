"""Receiving, learning, studying, collecting and connecting."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0168':dict(words=['receive','receives','receiving'],label='receive → receives／receiving：东西、消息到了这边',note='receive 接拉丁 re- 加 capere 的 recipere，经法语借入；receiving 去掉不发音 e 再加 -ing。'),
 'B2690':dict(words=['learn','learns'],label='learn → learns：学会、学到与得知',note='learn 继承古英语 leornian；learns 不只说上课，也可说新知道一个事实。'),
 'C1440':dict(words=['study','studying'],label='study → studies／studying：持续用心投入',note='study 加 -ing 保留 y，和 studies 变 y 为 i 的形式分开；名词、动词有相关法语、拉丁借入路线。'),
 'C0659':dict(words=['collect','collects'],label='collect → collects：聚到一起、收集领取',note='com- 与 legere 经 colligere、collectus 等形成收集词族，collects 是现代第三人称形式。'),
 'C0803':dict(words=['connect','connects','connecting'],label='connect → connects／connecting：把各部分系在一起',note='connect 接拉丁 con- 加 nectere 系、绑；具体连接可以是线路、交通或人与人的联系。'),
}
W('receives','/rɪˈsiːvz/','收到、接收到；得到、受到；receive 的第三人称单数',
 '别人把东西送来，或消息、支持传到这里，是 receives。它先说东西、反应到了这一方，再由宾语说明是什么。',
 'receive 已有 e，加 s；/v/ 后读 /z/。拉丁 re- 回、向回 + capere 拿形成 recipere 接纳，经古法语 receivre 等传入英语。',
 [['拉丁 re- + capere → recipere → 古法语 receivre → receive','拿到这边、接纳 → 收到'],['receive + -s → receives','单数主语现在收到、受到']],
 'receives a letter 收到信；receives support 得到支持；receives visitors 接待来访者；receives a signal 接收信号。',
 'receives from ...；receives good reviews。','receives an invitation 是收到了邀请，accepts an invitation 是接受邀请。receives visitors 常说接待来访者，receives a letter 是收到信；对象不同，接纳体现为不同动作。',
 ('The office receives deliveries every morning.','办公室每天早上都会收货。'),('The exhibition receives many visitors on weekends.','周末有很多人来参观这个展览。'),sources=['https://en.wiktionary.org/wiki/receives#English','https://en.wiktionary.org/wiki/receive#English'])
W('receiving','/rɪˈsiːvɪŋ/','正在接收、收到；接待；receive 的 -ing 形式',
 '东西、信息正在送到你这一边，是 receiving。它可以是接到消息、收货，也可以是接待来客。',
 'receive 去掉末尾不发音 e，加 -ing，保留 /siːv/。词基由拉丁 recipere 经法语相关形式传入，和拿、接纳词族相连。',
 [['拉丁 recipere → 法语 receivre 等 → receive','接纳、收到'],['receive 去 e + -ing → receiving','进行中的接收、接待']],
 'receiving messages 收消息；receiving goods 收货；receiving guests 接待客人；a receiving area 收货区、接待区〔看场景〕。',
 'thanks for receiving us；receiving from several sources。','receiving 常在信息、货物传输中说接收方的动作，sending 说送出方动作。接收、阅读、同意是不同环节，不能仅凭 receiving 把它们合成一件事。',
 ('The device is receiving a signal from the station.','设备正在接收来自站点的信号。'),('Thank you for receiving us at such short notice.','谢谢你在这么仓促的情况下接待我们。'),sources=['https://en.wiktionary.org/wiki/receiving#English','https://en.wiktionary.org/wiki/receive#English'])
W('learns','英 /lɜːnz/；美 /lɜːrnz/','学会、学到；得知；learn 的第三人称单数',
 '原来不会、不了解，后来把知识、技能或事实接进来，就是 learns。它可以说长期学习，也可以是刚知道一个消息。',
 'learn + -s，/n/ 后读 /z/。learn 继承古英语 leornian，经中古英语 lernen 等延续；现代既有学会，也有得知事实的用法。',
 [['古英语 leornian → 中古英语 lernen → learn','学习、获得知识技能；得知'],['learn + -s → learns','单数主语现在学到、得知']],
 'learns quickly 学得快；learns to drive 学会开车；learns from mistakes 从错误中学习；learns that ... 得知……。',
 'learns something new；learns by doing。','learns to do 侧重学会一种能力，learns that ... 是得知某个事实。studies 强调投入学习、研究的过程，learns 常也强调学到或知道了什么。',
 ('She learns new words by using them in short stories.','她通过把新词用进短故事里来学习。'),('He learns that the meeting has moved to another room.','他得知会议换到了另一个房间。'),sources=['https://en.wiktionary.org/wiki/learns#English','https://en.wiktionary.org/wiki/learn#English'])
W('studying','/ˈstʌdiɪŋ/','正在学习、研究、仔细查看；study 的 -ing 形式',
 '把注意力持续放进一件事，是 studying。可以是学一门课程，也可以是盯着地图、资料认真研究。',
 'study + -ing，直接保留 y，写 studying；读音里 /i/ 与 /ɪŋ/ 衔接。study 名词、动词经法语相关形式接拉丁 studium、studēre 用心投入的词族。',
 [['拉丁 studium／studēre → 法语 estudie／estudier 等 → study','专注、热衷 → 学习、研究'],['study + -ing → studying','进行中的学习、认真查看']],
 'studying history 学历史；studying for an exam 备考；studying the map 研究地图；studying how ... 研究如何……。',
 'keep studying；studying at college。','studying 常突出学习、研究过程，learning 也可强调获得了知识、能力。studies 把 y 变 ies，studying 则保留 y，加不同词尾的拼写规则要分开。',
 ('She is studying the map before choosing a route.','选路线前，她正在仔细看地图。'),('He spends two evenings a week studying local history.','他每周花两个晚上研究地方历史。'),sources=['https://en.wiktionary.org/wiki/studying#English','https://en.wiktionary.org/wiki/study#English'])
W('collects','/kəˈlekts/','收集、采集；领取；接人、接物；collect 的第三人称单数',
 '把分散的东西聚到一起，是 collects；把准备好的包裹、人接走，也常用 collect。',
 'collect + -s，/t/ 后读 /s/。com- 一起 + legere 选、收集形成 colligere、collectus 等，经中世纪拉丁和法语相关形式进入英语，前缀有 col- 同化形。',
 [['拉丁 com- + legere → colligere／collectus；相关中世纪拉丁、法语形式 → collect','聚到一起、收取'],['collect + -s → collects','单数主语现在收集、领取、接走']],
 'collects stamps 集邮；collects information 收集资料；collects a parcel 取包裹；collects the children 接孩子〔常见英式〕。',
 'collects from several sources；collects people at the station。','collects a parcel 强调去取，receives a parcel 强调收到。collects the children 在接送场景常是接孩子，和收集物件的用法靠对象分开。',
 ('She collects old photographs of the town.','她收集这个镇子的老照片。'),('He collects the children from school on Fridays.','周五由他去学校接孩子。'),sources=['https://en.wiktionary.org/wiki/collects#English','https://en.wiktionary.org/wiki/collect#English'])
W('connects','/kəˈnekts/','连接、接通；建立联系；使相连；connect 的第三人称单数',
 '把原本分开的部分接到一起，让它们能通行、传递或互相联系，是 connects。桥接两岸，线接设备，故事也能把人联系起来。',
 'connect + -s，/t/ 后读 /s/。拉丁 con- 一起 + nectere 系、绑形成 connectere、cōnectere 等形式，借入英语。',
 [['拉丁 con- + nectere → connectere／cōnectere → connect','系在一起 → 连接'],['connect + -s → connects','单数主语现在使相连、接通']],
 'connects the two rooms 连接两间房；connects to the network 连上网络；connects with people 与人建立联系；connects A to B 把 A 接到 B。',
 'connects directly；connects the village to the town。','connects A to B 说明把两端接起来，connects with someone 可以说联系、沟通上有共鸣。具体连接是实物、通路还是人际关系，靠对象判断。',
 ('A narrow bridge connects the island to the mainland.','一座窄桥把岛屿和大陆连接起来。'),('The small device connects to the computer with a cable.','这个小设备通过电缆连到电脑。'),sources=['https://en.wiktionary.org/wiki/connects#English','https://en.wiktionary.org/wiki/connect#English'])
W('connecting','/kəˈnektɪŋ/','正在连接、接通；起连接作用的；衔接下一程的；connect 的 -ing 形式',
 '把分开的部分接起来，是 connecting；一扇门、一条路或下一程交通负责把两边接上时，也能用它修饰名词。',
 'connect + -ing，直接加，末尾 ct 不双写。词基接拉丁 con- 一起 + nectere 系、绑，形成 connectere／cōnectere 等。',
 [['拉丁 con- + nectere → connectere／cōnectere → connect','系在一起、连接'],['connect + -ing → connecting','进行中的连接；有连接、衔接作用的']],
 'connecting the wires 正在接电线；a connecting door 连通门；a connecting flight 衔接下一程的航班；connecting with people 与人建立联系。',
 'connecting the two buildings；a connecting passage。','connecting a device 是进行中的动作；a connecting door 是说明门的用途。connecting 不必每次都译成正在，放到名词前也可描述连接关系。',
 ('A connecting door joins the two rooms.','一扇连通门把两个房间连接起来。'),('We are connecting the new display to the computer.','我们正在把新显示器连到电脑上。'),sources=['https://en.wiktionary.org/wiki/connecting#English','https://en.wiktionary.org/wiki/connect#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xh',ROOTS,WORDS)
 extend_lessons()
