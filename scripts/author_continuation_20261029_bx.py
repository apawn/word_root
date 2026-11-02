"""Death and interest: everyday senses, fixed expressions and important contrasts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
DE=[['古英语 dēaþ → 中古英语 deth / deeth','死亡'],['英语 death','死亡；生命、事物的终结']]
W('death','/deθ/','死亡；死；终结',
 '说生命终止这件事或这种状态，也能借说某种事物走到了尽头。',
 '继承古英语 dēaþ，经中古英语 deth 等形式发展，与 die、dead 同属古老词族。现代不能直接当成 die 加一个随意变形的后缀。',DE,
 'the death of a friend 朋友的去世；a death in the family 家中有人去世；the death of an industry 某行业的消亡。scared to death 吓死了常是夸张。',
 'after someone’s death；a sudden death；the death of；scared to death；bored to death。',
 'die 是死去的动词，dead 是死了的形容词，death 是死亡名词；不能说 he is death 来代替 he is dead。',
 ('The book was published after the author’s death.','这本书在作者去世后出版。'),('I was scared to death when the lights suddenly went out.','灯突然熄灭时，我吓坏了。'),('The article discusses the death of a once popular art form.','文章讨论一种曾经流行的艺术形式的消亡。'))
W('deathbed','/ˈdeθbed/','临终床榻；临终时',
 '不是一种特殊床的款式，而是人在生命最后阶段躺着的床及那个时刻。',
 'death 死亡 + bed 床，形成临终床榻这一复合名词；又可修饰 statement、wish 等表示临终时做出的。',C('death 死亡、临终','bed 床','deathbed','临终床榻；临终时刻'),
 'on one’s deathbed 在临终时；a deathbed confession 临终告白。小说、历史传记里常见，不等于所有病床。',
 'on his deathbed；a deathbed wish；a deathbed confession。',
 'deathbed 是临终处境中的床或时刻；sickbed 是病床，生病不一定就是临终。',
 ('In the novel, he reveals the secret on his deathbed.','小说里，他在临终时透露了秘密。'),('The biography questions whether the deathbed story is true.','传记质疑那则临终故事是否真实。'))
W('deathly','/ˈdeθli/','死一般的；极度地；令人联想到死亡的',
 '不是在说一定会杀死人，而是苍白、寂静、寒冷等状态像死亡一样强烈。',
 'death + -ly；旧英语已有对应形式。既可作形容词，也可作副词，后缀 -ly 不保证只生成副词。',DE+[['古英语 dēaþlīċ → deathly','与死亡相关、死一般；现代还可强化程度']],
 'deathly pale 惨白，deathly quiet 死一般寂静；a deathly silence 一片死寂。口语 deathly afraid 是怕得要命。',
 'deathly pale；deathly quiet；deathly afraid；a deathly silence。',
 'deathly 常是死一般、极度；deadly 常强调致命，也有程度副词等其他用法。deathly pale 不等于脸色会杀死人。',
 ('The room became deathly quiet after the announcement.','消息宣布后，房间里一片死寂。'),('He looked deathly pale under the harsh light.','在刺眼灯光下，他脸色惨白。'))
W('deathless','/ˈdeθləs/','不死的；不朽的，常用于文学或讽刺',
 '把死亡从图景里拿掉：生命不终止，或者名声、作品不会被遗忘。',
 'death + -less，无……的，形成不死、不朽的形容词。文学用法比日常口语更常见。',DE+[['death + -less → deathless','死亡 → 不死、不朽的']],
 'deathless fame 不朽名声；deathless prose 可赞不朽文字，也可反讽某人自以为不朽。实际褒贬看语气。',
 'deathless fame；deathless poetry；the deathless gods。',
 'deathless 与 immortal 有意义重合，但更有文学、修辞感；不是医学意义上的永远不会死亡的事实断言。',
 ('The poem promises its hero deathless fame.','诗歌许诺英雄将获得不朽声名。'),('The critic jokingly referred to the speech as “deathless prose.”','评论者开玩笑地把那篇演讲称为“不朽文章”。'))
W('deathtrap','/ˈdeθtræp/','极危险的地方、建筑或交通工具',
 '像一个能把人困在致命危险里的陷阱，借来形容危险得吓人的场所或东西。',
 'death 死亡 + trap 陷阱，形成常带强烈批评的名词；不一定指故意为杀人设计的真正机关。',C('death 死亡、致命危险','trap 陷阱','deathtrap','危险到可能致命的地方或东西'),
 'a building described as a deathtrap 被形容为危险陷阱的建筑；a deathtrap of a car 危险得不得了的车。说话人常在强调危险，未必已有死亡发生。',
 'a potential deathtrap；call a building a deathtrap；a deathtrap of a car。',
 'deathtrap 比 simply unsafe 强得多；它是评价危险程度的词，不自动说明这是蓄意杀人的陷阱。',
 ('Residents described the crumbling staircase as a deathtrap.','居民把破败的楼梯形容为可能致命的危险之地。'),('In the film, the abandoned mine becomes a deathtrap.','电影里，废弃矿井成了一个致命险境。'))
W('deathmatch','/ˈdeθmætʃ/','游戏中的对战模式；以击败对手为目标的较量',
 '在游戏里各自或分队对战，用击败对手等结果来计分；名字使用了夸张的生死较量画面。',
 'death 死亡 + match 比赛，形成对战名称。电子游戏里的具体模式、获胜条件由各款游戏确定，不把名字当作现实死亡事实。',C('death 死亡、生死较量意象','match 比赛','deathmatch','游戏对战等较量名称'),
 'a multiplayer deathmatch 多人对战；team deathmatch 团队对战。也可能见于其他带生死较量意味的比赛名称，需看媒介和背景。',
 'a deathmatch mode；a team deathmatch；join a deathmatch。',
 'deathmatch 是模式名称，不是所有多人游戏的总称；match 比赛也不等于 match 火柴。',
 ('The game includes a separate deathmatch mode.','这款游戏另设一种多人对战模式。'),('We tried a short team deathmatch after finishing the tutorial.','完成教程后，我们试了一局短暂的团队对战。'))
R('B3065','死亡；终结；强烈修辞和固定组合','DEATH：生命终止，也能借作夸张与比喻','death 是名词，不要与 die 动词、dead 形容词混用。复合词有些是实际临终，有些只借死亡的强烈画面。',
 'death 接古英语 dēaþ。deathbed 抓临终时刻，deathly 抓死一般的样子，deathless 抓不朽，deathtrap 抓危险。',
 'death → deathly、deathless；deathbed、deathtrap；游戏名称 deathmatch 单看固定用法。',
 [['基本概念与形容、程度','death · deathly · deathless'],['处境、危险和游戏名称','deathbed · deathtrap · deathmatch']],
 'deathly pale 是惨白；scared to death 是吓坏的夸张；deathtrap 不保证已有死亡，也不必是蓄意机关。',
 'The deathly silence made the old house feel like a deathtrap.\n\n死一般的寂静，让那座老房子仿佛成了致命险境。',
 'death deathly deathless deathbed deathtrap deathmatch')
IN=[['拉丁语 interesse，字面 inter- 在……之间 + esse 存在','相关、有影响、重要；并非现代兴趣的逐字翻译'],['中世纪拉丁语、法语相关名词 → 英语 interest','牵涉的权益、补偿等 → 后发展出兴趣、利息等用法']]
W('interest','英 /ˈɪntrəst/；美 /ˈɪntrəst/','兴趣；吸引注意；利益、权益；利息',
 '一件事与你有关，可能吸引你，也可能牵涉你的得失；钱的使用还有利息这个固定意思。',
 '经法语来自拉丁语 interesse 相关、有影响、重要。历史上有权益、损失补偿等用法，后发展出注意兴趣与借款利息；从损失到收益的每一步并非全清楚，不硬编成唯一直线。',IN,
 'an interest in music 对音乐的兴趣；interest someone 引起某人兴趣；in your interests 符合你的利益；pay interest 付利息。兴趣和金钱场景要看搭配，不靠拼写分词。',
 'take an interest in；show interest；in the interests of；a conflict of interest；interest on a loan。',
 'interest 不一定只是爱好；conflict of interest 是利益冲突。interest rate 是利率，interest 是利息本身或相关概念。',
 ('She has a strong interest in architecture.','她对建筑有浓厚兴趣。'),('The unusual design immediately interested me.','这个不同寻常的设计立刻引起了我的兴趣。'),('The statement lists the interest paid during the year.','账单列出了这一年支付的利息。'),sources=['https://en.wiktionary.org/wiki/interest#English','https://www.etymonline.com/word/interest'])
W('interested','英 /ˈɪntrəstɪd/；美 /ˈɪntrəstɪd/','感兴趣的；有利害关系的',
 '注意力被吸引的是我；或者这件事会影响我的利益，所以我也是相关一方。',
 'interest + -ed，过去分词形容词化。既接引起兴趣的动词义，也保留牵涉利益的意思。',IN+[['interest → interested','引起关注、牵涉利益 → 有兴趣或有利害关系的']],
 'be interested in art 对艺术感兴趣；interested parties 利害相关方。后一搭配不是对活动觉得有趣的派对。',
 'be interested in doing something；an interested buyer；interested parties。',
 'interested 说感受或关系，interesting 说能引起兴趣的特征。I’m interested in history，不是 I’m interesting in history。',
 ('I’m interested in learning how the machine works.','我有兴趣了解这台机器怎样运转。'),('The report was sent to all interested parties.','报告发给了所有相关方。'),sources=['https://en.wiktionary.org/wiki/interested#English','https://dictionary.cambridge.org/uk/grammar/british-grammar/word-choice-interesting-or-interested'])
W('interesting','英 /ˈɪntrəstɪŋ/；美 /ˈɪntrəstɪŋ/','有趣的；引人关注的',
 '这东西能把别人的注意力吸引过来，让人想继续了解。',
 'interest + -ing，分词形成形容词，表示具有引起兴趣的作用。',IN+[['interest → interesting','使人产生兴趣 → 引人关注的']],
 'an interesting question 有意思的问题；find something interesting 觉得某事有趣。事情可能严肃、复杂，却仍然 interesting，不必让人哈哈笑。',
 'an interesting idea；find something interesting；interesting to watch。',
 'interesting 引人关注，funny 常说好笑或奇怪；有趣的历史讲座不必是一场喜剧。',
 ('She raised an interesting question about the painting.','她就这幅画提出了一个有意思的问题。'),('The book is difficult but extremely interesting.','这本书很难，却极其引人入胜。'))
W('interestingly','英 /ˈɪntrəstɪŋli/；美 /ˈɪntrəstɪŋli/','有趣的是；值得注意的是',
 '提醒读者抬一下注意力：下面这个情况值得看看。',
 'interesting + -ly，副词；常作整句评论，指出信息有趣、出乎意料或值得注意。',IN+[['interesting → interestingly','引人关注的 → 值得注意的是']],
 'Interestingly, ... 放在句首，评论后面整件事；interestingly enough 也是常见插入说法。并不是每次都在说某人用有趣的方式做动作。',
 'Interestingly, ...；interestingly enough；more interestingly。',
 'interesting 是事物的特征，interestingly 可引出说话人对一句信息的评价；不等于 fortunately 幸好。',
 ('Interestingly, the smaller room was more expensive.','有意思的是，小房间反而更贵。'),('More interestingly, both teams reached the same conclusion independently.','更值得注意的是，两队独立得出了相同结论。'))
W('uninteresting','英 /ʌnˈɪntrəstɪŋ/；美 /ʌnˈɪntrəstɪŋ/','不有趣的；乏味的',
 '事物没有吸引住注意力，而不是说它本身对别的东西没有兴趣。',
 'un- 不 + interesting 有趣的，否定引起兴趣的性质。',IN+[['interesting → uninteresting','有趣的 → 乏味、不引人关注的']],
 'an uninteresting lecture 乏味讲座；find something uninteresting 觉得某事没意思。这常是个人评价，别人可能不同意。',
 'an uninteresting topic；find something uninteresting；visually uninteresting。',
 'uninteresting 形容事物不吸引人；uninterested 说人没兴趣。不要把词尾 -ing、-ed 当作无关细节。',
 ('The topic was important, but the presentation was uninteresting.','主题很重要，但讲法很乏味。'),('I found the early chapters uninteresting and almost stopped reading.','我觉得前几章没意思，差点不再读下去。'))
W('uninterested','英 /ʌnˈɪntrəstɪd/；美 /ʌnˈɪntrəstɪd/','不感兴趣的；不关心的',
 '东西可能摆在眼前，但我的注意力没被吸引过去。',
 'un- 不 + interested 感兴趣的。历史上曾有不同用法，现代常用义明确是没有兴趣、冷淡。',IN+[['interested → uninterested','感兴趣 → 没有兴趣']],
 'be uninterested in politics 对政治不感兴趣；seem uninterested 显得没兴趣。并不一定表示对方的内容客观上不值得关心。',
 'be uninterested in；remain uninterested；look uninterested。',
 'uninterested 常是没兴趣，disinterested 在正式常用义中是不偏不倚；冷淡与公正不是一回事。',
 ('He seemed uninterested in the new proposal.','他似乎对新提议不感兴趣。'),('She is uninterested in collecting expensive objects.','她对收藏昂贵物品不感兴趣。'),sources=['https://en.wiktionary.org/wiki/uninterested#English','https://www.merriam-webster.com/grammar/uninterested-or-disinterested'])
W('disinterest','英 /dɪsˈɪntrəst/；美 /dɪsˈɪntrəst/','不偏私；无利害关系；缺乏兴趣',
 '可以是没有私人得失夹在里面，也可以是在日常表达中显得没兴趣。',
 'dis- 否定、解除 + interest。interest 本来就有权益与兴趣两面，否定后也出现不偏私、缺乏兴趣等用法。',IN+[['dis- + interest → disinterest','无私利牵涉；另有缺乏兴趣用法']],
 'a lack of personal interest 所对应的不偏私，可以说 disinterest；show disinterest in a topic 在现代用法中也可能是对话题没有兴趣。读句子要确定是哪一面。',
 'a show of disinterest；apparent disinterest；disinterest in the outcome。',
 '不能把所有 disinterest 都判成只有无私，或只有无聊。正式表达公正可用 impartiality，表达没兴趣可用 lack of interest，意思更明确。',
 ('The committee valued her disinterest in the financial outcome.','委员会看重她在财务结果上没有个人利害关系。'),('His apparent disinterest in the discussion frustrated the group.','他对讨论似乎毫无兴趣，让小组很沮丧。'))
W('disinterested','英 /dɪsˈɪntrəstɪd/；美 /dɪsˈɪntrəstɪd/','不偏不倚的；无私利牵涉的；有时表示没兴趣',
 '做判断时没有自己的好处夹在中间，因此能更公正；并不是脑子已经不想参与。',
 '来自 disinterest 的分词或 dis- + interested，两个构词分析都与历史用法有关。无偏私与没兴趣两义长期有交叠，不是现代才发生的单纯误用。',IN+[['dis- + interested / disinterest + -ed → disinterested','无利害关系、不偏私；也有缺乏兴趣用法']],
 'a disinterested observer 不偏不倚的观察者；disinterested advice 不受个人利益影响的建议。正式写作中通常优先用它表达公正，用 uninterested 明确表达没兴趣。',
 'a disinterested observer；a disinterested opinion；disinterested advice。',
 '公正的人可以非常关心事情本身，只是不谋私利。读到没兴趣义也要认识它，但学习表达时分清两词更不容易含混。',
 ('We asked a disinterested expert to review both proposals.','我们请一位没有利害关系的专家评审两份提议。'),('A disinterested observer might reach a different conclusion.','一位不偏不倚的观察者可能得出不同结论。'),sources=['https://en.wiktionary.org/wiki/disinterested#English','https://www.merriam-webster.com/grammar/uninterested-or-disinterested'])
R('B2974','兴趣；利益、利害关系；利息','INTEREST：关注与得失，都可能与你有关','不要只用兴趣一种译法。懂得利害关系这一面，才容易理解 interested parties、disinterested。',
 'interest 经法语接拉丁语 interesse 相关、有影响等用法，中世纪还有补偿、权益背景；兴趣与利息等现代义各有发展，不编成单一步骤。',
 'interest → interested；interesting → interestingly；否定对照 uninteresting、uninterested；再看 disinterest、disinterested 的利益与兴趣两面。',
 [['兴趣来源与人的感受','interest · interested · interesting · interestingly'],['乏味与不感兴趣','uninteresting · uninterested'],['私利牵涉与公正','disinterest · disinterested']],
 'I’m interested，the topic is interesting；disinterested observer 通常是不偏不倚，并非冷淡不关心。',
 'An interested student asked an interesting question, and a disinterested expert assessed the answer.\n\n一位感兴趣的学生提出了有意思的问题，一位无利害关系的专家评估了回答。',
 'interest interested interesting interestingly uninteresting uninterested disinterest disinterested')
if __name__ == '__main__':save('continuation_20261029_bx',ROOTS,WORDS)
