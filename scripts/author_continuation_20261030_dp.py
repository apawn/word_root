"""Storm imagery, military calque and the sheltered lee."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['古英语 storm → 中古英语 storm → storm','暴风雨、骚动、冲击等'],['现代 storm 的常用画面','猛烈天气 → 情绪、争议的激烈爆发；冲入、怒冲冲行动']]
def SH(f,m):return S[:1]+[[f,m]]
W('storm','英 /stɔːm/；美 /stɔːrm/','风暴、暴风雨；激烈爆发；猛冲、怒气冲冲地走',
 '风、雨猛烈涌过来；一堆批评、争议同时冲来，也像一场风暴。人 storm out 则带着怒气冲出去。',
 '继承古英语 storm，本来就有风暴、冲击、骚动等范围，经中古英语进入现代。现代天气与情绪可以用同一猛烈冲击形象联系，不说每个军事义都是昨天才从天气复制。',S,
 'a violent storm 猛烈风暴，a storm of protest 一阵强烈抗议，storm out 怒气冲冲离开，take by storm 使轰动、迅速征服关注，weather the storm 渡过难关。',
 'a storm of；storm out；take by storm；weather the storm。',
 'storm 是强烈风暴类表达，不等于所有雨都是 storm；storm out 比 walk out 多愤怒、猛烈行动的色彩。',
 ('A storm of criticism followed the announcement.','公告后涌来一阵强烈批评。'),('He stormed out of the room without a word.','他一句话没说，怒气冲冲地冲出房间。'))
W('stormy','英 /ˈstɔːmi/；美 /ˈstɔːrmi/','有风暴的；激烈动荡、争吵不断的',
 '天气里风雨翻腾；关系、会议中也像风浪一阵阵，难以平静。',
 '对应 storm + -y，中古英语已有 stormy、stormi 等，可能承接更早相应形容词。用现代结构识别有风暴特点，不把有推测的古英语形式写成确定引文。',SH('中古英语 stormy、stormi → stormy；对应 storm + -y','多风暴的；比喻动荡、争吵多的'),
 'stormy weather 风暴天气，a stormy relationship 波折争吵多的关系，a stormy meeting 激烈争吵的会议。',
 'stormy weather；a stormy relationship；a stormy meeting。',
 'stormy weather 与只是下雨不同；stormy relationship 可在谈争执、波折，并非宣称有人遭遇真实气象风暴。',
 ('The ship returned to port in stormy weather.','船在风暴天气中返港。'),('They had a stormy meeting about the budget.','他们就预算开了一场争论激烈的会议。'))
W('thunderstorm','英 /ˈθʌndəstɔːm/；美 /ˈθʌndərstɔːrm/','雷暴、雷雨',
 '风暴里有雷电，常也伴随雨；名字中 thunder 先抓雷声这一明显特点。',
 'thunder 雷 + storm 风暴，按伴随的天气现象合成，不是 thunder 加某个单独后缀。',SH('thunder + storm → thunderstorm','伴有雷电的风暴天气'),
 'a summer thunderstorm 夏季雷暴，a severe thunderstorm 强雷暴，after a thunderstorm 雷暴过后。',
 'a summer thunderstorm；a severe thunderstorm；after a thunderstorm。',
 'thunderstorm 强调雷电，不是所有 rainstorm 大雨都有雷；thunder 是声音，lightning 是闪电，二者名称不同。',
 ('A thunderstorm interrupted the outdoor concert.','一场雷暴打断了露天音乐会。'),('The air felt cooler after the thunderstorm.','雷暴过后，空气凉快了些。'))
W('sandstorm','英 /ˈsændstɔːm/；美 /ˈsændstɔːrm/','沙暴、沙尘暴',
 '风把大量沙尘扬起来、推着走，眼前视野被遮住；不是天上像下雨一样制造出新沙子。',
 'sand 沙 + storm 风暴，按被风带起的物质命名。日常与 dust storm 有重叠，专业描述可进一步分颗粒等条件。',SH('sand + storm → sandstorm','夹带大量沙的风暴'),
 'a desert sandstorm 沙漠沙暴，caught in a sandstorm 遭遇沙暴，a wall of sand during a sandstorm 沙暴中的沙墙。',
 'a desert sandstorm；caught in a sandstorm；during a sandstorm。',
 'sandstorm 不是 snowstorm 雪暴；dust storm 尘暴与沙暴日常近用，但技术描述不只看中文同译便认为完全相同。',
 ('A sandstorm reduced visibility on the road.','沙暴使道路能见度降低。'),('The travellers waited for the sandstorm to pass.','旅行者等沙暴过去。'))
W('stormtrooper','英 /ˈstɔːmtruːpə/；美 /ˈstɔːrmtruːpər/','突击队员；纳粹冲锋队员〔历史〕；科幻中的帝国士兵等',
 '军事旧用借猛冲、突击的形象命名人员；在《星球大战》等作品里，又会看到特定虚构士兵形象。不是追着风暴观察的气象人员。',
 '仿译德语 Sturmtruppen 等，材料对应 storm 突击 + trooper 兵员。不同历史组织、作品中的所指须靠语境，不把所有 stormtrooper 都当同一支现实军队。',SH('德语 Sturmtruppen 等仿译为 storm + trooper → stormtrooper','突击兵员；历史与虚构语境进一步专用'),
 'a stormtrooper in the film 电影里的帝国士兵，historical accounts of stormtroopers 关于突击、冲锋队员的历史叙述。',
 'a stormtrooper；stormtroopers in the film；a stormtrooper costume。',
 'stormtrooper 突击兵、特定历史或虚构士兵，storm chaser 追风暴者；词里的 storm 不每次都在说坏天气。',
 ('He wore a stormtrooper costume to the film event.','他穿着帝国士兵服装参加电影活动。'),('The historian distinguished the different uses of stormtrooper.','历史学者区分了 stormtrooper 在不同语境中的用法。'))
W('shitstorm','英 /ˈʃɪtstɔːm/；美 /ˈʃɪtstɔːrm/','大乱子、激烈的批评风波〔粗俗口语〕',
 '坏消息、争吵、指责一下子到处飞，让局面失控；前项粗话加强脏乱、难收拾的情绪，不是正常气象名。',
 'shit 粗俗的排泄物词 + storm 风暴，组合成对混乱、争议的强烈比喻。',SH('shit + storm → shitstorm','猛烈混乱、争议、批评的粗俗比喻'),
 'a political shitstorm 政治争议风波，a media shitstorm 媒体批评风暴。粗俗程度明显，正式文稿通常换 controversy、backlash 等更具体表达。',
 'a political shitstorm；a media shitstorm；trigger a shitstorm。',
 'shitstorm 强情绪、粗俗，controversy 争议、backlash 反弹较中性；不要把它当正式新闻天气预报词。',
 ('The presenter called the controversy a “shitstorm.”','主持人用粗话 shitstorm 来形容这场争议。'),('The editor replaced shitstorm with public backlash.','编辑把粗俗的 shitstorm 换成了公众反弹。'))
R('B2536','猛烈天气与事情涌来的风暴形象','STORM：一股强力涌来，能是天气，也能是怒气、争议','storm → stormy；thunderstorm、sandstorm、snowstorm 等按天气分；情绪、讨论中的风暴另组；stormtrooper 和 shitstorm 讲清语域。',
 '不是每个 storm 复合词都对应真实天气。stormtrooper 军事、虚构语境另辨；shitstorm 是粗俗表达。',
 '古英语 storm → storm；storm + -y；thunder/sand/snow/rain/wind + storm；德语军词仿译 stormtrooper；shit + storm。',
 [['基础和性质','storm · stormy'],['天气与水流','thunderstorm · sandstorm · snowstorm · rainstorm · windstorm · superstorm · stormwater'],['其他比喻和语域','firestorm · brainstorm · stormtrooper · shitstorm']],
 'stormy 关系非真的天气；thunderstorm 雷电、sandstorm 沙尘；stormtrooper 非追风暴者；shitstorm 粗俗。',
 'The stormy meeting caused a storm of criticism.\n\n那场激烈争吵的会议招来一阵批评风暴。','storm stormy thunderstorm sandstorm snowstorm rainstorm windstorm superstorm stormwater firestorm brainstorm stormtrooper shitstorm')
L=[['古英语 hlēo、hlēow → 中古英语 lee → lee','遮蔽、庇护 → 避风处、背风侧']]
W('lee','/liː/','背风处、避风的一侧',
 '风从那边吹来，墙、山或船挡在前面，你躲在它后方较避风的地方，这一侧就是 lee。',
 '继承古英语 hlēo、hlēow 遮蔽、庇护，经中古英语 lee 到现代。不是 free 少掉 f，也不是专为某个人名 Lee 造的方向词。',L+[['现代 lee','被物体遮住风的一侧']],
 'in the lee of a wall 在墙的背风处，the lee side 背风侧，shelter in the lee 在背风处避风。',
 'in the lee of；the lee side；shelter in the lee。',
 'lee 由当时风向决定，不是永远地理上的东边、西边；windward 迎风方向与它对看。',
 ('We sat in the lee of the wall.','我们坐在墙的背风处。'),('The boats sheltered on the lee side of the island.','船只躲在岛的背风一侧。'))
W('leeward','英 /ˈliːwəd/、美 /ˈliːwərd/；航海也见 /ˈluːəd/','背风的、向背风侧；背风方向',
 '从迎着风的那边转向风吹过去、较受遮挡的一侧；-ward 标方向，不是某种奖励。',
 'lee 背风处 + -ward 朝向，名词、形容词、副词用法都有。传统航海读音可压成近 loo-ard，认得两种读法。',L+[['lee + -ward → leeward','朝向背风侧；背风方向']],
 'the leeward side 背风侧，move leeward 向背风方向移动，to leeward 在背风方向。',
 'the leeward side；move leeward；to leeward。',
 'leeward 背风，windward 迎风；leeway 现代常活动余地，但旧航海侧漂词不能直接替 leeward 的方向形容词。',
 ('The village lies on the leeward side of the hill.','村庄位于山的背风侧。'),('The flag showed which side was leeward.','旗帜显示出哪一侧是背风方向。'))
R('B4340','遮蔽、背风方向与活动余地','LEE：挡风物后面那块较安稳的地方','lee → leeward；leeway 从航海侧向漂移等背景进入活动余地的现代常用义。',
 '方向取决于风怎么吹，不能把背风一律记成西侧。leeway 活动余地与 leeward 背风方向要区分。',
 '古英语 hlēo、hlēow → lee；lee + -ward → leeward；lee + way → leeway。',
 [['避风处与方向','lee · leeward'],['侧漂到余地','leeway']],
 'lee 背风处、leeward 背风的方向、leeway 可调整余地；背风与迎风由实时风向决定。',
 'We found shelter in the lee of the hill, on its leeward side.\n\n我们在山的背风一侧找到了避风处。','lee leeward leeway')
if __name__=='__main__':save('continuation_20261030_dp',ROOTS,WORDS)
