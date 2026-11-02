"""Common rising, swelling and falling families, individually explained."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1760':dict(words='swell swells swelled swelling swellings swollen'.split(),label='swell：胀大与两种分词形式',note='swell 接古英语 swellan 变大，远源未定；规则 swelled 与保留强变化的 swollen 并存。通常过去式 swelled，过去分词常用 swollen；不能把 swollen 拆成现代 swell 加普通 -en 就解释其全部历史。'),
 'C0395':dict(words='soar soars soared soaring'.split(),label='soar：经法语演变的高飞',note='soar 经古法语 essorer 接重建通俗拉丁 *exaurare，材料为 ex- 与 aura 空气、微风。现代 soar 不再能按字母直接切出 ex-；aura 也不是 aur- 金或 auri- 耳。'),
 'C1077':dict(words='plunge plunges plunged plunging'.split(),label='plunge：从铅坠材料到猛扎进去',note='plunge 经法语 plongier 接重建 *plumbicare 与拉丁 plumbum 铅，可能关联测深铅坠或铅坠网具，具体最初场景不确定。抽象的陷入状态义在早期英语已存在。'),
 'A2238':dict(words='tumble tumbles tumbled tumbling'.split(),label='tumble：翻滚、跌落与旧反复动作尾',note='tumble 可能在旧 tumb 落、跃、舞动材料上形成反复动作词，与古英语 tumbian 等相关；不是把现代英语一个独立 tum 加 -ble 能完全拆清。'),
}
SWELL=[['古英语 swellan → 中古英语 swellen → swell','变大、胀起；更远来源未定'],['身体、海面等变大 → 情绪、音量、数量增强','过去式 swelled；旧强变化分词 swollen 仍常用']]
SOAR=[['拉丁 ex- 向外 + aura 空气、微风 → 重建 *exaurare','升到空中；星号表示重建形式'],['古法语 essorer → 英语 soar','鸟高飞、滑翔；后来扩展到志向、价格等升高']]
PLUNGE=[['拉丁 plumbum 铅 → 重建 *plumbicare → 古法语 plongier','可能联系测深铅坠或铅坠网具，最初具体场景未定'],['中古英语 plungen → plunge','猛地投入、浸入；早期也已说陷入困境等状态']]
TUMBLE=[['古英语 tumbian 等：跃动、舞动 → 中古英语 tumben、tumblen','可能有反复动作尾，更远来源未定'],['翻身、失足跌落 → 翻滚；后来也说价格急跌','名词再写一次跌落、翻滚或混乱']]
W('swell','/swel/','胀大、肿起；增强、增多；涌浪',
 '海绵吸水后鼓起来，声音一层层变响，人群越来越大，都能用 swell。先抓住“原来的体量或强度在变大”。',
 '古英语 swellan 变大延续至今，远源未定。动词之后形成名词；海上的 swell 常是连续、较长的涌浪。形容词 swell 很棒另由旧时髦人物义发展，口气较旧。',SWELL,
 'swell with pride 满心自豪；a swell of support 支持声势增强；ocean swell 海上涌浪。',
 'swell up 肿起、胀起；swell to a crowd of hundreds 增至数百人。',
 'swell 常给人逐步胀起的感觉，surge 常突出一股力量突然涌强；具体过程仍看上下文。',
 ('The music began to swell as the doors opened.','门打开时，音乐声开始增强。'),('A long swell lifted the boat gently.','一道长涌浪轻轻托起小船。'),sources=S('swell','swell'))
W('swells','/swelz/','胀大、增强〔第三人称单数〕；涌浪〔复数〕',
 '一个声音越来越响，是 it swells；海面上一道道缓长起伏的浪，是 swells。两种形式拼在一起，要看句中是在做什么。',
 'swell + -s，/l/ 后读 /z/；既可为动词三单，也可为名词复数。',SWELL+[['swell + -s → swells','它胀大、增强；多道涌浪']],
 'the river swells 河水上涨；ocean swells 海上涌浪。',
 'swells with emotion 满心激动；large swells 大涌浪。',
 'swells 是较长的海面起伏，ripples 是细小波纹；大小、波形的画面不同。',
 ('The crowd swells as more people arrive.','随着更多人赶来，人群越来越大。'),('The boat rose and fell with the swells.','小船随一道道涌浪起伏。'),sources=S('swells','swell'))
W('swelled','/sweld/','胀大、增强了；使增多了',
 '原来只有几十人的队伍，一路加入新人，最后扩大到几百人，这个变大的过程过去发生了，就用 swelled。',
 'swell + 完整 -ed，/l/ 后读 /d/。swelled 通常作过去式，也可作分词；swollen 是常用的另一过去分词。',SWELL+[['swell + -ed → swelled','规则过去式、过去分词形式']],
 'swelled to 增至；swelled with pride 充满自豪；swelled the total 使总数增加。',
 'the river swelled；the music swelled。',
 '叙述昨天肿起来可说 the ankle swelled；说现在肿着常用 a swollen ankle。swelled 和 swollen 的常用位置不同。',
 ('The crowd swelled to more than a thousand people.','人群扩大到一千多人。'),('Her heart swelled with pride as she watched her son perform.','看着儿子表演，她心中充满自豪。'),sources=S('swelled','swell'))
W('swelling','/ˈswelɪŋ/','正在胀大、增强；肿胀、肿起处',
 '脚踝比平常鼓出一块，that swelling 指那处肿胀；人群不断变大，a swelling crowd 则说人数在增长。',
 'swell + -ing；动作名词的对应形式在古英语已有，不是现代英语才临时造出。可说过程，也可说肿起的部位。',SWELL+[['swell + -ing → swelling','胀大过程、正在增强的性质，或具体肿胀处']],
 'reduce the swelling 让肿胀减轻；swelling crowds 越来越大的人群。',
 'swelling around the ankle 脚踝周围的肿胀；a swelling chorus 越来越响的合唱。',
 'swelling 常说胀大的过程或现象，swollen 常直接描述已经胀起的状态；两者可从不同角度写同一部位。',
 ('The swelling around his ankle had gone down by morning.','到了早晨，他脚踝周围的肿胀已经减轻。'),('We could hear a swelling chorus of voices outside.','我们听见外面的齐声呼喊越来越响。'),sources=S('swelling','swelling'))
W('swellings','/ˈswelɪŋz/','多处肿胀、肿起部位',
 '不是笼统说“有点肿”，而是身上能分出几处鼓起的部位，才把 swelling 数出来，写成 swellings。',
 'swelling 名词 + -s，读 /z/；可数时说一处处肿起的部位，泛说肿胀现象常用不可数 swelling。',SWELL+[['swelling + -s → swellings','数得出的多处肿起部位']],
 'small swellings 几处小肿块；swellings under the skin 皮下肿起处。',
 'swellings on the hands；several swellings。',
 'swellings 描述外观上肿起的部位，本身不说明原因；lumps 也可说块状物，但不一定是肿胀形成。',
 ('She noticed two small swellings on the back of her hand.','她注意到手背上有两处小肿起。'),('The report described several swellings under the skin.','报告描述了皮下几处肿起的部位。'),sources=S('swellings','swelling'))
W('swollen','英 /ˈswəʊlən/；美 /ˈswoʊlən/','肿起的、胀大的；swell 的过去分词',
 '脚踝、眼皮、河水已经胀起或涨满，swollen 把结果摆到眼前。a swollen river 是水量涨得很大的河。',
 '保留 swell 的旧强变化分词，与古英语 geswollen 相接。现代可对应 swell → swelled → swollen，但不是任意动词加 -en 都能照做。',SWELL+[['旧强变化分词 → swollen','已经胀起、涨大的状态']],
 'swollen ankles 肿起的脚踝；swollen eyes 肿起的眼睛；a swollen river 涨水的河。',
 'be swollen with pride 自大、自满；swollen by heavy rain 因大雨涨水。',
 'swollen 常是身体部位或体量已经鼓起，swelling 可描述仍在增长；有时都能形容河水，但关注点不同。',
 ('Her eyes were swollen from crying.','她的眼睛哭肿了。'),('The swollen river had covered the footpath.','涨水的河已经淹过小路。'),sources=S('swollen','swollen'))
W('soar','英 /sɔː/；美 /sɔr/','高飞、翱翔；猛涨；高耸',
 '鹰展开翅膀，乘着气流飞向高处，就是 soar。把这条向上的线放到图表里，价格、成本也能 soar。',
 '经古法语 essorer，上接重建通俗拉丁 *exaurare，材料为 ex- 向外与 aura 空气、微风。现代英语中把 soar 当整体，不能按现在的字母硬切成前缀和词根。',SOAR,
 'soar above 在高处翱翔、高耸于；prices soar 价格猛涨；spirits soar 心情大振。',
 'soar into the sky 飞上高空；costs soar 成本猛增。',
 'fly 泛说飞行，soar 尤其让人看到飞得高、借气流滑翔或快速上升的画面；并非所有飞行都要译成翱翔。',
 ('We watched an eagle soar above the valley.','我们看着一只鹰在山谷上空翱翔。'),('Heating costs could soar this winter.','今年冬天取暖费用可能猛涨。'),sources=S('soar','soar'))
W('soars','英 /sɔːz/；美 /sɔrz/','高飞、猛涨、高耸〔第三人称单数〕',
 '镜头跟着一只鸟越飞越高，或曲线一下往上冲，主语是单数时就用 soars。动作都带着明显向上的劲头。',
 'soar + -s，读 /z/；这是现代英语词尾，内部较早的法语、拉丁语演变不靠现代拼写直接呈现。',SOAR+[['soar + -s → soars','它高飞、猛涨或高耸']],
 'confidence soars 信心大增；the tower soars above 高塔耸立于……之上。',
 'a bird soars overhead；demand soars 需求猛增。',
 'demand soars 写增长强，demand rises 只中性地说上升；不能只凭一个百分比机械判定必须用哪一个。',
 ('The tower soars above the surrounding houses.','高塔耸立在周围房屋之上。'),('Demand for fans soars during hot weather.','炎热天气里，风扇需求猛增。'),sources=S('soars','soar'))
W('soared','英 /sɔːd/；美 /sɔrd/','高飞了；猛涨了；心情大振了',
 '听到好消息，原本低落的心情一下飞起来，就能说 my spirits soared。它也照常写鸟飞高、数字猛涨。',
 'soar + 完整 -ed，读 /d/；规则过去式、过去分词，主体可为鸟、数量、情绪等。',SOAR+[['soar + -ed → soared','过去高飞或显著上升']],
 'prices soared 价格猛涨；spirits soared 心情大振；soared to a new high 猛增至新高。',
 'soared above the trees；soared after the announcement。',
 'soared 常突出明显上升，rose 范围更广；写 his spirits soared 是心情振奋，不是身体实际飞起。',
 ('The kite soared above the trees.','风筝飞到了树梢之上。'),('Her spirits soared when she saw her family waiting outside.','看到家人在外面等着，她一下高兴起来。'),sources=S('soared','soar'))
W('soaring','英 /ˈsɔːrɪŋ/；美 /ˈsɔrɪŋ/','正在高飞的；猛涨的；高耸的',
 '高昂的旋律一路上扬，费用曲线一路猛冲，都可以说 soaring。它能写正在发生的动作，也能直接修饰某种高涨的状态。',
 'soar + -ing。英式单独 soar 常不读词尾 r，加元音开头 -ing 后 r 发音；没有凭空添一个新词根。',SOAR+[['soar + -ing → soaring','高飞过程，或高耸、显著上升的性质']],
 'soaring costs 猛涨的费用；soaring ceilings 高挑的天花板；a soaring melody 高昂的旋律。',
 'soaring temperatures；soaring above the cliffs。',
 'soaring costs 是费用强劲增长，high costs 只是费用水平高；一个说变化，一个说所处水平。',
 ('Soaring rents forced the shop to move.','租金猛涨，迫使这家店搬迁。'),('The hall has soaring ceilings and tall windows.','大厅的天花板高挑，窗户也很高。'),sources=S('soaring','soar'))
W('plunge','/plʌndʒ/','猛地投入、扎入；骤降；陷入；纵身一跃',
 '不是慢慢试水，而是一下扎进水里。钱数、温度忽然往下掉，或整个人一头投入新工作，也能用这个画面理解 plunge。',
 '经古法语 plongier 接重建 *plumbicare 与拉丁 plumbum 铅，可能联系测深铅坠或铅坠网具，具体最初场景未定。英语早期已有陷入某状态的抽象义，不是现代才想到比喻。',PLUNGE,
 'plunge into water 扎进水；plunge into work 一头投入工作；take the plunge 下决心迈出一步。',
 'plunge a room into darkness 使房间突然陷入黑暗；a plunge in prices 价格骤降。',
 'dip 可以只是轻蘸、短暂下降，plunge 通常动作更猛或降得更深；take the plunge 常说下定决心行动。',
 ('Plunge the vegetables into cold water after cooking.','蔬菜煮好后，马上放进冷水里。'),('After months of planning, we decided to take the plunge and open a café.','计划了几个月后，我们决定迈出这一步，开一家咖啡馆。'),sources=S('plunge','plunge'))
W('plunges','/ˈplʌndʒɪz/','猛扎、骤降、陷入〔第三人称单数〕；猛跌、跳入〔复数〕',
 '瀑布从高处直落而下，可以说 it plunges；价格一回回急跌，可以把那些跌落叫 plunges。',
 'plunge + -s，拼写加 -s，因 /dʒ/ 后读 /ɪz/ 而多一个音节。既可为动词三单，也可为名词复数。',PLUNGE+[['plunge + -s → plunges','它猛扎、急降；多次跳入或猛跌']],
 'plunges into darkness 突然陷入黑暗；sharp plunges 急剧下跌。',
 'the waterfall plunges；plunges in temperature 几次气温骤降。',
 'plunges 的 /ɪz/ 是这类词尾的发音，不能因为多出音节就把词基改猜成 plung。',
 ('The waterfall plunges into a deep pool.','瀑布直落进一个深潭。'),('The chart shows two sharp plunges in temperature.','图表显示了两次气温骤降。'),sources=S('plunges','plunge'))
W('plunged','/plʌndʒd/','猛扎、骤降、陷入了；使突然进入某状态',
 '灯一灭，整个房间一下黑了，是 was plunged into darkness；一整天温度突然下跌，也用 plunged。它把变化写得很突然。',
 'plunge 去不发音 e 加完整 -ed，/dʒ/ 后 -ed 读 /d/，不另加 /ɪd/ 音节。',PLUNGE+[['plunge + -ed → plunged','过去猛投入、骤降或使陷入状态']],
 'plunged into darkness 陷入黑暗；plunged into debt 陷入债务；prices plunged 价格猛跌。',
 'plunged into the water；plunged the town into confusion。',
 'plunged into debt 强调突然或深深陷进去，was in debt 只说明负债状态；原句没有交代的具体降幅不由词本身保证。',
 ('The power cut plunged the house into darkness.','停电让整栋房子一下陷入黑暗。'),('Temperatures plunged overnight.','气温在夜间骤降。'),sources=S('plunged','plunge'))
W('plunging','/ˈplʌndʒɪŋ/','正在猛扎、骤降；领口开得很低的',
 '曲线猛地往下，叫 plunging prices；衣服的领口向下开得很深，便是 a plunging neckline。同样借向下深入的画面。',
 'plunge 去不发音 e 加 -ing。动作形式可作修饰；plunging neckline 是后来固定下来的服装搭配。',PLUNGE+[['plunge + -ing → plunging','猛扎、急降的过程；低开领口的修饰']],
 'plunging temperatures 骤降的气温；a plunging neckline 低开的领口。',
 'plunging into the sea；plunging sales 急跌的销量。',
 'plunging neckline 说领口开得低，不能据此把 plunging 随意加到所有低矮物体上；固定搭配要整组学。',
 ('Plunging temperatures left the roads icy.','气温骤降，使道路结了冰。'),('The dress has a plunging neckline.','这条裙子的领口开得很低。'),sources=S('plunging','plunge'))
W('tumble','/ˈtʌmbəl/','翻滚、跌倒；急跌；一跤',
 '箱子没放稳，里面的球一股脑滚出来；人脚下一绊，翻着跌下去，都是 tumble。它常带着翻转、失去平稳的感觉。',
 '中古英语 tumblen 可能由旧 tumben 加反复动作尾，与古英语 tumbian 跃动、舞动相关，远源未定。不能把结尾 -ble 直接认作现代 -able 能够。',TUMBLE,
 'tumble down the stairs 从楼梯上跌滚下来；take a tumble 跌一跤；prices tumble 价格急跌。',
 'tumble out of a bag 从包里滚落出来；tumble into bed 倒上床。',
 'fall 泛指掉落，tumble 更容易让人看到翻滚、失去平稳；价格 tumble 则借急跌画面，不表示数字实际转圈。',
 ('The apples began to tumble out of the torn bag.','苹果开始从破袋子里滚落出来。'),('She took a tumble on the icy path.','她在结冰的小路上摔了一跤。'),sources=S('tumble','tumble'))
W('tumbles','/ˈtʌmbəlz/','翻滚、跌倒、急跌〔第三人称单数〕；翻滚、跌跤〔复数〕',
 '小狗扑得太急，翻个跟头，是 it tumbles；练滑冰摔的那几跤，则是 a few tumbles。别把复数和动词形式只凭外形混为一谈。',
 'tumble + -s，/l/ 后读 /z/；动词三单、名词复数同形，名词说具体的一次次跌滚。',TUMBLE+[['tumble + -s → tumbles','它翻滚、急跌；多次跌滚']],
 'takes a few tumbles 摔几跤；tumbles down 滚落下来。',
 'a puppy tumbles；tumbles in prices 价格急跌。',
 'tumbles 常有意外跌滚的感觉；somersaults 明确说翻筋斗，可能是训练好的主动动作。具体 tumble 也可用于体操。',
 ('The puppy tumbles onto its back during play.','小狗玩着玩着，翻倒得四脚朝天。'),('A few tumbles did not stop her from learning to skate.','摔了几跤，也没阻止她继续学滑冰。'),sources=S('tumbles','tumble'))
W('tumbled','/ˈtʌmbəld/','翻滚、跌落了；急跌了；倒下了',
 '纸箱一开，东西乱滚出来；辛苦一天后，人扑到床上，过去发生了这些动作，都能用 tumbled。',
 'tumble 去不发音 e 加完整 -ed；/l/ 后读 /d/，词干本有的 /əl/ 不属于后缀额外添出的音节。',TUMBLE+[['tumble + -ed → tumbled','过去翻滚、跌落或急跌']],
 'tumbled out 滚落、涌出；tumbled down 跌滚下来；tumbled into bed 倒上床。',
 'shares tumbled 股价急跌；words tumbled out 话一股脑冒出。',
 'tumbled into bed 写疲惫或匆忙地倒上床，went to bed 中性地说去睡觉；动作的劲头不同。',
 ('Coins tumbled out of his pocket.','硬币从他口袋里滚落出来。'),('After the long journey, we tumbled into bed.','长途旅行之后，我们一头倒上床。'),sources=S('tumbled','tumble'))
W('tumbling','/ˈtʌmblɪŋ/','正在翻滚、跌落；翻腾动作、技巧翻腾',
 '石头翻着滚下坡，是 tumbling；体操里连贯地做翻腾动作，也叫 tumbling。这里不一定摔倒，也可能是练好的动作。',
 'tumble 去不发音 e 加 -ing，常读 /ˈtʌmblɪŋ/。相关动作名词在中古英语已有翻腾、技巧舞动义。',TUMBLE+[['tumble + -ing → tumbling','翻滚的过程；作为活动的技巧翻腾']],
 'tumbling down 滚落下来；tumbling classes 翻腾技巧课；tumbling prices 急跌的价格。',
 'send stones tumbling 使石头滚落；practise tumbling 练习翻腾。',
 'tumbling 是翻腾活动时，可以在控制下完成；stumbling 常是脚下一绊，不能把二者都粗译为失足。',
 ('Loose stones came tumbling down the hillside.','松动的石头沿山坡翻滚下来。'),('The children practise tumbling on soft mats.','孩子们在软垫上练习翻腾动作。'),sources=S('tumbling','tumbling'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgx',ROOTS,WORDS)
 extend_lessons()
