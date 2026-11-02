"""Spy: seeing secretly and roles, acts, software, equipment."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['法兰克语等日耳曼语的观察相关形式 → 古法语 espier','观察、窥探'],['中古英语 espien／spien → spy','窥探、暗中搜集信息；也可说看到、发现']]
W('spy','/spaɪ/','间谍；暗中监视、搜集信息；看到、发现',
 '躲在对方不知情的地方观察、搜集消息，是 spy 的典型画面。但 spy a house in the distance 也能只是远远看见一座房子。',
 '经古法语 espier、中古英语 espien、spien，前面的弱读音节省去，形成 spy。法语这条线本身联系日耳曼语观察词源，不是所有法语借词都起于拉丁语。',S,
 'a spy novel 间谍小说，spy on someone 暗中监视某人，spy a familiar face 看见一张熟悉的脸。名词复数 spies，动词过去式 spied，但 spying 保留 y。',
 'a spy novel；spy on；spy a familiar face。',
 'spy on 常突出暗中窥探；watch 更普通。及物 spy a bird 可以只是看到一只鸟，不必每次都有间谍活动。',
 ('She enjoys reading spy novels.','她喜欢读间谍小说。'),('We spied a small café at the end of the street.','我们看见街尾有一家小咖啡馆。'))
W('spying','/ˈspaɪɪŋ/','间谍活动、暗中搜集信息；正在窥探',
 'spy 可以说人或动作，spying 则把暗中观察、搜集信息当作正在发生的事或整个行为来谈。',
 'spy + -ing，接中古英语 spyinge 等旧形式。y 在这里保留；不是每次见 -ing 都必须翻成正在。',S+[['spy + -ing → spying','暗中搜集信息这一行为；进行中的动作']],
 'accused of spying 被指控从事间谍活动，spying on a rival 暗中监视对手，a history of spying 间谍活动史。',
 'accused of spying；spying on；a history of spying。',
 'spying 可是名词，spying on someone 也可处于动词结构。public observation 公开观察不因看了别人就自动是 spying。',
 ('The documentary explores the history of spying.','纪录片探讨了间谍活动的历史。'),('The character discovers that someone has been spying on him.','这个角色发现有人一直在暗中监视他。'))
W('spyware','英 /ˈspaɪweə/；美 /ˈspaɪwer/','间谍软件',
 '软件在用户不知情时悄悄记录、报告活动，像躲在设备里的窥探者，因此叫 spyware。',
 'spy + -ware；-ware 取自 software 等软件名称的构词用法。把暗中搜集信息这一行为借给程序，不是有一个小人真的藏在里面。',S+[['spy + -ware → spyware','暗中监视、报告用户活动的程序类别']],
 'detect spyware 检测间谍软件，remove spyware 清除间谍软件，spyware detection 间谍软件检测。通常作不可数集合性名称，不把每个程序都常规说 a spyware。',
 'detect spyware；remove spyware；spyware detection。',
 'spyware 按暗中监控功能命名，virus 按特定传播、复制机制命名；不能把所有恶意软件都当同一种病毒。',
 ('The scan detected spyware on the computer.','扫描在电脑上发现了间谍软件。'),('The article explains how spyware can record a user’s activity.','文章解释了间谍软件如何记录用户活动。'))
W('spymaster','英 /ˈspaɪmɑːstə/；美 /ˈspaɪmæstər/','间谍首脑；谍报负责人',
 '不是亲自看见东西的人，而是组织、指挥一批间谍的人。master 在这里表示统领、负责人。',
 'spy + master，按负责指挥间谍群体的关系组合。与 spyglass 的 glass 器具部分、spyware 的软件部分分开理解。',S+[['spy + master → spymaster','组织、指挥间谍活动的人物']],
 'a fictional spymaster 小说中的谍报首脑，the spymaster’s network 谍报负责人的情报网络。历史、新闻及谍战作品常见。',
 'a fictional spymaster；the spymaster’s network。',
 'spy 是搜集情报者，spymaster 强调管理、指挥角色；并非每个资历老的 spy 都一定领导一个网络。',
 ('The novel’s spymaster rarely appears in public.','小说里的谍报首脑很少公开露面。'),('The biography describes the spymaster’s network of agents.','传记描述了这位谍报负责人的特工网络。'))
R('B3942','观察、暗中搜集信息，以及行为、负责人和软件器具','SPY：观察可以是发现，也可以是秘密窥探','spy → spying；spymaster 看指挥者；spyware 看程序；spyglass 看观察器具。',
 '前半都保留观察的联系，后半说明人、过程、软件还是器具。spy 本身也有单纯看到的用法。',
 '日耳曼语观察词源经古法语 espier、中古英语 espien／spien → spy；再与 -ing、master、-ware、glass 组合。',
 [['人物、动作与过程','spy · spying · spymaster'],['软件与观察器具','spyware · spyglass']],
 'spy on 与 spy a familiar face 语义不同；spyware 不等于所有 virus。',
 'The spy novel follows a spymaster whose agents uncover spying through software.\n\n这部间谍小说讲述一位谍报首脑手下的特工发现软件监视活动。','spy spying spymaster spyware spyglass')
if __name__=='__main__':save('continuation_20261030_jh',ROOTS,WORDS)
