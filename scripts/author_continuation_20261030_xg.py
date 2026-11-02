"""Searching, checking, sharing and sending in common reading forms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3210':dict(words=['search','searches','searched','searching'],label='search → searches／searched／searching：四处找、搜索',note='search 经法语接晚期拉丁 circāre 绕行、走查，与 circus 圆词族相连；现代搜索不受字面行走限制。'),
 'C0221':dict(words=['search','searches','searched','searching'],label='拉丁 circus → circāre → 法语 → search：圆、绕行到搜寻',note='search 的实际借入路线经法语相关形式，现代变形再按 search 加 s／ed／ing；circle 与 search 可通过更早的拉丁词族对照记忆，各自借入路径分别看。'),
 'B3378':dict(words=['check','checking'],label='check → checks／checked／checking：正在核查',note='checking 的 ch 为 /tʃ/，直接加 -ing，不另改词干；具体检查对象和 check 的其他搭配仍看语境。'),
 'B3341':dict(words=['share','sharing'],label='share → shares／shared／sharing：分给、共用与交流',note='share 去 e 加 -ing；sharing 可说交流信息，也可说共同使用、共同承担，不一律等于转发。'),
 'B2495':dict(words=['send','sends','sending'],label='send → sends／sending：把东西送向另一处',note='send 继承古英语 sendan；sends 和 sending 是现在形式，过去 sent 已另讲。'),
}
W('searches','英 /ˈsɜːtʃɪz/；美 /ˈsɜːrtʃɪz/','搜索、搜寻〔复数〕；搜索、查找〔search 的第三人称单数〕',
 '为了找到人、物或信息，到相关地方一个个查看，是 searches。可以是实际找房间，也可以是电脑里的几次检索。',
 'search + -es，/tʃ/ 后增加 /ɪz/。经法语相关形式与中古英语 serchen，接晚期拉丁 circāre 绕行、走查，远接 circus 圆词族。',
 [['拉丁 circus → 晚期拉丁 circāre → 法语相关形式 → search','圆、绕行 → 四处查看、搜寻'],['search 名词、动词 + -es → searches','多次搜索；单数主语查找']],
 'online searches 线上搜索；searches for a key 找钥匙；searches the room 搜查房间；searches through files 在文件里逐一查找。',
 'several searches；searches for information。','searches the room 是查找的范围，searches for the key 是要找的目标。看清有没有 for，就能知道后面是在哪里查，还是要查什么。',
 ('She searches the files for the missing invoice.','她在文件里查找那张丢失的发票。'),('The first two searches gave us no useful results.','前两次搜索没有找到有用结果。'),sources=['https://en.wiktionary.org/wiki/searches#English','https://en.wiktionary.org/wiki/search#English','https://www.etymonline.com/word/search'])
W('searched','英 /sɜːtʃt/；美 /sɜːrtʃt/','搜寻了；搜索、搜查了；search 的过去式和过去分词',
 '当时已经到相关范围里找过，是 searched。找过不等于找到了，结果还要用 found 等词另说。',
 'search + -ed，/tʃ/ 后读 /t/，结尾 /tʃt/。词基经法语接晚期拉丁 circāre 四处走查、绕行词族，现代过去形式按规则变化。',
 [['晚期拉丁 circāre → 法语相关形式 → search','绕行、走查 → 搜寻'],['search + -ed → searched','过去找过、搜查过']],
 'searched for the keys 找过钥匙；searched the bag 查过包；searched online 网上搜过；searched through the drawers 逐个翻查抽屉。',
 'carefully searched；had searched everywhere。','searched for it 说做了寻找动作，found it 才说找到了。searched the box for the letter 中 box 是查找范围，letter 是目标。',
 ('We searched the cupboard for the spare cups.','我们翻查柜子，寻找备用杯子。'),('She searched online before asking the group.','她问群里的人之前，先在网上搜过。'),sources=['https://en.wiktionary.org/wiki/searched#English','https://en.wiktionary.org/wiki/search#English'])
W('searching','英 /ˈsɜːtʃɪŋ/；美 /ˈsɜːrtʃɪŋ/','正在搜寻、搜索；追根究底、深入探究的；search 的 -ing 形式等',
 '持续往可能的地方找，是 searching；如果问题、目光像在往事情里面探，也可以用 searching 形容深入、锐利。',
 'search + -ing，保留 ch 的 /tʃ/，不双写 h。词基经法语、晚期拉丁绕行、走查词族传入；现代也有分词形容词用法。',
 [['法语与晚期拉丁 circāre 等 → search','四处找、查看'],['search + -ing → searching','进行中的搜索；带探究性质的']],
 'searching for a job 找工作；searching through notes 翻查笔记；searching questions 深入追问的问题；a searching look 探究、审视的目光。',
 'keep searching；searching for an answer。','searching questions 可以是有深度、直指关键的提问，不一定是在搜索引擎里输入问题。正在找东西的动作义与追问的形容词义，要看它在句中的位置。',
 ('We are still searching for a quieter place to meet.','我们还在找一个更安静的会面地点。'),('The editor asked several searching questions about the story.','编辑就这个故事问了几个深入的问题。'),sources=['https://en.wiktionary.org/wiki/searching#English','https://en.wiktionary.org/wiki/search#English'])
W('checking','/ˈtʃekɪŋ/','正在检查、核对；控制、托运等动作；check 的 -ing 形式',
 '把情况过一遍、核实有没有问题，是 checking。它也可随 check in、check on 等搭配，说报到、查看某人情况等不同动作。',
 'check + -ing，保留 ck，读 /ˈtʃekɪŋ/。词基的棋局称呼远接波斯 shāh，核查、限制、托运等现代分支按搭配使用。',
 [['棋局相关称呼 → 英语 check 的不同现代分支','核验、限制、托运等'],['check + -ing → checking','进行中的核查、控制、托运等动作']],
 'checking the figures 核对数字；checking on a friend 看看朋友的情况；checking in 办理入住、报到、值机；checking baggage 托运行李。',
 'keep checking；checking for mistakes。','checking for mistakes 是在查有没有错误，checking the figures 是把数字核一遍。check on someone 常是查看对方是否安好或事情进展怎样。',
 ('I am checking the names before printing the list.','打印名单前，我正在核对姓名。'),('Thanks for checking on us after the storm.','谢谢你在暴风雨后关心我们的情况。'),sources=['https://en.wiktionary.org/wiki/checking#English','https://en.wiktionary.org/wiki/check#English'])
W('sharing','英 /ˈʃeərɪŋ/；美 /ˈʃerɪŋ/','正在分享、共用、分担；分享、共用这一活动；share 的 -ing 形式',
 '让不止一个人一起用、一起承担或一起知道，是 sharing。可以分享消息，也可以共用空间、分担工作。',
 'share 去掉末尾不发音 e，加 -ing。share 接古英语 sċearu 分出的部分、切分词族，现代动词把分给、共用等关系带到不同对象上。',
 [['古英语 sċearu 等 → share','分出的一份；分给、共用、共同承担'],['share 去 e + -ing → sharing','进行中的分享、共用；相应活动']],
 'sharing ideas 交流想法；sharing a room 共用房间；sharing the work 分担工作；file sharing 文件共享。',
 'thanks for sharing；sharing with friends。','sharing a room 说共同使用，同一个房间可能仍保持完整；sharing the work 说分担任务。对象不同，共享不必每次都是把物品切开分掉。',
 ('Sharing the work made the task much easier.','分担工作让这项任务轻松多了。'),('We are sharing a table with another group.','我们正和另一个小组共用一张桌子。'),sources=['https://en.wiktionary.org/wiki/sharing#English','https://en.wiktionary.org/wiki/share#English'])
W('sends','/sendz/','送、发送；寄出、派遣；使进入某状态；send 的第三人称单数',
 '让人、物或信息朝另一个地方去，是 sends。信件寄出去，工作人员派过去，声音也能把人送进某种感受。',
 'send + -s，/d/ 后读 /z/。send 继承古英语 sendan，使前去、派送的本族词；现在第三人称是 sends，过去式和分词是 sent。',
 [['古英语 sendan → send','使前去、派送、传送'],['send + -s → sends','单数主语现在送、寄、派遣等']],
 'sends a message 发消息；sends a parcel 寄包裹；sends someone to ... 派某人去……；sends me a copy 给我发副本；sends someone to sleep 使某人入睡。',
 'sends by post；sends it to the group。','sends me a copy 与 sends a copy to me 都能说清人和物。send someone to a place 是派、送到某地；某人实际到达，还可用 arrives、reaches 另说。',
 ('She sends the schedule to everyone on Friday.','她周五把时间表发给所有人。'),('The office sends parcels twice a day.','办公室每天分两次寄包裹。'),sources=['https://en.wiktionary.org/wiki/sends#English','https://en.wiktionary.org/wiki/send#English'])
W('sending','/ˈsendɪŋ/','正在发送、寄出、派遣；发送这一动作；send 的 -ing 形式',
 '把内容从这里送向另一处，动作正在进行，便是 sending。它关注送出的过程，是否送达还要看后续结果。',
 'send + -ing，直接加，不双写 d。send 继承古英语 sendan，现代 -ing 形式保留完整词干；过去形式另用 sent。',
 [['古英语 sendan → send','使前去、传送'],['send + -ing → sending','进行中的送出；发送这一活动']],
 'sending emails 发邮件；sending invitations 发邀请；sending someone a link 给某人发送链接；before sending 发送前。',
 'thanks for sending；sending to the wrong address。','sending 强调动作，sent 常标记已经送出。sending a message 不必说明对方已读，received、read 才分别说接收、读过。',
 ('I am sending the corrected version now.','我现在正在发送修正后的版本。'),('Please check the names before sending the invitations.','发出邀请前，请核对姓名。'),sources=['https://en.wiktionary.org/wiki/sending#English','https://en.wiktionary.org/wiki/send#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xg',ROOTS,WORDS)
 extend_lessons()
