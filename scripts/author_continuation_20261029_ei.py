"""Follow, luck and figure extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
F=[['古英语 folgian → 中古英语 folwen → follow','跟随、追随'],['现代 follow','沿路或人物移动 → 遵守、理解、持续关注']]
W('follow','英 /ˈfɒləʊ/；美 /ˈfɑːloʊ/','跟随；遵循；理解；关注',
 '脚步可以跟着人，做法可以跟着指示，思路也可以跟着别人的解释走。',
 '继承古英语 folgian 跟随词。现代实体移动与抽象遵循、理解、持续关注并用，不从拼写硬凑别的词根。',F,
 'follow the path 沿路走，follow instructions 照指示做，I do not follow 没听懂思路；follow someone online 在网上关注某人。',
 'follow instructions；follow a path；follow an argument；follow online。',
 'follow 理解强调跟上思路，不一定真的跟踪人；follow someone 与 follow someone’s advice 宾语改变，动作也不同。',
 ('Follow the path until you reach the river.','沿着小路走，直到河边。'),('Sorry, I do not follow your argument.','不好意思，我没跟上你的论证思路。'))
W('follower','英 /ˈfɒləʊə/；美 /ˈfɑːloʊər/','追随者；支持者；社交平台关注者',
 '有人在行动、思想上跟着一个人，也有人只是点击关注、接收更新。',
 'follow + -er，形成执行跟随的主体名词。现代社交平台义沿用持续关注，不代表每位关注者都忠诚支持。',F+[['follow + -er → follower','跟随者 → 支持者、平台关注者']],
 'a loyal follower 忠实追随者，social media followers 平台关注者；gain followers 增加关注者。',
 'a loyal follower；gain followers；social media followers。',
 'follower 平台关注者与 fan 粉丝不同，关注也可能为工作、研究或好奇。',
 ('The writer gained many followers after the interview.','作家在访谈后增加了许多关注者。'),('The leader expected unquestioning loyalty from his followers.','领导者要求追随者毫无质疑地忠诚。'))
W('unfollow','英 /ʌnˈfɒləʊ/；美 /ʌnˈfɑːloʊ/','取消关注',
 '先前订阅了某个账号的更新，现在撤掉这层关注关系。',
 'un- 逆转、解除 + follow，现代平台动词。不是暂时没有看一条消息，而是取消相应关注。',F+[['un- + follow → unfollow','解除关注 → 取消关注']],
 'unfollow an account 取消关注账号；unfollow someone 并不一定等于 block 屏蔽对方。',
 'unfollow an account；unfollow someone；decide to unfollow。',
 'unfollow 取消关注，unsubscribe 取消订阅，block 阻止互动或访问；功能具体取决于平台。',
 ('I unfollowed the account because it posted too often.','账号更新太频繁，我就取消关注了。'),('You can unfollow someone without blocking them.','你可以取消关注某人，而不屏蔽对方。'))
R('B3634','跟随、遵循与关注','FOLLOW：脚步、做法、思路都能跟上','从实际跟随走到指令、思路与平台关注，再接 follower、unfollow。',
 '古英语继承词的现代扩展很直观，但平台关注不自动等于忠诚拥护。',
 'follow → follower；un- + follow → unfollow。',
 [['动作、人物与解除动作','follow · follower · unfollow']],
 'I do not follow 可以说没理解；follower 不一定粉丝；unfollow 不等于 block。',
 'Some followers unfollowed the account after the change.\n\n改动后，一些关注者取消了关注。',
 'follow follower unfollow')
L=[['中古荷兰语或中古低地德语运气词 → 中古英语 luk、lukke','运气、命运；更远来源不明确'],['现代 luck','偶然带来的结果 → 幸运或不幸的状态']]
W('luck','/lʌk/','运气；偶然的机遇',
 '事情顺不顺，有一部分不是你能控制的，这一部分常叫运气；luck 本身可好可坏。',
 '借中古荷兰语或中古低地德语相关词，远源不明确。把运气解释成机会缺口是推测，不讲成确定构词事实。',L,
 'good luck 好运，bad luck 坏运气，with any luck 运气好一点的话；try your luck 试试运气。',
 'good luck；bad luck；with any luck；try your luck。',
 'luck 不可数为主，不把许多好运说 many lucks；Good luck! 是祝愿，不是保证结果。',
 ('Good luck with your interview!','祝你面试顺利！'),('Finding the last ticket was pure luck.','找到最后一张票纯属运气。'))
W('lucky','/ˈlʌki/','幸运的；带来好运的',
 '事情恰巧向有利方向发展，或某件物品被人当作好运象征。',
 'luck + -y，形成有好运的形容词。a lucky charm 说被认为带好运的物品，不断言它真的影响结果。',L+[['luck + -y → lucky','有好运 → 幸运；被视为带好运']],
 'be lucky to do 很幸运能做，a lucky escape 侥幸脱险，a lucky number 幸运数字。',
 'be lucky to；a lucky escape；a lucky number。',
 'lucky 幸运，luckless 不走运；lucky 强调偶然有利，不等于所有成功都不靠努力。',
 ('We were lucky to find seats on the train.','我们很幸运在火车上找到了座位。'),('She always carries a lucky charm.','她总带着一个被她当作好运象征的小挂件。'))
W('luckless','/ˈlʌkləs/','不走运的；倒霉的',
 '事情总不巧地对这个人不利，语气常带一点同情。',
 'luck + -less 缺乏，成词后通常指缺少好运，而不是数学上完全没有任何随机因素。',L+[['luck + -less → luckless','缺好运 → 不走运的']],
 'a luckless traveller 倒霉旅客，the luckless team 不走运的队伍；比 unlucky 更有书面叙述感。',
 'a luckless traveller；a luckless attempt；the luckless team。',
 'luckless 不走运，不是 careless 粗心；损失可能源于意外，不自动源于疏忽。',
 ('The luckless traveller missed the last bus by a minute.','那位倒霉旅客差一分钟错过了末班车。'),('The luckless team lost another match to a late goal.','那支不走运的球队又因最后时刻失球输了一场。'))
W('potluck','/ˌpɒtˈlʌk/；美 /ˈpɑːtlʌk/','各自带菜的聚餐；有什么吃什么',
 '早期是锅里碰巧有什么就吃什么；现代常是一人带一道菜，凑出一顿聚餐。',
 'pot 锅 + luck 运气，先有现成饭菜的碰运气说法，再有各带食物的共同餐食义。不把它误说成原住民 potlatch 的直接借词。',L+[['pot + luck → potluck','锅里有什么吃什么 → 各自带菜聚餐']],
 'a potluck dinner 各带菜聚餐，bring a dish to the potluck 带一道菜参加聚餐；take potluck 也可说听凭现成情况。',
 'a potluck dinner；a potluck lunch；bring a dish to a potluck。',
 'potluck 聚餐的菜来自参与者，buffet 自助餐说取餐方式；两者可同时成立，但不是同义。',
 ('Everyone brought a dish to the potluck dinner.','大家各带一道菜来参加聚餐。'),('We are having a potluck lunch at the office on Friday.','周五办公室要办一场各自带菜的午餐聚会。'))
R('B2724','运气与碰巧现成的餐食','LUCK：自己不能完全控制的顺与不顺','基本 luck 之后读 lucky、luckless；potluck 从锅里现成的食物讲到大家带菜。',
 '借低地地区日耳曼运气词，远源未定。potluck 可按 pot 和 luck 解释，不借相似外语词编来源。',
 'luck → lucky、luckless；pot + luck → potluck。',
 [['基本词与状态','luck · lucky · luckless'],['餐食习俗','potluck']],
 'luck 可好可坏，lucky 已偏好运；potluck 不等于所有自助餐。',
 'With any luck, everyone will bring something different to the potluck.\n\n运气好的话，大家会给聚餐带来不同的菜。',
 'luck lucky luckless potluck')
FI=[['拉丁 figura 形状 ← fingere 塑形 → 法语 figure → 英语 figure','形状、图像、人物、数字等分支'],['现代 figure 派生','有图案、被计算的；微型人物模型']]
W('figured','英 /ˈfɪɡəd/；美 /ˈfɪɡjərd/','figure 的过去形式；有图案、纹理的',
 '在 I figured it out 里是想明白了；figured silk 里则是丝绸上有花纹，两条用法要分开。',
 'figure + -ed，形成过去式、分词和形容词。动词计算、推断与图案装饰的不同分支，各自保留在搭配中。',FI+[['figure + -ed → figured','想出、推断的过去形式；带图案的']],
 'figured out 想明白，figured silk 提花丝绸，figured wood 有纹理图案的木材。',
 'figured out；figured silk；figured wood。',
 'figured out 是动词短语，不是有图案的外面；不能只凭 figured 一个词把所有句子译成计算过。',
 ('I finally figured out why the door would not close.','我终于弄明白门为什么关不上。'),('The curtains were made of figured silk.','窗帘用带花纹的丝绸做成。'))
W('minifigure','英 /ˈmɪnɪfɪɡə/；美 /ˈmɪnifɪɡjər/','迷你人偶；小人物模型',
 '把一个人物缩成小模型，玩具积木套装里尤其常见。',
 'mini- 小型 + figure 人物、模型，组合成小人偶名。不是小号数学数字的唯一说法。',FI+[['mini- + figure → minifigure','小型人物模型 → 迷你人偶']],
 'a toy minifigure 玩具小人偶，a collectible minifigure 收藏人偶；品牌、套装可能有具体称法。',
 'a toy minifigure；a collectible minifigure；a minifigure collection。',
 'minifigure 与 figurine 小雕像都可指小人物造型，前者更常见于玩具模型语境。',
 ('The building set includes three minifigures.','这套拼搭玩具里有三个小人偶。'),('She placed a minifigure beside the model station.','她把一个小人偶放在车站模型旁。'))
R('B3533','塑形词族的图案与小模型扩展','FIGURE：形状、人物、数字与推断在不同搭配中分开','已有 figure、figurine、figurehead 一起读，接 figured 的两条用法与 minifigure 小人偶。',
 '词族经法语接拉丁塑形、形状词。现代想明白不必画成真实捏泥，也不能把一切 figure 都译数字。',
 'figure → figured、figurine；figure + head → figurehead；mini- + figure → minifigure。',
 [['基本词与过去形式','figure · figured'],['小模型与代表人物','figurine · minifigure · figurehead']],
 'figured out 想明白，figured silk 有图案丝绸；minifigure 是玩具小人偶的常见称呼。',
 'She figured out how to assemble the minifigure.\n\n她弄明白了怎样组装小人偶。',
 'figure figured figurine minifigure figurehead')
if __name__=='__main__':save('continuation_20261029_ei',ROOTS,WORDS)
