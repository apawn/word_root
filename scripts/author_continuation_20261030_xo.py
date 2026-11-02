"""Daily-life base words missed by the earlier export: restaurant, opposite, email."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B4377':dict(words=['restore','restaurant','restaurants'],label='restore／restaurant：从恢复体力的食物到餐馆',note='restaurant 借法语 restaurer 的分词名词化，先关联恢复体力的食物，后指供应食物的店；不是英语 restore 直接加 -ant。'),
 'C1208':dict(words=['restore','restaurant','restaurants'],label='re- 恢复词族中的餐馆名称',note='拉丁 restaurare 经法语形成 restore、restaurant 的不同借入路线。'),
 'C0847':dict(words=['oppose','opposite','opposites','opposition'],label='oppose／opposite／opposition：放在对面、相对与反对',note='ob- 在 /p/ 前有 op- 同化形式；这些英语词分别承接较早相关形式。'),
 'B3331':dict(words=['mail','email','emails','emailed','emailing'],label='mail → email → emails／emailed／emailing：电子邮件与发送',note='email 缩自 electronic mail，名词再作动词；这里只列无连字符的常见写法。'),
 'C0367':dict(words=['electronic','email','emails','emailed','emailing'],label='electronic mail → email：电子通信的缩短形式',note='e 来自 electronic；更早电的名称接希腊 ēlektron 琥珀，但邮件构词直接发生在现代英语。'),
}
W('restaurant','英 /ˈrestrɒnt/；美 /ˈrestərɑːnt/','餐馆；饭店〔供用餐的店〕',
 '走进去坐下，点一顿饭来吃的地方，就是 restaurant。它名字背后的画面很生活化：吃点东西，让体力恢复。',
 '借法语 restaurant，原是 restaurer 恢复、补养的现在分词用作名词，曾指恢复体力的食物，后指供应餐食的店。较早接拉丁 restaurāre，与英语 restore 同族；法语 -ant 不应直接当成英语把 restore 改成餐馆的现造规则。',
 [['拉丁 restaurāre → 法语 restaurer','修复、恢复 → 使体力恢复'],['法语 restaurant：分词名词化','补养的食物 → 供应餐食的店'],['英语借入 restaurant','餐馆']],
 'a small restaurant 小餐馆；eat at a restaurant 在餐馆吃饭；book a table at a restaurant 订餐桌；a restaurant menu 餐馆菜单。',
 'a family restaurant；a restaurant near the station。','中文饭店可以指吃饭处，也可能指旅馆；restaurant 指供餐用餐的店，hotel 指住宿的酒店。cafe 常以咖啡、简餐为主，具体经营内容会重合。',
 ('We found a small restaurant beside the river.','我们在河边找到一家小餐馆。'),('Could you book a table at the restaurant for six o’clock?','你能在那家餐馆订一张六点的餐桌吗？'),sources=['https://en.wiktionary.org/wiki/restaurant#English','https://www.etymonline.com/word/restaurant'])
W('restaurants','英 /ˈrestrɒnts/；美 /ˈrestərɑːnts/','餐馆；饭店〔restaurant 的复数〕',
 '一条街上、一个城市里的一家家吃饭的店，就是 restaurants。',
 'restaurant + -s，/t/ 后读 /s/，结尾形成 /nts/。restaurant 是法语借词，背后有恢复体力、补养食物到餐馆的意义变化；复数按英语常见规则加 s。',
 [['法语恢复、补养词族 → restaurant → 英语 restaurant','补养食物 → 餐馆'],['restaurant + -s → restaurants','多家餐馆']],
 'local restaurants 当地餐馆；seafood restaurants 海鲜餐馆；restaurants within walking distance 步行可达的餐馆。',
 'several restaurants nearby；restaurants along the waterfront。','restaurants 是店铺的可数复数，food 通常说食物。restaurant 里的 au 延续借词拼写，学习时按完整单词记，不按字母分别猜音。',
 ('Several restaurants on this street stay open late.','这条街上有几家餐馆营业到很晚。'),('The guide lists restaurants within walking distance of the station.','指南列出了车站附近步行可达的餐馆。'),sources=['https://en.wiktionary.org/wiki/restaurants#English','https://en.wiktionary.org/wiki/restaurant#English','https://www.etymonline.com/word/restaurant'])
W('opposite','英 /ˈɒpəzɪt/；美 /ˈɑːpəzɪt/','对面的；相反的；对面；相反的人或事物',
 '两边面对面摆着，是 opposite 的空间画面；把这个关系用到方向、性质和想法上，就有相反的意思。',
 '经古法语 opposite、oposite 接拉丁 oppositus，来自 oppōnere 放在对面，历史由 ob- 朝向、对着与 pōnere 放构成，ob- 在 p 前同化为 op-。英语 oppose、opposition 与它同族，有各自借入历史。',
 [['拉丁 ob- + pōnere → oppōnere、oppositus','放在对面、对立'],['古法语 opposite／oposite → 英语 opposite','位置在对面 → 性质、方向相反']],
 'the opposite side 对面那一边；the opposite direction 相反方向；opposite the station 在车站对面；the exact opposite 完全相反的人或事物。',
 'sit opposite someone；have opposite views。','opposite the station 可直接接地点，不必加 to；opposite to 在某些比较结构也可用。the opposite of something 常接 of，说明与什么相反。',
 ('The library is opposite the station.','图书馆在车站对面。'),('We walked in opposite directions after leaving the café.','离开咖啡馆后，我们向相反方向走去。'),sources=['https://en.wiktionary.org/wiki/opposite#English','https://www.etymonline.com/word/opposite'])
W('opposites','英 /ˈɒpəzɪts/；美 /ˈɑːpəzɪts/','相反的人或事物；反义词〔opposite 的名词复数〕',
 '把热与冷、开与关放到一起看，它们分别站在意义的两头，可以叫 opposites；性格截然不同的两个人也常这样说。',
 'opposite 名词加 -s，/t/ 后读 /s/。opposite 经法语接拉丁 oppositus 放在对面的，历史含 ob- 与 pōnere 放；名词义很早已随相对、相反分支发展。',
 [['拉丁 oppositus → 法语、英语 opposite','放在对面的 → 相反的一方'],['opposite + -s → opposites','两个或多个相反的人、事物、词']],
 'complete opposites 完全相反的人或事物；exact opposites 恰好相反；opposites attract 性格相反的人相吸引〔常见说法〕。',
 'learn words in pairs of opposites；two opposites。','opposites 可以说词义，也可以说性格、性质；opponents 是比赛、争论中的对手。互为反义词常说 antonyms，日常学习里也能说 opposites。',
 ('Hot and cold are opposites.','hot 和 cold 意思相反。'),('The twins are complete opposites in personality.','这对双胞胎的性格截然相反。'),sources=['https://en.wiktionary.org/wiki/opposites#English','https://en.wiktionary.org/wiki/opposite#English','https://www.etymonline.com/word/opposite'])
W('email','/ˈiːmeɪl/','电子邮件；用电子邮件发送、联系',
 '把信件放到电子通信里传送，是 email。既可以说一封邮件，也可以把“给人发邮件”直接当成动作。',
 '缩自 electronic mail：electronic 的开头 e 与 mail 结合，形成 email；名词随后用作动词。mail 的邮件义较早由袋、邮袋及其中的信件发展，electronic 则属于电、电子的词族。',
 [['electronic + mail → electronic mail','电子方式传送的邮件'],['electronic mail 缩短 → email；名词转用为动词','电子邮件；给人发电子邮件']],
 'send an email 发一封邮件；check your email 查看电子邮件；by email 通过邮件；email me the details 把详情发邮件给我。',
 'an email address；email someone about the meeting。','email 可不可数地说通信方式、邮件总体，也可用 an email 数一封邮件。动词可直接接人：email me；也可接内容，再用 to 指收件人：email the file to me。',
 ('Please send me an email when you have the details.','有了具体信息后，请给我发封邮件。'),('I will email you the map this afternoon.','我今天下午会把地图发邮件给你。'),sources=['https://en.wiktionary.org/wiki/email#English','https://www.etymonline.com/word/email'])
W('emails','/ˈiːmeɪlz/','电子邮件〔复数〕；发电子邮件〔第三人称单数〕',
 '收件箱里一封封信是 emails；一个人经常用邮件把东西发出去，也是 emails。',
 'email + -s，/l/ 后读 /z/。email 缩自 electronic mail，名词和动词共用拼写、读音；emails 是名词复数或现在第三人称单数。',
 [['electronic mail → email','电子邮件；发送电子邮件'],['email + -s → emails','多封邮件；单数主语发邮件']],
 'unread emails 未读邮件；reply to emails 回复邮件；emails the team 给团队发邮件；emails me a copy 发邮件给我一份副本。',
 'sort your emails；emails sent yesterday。','These emails are short 中是复数名词；She emails me every Friday 中是现在动词。reply to emails 常用 to 连接要回复的邮件。',
 ('I read the unanswered emails before the meeting.','开会前，我读了那些还没回复的邮件。'),('She emails the group a short update every Friday.','她每周五都会给小组发邮件，简短说明最新情况。'),sources=['https://en.wiktionary.org/wiki/emails#English','https://en.wiktionary.org/wiki/email#English'])
W('emailed','/ˈiːmeɪld/','已经发邮件；用邮件发送过；email 的过去式和过去分词',
 '邮件发送这个动作已经发生，就是 emailed。句子后面可以交代给谁发了、发了什么。',
 'email + -ed，/l/ 后过去词尾读 /d/，不增加音节。email 是 electronic mail 的缩短形式转作动词后，按普通英语动词形成过去式。',
 [['electronic mail → email 名词、动词','电子邮件 → 用邮件发送'],['email + -ed → emailed','过去发过；已经通过邮件发送']],
 'emailed me 给我发过邮件；emailed the file 把文件发过邮件；emailed it to the team 把它发给了团队；has emailed 已经发了邮件。',
 'emailed yesterday；the document was emailed。','emailed someone 是给某人发邮件；emailed something to someone 交代把什么发给谁。was emailed 说明某物被发出，是否收到、读过还需其他信息。',
 ('She emailed me the revised schedule last night.','她昨晚把修改后的日程发邮件给了我。'),('The completed form was emailed to the office.','填好的表格已通过电子邮件发给办公室。'),sources=['https://en.wiktionary.org/wiki/emailed#English','https://en.wiktionary.org/wiki/email#English'])
W('emailing','/ˈiːmeɪlɪŋ/','正在发邮件；发送电子邮件这一活动；email 的 -ing 形式',
 '把发邮件当成正在进行的动作，或当成一件占用时间的事，就是 emailing。',
 'email + -ing，直接加，保留原有 l。email 缩自 electronic mail，先有电子邮件的名词表达，再作动词及 -ing 形式。',
 [['electronic mail → email 名词、动词','电子邮件 → 发邮件'],['email + -ing → emailing','正在发邮件；发邮件这一活动']],
 'emailing the details 正在把详情发邮件；emailing a colleague 给同事发邮件；spend time emailing 花时间处理、发送邮件。',
 'thanks for emailing；emailing rather than calling。','is emailing 表示现在正在发或相关安排；after emailing、thanks for emailing 中则把动作作为一件事接在介词后。emailing 本身不表示对方已经阅读。',
 ('She is emailing the directions to everyone in the group.','她正在把路线说明发邮件给小组里的每个人。'),('Thanks for emailing the photographs so quickly.','谢谢你这么快就把照片发了过来。'),sources=['https://en.wiktionary.org/wiki/emailing#English','https://en.wiktionary.org/wiki/email#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xo',ROOTS,WORDS)
 extend_lessons()
