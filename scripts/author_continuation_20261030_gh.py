"""Thick, thin and marked: dimensions, concentration, degree and visibility."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['古英语 þicce → 中古英语 thikke → thick','厚、密、稠'],['英语 thick','厚度大；密集；难流动，也可比喻理解迟钝']]
W('thick','/θɪk/','厚的；稠的、密的；迟钝的〔贬、口语〕',
 '两面隔得远是厚；单位空间挤得多是密；汤里东西多、水少，流得慢就是稠。英语把这些相近感觉放在 thick 里。',
 '古英语 þicce 经中古英语到 thick；旧字母 þ 对应今天 th。th-、-ick 不是这里可独立拼义的前后缀。',T,
 'a thick book 厚书，thick soup 浓汤，thick fog 浓雾，a thick accent 很重的口音；in the thick of 正处于最忙、最激烈的部分。',
 'a thick book；thick fog；thick soup；in the thick of。',
 'thick 说厚、稠、密，wide 常说宽；纸的厚度和纸面宽度不是同一方向。称人 thick 有冒犯意味。',
 ('The book is only two centimetres thick.','这本书只有两厘米厚。'),('A thick fog covered the valley.','浓雾笼罩了山谷。'))
W('thicken','/ˈθɪkən/','变厚、变稠、变密；使变厚、稠、密',
 '汤慢慢不那么好流了，雾渐渐把远处挡住了：都是从不那么 thick 走向更 thick。',
 '现代可对照 thick + -en 变得、使变得；中古英语已有形式，历史也可能有古北欧相关动词影响，不只是一条现代临时拼接。',T+[['中古英语 thickenen 等 → thicken','变厚、变稠；现代对应 thick + -en']],
 'The sauce thickens 酱汁变稠，thicken the sauce 使酱汁变稠；The plot thickens 是情节更复杂、更扑朔迷离了。',
 'thicken the sauce；the fog thickens；the plot thickens。',
 'thicken 可及物也可不及物：厨师 thicken the soup，汤自己 the soup thickens；不是所有句子都必须加 make。',
 ('The sauce thickened as it cooled.','酱汁冷却时变稠了。'),('The fog began to thicken after sunset.','日落后雾开始变浓。'))
W('thickness','/ˈθɪknəs/','厚度；浓稠、密集程度；一层厚料',
 '从“这块板很厚”转到“它究竟多厚”：把 thick 的性质拿出来量、拿出来谈。',
 'thick + -ness 的性质名词对应，古英语 þicnes 等旧形式已存在，后来延续为 thickness。',T[:1]+[['古英语 þicnes → thickness','厚、稠、密的性质；对应 thick + -ness']],
 'measure the thickness 测厚度，a thickness of five millimetres 五毫米厚，the thickness of the sauce 酱汁浓稠度。',
 'measure the thickness；a thickness of；the thickness of the sauce。',
 'thickness/width/depth 分别是厚度、宽度、深度；同一物体采用哪个方向量，要看说明，不可只说都是尺寸。',
 ('The two sheets differ in thickness.','这两张板的厚度不同。'),('The thickness of the sauce makes it cling to the pasta.','酱汁的浓稠度让它能裹住意大利面。'))
W('thickly','/ˈθɪkli/','厚厚地、浓密地；含混低沉地',
 '把黄油抹得厚，把树种得密；thickly 说明动作最后形成怎样的厚、密状态。说话时也可有声音含混、受阻的感觉。',
 'thick + -ly，中古英语已有相应副词。后缀变的是句中用法，厚、稠、密的具体意思还由对象决定。',T+[['thick + -ly → thickly','以厚、密等方式；声音含混地']],
 'thickly sliced 厚切的，thickly wooded 树木茂密的，spread thickly 厚厚涂开，speak thickly 声音含混地说。',
 'thickly sliced；thickly wooded；spread thickly。',
 'thickly sliced 厚切，thinly sliced 薄切；thickly 不表示把切片的数量切得更多。',
 ('She spread the butter thickly on the toast.','她在吐司上抹了厚厚的黄油。'),('The hills are thickly wooded.','山上树木茂密。'))
R('B2646','厚、密、稠；相应变化与程度','THICK：两面隔得厚，空间挤得密，汤汁浓得稠','thick → thicken 变厚、稠、密；thickness 量程度；thickly 说方式。',
 '把一块厚板、一片浓雾、一锅稠汤放在一起看。共同点是某个方向或单位里有很多东西，中文分别用了不同形容词。',
 'þicce → thick；thick + -en/-ness/-ly；thickness、thicken 也有相应旧词历史。',
 [['基本性质与变化','thick · thicken'],['程度与方式','thickness · thickly']],
 'thick/wide 厚与宽；thick soup 稠汤，thick fog 浓雾；the plot thickens 情况更复杂。',
 'The sauce will thicken, so check its thickness before serving.\n\n酱汁会变稠，上桌前先看看浓稠度。','thick thicken thickness thickly')
N=[['古英语 þynne → 中古英语 thinne → thin','薄、稀、细'],['英语 thin','厚度小、密度低；动词使变薄、变稀']]
W('thin','/θɪn/','薄的；瘦的、稀的；变稀、使变薄',
 '一张纸薄，是两面挨得近；头发稀，是同样地方剩下的发丝少；证据薄弱，是能支撑结论的东西少。',
 '古英语 þynne 延续而来，更远与伸展类材料有关：东西铺开可变薄。现代 thin 当整体，不按 th + in 拆成里面。',N,
 'thin paper 薄纸，thin hair 稀疏头发，thin evidence 薄弱证据；thin the seedlings 给幼苗间苗，thin out 逐渐变稀、减少。',
 'thin paper；thin hair；thin evidence；thin out。',
 'thin 人瘦可以是中性也可显得太瘦，slim 常带匀称、好看的评价；thin wall 薄墙不等于 narrow wall 窄墙。',
 ('The crowd began to thin after midnight.','午夜后人群开始稀疏。'),('The claim rests on very thin evidence.','这个主张依赖的证据很薄弱。'))
W('thinner','英 /ˈθɪnə/；美 /ˈθɪnər/','更薄、更瘦、更稀；稀释剂',
 '看到更薄的纸，是比较级；看到油漆旁的一罐 thinner，是把液体调稀的东西。两个 -er 执行的任务不同。',
 'thin 双写 n + -er：形容词比较级表示更薄；另一路由动词 thin 使稀 + -er 形成起作用的材料名，常指稀释剂。',N+[['thin + 比较级 -er → thinner','比原来更薄、瘦或稀'],['thin 动词 + -er → thinner','使另一材料变稀的物质']],
 'thinner paper 更薄的纸，paint thinner 油漆稀释剂。a thinner person 的 thinner 修饰人，a bottle of thinner 中则是物质名词。',
 'thinner paper；get thinner；paint thinner。',
 'thinner 与 thinner 拼写读音一样，但名词稀释剂不表示更瘦的人；thinness 才是薄、瘦等性质。',
 ('This paper is thinner than the card we used yesterday.','这张纸比昨天用的卡纸薄。'),('The label on the bottle reads paint thinner.','瓶子标签上写着油漆稀释剂。'))
W('thinly','/ˈθɪnli/','薄薄地、稀疏地；勉强掩饰地',
 '奶酪切得很薄，村庄散得很稀；秘密只盖一层薄布，轮廓仍看得见，就成了几乎掩不住的比喻。',
 'thin + -ly，历史有中古英语相应形式。薄、稀的物理程度进一步延伸到遮掩不充分。',N+[['thin + -ly → thinly','薄、稀疏地 → 掩饰很浅、容易看穿']],
 'thinly sliced 薄切的，thinly populated 人口稀疏的，thinly veiled anger 几乎掩饰不住的愤怒。',
 'thinly sliced；thinly populated；thinly veiled。',
 'thinly veiled 不是完全公开，但已经容易看出；openly angry 则直接说公开表现愤怒。',
 ('Slice the cucumber thinly.','把黄瓜切成薄片。'),('His reply contained a thinly veiled threat.','他的答复里藏着几乎没掩饰住的威胁。'))
W('thinness','/ˈθɪnnəs/','薄、瘦、稀疏；单薄、缺乏分量',
 '把纸有多薄、人有多瘦、论据有多单薄，当作一种性质来谈。词义跟着对象走，不只指体形。',
 'thin + -ness，古英语已有 þynnes 一类名词。现代拼写两处 n 相邻：词基末尾 n 与后缀开头 n 都保留。',N[:1]+[['古英语 þynnes → thinness','薄、稀等性质；现代对应 thin + -ness']],
 'the thinness of the paper 纸的薄，the thinness of the evidence 证据的单薄，extreme thinness 极瘦状态。',
 'the thinness of the paper；the thinness of the evidence。',
 'thinness 是状态，thinner 可是比较级或稀释剂；thinness 不自带赞美，不等于 slimness 常有的匀称感。',
 ('The thinness of the paper made it easy to tear.','纸很薄，因而容易撕破。'),('The reviewer criticized the thinness of the plot.','评论者批评了情节的单薄。'))
R('B2547','薄、细、瘦、稀；支撑少的比喻','THIN：厚度少一点，密度少一点，支撑也可能少一点','thin → thinner 比较级或稀释剂；thinly 方式；thinness 性质；ultrathin 极薄。',
 '薄纸、稀疏人群、单薄证据，靠不同对象选中文。thinner 的名词和比较级尤其要放进句子分清。',
 'þynne → thin；thin + -er 双写 n；thin + -ly/-ness；ultra- + thin。',
 [['基本性质、变化和比较','thin · thinner'],['方式与性质名词','thinly · thinness'],['强化程度','ultrathin']],
 'thin/thick 是薄稀与厚密；thinner 名词为稀释剂；thinly veiled 几乎掩不住。',
 'Thinly sliced cheese goes on the thinner pieces of bread.\n\n薄切奶酪放在那些更薄的面包片上。','thin thinner thinly thinness ultrathin')
W('markedly','英 /ˈmɑːkɪdli/；美 /ˈmɑːrkɪdli/','明显地、显著地',
 '差别大到一眼能看出来，不需要使劲找那一点变化；markedly better 就是明显好转。',
 'marked 显著、明显的 + -ly。这里 marked 的形容词支在派生副词中通常保留 /ɪd/，读 markedly /ˈmɑːkɪdli/。',
 [['mark 标记 → marked','被标记；显著、明显的'],['marked + -ly → markedly','明显地、显著地']],
 'markedly different 明显不同，markedly improved 显著改善，markedly lower 明显更低。',
 'markedly different；markedly improved；markedly lower。',
 'markedly 不是逐个打标记地；marked the page 中 marked 通常 /mɑːkt/，不要照搬那个过去式读音来漏掉副词中的音节。',
 ('The two neighborhoods are markedly different.','这两个街区有明显差别。'),('Her confidence improved markedly during the course.','课程期间，她的自信心显著增强。'))
W('unmarked','英 /ʌnˈmɑːkt/；美 /ʌnˈmɑːrkt/','无标记的、未注明的；没有明显痕迹的',
 '纸箱上没写名字，车上没喷警车标识，表面没有刮痕；都可按没有相应 mark 理解。',
 'un- 不、没有 + marked 带标记的。这里的 un- 否定状态，不是已经把某个标记主动擦掉的完整叙事。',
 [['mark → marked','标记 → 有标记的'],['un- + marked → unmarked','未标明、无明显痕迹']],
 'an unmarked box 未标记的箱子，an unmarked police car 无警车涂装的警车，an unmarked grave 无碑或未标明身份的坟墓。',
 'an unmarked box；an unmarked police car；an unmarked grave。',
 'unmarked 无标记，unremarkable 不引人注意、平常；无标记的东西仍可能很醒目。',
 ('The papers arrived in an unmarked envelope.','文件装在没有任何标记的信封里寄到了。'),('An unmarked police car waited across the street.','一辆没有警车标识的警车等在街对面。'))
R('B4349','有标记、明显；无标记和显著程度','MARKED：能被看出来的痕迹，也能是看得出的差别','marked → markedly 显著地；unmarked 没有标记。',
 'mark 能留下真实记号，也能让差别显眼。markedly 选显著这一支，unmarked 多回到身份、记号、表面痕迹。',
 'mark + -ed → marked；marked + -ly → markedly；un- + marked → unmarked。',
 [['基本状态与程度','marked · markedly'],['否定状态','unmarked']],
 'marked 动词过去式与 markedly 的 /ɪd/ 读音区别；unmarked 无标记不等于 unremarkable 平常。',
 'The marked and unmarked boxes were markedly different in size.\n\n有标记和没标记的箱子，大小明显不同。','marked markedly unmarked')
if __name__=='__main__':save('continuation_20261030_gh',ROOTS,WORDS)
