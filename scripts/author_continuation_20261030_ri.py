"""Common affirmative/negative replies and expressive final-p spellings."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
W('yes','/jes/','是的；好的；表示肯定、同意的回答',
 '对方问你要不要、是不是、同不同意，你把答案往肯定方向落下：Yes。语调还可以表示高兴、耐心或不耐烦。',
 '古英语 gīese 等经中古英语 yes／yis 延续，常见分析联系旧肯定 gea 与表示如此的动词材料。它不是现代 y 加一个表示复数的 -es。',
 [['古英语 gīese 等 → 中古英语 yes／yis','较强的肯定、同意表达'],['现代 yes','肯定回答；也可作同意这一名词等']],
 'Yes, please 好的，请；say yes to 答应、同意；a yes 表一个肯定回答。英文否定问句回答要看事实：Didn’t you go?—Yes, I did，意思是我去了。',
 'Yes, please；say yes；a definite yes。','回答否定问句时不要机械照搬中文的对、不对；用完整的 Yes, I did 或 No, I didn’t 最能说明事实。yeah、yep 更口语，正式答复常用 yes。',
 ('Yes, I have read the instructions.','是的，我读过说明了。'),('She said yes to the invitation.','她接受了邀请。'),sources=['https://www.etymonline.com/word/yes'])
W('yea','/jeɪ/','赞成；赞成票；是〔旧式或特定用法〕',
 '表决里一边是 yeas 赞成票，另一边是 nays 反对票；这个 yea 和今天聊天里的 yeah 发音不同。',
 '古英语 gea／ge 经中古英语 ye 等延续，是旧肯定词。现代常见读音 /jeɪ/ 的形成可能受 nay 的对应影响，不是 yeah 随手少写一个 h 就保证同音。',
 [['古英语 gea／ge → 中古英语 ye 等','肯定、同意'],['现代 yea 的保留用法','赞成、赞成票；旧式肯定语']],
 'vote yea 投赞成票；the yeas and nays 赞成与反对票。古文里也可见带强调的确然、是的等用法，现代日常肯定通常用 yes、yeah。',
 'vote yea；the yeas and nays。','yea 赞成票、yay 欢呼在很多口音同读 /jeɪ/，但用法不同；yeah 常读 /jeə/ 等，不能只按拼写接近就混写。',
 ('The clerk counted the yeas and the nays.','书记员清点了赞成票和反对票。'),('She voted yea on the motion.','她对这项动议投了赞成票。'),sources=['https://www.etymonline.com/word/yea'])
W('yeah','/jeə/、/je/ 等口语变体','嗯、对、是的〔非正式肯定〕',
 '聊天时轻轻应一声“嗯，对”，通常比 yes 放松；有时还只是在表示自己听着、跟上了。',
 'yes／yea 的口语变体，拼写表现实际说话里的元音、拖长等变化。不能把末尾 h 当成一个固定表示肯定的古典词根。',
 [['yes／yea 的口语发音变化','较随意的肯定回答'],['yeah 的固定拼写','日常聊天中嗯、对、是的']],
 'Yeah, sure 嗯，当然；Oh yeah? 噢，是吗？后者可真询问，也可怀疑。Yeah, right 还可能是讽刺，不宜只凭词面当成强烈认同。',
 'Yeah, sure；Oh yeah?；Yeah, right。','yeah 常用于轻松对话；yes 在正式回答里更通用。yeah 不等于每次都已经同意方案，有时只是听到了，关键决定最好完整说清。',
 ('Yeah, I remember that café.','嗯，我记得那家咖啡馆。'),('“Can you help me later?” “Yeah, sure.”','“你晚点能帮我吗？”“嗯，当然。”'),sources=['https://www.etymonline.com/word/yeah'])
W('yep','/jep/','嗯、对〔非正式的 yes〕',
 '肯定答复说到末尾把嘴唇一合，听起来短促、干脆，写成 yep。',
 'yes／yeah 的口语变体，末尾 /p/ 形成突然而收住的发音，有与 nope 互相类比的解释。不是 -p 提供了一个独立的赞同含义。',
 [['yes／yeah 的口语变体','肯定回答'],['末尾闭唇收音 → yep','短促、随意的肯定表达']],
 'Yep, that’s right 对，就是这样。朋友、同事轻松聊天常用，正式表格、正式确认中 yes 更稳妥；是否显得敷衍取决于语调和上下文。',
 'Yep, exactly；Yep, I’m ready。','yep 与 yup 都是口语肯定，元音不同；nope 则是否定。不要以为结尾相同就把答案方向弄反。',
 ('“Are these your keys?” “Yep, thanks.”','“这些是你的钥匙吗？”“对，谢谢。”'),('Yep, the file has finished downloading.','对，文件已经下载好了。'),sources=['https://www.etymonline.com/word/nope'])
W('yup','/jʌp/','嗯、对〔非正式的 yes〕',
 '和 yep 一样，是嘴唇在末尾干脆一合的肯定答复，只是中间的元音换了。',
 'yeah／yes 口语词族的变体，含末尾 /p/ 的表达形式；不需要另外假设一个拉丁 yup 表同意。',
 [['yes／yeah 的口语表达','非正式肯定'],['yup 的元音及闭唇末音形式','嗯、对的另一种常见写法']],
 'Yup, all done 嗯，都做完了。多见于随意说话、聊天文字，没有 yep、yup 一个必然更礼貌的统一规则。',
 'Yup, that’s it；Yup, I agree。','yup 不是 yuppie 雅皮士的通用缩写；yep／yup 的核心区别主要在读音、使用习惯，不能据此排正式等级。',
 ('“Did you lock the door?” “Yup, I checked twice.”','“门锁了吗？”“嗯，我检查过两遍。”'),('Yup, that is the address I was looking for.','对，那就是我要找的地址。'))
W('nope','英 /nəʊp/；美 /noʊp/','不、没有〔非正式的 no〕',
 'No 的尾音用嘴唇干脆收住，变成 nope：可以是轻松答一句，也可以是坚定拒绝，语气和场合决定。',
 'no 的口语、强调变体，末尾 /p/ 与闭唇收音有关。不是 no 后面加一个表示做事的 -pe 拉丁后缀。',
 [['no','否定回答'],['带闭唇收音的 nope','短促、非正式的否定']],
 'Nope, not yet 没，还没；Nope, that’s not mine 不，那不是我的。不是名词限定词 no 的所有用法都能换成 nope，不能说 nope money。',
 'Nope, not yet；Nope, I’m fine。','nope 不自动比 no 更凶、更客气，语调可能把同一个词说成玩笑、干脆、敷衍或严厉；正式答复用完整句更清楚。',
 ('“Have they replied?” “Nope, not yet.”','“他们回复了吗？”“没，还没有。”'),('Nope, that is not the folder I meant.','不，那不是我说的文件夹。'),sources=['https://www.etymonline.com/word/nope'])
W('nah','常见 /nɑː/，亦见 /næː/ 等变体','不了；不、没有〔很口语〕',
 '朋友问要不要再喝点，你轻松拖一声 Nah, I’m good，类似“不了，我够了”。也可用于否认前面的话。',
 'no 的口语发音、拼写变体，元音和末尾写法表现随意说话；h 在这里不是一个可普遍套用的否定词根。',
 [['no 的口语变体','随意、放松的否定'],['nah 的固定拼写','不了、不的非正式回答']],
 'Nah, thanks 不用了，谢谢；Nah, that’s wrong 不，那不对。语气可软可硬，不能只因词短就断定没有礼貌。',
 'Nah, I’m good；Nah, not today。','nah 是口语否定，nay 常用于表决或旧式表达；两者字母相近但现代读音、场合不同。',
 ('“Would you like another cup?” “Nah, thanks.”','“还要一杯吗？”“不了，谢谢。”'),('Nah, I do not think that is the right date.','不，我觉得日期不是那个。'))
W('nay','/neɪ/','不、反对；反对票〔表决、旧式等语境〕',
 '表决点名时答 nay，就站在反对那一边；普通聊天里说不，no 通常更自然。',
 '中古英语 nai／nei 借古诺尔斯语 nei，较早含否定与 ever 一类材料；和 no 有古老同族关系，不是现代 no 只换一个字母就临时构成。',
 [['古诺尔斯 nei → 中古英语 nai／nei','否定、反对'],['现代 nay 的保留用法','表决反对、反对票；旧式否定']],
 'vote nay 投反对票；the yeas and nays 赞成与反对票。文学里还可能用来修正、加强前面的说法，先读懂现代常见表决用法即可。',
 'vote nay；the nays have it。','nay 常读 /neɪ/，nah 常是 /nɑː/；yea 与 nay 是传统肯定、否定的对应，不是 yay 欢呼的反义情绪词。',
 ('Three members voted nay on the proposal.','三名成员对提案投了反对票。'),('The clerk recorded each yea and nay.','书记员记录了每一票赞成和反对。'))
W('yay','/jeɪ/','好耶；太好了〔欢呼〕',
 '等了好久终于成功，忍不住喊一句 Yay!，重点不是平静回答是，而是把高兴喊出来。',
 'yea 的变体，后来固定为表示喜悦、庆祝的感叹词。这里讲欢呼用法，不混入同形俚语的其他来源。',
 [['yea 的形式变体','肯定、兴奋的声音材料'],['yay 的感叹用法','欢呼、庆祝']],
 'Yay, we did it! 耶，我们成功了！文本里也常单写 Yay!。随意、带情绪的表达，不用来代替正式表决中的 yea。',
 'Yay, it worked；Yay for the team。','yea 可是赞成票，yay 是欢呼；yeah 常是随意肯定。相近的声音并不让三个拼写在所有场合互换。',
 ('Yay, the missing file is back!','太好了，丢失的文件找回来了！'),('The children shouted “Yay!” when they saw the cake.','孩子们看到蛋糕时高兴地喊起了“耶！”'))
W('welp','/welp/','唉，好吧；那就这样吧〔非正式，常带无奈〕',
 '计划没成、结果出来了，一时也改不了，叹一句 Welp，像把 well, ... 的尾巴干脆合住：好吧，只能这样了。',
 'well 的口语变体，末尾加闭唇 /p/ 并形成相应拼写，与 yep、nope 的收音方式可对照；不含一个独立表示失败的 -p 词根。',
 [['well 的口语变体','承接、回应当前局面的声音'],['welp 的末音与拼写固定','常带接受现实、无奈转折的口吻']],
 'Welp, that didn’t work 好吧，那没成功；Welp, time to go 那好，该走了。多用于随意对话、网络文字；具体情绪还看后文。',
 'Welp, ...；Welp, here we go。','welp 和 whelp 幼兽等词常同音或近音，但不是同一词源；welp 并非语法上的 well 的过去式。',
 ('Welp, that plan did not work. Let us try another one.','好吧，那个计划没成功。我们换个办法试试。'),('Welp, it is getting late. I should head home.','那好，天不早了。我该回家了。'))
R('A2265','口语回复中闭唇收住的末尾音、相应拼写〔不是古典词根义〕','末尾 P：让回复短促收住，肯定还是否定由原词决定',
 'yeah、yes 的肯定可以变成 yep、yup；no 的否定可以变成 nope；well 的承接、无奈口吻可写成 welp。',
 '这一项是口语发音、拼写形式的整理。末尾 /p/ 常与闭唇收音、表达口吻有关，不是一个一加上去就表示同意或反对的拉丁、希腊词根。肯定、否定回复各自还有更早的不同历史。',
 'yes／yeah → yep、yup；no → nope；well → welp，是现代识别这些形式的对照。yea、yay、nay、nah 放在旁边帮助辨读，不声称它们都由同一个 p 后缀派生。',
 [['肯定及口语变体','yes · yea · yeah · yep · yup'],['否定及对应读法','no · nah · nay · nope'],['欢呼与承接口吻','yay；well · welp']],
 'yea 赞成票、yay 欢呼、yeah 口语肯定分开；nope 不能随意替代限定名词的 no，如 no money；yep、nope 是否显得礼貌取决于整句和语调。',
 '“Ready?” “Yep.” “Any problems?” “Nope.”\n\n“准备好了？”“嗯。”“有问题吗？”“没有。”',
 'yes yea yeah yep yup no nah nay nope yay well welp')
if __name__=='__main__':save('continuation_20261030_ri',ROOTS,WORDS)
