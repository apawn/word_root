"""Show and shower are separate near-looking families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,name,meaning):return [[f'英语 {a}；{b}','并列的构词材料'],[f'{a} + {b} → {name}',meaning]]
SHOW=[['古英语 scēawian → 中古英语 schewen','看、察看、展示等'],['英语 show','使看见、展示；节目、展出等名词义']]
W('show','英 /ʃəʊ/；美 /ʃoʊ/','展示；说明；带路；节目；展览',
 '把原本对方看不见、不明白的东西，放到他眼前。',
 '接古英语 scēawian 一系，经中古英语 schewen 等形式延续。现代动词有使看见、表明等用法，名词也指表演、展览。',SHOW,
 'show me the photo 是给我看照片，show that 是结果表明，show someone to a seat 是领某人到座位。a TV show 是电视节目，a flower show 是花展。',
 'show someone something；show how；show up；on show；a TV show。',
 'show 常把结果、证据或动作展示出来，tell 主要靠话语告知。Show me how to do it 强调示范，不只是告诉名称。',
 ('Could you show me how this machine works?','你能示范一下这台机器怎么用吗？'),('The figures show a steady increase.','数字表明有稳定增长。'),('We went to a photography show.','我们去看了摄影展。'))
W('showing','英 /ˈʃəʊɪŋ/；美 /ˈʃoʊɪŋ/','放映；表现；展示；show 的 -ing 形式',
 '一部电影被放出来算一场放映，一个团队拿出的实际表现也能作为一次 showing。',
 'show + -ing，接古英语 scēawung 等相应名词形式，现代有放映场次、表现等独立名词义。',SHOW[:1]+[['古英语 scēawung／中古英语 showing 一系','察看、展示等动作名词'],['英语 showing','展示；电影场次；表现']],
 'the evening showing 是晚场放映，a strong showing 是出色表现。be showing a film 又可以是普通动词正在放片。',
 'a strong showing；a poor showing；the first showing；a film showing。',
 'showing 的表现义不只指舞台演员，候选人、运动队、产品销售也可有 strong showing。',
 ('We booked tickets for the late showing.','我们订了晚场放映的票。'),('The new team made a strong showing in the tournament.','新队在锦标赛上表现出色。'))
W('showcase','英 /ˈʃəʊkeɪs/；美 /ˈʃoʊkeɪs/','展示柜；展示平台；展示长处',
 '挑出最值得看的东西，放进能让人注意到的柜子或活动里。',
 'show（展示）+ case（柜、盒），实体展示柜扩展为展示机会或平台，又转为动词。',C('show','case','showcase','展柜；使才华、产品显眼的平台或动作'),
 'a showcase for new talent 是新人展示平台，showcase local art 是展示当地艺术。通常带精心选择、突出优点的意味。',
 'a showcase for；showcase talent；showcase new products。',
 'showcase 比普通 show 常更强调有意突出亮点，但并不保证被展示的东西就是同类最好。',
 ('The festival is a showcase for young musicians.','音乐节是年轻音乐人的展示平台。'),('The museum showcases local craftsmanship.','博物馆展示当地工艺。'))
W('showroom','英 /ˈʃəʊruːm/；美 /ˈʃoʊruːm/','商品展厅；样品陈列室',
 '想买之前，先到一个能看实物、样品、摆设效果的地方。',
 'show（展示）+ room（房间），按展示商品用途命名。',C('show','room','showroom','用于展示商品、样品的空间'),
 '常说汽车、家具、厨房设备展厅，不要求每件商品都能当场提走。作动词的零售术语也可说到店看货后去别处买，需看具体句法。',
 'a car showroom；a furniture showroom；visit a showroom。',
 'showroom 是展示空间，warehouse 是存储空间；两者可在同一建筑里，但功能不一样。',
 ('They visited the showroom to compare the sofas.','他们到展厅比较沙发。'),('The car looked different under the showroom lights.','车在展厅灯光下看起来不一样。'))
W('roadshow','英 /ˈrəʊdʃəʊ/；美 /ˈroʊdʃoʊ/','巡回展演；巡回推介活动',
 '活动不是固定在一处等观众，而是带着内容到不同地方见人。',
 'road（路途）+ show（展示、演出），组合强调巡回移动，可用于娱乐、产品推介、融资介绍等。',C('road','show','roadshow','到不同地点进行的展示、推介'),
 'a product roadshow 是巡回产品推介；an investment roadshow 是面向潜在投资方的巡回介绍。是否正式演出要看主题，不因 show 就一定有舞台戏。',
 'a national roadshow；take a roadshow to；a product roadshow。',
 'roadshow 是移动到多地的活动，showroom 通常是固定展厅；一个公司可两者都用。',
 ('The company took its new products on a roadshow.','公司带着新产品进行巡回推介。'),('The science roadshow visited six schools.','科学巡回展示活动走访了六所学校。'))
W('slideshow','英 /ˈslaɪdʃəʊ/；美 /ˈslaɪdʃoʊ/','幻灯片放映；图片轮播',
 '把一张张图或一页页内容排好，按顺序切换给观众看。',
 'slide（幻灯片）+ show（展示），由实体幻灯片放映扩到电子演示和图片轮播。',C('slide','show','slideshow','连续展示一组幻灯片或图片'),
 'a slideshow of holiday photos 是假期照片轮播；课堂 slideshow 可含文字和图表。不是所有 slideshow 都有现场演讲者。',
 'a photo slideshow；start a slideshow；a slideshow presentation。',
 'slideshow 是放映过程或组合展示，slide 是单页；screenplay 是影视剧本，不是演示文稿。',
 ('She made a slideshow of family photographs.','她把家庭照片做成幻灯片展示。'),('The slideshow included maps and short video clips.','幻灯片演示包括地图和短视频片段。'))
W('showy','英 /ˈʃəʊi/；美 /ˈʃoʊi/','显眼的；艳丽的；炫耀的',
 '颜色、动作或装饰故意很抢眼，让人一眼注意到。',
 'show（展示、炫示）+ -y，形成有显眼展示性质的形容词；不等于 show 的副词。',SHOW+[['show + -y → showy','抢眼、花哨、炫示的']],
 'showy flowers 可中性说艳丽花朵，a showy display 可批评卖弄。评价在对象和语境里，不是所有 showy 都贬义。',
 'showy flowers；a showy gesture；showy clothing。',
 'showy 强调外表显眼，effective 强调实际效果；一个设计可以很显眼却不好用。',
 ('The plant produces large, showy flowers.','这种植物开出大而艳丽的花。'),('She preferred a simple design to something showy.','她喜欢简单设计，不喜欢花哨的。'))
W('showman','英 /ˈʃəʊmən/；美 /ˈʃoʊmən/','演出经营者；善于吸引观众的人',
 '知道怎样摆出场面、抓住注意力，让观众愿意看下去。',
 'show（演出）+ man（人这一称呼材料），历史上可说展演经营者，后来也说善表演、造声势者。',C('show','man','showman','经营展演或懂得吸引观众的人'),
 'a born showman 是天生会掌控观众的人，可用于演员、主持或公众人物。是否真诚、有实质内容不能仅由会做场面判断。',
 'a natural showman；a great showman；a travelling showman。',
 'showman 关注展示和带动观众的能力，showrunner 是电视创作制作的负责角色，不是另一种写法。',
 ('The singer is a natural showman.','这位歌手天生善于调动观众。'),('A travelling showman brought the attraction to the village.','一位巡回展演经营者把这个节目带到村子。'))
W('showrunner','英 /ˈʃəʊrʌnə/；美 /ˈʃoʊrʌnər/','电视剧主创统筹；剧集运作负责人',
 '不仅写一集或导一场，而是把整部剧的创作方向与制作推进接起来。',
 'show（电视节目、剧集）+ runner（运营、推动某事的人），在电视制作中形成特定职位名称。',C('show','runner','showrunner','统筹剧集创作与运作的人'),
 '常由兼任编剧、执行制作等职责的人承担，具体权限随制作安排。不是每个制片人或每集导演都自动是 showrunner。',
 'the series showrunner；a new showrunner；showrunner responsibilities。',
 'runner 在片场也可指助理工作，但 showrunner 不是简单“在节目里跑腿的人”；整词已有特定行业义。',
 ('The showrunner explained the direction of the new season.','主创统筹解释了新一季的方向。'),('A new showrunner joined the series after its first season.','第一季后，一位新的主创统筹加入剧集。'))
W('showgirl','英 /ˈʃəʊɡɜːl/；美 /ˈʃoʊɡɜːrl/','歌舞表演女演员',
 '在大型歌舞或娱乐舞台上，以舞蹈、歌唱和造型参与演出。',
 'show（娱乐表演）+ girl（女性称呼），形成特定职业、表演角色名称，不只泛指所有从事演出的女孩。',C('show','girl','showgirl','特定歌舞娱乐表演中的女演员'),
 '常见歌舞秀、历史娱乐业叙述，可能强调华丽服装和群舞。称呼范围随时代、场所，不宜把每位女性演员都叫 showgirl。',
 'a Las Vegas showgirl；a former showgirl；showgirl costumes。',
 'actress 是更广的女演员，showgirl 多指特定歌舞秀角色；职业种类不能只用 show 的宽义包办。',
 ('The museum displays costumes worn by showgirls.','博物馆展示歌舞女演员穿过的服装。'),('She began her stage career as a showgirl.','她以歌舞秀女演员身份开始舞台生涯。'))
W('showpiece','/ˈʃəʊpiːs/〔英〕；/ˈʃoʊpiːs/〔美〕','展示精品；代表性展品；亮点项目',
 '从许多东西里挑一件最能展示水平、值得拿到前台的。',
 'show（展示）+ piece（作品、物件），组合强调用于展现优势、技巧的一件东西。',C('show','piece','showpiece','专为展示水平而突出的物件或项目'),
 'a museum showpiece 是重点展品，a city’s showpiece building 是门面建筑。音乐 showpiece 可展示演奏技巧，未必就是最深刻作品。',
 'a showpiece for；a showpiece building；a musical showpiece。',
 'showpiece 是拿来展示的代表物，masterpiece 是评价达到杰作水平；代表物不自动就是最高艺术成就。',
 ('The restored hall is the showpiece of the museum.','修复后的大厅是博物馆的一大亮点。'),('The piece was written as a showpiece for the violin.','这首作品是为展示小提琴技巧而写的。'))
W('showstopper','英 /ˈʃəʊstɒpə/；美 /ˈʃoʊstɑːpər/','惊艳的节目或事物；使项目无法继续的严重问题',
 '同样是让节目停下来：一种是好到观众掌声不停，另一种是出了问题无法继续。',
 'show + stopper，早期舞台用法说掌声强烈到暂停演出的节目；商业、技术中后来也用作严重阻断问题。保留两种相反评价，不只猜正负。',C('show','stopper','showstopper','令演出停顿的精彩节目；后来也指阻断项目的问题'),
 'a musical showstopper 是惊艳曲目；a release showstopper 是严重到阻止发布的问题。读到 no showstoppers 在项目语境多是没有致命阻碍，不是没有精彩表演。',
 'a real showstopper；a potential showstopper；a showstopper bug。',
 'showstopper 的褒贬由领域和搭配决定，不能看到 stopper 就一概翻成坏问题，也不能一律夸惊艳。',
 ('Her final song was a showstopper.','她最后一首歌惊艳全场。'),('The missing approval is a showstopper for the project.','缺少批准让项目无法继续。'),
 sources=['https://brians.wsu.edu/2016/05/31/show-stopper/','https://en.wiktionary.org/wiki/showstopper'])
W('showboat','英 /ˈʃəʊbəʊt/；美 /ˈʃoʊboʊt/','演出船；爱炫技的人；卖弄、出风头',
 '一艘船载着舞台沿河演出；后来把夸张抢镜的表演感用来形容爱出风头。',
 'show + boat，历史上指有戏剧等表演的河船；动词炫技、出风头义联系过于戏剧化的表演方式。',
 [['show + boat → 供演出的河船','把演出带到沿河地区的船'],['英语 showboat 的人物、动词比喻','炫技抢镜、卖弄自己']],
 'He was showboating 常批评不必要地炫技，体育里可说光顾吸引观众忘了稳妥完成。也可保留演出船的历史名词义。',
 'stop showboating；a natural showboat；a river showboat。',
 'showboat 比 showman 常更含卖弄、抢镜评价，showman 可以赞其调动观众能力；两者语气不固定等同。',
 ('The coach warned the player to stop showboating.','教练警告球员别再卖弄。'),('The exhibit tells the history of river showboats.','展览讲述沿河演出船的历史。'),
 sources=['https://www.etymonline.com/word/showboat','https://en.wiktionary.org/wiki/showboat'])
W('showground','英 /ˈʃəʊɡraʊnd/；美 /ˈʃoʊɡraʊnd/','展览场地；农业或大型活动场地',
 '演出或展览需要一大片地方，人、摊位、展示物都在这里聚集。',
 'show（展览、展演）+ ground（场地），按活动用途组合，常见复数 showgrounds。',C('show','ground','showground','供展览、展演等活动的场地'),
 '在英式等语境常涉及农业展、牲畜展及大型活动。场地平时也可另作使用，不保证每天都有 show。',
 'an agricultural showground；at the showground；the showgrounds。',
 'showground 是场地，showroom 多是室内商品展厅；规模和用途有别。',
 ('The agricultural fair was held at the showground.','农业展在展览场地举行。'),('Visitors parked near the entrance to the showgrounds.','访客把车停在展场入口附近。'))
R('B2977','展示；表明；节目与展览','SHOW：让别人看见，也让内容成一场展示','照片拿给人看是 show，事实把趋势显出来也是 show；节目则成为可看的整体。',
 'show 接古英语 scēawian 一系。showcase 突出长处，showroom 指展示空间，roadshow 带内容去不同地点，showstopper 在不同领域还能有惊艳和阻断两种评价。',
 'show／showed／shown 是常见动词变化。showing 的 -ing 可成为放映场次、表现名词。常见 shower“阵雨、淋浴”来自古英语 scūr，不是本页 show + -er 的后代；另在 shower 页精讲。',
 [['展示与表现','show · showing · showcase · showpiece'],['场地与传播','showroom · showground · roadshow · slideshow · showtime'],['人物和风格','showman · showrunner · showgirl · showy · showboat'],['重大反应与主次','showstopper · showdown · sideshow']],
 'showrunner 是剧集主创统筹，showman 是懂得吸引观众的人；showcase 是展示平台，showpiece 是展示精品；showstopper 可能夸惊艳，也可能说项目被阻断。',
 'The roadshow showcased new talent, and one young singer proved to be a real showstopper.\n\n巡回演出展示了新人，其中一名年轻歌手惊艳全场。',
 'show showing showcase showroom roadshow slideshow showy showman showrunner showgirl showpiece showstopper showboat showground showtime showdown sideshow')
ROOTS[-1]['exclude']['shower']='常用的阵雨、淋浴义来自古英语 scūr，与 show 的展示义近源不同；由 shower B3987 单独精讲。'

SHOWER=[['古英语 scūr → 中古英语 schour','阵雨、一阵降落的东西'],['英语 shower','阵雨；喷淋、淋浴；成阵出现或落下的东西']]
W('shower','英 /ˈʃaʊə/；美 /ˈʃaʊər/','阵雨；淋浴；一阵大量落下的东西；纷纷给予',
 '不是一条集中水柱，而是一阵细密水滴落下，浴室喷头也制造类似感觉。',
 '常用阵雨、淋浴义接古英语 scūr，经中古英语 schour 延续；不是 show“展示”加人物 -er。另有较少见 show-er 展示者，须分义和读音。',SHOWER,
 'a shower of rain 是阵雨，take a shower 是淋浴，a shower of sparks 是一阵火花，shower someone with praise 是大量赞扬某人。a baby shower 则是准父母收到礼物祝福的聚会。',
 'take a shower；a rain shower；a shower of；shower someone with。',
 'shower 的常见读音中有 /aʊ/，show 是 /əʊ/ 或 /oʊ/；不能用相同字母 show 判断它们同源同音。',
 ('We took shelter from a sudden shower.','我们躲避一阵突如其来的雨。'),('I will take a shower before dinner.','晚饭前我要洗个淋浴。'),('The team was showered with praise after the match.','比赛后，球队获得了大量赞扬。'))
W('showery','英 /ˈʃaʊəri/；美 /ˈʃaʊəri/','有阵雨的；时有阵雨的',
 '天气不是整天一直下，而是一阵下、一阵停，仍要留意随时来一场。',
 'shower（阵雨）+ -y，-y 形成具有某种天气特征的形容词，不接 show“展示”的一支。',SHOWER+[['shower + -y → showery','时有阵雨、具阵雨天气的']],
 'a showery day 是时有阵雨的一天，showery weather 是阵雨天气。词本身不说明具体雨量、时间和地点，那要看完整预报。',
 'showery weather；a showery afternoon；remain showery。',
 'showery 是阵雨性的，rainy 泛说多雨、下雨；阵雨是降水的某种时间分布，不等于一定很小。',
 ('It was a cool, showery afternoon.','那是个凉爽、时有阵雨的下午。'),('The forecast described the weekend as showery.','预报说周末时有阵雨。'))
W('showerhead','英 /ˈʃaʊəhed/；美 /ˈʃaʊərhed/','淋浴喷头',
 '水到了这一端，被许多孔分散成适合淋浴的水流。',
 'shower（淋浴）+ head（装置末端、头部），按部件在装置中的位置和用途命名。',C('shower','head','showerhead','淋浴系统出水的喷头'),
 '可固定在墙上，也可为手持喷头；a showerhead 说部件，不指整个浴室或完整淋浴间。',
 'a handheld showerhead；replace a showerhead；water from the showerhead。',
 'showerhead 是喷头，shower curtain 是浴帘，shower enclosure 是淋浴围隔；共享 shower 仍要看后半具体物件。',
 ('The plumber replaced the old showerhead.','水管工换掉了旧淋浴喷头。'),('The hotel room had a large overhead showerhead.','酒店房间配有一个大顶喷。'))
R('B3987','阵雨；淋浴；成阵落下','SHOWER：一阵水滴散落，也延伸到大量给予','天上雨滴成阵落下，浴室喷头也让水散成一阵阵细流。',
 '常见 shower 接古英语 scūr“阵雨”，与 show“展示”的近源不同。showery 形容阵雨天气，showerhead 是淋浴喷头；a shower of praise 等又把成阵的画面用于赞扬。',
 'show 的常见元音是 /əʊ/ 或 /oʊ/，shower 的是 /aʊ/；相同字母并不保证相同词根。showerhead 的 head 是装置末端，showery 的 -y 是性质形容词。',
 [['阵雨与天气','shower · showery'],['淋浴与器具','shower · showerhead'],['大量落下、给予','a shower of · shower someone with']],
 'shower 不是常用 show + -er 展示者的意思；showery 说阵雨，showy 说花哨显眼。',
 'After walking home in showery weather, I took a warm shower.\n\n在阵雨天气里走回家后，我洗了个温暖的淋浴。','shower showery showerhead')
if __name__=='__main__':save('continuation_20261028_o',ROOTS,WORDS)
