"""Tide, renew and shoe: useful historical and modern branches."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['古英语 tīd → 中古英语 tyde','时间、时节；与 time 有历史联系'],['按时往复的海水变化 → tide','潮汐；再比喻涌动的人群、趋势'],['旧时间义的另一支 → tidy','适时、合宜 → 状态妥当 → 整洁']]
W('tide','/taɪd/','潮、潮汐；涌动的趋势；帮助暂时渡过难关',
 '海水按周期涨落是 tide；一股舆论、人群、局势也像潮水一样涌来或转向。它更早说时间、时节，今天的海潮义是这条历史的一部分。',
 '古英语 tīd 经中古英语 tyde 传下。旧义包括时间、时节，后来集中发展海潮等用法；潮汐义形成过程中也有其他日耳曼语言影响的讨论。',T[:2],
 'high tide 高潮，low tide 低潮，turn the tide 扭转局势，a tide of criticism 一片批评声。tide someone over 帮某人暂时撑过缺口。',
 'high tide；low tide；turn the tide；tide someone over。',
 'tide 是潮汐或涌动的趋势，wave 是一波波的波浪。tide over 强调撑到下一阶段，不必是彻底解决困难。',
 ('The path disappears under water at high tide.','涨潮时，小路淹在水下。'),('This snack should tide us over until dinner.','这点零食应该能让我们撑到晚饭。'),sources=['https://en.wiktionary.org/wiki/tide#English','https://www.etymonline.com/word/tide'])
W('tidal','/ˈtaɪdəl/','潮汐的、受潮汐影响的',
 '海水的涨落会带动水位和水流变化；由这些变化形成、驱动、影响的东西，可以用 tidal 修饰。',
 '通常按 tide + -al 理解，接关系形容词后缀。历史上也有中世纪拉丁语相关构词的分析；学习时先抓与潮汐有关。',T[:2]+[['tide + -al → tidal','潮汐相关的性质、运动、能量']],
 'a tidal river 受潮汐影响的河段，tidal currents 潮流，tidal energy 潮汐能。潮流与海面波浪并非一回事。',
 'tidal currents；tidal energy；a tidal river。',
 'tidal wave 在日常表达中有时被拿来说海啸，但海啸通常不是潮汐造成。严谨区分时用 tsunami。',
 ('The lower part of the river is tidal.','这条河的下游受潮汐影响。'),('The model shows how tidal currents change direction.','模型展示潮流怎样改变方向。'))
W('tidy','/ˈtaɪdi/','整洁、井然有序的；整理；相当可观的〔金额等〕',
 '桌上各样东西放得妥妥当当，是 tidy。历史起点是适时、合宜，后来偏向状态妥当、整齐；不是海潮把房间冲干净。',
 '中古英语 tidy、tydy，由 tide 旧时间、时节义 + -y。适时、合宜等旧义，再发展状态良好、整洁等现代用法。',T[:1]+T[2:],
 'keep the room tidy 保持房间整洁，tidy up 整理一下，a tidy sum 一笔相当可观的钱。tidy 作动词直接说收拾。',
 'a tidy room；tidy up；a tidy sum。',
 'tidy 重点是有秩序、摆放整齐，clean 重点是干净。地板没灰却堆满东西，可以 clean 而不 tidy。',
 ('Please tidy your desk before you leave.','离开前请收拾一下书桌。'),('They sold the old camera for a tidy sum.','他们把旧相机卖了一笔可观的钱。'),sources=['https://en.wiktionary.org/wiki/tidy#English','https://www.etymonline.com/word/tidy'])
W('tidewater','英 /ˈtaɪdwɔːtə/；美 /ˈtaɪdwɔːtər/，也读 /ˈtaɪdwɑːtər/','受潮汐影响的水域；低平沿海地带',
 '沿海河口里的水会随海潮涨落，属于 tidewater；名称也能转指这类水域旁的低平沿海地区。',
 'tide 潮汐 + water 水。先抓潮汐影响的水，再看由水域转指沿岸地带的用法。',T[:2]+[['tide + water → tidewater','潮汐水域 → 相应低平沿海地带']],
 'tidewater marshes 潮汐沼泽，the tidewater region 沿海低地。大写 Tidewater 还可用于特定地区名称。',
 'tidewater marshes；a tidewater region。',
 'tidewater 的关键是潮汐影响，freshwater 的关键是淡水性质。河口混合水域不宜只凭一个名称判断全部盐度。',
 ('Birds gathered in the tidewater marshes.','鸟聚集在潮汐沼泽里。'),('The museum tells the history of the tidewater region.','博物馆讲述这片沿海低地的历史。'),sources=['https://en.wiktionary.org/wiki/tidewater#English','https://www.merriam-webster.com/dictionary/tidewater'])
W('tidily','/ˈtaɪdɪli/','整齐地、有条理地',
 '东西不仅放好了，还放得很整齐，tidily 说明整理、摆放等动作完成的方式。',
 'tidy + -ly，词尾 y 变 i。中古英语已有相应副词形式。',T[:1]+T[2:]+[['tidy + -ly → tidily','整洁的 → 整齐地']],
 'neatly and tidily 整整齐齐地，arranged tidily 摆得整齐。可说物件、书写或处理事情的方式。',
 'arranged tidily；folded tidily。',
 'tidy 是形容词或整理的动词，tidily 是副词：a tidy desk；arrange things tidily。',
 ('The towels were folded tidily on the shelf.','毛巾整齐地叠放在架子上。'),('She arranged the notes tidily in a folder.','她把笔记有条理地放进文件夹。'))
W('tidiness','/ˈtaɪdinəs/','整洁、有条理的状态',
 '桌上每件东西都有位置，房间看着井井有条；把这种状态作为一件事来谈，就用 tidiness。',
 'tidy + -ness，y 变 i。-ness 把形容词性质变成名词。',T[:1]+T[2:]+[['tidy + -ness → tidiness','整洁、有条理的状态']],
 'a sense of tidiness 整洁感，tidiness and cleanliness 整洁与清洁。可谈对整齐的要求、习惯。',
 'tidiness and cleanliness；a concern for tidiness。',
 'tidiness 是有条理、整齐；cleanliness 是清洁。两者常一起出现，侧重点仍不同。',
 ('Tidiness makes the small room feel more spacious.','整洁让小房间显得更宽敞。'),('They value both tidiness and cleanliness in the kitchen.','他们既重视厨房整齐，也重视清洁。'))
W('untidy','/ʌnˈtaɪdi/','不整洁、凌乱的',
 '东西东一件西一件，头发、字迹或安排也缺少条理，可以用 untidy。',
 'un- 不 + tidy 整洁的，否定整齐、有秩序的性质。',T[:1]+T[2:]+[['un- + tidy → untidy','整洁的反面：凌乱、缺少条理']],
 'an untidy room 凌乱房间，untidy handwriting 不工整字迹，look untidy 看起来邋遢、不整齐。',
 'an untidy room；untidy handwriting。',
 'untidy 不自动表示肮脏；也可以只是摆放乱、字写得不齐。',
 ('His desk was untidy but clean.','他的桌子很乱，但很干净。'),('The teacher struggled to read the untidy handwriting.','老师费劲地辨认那些不工整的字。'))
R('B2704','时间、时节的旧义，分成海潮与合宜、整洁的支线','TIDE：旧时说时节，现代常说按时往复的潮汐','tide → tidal、tidewater；旧时间义 → tidy → tidily、tidiness、untidy；riptide 看潮流。',
 'tidy 和海潮看起来很远，连接点藏在 tide 的旧时间义。先分清这条分叉，再记现代搭配。',
 'tīd 时间、时节 → tide；-al 相关，-y 旧义合宜；tide + water 水域、地区。',
 [['基础、性质与水域','tide · tidal · tidewater · riptide'],['旧时间义留下的支线','tidy · tidily · tidiness · untidy']],
 'tide 与 wave 不同；tidy 不等于 clean；tide someone over 强调暂时撑过去。',
 'We tidied the room, then walked to the coast to watch the tide.\n\n我们整理好房间，然后走到海边看潮水。','tide tidal tidewater riptide tidy tidily tidiness untidy')
N=[['re- 再 + new 新','使恢复、更新'],['renew → renewal、renewable','更新行动；能够续期、补充的性质']]
W('renewable','英 /rɪˈnjuːəbəl/；美 /rɪˈnuːəbəl/','可续期、可更新的；可再生的',
 '合同到期后还能续，是 renewable；能源来自自然中持续补充的来源，也叫 renewable。共同点是来源或有效期能够得到延续。',
 'renew 更新、续期 + -able 能够……的。合同、资源等语境各自固定了可续与可再生的用法。',N,
 'a renewable contract 可续期合同，renewable energy 可再生能源，renewable resources 可再生资源。renewables 也可概称可再生能源。',
 'a renewable contract；renewable energy；renewable resources。',
 'renewable 说明能够补充、更新，不表示任何地点、任何时刻都能无限供给；reusable 说同一件物品可反复使用。',
 ('The job comes with a renewable annual contract.','这份工作采用可续期的一年期合同。'),('The school project compares several sources of renewable energy.','学校项目比较几种可再生能源来源。'),sources=['https://en.wiktionary.org/wiki/renewable#English','https://www.eia.gov/energyexplained/renewable-sources/'])
R('B4503','使重新有效、恢复或得到补充','RENEW：把已有事物接着更新、延续','renew → renewal、renewable。',
 '续合同、恢复精力、更新资源，都可以围绕使某事重新或继续有效理解；具体怎样更新由对象决定。',
 're- 再 + new → renew；-al 行为、结果；-able 可更新、可续或可再生。',
 [['行动、名词与性质','renew · renewal · renewable']],
 'renewable 可续、可再生；reusable 可反复用；renewal 是更新、续期这件事。',
 'The renewable contract is due for renewal next month.\n\n可续期的合同下个月需要办理续期。','renew renewal renewable')
S=[['古英语 scōh → 中古英语 sho、scho → shoe','穿在脚上的保护物；远源未定'],['物件与配件的组合','shoelace、shoeless；gumshoe 用橡胶底鞋转指侦探'],['音乐领域的固定名称','shoe + gaze 相关形式 → shoegaze 盯鞋摇滚']]
W('shoe','/ʃuː/','鞋；马蹄铁；给穿鞋、钉蹄铁',
 '鞋保护脚，马蹄铁也保护马蹄，因此 shoe 可说两者。动词 shoe a horse 就是给马钉蹄铁；in someone’s shoes 则借鞋里的位置说处境。',
 '古英语 scōh，经中古英语 sho、scho 传为 shoe。更早来源未定，现代核心词不用强拆小词根。',S[:1]+[['穿鞋、鞋的形状和位置','动词给穿鞋、钉蹄铁；器具名称、处境比喻']],
 'a pair of shoes 一双鞋，take off your shoes 脱鞋，put yourself in her shoes 设身处地想她的处境。shoe 作动词的常见过去式、过去分词为 shod。',
 'a pair of shoes；take off your shoes；in someone’s shoes。',
 'shoe 是单只鞋，a pair 是一双。boot 通常有较高的靴筒；很多日常鞋类则以 shoes 统称。',
 ('He left his shoes by the door.','他把鞋留在门边。'),('Try putting yourself in her shoes before you reply.','回复之前，试着站在她的处境想一想。'))
W('shoelace','/ˈʃuːleɪs/','鞋带',
 '穿过鞋孔、拉紧后系住鞋的那根带子，就是 shoelace。这里 lace 取系物的细绳、带义。',
 'shoe 鞋 + lace 系带，直接按用途组成复合词。通常复数 shoelaces 说一双鞋上的鞋带。',S[:1]+[['shoe + lace → shoelace','给鞋系紧的带子']],
 'tie your shoelaces 系鞋带，untie a shoelace 解开鞋带，Your shoelace is undone. 你的鞋带开了。',
 'tie your shoelaces；a loose shoelace。',
 'lace 单独还可说蕾丝织物；shoelace 的固定意思是鞋带，不随意译成鞋上的蕾丝。',
 ('Her shoelace came undone during the race.','比赛中她的鞋带松开了。'),('He stopped to tie his shoelaces.','他停下来系鞋带。'))
W('shoeless','/ˈʃuːləs/','没穿鞋的、没有鞋的',
 '只说明鞋不在脚上，或一个人没有鞋穿；原因可以是进屋脱鞋、在沙滩玩，也可以是缺少鞋。',
 'shoe + -less 没有……的；中古英语已有对应形式。把有鞋的状态改为无鞋的状态。',S[:1]+[['shoe + -less → shoeless','未穿鞋、没有鞋']],
 'shoeless children 没穿鞋的孩子，walk shoeless 没穿鞋走路。语境决定是在描述一时状态还是物资缺乏。',
 'walk shoeless；a shoeless child。',
 'shoeless 只排除鞋，可能仍穿袜子；barefoot 则直接说赤脚。',
 ('The children ran shoeless across the sand.','孩子们没穿鞋，在沙地上跑。'),('He stood shoeless in his socks while the floor dried.','等地板干时，他脱了鞋，穿着袜子站着。'))
W('gumshoe','/ˈɡʌmʃuː/','侦探〔口语、常带旧式故事色彩〕；橡胶底鞋、橡胶套鞋〔旧用〕',
 '先有橡胶底的鞋，再用鞋来代称穿这类鞋的侦探。读侦探小说时，一个 gumshoe 往往就是一个查案的人。',
 'gum 橡胶 + shoe。英语先有橡胶鞋义，随后出现侦探义；gum 在这里不是口香糖。',S[:1]+[['gum 橡胶 + shoe → gumshoe','橡胶鞋 → 侦探的口语代称']],
 'a private gumshoe 私家侦探，an old gumshoe 老侦探。现代普通正式表达通常用 detective、private investigator。',
 'a private gumshoe；a fictional gumshoe。',
 'gumshoe 带口语、旧式侦探故事色彩；police officer 范围更广，不是每位警察都专门调查案件。',
 ('The novel follows a gumshoe through the rainy city.','小说跟着一名侦探穿行在雨城里。'),('They hired a private gumshoe to find the missing papers.','他们雇了一位私家侦探寻找遗失的文件。'),sources=['https://en.wiktionary.org/wiki/gumshoe#English','https://www.etymonline.com/word/gumshoe'])
W('shoegaze','/ˈʃuːɡeɪz/','盯鞋摇滚、瞪鞋摇滚',
 '吉他声经过效果处理，像层层铺开的声浪，人声常朦胧地融在里面。这是音乐风格名；名称让人想到台上低头看脚边的演出姿态。',
 'shoe + gaze 凝视；可能由 shoegazing、shoegazer 等相关名称逆构而来。命名联系乐手低头演奏、看地面或脚边设备的形象，具体最初故事有不同记述。',S[:1]+S[2:],
 'a shoegaze band 盯鞋摇滚乐队，shoegaze guitars 此类风格的吉他音色。这个名称主要用来识别音乐风格。',
 'a shoegaze band；shoegaze guitars。',
 '名称来自表演形象，不要求每位乐手一直盯着鞋；也不能仅凭一个人低头就判断音乐属于 shoegaze。',
 ('The band blends shoegaze guitars with soft vocals.','乐队把盯鞋摇滚式的吉他声与轻柔人声结合起来。'),('She discovered shoegaze through a friend’s playlist.','她通过朋友的歌单接触到盯鞋摇滚。'),sources=['https://en.wiktionary.org/wiki/shoegaze#English','https://www.merriam-webster.com/dictionary/shoegaze'])
R('B2912','保护脚的鞋，配件、人物代称与音乐名称','SHOE：从脚上穿的物件出发，看用途与转称','shoe → shoeless；shoelace、shoemaker、shoebox 等按配件用途展开；gumshoe、shoegaze 各有固定转义。',
 '多数 shoe 组合很直观，但侦探与音乐名称要多走一步：前者用鞋代人，后者把演出形象变成风格名。',
 'scōh → shoe；-less 无，maker 制作者；lace 系带、box 盒；gum 橡胶，gaze 凝视。',
 [['基础与性质','shoe · shoeless'],['配件、制作、储放与保养','shoelace · shoemaker · shoebox · shoehorn · shoeshine'],['形状、用途与固定比喻','snowshoe · shoestring · gumshoe · shoegaze']],
 'shoeless 可能仍有袜子；gumshoe 的 gum 是橡胶；shoegaze 是音乐风格。',
 'The shoemaker replaced the shoelaces and polished the shoes.\n\n鞋匠换了鞋带，又把鞋擦亮。','shoe shoeless shoelace shoemaker shoebox shoehorn shoeshine snowshoe shoestring gumshoe shoegaze')
if __name__=='__main__':save('continuation_20261030_ke',ROOTS,WORDS)
