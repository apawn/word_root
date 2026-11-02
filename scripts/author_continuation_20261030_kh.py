"""Edit, knight and worship."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
E=[['拉丁 ēdere、ēditus 等出版相关形式 → editor','把作品刊出、整理出版的人'],['editor → edit〔逆构〕','英语从较长的人物名称取出动词，也受法语 éditer 影响'],['edit + -able → editable','能够编辑、修改的']]
W('edit','/ˈedɪt/','编辑、修改；剪辑；编辑改动、剪辑版本',
 '原稿或素材放在那里，你修改内容、安排顺序、剪掉不需要的部分，让它适合使用，这个过程是 edit。',
 '英语从 editor 逆构出 edit，也受法语 éditer、拉丁 editus 等影响。今天可以按 edit → editor 学构词，但真实出现顺序不能直接倒过来讲。',E[:2],
 'edit a document 修改文档，edit a video 剪辑视频，edit a magazine 担任杂志编辑，make an edit 作一次编辑改动。',
 'edit a document；edit a video；make an edit。',
 'edit 可改内容、结构、语言或素材顺序；proofread 更集中检查文字差错。一次 edit 也可能是一个剪辑版本。',
 ('Please edit the introduction to make it clearer.','请修改引言，让意思更清楚。'),('He edited the footage into a short film.','他把素材剪成一部短片。'))
W('editable','/ˈedɪtəbəl/','可编辑、可修改的',
 '文件里的文字、表格能直接改动，便是 editable；截图上看得到字，却未必能像原文档一样编辑。',
 'edit + -able，表示能够接受编辑的性质。',E,
 'an editable file 可编辑文件，editable text 可编辑文字，an editable template 可编辑模板。',
 'an editable file；editable text；an editable template。',
 'editable 说能否编辑，readable 说能否读取、读懂。文件可读，不表示有编辑权限或内容结构方便改。',
 ('Please send an editable version of the document.','请发送可编辑版本的文档。'),('The names are editable, but the logo is fixed.','名称可以修改，但标志是固定的。'))
R('B3200','整理、修改文本与素材，形成可发布或可用的版本','EDIT：把现成内容整理、改成合用的样子','edit → editable；editor 是历史上先出现的人物名称。',
 '现代构词可以帮助记忆，历史顺序则要另说。edit 的直接英语来历是从 editor 逆构，不能只按长短猜先后。',
 '拉丁出版相关形式 → editor → 逆构 edit；-able 可编辑；edition、editorial 是同族相关词。',
 [['编辑动作与可编辑性质','edit · editable'],['人物、版本与编辑相关','editor · edition · editorial']],
 'edit 比校对范围广；editable 与 readable 不同；词短不保证历史更早。',
 'The editor asked for an editable file so she could edit the introduction.\n\n编辑要了一个可编辑文件，以便修改引言。','edit editable editor edition editorial')
K=[['古英语 cniht','男孩、侍从、服役者等旧义'],['中古英语 knight、knyght → knight','身份发展为骑士；现代另有爵位、棋子等用法'],['-hood、-ly 的扩展','身份、称号；骑士的、符合骑士风范的']]
W('knight','/naɪt/','骑士；获授骑士称号者；国际象棋中的马；授予骑士称号',
 '旧时的侍从、服役者称呼，逐渐走向骑士身份。现代可能谈中世纪战士、荣誉称号，或棋盘上像马头的棋子。',
 '古英语 cniht 经中古英语 knight、knyght 传下。旧开头的辅音群后来简化，现代 k、gh 不读，和 night 同音。',K[:2],
 'a medieval knight 中世纪骑士，a knight in shining armor 救助他人的理想人物，move a knight 移动马棋子，be knighted 获授骑士称号。',
 'a medieval knight；move a knight；be knighted。',
 'knight 今天不总是骑马作战的人。现代荣誉称号与历史军事身份、棋子名称，要看语境分辨。',
 ('The knight in the painting carries a shield.','画里的骑士拿着盾牌。'),('She moved her knight to the center of the board.','她把马走到棋盘中央。'))
W('knighthood','/ˈnaɪthʊd/','骑士身份、骑士称号；骑士阶层〔集合义〕',
 'knight 说人，knighthood 则把镜头转向这个人获得的身份、称号，也能合称骑士群体。',
 '承接古英语 cnihthād、中古英语 knyghthode 等，现代对应 knight + -hood。-hood 在这里表身份、状态，和 childhood 是同类后缀。',K[:1]+[['cnihthād → knyghthode → knighthood','骑士身份、称号；现代对应 knight + -hood']],
 'receive a knighthood 获授骑士称号，the ideals of knighthood 骑士风范的理想。具体授予制度由相应历史、地区语境决定。',
 'receive a knighthood；the ideals of knighthood。',
 'knighthood 是身份、称号等名词，knightly 是形容词。这里 hood 不指衣服上的帽兜。',
 ('The biography describes how he received a knighthood.','传记讲到他怎样获授骑士称号。'),('The exhibition explores medieval ideas of knighthood.','展览探讨中世纪的骑士观念。'))
W('knightly','/ˈnaɪtli/','骑士的；有骑士风范、彬彬有礼的',
 '可以描述骑士的装备、生活，也可以借理想骑士的形象说礼貌、勇敢、守信等风范。',
 '中古英语已有 knyghtly、knightlich 等，现代对应 knight + -ly。这里常用形容词后缀 -ly，历史上也有副词用法。',K[:2]+[['knight + -ly → knightly','与骑士有关；符合骑士理想风范']],
 'knightly armor 骑士铠甲，knightly virtues 骑士美德，knightly courtesy 骑士般的礼貌。多见历史、文学语境。',
 'knightly armor；knightly virtues；knightly courtesy。',
 'knightly manners 是骑士般的举止，不保证这个人真有 knight 身份。-ly 结尾也不保证一定是副词。',
 ('The hall displayed knightly armor and shields.','大厅陈列着骑士铠甲与盾牌。'),('The story praises courage and other knightly virtues.','故事赞美勇气等骑士美德。'))
R('B2602','从侍从、服役者走向骑士身份，再扩到称号、风范与棋子','KNIGHT：身份的历史变化，比现代字面拆分更重要','knight → knighthood、knightly。',
 '男孩、侍从等旧义并不等于现代骑士。沿身份演变理解，比把今天的 knight 倒推成所有时代都相同更清楚。',
 'cniht → knight；-hood 身份，-ly 相关性质、风范；现代 /naɪt/ 与 night 同音。',
 [['人物、身份与风范','knight · knighthood · knightly']],
 'knighthood 不是帽兜；knightly 常作形容词；knight 还有国际象棋棋子义。',
 'The tale describes a knight whose courtesy reflects the ideals of knighthood.\n\n故事描写一位骑士，他的礼貌体现了理想的骑士风范。','knight knighthood knightly')
P=[['古英语 weorðscipe 等','worth 价值、值得尊重 + -ship 状态：尊荣、敬重'],['worship 的宗教与敬仰用法','崇拜、敬拜；对人、事物的强烈仰慕'],['worshipful、worshipper','敬仰的／尊称；敬拜、崇拜的人']]
W('worshipful','英 /ˈwɜːʃɪpfəl/；美 /ˈwɜːrʃɪpfəl/','充满敬仰的；可敬的〔旧义、尊称〕',
 'a worshipful gaze 是带着深深仰慕的目光；某些正式名称里的 Worshipful 则保存可敬、值得尊重的旧用法。',
 '中古英语 worshipful，现代对应 worship + -ful。worship 原有尊荣、敬重义，所以正式尊称不必理解成把对象当神。',P,
 'a worshipful gaze 仰慕的目光，a worshipful audience 满怀敬仰的听众。The Worshipful Company of ... 可见于伦敦同业公会等固定名称。',
 'a worshipful gaze；worshipful admiration。',
 'worshipful 可说敬仰者的态度，也可在固定尊称中说对象可敬。先看它修饰谁、是不是名称的一部分。',
 ('The young musicians watched her with worshipful admiration.','年轻音乐人满怀敬仰地看着她。'),('He gave his teacher a worshipful look.','他向老师投去仰慕的目光。'),sources=['https://en.wiktionary.org/wiki/worshipful#English','https://www.etymonline.com/word/worship'])
W('worshipper','英 /ˈwɜːʃɪpə/；美 /ˈwɜːrʃɪpər/','礼拜者、敬拜者；崇拜者',
 '参加宗教敬拜的人可叫 worshipper；特别仰慕某个人、某种东西，也可以借这个词描述。',
 'worship + -er，中古英语已有相应人物名词。worshipper 常双写 p，也有 worshiper 的拼法，尤见美式英语。',P[:2]+[['worship + -er → worshipper／worshiper','进行敬拜、崇拜的人']],
 'worshippers gathered 礼拜者聚集，a place for worshippers 礼拜者使用的场所，a sun worshipper 爱晒太阳的人〔常为比喻〕。',
 'worshippers gathered；a sun worshipper。',
 'worshipper 可以是虔诚信徒，也可借作强烈爱好者。修饰语和场景决定是否真在说宗教仪式。',
 ('Worshippers entered the hall quietly.','礼拜者安静地走进大厅。'),('The benches provided space for the worshippers.','长凳为礼拜者提供了座位。'))
R('B3146','把对象视为值得敬重，发展为敬拜与强烈仰慕','WORSHIP：旧起点是尊荣、敬重','worship → worshipful、worshipper；人物名词也拼 worshiper。',
 'worth + 旧 -ship 的历史解释能帮助理解尊称和敬仰。现代 worship 则既有宗教用法，也有对人、事物过度仰慕的比喻。',
 'weorðscipe → worship；-ful 性质、态度，-er 人物。',
 [['敬拜动作与人物','worship · worshipper'],['敬仰态度与固定尊称','worshipful']],
 'worshipful 的固定尊称保存可敬旧义；worshipper 不只一种宗教的专属称呼。',
 'The singer’s worshippers greeted her with worshipful smiles.\n\n歌手的崇拜者带着仰慕的笑容迎接她。','worship worshipper worshipful')
if __name__=='__main__':save('continuation_20261030_kh',ROOTS,WORDS)
