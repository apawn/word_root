"""Seven weekday names: inherited compounds, naming traditions and everyday use."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2422':dict(words=['day','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],label='day 与七个星期名：月、太阳及古代神名',note='星期名保留古英语的 day 组合；有些部分已随发音、拼写变化而不透明。统一按星期一到星期日阅读，这个阅读顺序不宣称所有历法都用同一天起周。'),
 'B2638':dict(words=['moon','Monday'],label='moon → Monday：月亮之日',note='Monday 延续古英语月亮的所属形式加 day 的组合，是历史意译命名；今天不按现代 moon 的完整发音逐字拼读。'),
 'B2467':dict(words=['sun','Sunday'],label='sun → Sunday：太阳之日',note='Sunday 承古英语 sunnandæg，太阳名称与 day 的旧组合。'),
}
W('Monday','/ˈmʌndeɪ/〔末尾也可弱读 /di/〕','星期一、周一',
 '先给这一格贴上月亮的图景：Monday 原来的字面就是月亮之日。今天只要把它当固定的星期名来用。',
 '古英语 monandæg，由 mona 月亮的所属形式 monan 加 dæg 日组成，经缩短、语音变化成为 Monday；是对拉丁月亮日等命名传统的意译继承。',
 [['古英语 monan + dæg → monandæg','月亮的日子'],['中古英语 monedai 等 → Monday','旧组合缩短为现代星期名']],
 'on Monday 在周一；Monday morning 周一早上；next Monday 下周一；every Monday 每周一；Mon. 常见缩写。',
 'a Monday meeting；by Monday。','on Monday 说明在周一，by Monday 常说明到周一之前或最迟周一。next Monday、every Monday 前通常不再加 on。英语星期名首字母大写。',
 ('The course begins on Monday.','课程星期一开始。'),('Please send me the draft by Monday.','请最迟在星期一把草稿发给我。'),sources=['https://www.etymonline.com/word/Monday','https://en.wiktionary.org/wiki/Monday#English'])
W('Tuesday','英 /ˈtjuːzdeɪ/、/ˈtʃuːzdeɪ/；美 /ˈtuːzdeɪ/','星期二、周二',
 'Tuesday 中较难认的一段，是古代神名 Tiw 留下来的痕迹。把它记为 Tiw 的日子，比硬背一串不熟悉的字母更有线索。',
 '古英语 Tiwesdæg：Tiw 的所属形式 Tiwes + dæg 日。命名传统把日耳曼战神与罗马 Mars 的对应关系用于星期名称，再经中古英语演变为 Tuesday。',
 [['Tiwes + dæg → 古英语 Tiwesdæg','Tiw 的日子'],['中古英语 Tiuesdai 等 → Tuesday','旧神名、所属形式和 day 组合发生变化']],
 'on Tuesday 在周二；Tuesday afternoon 周二下午；every Tuesday 每周二；Tue.、Tues. 常见缩写。',
 'a Tuesday appointment；this Tuesday。','英式常见开头 /tjuː/ 或合流后的 /tʃuː/，美式常见 /tuː/。它们都属于常见读法，主重音在第一节。',
 ('Our class meets every Tuesday afternoon.','我们班每周二下午上课。'),('I will be back on Tuesday.','我星期二回来。'),sources=['https://www.etymonline.com/word/Tuesday','https://en.wiktionary.org/wiki/Tuesday#English'])
W('Wednesday','/ˈwenzdeɪ/〔末尾也可弱读 /di/〕','星期三、周三',
 '拼写里还看得出旧名字的痕迹，现代读音却已经缩短，常按 Wenz-day 的节奏读。它的命名来自 Woden 的日子。',
 '古英语 Wodnesdæg，由 Woden 的所属形式 Wodnes 与 dæg 日组成。Woden 是与北欧 Odin 对应的日耳曼神名；中古英语多种写法逐渐形成 Wednesday，读音较早已收缩。',
 [['Wodnes + dæg → Wodnesdæg','Woden 的日子'],['中古英语 Wednesdai 等 → Wednesday','拼写保留较多历史痕迹，常见读音缩短']],
 'on Wednesday 在周三；Wednesday evening 周三晚上；next Wednesday 下周三；Wed. 常见缩写。',
 'the Wednesday meeting；until Wednesday。','常见标准读音是 /ˈwenzdeɪ/，不用把拼写中的每个字母都分出一音节。记拼写可把 Wednes 与 day 分段，再单独记读音。',
 ('The library opens late on Wednesday.','图书馆星期三较晚开门。'),('We moved the meeting from Wednesday to Thursday.','我们把会议从星期三改到了星期四。'),sources=['https://www.etymonline.com/word/Wednesday','https://en.wiktionary.org/wiki/Wednesday#English'])
W('Thursday','英 /ˈθɜːzdeɪ/；美 /ˈθɜːrzdeɪ/','星期四、周四',
 '这一天的旧名字与雷神有关。把雷鸣的画面放在 day 前，就能记住 Thursday 里较不透明的 Thurs 一段。',
 '古英语 Thunresdæg 是雷神 Thunor 的日子；后有缩短形式，可能受古诺尔斯语 Thorsdagr 影响。Thunor 与 Thor 是相关日耳曼传统中的神名，现代 Thursday 经这些旧形式演变。',
 [['古英语 Thunresdæg','雷神 Thunor 的日子'],['缩短形式、可能的北欧语影响 → Thursday','旧日名逐步形成现代词形']],
 'on Thursday 在周四；Thursday morning 周四早上；by Thursday 最迟到周四；Thu.、Thur.、Thurs. 常见缩写。',
 'this Thursday；Thursday’s class。','Thursday 开头 /θ/ 要与 Tuesday 的 /t/ 或 /tʃ/ 区分。神名是历史命名材料，现代使用时它就是固定星期名。',
 ('We are flying home on Thursday.','我们星期四坐飞机回家。'),('Can you finish the drawing by Thursday?','你能最迟在星期四完成这幅画吗？'),sources=['https://www.etymonline.com/word/Thursday','https://en.wiktionary.org/wiki/Thursday#English'])
W('Friday','/ˈfraɪdeɪ/〔末尾也可弱读 /di/〕','星期五、周五',
 'Friday 的 Fri 留着一位日耳曼女神名称的痕迹。今天在许多人的日常安排里，它也常是工作周接近结束的一格。',
 '古英语 Frigedæg，由 Frige 的日名材料加 dæg 日组成，常联系女神 Frigg 的名字。古代传统中她与 Freyja 有相近、交叠的联系，但不能简单把两个神名全当成同一个词。',
 [['古英语 Frige + dæg → Frigedæg','女神名称 + 日'],['Frigedæg → Friday','经过语音、拼写变化形成现代星期名']],
 'on Friday 在周五；Friday night 周五晚上；this Friday 本周五；every Friday 每周五；Fri. 常见缩写。',
 'a Friday evening；by Friday afternoon。','Friday night 中 Friday 直接修饰 night，on Friday night 说在周五那一夜。on Friday afternoon 是在周五下午，by Friday afternoon 常说最迟周五下午。',
 ('We usually cook together on Friday evenings.','我们通常周五晚上一起做饭。'),('The application must arrive by Friday afternoon.','申请材料必须最迟在星期五下午送达。'),sources=['https://www.etymonline.com/word/Friday','https://en.wiktionary.org/wiki/Friday#English'])
W('Saturday','英 /ˈsætədeɪ/；美 /ˈsætərdeɪ/','星期六、周六',
 'Saturday 保存的是 Saturn 的旧名称线索：土星、萨图恩之日。它与 Sunday 的太阳日、Monday 的月亮日一起，留下古代七日命名传统。',
 '古英语 Saeternesdaeg 等形式由 Saetern 的所属形式加 daeg 日组成，部分意译拉丁 Saturni dies。现代词中早期名称的元音、音节发生变化，形成 Saturday。',
 [['拉丁 Saturni dies → 古英语相应日名','Saturn 的日子；日用本族词替换'],['古英语 Saeternesdaeg 等 → Saturday','所属形式和日组合，经音变、缩短延续']],
 'on Saturday 在周六；Saturday morning 周六早上；next Saturday 下周六；Saturdays 每逢周六；Sat. 常见缩写。',
 'a Saturday afternoon；from Saturday to Monday。','Saturday 作为星期名首字母大写。Saturday mornings 常指每个周六的早上；a Saturday morning 可说某一个周六的早上。',
 ('We are going to the market on Saturday.','我们星期六要去市场。'),('She works at the bookshop on Saturday mornings.','她每周六早上在书店工作。'),sources=['https://www.etymonline.com/word/Saturday','https://en.wiktionary.org/wiki/Saturday#English'])
W('Sunday','/ˈsʌndeɪ/〔末尾也可弱读 /di/〕','星期日、周日',
 'sun 是太阳，day 是日子；Sunday 的旧字面太阳之日，今天也最容易从字形直接看出来。',
 '古英语 sunnandæg，由 sunne 太阳的相应屈折形式 sunnan 加 dæg 日组成，是对拉丁太阳日等名称的意译；现代 sun、Sunday 各自延续这些本族词形。',
 [['古英语 sunnan + dæg → sunnandæg','太阳之日'],['中古英语相关形式 → Sunday','现代星期日名称']],
 'on Sunday 在周日；Sunday afternoon 周日下午；every Sunday 每周日；Sunday best 最好的、较正式的衣服；Sun. 常见缩写。',
 'a quiet Sunday；the Sunday newspaper。','Sunday 的旧太阳日命名已固定为星期名。谈固定习惯可用 every Sunday 或 on Sundays；具体一天则常用 on Sunday。',
 ('We usually have a long walk on Sunday afternoons.','我们通常周日下午会散步很久。'),('The museum is closed on Sundays.','博物馆每逢星期日闭馆。'),sources=['https://www.etymonline.com/word/Sunday','https://en.wiktionary.org/wiki/Sunday#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vx',ROOTS,WORDS)
 extend_lessons()
