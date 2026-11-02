"""Rain and glad: concrete weather and the older brightness behind happiness."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
RA=[['古英语 reġn → 中古英语 reyn、rein → rain','雨；更远来源不确定'],['现代 rain','雨、下雨；大量落下或接连出现的比喻']]
def RAH(f,m):return RA+[[f,m]]
W('rain','/reɪn/','雨；下雨；大量落下、接连出现',
 '水滴从天上落下来；问题、礼物或拳头接连落下，也能借下雨形容。',
 '继承古英语 reġn，远源有不同假说，本文从可靠旧词形讲。名词 rain 常不可数，动词天气句用形式主语 it。',RA,
 'heavy rain 大雨，It’s raining. 正下雨，rain down on 大量落向；save for a rainy day 相关比喻见 rainy。',
 'heavy rain；in the rain；it is raining；rain down on。',
 'rain 下雨、雨，reign 统治、rein 缰绳许多口音同音，但词源不同。heavy rain 常规大雨，不照中文机械用 big rain。',
 ('Heavy rain delayed the match.','大雨耽误了比赛。'),('It began to rain just as we left.','我们刚离开就开始下雨了。'))
W('rainy','/ˈreɪni/','下雨的；多雨的',
 '一天正在下雨，或一季常下雨，都能 rainy；关注天气、气候的雨多。',
 'rain + -y，古英语 reġniġ 等同族形容词已存在。rainy day 还借指生活遇到难处、需要储备的时候。',RA[:1]+[['古英语 reġniġ → rainy','有雨、多雨；现代 rain + -y 对应']],
 'a rainy day 雨天，the rainy season 雨季，save for a rainy day 未雨绸缪、为困难时期留储备。',
 'a rainy day；the rainy season；save for a rainy day。',
 'rainy 性质多雨，raining 正在下雨；a rainy season 不要求那一季每一分钟都在 raining。',
 ('We spent the rainy afternoon reading indoors.','下雨的下午，我们在屋里读书。'),('The rainy season starts in May.','雨季五月开始。'))
W('rainbow','英 /ˈreɪnbəʊ/；美 /ˈreɪnboʊ/','彩虹；缤纷的一系列〔比喻〕',
 '天空弯出一道彩色弓；bow 在这里抓住弯弧的形状。',
 '古英语 reġnboga 等旧组合延续，现代 rain + bow 弓、弧。不是 bow /baʊ/ 鞠躬的那种读法。',RA[:1]+[['古英语 reġn + boga → rainbow','雨与弓弧组合的彩虹名称']],
 'a rainbow in the sky 天空彩虹，a rainbow of colours 缤纷色彩；名称不要求只有特定几条实际界线分明的色带。',
 'a rainbow in the sky；a rainbow of colours；a double rainbow。',
 'rainbow 的 bow 常读 /bəʊ/ 或 /boʊ/，和 bow tie 蝴蝶结同一弓形读法；鞠躬 bow 则 /baʊ/。',
 ('A rainbow appeared after the shower.','阵雨后出现了一道彩虹。'),('The market stalls displayed a rainbow of colours.','市场摊位上呈现出缤纷色彩。'))
W('rainforest','英 /ˈreɪnfɒrɪst/；美 /ˈreɪnfɔːrɪst/','雨林',
 '降水丰富，森林长期湿润茂密；名字看的是水分条件，不只某一个国家的树。',
 'rain + forest，仿译德语 Regenwald。现代雨林也包括温带类型，不等于只在热带、只在亚马孙。',RA+[['rain + forest；仿译德语 Regenwald → rainforest','降水丰富地区的森林类别']],
 'tropical rainforest 热带雨林，temperate rainforest 温带雨林，rainforest plants 雨林植物。',
 'tropical rainforest；temperate rainforest；rainforest plants。',
 'rainforest 是森林类型，rainy forest 可只是当天、当地多雨的森林描述；名称不由某一场雨临时决定。',
 ('The film explores life in a tropical rainforest.','影片探索热带雨林中的生命。'),('Temperate rainforests also grow in cooler regions.','较凉爽地区也会生长温带雨林。'))
W('raincoat','英 /ˈreɪnkəʊt/；美 /ˈreɪnkoʊt/','雨衣',
 '穿在身上挡雨的外衣；前部说明用途，后部说明衣物类别。',
 'rain + coat 外套。名字按防雨用途命名，不要求只能在下雨时穿。',RAH('rain + coat → raincoat','为挡雨设计的外衣'),
 'a waterproof raincoat 防水雨衣，put on a raincoat 穿上雨衣，a hooded raincoat 带帽雨衣。',
 'a waterproof raincoat；put on a raincoat；a hooded raincoat。',
 'raincoat 雨衣，overcoat 大衣着眼外层、保暖等；普通外套不一定有同样防雨用途。',
 ('Take a raincoat in case the weather changes.','带件雨衣，以防天气有变。'),('She hung her wet raincoat by the door.','她把湿雨衣挂在门边。'))
W('rainstorm','英 /ˈreɪnstɔːm/；美 /ˈreɪnstɔːrm/','暴风雨；强降雨风暴',
 '不只几滴小雨，而是一场有明显强度的雨天气过程，可能伴风等。',
 'rain + storm 风暴，组合突出以雨为主要特征的风暴。不能从词形保证一定有雷电。',RAH('rain + storm → rainstorm','以降雨为主要特征的风暴天气'),
 'a heavy rainstorm 强暴雨，be caught in a rainstorm 遇上暴风雨。',
 'a heavy rainstorm；be caught in a rainstorm；a sudden rainstorm。',
 'rainstorm 强雨过程，thunderstorm 明确突出雷暴；二者可同时发生，但不是完全同义。',
 ('A sudden rainstorm sent everyone running for shelter.','突如其来的暴风雨让大家跑去避雨。'),('The rainstorm lasted for two hours.','暴风雨持续了两小时。'))
W('rainmaker','英 /ˈreɪnmeɪkə/；美 /ˈreɪnmeɪkər/','求雨者；带来大量客户、业务或资金的人〔比喻〕',
 '旱地盼雨，公司盼业务；能把客户和收益带进来的人，就被比作带来雨水的人。',
 'rain + maker，旧用法指试图借仪式等带来雨的人，现代也用于催雨相关人或设备；商业比喻突出带来业务，不声称仪式实际必能控制天气。',RAH('rain + maker → rainmaker','试图造雨、求雨者；引申带来业务和资金的能人'),
 'the firm’s rainmaker 公司的业务能手，a rainmaker who attracts clients 能吸引客户的业务人物。',
 'the firm’s rainmaker；a successful rainmaker；a traditional rainmaker。',
 'rainmaker 商业里说客户、业务能力，weather forecaster 是预报天气的人；预报雨并不等于造雨。',
 ('She became the firm’s leading rainmaker by attracting major clients.','她通过吸引大客户，成了公司的头号业务能手。'),('The story describes a rainmaker performing a ritual.','故事描写了一位求雨者举行仪式。'))
R('B2791','雨与下雨；天气、用品、生态和业务比喻','RAIN：从天落下的水；组合告诉形态、场景或用途','rain → rainy；rainfall、rainwater、raindrop 既有共享；rainbow 弓形，raincoat 防护，rainstorm 强天气，rainforest 生态，rainmaker 最后讲比喻。',
 '更远来源不确定，不强接拉丁灌溉词。雨林不只热带，rainmaker 的仪式、技术、商业用法不混为一个因果事实。',
 'rain + -y/fall/water/drop/bow/coat/storm/forest/maker；rainforest 有德语仿译背景。',
 [['基本雨、多少和形态','rain · rainy · rainfall · rainwater · raindrop · rainbow'],['用品、强天气和生态','raincoat · rainstorm · rainforest'],['造雨与业务比喻','rainmaker']],
 'rain/reign/rein 同音不同源；rainy 不等于每刻 raining；rainbow 的 bow 弓形读法；rainforest 含温带类型。',
 'After the rainstorm, she took off her raincoat and saw a rainbow.\n\n暴风雨后，她脱下雨衣，看见了一道彩虹。',
 'rain rainy rainfall rainwater raindrop rainbow raincoat rainstorm rainforest rainmaker')
GL=[['古英语 glæd → 中古英语 glad → glad','明亮、欢快等相联旧义'],['现代 glad','高兴；庆幸；乐意、愿意']]
def G(f,m):return GL+[[f,m]]
W('glad','/ɡlæd/','高兴的；庆幸的；乐意的',
 '听到好消息，心一下亮起来；松一口气觉得幸好如此，也常说 glad。',
 '继承古英语 glæd，旧有明亮、欢快联系。今天常说对某件事高兴、庆幸，或愿意做某事。',GL,
 'glad to see you 很高兴见到你，glad that ... 很高兴、庆幸……，glad to help 乐意帮忙。',
 'glad to see；glad that；glad to help；glad about。',
 'glad 常放表语说感受，happy 用法更宽。生日祝语习惯 Happy birthday，不按同义词替换成 Glad birthday。',
 ('I’m glad you could come.','我很高兴你能来。'),('She was glad that the exam was over.','考试结束了，她感到庆幸、轻松。'))
W('gladly','/ˈɡlædli/','乐意地；欣然；高兴地',
 '不只是嘴上答应，心里也愿意做；常用来爽快接受、提供帮助。',
 'glad + -ly，古英语 glædlīce 等副词已存在。现代乐意义常强调自愿、欣然。',GL+[['古英语 glædlīce → gladly','高兴、欣然、自愿地']],
 'gladly help 乐意帮，gladly accept 欣然接受，would gladly do 很乐意做。',
 'gladly help；gladly accept；would gladly do。',
 'gladly 多有愿意、高兴的态度，quickly 只说速度；答应得快不保证心甘情愿。',
 ('I would gladly help if I had more time.','如果时间多一点，我很乐意帮忙。'),('She gladly accepted the invitation.','她欣然接受了邀请。'))
W('gladness','/ˈɡlædnəs/','喜悦；高兴的心情',
 '把心里那份明亮、开心拿出来作为一种感受说，语气往往比常见的 happiness 更偏书面。',
 'glad + -ness，性质、情绪名词。不是某一种具体礼物或让人开心的物品。',GL+[['glad + -ness → gladness','高兴、喜悦的状态']],
 'a feeling of gladness 喜悦感，with gladness 怀着喜悦。可见于文学、宗教或较抒情表达。',
 'a feeling of gladness；with gladness；a sense of gladness。',
 'gladness 喜悦情绪，gladden 使喜悦的动作；两词只差后部，句中角色不同。',
 ('A feeling of gladness came over her as she reached home.','到家时，一阵喜悦涌上她心头。'),('He welcomed the visitors with gladness.','他满怀喜悦地迎接访客。'))
W('gladden','/ˈɡlædən/','使高兴；使欣慰',
 '一件事把别人的心情点亮；较书面，常见 gladden someone’s heart 让人心里高兴。',
 'glad + -en，使变成 glad。双写 d 后接 -en，属于改变状态的动词。',GL+[['glad + -en → gladden','使高兴、使心里欣慰']],
 'gladden someone’s heart 让某人心里欣慰，be gladdened by 因……而高兴。',
 'gladden someone’s heart；be gladdened by；news that gladdens。',
 'gladden 使人高兴，glad 高兴状态；The news gladdened her 与 She was glad about the news 观察角度不同。',
 ('The children’s laughter gladdened her heart.','孩子们的笑声让她心里欣慰。'),('We were gladdened by the news of his safe return.','听说他平安归来，我们都很高兴。'))
R('B3428','明亮、欢快背景到高兴、庆幸和乐意','GLAD：心情亮起来，也可说幸好、我乐意','glad → gladly、gladness、gladden，按状态、方式态度、情绪名词、引发变化连读。',
 '旧明亮与欢快相联可帮助记忆，现代先熟悉 glad to、glad that。更书面的 gladness、gladden 用例说明语气。',
 'glad + -ly/-ness/-en；gladden 双写 d。',
 [['状态和乐意态度','glad · gladly'],['情绪及使人高兴','gladness · gladden']],
 'glad 常表语，Happy birthday 固定祝语不替换；gladly 自愿不只速度；gladden 动词不同于 gladness 名词。',
 'Glad to see them, she gladly opened the door, and their visit gladdened her heart.\n\n见到他们她很高兴，欣然开门，他们的到访让她心里欣慰。',
 'glad gladly gladness gladden')
if __name__=='__main__':save('continuation_20261030_bl',ROOTS,WORDS)
