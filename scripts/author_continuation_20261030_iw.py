"""Tongue, deriving from a source, and separate tap histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['古英语 tunge → 中古英语 tunge/tonge → tongue','舌头；说话、语言这一用法也很早'],['按作用或形状扩展','母语、说话方式；鞋舌、火舌、突出片等'],['历史拼写与现代读音','常见标准读音 /tʌŋ/，不逐字念出 -gue']]
W('tongue','/tʌŋ/','舌头；语言、说话方式；鞋舌、舌状突出物',
 '嘴里那块会动的舌头帮助发声，便能代指语言；鞋带下面那片伸出的材料形似舌头，就叫鞋舌。',
 '接古英语 tunge。中古拼写逐渐出现 tongue，历史字母变化不能直接当现代读音指南；普通标准读音是 /tʌŋ/，并非 /tɒŋɡjuː/。',T,
 'stick out your tongue 伸舌头，mother tongue 母语，a sharp tongue 说话刻薄，the tongue of a shoe 鞋舌，on the tip of my tongue 话到嘴边却想不起来。',
 'mother tongue；a sharp tongue；the tongue of a shoe；on the tip of my tongue。',
 'mother tongue 是语言，不是母亲的生理舌头；tongue 也不按 tongs 夹子拆。hold your tongue 是别说话，on the tip of my tongue 常说想不起那个已很熟悉的词。',
 ('English is not her mother tongue.','英语不是她的母语。'),('His name is on the tip of my tongue.','他的名字就在我嘴边，可我一下想不起来。'),('The tongue of the shoe had folded under the laces.','鞋舌折到了鞋带下面。'),sources=['https://en.wiktionary.org/wiki/tongue#English','https://www.etymonline.com/word/tongue'])
R('B2768','发声器官借指语言，形状借指突出片','TONGUE：嘴里会动的舌，也能指说的语言','tongue → 器官、语言和按舌状外形命名的部件；固定搭配各看整句。',
 '把语言当成舌头的作用，把鞋舌、火舌当成外形。两种扩展容易直观看懂，但拼写 tongue 不能逐字硬读。',
 'tunge → tunge/tonge → tongue；现代常见读音 /tʌŋ/。',
 [['器官、语言与形似部件','tongue']],
 'mother tongue 母语；hold your tongue 少说、别说；tip of my tongue 常指一时想不起来。',
 'The phrase was on the tip of my tongue, but I could not recall it even in my mother tongue.\n\n那个说法就在嘴边，可我连用母语都一下想不起来。','tongue')
D=[['拉丁 dē- 离开 + rīvus 溪流 → dērīvāre','把水从原来的河流引出、导向别处'],['法语 deriver → 英语 derive','从源头而来、取得；后来可由依据推导'],['平行名词借入与英语形态','dērīvātiō / dérivation → derivation；derive + -ed → derived']]
W('derive','/dɪˈraɪv/','来自、源于；从中获得；推导出',
 '沿一条水渠追上去，能找到原来的溪流。词义借到来源：快乐从工作中来，结论从证据中来，单词也能从旧词形发展而来。',
 '借法语 deriver，接拉丁 dērīvāre，dē- 从、离开 + rīvus 溪流。现代 rive 不当作单独河流词硬拆，更不是 de- + drive。',D,
 'derive from Latin 源自拉丁语，derive pleasure from music 从音乐中获得快乐，derive a formula 推导公式，derive a conclusion from evidence 根据证据推导结论。',
 'derive from；derive pleasure from；derive a formula。',
 'A derives from B 是 A 来源于 B；derive A from B 是从 B 得到 A。arrive 到达有自己的岸边词源路线，不是把 derive 的前缀换一下就直接形成。',
 ('The word derives from Latin.','这个词源自拉丁语。'),('She derives great satisfaction from teaching.','她从教学中获得很大的满足感。'),sources=['https://en.wiktionary.org/wiki/derive#English','https://www.etymonline.com/word/derive'])
W('derived','/dɪˈraɪvd/','由……得来、派生的；推导出的；演化而来的〔相对祖先性状〕',
 '不是凭空冒出，而是有一条来源路径。计算后的 derived value 来自原数据，derived word 来自相应词基的构词过程。',
 'derive 去 e + -ed，末尾 /vd/，不额外加 /ɪd/。作分词或形容词说明获得、派生关系；演化分类中又有相对祖先状态的专门用法。',D[:2]+[['derive + -ed → derived','已经从某来源得出、形成的；相关专门性状概念']],
 'derived data 派生数据，a derived value 计算所得值，a derived word 派生词，derived from natural materials 由天然材料提取或制得。',
 'derived data；a derived value；a derived word；derived from。',
 'derived 不保证来源与产物完全相同，也不证明结果天然更好。生物学 derived 相对祖先状态说变化，不是优劣排名。',
 ('The table includes both original and derived values.','表格同时列出原始值和计算所得值。'),('The dye is derived from plant material.','这种染料从植物材料中提取制得。'))
W('derivation','/ˌderɪˈveɪʃən/','来源、词源形成；派生构词；推导过程',
 'derive 是从哪里来、怎样得出，derivation 就把这条来路或推导步骤拿出来。词源研究看历史，数学看推导，构词学看怎样造新词。',
 '经法语 dérivation 接拉丁 dērīvātiō，来自 dērīvāre 的过程名词。现代对应 derive 与 -ation，但名词有平行借入史，不只在英语里现场接词尾。',D[:2]+[['dērīvātiō → 法语 dérivation → derivation','引出、导出过程 → 来源、构词派生、推导']],
 'the derivation of a word 一个词的来源，a mathematical derivation 数学推导，derivation by suffixation 通过加后缀派生新词。',
 'the derivation of a word；a mathematical derivation；derivation by suffixation。',
 'derivation 在构词学常指形成新词，walks、walked 这类时态、人称变化通常讨论 inflection 屈折；历史来源解释又不等于每个单词都能按现代英语规则重新造一遍。',
 ('The dictionary explains the derivation of the word.','词典解释了这个词的来源。'),('The appendix gives a step-by-step derivation of the formula.','附录逐步给出了公式的推导。'),sources=['https://en.wiktionary.org/wiki/derivation#English','https://www.etymonline.com/word/derive'])
R('B3196','从溪流引出，借来理解来源、取得与推导','DERIVE：从一个源头流出来、拿出来','derive → derived；derivation 说来路、构词派生或推导过程。',
 '物质从原料来，词从旧词形来，结论从依据来。每次先找到 from 后面的源头，再看得到的是什么。',
 'dē- + rīvus → dērīvāre → deriver → derive；dērīvātiō → derivation；derive 接 -ed。',
 [['来源动作、所得状态与过程','derive · derived · derivation']],
 'derive from 与 derive A from B 分清方向；derived 不保证原物与产物相同；构词 derivation 与普通屈折变化分开。',
 'The derivation shows how the final value is derived from the original data.\n\n推导过程展示了最终值如何从原始数据中得到。','derive derived derivation')
A=[['塞子与放流路线：古英语 tæppa / tæppian → tap','桶塞、龙头；放出液体 → 取用资源、接入通信'],['轻敲路线：中古英语 tappen 等 → tap','轻敲、拍碰，可能拟声，也有法语等相关形式影响'],['固定名称和组合词','taproom 接放酒龙头；Taps 熄灯号名称另有 taptoo 等分析']]
W('tap','/tæp/','轻敲、轻触；水龙头；取用、开发；接入窃听；指定某人',
 '手机上轻触一下是 tap；水从龙头放出来也是 tap。前者看轻敲动作，后者看开口放流，历史不必硬合成点一下就出水。',
 '龙头、放流义接古英语 tæppa、tæppian，借到利用资源、接入线路。轻敲义接中古英语 tappen，可能拟声或受法语等影响；两条直接来源分别看。',A,
 'tap the screen 轻点屏幕，tap on a window 轻敲窗，turn off the tap 关水龙头，tap into local knowledge 利用当地知识，tap someone for a role 选某人担任角色。',
 'tap the screen；tap on；turn off the tap；tap into；tap someone for。',
 '英式 tap 水龙头常对应美式 faucet；tap into 常是利用、接入，不是真敲打一池资源。on tap 可指桶装放出的饮品，也比喻随时可用。',
 ('Tap the icon to open the menu.','轻点图标打开菜单。'),('The project taps into local knowledge.','项目利用当地人的知识。'),('Please turn off the tap.','请关掉水龙头。'),sources=['https://en.wiktionary.org/wiki/tap#English','https://www.etymonline.com/word/tap'])
W('taproom','英 /ˈtæpruːm/；美 /ˈtæpˌruːm/','供应桶装酒的酒吧间、酒厂品饮空间',
 'tap 在这里是放酒的龙头，不是轻敲。酒厂里对顾客开放、供应自家酒的空间，常叫 taproom。',
 'tap 放酒龙头 + room 房间，按服务功能组合。现代 taproom 可以是酒厂附设空间，也可更广指相应酒吧间。',A[:1]+[['tap + room → taproom','供应从龙头放出饮品的空间']],
 'a brewery taproom 酒厂附设酒吧间，a small taproom 小酒吧间，the taproom menu 酒吧间菜单。',
 'a brewery taproom；the taproom menu。',
 'taproom 不是装满自来水龙头的洗手间，也不等于整座 brewery 酿酒厂；一个是面向顾客的空间，一个是生产场所或企业。',
 ('The brewery opened a small taproom beside the production hall.','酒厂在生产车间旁开了一间小酒吧。'),('The taproom menu lists several locally made beers.','酒吧间的菜单列出了几款当地酿造的啤酒。'))
W('taps','/tæps/','熄灯号；美军仪式中的安息号〔Taps〕；另有 tap 的普通复数、动词形式',
 '故事里夜间军号响起，或纪念仪式上吹奏 Taps，通常指一种特定号音。two taps 则可能只是两个水龙头、两下轻敲，别混成同一含义。',
 '普通 taps 是 tap + -s。军号名称有联系 tap 鼓击的解释，也常被分析为旧 taptoo、tattoo 熄灯信号名称的变化，不能只凭末尾 s 判成多个现代龙头。',
 [['普通 tap + -s → taps','复数；或第三人称单数动词'],['军事信号名 taps / Taps','来源有鼓击、旧 taptoo 等分析；现指固定熄灯号及相关仪式号音'],['今日熟知的号曲发展','1862 年巴特菲尔德和号手诺顿调整旧号音后传播']],
 'sound taps 吹熄灯号、安息号，play Taps at a ceremony 仪式上吹奏 Taps；two taps 两个龙头或两下敲击；she taps 她轻敲。',
 'sound taps；play Taps；two taps；she taps。',
 'Taps 曲名不能按水龙头义翻译。名称历史与曲调发展分开；这首号曲由旧军号改编，流行的战场父子遗曲故事不当作确定起源。',
 ('The bugler played Taps at the memorial ceremony.','号手在纪念仪式上吹奏了安息号。'),('She gave two taps on the door.','她在门上轻敲了两下。'),sources=['https://en.wiktionary.org/wiki/taps#English','https://www.merriam-webster.com/dictionary/taps','https://www.va.gov/opa/publications/celebrate/taps.pdf'])
R('B3350','轻敲与塞子放流的两条来源，另辨军事号名','TAP：屏幕看轻触，龙头看放流','tap 轻敲 → 常规 taps；tap 龙头、放流 → taproom / wiretap；Taps 是固定军事名称。',
 '从桶里放出酒，再借到从资源里取得东西、接入通信线路，很容易理解。轻敲动作另看；军号名的形成也不只是一条现代复数规则。',
 'tæppa/tæppian → tap 龙头、放流；tappen 等 → tap 轻敲；tap + room、wire + tap；taps 军号名另有旧词形变化。',
 [['常用基础词与形式','tap · taps'],['服务空间和通信组合','taproom · wiretap']],
 'taproom 不是洗手间；tap into 常说利用；Taps 军号名与普通复数、动词 taps 分开。',
 'She tapped the menu icon to read about the brewery’s taproom.\n\n她轻点菜单图标，查看酒厂附设酒吧间的介绍。','tap taps taproom wiretap')
if __name__=='__main__':save('continuation_20261030_iw',ROOTS,WORDS)
