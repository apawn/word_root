"""Marks on paper, rough writing, smudges and light touches of colour."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C1288':dict(words='scribble scribbles scribbled scribbling'.split(),label='scribble：快速落笔、潦草写画',note='scribble 可联系中古英语 scriben 加旧细小反复尾，也有中世纪拉丁语 scribillare 来源分析；现代去不发音 e 再加完整词尾。'),
 'A2238':dict(words='scribble scribbles scribbled scribbling wriggle squirm squiggle squiggles squiggled squiggling'.split(),label='scribble 的旧尾与 squiggle 的可能混成',note='scribble 的细小反复形式有不同借入路线；squiggle 可能混合 squirm、wriggle，不能把每个 -gle 都当作同一套现代后缀。'),
 'B3607':dict(words='sketch sketches sketched sketching'.split(),label='sketch：先把轮廓留下',note='sketch 经荷兰语等接意大利 schizzo，更远有即兴、飞溅等不同来源分析；名词草图、简述较早，英语相应动词较晚。'),
 'A1760':dict(words='doodle doodles doodled doodling scribble scribbles scribbled scribbling scrawl scrawls scrawled scrawling sketch sketches sketched sketching squiggle squiggles squiggled squiggling smudge smudges smudged smudging smear smears smeared smearing dab dabs dabbed dabbing'.split(),label='涂画、潦草写字、勾草图、抹痕和点涂的变化',note='sketched 的 -ed 读 /t/，smudged 为 /dʒd/，其余本组过去词尾多读 /d/。dabbed 双写 b，其他形式按各自基础词变化。'),
}
DOODLE=[['较早 doodle、dudle 的闲混、琐事材料 → 近代涂画义','可能联系 dawdle，具体形成有疑问；旧称闲人不等于今天在骂画画的人'],['二十世纪随手涂画 → 小涂鸦、随手图案','手在纸上画，注意力可能还在听电话、想事情']]
W('doodle','/ˈduːdəl/','随手涂画；小涂鸦、随手画的图案',
 '听电话时手没闲着，在纸角画圈、画星星，是 doodle。重点是随手画，不一定为了完成一幅正式作品。',
 '现代随手涂画义较晚，可能接方言 doodle、dudle 的闲混、做琐事材料，也可能关联 dawdle。不能把 do 做加一个通用小尾就当完整词史。',DOODLE,
 'doodle in the margin 是在页边涂画，draw a doodle 是画一个小涂鸦；可以有好看的图案，也可以只是无意识线条。',
 'a quick doodle 随手一画；doodle during a call 打电话时随手画。',
 'doodle 侧重随意、常非主要任务，sketch 常有抓轮廓的目标；doodle 漂亮与否不由词本身决定。',
 ('I often doodle while I am on the phone.','我打电话时常随手涂画。'),('She added a little doodle beside her signature.','她在签名旁添了一个小涂鸦。'),sources=S('doodle','doodle'))
W('doodles','/ˈduːdəlz/','随手涂画〔第三人称单数〕；小涂鸦、随手图案〔复数〕',
 '一个人边听边在纸角画，动词用 doodles；笔记边缘一串小脸、小花，也叫 doodles。',
 'doodle + -s，/l/ 后读 /z/；动词三单与小图案名词复数同形，末尾 e 保留。',DOODLE+[['doodle + -s → doodles','他、她随手画；多个小涂鸦']],
 'doodles on a pad 是在纸垫上随手画，doodles in the notebook 是本子里的小图案；可用介词、主语看词性。',
 'absent-minded doodles 无意识的小涂鸦；doodles little faces 随手画小脸。',
 'doodles 可是随手图案，notes 侧重记下的信息；一页上能同时有学习笔记和小涂鸦。',
 ('He doodles little faces during long calls.','打长电话时，他会随手画些小脸。'),('The notebook margins were full of doodles.','笔记本页边画满了小涂鸦。'),sources=S('doodles','doodle'))
W('doodled','/ˈduːdəld/','随手涂画了；画了些小图案',
 '刚才一边听、一边在纸角画圈圈，是 doodled；动笔可以很自然，并非每次都在认真构图。',
 'doodle 去末尾 e + 完整 -ed → doodled，/l/ 后读 /d/；基础 oo 保留。',DOODLE+[['doodle 去 e + -ed → doodled','过去随手涂画']],
 'doodled on a scrap of paper 是在一小片纸上涂画，doodled a flower 是随手画朵花；可直接带所画图案。',
 'doodled in the margin 在页边画了；doodled while listening 边听边随手画。',
 'doodled 不自动说明没在听，有时人在听、手也在画；drawn 则是更中性的画过，不带这种随意伴随感。',
 ('She doodled flowers in the corner of the page.','她在页角随手画了些花。'),('I doodled on a scrap of paper while I waited.','等着时，我在一小片纸上随手涂画。'),sources=S('doodled','doodle'))
W('doodling','/ˈduːdəlɪŋ/','正在随手涂画；随手涂画这件事',
 '笔正随心走，在纸边画小圈、小图案，是 doodling；也可以把这种手上的轻松活动当成一个整体。',
 'doodle 去末尾 e + 完整 -ing → doodling；分词、动作名词同形，保留 /dəl/ 的发音基础。',DOODLE+[['doodle 去 e + -ing → doodling','随手画的过程、活动']],
 'doodling on a notepad 是正随手画，enjoy doodling 是喜欢涂画；不必最后交付一幅完整作品。',
 'a page of doodling 一页随手画的东西；keep doodling 继续随手画。',
 'doodling 与 sketching 都能落笔画线，前者常是随意玩画，后者更强调用少量线条抓住对象、想法的大体样子。',
 ('He was doodling in the margin while he listened.','他边听边在页边随手画。'),('She enjoys doodling little animals in her spare time.','她闲时喜欢随手画些小动物。'),sources=S('doodling','doodle'))
SCRIBBLE=[['拉丁 scribere 写的相关材料 → 中古英语 scriblen → scribble','可经中世纪 scribillare，或接中古英语 scriben 加旧细小反复尾'],['快速潦草写 → 随手乱线、潦草字迹名词','现代可以写实际信息，也可以只是笔划来划去']]
W('scribbles','/ˈskrɪbəlz/','潦草地写、乱画〔第三人称单数〕；潦草字迹、乱线〔复数〕',
 '手追不上想法，笔很快记下几个词，动词用 scribbles；纸上一团潦草字、乱线，也叫 scribbles。',
 'scribble + -s，/l/ 后读 /z/；动词三单与潦草字迹名词复数同形，基础联系拉丁写字词族。',SCRIBBLE+[['scribble + -s → scribbles','他、她潦草写；几团乱字、乱线']],
 'scribbles a note 是匆匆写便条，scribbles on the wall 是在墙上乱画；decode his scribbles 是辨认他的潦草字迹。',
 'scribbles down an address 匆匆记地址；pencil scribbles 铅笔乱线、潦草字。',
 'scribbles 可有要记住的信息，只是字快、潦草；doodles 常更像随手小图案，未必想写具体词句。',
 ('She scribbles a note before the train arrives.','火车到来前，她匆匆写了张便条。'),('I could not read his pencil scribbles.','我看不清他那些潦草的铅笔字。'),sources=S('scribbles','scribble'))
W('scribbled','/ˈskrɪbəld/','潦草写下、匆匆记下、乱画了',
 '刚才赶紧抓张纸，歪歪扭扭记下电话号，是 scribbled；重点像笔跑得快，没顾上写漂亮。',
 'scribble 去末尾 e + 完整 -ed → scribbled，/l/ 后读 /d/；原有双 b 保留。',SCRIBBLE+[['scribble 去 e + -ed → scribbled','过去快速潦草写画']],
 'scribbled down the number 是匆匆记下号码，scribbled a message 是潦草写条消息；on 后补写在哪里。',
 'scribbled on a receipt 在收据上匆匆写了；a scribbled note 潦草便条。',
 'scribbled 不等于内容没价值，可能只是记得匆忙；a carefully written note 才另外强调落笔工整、仔细。',
 ('He scribbled the address on the back of a receipt.','他在收据背面匆匆写下地址。'),('She scribbled a reminder before leaving.','离开前，她匆匆写了条提醒。'),sources=S('scribbled','scribble'))
W('scribbling','/ˈskrɪbəlɪŋ/','正在潦草写、乱画；匆匆书写、乱线',
 '笔正飞快地划，字没顾上排整齐，是 scribbling；孩子把纸涂成一团线，也可以用同一个动作名。',
 'scribble 去末尾 e + 完整 -ing → scribbling；保留 bb，动作分词与动作名词同形。',SCRIBBLE+[['scribble 去 e + -ing → scribbling','快速潦草写、随手乱线的过程']],
 'scribbling notes 是正匆匆记笔记，scribbling on a page 是在纸上乱画；could hear scribbling 可说能听见笔急写的声音。',
 'frantic scribbling 飞快写字；scribbling down ideas 匆匆记点子。',
 'scribbling 的线条可能组成字，也可能不成字；sketching 通常更有意抓一个可辨认的轮廓、结构。',
 ('Everyone was scribbling notes as she spoke.','她说话时，大家都在飞快记笔记。'),('The child sat scribbling on a large sheet of paper.','孩子坐着，在一大张纸上乱画。'),sources=S('scribbling','scribble'))
SCRAWL=[['十七世纪 scrawl 的潦草写画义','可能联系较早伸展手脚的 scrawlen，或由其他乱划词改形，来源未定'],['写得散乱 → 潦草字迹、潦草一行字','现代可用“字像没站齐”抓外观，不当作确定历史故事']]
W('scrawl','英 /skrɔːl/；美 /skrɔːl/','潦草地写、乱画；潦草字迹',
 '字大小不齐、歪着挤着，别人得费劲辨认，是 scrawl。像文字没站好队，摊散在纸上。',
 '十七世纪已有乱写义，早源未定；可能接中古英语 scrawlen 的伸展手脚材料，也有联系 scrabble 等分析。字像摊散只是学习图景。',SCRAWL,
 'scrawl a name 是潦草写名字，an untidy scrawl 是一团潦草字，in a scrawl 是用很乱的笔迹；常关注结果不好辨认。',
 'scrawl across a wall 在墙上乱写；a hurried scrawl 匆忙潦草的字。',
 'scribble 更常突出快速、随手写，scrawl 更常让人看到字很不整齐；同一张便条可以两者都适用。',
 ('Please write clearly instead of leaving an unreadable scrawl.','请写清楚些，别留下一团看不懂的潦草字。'),('He tried to scrawl his name on the tiny label.','他试着在小标签上潦草写下名字。'),sources=S('scrawl','scrawl'))
W('scrawls','英 /skrɔːlz/；美 /skrɔːlz/','潦草地写、乱画〔第三人称单数〕；潦草字迹、字行〔复数〕',
 '一个人写得七扭八歪，用 scrawls；几处难认的字，也能当几团、几行 scrawls 来看。',
 'scrawl + -s，/l/ 后读 /z/；动词三单与潦草字迹名词复数同形，基础 aw 保持原来音值。',SCRAWL+[['scrawl + -s → scrawls','他、她乱写；几处潦草笔迹']],
 'scrawls his name 是潦草写名字，scrawls across the page 可以是散在纸面的潦草字；看主语、冠词分开。',
 'scrawls a message 潦草写消息；faint scrawls 淡淡的乱字。',
 'scrawls 强调不工整，writes 只交代写；工整誊写是 writes clearly，而 scrawls 通常没有这种整齐感。',
 ('He scrawls his name at the bottom of the form.','他在表格底部潦草签下名字。'),('The notebook contained several unreadable scrawls.','本子里有几处看不懂的潦草字。'),sources=S('scrawls','scrawl'))
W('scrawled','英 /skrɔːld/；美 /skrɔːld/','潦草写下、乱画了；潦草写成的',
 '刚才在纸背胡乱写了几行，是 scrawled；a scrawled address 就是写得歪斜、让人得辨认的地址。',
 'scrawl + 完整 -ed，/l/ 后读 /d/；直接加词尾，基础 aw、l 保留。',SCRAWL+[['scrawl + -ed → scrawled','过去乱写；字迹已经潦草留下']],
 'scrawled on the envelope 是潦草写在信封上，scrawled across the wall 是在墙上乱写；可形容一条记录的外观。',
 'a scrawled signature 潦草签名；scrawled in pencil 用铅笔潦草写成。',
 'scrawled 常让人觉得笔迹不整，printed 在手写里可以说清楚地写印刷体；签名 scrawled 不等于信息一定错。',
 ('She scrawled her phone number on the envelope.','她在信封上潦草写下电话号码。'),('A warning was scrawled across the wall.','墙上被潦草写了一条警告。'),sources=S('scrawled','scrawl'))
W('scrawling','英 /ˈskrɔːlɪŋ/；美 /ˈskrɔːlɪŋ/','正在潦草写、乱画；潦草书写',
 '笔正一路乱走，把字歪斜地铺到纸上，是 scrawling；常让人担心别人一会儿读不出来。',
 'scrawl + 完整 -ing，直接加；分词可描述眼前书写，动作名词可说潦草写字这种方式。',SCRAWL+[['scrawl + -ing → scrawling','写得不工整的过程']],
 'scrawling a note 是正潦草写便条，scrawling on the desk 是在桌面乱写；写在哪、写什么能用介词和宾语补清。',
 'scrawling his name 潦草签名；messy scrawling 杂乱的书写。',
 'scrawling 与 scribbling 常重叠，但 scrawling 更突出外观歪乱；不能靠它自动推断作者是生气还是赶时间。',
 ('He was scrawling a note on the back of the leaflet.','他正在传单背面潦草写便条。'),('She caught him scrawling on the desk.','她撞见他在桌面上乱写。'),sources=S('scrawling','scrawl'))
SKETCH=[['意大利 schizzo → 荷兰语 schets、低地德语等 → sketch','更远有即兴词、飞溅词等不同分析，近源较清楚'],['草图、简述名词 → sketch 的简述、画轮廓动词','英语动词的简述义记录早于相应绘画义，不能一律按实体先来排序']]
W('sketches','/ˈsketʃɪz/','草图、速写、短文、短喜剧〔复数〕；勾草图、简述〔第三人称单数〕',
 '几笔留下桥的形状，是 sketches；几句话留下人物或事件大概，也像文字速写。舞台上短小的一段喜剧，也叫 a sketch。',
 'sketch + -es，/tʃ/ 后读 /ɪz/；名词复数和动词三单同形，英语名词早于相应动词。',SKETCH+[['sketch + -es → sketches','几幅草图、几个短表演；他、她勾大体轮廓']],
 'pencil sketches 是铅笔速写，comedy sketches 是短喜剧；sketches the plan 是简述方案，sketches the bridge 是勾桥的轮廓。',
 'rough sketches 粗略草图；sketches out an idea 勾出想法大致内容。',
 'sketches 主要抓整体，不自动表示画得差；finished paintings 更强调完成品，草图也可以画得很有功力。',
 ('She filled the book with pencil sketches of old buildings.','她在本子里画满了旧建筑的铅笔速写。'),('He sketches out the plan before discussing the details.','他先勾出方案大概，再讨论细节。'),sources=S('sketches','sketch'))
W('sketched','/sketʃt/','勾画了草图、轮廓；简述了',
 '刚才几笔画出房间大概，或几句话讲出计划主线，是 sketched。它先把骨架留下，细节可以以后再填。',
 'sketch + 完整 -ed，/tʃ/ 后读 /t/，结尾 /tʃt/；基础 tch 保留，整词不增 /ɪd/ 音节。',SKETCH+[['sketch + -ed → sketched','过去留下大体轮廓、主线']],
 'sketched a map 是粗画地图，sketched out a proposal 是概述提案；都常把详情留到后面。',
 'sketched in pencil 用铅笔勾过；a hastily sketched plan 匆忙勾出的方案。',
 'sketched out 关注框架，spelled out 更像把细节说清楚；先 sketched out the plan，之后才逐项解释也很自然。',
 ('He sketched a quick map on the back of the receipt.','他在收据背面迅速画了张简图。'),('She sketched out her proposal in a few sentences.','她用几句话概述了提案。'),sources=S('sketched','sketch'))
W('sketching','/ˈsketʃɪŋ/','正在画草图、速写、简述；速写活动',
 '笔正用少量线条抓住对象大体样子，是 sketching；嘴上或文字勾出想法主线，也能用这个词。',
 'sketch + 完整 -ing，直接加；名词活动和分词同形，tch 仍读 /tʃ/。',SKETCH+[['sketch + -ing → sketching','勾轮廓、讲大概的过程']],
 'sketching buildings 是给建筑画速写，sketching out ideas 是勾出想法；a sketching trip 是以速写为主的外出活动。',
 'practise sketching 练速写；sketching in a notebook 在本子里勾草图。',
 'sketching 常有抓形状、框架的方向，doodling 更能是随意画图案；两者不按谁更高明来分。',
 ('She spent the afternoon sketching by the river.','她整个下午都在河边画速写。'),('We started by sketching out the main stages of the project.','我们先勾出了项目的主要阶段。'),sources=S('sketching','sketch'))
SQUIGGLE=[['近代 squiggle 可能混合 squirm 与 wriggle','较早说像鳗鱼那样扭来扭去，不先从现代画线动作出发'],['扭曲动作 → 卷曲形状、弯曲线条名词','现代看纸上的线像小虫扭来扭去，形成不规则弯线']]
W('squiggle','/ˈskwɪɡəl/','弯弯曲曲的线、乱弯；画弯线、扭动',
 '签名末尾拖出的乱弯，纸上像小虫爬的波浪线，都是 squiggle。好像原本扭动的小东西，被笔留成了一条线。',
 '可能由 squirm 与 wriggle 混成，早期动词说扭动，后来名词说卷曲、弯线；现代乱画义不代表历史从纸笔开始。',SQUIGGLE,
 'draw a squiggle 是画一条乱弯，a squiggle under a word 是词下面的一条曲线；squiggle across the page 是在页上画弯线。',
 'a little squiggle 一个小乱弯；a red squiggle 一条红曲线。',
 'squiggle 重点是线的弯曲外形，doodle 可以是一整幅小图案；一个 doodle 里能包含许多 squiggles。',
 ('He added a squiggle below his signature.','他在签名下添了一条弯线。'),('She watched the child squiggle a line across the page.','她看着孩子在纸上画出一条歪歪扭扭的线。'),sources=S('squiggle','squiggle'))
W('squiggles','/ˈskwɪɡəlz/','弯曲乱线、卷曲〔复数〕；画弯线、扭动〔第三人称单数〕',
 '纸上几条像虫爬的小弯线，是 squiggles；一个人随手把线拐来绕去，动词三单也同形。',
 'squiggle + -s，/l/ 后读 /z/；弯线名词复数与画弯线等三单同形。',SQUIGGLE+[['squiggle + -s → squiggles','几条乱弯线；他、她画弯线']],
 'red squiggles 是几条红曲线，squiggles on the paper 是纸上乱线；孩子 squiggles a line 则是画线动作。',
 'a page of squiggles 一页乱弯线；small squiggles 小曲线。',
 'squiggles 未必能读成文字，letters 则是有约定形状的字母；陌生文字看着像 squiggles 只是观察者的感觉，不是它真无意义。',
 ('The child covered the page with colourful squiggles.','孩子在纸上画满了彩色的乱弯线。'),('He decorated the border with loops and squiggles.','他用圆环和弯线装饰边框。'),sources=S('squiggles','squiggle'))
W('squiggled','/ˈskwɪɡəld/','画了弯弯曲曲的线；扭动了',
 '刚才笔没走直线，而是弯弯绕绕拉过去，是 squiggled。像把扭动的小虫的路径留在纸上。',
 'squiggle 去末尾 e + 完整 -ed → squiggled，/l/ 后读 /d/；原有 gg 保留。',SQUIGGLE+[['squiggle 去 e + -ed → squiggled','过去画弯线、扭曲移动']],
 'squiggled a line 是画一条乱弯线，squiggled across the page 是弯弯地画过纸面；也能说身体扭动。',
 'squiggled a border 画出弯曲边框；squiggled around 绕来扭去。',
 'squiggled 关注线、动作弯绕，scrawled 更常关注字写得乱；画装饰花边能 squiggle，不必在写难认的字。',
 ('She squiggled a line beneath the title.','她在标题下画了一条弯线。'),('He squiggled a border around the drawing.','他在画周围画了一圈弯弯曲曲的边框。'),sources=S('squiggled','squiggle'))
W('squiggling','/ˈskwɪɡəlɪŋ/','正在画曲线、弯线；扭来扭去的',
 '笔正绕出一条不规则弯线，是 squiggling；小虫身体弯来扭去，也保留更早的动作画面。',
 'squiggle 去末尾 e + 完整 -ing → squiggling；gg 保留，分词描写弯绕的过程。',SQUIGGLE+[['squiggle 去 e + -ing → squiggling','画弯线或扭动的过程']],
 'squiggling lines 是正在画弯线或弯扭的线，squiggling across the page 是在页上弯弯绕绕地画。',
 'squiggling a pattern 画弯绕图案；squiggling around 扭来扭去。',
 'squiggling 的画面是弯绕，zigzagging 则更容易是一段直线再折向另一段；两者都是不直，却不总是同一种曲折。',
 ('The child was squiggling lines across the paper.','孩子正在纸上画弯弯曲曲的线。'),('She relaxed by squiggling patterns in her notebook.','她在本子里画些弯绕图案来放松。'),sources=S('squiggling','squiggle'))
SMUDGE=[['中古英语 smogen 等弄脏、抹黑材料 → smudge','更早来源不明，可比较德荷弄脏词形，但不能定为 smoke 的改造'],['污痕 → 擦开、抹糊线条；现代绘画也可有意抹柔','轮廓不再清楚，像手蹭过湿墨、炭粉或妆容']]
W('smudge','/smʌdʒ/','污痕、蹭痕；蹭脏、抹糊、晕开',
 '湿墨没干，手一蹭，字边散开成黑糊糊的一块，是 smudge。炭笔画里有意用手把阴影抹柔，也能用同一个动作。',
 '接较早 smogen 等弄脏、抹黑材料，更远来源未定；现代抹开、抹糊义后来发展。浓烟相关同形义的联系也有来源疑问。',SMUDGE,
 'a smudge of ink 是一块墨迹，smudge the writing 是把字蹭花；smudge the charcoal 是抹开炭粉形成柔边。',
 'a dirty smudge 一块污痕；smudge easily 容易蹭花。',
 'smudge 常让轮廓变糊、留下蹭痕，stain 更宽，可能是渗进材料的污渍；泼咖啡染色不一定需要来回抹。',
 ('There was a black smudge on the edge of the page.','页边有一块黑色蹭痕。'),('Be careful not to smudge the wet ink.','小心别把未干的墨迹蹭花。'),sources=S('smudge','smudge'))
W('smudges','/ˈsmʌdʒɪz/','污痕、蹭痕〔复数〕；蹭脏、抹糊、晕开〔第三人称单数〕',
 '纸上几块指头蹭出的灰黑痕，是 smudges；一种墨水一碰就花，动词也可说 it smudges。',
 'smudge + -s，基础末尾已有 e，直接加 s；/dʒ/ 后读 /ɪz/，名词复数与动词三单同形。',SMUDGE+[['smudge + -s → smudges','几块蹭痕；它蹭花、晕开']],
 'finger smudges 是指头留下的蹭痕，ink smudges easily 是墨迹容易蹭花；不同句型分别指结果、发生动作。',
 'smudges on the glass 玻璃上的蹭痕；smudges the outline 把轮廓抹糊。',
 'smudges 常是不清晰的一块、一道痕，dots 可以是清楚的小点；污痕不一定长得像圆点。',
 ('The glass was covered in finger smudges.','玻璃上满是手指留下的蹭痕。'),('This ink smudges if you touch it too soon.','这种墨迹没等干就碰，会蹭花。'),sources=S('smudges','smudge'))
W('smudged','/smʌdʒd/','蹭脏、抹花、晕开了；带蹭痕、模糊的',
 '刚才手碰到湿墨，字变成模糊一团，是 smudged；妆、炭笔线条也能被抹得没那么清楚。',
 'smudge 去末尾 e + 完整 -ed → smudged，/dʒ/ 后读 /d/，结尾 /dʒd/，不增 /ɪd/ 音节。',SMUDGE+[['smudge 去 e + -ed → smudged','过去留下蹭痕；轮廓已抹糊']],
 'smudged ink 是被蹭花的墨，smudged makeup 是晕开的妆；smudged the charcoal 是抹柔炭笔痕，也可有意做。',
 'a smudged signature 蹭花的签名；smudged around the edges 边缘被抹糊。',
 'smudged 常失去清晰边缘，faded 是颜色变淡；字可以颜色很深却蹭糊，也可边缘清楚却年久褪色。',
 ('The address was smudged and hard to read.','地址被蹭花了，很难辨认。'),('She smudged the charcoal with her thumb to soften the shadow.','她用拇指抹开炭粉，让阴影柔和些。'),sources=S('smudged','smudge'))
W('smudging','/ˈsmʌdʒɪŋ/','正在蹭脏、抹花、晕开；抹柔、擦开的手法',
 '手指正让线、色块散开，变成没那么利落的边，是 smudging；可以是弄花字迹，也可以是画阴影时有意揉开。',
 'smudge 去末尾 e + 完整 -ing → smudging；g 在 i 前仍读 /dʒ/，分词和动作名词同形。',SMUDGE+[['smudge 去 e + -ing → smudging','留下蹭痕、擦开轮廓的过程']],
 'smudging the ink 是正蹭花墨迹，smudging charcoal 是抹开炭笔粉；prevent smudging 是防止蹭花。',
 'smudging around the eyes 眼周妆晕开；a smudging technique 抹柔边缘的手法。',
 'smudging 可故意也可无意，ruining 是把东西毁坏的评价；画家有意抹柔线条，不等于毁画。',
 ('He was smudging the pencil lines with his sleeve.','他的袖子正把铅笔线蹭花。'),('She used smudging to create a softer shadow.','她用抹柔的手法，让阴影更柔和。'),sources=S('smudging','smudge'))
SMEAR=[['古英语 smerian 的涂油与 smeoru 的油脂材料 → smear','动词抹涂、旧名词油脂各有历史，不都从现代污痕名词出发'],['涂抹、拖出污痕 → 给名声抹黑','现代像把不干净的东西摊到表面，也借给恶意损害声誉']]
W('smear','英 /smɪə/；美 /smɪr/','涂抹、抹开、蹭糊；抹黑、污蔑；一道污痕、抹黑言论',
 '把软膏、巧克力从一点抹成一片，是 smear；玻璃上拖出一道油痕也是 smear。抹黑别人名声，像把脏东西抹到对方身上。',
 '接古英语 smerian 涂油等动词及 smeoru 油脂名词材料；现代污痕名词与声誉攻击义后来发展，旧油脂名词并非由现代动词临时造出。',SMEAR,
 'smear butter on bread 是把黄油抹上面包，a greasy smear 是一道油痕；smear someone\'s name 是抹黑名声，a smear campaign 是抹黑攻势。',
 'smear across the glass 在玻璃上抹出痕；a smear of paint 一抹颜料。',
 'smear 更像把软黏物摊开、拖成痕，smudge 更常突出蹭糊、边界模糊；两者可描述同一次抹动的不同侧面。',
 ('There was a smear of chocolate on his cheek.','他脸颊上有一道巧克力痕。'),('They tried to smear her reputation with false claims.','他们试图用虚假说法抹黑她的名声。'),sources=S('smear','smear'))
W('smears','英 /smɪəz/；美 /smɪrz/','涂抹、蹭糊、抹黑〔第三人称单数〕；污痕、抹黑言论〔复数〕',
 '一个人把颜料抹成一道，是 smears；玻璃上的几道油痕，或针对名声散布的几条污蔑，也叫 smears。',
 'smear + -s，读 /z/；动词三单和污痕、声誉攻击名词复数同形，ear 的基础读音保留。',SMEAR+[['smear + -s → smears','他、她抹涂、抹黑；几道污痕或污蔑']],
 'smears paint on paper 是把颜料抹到纸上，smears on the window 是窗上污痕；political smears 是政治抹黑言论。',
 'greasy smears 油污痕；smears someone\'s name 抹黑某人名声。',
 'smears 作言论名词带攻击、败坏名声的评价，criticisms 是批评；有根据的不同意见不自动等于 smears。',
 ('The toddler smears paint across the paper.','小宝宝把颜料在纸上抹开。'),('She wiped the greasy smears from the window.','她擦掉窗上的一道道油污痕。'),sources=S('smears','smear'))
W('smeared','英 /smɪəd/；美 /smɪrd/','涂抹、抹开、蹭糊了；被污物抹着的；被抹黑的',
 '刚才手把湿颜料从一点拖成一片，是 smeared；某人的名声被恶意说法弄脏，也可说被 smeared。',
 'smear + 完整 -ed，读 /d/；基础 ear 后直接加，英式、美式基础元音加 r 的习惯不同。',SMEAR+[['smear + -ed → smeared','过去涂抹、拖糊；已经被抹黑']],
 'smeared with mud 是抹着泥，smeared across the page 是被抹过纸面；smeared her name 是抹黑她的名声。',
 'smeared makeup 被抹花的妆；smeared the paint 把颜料抹开了。',
 'smeared 常像一道拖开的痕，splashed 像液体溅出；同样让衣服脏，留下的形状和动作不同。',
 ('His hands were smeared with paint.','他的手上抹得到处是颜料。'),('The false story smeared her reputation.','那篇虚假故事抹黑了她的名声。'),sources=S('smeared','smear'))
W('smearing','英 /ˈsmɪərɪŋ/；美 /ˈsmɪrɪŋ/','正在涂抹、抹糊、抹黑；涂抹、污蔑行为',
 '软东西正从一点铺成一片，或手在表面拖出一道脏痕，是 smearing；恶意言论正在损害名声，也像在往人身上抹脏。',
 'smear + 完整 -ing，直接加；英式在元音词尾前也发 r，分词和动作名词同形。',SMEAR+[['smear + -ing → smearing','涂抹或损害名声的过程']],
 'smearing paint 是抹颜料，smearing the writing 是把字抹糊；smearing a rival 是恶意败坏对手的名声。',
 'smearing across the surface 在表面抹开；smearing someone\'s reputation 抹黑名声。',
 'smearing 不必永远负面：涂抹软膏可以是普通动作；说人名、reputation 时才进入声誉攻击义。',
 ('The child was smearing paint across the paper.','孩子正在纸上把颜料抹开。'),('The article was aimed at smearing her reputation.','那篇文章意在抹黑她的名声。'),sources=S('smearing','smear'))
DAB=[['中古英语 dabben 与 dab 的打击材料','更早来源不明，可能拟声；较早的动作、名词不都先是轻点'],['较轻接触 → 轻按、点涂；一小团软物','轻触纸巾、点一点颜料是现代直观画面；dab hand 能手的近源另有疑问']]
W('dab','/dæb/','轻按、轻点、点涂；一小团、一点；〔dab hand〕能手',
 '纸巾轻轻碰脸，不来回擦，是 dab；画笔蘸一点颜色点下去，也是 dab。一小团奶油、颜料就叫 a dab。',
 '较早 dabben 有打击义，更远来源未定；轻按、轻点义后来发展，也受 daub 相关用法影响。dab hand 能手的具体来源不确定。',DAB,
 'dab your eyes 是用纸巾轻按眼睛周围，dab paint on the paper 是点上颜料；a dab of cream 是一点奶油或膏体，看场景。',
 'a dab hand at cooking 做饭能手；dab gently 轻轻点按。',
 'dab 是点到一下、再抬开，rub 是接触着来回擦；擦一大块表面与轻点某处，动作轨迹不同。',
 ('She used a tissue to dab her cheeks dry.','她用纸巾轻按脸颊，吸干水分。'),('He added a dab of yellow paint.','他添了一小点黄色颜料。'),sources=S('dab','dab'))
W('dabs','/dæbz/','轻按、点涂〔第三人称单数〕；几点、一小团团〔复数〕',
 '一个人用画笔在纸上点一点，动词用 dabs；画上几小团颜色也叫 dabs，像把每次点触留下的量数出来。',
 'dab + -s，/b/ 后读 /z/；动词三单与小团、小点名词复数同形，原来的单 b 保留。',DAB+[['dab + -s → dabs','他、她点按；几小团、几点']],
 'dabs paint on the canvas 是在画布上点颜料，small dabs of cream 是几小团奶油；动作和留下的量相连。',
 'dabs at her eyes 用纸巾轻按眼周；dabs of blue 几点蓝色。',
 'dabs 强调点下来的局部小量，streaks 更像拖出长条；同一颜色落在纸上，点与条形状不同。',
 ('She dabs blue paint onto the paper.','她在纸上点上蓝色颜料。'),('The dessert was topped with small dabs of cream.','甜点上点缀着几小团奶油。'),sources=S('dabs','dab'))
W('dabbed','/dæbd/','轻按、点触、点涂了',
 '刚才纸巾轻轻碰几下，把水吸掉，或画笔点几下留下颜色，是 dabbed。动作像碰一下就抬开，不长距离拖。',
 'dab 双写 b + 完整 -ed → dabbed，/b/ 后读 /d/；短元音重读单音节按规则双写。',DAB+[['dab 双写 b + -ed → dabbed','过去轻按、点涂']],
 'dabbed her face with a towel 是用毛巾轻按脸，dabbed paint onto the canvas 是在画布上点颜料；with 后可说工具。',
 'dabbed gently 轻轻点按了；dabbed at the stain 轻按污渍。',
 'dabbed 关注点按动作，wiped 更常是布或手横着擦过去；同样擦干脸，接触轨迹不同。',
 ('She dabbed her face with a towel.','她用毛巾轻轻按了按脸。'),('He dabbed white paint onto the dark background.','他在深色背景上点上白色颜料。'),sources=S('dabbed','dab'))
W('dabbing','/ˈdæbɪŋ/','正在轻按、点触、点涂；点按手法',
 '画笔正一触一抬，留下一点点色块；纸巾正轻轻按水痕，都是 dabbing。核心是小范围接触，而非长长抹开。',
 'dab 双写 b + 完整 -ing → dabbing；双写不多发一遍 /b/，分词、动作名词同形。',DAB+[['dab 双写 b + -ing → dabbing','轻点、点按的过程或手法']],
 'dabbing paint 是点涂颜料，dabbing at tears 是轻按眼泪；a dabbing motion 是一触一抬的点按动作。',
 'dabbing with a tissue 用纸巾轻按；dabbing colour onto the paper 在纸上点颜色。',
 'dabbing 更像留下一个个点或小团，smearing 更像把软物拖开摊成痕；画一片阴影和点几朵小花，可以选不同动作。',
 ('She was dabbing at her tears with a tissue.','她正用纸巾轻按眼泪。'),('He created the flowers by dabbing paint onto the paper.','他把颜料一点点点在纸上，画出花朵。'),sources=S('dabbing','dab'))

def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfs',ROOTS,WORDS)
 extend_lessons()
