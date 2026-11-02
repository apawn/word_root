"""Common missing base words: comic, funeral, arena and resort."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B4294':dict(words=['comedy','comic','comics','comical'],label='comedy／comic／comical：喜剧、漫画与滑稽效果',note='共享希腊欢庆表演材料，但各英语词有自己的借入或派生历史，不把 comic 说成剪短 comedy。'),
 'A1771':dict(words=['funeral','funerals'],label='funeral → funerals：葬礼相关形容词的名词用法',note='拉丁 funus、funer- 与 alis 形成相关性质形容词，借入后用于葬礼名称。'),
 'A1776':dict(words=['arena','arenas'],label='arena → arenas：拉丁沙地名称与英语规则复数',note='借词 arena 整体学习，复数在现代英语通常用 s，不必一律恢复拉丁 ae。'),
 'C1208':dict(words=['resort','resorts'],label='resort → resorts：转向求助与休闲目的地',note='法语 re- 加 sortir 出去的历史材料，不能和英语 sort 分类的词族混同。'),
}
W('comic','英 /ˈkɒmɪk/；美 /ˈkɑːmɪk/','喜剧的、滑稽有趣的；漫画刊物；喜剧演员',
 '让人从情节、表演里感到好笑，是 comic 的喜剧画面；逗笑的人、早期以幽默为主的连环图画，也用了这个名称。',
 'comic 借拉丁 cōmicus，接希腊 kōmikós 喜剧的，较早联系 kōmos 欢庆、游乐。现代 -ic 可认作相关性质的成分；comedy 与 comic 是较早同族的不同词形。',
 [['希腊 kōmos、kōmikós → 拉丁 cōmicus → comic','欢庆、喜剧表演 → 喜剧的'],['comic 形容词 → 人、出版物名词','喜剧演员；漫画刊物，现代内容范围扩展']],
 'comic scenes 喜剧场面；comic timing 喜剧节奏；a comic 漫画刊物或喜剧演员。',
 'a comic character；read a comic on the train。','comic 作形容词可以说喜剧性质，也可说好笑；作可数名词时看是在谈演员还是读物。现代漫画不一定都以搞笑为目的。',
 ('The film has several memorable comic scenes.','这部电影有几场令人难忘的喜剧场面。'),('She read a comic on the train.','她在火车上读了一本漫画。'),sources=['https://en.wiktionary.org/wiki/comic#English','https://www.etymonline.com/word/comic'])
W('comics','英 /ˈkɒmɪks/；美 /ˈkɑːmɪks/','漫画、漫画出版物；喜剧演员〔comic 的复数及集合用法〕',
 '漫画架上一册册故事、报纸上的连环图，可以叫 comics；台上几位逗笑观众的人，也可以数成 comics。',
 'comic + -s，/k/ 后读 /s/。comic 的喜剧形容词借自拉丁、希腊词族；英语名词先有人物用途，再发展到幽默插图与连环漫画，现代媒介范围更宽。',
 [['希腊、拉丁喜剧词 → comic；英语名词用途','喜剧的 → 演员、幽默图画'],['comic + -s → comics','多位喜剧演员；漫画作品、出版物或媒介']],
 'read comics 读漫画；a shelf of comics 一架漫画；stand up comics 单口喜剧演员。',
 'comics for young readers；comics performing on stage。','comics 在读物语境常是漫画，在演出阵容里可以是喜剧演员。它也可整体说漫画这种媒介，具体数和谓语看句中所指。',
 ('The library has a shelf of comics for young readers.','图书馆有一架供年轻读者看的漫画。'),('Three comics performed at the theatre that evening.','那天晚上有三位喜剧演员在剧院表演。'),sources=['https://en.wiktionary.org/wiki/comics#English','https://www.etymonline.com/word/comic'])
W('comical','英 /ˈkɒmɪkəl/；美 /ˈkɑːmɪkəl/','滑稽的、令人发笑的',
 '姿势、表情或场面看起来有点滑稽，让人忍不住笑，就是 comical；不一定是特意设计来演喜剧。',
 '以 comic 或相关拉丁 cōmicus 为基础，加 -al → comical，形成性质形容词。较早接希腊、拉丁喜剧词；英语从喜剧相关，逐渐常用于实际显出的好笑效果。',
 [['希腊、拉丁喜剧词 → 英语 comic','喜剧相关、引人笑'],['comic + -al → comical','具有滑稽、好笑的效果']],
 'a comical expression 滑稽表情；a comical scene 滑稽场面；look comical 看起来滑稽。',
 'a comical misunderstanding；a comical attempt to look serious。','comic 也可泛说喜剧的，comical 更常直接评价眼前效果好笑。二者有重叠，不必把每个例子都强制分成绝对两类。',
 ('He made a comical attempt to look serious.','他努力装严肃，样子却很滑稽。'),('The dog’s comical expression made everyone smile.','狗滑稽的表情把大家都逗笑了。'),sources=['https://en.wiktionary.org/wiki/comical#English','https://www.etymonline.com/word/comical'])
W('funeral','/ˈfjuːnərəl/','葬礼；葬礼的',
 '人去世后，亲友以仪式悼念、告别，是 funeral；具体的宗教和安排可以不同，词的中心是为逝者举行的告别仪式。',
 '拉丁 fūnus，词干 fūner-，是葬礼、丧葬仪式，形成 fūnerālis 相关的形容词，并有 fūnerālia 礼仪用法。英语 funeral 较早作形容词，后来可从 funeral service 等表达省略成名词。',
 [['拉丁 fūnus、fūner- → fūnerālis、fūnerālia','丧葬仪式 → 葬礼相关的、葬礼仪式'],['英语 funeral 形容词、名词用法','葬礼的；一场葬礼']],
 'attend a funeral 参加葬礼；funeral service 葬礼仪式；funeral arrangements 葬礼安排。',
 'a funeral for a family member；the day of the funeral。','funeral 可作名词，也可在 funeral service 等组合中说明与葬礼相关。它常与 ceremony 仪式、mourn 悼念等词出现在同一语境。',
 ('The family gathered for the funeral.','家人聚在一起参加葬礼。'),('The funeral service was held in a small chapel.','葬礼仪式在一间小礼拜堂举行。'),sources=['https://en.wiktionary.org/wiki/funeral#English','https://www.etymonline.com/word/funeral'])
W('funerals','/ˈfjuːnərəlz/','葬礼〔funeral 的复数〕',
 '把不同人、不同次举行的告别仪式分别谈，就用 funerals；共同都是亲友悼念、送别逝者的场合。',
 'funeral + -s，/l/ 后读 /z/。底词接拉丁 fūner- 与葬礼相关形容词、礼仪名词材料；现代英语名词按普通规则形成复数。',
 [['拉丁葬礼词族 → 英语 funeral 名词','丧葬仪式、相关的 → 葬礼'],['funeral + -s → funerals','多场葬礼、不同的告别仪式']],
 'attend funerals 参加葬礼；customs at funerals 葬礼习俗；funerals in different traditions 不同传统中的葬礼。',
 'funerals described in the book；music played at funerals。','funerals 数仪式、场合；funeral music 中前面的 funeral 说明音乐用途，通常用单数形式。文化比较时，可用 funerals 谈不同传统的仪式。',
 ('The book describes customs at funerals in different communities.','这本书描述了不同群体的葬礼习俗。'),('The choir sings at weddings and funerals.','这个合唱团在婚礼和葬礼上演唱。'),sources=['https://en.wiktionary.org/wiki/funerals#English','https://www.etymonline.com/word/funeral'])
W('arena','/əˈriːnə/','竞技场、表演场馆；竞争、活动领域',
 '人们围着中间一块场地，看比赛、表演，是 arena。更早拉丁词的意思是沙，古罗马圆形场馆中央铺沙，沙地名称便用于竞技场。',
 '整体借拉丁 harēna、arēna，已有沙、沙地与竞技场义，更远来源不确定，可能有伊特鲁里亚语背景；现代不把 ar-、ena 任意拆作英语前后缀。',
 [['拉丁 harēna、arēna','沙、铺沙的地面 → 场馆中央竞技场'],['英语 arena','比赛、表演场馆；比喻竞争、活动的领域']],
 'a sports arena 体育竞技馆；an indoor arena 室内场馆；the political arena 政治领域。',
 'an arena filled with spectators；enter a new arena of activity。','arena 可以是实物场馆，也可以比喻一块人们竞争、活动的领域。体育设施的具体名称受地方和项目习惯影响，不只按屋顶有无来分。',
 ('The concert will take place in the new arena.','音乐会将在新场馆举行。'),('The debate brought new voices into the public arena.','这场辩论让新的声音进入公共讨论领域。'),sources=['https://en.wiktionary.org/wiki/arena#English','https://www.etymonline.com/word/arena'])
W('arenas','/əˈriːnəz/','竞技场、表演场馆；竞争、活动领域〔arena 的复数〕',
 '不同城市的一座座比赛场馆，是 arenas；把场地换成公共事务、文化活动，也可说人们参与竞争的不同领域。',
 'arena + -s，/ə/ 后读 /z/。借词 arena 接拉丁沙地、竞技场名称；现代英语通常用规则复数 arenas，a 结尾借词的英语复数不必一律按拉丁语恢复。',
 [['拉丁沙地、竞技场词 → 英语 arena','沙地 → 供人比拼、表演的场地'],['arena + -s → arenas','多个场馆、不同角逐领域']],
 'sports arenas 体育场馆；large arenas 大型场馆；different public arenas 不同公共活动领域。',
 'arenas built for indoor sports；arenas for artistic debate。','arenas 是英语常用复数，和 ideas 一样直接加 s。它数比赛场馆，也能数抽象活动领域，名词前面的修饰词说明具体内容。',
 ('The city has several arenas for indoor sports.','这座城市有几座供室内运动使用的场馆。'),('The book compares debates in different public arenas.','这本书比较不同公共活动领域中的讨论。'),sources=['https://en.wiktionary.org/wiki/arenas#English','https://www.etymonline.com/word/arena'])
W('resort','英 /rɪˈzɔːt/；美 /rɪˈzɔːrt/','度假地；求助、诉诸〔resort to〕；最后手段等',
 '遇到需要时，人会转向一个可用的地方、办法，是 resort 的理解线索；它既能说可以去休闲的地点，也保留转向某种手段的用途。',
 '古法语 resort 资源、帮助与 resortir 相连，较早 re- 再 + sortir 出去；英语名词、动词各有借入与发展。这里的 sortir 与现代 sort 分类词族不同。',
 [['古法语 resort、resortir → 英语 resort','再次出去、转向 → 可求助的对象、办法'],['英语后续用途','度假休闲目的地；resort to 转向某种手段']],
 'a seaside resort 海滨度假地；resort to... 诉诸、采用……；as a last resort 作为最后手段。',
 'stay at a resort；resort to drawing a diagram。','resort to 后接名词或 -ing，如 resort to using a map，常是在其他办法不够时改用这一步。a resort 作地点名词时则按度假地、休闲场所理解。',
 ('They stayed at a quiet seaside resort.','他们住在一个安静的海滨度假地。'),('We used the spare room as a last resort.','实在没有别的办法时，我们用了备用房间。'),sources=['https://en.wiktionary.org/wiki/resort#English','https://www.etymonline.com/word/resort'])
W('resorts','英 /rɪˈzɔːts/；美 /rɪˈzɔːrts/','度假地〔复数〕；诉诸、采用〔第三人称单数〕',
 '供人去休闲的一处处地点，是 resorts；一个人转向某种办法，也会写 resorts to。两种场景都能接到去、转向的理解线索。',
 'resort + -s，/t/ 后读 /s/。底词经古法语 resort、resortir 的求助、资源与出去相关用法借入，re- 在法语历史里是再；现代地点和动词用途分开读。',
 [['古法语 resort、resortir → resort','转向、求助；后来休闲目的地义'],['resort + -s → resorts','多个度假地；单数主语采用某手段']],
 'ski resorts 滑雪度假地；beach resorts 海滨度假地；resorts to a diagram 改用图示说明。',
 'resorts along the coast；resorts to writing the steps down。','resorts 作地点复数不必接 to；resorts to doing 则是动词，to 是介词。这个读音、词源与把东西重新分类的表达要分清。',
 ('The coast has several small beach resorts.','这段海岸有几个小型海滨度假地。'),('She resorts to drawing when words are not enough.','语言说不清时，她就改用画图说明。'),sources=['https://en.wiktionary.org/wiki/resorts#English','https://www.etymonline.com/word/resort'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zd',ROOTS,WORDS)
 extend_lessons()
