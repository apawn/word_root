"""Bang, eliminate and pee; distinguish lookalikes."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['bang：拟声形成，或联系斯堪的纳维亚语 banga 等','重击、砰的一声；远处路线不完全确定'],['英语 bang 的扩展','猛撞、突然响声；恰好、正中；刘海的固定复数用法']]
W('bang','/bæŋ/','砰的一声；猛敲、猛撞；恰好；刘海〔bangs，美式〕',
 '门猛地关上，砰！bang 很容易先用声音记住。它也能说猛撞的动作；bang in the middle 则借直接、正中的劲头说正好在中央。',
 '通常看作拟声形成，或与古诺尔斯语 banga 敲打等形式有关。名词、动词和语气加强用法逐步扩展，不把未确证的古英语重建形式写成既成事实。',B,
 'a loud bang 一声巨响，bang on the door 猛敲门，bang your head 撞到头，bang in the middle 正在中央。美式 bangs 刘海，对应英式 fringe。另有粗俗性用法，读语境识别。',
 'a loud bang；bang on the door；bang in the middle；bangs。',
 'bang 常有突然、响亮的冲击，tap 往往轻得多。bangs 的刘海义是固定旧用法，不把每缕头发都解释成一次爆炸。',
 ('The door shut with a loud bang.','门砰的一声关上了。'),('The café is bang in the middle of the village.','咖啡馆正好在村子中央。'))
W('banger','英 /ˈbæŋə/；美 /ˈbæŋər/','香肠、破旧汽车〔英式口语〕；特别带劲的歌曲〔口语〕；爆竹',
 '这个词随语境换画面：英国菜单 bangers and mash 是香肠配土豆泥；聊音乐说 a banger，是特别带劲、抓耳的歌。',
 'bang + -er，原可命名发出砰声的人或物，后来形成不同口语义。香肠义常联系烹煮时爆裂的说法，但具体起因存在不同解释，不把一种故事定为唯一事实。',B+[['bang + -er → banger','响声相关物件；再形成食物、车辆、歌曲等固定口语义']],
 'bangers and mash 香肠配土豆泥，an old banger 破旧汽车，a dancefloor banger 舞池里很带劲的歌。英国食物、车辆与现代音乐语境要分开。',
 'bangers and mash；an old banger；a dancefloor banger。',
 'banger 不总是人物；a great song 可以较中性，a banger 更口语、更强调冲击力或让人兴奋。',
 ('He ordered bangers and mash for lunch.','他午餐点了香肠配土豆泥。'),('The DJ ended the set with a real banger.','DJ 用一首特别带劲的歌结束了这段演出。'))
W('bangle','/ˈbæŋɡəl/','手镯；硬质环形饰物',
 '想象一个硬的圆环，套在手腕上，而不是软链条连成的手链。这是 bangle 常指的首饰形态。',
 '首饰名借自印地语 baṅglī、baṅgrī 等表示玻璃手镯的形式。不是 bang 砰响 + -le 小物件；另有罕见同形动词与 bang 相关，不能混作首饰词源。',
 [['印地语 baṅglī 等','玻璃手镯、环形饰物'],['借入英语 bangle','材质范围扩大的硬质手镯名称']],
 'a silver bangle 银手镯，a stack of bangles 一叠、多个叠戴手镯。常是硬环，也有开口、铰链等样式，不必把没有扣作为每件产品的绝对条件。',
 'a silver bangle；wear bangles；a stack of bangles。',
 'bracelet 是手腕饰物的宽泛名称；bangle 通常强调硬环。和 bang 拼写相似，不足以证明它因碰响而得名。',
 ('She wore a silver bangle on her wrist.','她手腕上戴着一个银手镯。'),('The shop sells colourful glass bangles.','这家店卖彩色玻璃手镯。'),sources=['https://en.wiktionary.org/wiki/bangle#English','https://www.etymonline.com/word/bangle'])
R('B3319','重击、响声和固定口语扩展；另辨不同源的首饰词','BANG：声音有冲击；BANGLE 首饰词另有来源','bang → banger 的不同固定口语义；bangle 放在这里作近形辨认，不当作同源扩展。',
 '先抓砰的一声，再看具体搭配。拼写长得像的首饰 bangle，则需要另接印地语来源。',
 'bang 拟声或斯堪的纳维亚语相关来源；bang + -er；bangle 首饰名为独立借词。',
 [['响声与口语扩展','bang · banger'],['近形、不同源辨认','bangle']],
 'bangers 可是香肠，bangs 可是刘海；bangle 手镯不能拆成 bang + -le。',
 'The bang startled the customer while she was looking at a silver bangle.\n\n顾客看银手镯时，被砰的一声吓了一跳。','bang banger bangle')
ROOTS[-1]['exclude']['shebang']='常用整词的远源有争议，不按外形强接 bang；已有独立精讲。'
E=[['拉丁 ē- 向外 + līmen 门槛 → ēlīmināre','把人赶出门，逐出'],['拉丁 ēlīmināt- → 英语 eliminate','移除、排除；淘汰等领域用法']]
W('eliminate','/ɪˈlɪmɪneɪt/','消除、排除；淘汰',
 '原来像把东西请出门外：不再留在这里。今天可以把错误消掉，把一个可能性排除，或让选手退出下一轮。',
 '拉丁 ēlīmināre 逐出门外，ē- 是 ex- 向外的变体，līmen 是门槛；英语词形联系其 ēlīmināt- 词干。不是 e + limit 限制 + nate。',E,
 'eliminate errors 消除错误，eliminate a possibility 排除可能性，be eliminated from the competition 被淘汰。另在暴力语境里可能委婉说杀害，不能把普通排错也这样理解。',
 'eliminate errors；eliminate a possibility；be eliminated from。',
 'reduce 降低数量、程度，eliminate 通常说消除、移出相应范围。比赛中被 eliminate 是失去继续争夺资格，不是从此不能再运动。',
 ('The new checklist helped eliminate common errors.','新检查清单帮助消除了常见错误。'),('The team was eliminated in the first round.','球队第一轮就被淘汰了。'))
W('elimination','/ɪˌlɪmɪˈneɪʃən/','消除、排除；淘汰；消元',
 '把 eliminate 的动作当成一个过程来谈：去掉错误、排除选项、淘汰选手，或在方程里消去某个未知量。',
 '与 eliminate + -ion 的名词结构对应，来源联系拉丁 ēlīminātiō。词尾从动词 -ate 对应到名词 -ation，重音移到 /neɪ/ 这一段。',E+[['eliminate／拉丁 ēlīminātiō → elimination','逐出、消除这一过程；淘汰、消元']],
 'the elimination of errors 错误的消除，an elimination round 淘汰轮，solve by elimination 用消元法解题，a process of elimination 逐一排除法。',
 'the elimination of；an elimination round；by elimination。',
 'elimination 看去掉某项这一过程；selection 看选择留下谁。逐一排除得出答案，不代表只有凭直觉乱猜。',
 ('We found the answer by a process of elimination.','我们用逐一排除法找到了答案。'),('The next stage is an elimination round.','下一阶段是淘汰轮。'))
W('eliminator','英 /ɪˈlɪmɪneɪtə/；美 /ɪˈlɪmɪneɪtər/','消除器、消除剂；淘汰选拔赛；执行消除者',
 '把不需要的东西去掉的装置，可以叫 eliminator；体育里的 eliminator 则可能是一场决定谁能晋级的比赛。',
 'eliminate + -or，去末尾 e 后形成执行者、器具等名词。与 -er 类似，-or 不保证一定是人。',E+[['eliminate + -or → eliminator','执行消除的东西、人物；决定淘汰晋级的赛事']],
 'an odour eliminator 除味产品，a title eliminator 决定冠军挑战资格的选拔赛。产品名里的词说明声称的功能，不代替具体效果证据。',
 'an odour eliminator；a title eliminator。',
 'eliminator 是器具、产品或赛事等名称；elimination 是过程。不是给 elimination 随意省掉几个字母。',
 ('The catalogue lists an odour eliminator for household use.','目录列出了一款家用除味产品。'),('The boxer won the title eliminator.','这名拳手赢了冠军挑战资格选拔赛。'))
R('B3749','把对象移出范围，从逐出门外到消除、排除和淘汰','ELIMINATE：让它不再留在这一范围里','eliminate 动作 → elimination 过程 → eliminator 器具、产品或选拔赛。',
 '词源里的门槛给了一个好画面，但现代不一定真有门：错误离开清单、选手离开晋级名单、未知量从方程中被消去。',
 'ē- 向外 + līmen 门槛 → ēlīmināre；ēlīmināt- 联系英语 eliminate；-ation／-or 形成名词。',
 [['动作、过程与执行者','eliminate · elimination · eliminator']],
 'eliminate 常说消除，reduce 只是减少；eliminator 不必是人。',
 'The elimination round will eliminate half the teams from the tournament.\n\n这一淘汰轮会让半数球队退出赛事。','eliminate elimination eliminator')
W('pee','/piː/','尿；小便、撒尿〔口语〕',
 '比粗俗的 piss 委婉、日常一些，孩子和成人口语都会说。名词说尿或一次小便，动词说这个动作。',
 '把 piss 的首字母 p 按字母名读出来，再写成 pee，形成委婉说法。不是拉丁、希腊词根，也不是由 pea 豌豆变化而来。',
 [['piss → 首字母 p 的字母读音','用字母名称绕开原来的直说'],['p 的读音写作 pee','形成口语名词和动词']],
 'need to pee 需要小便，have a pee 上个厕所〔常见英式〕，take a pee〔常见美式〕。正式说明常用 urinate，礼貌对话也可直接说 use the bathroom。',
 'need to pee；have a pee；take a pee。',
 'pee、pea 同音不同词。peer 的常用同龄人、凝视两义也不由 pee 生成；只有极罕见 pee + -er 的同形人物词才是另一回事。',
 ('The child said she needed to pee.','孩子说她想小便。'),('He stopped to have a pee before the journey.','出发前他停下来上了个厕所。'))
R('B3542','用首字母的读音形成委婉口语','PEE：把 p 的读音写成词','piss → p → pee；不要把常用 peer 按外形接过来。',
 '英语不只靠古典词根造词，也会用字母名作委婉替代。pee 就是常见例子。',
 '首字母 p 的读音 /piː/ → 拼写 pee；名词、动词并用。',
 [['日常委婉用法','pee']],
 'pee 与 pea 同音；常用 peer 的凝视、同等身份各有自己的来源。',
 'The parent used pee when speaking to the child.\n\n家长对孩子说话时用了 pee 这个口语词。','pee')
ROOTS[-1]['exclude']['peer']='常用的同等者、同龄人来自拉丁 pār 经法语；凝视义另有来源。只有罕见 pee + -er 同形词与此有关，先不列。'
if __name__=='__main__':save('continuation_20261030_jd',ROOTS,WORDS)
