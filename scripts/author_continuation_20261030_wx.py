"""Frequent reading forms: conditions, forces, jobs and resources."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0327':dict(words=['condition','conditions'],label='condition → conditions：条件、环境与状况',note='condition 接拉丁 condicio 及说定、约定词族，后来的拼写有其他拉丁形式影响；conditions 在现代有条件、环境、状况等分支。'),
 'C0446':dict(words=['force','forces'],label='force → forces：力量、部队；迫使',note='force 名词、动词经相关法语形式接拉丁 fortis 强壮词族；forces 在 /s/ 后加 /ɪz/。'),
 'B3486':dict(words=['job','jobs'],label='job → jobs：工作职位与具体任务',note='job 早有一份活的表达，更远来源未定；jobs 可数职位，也可数要完成的一项项工作。'),
 'C1045':dict(words=['picture','pictures'],label='picture → pictures：图像；想象出来',note='picture 接拉丁 pictura、pictus、pingere 绘画词族，动词由英语名词发展。'),
 'B3216':dict(words=['call','calls'],label='call → calls：呼叫、电话；称为、要求',note='call 接早期英语与北欧相关呼叫词，calls 可作电话等复数，也可作命名、召唤等动词形式。'),
 'C0973':dict(words=['patient','patients'],label='patient → patients：耐心形容词与病人名词',note='patient 接拉丁 pati 承受的现在分词材料；patients 是病人名词复数，形容词 patient 不靠加 s 标人多。'),
 'C1459':dict(words=['resource','resources'],label='resource → resources：可调用的材料、能力、手段',note='resource 经法语恢复、重新起来词族接拉丁 resurgere，与现代 source 的关系不简化成英语现场 re- 加 source。'),
 'C1105':dict(words=['report','reports'],label='report → reports：报告、报道；汇报',note='report 接拉丁 re- 加 portare 带回来词族；reports 既数多份报告，也可作汇报的第三人称。'),
}
W('conditions','/kənˈdɪʃənz/','条件、条款；环境、状况；疾病、病况等；调节、护理等〔动词形式〕',
 '先看场景：答应合作前提出的要求是 conditions，工作、生活周围的情况也是 conditions；健康语境又可能说几种病况。',
 'condition + -s，词尾 /z/。经法语接拉丁 condicio，与 condicere 共同说定、约定词族相关；英语拼写后受其他拉丁形式影响，现代多个义项分别按搭配理解。',
 [['拉丁 condicio 及相关约定词族 → 法语、英语 condition','条件、状态等历史材料；拼写后有混合影响'],['condition + -s → conditions','多个条件、环境状况等；也有相应动词形式']],
 'working conditions 工作条件、环境；weather conditions 天气状况；terms and conditions 条款和条件；living conditions 生活条件；medical conditions 疾病、病况。作动词时，conditions the hair 可说护理头发，conditions someone to ... 可说训练某人适应某种反应。',
 'under these conditions；conditions for joining。','conditions for joining 说加入的要求，conditions in the room 说房间里的环境。The machine is in good condition 常用单数说整台机器状况良好。',
 ('The team worked well despite the difficult conditions.','尽管条件艰苦，团队还是干得很好。'),('The leaflet explains the conditions for joining the club.','小册子说明了加入俱乐部的条件。'),sources=['https://en.wiktionary.org/wiki/conditions#English','https://en.wiktionary.org/wiki/condition#English','https://www.etymonline.com/word/condition'])
W('forces','英 /ˈfɔːsɪz/；美 /ˈfɔːrsɪz/','力量、作用力；部队、军队；迫使〔force 的第三人称单数〕',
 '推动、拉动或影响事情的力是 forces；有组织地发挥力量的军队也叫 forces。作动词时，是强推某个结果、迫使人做事。',
 'force 已有 e，加 s；/s/ 后增加 /ɪz/。力量名词经法语 force 接拉丁 fortis 强壮的材料；动词经法语 forcer／forcier 等相连路线借入。',
 [['拉丁 fortis 词族 → 法语名词、动词 → force','强壮、力量；强迫、用力'],['force 名词、动词 + -s → forces','多种力量、部队；单数主语迫使']],
 'natural forces 自然力量；market forces 市场力量；armed forces 武装部队；forces someone to ... 迫使某人……；forces the door open 强行打开门。',
 'opposing forces；forces a change of plan。','forces someone to do 的 to 接被迫做的动作。forces 作部队、军队时常用复数；a force 也可说一支队伍或某种作用力，按语境区分。',
 ('Several different forces act on the moving object.','这个运动物体受到几种不同的力。'),('The small room forces us to use folding chairs.','房间太小，我们只能用折叠椅。'),sources=['https://en.wiktionary.org/wiki/forces#English','https://en.wiktionary.org/wiki/force#English'])
W('jobs','英 /dʒɒbz/；美 /dʒɑːbz/','工作职位；任务、活；作业〔计算机等语境〕；job 的复数',
 '一份受雇的职位是 job，要做的一件活也叫 job。jobs 因此既能说社会上有多少岗位，也能说今天还要干几件事。',
 'job + -s，/b/ 后读 /z/。早期英语有 jobbe of work 一份活等表达，更远与一块、一团、动作词等联系有不同假说，未作定论。',
 [['早期英语 jobbe of work 等 → job','一份活；更远来源未定'],['job + -s → jobs','多个职位、任务；成批运行的作业等']],
 'full-time jobs 全职职位；part-time jobs 兼职职位；household jobs 家务活；print jobs 打印任务；jobs to finish 要做完的活。',
 'apply for jobs；several small jobs。','jobs 可数，work 作工作活动常不可数：three jobs 可以是三个职位或三项任务，a lot of work 则说很多工作量。具体是职位还是任务，看前后文。',
 ('She applied for three jobs near her home.','她申请了家附近的三个职位。'),('I have a few small jobs to finish before lunch.','午饭前我还有几件小事要做完。'),sources=['https://en.wiktionary.org/wiki/jobs#English','https://en.wiktionary.org/wiki/job#English'])
W('pictures','英 /ˈpɪktʃəz/；美 /ˈpɪktʃərz/','图片、图画、照片；影片等；在脑中想象〔picture 的第三人称单数〕',
 '看得见的一幅幅图像是 pictures；在脑中把场景摆出来，picture 又可以作想象的动词。',
 'picture 已有 e，加 s，词尾 /z/。拉丁 pictura 绘画、图画接 pictus，即 pingere 绘画的分词，经借入进入英语；动词再由名词形成。',
 [['拉丁 pingere → pictus／pictura → 英语 picture','绘画 → 图画、图像'],['picture 名词、动词 + -s → pictures','多幅图、照片等；单数主语想象']],
 'take pictures 拍照；draw pictures 画画；picture books 图画书；the pictures 英式口语可说电影院、看电影活动；pictures the scene 想象场景。',
 'pictures of the town；pictures on the wall。','pictures 范围比 photos 广，照片是图像的一类，图画、插图等也可叫 pictures。take a picture 常是拍照，draw a picture 是画图，动作不同。',
 ('The children drew pictures of their homes.','孩子们画了自己家的图画。'),('She pictures the room with a larger window and fewer chairs.','她在脑中想象这个房间窗户更大、椅子更少的样子。'),sources=['https://en.wiktionary.org/wiki/pictures#English','https://en.wiktionary.org/wiki/picture#English'])
W('calls','英 /kɔːlz/；美 /kɔːlz, kɑːlz/','电话、呼叫、召唤；请求、判断等；打电话、称为、召唤〔动词形式〕',
 '把声音或信息朝某个人送去，让对方注意，是 call 的直观感觉。电话、呼喊、要求回应都沿这个画面理解；动词又能说给出名称。',
 'call + -s，/l/ 后读 /z/。call 经中古英语 callen 延续，受古英语 ċeallian 与古诺尔斯语 kalla 等相关形式影响，命名、召唤、通话等义逐渐扩展。',
 [['古英语 ċeallian、古诺尔斯语 kalla 等 → 中古英语 callen → call','呼叫、召唤；称呼等'],['call 名词、动词 + -s → calls','多次通话、请求等；单数主语称为、呼叫']],
 'phone calls 电话；missed calls 未接来电；calls for help 求助呼声；calls someone a friend 称某人为朋友；calls for a change 要求改变。',
 'takes calls；calls me every week。','calls for ... 常说某情况需要、某人要求……；calls someone 可说打电话，也可在后接称呼时表示把某人叫作……。多看后面的结构，才能分清。',
 ('I missed two calls while I was on the train.','我在火车上时漏接了两个电话。'),('She calls this small room her office.','她把这个小房间叫作自己的办公室。'),sources=['https://en.wiktionary.org/wiki/calls#English','https://en.wiktionary.org/wiki/call#English'])
W('patients','/ˈpeɪʃənts/','病人、患者；patient 的名词复数',
 '正在接受诊察、治疗、护理等医疗照顾的人，是 patients。这个词说的是人与医疗服务的关系，不等于某一种具体疾病。',
 'patient + -s，/t/ 后读 /s/，结尾 /nts/。经法语接拉丁 patiēns 承受着的，来自 pati 承受；耐心形容词与病人名词在借入历史里已有相关用法。',
 [['拉丁 patī → patiēns → 法语、英语 patient','承受；耐心形容词与病人名词各有相关用法'],['patient 名词 + -s → patients','多位接受医疗照顾的人']],
 'patients at the clinic 诊所的患者；new patients 新接诊患者；patients and staff 患者和工作人员。',
 'patients waiting outside；care for patients。','patients 是病人们；patience 是耐心，常不可数。patient 作耐心的形容词时不随人数加 s：The nurses are patient，意思是护士们有耐心。',
 ('The receptionist asked the patients to take a seat.','接待员请患者们坐下。'),('The leaflet helps patients prepare questions for their appointments.','这份说明帮助患者准备就诊时想问的问题。'),sources=['https://en.wiktionary.org/wiki/patients#English','https://en.wiktionary.org/wiki/patient#English'])
W('resources','英 /rɪˈzɔːsɪz, rɪˈsɔːsɪz/；美 /ˈriːsɔːrsɪz, rɪˈsɔːrsɪz/','资源；可用的材料、人力、时间、能力、手段等；resource 的复数',
 '做一件事能调动什么来帮忙，就是 resources。它可以是钱、人员、自然材料，也可以是教材、时间、经验和应变办法。',
 'resource 已有 e，加 s；结尾 /s/ 后增加 /ɪz/。经法语 ressource、古法语 resourse，接 resourdre 重新起来、恢复，再上接拉丁 resurgere。',
 [['拉丁 resurgere → 古法语 resourdre／resourse → 法语 ressource','重新起来、恢复 → 可依靠的办法、手段'],['英语 resource + -s → resources','多种可调用的资源、支持材料等']],
 'natural resources 自然资源；human resources 人力资源；learning resources 学习资料、资源；limited resources 有限资源；pool resources 汇集资源。',
 'resources for teachers；make good use of resources。','resources 说能调动来做事的材料、能力和手段，sources 常说信息、材料从哪里来。learning resources 可以包括教材，sources for a claim 是支持某说法的出处。',
 ('The website provides free learning resources for adults.','这个网站提供免费的成人学习资料。'),('The two groups pooled their resources to organise the event.','两个小组汇集资源，组织了这场活动。'),sources=['https://en.wiktionary.org/wiki/resources#English','https://en.wiktionary.org/wiki/resource#English'])
W('reports','英 /rɪˈpɔːts/；美 /rɪˈpɔːrts/','报告、报道、汇报；报告、报道〔report 的第三人称单数〕',
 '把得到的信息整理后带给别人，是 reports。可以是几份书面报告，也可以是某个记者、机构正在报道某事。',
 'report + -s，/t/ 后读 /s/。经法语 reporter 接拉丁 re- 往回 + portare 携带，信息带回来、转述的画面帮助理解现代汇报义。',
 [['拉丁 re- + portare → reportare → 法语 reporter → report','带回、转述 → 报告、报道'],['report 名词、动词 + -s → reports','多份报告、报道；单数主语报告']],
 'news reports 新闻报道；annual reports 年度报告；reports of damage 损坏情况报告；reports that ... 报道说……；reports to a manager 向经理汇报、由经理管理。',
 'read the reports；reports directly to ...。','reports that 后接报道内容，reports to 后可接汇报对象、上级。reports 说明有人作了报告，不自动表示报告内容已经被另外核实。',
 ('The reports describe the changes made over the past year.','这些报告描述了过去一年作出的变化。'),('She reports directly to the project manager.','她直接向项目经理汇报。'),sources=['https://en.wiktionary.org/wiki/reports#English','https://en.wiktionary.org/wiki/report#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wx',ROOTS,WORDS)
 extend_lessons()
