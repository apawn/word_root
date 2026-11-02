"""Fragments, fraying, quiet heat and repeated-action verb histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1697':dict(words=['splint','splinter','clot','clutter','banter','simmer','slumber'],label='旧词里的 -er 与不能硬拆的相似结尾',note='splinter 借自中古荷兰语，与 splint 同族，是碎片而非某类人。clutter、slumber 涉及旧动词反复材料；simmer 的早期拟声来源未定，banter 来源也不确定，不能把结尾都当人物后缀。'),
 'A1741':dict(words=['splinter','splintering','fray','fraying','simmer','simmering'],label='裂成碎片、磨损散线与情绪暗涌',note='splintering、fraying、simmering 都可以说正在发生的动作，也可修饰带有相应状态的事物；从物理过程到关系、情绪比喻要保留各自的画面。'),
 'A1760':dict(words=['fray','frayed','clutter','cluttered'],label='已经磨散与杂物堆满的状态',note='frayed 接磨损散线的 fray，不接争斗名词的另一词源；cluttered 接 clutter 堆得杂乱。'),
}
W('splint','/splɪnt/','夹板；细长的木片、金属条等',
 '先想一条细长而较硬的材料：可用于支撑，也能成为固定受伤部位的夹板。',
 '中古英语 splent、splint 等借自中古低地德语、荷兰语的薄条材料，与分裂、劈开词族相关。由薄条扩展到具有特定支撑用途的器具。',
 [['日耳曼语薄片、细条材料 → 中古英语 splint','劈出的细长材料、护甲薄条等'],['splint 的专门器具义','用于支撑、固定的夹板']],
 'a wooden splint 木夹板；a finger splint 手指夹板；an arm in a splint 用夹板固定着的手臂。',
 'a thin wooden splint；a splint for the wrist。','splint 常是作为材料或器具的细条、夹板；splinter 常是裂出来、可能扎人的细碎片。两词同族，现代用法不同。',
 ('His wrist was supported by a splint.','他的手腕用夹板支撑着。'),('The model was made from thin wooden splints.','模型是用细木条做的。'),sources=['https://www.etymonline.com/word/splint','https://en.wiktionary.org/wiki/splint#English'])
W('splinter','英 /ˈsplɪntə/；美 /ˈsplɪntər/','细碎片、木刺；裂成碎片、分裂',
 '木板裂开，蹦出一条尖尖的细片，就是 splinter。团队裂成几小块，也借这个画面说 splinter。',
 '名词经中古荷兰语 splinter 借入，与 splint 的薄片词族相连；英语再由名词发展出裂成细片、使分裂的动词。',
 [['中古荷兰语 splinter → 英语名词','劈裂后的细长碎片'],['名词 → 动词与群体比喻','裂碎；团队、组织分裂']],
 'a splinter of wood 一根木刺；a splinter in your finger 手指上的木刺；a splinter group 分裂出去的小团体。',
 'wood splinters；splinter into small groups。','splinter 的 -er 在这里不表示做事的人。shard 常说玻璃、陶器等硬物碎片，splinter 常突出细长、尖的碎片。',
 ('A splinter of wood caught in his sleeve.','一根木刺挂住了他的袖子。'),('The group splintered into several smaller factions.','这个团体分裂成了几个较小派别。'),sources=['https://www.etymonline.com/word/splinter','https://en.wiktionary.org/wiki/splinter#English'])
W('splintering','英 /ˈsplɪntərɪŋ/；美 /ˈsplɪntərɪŋ/','裂碎、分裂；splinter 的 -ing 形式',
 '材料正在一片片裂开，或一个原本完整的群体正在分成小块。强调裂开的过程和声音、局面。',
 'splinter 裂成碎片 + -ing；名词的碎片画面先进入动词，再形成动作名词、分词。',
 [['splinter 碎片名词 → 裂碎动词','整体分裂成细小部分'],['splinter + -ing','正在裂碎；分裂过程']],
 'the splintering of wood 木材裂碎；a splintering sound 裂碎声；the splintering of a movement 一场运动的分裂。',
 'the sound of splintering wood；splintering into factions。','splitting 泛指分开，splintering 更容易让人想到碎裂成好几个部分；比喻群体时也突出碎片化。',
 ('They heard the sound of splintering wood.','他们听见木头裂碎的声音。'),('The dispute led to the splintering of the group.','争端导致这个团体分裂。'))
W('fray','/freɪ/','磨损散线；使烦躁、关系受损；争斗〔名词，另一源〕',
 '绳头、衣边磨久了，一根根线松散出来；耐心、神经也会像这样被一点点磨坏。the fray 的争斗义另走一条来源。',
 '磨损动词经古法语 fraier、froiier 等接拉丁语 fricare 摩擦；争斗名词缩自 affray，与较早惊扰、骚动材料相连。',
 [['拉丁语 fricare → 法语相关词 → fray 动词','摩擦磨损 → 线头散开；情绪、关系受损'],['affray 缩短为 fray 名词','惊扰、骚动 → 争斗、激烈竞争']],
 'the rope is fraying 绳子正在散线；tempers begin to fray 人们开始失去耐心；enter the fray 加入争斗、竞争。',
 'fray at the edges；stay above the fray。','frayed nerves 接磨损、受刺激的比喻；enter the fray 接争斗名词。两支不能仅凭同形编成同一条历史。',
 ('The rope began to fray at one end.','绳子的一端开始散线。'),('As the delay grew longer, tempers began to fray.','随着延误越来越久，人们开始烦躁起来。'),('Another candidate entered the fray.','又一位候选人加入了角逐。'),sources=['https://www.etymonline.com/word/fray','https://en.wiktionary.org/wiki/fray#English'])
W('frayed','/freɪd/','边缘磨损散线的；紧张疲惫、烦躁的',
 '袖口已经磨出了毛边，耐心也已经被磨得所剩无几。frayed 同时描写物件和人的状态。',
 'fray 磨损散线 + -ed；由受摩擦后线头散开，转到神经、情绪、关系被消耗的比喻。',
 [['fray 磨损 + -ed','磨损后散线、起毛边的'],['frayed 的心理比喻','神经紧绷、耐心耗损的']],
 'frayed cuffs 磨破散线的袖口；frayed nerves 紧张烦躁的神经；frayed tempers 被耗尽的耐心。',
 'a frayed rope；soothe frayed nerves。','frayed 常突出被磨耗、拉扯后的状态；torn 是被撕破，可以是突然发生的。frayed nerves 则是固定比喻。',
 ('The jacket had frayed cuffs.','那件夹克的袖口已经磨出了毛边。'),('The long wait left everyone with frayed nerves.','漫长的等待让每个人都紧张烦躁。'))
W('fraying','/ˈfreɪɪŋ/','磨损散线、逐渐受损；fray 的 -ing 形式',
 '线头还在一根根松开，关系也可能还在一点点变坏。fraying 抓住这个持续变化的过程。',
 'fray + -ing，保留 y；取摩擦、磨损的动词分支。比喻用于耐心、关系、社会联系等逐渐受损。',
 [['fray 的磨耗、散线动作','材料逐渐失去原本完整边缘'],['fray + -ing 的持续及比喻用法','正在散线；关系、耐心逐渐受损']],
 'fraying fabric 正在散线的布料；fraying ties 逐渐受损的联系；patience is fraying 耐心正在消磨。',
 'a fraying friendship；fraying at the seams。','frayed 常看已经磨坏的状态，fraying 常看正在磨坏的过程；两者都可能作修饰语，语境决定时间侧重。',
 ('The fabric is fraying around the buttonhole.','扣眼周围的布料正在散线。'),('The letters reveal a fraying friendship.','这些信件显示出一段逐渐受损的友谊。'))
W('simmer','英 /ˈsɪmə/；美 /ˈsɪmər/','小火慢煮、微沸；情绪暗涌、怒气未消',
 '锅里轻轻冒泡，热着但没有翻腾；怒气藏在表面下面，也像锅里一直有热度。',
 '由较早 simperen 等慢煮、轻响形式变化而来，可能有拟声成分，更远来源未定。轻微加热的画面后来用于情绪。',
 [['较早 simperen 等 → simmer','液体轻响、缓慢加热、微沸'],['simmer 的情绪与固定搭配','压着的怒气或紧张持续；simmer down 平静下来']],
 'simmer the soup 小火慢煮汤；simmer with anger 生着闷气；let it simmer 让它慢慢煮。具体时间由食谱决定。',
 'bring to a simmer；simmer down。','boil 常说明显沸腾；simmer 是轻微冒泡、温和持续加热。情绪 simmer 则突出热度压在表面下。',
 ('Leave the soup to simmer gently.','让汤用小火轻轻煮着。'),('He sat silently, simmering with anger.','他默默坐着，心里憋着怒气。'),sources=['https://www.etymonline.com/word/simmer','https://en.wiktionary.org/wiki/simmer#English'])
W('simmering','英 /ˈsɪmərɪŋ/；美 /ˈsɪmərɪŋ/','小火煮着的；暗中持续、酝酿着的',
 '表面可能平静，里面的热度却一直在。可以是慢煮的锅，也可以是迟迟没有消失的矛盾、怨气。',
 'simmer + -ing，形成分词、形容词。由持续微沸转到情绪和问题长期保持活跃的比喻。',
 [['simmer 轻微持续加热 + -ing','正在微沸、慢煮'],['simmering 的比喻状态','怨气、紧张、争执暗中持续']],
 'simmering soup 小火煮着的汤；simmering resentment 暗藏而持续的怨恨；a simmering dispute 酝酿不息的争端。',
 'simmering tensions；a simmering pot。','simmering 常表示尚未完全爆发的紧张；explosive 更强调有爆发力或容易爆发。暗中持续多久，要看上下文。',
 ('Steam rose from the simmering soup.','小火煮着的汤冒出蒸汽。'),('The meeting exposed simmering resentment within the team.','会议暴露出团队内一直暗藏的怨气。'))
W('clot','英 /klɒt/；美 /klɑːt/','凝块；凝结成块',
 '原来能流动或分散的东西，聚到一起成一团。现代最常遇到 blood clot 血凝块、血栓这样的搭配。',
 '古英语 clott 团块，经中古英语延续。团块名词后来专用于血液等凝块，也可作动词说凝结。',
 [['古英语 clott → 中古英语 clot','圆团、块状物'],['现代 clot 的凝块名词、动词','凝结成的一团；形成凝块']],
 'a blood clot 血凝块、血栓；blood clots 血液凝结；a clot of cream 一团凝结的奶油。这里说明词义与搭配。',
 'clot formation；form a clot。','clot 强调聚成或凝成一块；clutter 则联系堆成一团的旧词族，但现代常说杂物，不是血凝块的另一种叫法。',
 ('The diagram shows how blood forms a clot.','图解展示血液怎样形成凝块。'),('A small clot of cream floated on the surface.','表面浮着一小团凝结的奶油。'))
W('clutter','英 /ˈklʌtə/；美 /ˈklʌtər/','杂物、杂乱堆积；把……堆得杂乱',
 '桌上小东西越积越多，挡手又碍眼，这些杂乱堆着的东西是 clutter；动词则说它们把空间挤乱了。',
 '中古英语 cloteren 等有结成团块、堆积义，与 clot 团块及旧反复动作材料相连。后来集中说东西无序地挤在一起。',
 [['clot 团块词族 → cloteren 等旧动词','聚成团、堆上去'],['现代 clutter 名词、动词','杂乱堆积的物品；把地方弄得拥挤凌乱']],
 'clear the clutter 清理杂物；clutter the desk 把桌子堆乱；visual clutter 视觉上过多、杂乱的元素。名词通常不可数。',
 'clutter up a room；a desk full of clutter。','clutter 不要求东西是垃圾；有用的物品堆得太多太乱，也叫 clutter。litter 常指随处丢弃的垃圾。',
 ('Old papers cluttered the desk.','旧文件把桌子堆得乱七八糟。'),('She cleared the clutter from the hallway.','她清理了走廊里的杂物。'),sources=['https://www.etymonline.com/word/clutter','https://en.wiktionary.org/wiki/clutter#English'])
W('cluttered','英 /ˈklʌtəd/；美 /ˈklʌtərd/','堆满杂物的、杂乱拥挤的',
 '东西一件挨一件地挤满，空间显得乱、使用不方便。房间、桌面、网页都可以 cluttered。',
 'clutter 堆得杂乱 + -ed，由分词形成状态形容词；从实物堆积也扩展到界面、版面元素过多。',
 [['clutter 无序堆积 + -ed','已经被物品挤乱的'],['cluttered 的实物和视觉用法','杂乱、过于拥挤的']],
 'a cluttered desk 杂乱桌面；cluttered with papers 堆满纸张；a cluttered interface 元素过多、显得乱的界面。',
 'a cluttered room；a cluttered layout。','crowded 强调人或物很多、拥挤；cluttered 更突出不必要的堆积和凌乱，不只是数量大。',
 ('The desk was cluttered with papers and cups.','桌上堆满纸张和杯子，很凌乱。'),('The page looks cluttered because there are too many buttons.','按钮太多，让这个页面显得很乱。'))
W('banter','英 /ˈbæntə/；美 /ˈbæntər/','打趣、轻松斗嘴；互相开玩笑',
 '你逗我一句，我回你一句，气氛轻松、不把话当真。这种来回的玩笑、调侃，就是 banter。',
 '十七世纪英语已有动词，随后出现名词；更早来源不确定，有伦敦俚语背景的说法。现代不能据此虚构一个常用 bant 基础词。',
 [['较早英语 banter 动词','用玩笑话调侃'],['名词 banter 与现代用法','轻松诙谐的来回打趣、斗嘴']],
 'friendly banter 友善打趣；exchange banter 互相斗嘴；banter with colleagues 和同事说笑。名词通常不可数。',
 'lighthearted banter；playful banter。','banter 通常把交流看成轻松玩笑；insult 强调侮辱。某人称话为 banter，不代表听的人一定觉得好笑。',
 ('The two friends exchanged friendly banter.','两个朋友轻松地互相打趣。'),('They bantered with each other while preparing dinner.','他们一边准备晚餐，一边说笑。'),sources=['https://www.etymonline.com/word/banter','https://en.wiktionary.org/wiki/banter#English'])
W('slumber','英 /ˈslʌmbə/；美 /ˈslʌmbər/','睡眠、沉睡；睡着〔较文学〕',
 '比 sleep 更容易让人想到安静睡着、沉在梦里。日常还常在 slumber party 留宿聚会中遇到。',
 '中古英语 slumeren、slomberen 等与较早 slumen 打盹、古英语 sluma 相连，带旧动词反复动作材料。后来名词也表示睡眠。',
 [['较早 sluma、slumen → 中古英语相关动词','轻睡、打盹、反复浅睡'],['现代 slumber 名词、动词','睡眠、沉睡；比喻休眠、不活跃']],
 'fall into a deep slumber 沉沉入睡；awake from slumber 从睡梦中醒来；a slumber party 通常是孩子、青少年留宿的聚会。',
 'peaceful slumber；slumber peacefully。','sleep 是普通用词，slumber 多较文学、柔和。它的历史有浅睡背景，但现代 deep slumber 很自然，不应机械限制成只能浅睡。',
 ('The baby fell into a peaceful slumber.','婴儿安静地睡着了。'),('The children are having a slumber party on Friday.','孩子们星期五要办留宿聚会。'),sources=['https://www.etymonline.com/word/slumber','https://en.wiktionary.org/wiki/slumber#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tm',ROOTS,WORDS)
    extend_lessons()
