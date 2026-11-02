"""Bass homographs and drilling."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['base 低的旧用法，受意大利 basso 影响改写 bass','音乐低音，读 /beɪs/'],['古英语 bærs 等 → bass 鱼名','鲈鱼等俗名，读 /bæs/'],['bast 韧皮的变化 → bass','basswood 的前半接树皮纤维，读 /bæs/']]
W('bass','音乐义 /beɪs/；鱼、韧皮等义 /bæs/','低音、男低音、低音乐器；鲈鱼等〔不同读音、来源〕',
 '乐队里的 bass 与菜单里的 bass，拼写相同，发音和来源却不同。先用声音分开，音乐 /beɪs/，鱼 /bæs/。',
 '低音义是 base 的旧义在意大利 basso 低的影响下改写；鱼名承接古英语 bærs；另有 bast 韧皮的变体用于 basswood。这是多条历史汇到一套拼写。',B,
 'a bass guitar 贝斯、电低音吉他，a bass voice 男低音，turn up the bass 调高低音，sea bass 海鲈类鱼。低音既能说音域，也能依语境说乐手、乐器。',
 'a bass guitar；a bass voice；turn up the bass；sea bass。',
 '音乐 bass 与 base 同音，鱼 bass 不同。bass 低音不等于 bass drum 低音鼓以外的所有具体低音乐器都长一个样。',
 ('She plays bass in a jazz band.','她在爵士乐队里演奏贝斯。'),('The restaurant served sea bass with vegetables.','餐馆供应配蔬菜的海鲈。'))
W('bassist','/ˈbeɪsɪst/','贝斯手、低音乐器演奏者',
 '弹奏或演奏低音乐器的人，是 bassist。现代乐队常想到电贝斯手，爵士、古典语境也可指低音提琴等演奏者。',
 '音乐 bass /beɪs/ + -ist 人物后缀。接音乐这条来源，不接鱼名 /bæs/，不是钓鲈鱼者。',B[:1]+[['bass + -ist → bassist','演奏低音乐器的人']],
 'a jazz bassist 爵士低音乐手，the band’s bassist 乐队贝斯手。具体演奏哪种乐器，由编制、上下文决定。',
 'a jazz bassist；the band’s bassist。',
 'bassist 不是 bass singer 男低音歌手的常规替换称呼。低音歌唱与低音乐器演奏的角色要分开。',
 ('The bassist joined the band last year.','贝斯手去年加入了乐队。'),('The jazz bassist played a short solo.','爵士低音乐手演奏了一段短独奏。'))
W('bassline','/ˈbeɪslaɪn/','低音声部、低音线条',
 '一首歌里那条较低音域、持续组织节奏与和声的乐器线条，是 bassline。不是音量最低、最难听见的那条线。',
 'bass 低音 + line 声部线条。line 在音乐里不是画纸上的直线，而是可以沿着听下去的一条音符、旋律或伴奏进程。',B[:1]+[['bass + line → bassline','乐曲中低音域的乐器声部']],
 'a strong bassline 鲜明有力的低音线条，a repeating bassline 反复的低音线条，follow the bassline 跟着低音声部听。',
 'a strong bassline；a repeating bassline；follow the bassline。',
 'bassline 与 baseline 基线同音不同词；低音域说音高较低，不等于 loudness 音量小。',
 ('The song opens with a repeating bassline.','歌曲以反复的低音线条开场。'),('Listen to how the drums interact with the bassline.','听听鼓点怎样与低音声部配合。'))
W('basswood','/ˈbæswʊd/','椴树；椴木〔尤北美用法〕',
 '这个 bass 不在讲低音，也不在讲鱼，而是树皮里的韧皮纤维。名字把这种材料特征和树木联系起来。',
 'bass 韧皮、纤维义，是 bast 的变化形式 + wood。常指 Tilia 椴树属的若干树，尤见美洲椴的名称，也可说木材。',B[2:]+[['bass 韧皮 + wood → basswood','按韧皮纤维联系形成的树木、木材名']],
 'an American basswood 美洲椴，basswood carving 椴木雕刻。一般木工、植物语境常见，具体是哪种树仍看完整物种名。',
 'American basswood；basswood carving。',
 'basswood 读 /bæs/ 这一支，不按音乐 bass 的 /beɪs/。俗名中的 wood 可以指树，也可以指木材。',
 ('The carver chose basswood for the small figure.','雕刻者选用椴木来做小人像。'),('A large basswood shaded the path.','一棵大椴树给小路遮阴。'))
R('B3147','同形不同音：音乐低音、鱼名与韧皮材料','BASS：先用 /beɪs/ 与 /bæs/ 分开来源','音乐 bass → bassist、bassline；basswood 接 bast 韧皮变体；鱼名 bass 独立记。',
 '拼写相同不代表读音、词源相同。三条短线比一个硬编的低音鱼故事更清楚。',
 'base 受 basso 影响改写为音乐 bass；bærs → 鱼名 bass；bast 变化 → basswood 的前半。',
 [['音乐及人物、声部','bass · bassist · bassline'],['韧皮相关树名','basswood']],
 'bassline 不是 baseline；basswood 不读音乐 bass；bassist 通常说乐器演奏者。',
 'The bassist played the bassline while a basswood carving stood beside the stage.\n\n贝斯手演奏低音声部，舞台旁放着一件椴木雕刻。','bass bassist bassline basswood')
D=[['中古荷兰语 drillen 等 → 英语 drill','钻、转动；工具与反复操练'],['现代动作、器具与练习','钻孔、钻具；反复训练、演练'],['同形的其他借词','drill 斜纹布联系德语 Drillich；山魈类动物名另有来源']]
W('drill','/drɪl/','钻、钻具；钻孔；操练、演练；斜纹布、山魈类动物〔其他来源〕',
 '钻头转着打孔，是 drill；技能反复练熟，也叫 drill。fire drill 是消防演习，不是在火里钻洞。',
 '工具、动作与操练主线借中古荷兰语 drillen 等转动、钻的形式。斜纹布义另借德语 Drillich；非洲灵长类 drill 的名称来源不明，不能全部塞进旋转画面。',D,
 'an electric drill 电钻，drill a hole 钻孔，a fire drill 消防演习，pronunciation drills 发音反复练习，You know the drill. 你知道该怎么做。',
 'an electric drill；drill a hole；a fire drill；know the drill。',
 'a drill 可以是工具，也可是一轮演习、训练。drill into someone 反复灌输某事，与把钻头钻进物体在句意上要分开。',
 ('He used a drill to make the holes.','他用钻具打孔。'),('The school held a fire drill this morning.','学校今天上午进行了消防演习。'))
W('drilling','/ˈdrɪlɪŋ/','钻孔、钻探；反复操练；斜纹布等〔另有同形用法〕',
 'drilling noise 多半是钻孔声，drilling students on verbs 则是让学生反复练动词。前半动作换了领域，-ing 仍可表示过程。',
 'drill + -ing，双写 l。另有德语 Drilling 三联装枪的借词，以及布料用法，不把所有 drilling 都按英语正在钻解释。',D[:2]+[['drill + -ing → drilling','钻孔、钻探或操练过程']],
 'oil drilling 石油钻探，drilling equipment 钻探设备，repetitive drilling 反复操练。行业名词和动词进行形式在句子里的角色不同。',
 'oil drilling；drilling equipment；repetitive drilling。',
 'drilling 不必是地下开采，墙上打孔也可以；语言训练 drilling 也不要求学生在军事队列里活动。',
 ('The drilling noise stopped at noon.','钻孔声中午停了。'),('The lesson combines explanation with short periods of drilling.','这节课把讲解与短时反复操练结合起来。'))
W('driller','英 /ˈdrɪlə/；美 /ˈdrɪlər/','钻工、钻探人员；钻机操作者',
 '把钻孔、钻探交给负责操作的人，是 driller。行业里也可能是一项具体职位，不只是随手拿过一次电钻的人。',
 'drill + -er，双写 l，形成操作、从事钻探的人物名称。另有 drill 音乐的表演者口语用法，须由音乐语境识别。',D[:2]+[['drill + -er → driller','从事钻孔、钻探或操作钻机的人']],
 'an experienced driller 有经验的钻工，a well driller 钻井人员。具体职责由行业和岗位决定。',
 'an experienced driller；a well driller。',
 'drill 是工具或动作，driller 常是人；drill bit 才是钻头，不能用 driller 当所有钻具零件的名称。',
 ('The experienced driller checked the equipment.','有经验的钻工检查了设备。'),('A well driller examined the site before work began.','钻井人员在开工前查看了现场。'))
R('B3137','转动钻孔的动作、工具与反复操练；另辨同形借词','DRILL：钻孔与练熟都有固定用法，布料、动物另看来源','drill → drilling、driller。',
 '从工具主线学最常见用法，再把消防演习、发音操练等真实搭配接上；遇到布料或动物介绍则换到另一条来源。',
 '中古荷兰语 drillen 等 → 工具、动作、操练 drill；-ing、-er 前双写 l；布料等另有借词线。',
 [['动作、工具与练习','drill · drilling · driller']],
 'fire drill 是消防演习，drill bit 是钻头；drilling 不全是英语 -ing 词形。',
 'The driller paused the drilling while the workers attended a fire drill.\n\n工人参加消防演习时，钻工暂停了钻探。','drill drilling driller')
if __name__=='__main__':save('continuation_20261030_jw',ROOTS,WORDS)
