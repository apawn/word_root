"""Common participial adjectives with direction, spelling and pronunciation."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1760':dict(words=['embarrass','embarrassed','embarrassing','frustrate','frustrated','frustrating','fascinate','fascinated','fascinating','delight','delighted','bless','blessed'],label='受到影响的状态与造成感受的性质',note='embarrassed、frustrated、fascinated 等分词常说受到影响的一方，对应 -ing 形式常说造成影响的性质；这个作用方向不能硬简化成人用 ed、物用 ing。blessed 另有一、二音节读法。'),
 'A1741':dict(words=['embarrass','embarrassing','embarrassed','fascinate','fascinating','fascinated'],label='embarrassing 与 fascinating：引起感受的一方',note='-ing 可说正在发生的动作，也能形成性质形容词；和相应 -ed 状态并读，区分令人难堪、令人入迷与已经感到难堪、入迷。'),
 'B3427':dict(words=['trust','trusted'],label='trusted：别人愿意把事托付给它',note='trust 接北欧语可靠、信赖词族，trusted 是规则 -ed 形式；被信任、值得信赖及自己容易信人的三种角度需区分。'),
 'B2861':dict(words=['fit','fitted','fitting'],label='fitted：剪裁贴合、配套装配与过去动作',note='fit 双写 t 加 -ed，分词形容词说剪裁、安装好的性质；动词过去和分词 fitted、fit 有实际用法差异，不照搬某一地区的单一形式为全球规则。'),
}
W('embarrassed','/ɪmˈbærəst/','尴尬的、难堪的；被弄得不自在；embarrass 的过去式、过去分词',
 '当众叫错了名字，大家看过来，你一时不知道怎样接话。这种局促、难堪的感受就是 embarrassed。',
 'embarrass + -ed，末尾 /s/ 后读 /t/。embarrass 经法语 embarrasser，较早有妨碍、困住等义，更深罗曼语传入路径有不同解释；现代常说使人社交上窘迫。',
 [['法语 embarrasser → embarrass','妨碍、困住等 → 使局促难堪'],['embarrass + -ed → embarrassed','受到这种影响；感到难堪']],
 'feel embarrassed 感到尴尬；embarrassed about a mistake 为错误难堪；embarrassed to ask 不好意思开口问；an embarrassed smile 尴尬的笑。',
 'look embarrassed；be embarrassed by someone’s behaviour。','embarrassed 描写受到影响后的感受，embarrassing 描写造成尴尬的性质。人也可以很 embarrassing，只要他的言行让别人难堪。',
 ('I felt embarrassed when I forgot her name.','忘记她名字时，我觉得很尴尬。'),('He was too embarrassed to ask the question.','他不好意思开口问那个问题。'),sources=['https://www.merriam-webster.com/dictionary/embarrass','https://en.wiktionary.org/wiki/embarrassed#English'])
W('embarrassing','/ɪmˈbærəsɪŋ/','令人尴尬、难堪的；embarrass 的 -ing 形式',
 '同样一个口误，从当事人的感受看是 embarrassed，从这件事给人的影响看是 embarrassing。它把尴尬带给别人。',
 'embarrass 保留词尾加 -ing。继承妨碍、使局促的动词线，常作性质形容词说令人不自在，不一定表示动作此刻正在进行。',
 [['embarrass','使人局促、难堪'],['embarrass + -ing → embarrassing','正在使难堪；具有使人难堪的性质']],
 'an embarrassing mistake 尴尬的错误；an embarrassing question 令人难堪的问题；an embarrassing silence 尴尬的沉默；find something embarrassing 觉得某事让人尴尬。',
 'an embarrassing moment；an embarrassing situation。','I am embarrassing 在某些语境是我让人难堪；I am embarrassed 才是我感到难堪。词尾在改变感受从哪一方来。',
 ('It was an embarrassing mistake, but we corrected it quickly.','那是个令人尴尬的错误，但我们很快纠正了。'),('He can be very embarrassing in public.','他在公共场合有时很让旁人难堪。'),sources=['https://www.merriam-webster.com/dictionary/embarrass','https://en.wiktionary.org/wiki/embarrassing#English'])
W('frustrated','/frʌˈstreɪtɪd/；亦 /ˈfrʌstreɪtɪd/','受挫的、沮丧烦躁的；受到阻挠的；frustrate 的过去式、过去分词',
 '想做成一件事，却反复被卡住；越想推进越推进不了，心里有受挫和烦躁，这就是 frustrated 的常见感觉。',
 'frustrate 去词末 e 加 -ed，末尾读 /ɪd/。frustrate 接拉丁 frustrari 使落空、使徒劳，与 frustra 徒然相关；分词既可说人受挫，也可说尝试被挫败。',
 [['拉丁 frustra／frustrari → frustrate','徒然、落空 → 使不能如愿、阻挠'],['frustrate + -ed → frustrated','受阻、受挫；因此感到烦躁沮丧']],
 'frustrated with the situation 对处境感到受挫；frustrated by delays 因延误受挫；a frustrated attempt 被挫败的尝试；feel frustrated 感到沮丧烦躁。',
 'increasingly frustrated；a frustrated expression。','disappointed 常在期望落空后失望；frustrated 更容易有想推进却受阻的烦闷。frustrating 描写引起这种感受的事物或行为。',
 ('I felt frustrated after trying the same solution three times.','同一个办法试了三遍之后，我感到又受挫又烦躁。'),('The delays left everyone frustrated.','一再延误让所有人都感到挫败。'),sources=['https://www.etymonline.com/word/frustrate','https://en.wiktionary.org/wiki/frustrated#English'])
W('fascinated','/ˈfæsɪneɪtɪd/','入迷的、被深深吸引的；fascinate 的过去式、过去分词',
 '眼前的东西让你忍不住继续看，耳边的故事让你不想漏掉一句：你的注意力被牢牢吸住了。',
 'fascinate 去 e 加 -ed，末尾读 /ɪd/。较早接拉丁 fascinare 施魅、使着迷，词源更深不明；英语后来把像着了魔的吸引力转成日常使注意力入迷。',
 [['拉丁 fascinare → 法语、英语相关词','施魅、使着迷 → 吸引并留住注意力'],['fascinate + -ed → fascinated','被吸引、处于入迷状态']],
 'fascinated by a machine 被机器深深吸引；fascinated with a subject 对某主题入迷；fascinated to learn 很感兴趣地了解到。',
 'watch in fascinated silence；be absolutely fascinated。','fascinated 关注注意力被吸引，不保证赞同对象或觉得它漂亮。fascinating 则描写有吸引力、令人想继续了解的一方。',
 ('The children were fascinated by the old machine.','孩子们被那台老机器深深吸引。'),('She listened, fascinated, as he described the journey.','他讲述旅程时，她听得入了迷。'),sources=['https://www.etymonline.com/word/fascinate','https://en.wiktionary.org/wiki/fascinated#English'])
W('fascinating','/ˈfæsɪneɪtɪŋ/','引人入迷的、极有趣的；fascinate 的 -ing 形式',
 '它勾起你的好奇，越看越想知道后面怎样。这种能抓住注意力的性质，就是 fascinating。',
 'fascinate 去 e 加 -ing。从较早施魅、使着迷的词族发展为引起强烈兴趣的形容词；现代不要求真有魔法意味。',
 [['fascinate','使着迷、吸引注意力'],['fascinate 去 e + -ing → fascinating','正在吸引；具有引人入迷的性质']],
 'a fascinating story 引人入胜的故事；a fascinating question 极有趣的问题；a fascinating insight 很有启发、让人感兴趣的见解。',
 'find something fascinating；a fascinating subject。','fascinating 通常比普通 interesting 强，更突出留住注意力。a fascinating person 是一个引人入迷的人，证明 -ing 不只用来形容物。',
 ('The exhibition tells a fascinating story about the town.','展览讲述了小镇一段引人入胜的故事。'),('She is a fascinating person to talk to.','她是个聊起来很有意思的人。'),sources=['https://www.etymonline.com/word/fascinate','https://en.wiktionary.org/wiki/fascinating#English'])
W('delighted','/dɪˈlaɪtɪd/','很高兴的、欣喜的；delight 的过去式、过去分词',
 '等了很久的好消息终于来了，你忍不住高兴起来。delighted 通常比普通 pleased 更显欣喜。',
 'delight + -ed，/t/ 后结尾读 /ɪd/。delight 经法语 delit、delitier 接拉丁 delectare 使愉快、吸引；现代 gh 是受 light 等拼写影响后加入，来源不是光线词。',
 [['拉丁 delectare → 法语 delit 等 → delight','使愉快、满足；英语拼写后来受类推影响'],['delight + -ed → delighted','受到愉快影响；很高兴、欣喜']],
 'delighted to hear 很高兴听到；delighted with the result 对结果很满意；delighted that ... 因某事很高兴；absolutely delighted 欣喜极了。',
 'be delighted to help；a delighted smile。','delighted 说感到欣喜，delightful 说让人愉快。I was delighted；The evening was delightful，分别描述感受与带来感受的性质。',
 ('We were delighted to hear the good news.','听到好消息，我们非常高兴。'),('She was delighted with the finished drawing.','她对完成的画很满意。'),sources=['https://www.etymonline.com/word/delight','https://en.wiktionary.org/wiki/delighted#English'])
W('blessed','过去、分词常 /blest/；部分形容词用法常 /ˈblesɪd/','受祝福的；幸运拥有的；令人宽慰的〔加强语〕；bless 的过去式、过去分词',
 '把好意、祝福送到某人身上，是 bless；说自己幸运地拥有好邻居，也可用 be blessed with。生活里 a blessed relief 则像终于松了一口气。',
 'bless + -ed，规则分词常读 /blest/；祝福、神圣、强调等形容词用法另保留常见两音节 /ˈblesɪd/。bless 承接古英语 bletsian 祝圣、祈福等词，后来扩大到祝福与幸运拥有的表达。',
 [['古英语 bletsian → bless','祝圣、祝福；后来也说赐予好处'],['bless + -ed → blessed','受祝福、幸运拥有；读音随用法分化']],
 'be blessed with wonderful friends 幸运地拥有好朋友；a blessed place 受祝福、神圣的地方；a blessed relief 极大的宽慰；Blessed are ... 宗教、文学用法。',
 'blessed with good weather；a blessed silence。','过去动词如 blessed the meal 常为一音节 /blest/；a blessed relief 等强调性形容词常两音节。读音有传统和语境差异，不只按字母 ed 一刀切。',
 ('We are blessed with wonderful neighbours.','我们很幸运，有一群好邻居。'),('The quiet room was a blessed relief after the noisy journey.','喧闹的旅程之后，这间安静的房间真让人舒坦。'),sources=['https://www.etymonline.com/word/bless','https://en.wiktionary.org/wiki/blessed#English'])
W('trusted','/ˈtrʌstɪd/','受信任的、可靠的；trust 的过去式、过去分词',
 '别人愿意把重要事交到他手里，或者愿意把这个来源当作可靠依据，就是 trusted。重点是被人信赖的地位。',
 'trust + -ed，词末 /t/ 后加 /ɪd/。trust 接北欧语 traust 可靠、信任等材料；分词形容词描述已经受到信赖的人、来源、工具等。',
 [['北欧语信任、可靠材料 → trust','相信、托付'],['trust + -ed → trusted','曾信任；被信任、受信赖的']],
 'a trusted friend 可信赖的朋友；a trusted source 可靠来源；a trusted adviser 受信任的顾问；be trusted to do 被信任能做某事。',
 'a trusted colleague；trusted information。','trusted 是被信任，trusting 更偏自己愿意相信别人，trustworthy 说值得信任。一个人很 trusting，不保证所有人都把他看作 trusted。',
 ('She asked a trusted colleague to review the draft.','她请一位信任的同事审阅草稿。'),('The report relies on several trusted sources.','报告依据几个可靠来源。'),sources=['https://en.wiktionary.org/wiki/trusted#English','https://en.wiktionary.org/wiki/trust#English'])
W('fitted','/ˈfɪtɪd/','剪裁贴合的；嵌装配套的；安装好、适合了；fit 的过去式、过去分词之一',
 '衣服按身形贴合，柜子按房间尺寸装进去，都抓住对准尺寸、位置的 fit。fitted 看完成后的贴合、安装状态。',
 'fit 双写 t 加 -ed，末尾读 /ɪd/。适合、装配的 fit 在中古英语已有相应材料，更远来源不定；现代动词过去、分词 fitted 与 fit 都有使用，受义项、地区影响。',
 [['fit 的合适、装配动词线','与尺寸、用途、位置相配'],['fit + -ed → fitted','剪裁、安装后贴合；过去的装配、适合']],
 'a fitted shirt 贴身衬衫；a fitted kitchen 嵌装配套厨房；fitted cupboards 嵌装柜；be fitted with a device 装有某装置。',
 'a fitted sheet；a newly fitted door。','fitted 侧重剪裁、装配好的状态；fitting 作性质词常是适当、合宜的：a fitting tribute。fit 作过去式与 fitted 的选择有用法差异，不把一种形式一律判错。',
 ('She wore a fitted blue shirt.','她穿着一件贴身的蓝衬衫。'),('The flat has a modern fitted kitchen.','公寓有一间现代嵌装配套厨房。'),('The carpenter fitted a new door yesterday.','木匠昨天装了一扇新门。'),sources=['https://www.merriam-webster.com/dictionary/fit','https://en.wiktionary.org/wiki/fitted#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vg',ROOTS,WORDS)
 extend_lessons()
