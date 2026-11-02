"""Common past forms in reports, instructions and everyday speech."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0268':dict(words=['create','created'],label='create → created：使新的东西出现',note='created 的 -ed 读 /ɪd/；create 借拉丁 creare 的分词材料进入英语，创作与造成均可。'),
 'B3634':dict(words=['follow','followed'],label='follow → followed：跟随、遵循与随后发生',note='followed 词尾读 /d/；was followed by 说后面接着什么，followed by 可缩成修饰结构。'),
 'C0655':dict(words=['release','released'],label='release → released：松开、释放到公开发布',note='release 接拉丁 relaxare 松开的词族，released 表过去或完成；不误归 ligare 捆绑词族。'),
 'C1635':dict(words=['provide','provided'],label='provide → provided：预先准备到提供、配备',note='provide 历史 pro- 向前加 videre 看，发展出预备、供给；本组先讲提供的动词形式。'),
 'C1288':dict(words=['describe','described'],label='describe → described：写下来、描画到描述',note='describe 的 de- 在这里不作否定；described 常与 as 连用说被描述为何种样子。'),
 'C1105':dict(words=['report','reported'],label='report → reported：把信息带回来',note='report 接拉丁 re- 加 portare 带，reported 词尾读 /ɪd/；报道、汇报都不自动等于内容已证实。'),
 'C1487':dict(words=['continue','continued'],label='continue → continued：把前后接起来',note='continue 来自拉丁 continuare，联系连在一起；continued 是持续、继续的过去或分词形式。'),
 'C1379':dict(words=['expect','expected'],label='expect → expected：向外望着等待到预期',note='expect 接拉丁 exspectare 词族；expected 既可说预期会发生，也可在 be expected to 中说职责、要求。'),
 'C0957':dict(words=['compare','compared'],label='compare → compared：放在一起看异同',note='compare 接拉丁 com- 加 par 相等词族，经法语进入；compared with／to 常引出比较参照。'),
 'B3045':dict(words=['end','ended'],label='end → ended：结束；最终落到某种结果',note='ended 的 -ed 读 /ɪd/；ended up 常说最后结果，ended in 常交代结局。'),
 'C0271':dict(words=['increase','increased'],label='increase → increased：数量、程度长上去了',note='increase 接拉丁 increscere 生长、增加；increased 的结尾读 /st/，此处 in- 不是否定。'),
 'C1163':dict(words=['publish','published'],label='publish → published：把内容公开给读者',note='publish 接拉丁 publicare、法语 publier 的公开词族；-ish 的现有拼写不能当现代 public 规则加后缀。'),
}
W('created','/kriˈeɪtɪd/','创造了；建立了；造成了；create 的过去式和过去分词',
 '原来没有的东西或局面被做出来了，就是 created。可以创造作品、建立文件，也可以造成麻烦，不一定全是好事。',
 'create 去末尾 e，加完整 -ed；原词结尾 /t/ 后，过去词尾读 /ɪd/。create 经中古英语接拉丁 creatus、creare 使产生的词族。',
 [['拉丁 creare／creatus → 英语 create','使产生、创造'],['create 去 e + -ed → created','过去创造、建立、造成']],
 'created a file 创建了文件；created jobs 创造了工作岗位；created a problem 造成了问题；was created by ... 由……创作、建立。',
 'newly created；created for a purpose。','created 说使某物出现，discovered 说发现原来就存在的东西。created a problem 是造成了问题，不能因为 create 常译创造就当成褒义。',
 ('The new entrance created more space for waiting visitors.','新入口为等候的访客腾出了更多空间。'),('She created a folder for each project.','她为每个项目建了一个文件夹。'),sources=['https://en.wiktionary.org/wiki/created#English','https://en.wiktionary.org/wiki/create#English'])
W('followed','英 /ˈfɒləʊd/；美 /ˈfɑːloʊd/','跟随了；遵循了；随后发生了；follow 的过去式和过去分词',
 '有人走在前，你在后面跟着；规则、线索或事件也可以处在前面，让动作或另一件事接着它来。',
 'follow + -ed，元音后读 /d/。follow 继承古英语 folgian 跟随，经中古英语延续，实体移动、遵循规则和先后顺序等用法并存。',
 [['古英语 folgian → follow','跟随；发展出遵循、接着发生等义'],['follow + -ed → followed','过去跟随、遵循；随后出现']],
 'followed the instructions 按照说明做了；followed a path 沿小路走了；followed by ... 后面接着……；what followed 随后发生的事。',
 'followed closely；was followed by a discussion。','A was followed by B 的顺序是先 A 后 B；B followed A 也是先 A 后 B。被动结构把叙述起点换了，时间顺序没有倒过来。',
 ('We followed the signs to the main entrance.','我们沿着路标走到了正门。'),('The short talk was followed by a discussion.','简短讲话之后进行了讨论。'),sources=['https://en.wiktionary.org/wiki/followed#English','https://en.wiktionary.org/wiki/follow#English'])
W('released','/rɪˈliːst/','释放了；松开了；发布、发行了；release 的过去式和过去分词',
 '原来被关着、握着或没有对外开放的东西，现在放出来了。人可以获释，按钮可以松开，新作品也可以向公众发布。',
 'release 去末尾 e，加完整 -ed；原词结尾 /s/ 后读 /t/，整词结尾 /st/。经古法语 relaisser／relesser 等接拉丁 relaxare 松开，不源自 ligare 捆绑。',
 [['拉丁 relaxare → 古法语相关形式 → release','松开、放开 → 释放、公开提供'],['release 去 e + -ed → released','过去释放、松开、发布']],
 'released the button 松开了按钮；released a statement 发布声明；released an album 发行专辑；was released from ... 从……获释、解除。',
 'released to the public；released last month。','released 描述已经放出或发布，relieved 更常说感到宽慰。release 与 relax 有历史联系，但现代 relax 通常说放松，不能直接替代发布文件的 release。',
 ('The team released a new version of the app.','团队发布了这个应用的新版本。'),('She released the button when the light turned green.','灯变绿时，她松开了按钮。'),sources=['https://en.wiktionary.org/wiki/released#English','https://en.wiktionary.org/wiki/release#English'])
W('provided','英 /prəˈvaɪdɪd/；美 /prəˈvaɪdɪd/','提供了、配备了；provide 的过去式和过去分词',
 '把别人需要的东西准备好、送到位，是 provided：房间提供毛巾，主办方提供信息，人提供帮助。',
 'provide 去末尾 e，加完整 -ed，/d/ 后过去词尾读 /ɪd/。拉丁 pro- 向前 + videre 看形成 providere 预见、预备，供给义沿这条路线发展；这里先讲提供义的动词形式。',
 [['拉丁 pro- + videre → providere → provide','向前看、预先安排 → 供给、提供'],['provide 去 e + -ed → provided','过去提供；已经配备']],
 'provided information 提供了信息；provided someone with ... 给某人提供……；provided ... for someone 为某人提供……；meals are provided 提供餐食。',
 'provided by the organiser；provided with a map。','provided us with chairs 是为我们提供椅子，provided chairs for us 也表达这个关系。provide 常用 with 或 for 来接人和物，不照搬 give 的所有双宾语结构。',
 ('The hotel provided us with clean towels.','酒店为我们提供了干净毛巾。'),('All the information you need is provided below.','你需要的信息都列在下面了。'),sources=['https://en.wiktionary.org/wiki/provided#English','https://en.wiktionary.org/wiki/provide#English'])
W('described','/dɪˈskraɪbd/','描述了；描绘了；described 为 describe 的过去式和过去分词',
 '把看到、想到的东西用语言勾勒出来，让别人也能在脑中看见，就是 described。它可以讲外貌、过程，也可以说明某物属于哪一类。',
 'describe 去末尾 e，加完整 -ed；/b/ 后读 /d/。拉丁 de- + scribere 写形成 describere 写下、描画，经法语等借入路线进入英语；这里 de- 不作否定。',
 [['拉丁 de- + scribere → describere → 法语、英语 describe','写下、描画 → 描述'],['describe 去 e + -ed → described','过去描述；被描绘为']],
 'described the scene 描述了场景；described how ... 说明了如何……；described as ... 被描述为……；described in detail 详细描述。',
 'described by a witness；described as useful。','describe something to someone 是向某人描述某事；describe someone as ... 是把某人描述为……。后者的 as 引出评价或身份，不能用 to 替代。',
 ('She described the route so clearly that we did not need a map.','她把路线说得很清楚，我们连地图都不需要。'),('The room was described as small but comfortable.','这个房间被描述为虽小却舒适。'),sources=['https://en.wiktionary.org/wiki/described#English','https://en.wiktionary.org/wiki/describe#English'])
W('reported','英 /rɪˈpɔːtɪd/；美 /rɪˈpɔːrtɪd/','报道、报告了；据报的；report 的过去式和过去分词等',
 '把知道的信息带回来、告诉别人，是 reported。它说信息经过了报道或汇报，不自动保证内容已经被独立证实。',
 'report + -ed，原词 /t/ 后加 /ɪd/。经法语 reporter 接拉丁 re- 往回 + portare 携带，reportare 把消息带回等用法提供语义联系。',
 [['拉丁 re- + portare → reportare → 法语 reporter → report','带回来 → 报告、转述消息'],['report + -ed → reported','过去汇报；据报道、被转述的']],
 'reported the problem 报告了问题；reported that ... 报道称……；was reported missing 被报失踪；reported speech 间接引语、转述话语。',
 'reported by local media；is reported to be ...。','reported to be 与 confirmed to be 信息强度不同：前者说据报如此，后者说已获确认。reported speech 是转述别人说话的语法名称。',
 ('Several passengers reported the broken light to the driver.','几位乘客向司机反映灯坏了。'),('The newspaper reported that the bridge would reopen on Monday.','报纸报道称，这座桥将于周一重新开放。'),sources=['https://en.wiktionary.org/wiki/reported#English','https://en.wiktionary.org/wiki/report#English'])
W('continued','英 /kənˈtɪnjuːd/；美 /kənˈtɪnjuːd/','继续了；持续的、接连的；continue 的过去式和过去分词等',
 '把前一段和后一段接起来，让事情不断下去，是 continued。它既可说做事继续了，也可形容支持、努力一直在。',
 'continue 去末尾 e，加完整 -ed；末尾元音后读 /d/。经古法语 continuer 接拉丁 continuare，联系 continuus 连在一起的，更远接 continere 保持在一起。',
 [['拉丁 continuus／continuare → 法语 continuer → continue','连在一起 → 持续、继续'],['continue 去 e + -ed → continued','过去继续；一直持续的']],
 'continued working／continued to work 继续工作；continued support 持续的支持；continued on 继续前行；to be continued 未完待续。',
 'continued throughout the night；continued interest。','continued 可修饰名词，如 continued support；continuously 是副词，修饰动作连续进行。两者都接得上持续画面，但句中位置不同。',
 ('The rain continued throughout the afternoon.','雨下了整整一个下午。'),('Thank you for your continued support.','感谢你一直以来的支持。'),sources=['https://en.wiktionary.org/wiki/continued#English','https://en.wiktionary.org/wiki/continue#English'])
W('expected','/ɪkˈspektɪd/','预料到的；被要求、被认为应当的；expect 的过去式和过去分词',
 '往前看，心里已经等着某件事发生，是 expected。也可以说别人对你的行为有期待：你应该按时到。',
 'expect + -ed；/t/ 后读 /ɪd/。拉丁 ex- 向外 + spectare 观看形成 exspectare 等待、期待，提供词源画面；现代 ex- 不单独表示以前的。',
 [['拉丁 ex- + spectare → exspectare → expect','向外望、等待 → 预料、期待'],['expect + -ed → expected','预料过；预期的、被要求的']],
 'as expected 正如预料；earlier than expected 比预料的早；expected to arrive 预计会到；expected to attend 被要求、被期待出席。',
 'the expected result；is expected to ...。','The train is expected to arrive 说预计到达；Staff are expected to arrive early 常是要求员工提前到。主语和场景决定是在预测，还是在提出要求。',
 ('The parcel arrived earlier than expected.','包裹比预料的更早到了。'),('Everyone is expected to keep the room tidy.','大家都应当保持房间整洁。'),sources=['https://en.wiktionary.org/wiki/expected#English','https://en.wiktionary.org/wiki/expect#English'])
W('compared','英 /kəmˈpeəd/；美 /kəmˈperd/','比较过；与……相比；compare 的过去式和过去分词',
 '把两个东西摆到一起，看看哪里相同、哪里不同，就是 compared。后面常接 with 或 to，把比较对象带出来。',
 'compare 去末尾 e，加完整 -ed；词尾 /d/。经法语 comparer 接拉丁 comparare 比较、配对，历史 com- 一起 + par 相等；不是 prepare 的准备词族。',
 [['拉丁 com- + par → comparare → 法语 comparer → compare','使相配、放在一起比较'],['compare 去 e + -ed → compared','过去比较；拿某参照来对比']],
 'compared prices 比较了价格；compared with last year 与去年相比；compared to ... 与……相比、比作……；cannot be compared 无法相提并论。',
 'compared side by side；compared with the old design。','compare A with B 常说对照异同，compare A to B 也可作比较，另常用于比喻；真实用法有重叠，不把 with／to 说成任何场景下都严格分开的两条死规矩。',
 ('We compared the two maps before leaving.','出发前，我们对照了两张地图。'),('Compared with the old chair, this one is much lighter.','和旧椅子相比，这把轻多了。'),sources=['https://en.wiktionary.org/wiki/compared#English','https://en.wiktionary.org/wiki/compare#English'])
W('ended','/ˈendɪd/','结束了；使结束了；最终落到某种结果；end 的过去式和过去分词',
 '走到事情的尾端，前面的过程收住了，是 ended。ended up 还会把目光带到最后：折腾一番，结果到了哪一步？',
 'end + -ed；原词 /d/ 后读 /ɪd/，多一个音节。名词、动词延续古英语 ende 等本族词族，尾端与终止义相连。',
 [['古英语 ende 等 → end','末端、结束；使到尽头'],['end + -ed → ended','过去结束；最后处于某种结果']],
 'the meeting ended 会议结束了；ended the conversation 结束谈话；ended up doing 最后竟做了……；ended in a draw 以平局结束。',
 'ended well；ended up at the wrong station。','ended up doing 常说最后的结果，有时带出乎意料的感觉；ended by doing 常说以某个动作收尾。具体意义要把 up、by、in 一起看。',
 ('The meeting ended earlier than we expected.','会议比我们预计的更早结束了。'),('We took the wrong bus and ended up at the airport.','我们坐错公交，最后到了机场。'),sources=['https://en.wiktionary.org/wiki/ended#English','https://en.wiktionary.org/wiki/end#English'])
W('increased','/ɪnˈkriːst/','增加了、提高了；增加的；increase 的过去式和过去分词等',
 '原来的数量或程度往上长了，是 increased。可以是人数、音量、需求，也可以是压力，不一定都是钱或尺寸。',
 'increase 去末尾 e，加完整 -ed；结尾 /s/ 后读 /t/，所以 /kriːst/ 不添 /ɪd/。拉丁 in- + crescere 生长形成 increscere，经法语进入英语。',
 [['拉丁 increscere → 法语相关形式 → increase','长大、增加'],['increase 去 e + -ed → increased','过去增加；增大的、提高的']],
 'increased demand 增长的需求；increased the volume 调高了音量；increased by ... 增加了……；increased to ... 增加到……。',
 'greatly increased；increased from ... to ...。','increased by ten 是增加了十，increased to ten 是增加到十。by 说增量，to 说最后数值，不能读反。',
 ('Attendance increased from thirty to forty people.','出席人数从三十人增加到了四十人。'),('She increased the text size so that everyone could read it.','她调大了文字，方便大家阅读。'),sources=['https://en.wiktionary.org/wiki/increased#English','https://en.wiktionary.org/wiki/increase#English'])
W('published','/ˈpʌblɪʃt/','出版了；发表、公布了；publish 的过去式和过去分词',
 '把内容从个人手里拿出来，交给读者或公众看到，是 published。可以是印成书，也可以是在网站上正式发表。',
 'publish + -ed；/ʃ/ 后读 /t/，整词结尾 /ʃt/。拉丁 publicare 使公开经法语 publier 成为早期英语 publicen 等，后来词形受 finish 等影响出现 publish；不作现代 public + -ish 的规则拼接。',
 [['拉丁 publicare → 法语 publier → 早期英语 publicen 等 → publish','使公开、出版'],['publish + -ed → published','过去出版、发表；已公布的']],
 'published a book 出版了书；published an article 发表文章；published online 在线发表；published figures 已公布的数据；was first published 首次出版于。',
 'recently published；published by a small press。','printed 说明印出来了，published 强调已向读者、公众推出。一本材料可以印了少量内部使用而没有出版，一篇文章也可以在线发表而不印纸。',
 ('Her first book was published by a small local press.','她的第一本书由当地一家小出版社出版。'),('The timetable was published on the school website.','时间表公布在学校网站上了。'),sources=['https://en.wiktionary.org/wiki/published#English','https://en.wiktionary.org/wiki/publish#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wf',ROOTS,WORDS)
 extend_lessons()
