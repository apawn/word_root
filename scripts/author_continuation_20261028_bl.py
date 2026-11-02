"""Net: mesh and net amount are parallel etymologies."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
NET=[['两条独立来路：古英语 net(t)；拉丁语 nitidus → 古法语 net','前者是网；后者是明亮、洁净'],['英语 net','网、用网捕捉；另一支为净的、扣除后的']]
W('net','/net/','网；用网捕捉；净的；净得',
 '一边是一根根线连成的网，另一边是把应扣部分拿走后剩下的净数。两个画面分别记。',
 '网继承古英语 net(t)。净的经古法语 net 追到拉丁语 nitidus 明亮、洁净。它们只是后来同形，不能把净利润编成渔网捞到的钱。',NET,
 'a fishing net 捕鱼网；net a goal 把球打进球门。net weight 净重扣掉包装，net profit 净利润扣掉相关成本费用；net 也可作动词表示净得。the Net 常简称互联网。',
 'a safety net；a mosquito net；net weight；net profit；net a goal。',
 'gross 总的、未扣除的，net 净的、扣除后的；具体扣什么由所谈的重量、收入等决定。网络词中的 net 属于网这一支。',
 ('The ball landed in the net.','球落进了网里。'),('The net weight excludes the packaging.','净重不包括包装。'),('The school fair netted enough money to buy new books.','学校义卖净得的钱足够买一批新书。'))
W('netting','/ˈnetɪŋ/','网状材料；网；结网、用网捕捉的活动',
 '把网当成一片材料来看，例如罩在果树上的网布。',
 'net + -ing，末尾 t 双写。材料义来自网这一支；也可作为 net 的现在分词，意思随动词而定。',NET+[['net → netting','网 → 网状材料；相关活动']],
 'fine netting 细网，protective netting 防护网。名词材料义通常不可数；netting a goal 这样的动词用法则是把球打进。',
 'fine netting；protective netting；cover something with netting。',
 'a net 强调一张网这个成品，netting 常强调网状材料；不是每个 -ing 结尾都只是正在做某事。',
 ('Fine netting covered the young plants.','细网罩在幼苗上方。'),('The costume was decorated with layers of soft netting.','服装上装饰了几层柔软的网纱。'))
W('fishnet','/ˈfɪʃnet/','渔网；网眼织物',
 '先是用来捕鱼的网；同样的网眼外观也给了一类织物名字。',
 'fish 鱼 + net 网，中古英语已有 fishnet。后来又用来称有明显网眼、常呈菱形的织物。',C('fish 鱼','net 网','fishnet','渔网；外观像渔网的织物'),
 'a fishnet 可以是一张渔网；fishnet fabric 是网眼面料，fishnet stockings 是网眼长袜。织物只是网状外观相似，不是旧渔网改成的衣服。',
 'a fishing boat’s fishnet；fishnet fabric；fishnet stockings。',
 'fishnet 与 fishing net 都可说渔网；谈服装面料时 fishnet 是一种外观名称，不暗示实际用途是捕鱼。',
 ('An old fishnet hung on the wall of the fishing museum.','渔业博物馆墙上挂着一张旧渔网。'),('The designer added a strip of fishnet fabric to the jacket.','设计师在夹克上加了一条网眼面料。'))
W('dragnet','/ˈdræɡnet/','拖网；大规模搜捕',
 '一张网拖过去，把一片范围都搜过；这个画面后来借给警方的广泛搜查。',
 '现代可拆 drag 拖 + net 网；旧英语已有相近的拖网复合形式，后来形成 dragnet。由捕鱼方式引申到大范围搜捕。',C('drag 拖','net 网','dragnet','拖网 → 大范围搜捕'),
 'a police dragnet 指警方扩大范围寻找、搜捕嫌疑人。比喻重点在撒开范围搜，不保证已经抓到人。',
 'a police dragnet；launch a dragnet；escape the dragnet。',
 'dragnet 是一场搜捕或一种网；drag 是拖这个动作。不要因电视剧使用这个名字就把它只记成剧名。',
 ('The display shows how a traditional dragnet was used.','展览展示了传统拖网的使用方式。'),('In the novel, the suspect escapes a citywide dragnet.','小说里，嫌疑人逃过了一场全市搜捕。'))
W('netball','英 /ˈnetbɔːl/；美 /ˈnetbɔːl/','篮网球；无挡板篮球',
 '名字抓住了球投向篮网上的画面，但它是有自己规则的一项运动。',
 'net 网 + ball 球，英语复合名称；运动与篮球有历史关系。',C('net 网','ball 球','netball','以篮网为得分目标的球类运动名称'),
 'play netball 打篮网球，a netball team 篮网球队。看到这个词应想到具体运动，不是所有带球网的球类总称。',
 'play netball；a netball match；the school netball team。',
 'netball 与 basketball 相关但不是完全相同的项目；也不是排球 volleyball。',
 ('She joined the school netball team last term.','她上学期加入了学校篮网球队。'),('Our netball match was moved indoors because of the rain.','我们的篮网球比赛因下雨改到室内。'))
W('botnet','英 /ˈbɒtnet/；美 /ˈbɑːtnet/','僵尸网络',
 '很多被控制的设备连成一群，像一支能被远程调动的队伍。',
 'bot 是 robot 的缩短形式，net 缩自 network；组合表示一组受协调控制的网络设备。安全语境常指被恶意控制的设备群。',C('bot 自动程序、受控设备，源于 robot','net 网络，缩自 network','botnet','可协调控制的一群联网设备'),
 '安全新闻中的 botnet 不是一个孤立病毒，而是由被控制的设备组成的网络。它可以被用来发送垃圾信息或发起攻击。',
 'a botnet of infected devices；disrupt a botnet；botnet activity。',
 'bot 可是一个自动程序或受控设备，botnet 强调它们组成的群体；不等于 spyware 间谍软件这个软件类别。',
 ('The report described a botnet of infected home routers.','报告描述了一个由受感染家用路由器组成的僵尸网络。'),('Researchers detected unusual traffic linked to a botnet.','研究人员发现了与一个僵尸网络有关的异常流量。'),sources=['https://en.wiktionary.org/wiki/botnet#English','https://csrc.nist.gov/glossary/term/botnet'])
W('darknet','英 /ˈdɑːknet/；美 /ˈdɑːrknet/','暗网；需特定软件、配置或授权访问的网络',
 '想成普通公开浏览之外的一层网络，dark 在这里强调不直接显露于普通访问方式。',
 'dark 暗的 + net 网络；由可见性、访问受限的比喻形成网络术语。',C('dark 不直接显露的','net 网络','darknet','需要特定访问条件的网络'),
 '这个词指一类需要特殊软件、配置或授权才能访问的网络；具体技术和用途并不全相同。新闻常把它与其中的犯罪活动联系起来，但词本身不是所有非法网站的总称。',
 'a darknet；darknet traffic；research on darknet networks。',
 'darknet 不能泛指搜索引擎搜不到的所有网页。普通网站没被搜索引擎收录，也不因此就成了 darknet。',
 ('The article explains what the term darknet means.','这篇文章解释了 darknet 一词的意思。'),('Her research examines communication on darknet networks.','她的研究考察暗网网络上的通信。'))
R('B3310','网、网络；另有不同源的净额义','NET：线与节点相连；净额另记','实体网的网眼容易看见，通信网络则把设备与连接织在一起。净的来自另一条洁净的词源。',
 '网一支接古英语 net(t)，可扩展为通信网络；净的一支经法语来自拉丁语 nitidus，表示去掉应扣部分后所余。',
 'net → netting；fish + net、drag + net、net + ball；network 一支再看 internet、intranet、subnet、botnet、darknet。',
 [['实体网与其外观、用途','net · netting · fishnet · dragnet · netball'],['设备相连的网络','network · internet · intranet · subnet · botnet · darknet']],
 'net profit 净利润不是捕鱼网义；fishnet 是渔网或网眼织物，botnet 是受协调控制的设备网络。',
 'A fishnet catches fish; a botnet connects controlled devices.\n\n渔网用于捕鱼；僵尸网络把受控设备连接成群。',
 'net netting fishnet dragnet netball network internet intranet subnet botnet darknet')
if __name__ == '__main__':save('continuation_20261028_bl',ROOTS,WORDS)
