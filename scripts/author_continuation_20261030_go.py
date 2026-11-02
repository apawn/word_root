"""Tag and several common extensions: labels, consistency, defence and return."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['中古英语 tagge','衣物挂出的小片、垂饰；更早来源不确定'],['英语 tag','附着的小标签 → 身份标记、数字标签；贴标签']]
W('tag','/tæɡ/','标签、标记；贴标签、标注；捉人游戏〔另一支〕',
 '行李上挂一片写名字的小牌，照片旁也能挂一个可点击的名字；tag 就从实物标签伸进了数字世界。',
 '标签义接中古英语 tagge 挂出的小片，更早可能与北欧等材料相关。捉人游戏 tag 常另联系到 tig 触碰等词，来路有不确定性；不把全部义定成同一条标签派生。',T+[['另一路：tig 等触碰词 → 游戏 tag','捉人、轻触；具体路线不确定']],
 'a price tag 价签，a luggage tag 行李牌，tag someone in a photo 在照片里标出某人；play tag 玩捉人游戏，tag along 跟着一起去。',
 'a price tag；a luggage tag；tag someone in a photo；play tag；tag along。',
 'tag 数字标签不一定只指 # 话题，HTML tag、人员标记也是 tag；hashtag 是带 # 的具体一类。',
 ('Please leave the price tag on the gift.','请把礼物上的价签留着。'),('She tagged me in the group photo.','她在合照里标出了我。'),sources=['https://www.etymonline.com/word/tag'])
W('hashtag','/ˈhæʃtæɡ/','带 # 的话题标签；# 号〔相关语境〕',
 '给一条内容贴上 # 后跟关键词的标签，别人能沿标签找同主题内容；hash 指 #，tag 指标签。',
 'hash 符号名 + tag 标签，早期也写 hash tag。现代网络用法把符号和标签内容结合，不是 hash 食物肉末，也不等于密码散列值。',T+[['hash 符号 + tag → hashtag','# 开头的主题、元数据标签']],
 'add a hashtag 添加话题标签，a trending hashtag 热门话题标签，use the same hashtag 用同一话题标签。',
 'add a hashtag；a trending hashtag；use the same hashtag。',
 'hashtag 完整标签常包括 # 和后面的关键词；把 # 本身叫 hashtag 也有口语用法，但符号名 hash 与完整标签仍可区分。',
 ('Use the hashtag #CityWalk for photos from the event.','活动照片请使用 #CityWalk 这个话题标签。'),('The hashtag helped us find posts about the same topic.','这个话题标签帮我们找到了同主题帖子。'))
W('tagline','/ˈtæɡlaɪn/','广告语、品牌标语；结尾点题句',
 '一小句跟在品牌、电影或广告旁边，像标签一样让人记住它的主张；不是整篇广告正文。',
 'tag 附加、标记材料 + line 一行话，组合为附在后面的短句；常用义是广告、宣传中的标语。',T+[['tag + line → tagline','附带、点题的短句 → 宣传标语']],
 'a memorable tagline 令人记住的广告语，a movie tagline 电影宣传短句，the brand’s tagline 品牌标语。',
 'a memorable tagline；a movie tagline；a brand tagline。',
 'tagline 宣传短句，headline 标题，caption 图注；短不等于同一种功能，位置、用途要看内容。',
 ('The poster uses a short, memorable tagline.','海报用了一句简短好记的宣传语。'),('They changed the logo but kept the old tagline.','他们换了标志，却保留了原来的标语。'))
W('gamertag','英 /ˈɡeɪmətæɡ/；美 /ˈɡeɪmərtæɡ/','玩家代号、游戏用户名',
 '多人游戏里，别人不一定知道你的真名，先认屏幕上的那串名字；那就是你挂在游戏身份上的标签。',
 'gamer 玩家 + tag 身份标签。gamer 自己是 game + -er，-er 在前半段，不是整个 gamertag 的人物后缀。',T+[['game → gamer；gamer + tag → gamertag','玩家 → 标识玩家的代号']],
 'choose a gamertag 选择玩家代号，change your gamertag 更改游戏用户名，recognize a gamertag 认出玩家代号。',
 'choose a gamertag；change your gamertag。',
 'gamertag 是显示的玩家标识，不必是真名，也不等于登录密码；username 更泛。',
 ('She chose a gamertag that her friends could remember.','她选了一个朋友们记得住的玩家代号。'),('I recognized his gamertag before I heard his voice.','还没听到他的声音，我就认出了他的玩家代号。'))
W('tagger','英 /ˈtæɡə/；美 /ˈtæɡər/','标注者、标注工具；涂鸦签名者；捉人者',
 '谁在贴标记、什么工具在做标注，都可接 -er；墙上留下固定涂鸦签名的人也能这样称。游戏义则是在追着碰别人的人。',
 'tag 双写 g + -er，按 tag 的标签、涂鸦、游戏等义分别命名执行者。双写保留短元音构词习惯，不把 g 读成长音。',T+[['tag + -er → tagger','贴标签、标注或涂鸦的人或工具；游戏中的追捕者']],
 'a graffiti tagger 涂鸦签名者，a part-of-speech tagger 词性标注工具，the tagger in a game 捉人游戏中负责追的人。',
 'a graffiti tagger；a part-of-speech tagger；the tagger in a game。',
 'tagger 可是程序，不限人；tagline 是短句，不是做标记的人。具体含义先看 tag 做了哪种动作。',
 ('The program includes a part-of-speech tagger.','程序包含一个词性标注工具。'),('The tagger chased the other children across the playground.','负责捉人的孩子追着其他孩子跑过操场。'))
R('B3864','标签、身份与数字标注；游戏触碰义分支','TAG：挂一片身份记号，或者在数字世界贴个标记','tag → tagger；hashtag # 话题标签；gamertag 玩家代号；nametag 姓名牌；tagline 宣传短句。',
 '大部分扩展从附着小标签很容易看懂。捉人游戏的历史却需另联系触碰词，不能因为现代 tag 有多个义就强画成一条。',
 'tagge → tag 标签；tag + -er 双写 g；hash/gamer/name + tag；tag + line；游戏 tag 的触碰来源另看。',
 [['基本标签与标注者','tag · tagger'],['标签内容和使用场景','hashtag · gamertag · nametag'],['短句宣传','tagline']],
 'hashtag 是具体一类 tag；gamertag 不是密码；tagline/headline/caption 按宣传、标题、图注功能分。',
 'Her nametag and gamertag were different, but she used the same hashtag.\n\n她的姓名牌和玩家代号不同，但用了同一个话题标签。','tag tagger hashtag gamertag nametag tagline')
W('reliably','/rɪˈlaɪəbli/','可靠地、稳定可信地',
 '不是只碰巧成功一次，而是反复用都靠得住；reliably works 就是能稳定运行，不让人一直提心吊胆。',
 'reliable → reliably，-le 这类形容词形成 -ly 副词时，末尾 -le 对应 -ly；可理解为可靠的性质转成做事方式。',
 [['rely + -able → reliable','可以依靠的'],['reliable → reliably','以稳定、可信的方式']],
 'work reliably 稳定运行，reliably predict 可靠预测，reliably informed 由可信来源获悉。后一表达说消息来源可靠，仍应按具体证据判断。',
 'work reliably；reliably predict；reliably informed。',
 'reliably 说可靠程度，regularly 说规律、定期；定期开机不保证每次都能可靠运行。',
 ('The device works reliably even in cold weather.','这个设备即使在冷天也能稳定运行。'),('We cannot reliably predict the result from one example.','仅凭一个例子，我们无法可靠预测结果。'))
R('B3426','可以依靠、运行稳定；性质和方式','RELIABLE：反复交给它，仍然靠得住','reliable → reliability 可靠性 → reliably 可靠地；unreliable 否定可靠。',
 '人能守约、机器少掉链子、材料有可信依据，都能从可以依靠理解。性质名词和副词放在基本形容词后，别散开背。',
 'rely + -able，y 改 i → reliable；reliable → reliability/reliably；un- + reliable。',
 [['基本性质、程度与方式','reliable · reliability · reliably'],['否定可靠','unreliable']],
 'reliable/reliability 可靠的与可靠性；reliably/regularly 稳定可信与规律定期。',
 'A reliable system should work reliably, and its reliability should be tested.\n\n可靠系统应当稳定运行，可靠性也应经过检验。','reliable reliability reliably unreliable')
W('defenceman','英 /dɪˈfensmən/；美同音；美式常拼 defenseman','后卫〔尤冰球、长曲棍球〕',
 '球队里主要负责挡住对方进攻、保护本方得分区域的那个位置；这是具体运动的位置名称，不是所有帮助辩护的人。',
 'defence 防守 + man 人，复数 defencemen，尾部读 /mən/。defenseman 是美式拼写对应，不是另一个位置。',
 [['defence 防御、防守','与 defend 等同族'],['defence + man → defenceman','承担防守职责的球员；复数 defencemen']],
 'an ice hockey defenceman 冰球后卫，a veteran defenceman 经验丰富的后卫；具体站位、分工依运动而定。',
 'an ice hockey defenceman；a veteran defenceman；defencemen〔复数〕。',
 'defenceman 运动位置；defender 范围更宽，也可指辩护者、保护者。别把每个 defender 都改成 defenceman。',
 ('The defenceman blocked the shot.','后卫挡住了射门。'),('The team signed an experienced defenceman.','球队签下了一名经验丰富的后卫。'))
R('B3994','防御、防守；无防护与防守球员','DEFENCE：把对面的攻击挡在外面','defence → defenceless 无力自卫；defenceman 防守位置球员。',
 '这页沿英式拼写复习。-less 拿掉防护，-man 标出负责防守的人；同一个词基在社会、比赛中各选搭配。',
 'defens/defense → defence 拼写；defence + -less/man；defencemen 复数。',
 [['防守及缺少防护','defence · defenceless'],['运动中的防守者','defenceman']],
 'defence/defense 拼写差异；defenceman/defender 具体位置与更宽的保护、辩护角色。',
 'The defenceman strengthened the team’s defence.\n\n这名后卫加强了球队的防守。','defence defenceless defenceman')
W('reintroduction','英 /ˌriːɪntrəˈdʌkʃən/；美 /ˌriːɪntrəˈdʌkʃən/','重新引入、恢复推行；把物种重新引回原有地区',
 '以前有过，后来没有了，如今再带回来：政策可以重推，物种也可以回到原有分布区。',
 're- 再次 + introduction 引入。introduction 上接拉丁 intrōdūctiō 的 duct- 带领材料，长词不是随意把 introduce 字尾拼错。',
 [['拉丁 intrōdūctiō → introduction','带进、引入的动作或结果'],['re- + introduction → reintroduction','再次引入；恢复原有状态或分布']],
 'the reintroduction of a policy 重新推行政策，species reintroduction 物种重新引入，a reintroduction program 重引入计划。',
 'the reintroduction of；species reintroduction；a reintroduction program。',
 'reintroduction 物种义通常是回到原有地区；把从未在此存在的外来物种随便带来，不因此就叫重引入。',
 ('The proposal calls for the reintroduction of the old bus route.','提议要求恢复原来的公交线路。'),('The documentary follows a species reintroduction program.','纪录片跟踪了一项物种重新引入计划。'))
R('B4115','引入、介绍和再次带回','INTRODUCTION：把人、主题或事物带进来','introduction → reintroduction 再次引入、恢复。',
 '介绍人让彼此认识，引言把读者带进主题，引入设备把东西带进系统。re- 加上后，是同类动作再发生一次。',
 'intrō- 向里 + dūc- 带领 → intrōdūctiō → introduction；re- + introduction。',
 [['基本带入及再次带入','introduction · reintroduction']],
 'introduction 引言与 introduce 动词分用；reintroduction 不只是首次引进，物种语境尤其看原有分布。',
 'The introduction explains why the reintroduction of the route is being considered.\n\n引言解释了为什么正在考虑恢复这条线路。','introduction reintroduction')
if __name__=='__main__':save('continuation_20261030_go',ROOTS,WORDS)
