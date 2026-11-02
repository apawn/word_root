"""Common scientific adjectives and familiar -y nouns."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1771':dict(words=['base','basal','fetus','fetal','artery','arterial','mitochondrion','mitochondria','mitochondrial'],label='基部、胎儿、动脉与线粒体：科学名称的关系形容词',note='base + -al → basal；fetus 的词干 fet- + -al → fetal；arterial 历史有法语借入，同时与 artery 的词干构词对应；mitochondria 与 -al 形成 mitochondrial。不能把这些形容词都译成模糊的某某性质。'),
 'A1699':dict(words=['bunny','bully'],label='熟悉称呼及后来的词义变化',note='bunny 接较早兔的亲昵称呼 bun 与小称 -y，旧 bun 的更远来源未定；bully 早期也有亲昵称呼背景，可能与荷兰语 boel 等相连，不能径直断成 bull + -y。'),
 'A1741':dict(words=['bully','bullying'],label='欺负的基础词与行为名称',note='bully 是名词、动词基础；bullying 已在本页精讲，补齐基础词便于连着读。'),
 'A1760':dict(words=['bully','bullied'],label='被欺负、被胁迫的状态',note='bully + -ed → bullied，辅音字母加 y 结尾时把 y 改为 i；bully into 与 bully out of 的方向分别见例句。'),
}
W('basal','/ˈbeɪsəl/〔也见 /ˈbeɪzəl/〕','基部的、底层的；基础水平的',
 '把目光放到最下面、最基础的一层。植物基部、组织底层，或维持基本运行的水平，都可能用 basal。',
 'base 基础、底部 + -al 相关的，形成关系形容词。科学语境常把底部、基本水平表达得比普通 basic 更具体。',
 [['base 底部、基础 + -al','与基部、底层有关的'],['basal 在科学描述中的使用','基部位置；基础状态或水平']],
 'basal leaves 基生叶、长在植株基部的叶；the basal layer 基底层；basal metabolic rate 基础代谢率。',
 'the basal part of the stem；basal activity。','basic 常说基础、基本的，范围很广；basal 常指具体基部、底层或特定基础水平。basic English 通常不改成 basal English。',
 ('The plant has a cluster of basal leaves.','这株植物的基部簇生着一丛叶子。'),('The diagram labels the basal layer of the tissue.','图解标出了该组织的基底层。'),sources=['https://www.etymonline.com/word/basal','https://en.wiktionary.org/wiki/basal#English'])
W('fetus','/ˈfiːtəs/','胎儿',
 '指还在子宫内发育的后代。现代生物学、医学里常用来称胚胎期之后、出生之前的发育阶段。',
 '从拉丁语 fetus 后代、产物等书面借入。较宽的后代、孕育材料进入现代术语后，具体用于胎儿阶段。',
 [['拉丁语 fetus 后代、产物等','孕育、出生相关的旧名词'],['英语 fetus 的现代术语义','子宫内发育的胎儿']],
 'the developing fetus 发育中的胎儿；a human fetus 人类胎儿；fetus 的常见复数 fetuses。英式也见 foetus。',
 'fetus and embryo；development of the fetus。','embryo 是更早的胚胎阶段，fetus 是之后的胎儿阶段。两词在科学描述中有阶段区别，不能一律当同义词替换。',
 ('The textbook explains how the fetus develops.','教材解释了胎儿怎样发育。'),('The diagram shows the position of the fetus in the uterus.','图解展示了胎儿在子宫内的位置。'),sources=['https://en.wiktionary.org/wiki/fetus#English','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/fetus'])
W('fetal','/ˈfiːtəl/','胎儿的、与胎儿有关的',
 'fetus 是胎儿这个名词；fetal 把它放到另一个名词前面，说明讨论的是胎儿的生长、心跳等。',
 'fetus 的词干 fet- + -al，形成关系形容词。英式相应拼写还见 foetal，发音相同。',
 [['fetus 的词干 fet- + -al','与胎儿有关的'],['fetal 作名词修饰语','胎儿发育、胎儿心跳等']],
 'fetal development 胎儿发育；fetal movement 胎动；fetal heartbeat 胎儿心跳。',
 'fetal growth；the fetal stage。','fetus 是名词，fetal 是形容词；fetal development 不能机械逐字换成 fetus development。foetal 是常见的另一拼写。',
 ('The chapter focuses on fetal development.','这一章重点讲胎儿发育。'),('The recording captured the fetal heartbeat.','这段记录录下了胎儿的心跳。'))
W('artery','英 /ˈɑːtəri/；美 /ˈɑːrtəri/','动脉；交通干线、大通道〔比喻〕',
 '把血从心脏送出去的血管叫 artery。城市里承载大量交通的主干道，也像输送流量的大血管。',
 '经法语及拉丁语 arteria，接希腊语 arteria 的气管、动脉等旧用法。英语现代主要保留动脉义，再扩展到主干输送通道。',
 [['希腊语 arteria → 拉丁语、法语 → 英语','较早身体管道名称进入英语'],['现代 artery 的解剖与通道比喻','动脉；交通、河流等主要通道']],
 'a major artery 一条大动脉，也可比喻重要干道；the coronary arteries 冠状动脉；traffic arteries 交通干线。复数 arteries。',
 'a main artery through the city；arteries and veins。','artery 按血流从心脏流出的方向理解；vein 通常联系回流到心脏。交通比喻里的 artery 突出主干输送作用。',
 ('The diagram shows an artery carrying blood away from the heart.','图解展示一条把血液从心脏送出的动脉。'),('This road is a major artery through the city.','这条路是穿过城市的一条重要交通干道。'),sources=['https://www.etymonline.com/word/artery','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/artery','https://en.wiktionary.org/wiki/artery#English'])
W('arterial','英 /ɑːˈtɪəriəl/；美 /ɑːrˈtɪriəl/','动脉的；干线的、主干通道的',
 'artery 叫动脉或主干道；arterial 把这层关系放到前面：arterial blood 是动脉血，arterial road 是交通干道。',
 '历史有法语 arterial 等借入，与拉丁语 arteria 相连；现代可按 artery 的词干 arteri- 与 -al 认识其关系形容词结构。',
 [['arteria 词族与法语相关形容词 → 英语 arterial','动脉的、与动脉有关的'],['arterial 的交通比喻','承担主干输送作用的、干线的']],
 'arterial blood 动脉血；arterial pressure 动脉压力；an arterial road 一条主干道。常作名词前的修饰语。',
 'the arterial system；arterial traffic。','artery 是名词，arterial 是形容词。主干道的比喻强调输送和分支关系，并不表示道路和血管结构完全一样。',
 ('The chart compares arterial and venous blood.','图表对比了动脉血和静脉血。'),('The new arterial road connects the outer districts.','新建主干道把外围几个城区连接起来。'),sources=['https://www.etymonline.com/word/artery','https://en.wiktionary.org/wiki/arterial#English'])
W('mitochondria','英 /ˌmaɪtəˈkɒndriə/；美 /ˌmaɪtoʊˈkɑːndriə/','线粒体〔mitochondrion 的复数〕',
 '细胞里参与能量转换的一类小结构，常被形象地叫作供能站。mitochondria 说复数，mitochondrion 说一个。',
 '近代科学名称借助希腊语 mitos 丝、线与 chondrion 小颗粒构成，经德语术语传播。名字先描写显微观察中的丝状、颗粒状外观，后来功能研究更深入。',
 [['希腊语 mitos + chondrion → 近代科学命名','丝、线 + 小颗粒，描写观察到的形态'],['mitochondrion → mitochondria','现代英语的单数与复数形式']],
 'mitochondria in a cell 细胞内的线粒体；mitochondria have their own DNA 线粒体有自身 DNA。标准复数搭配 mitochondria are。',
 'many mitochondria；the membranes of mitochondria。','细胞供能站是帮助理解功能的比喻；词源中的丝、颗粒则描写形态。不要用后来发现的功能替换原来的命名理由。',
 ('The cell contains many mitochondria.','这个细胞内含有许多线粒体。'),('The lesson explains how mitochondria help supply energy to cells.','这一课解释线粒体怎样帮助细胞获得能量。'),sources=['https://www.etymonline.com/word/mitochondria','https://www.genome.gov/genetics-glossary/Mitochondria','https://en.wiktionary.org/wiki/mitochondria#English'])
W('mitochondrial','英 /ˌmaɪtəˈkɒndriəl/；美 /ˌmaɪtəˈkɑːndriəl/','线粒体的、与线粒体有关的',
 '看到 mitochondrial DNA，就把它读成线粒体里的 DNA；它说明所属位置、研究对象，不是另一类细胞的名字。',
 'mitochondria 与 -al 形容词材料组合，保留 mitochondri- 这一词干，形成与线粒体有关的修饰语。',
 [['mitochondrion、mitochondria 的线粒体词族','丝粒状结构的科学名称'],['mitochondri- + -al → mitochondrial','线粒体的']],
 'mitochondrial DNA 线粒体 DNA；mitochondrial membrane 线粒体膜；mitochondrial function 线粒体功能。',
 'mitochondrial genes；mitochondrial activity。','mitochondria 是复数名词，mitochondrial 是形容词。两者尾部变化承担当下语法功能，不是线粒体变成另一种东西。',
 ('The researchers compared mitochondrial DNA from several samples.','研究者比较了几个样本的线粒体 DNA。'),('The diagram labels the mitochondrial membranes.','图解标出了线粒体膜。'),sources=['https://www.genome.gov/genetics-glossary/Mitochondria','https://en.wiktionary.org/wiki/mitochondrial#English'])
W('bunny','/ˈbʌni/','兔子、小兔〔亲昵、儿童用语〕',
 '比 rabbit 更软、更亲昵，像中文说小兔兔。也常称兔形玩具、复活节兔子形象。',
 '较早苏格兰等方言的 bun 兔或小动物昵称 + 小称 -y；旧 bun 的更远来源仍有不同说法。这里不是由现代面包 bun 的形状推导。',
 [['较早动物昵称 bun + -y','形成亲昵、小称的称呼'],['现代 bunny','兔子、兔形玩具等的亲切叫法']],
 'a baby bunny 小兔；a toy bunny 兔子玩具；the Easter Bunny 复活节兔子。复数 bunnies。',
 'a fluffy bunny；a chocolate bunny。','rabbit 是通用动物名；bunny 常带亲昵、儿童语气，不是严格规定只有幼兔才能用。',
 ('The child hugged a soft toy bunny.','孩子抱着一只软软的兔子玩具。'),('A little bunny hopped across the garden.','一只小兔蹦跳着穿过花园。'),sources=['https://www.etymonline.com/word/bunny','https://en.wiktionary.org/wiki/bunny#English'])
W('bully','/ˈbʊli/','欺凌者；欺负、威逼',
 '仗着力量、地位或人数压别人，逼别人害怕、服从。名词说这个人，动词说他怎样对待别人。',
 '早期英语有亲爱的、好伙伴等褒义称呼，可能接荷兰语 boel 等材料，确切来源未定；后来经逞威风者等意思，发展为欺负弱者的人，并出现动词。',
 [['早期 bully 的亲昵称呼、好伙伴义','可能与荷兰语相关称呼相连'],['词义贬化与动词形成','逞威风者 → 欺凌者；欺负、胁迫']],
 'a school bully 校园里的欺凌者；bully someone into doing something 胁迫某人做某事；bully someone out of something 胁迫某人放弃某物。',
 'stand up to a bully；bully someone into agreeing。','bully 的历史不宜直接说成 bull 公牛 + -y。现代 tease 可指轻微逗弄，bully 常突出以强压弱的伤害、威逼。',
 ('The new student refused to give in to the bully.','新来的学生不肯向那名欺凌者屈服。'),('He tried to bully the others into accepting his plan.','他试图威逼其他人接受自己的计划。'),sources=['https://www.etymonline.com/word/bully','https://en.wiktionary.org/wiki/bully#English'])
W('bullied','/ˈbʊlid/','被欺负、被胁迫；bully 的过去式、过去分词',
 'someone was bullied 说一个人被欺负了；was bullied into agreeing 则说是在压力下被逼着同意。',
 'bully + -ed，末尾辅音字母加 y 的结构把 y 改为 i，写成 bullied；读音 /d/，不另添一个音节。',
 [['bully 欺负、威逼 + -ed','形成过去、过去分词形式'],['bullied 的主动过去与被动结构','欺负了；被欺负、被迫做某事']],
 'was bullied at school 在学校被欺负；bullied into silence 被威逼得不敢说话；bullied out of giving evidence 被胁迫而放弃提供证词。',
 'felt bullied；bullied into signing。','bullied 常说经历或被动状态，bullying 常说欺凌行为。bully into 是逼着去做，bully out of doing 是逼着不做。',
 ('He was bullied at his old school.','他在原来的学校受过欺负。'),('She refused to be bullied into signing the letter.','她拒绝在威逼下签署那封信。'))
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tn',ROOTS,WORDS)
    extend_lessons()
