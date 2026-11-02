"""Ski, thankful, minded and freak."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['挪威语 ski，承古诺尔斯 skíð','木片、滑雪用长木板'],['英语 ski','一支滑雪板；用板滑行的动作'],['ski + -er → skier','滑雪的人，保持原词 /skiː/ 的读音']]
W('ski','/skiː/','滑雪板；滑雪、乘板滑行',
 '脚下绑着长板，让人沿雪面滑行，板叫 ski，滑的动作也叫 ski。数一双板是 a pair of skis，不把名词和运动一律按同一种数法处理。',
 '借挪威语 ski，上接古诺尔斯 skíð 木片、滑雪长板，联系切分木材的旧词族。现代英语常读 /skiː/，不是照英语 sky 天空读。',S[:2],
 'a pair of skis 一双滑雪板，ski down a slope 滑下斜坡，go skiing 去滑雪。water skis 也可说滑水板，前项会换活动场景。',
 'a pair of skis；ski down a slope；go skiing。',
 'ski 是一支板或动词，skis 是板的复数；skiing 双 i 分属 ski 和 -ing，不需要删掉原词 i。',
 ('She carried a pair of skis to the lift.','她把一双滑雪板带到缆车处。'),('They skied down the gentle slope.','他们滑下平缓雪坡。'),sources=['https://en.wiktionary.org/wiki/ski#English','https://www.etymonline.com/word/ski'])
W('skier','英 /ˈskiːə/；美 /ˈskiːər/','滑雪者、滑雪运动员',
 'ski 是滑，skier 是滑的人。可能刚开始学，也可能参加比赛，词本身不把水平限定成专业运动员。',
 'ski + -er，保留原词 i，加人物后缀。此处读 /skiː/ 的词干，不是 sky 天空的另源动词派生。',S,
 'a beginner skier 初学滑雪者，an experienced skier 有经验的滑雪者，an Olympic skier 奥运滑雪运动员。',
 'a beginner skier；an experienced skier。',
 'skier 是人，ski 是板或动作，skiing 是活动；三者按角色一起记。',
 ('The beginner skier practised on a gentle slope.','初学滑雪者在缓坡上练习。'),('Several skiers waited for the lift to open.','几位滑雪者等候缆车开放。'))
R('B3626','木片、长板转为滑雪器材与相应动作、人物','SKI：脚下长板把人在雪上托着滑','ski → skier；skiing 是活动形式。',
 '器材叫 ski，一双是 skis；动作也可 ski，做的人 skier。词来自挪威语木片、长板的旧名称。',
 'skíð → 挪威 ski → 英语 ski；-er 人物，-ing 活动，均保留词干 i。',
 [['器材、动作与参与者','ski · skier']],
 '读 /skiː/；a pair of skis 数一双板；skier 不一定专业运动员。',
 'The skier checked her skis before starting.\n\n滑雪者出发前检查了滑雪板。','ski skier')
R('B4196','感激的心情、品质，以及对好结果的庆幸评论','THANKFUL：既可谢谢某件事，也可庆幸结果还好','thankful → thankfully、thankfulness。',
 'I’m thankful for your help 是感谢帮助；Thankfully, nobody was hurt 是幸好没人受伤，句首副词表达说话人的庆幸。thankfulness 则把感激变成可谈论的状态。',
 'thank + -ful 具有感激；-ly 方式或全句评论；-ness 抽象品质。',
 [['感激性质、表达方式与状态','thankful · thankfully · thankfulness']],
 'thankfully 不只机械译为感谢地；句首常译幸好；thankfulness 不是一封感谢信。',
 'Thankfully, we arrived safely, and we were thankful for their help.\n\n幸好我们平安抵达，也很感谢他们的帮助。','thankful thankfully thankfulness')
R('B4584','心思朝向某事、具有某种想法或态度','MINDED：看一个人的心思、想法往哪边去','minded 常在 be minded to do 或复合形容词里说明想法、态度。',
 'be minded to agree 较正式，说有意、倾向同意；open-minded 的 open 说明愿意接纳，narrow-minded 则说明想法狭窄。先理解整组，不单背一个有思想的。',
 'mind 心思 + -ed 性质，minded；复合前项给出心思的方向、特点，-ed 在这里不都表示过去发生一次动作。',
 [['倾向与心态性质','minded']],
 'be minded to 比普通 want 更正式；open-minded 的含义由 open + minded 共同形成；很少独立使用的后缀扩展先略过。',
 'After hearing the explanation, she was minded to agree.\n\n听过解释后，她倾向于同意。','minded')
F=[['早期 freak 突然念头、古怪变化','更远来源有迅捷动作、热切旧词等不同分析'],['古怪、异常之物 → 现代多义','意外现象；带贬义的人称；某事爱好者；情绪失控'],['后缀、短语与名词化','freaky、freakish 性质；freak out 动作 → freakout 一次失控等']]
W('freak','/friːk/','反常现象、怪事；〔常贬〕怪人；……迷；〔freak out〕惊慌、失控',
 'freak accident 是罕见、意外的事故；a neat freak 是对整洁特别执着的人；freak out 是一下慌了、激动失控。先看搭配，不把全家都翻怪物。',
 '早期有突发念头、古怪行为等义，更早与迅捷动作、热切旧词的关系有不同分析。后来扩到异常现象、人物称呼、强烈爱好和情绪反应。',F[:2],
 'a freak accident 反常意外事故，a control freak 控制欲很强的人，freak someone out 吓坏某人，freak out about something 因某事慌乱。',
 'a freak accident；freak out；freak someone out。',
 '直接把人叫 a freak 往往侮辱；爱好者式复合可打趣、自称，语气仍看关系。freak accident 不表示出现了真实怪物。',
 ('A freak storm damaged the roof.','一场反常暴风雨损坏了屋顶。'),('The sudden noise freaked me out.','突如其来的噪声把我吓坏了。'),sources=['https://en.wiktionary.org/wiki/freak#English','https://www.etymonline.com/word/freak'])
W('freaky','/ˈfriːki/','古怪、诡异的；令人害怕的〔口语〕',
 '走廊里突然传来和你一模一样的声音，让人觉得怪得发毛，可以 freaky。这个词常把奇怪和情绪反应连在一起。',
 'freak + -y，形成像怪事、异常现象的性质；在口语中常表示离奇、诡异、吓人等。',F[:2]+[['freak + -y → freaky','异常、古怪的性质，常有诡异感']],
 'a freaky coincidence 离奇巧合，a freaky sound 诡异声音，a freaky dream 古怪的梦。其他俚语义需按作品场景理解。',
 'a freaky coincidence；a freaky sound。',
 'freaky 不保证真的危险；有时只是新奇离奇，也可能是称赞某种独特风格。',
 ('We had a freaky coincidence: we both chose the same unusual name.','巧得离奇，我们都选了同一个少见名字。'),('A freaky sound came from the empty room.','空房间里传来诡异声音。'))
W('freakish','/ˈfriːkɪʃ/','反常、奇特的；怪异、难以预料的',
 '比平常偏得很远，可以 freakish：异常天气、惊人的力量、古怪变化。它常突出异乎寻常，不一定只有恐怖一种评价。',
 'freak + -ish，早有任性、变化无常等义，后来也说怪异、反常。-ish 此处表具有相应特点，不保证程度轻。',F[:2]+[['freak + -ish → freakish','变化无常、反常、奇异的性质']],
 'freakish weather 反常天气，freakish strength 异乎寻常的力量，a freakish accident 罕见反常事故。',
 'freakish weather；freakish strength。',
 'freakish 的评价可赞叹、惊异或批评；freaky 更口语，但两者有重叠，不用一条绝对褒贬线硬分。',
 ('Freakish weather brought snow after a week of heat.','天气反常，热了一周后竟下起雪。'),('The athlete showed freakish strength for someone so young.','这名运动员年纪轻轻，力量却异乎寻常。'))
W('freakout','/ˈfriːkaʊt/','一阵惊慌、激动失控；令人失措的经历〔口语〕',
 'freak out 是动作，a freakout 把那一阵慌乱、情绪失控当成一件事。后来发现护照没丢，刚才那场慌乱就结束了。',
 '由短语动词 freak out 名词化，合写为 freakout；早期还与迷幻体验有关，现代可泛指强烈失措的反应，不必涉及药物。',F[:2]+[['freak out → freakout','失控动作 → 一次失控反应、经历']],
 'have a freakout 慌乱、失控一阵，a brief freakout 短暂惊慌，a public freakout 当众情绪失控。也可见分写、连字符拼法，本页用合写词头。',
 'have a freakout；a brief freakout。',
 '动词常分开 freak out，名词可合写 a freakout；这是口语描述，不凭一个词推断完整心理状况。',
 ('He had a brief freakout when he thought he had lost his passport.','以为护照丢了时，他慌了一阵。'),('The freakout ended as soon as she found the keys.','她一找到钥匙，刚才那阵慌乱就结束了。'),sources=['https://en.wiktionary.org/wiki/freakout#English','https://www.etymonline.com/word/freak'])
R('B4038','古怪、异常与突发反应，区分性质、动作和一次经历','FREAK：超出寻常，会让人惊讶，也可能让人慌乱','freak → freaky、freakish；freak out → freakout。',
 '天气、巧合、力量各有异常，人的反应可能 freak out。异常不只恐怖，也可能惊人；人物称呼则须读出贬义或自嘲。',
 'freak 更远来源未定；-y、-ish 性质；out 与动词成短语，再名词化为 freakout。',
 [['异常与相应性质','freak · freaky · freakish'],['失控动作的名词化','freakout']],
 'freaky 不必真危险；freakish 不一定贬义；freak out 动词分开，a freakout 名词可合写。',
 'The freaky noise caused a brief freakout.\n\n那个诡异声音让人短暂慌乱了一阵。','freak freaky freakish freakout')
if __name__=='__main__':save('continuation_20261030_lu',ROOTS,WORDS)
