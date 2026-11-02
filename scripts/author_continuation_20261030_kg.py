"""Franchise, imperial, powder, realistic and clip."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
F=[['古法语 franc 自由 → franchise 自由、豁免','获准免于某种限制，或享有特定权利'],['英语 franchise 的权利、许可支线','选举权；特许经营权、相应企业；体育联盟中的队伍'],['名称与作品的扩展','共享角色、世界观等的系列作品']]
W('franchise','/ˈfræntʃaɪz/','特许经营权、加盟企业；选举权；职业球队；系列作品；授予特许经营权',
 '起点是自由、获准享有某种权利。商业里变成获准用某个品牌经营，体育里可指联盟中的球队，影视里又扩到持续开发的系列作品。',
 '经中古英语 franchise、fraunchise，借古法语 franchise，来自 franc 自由。动词另接法语 franchir 使自由等相关形式；现代多用于授权经营。',F,
 'a fast food franchise 快餐加盟店，the franchise 选举权〔特定语境〕，a film franchise 系列电影，franchise a business 把经营模式授权给加盟方。',
 'a fast food franchise；a film franchise；grant a franchise。',
 'franchise 不一定指门店，也可指经营权、球队、系列作品。电影 franchise 可能跨电影、剧集、小说，不要求每部都直接续前一部。',
 ('She runs a small coffee franchise.','她经营一家小型咖啡加盟店。'),('The studio plans another film in the franchise.','制片公司打算再拍一部这个系列的电影。'),sources=['https://en.wiktionary.org/wiki/franchise#English','https://www.merriam-webster.com/dictionary/franchise'])
W('franchisee','/ˌfræntʃaɪˈziː/','加盟方、受许经营者',
 '品牌允许别人使用它的名称、模式经营；接受这项许可的一方，就是 franchisee。',
 'franchise + -ee，表示接受授权的一方。末尾重读 /ziː/；不是英语 see 看的独立成分。',F[:2]+[['franchise + -ee → franchisee','得到特许经营许可的一方']],
 'a local franchisee 当地加盟商，the franchisee’s store 加盟方的门店。一个加盟方也可能经营多家门店。',
 'a local franchisee；a franchisee’s store。',
 'franchisee 接受许可，franchisor 授出许可。二者角色相对，不是同一个门店里的员工与店长之分。',
 ('The franchisee opened a second store in the town.','加盟商在镇里开了第二家店。'),('Each franchisee received a training manual.','每家加盟商都收到一份培训手册。'))
W('franchisor','英 /ˈfræntʃaɪzə/；美 /ˌfræntʃaɪˈzɔːr/','特许经营授权方、品牌授权商',
 '把品牌、经营方式等许可给加盟方使用的一方，是 franchisor。抓住授权往外给的方向。',
 'franchise 授权经营 + -or，标示执行这一行为的一方。英美重音、词尾存在不同读法。',F[:2]+[['franchise + -or → franchisor','授出特许经营许可的一方']],
 'the franchisor’s brand 授权方的品牌，support from the franchisor 授权方提供的支持。角色名称本身不规定所有合同细节。',
 'a franchisor and its franchisees；the franchisor’s brand。',
 'franchisor 授权，franchisee 获授权；franchise 是许可、相应企业等。先辨角色再看句子。',
 ('The franchisor supplied signs for the new shop.','授权方给新店提供了招牌。'),('The franchisees met with the franchisor to discuss training.','加盟方与授权方会面，讨论培训。'),sources=['https://en.wiktionary.org/wiki/franchisor#English','https://www.merriam-webster.com/dictionary/franchisor'])
R('B4562','自由、特定权利，走向授权经营及其他许可、系列名称','FRANCHISE：历史起点是获准享有权利','franchise → franchisee 接受授权；franchisor 授出授权。',
 '商业角色看许可方向，体育、选举、影视则按各自固定语境理解。不要看到 franchise 就只想到连锁餐厅。',
 'franc 自由 → franchise；-ee 接受者，-or 行为方。',
 [['基础词与相对角色','franchise · franchisee · franchisor']],
 'franchisee 获授权，franchisor 授权；film franchise 说系列作品。',
 'The franchisor gave the new franchisee a training schedule.\n\n授权方给新加盟商一份培训安排。','franchise franchisee franchisor')
R('B3646','帝国、帝权及扩张体系相关的性质、主张与人','IMPERIAL：先看帝国与帝权，再分派生词的角色','imperial → imperialism、imperialist、imperialistic。',
 '皇室、帝国行政的 imperial，与主张或实行对外扩张的 imperialism 不应在所有语境里直接互换。',
 '拉丁 imperium 统治、权力 → imperialis → imperial；-ism 体系，-ist 人，-istic 相应性质。',
 [['性质与体系','imperial · imperialism'],['人与相关性质','imperialist · imperialistic']],
 'imperial 可中性描述历史帝国机构；imperialistic 常评价扩张、支配倾向。',
 'The chapter contrasts imperial administration with imperialism.\n\n这一章比较帝国行政与帝国主义。','imperial imperialism imperialist imperialistic')
R('B3140','细小颗粒的物质与相关用途、质地','POWDER：把物质看成细小颗粒组成的粉','powder → powdery；gunpowder 是固定复合名称。',
 '面粉、化妆粉、细雪等对象不同，粉状的共同形态让同一个词能扩展到不同领域。',
 '法语 poudre 等上接拉丁 pulvis、pulver- 尘、粉；-y 形成粉状、覆粉等性质。',
 [['物质、用途与质地','powder · gunpowder · powdery']],
 'powder 是粉状物，powdery 形容粉状、像粉或覆粉；gunpowder 是特定材料名称。',
 'A powdery layer covered the old box.\n\n一个粉状薄层覆在旧盒子上。','powder gunpowder powdery')
Q=[['拉丁 rēs 事物 → reālis → real','实际、真实'],['realist + -ic → realistic','符合现实条件；表现得像真实世界'],['否定和副词扩展','unrealistic；realistically']]
W('realistic','/ˌrɪəˈlɪstɪk/','切合实际的；逼真、写实的',
 '计划按现实条件能做成，是 realistic；画面像真实世界，也可以 realistic。前者谈可行，后者谈表现效果。',
 'realist + -ic，联系 real 实际、真实这一词族。现代常从实际条件和如实表现两条线理解。',Q[:2],
 'a realistic goal 切实目标，a realistic estimate 实际合理的估计，realistic graphics 逼真图形，be realistic about 对……面对现实。',
 'a realistic goal；a realistic estimate；realistic graphics。',
 'realistic model 可以是仿真模型，不代表模型就是 real 的原物。realistic plan 则是在现实中有望执行的计划。',
 ('We need a realistic deadline for the project.','我们需要给项目定个切实可行的期限。'),('The film uses realistic models of insects.','电影用了很逼真的昆虫模型。'))
W('unrealistic','/ˌʌnrɪəˈlɪstɪk/','不切实际的；不逼真、不符合现实的',
 '时间、人手、预算摆在那里，目标却远超条件，就说 unrealistic。表现出来的画面不像真实情况，也可用它评价。',
 'un- 不 + realistic，否定切合实际、逼真等性质。',Q+[ ['un- + realistic → unrealistic','不符合现实条件或真实表现']],
 'unrealistic expectations 不切实际的期望，an unrealistic deadline 不现实的期限，an unrealistic portrayal 失真的描写。',
 'unrealistic expectations；an unrealistic deadline。',
 'unrealistic 评价某个目标、表现与现实不合；不表示故事本身必须发生在真实世界。虚构世界也可以有可信的内部逻辑。',
 ('It is unrealistic to finish all this work in one afternoon.','想一下午做完这些工作不切实际。'),('The story gives an unrealistic picture of village life.','故事对乡村生活的描写不符合实际。'))
W('realistically','/ˌrɪəˈlɪstɪkli/','切合实际地；逼真地；实事求是地说',
 'Realistically 放句首，像提醒大家先把现实条件算进来；描写画法、演法时，又是在说表现得逼真。',
 'realistic + -ally。-ic 结尾形容词常用 -ally 形成副词，实际读音通常不把每个字母逐个展开。',Q,
 'think realistically 现实地考虑，portray realistically 逼真地刻画，Realistically, ... 实事求是地说……。',
 'think realistically；portray realistically；Realistically, ...。',
 'realistically 常评估可行性或表现方式；really 常是确实、很。We can realistically finish 表有实际可能，不只是加强肯定语气。',
 ('Realistically, we can finish two chapters today.','实事求是地说，我们今天能完成两章。'),('The artist painted the old hands realistically.','画家把那双苍老的手画得很逼真。'))
R('B4286','符合现实的可行性，以及接近真实的表现','REALISTIC：一问做不做得到，一问像不像实际情况','realistic → realistically；unrealistic 否定；photorealistic 强调照片般逼真。',
 '期限、预算、目标主要看可行性；绘画、图形、表演主要看表现。先判断在谈哪一种实际。',
 'realist + -ic → realistic；-ally 副词，un- 否定；photo- 照片相关。',
 [['性质、副词与否定','realistic · realistically · unrealistic'],['照片般的表现效果','photorealistic']],
 'realistic 不等于 real；realistically 不等于 really；不现实的期限与不逼真的画面是不同对象。',
 'Realistically, the team needs another week to make the graphics more realistic.\n\n实事求是地说，团队还需要一周，让图形更逼真。','realistic realistically unrealistic photorealistic')
C=[['古英语 clyppan → 中古英语 clippen','拥抱、抱紧 → 夹住、扣住'],['古诺尔斯语 klippa → 英语 clip','剪、修剪 → 剪下的片段'],['clip + -er、-ing','剪切器具、剪下物；另有快速帆船等固定义']]
W('clip','/klɪp/','夹子、夹住；剪、修剪；音视频片段；擦碰',
 '夹住纸张是一条线，剪掉一小截是另一条线。电影片段像从长片里取出的一段；夹板则直接靠夹子固定纸张。',
 '夹住义承古英语 clyppan 拥抱、抱紧；剪切义借斯堪的纳维亚语，联系古诺尔斯语 klippa。两个来源后来同形，现代还有擦碰、短促打击等扩展。',C[:2],
 'a paper clip 回形针，clip papers together 把纸夹在一起，clip a hedge 修剪树篱，a video clip 视频片段，clip a mirror 擦碰后视镜。',
 'a paper clip；clip papers together；a video clip。',
 'a clip 可以夹住东西，也可以是剪出的片段，先看搭配。clipboard 用的是夹持义，不是因为板子由视频剪成。',
 ('She clipped the papers together.','她把纸张夹在一起。'),('We watched a short clip from the documentary.','我们看了纪录片的一个短片段。'))
W('clipping','/ˈklɪpɪŋ/','剪下物；剪报；修剪；截短、截词',
 '剪草后留下 grass clippings，剪报收集的是 newspaper clippings。语言里把较长词截短，也叫 clipping。',
 'clip 剪 + -ing，双写 p。可指过程，也可指剪下的东西；语言学里再用来命名截短构词。',C[1:2]+[['clip + -ing → clipping','剪的过程、剪下物；词语截短']],
 'grass clippings 碎草，newspaper clippings 剪报，word clipping 截短构词，如 advertisement 变 ad。电子信号 clipping 则说超过限度后波形被截平的现象。',
 'grass clippings；newspaper clippings；word clipping。',
 'clipping 可以是剪下的一张报刊材料；clip 在现代媒体里更常直接说音视频短段。缩略构词还包括首字母缩写等其他方法，不能全叫 clipping。',
 ('He kept newspaper clippings in a folder.','他把剪报保存在文件夹里。'),('The gardener collected the grass clippings.','园丁收起剪下的碎草。'))
W('clipper','英 /ˈklɪpə/；美 /ˈklɪpər/','修剪工具、理发推子〔常用复数〕；快速帆船',
 '剪指甲、理头发的工具可以叫 clippers；海事历史里的 clipper 却是以速度著称的一类帆船，要按固定船名认。',
 'clip 剪 + -er，起初可说修剪的人。船名大概联系 clip 快速移动的用法，也可能受荷兰语快马词影响，不能说船用来剪头发。',C[1:]+[['快速移动的相关用法 → clipper 帆船','名称突出快速；具体命名影响有讨论']],
 'nail clippers 指甲剪，hair clippers 理发推子，a clipper ship 快速帆船。修剪工具常用复数，也可用 a pair of clippers。',
 'nail clippers；hair clippers；a clipper ship。',
 'clipper 的工具义和船名必须看对象。普通剪刀常叫 scissors，hair clippers 常指推剪头发的工具。',
 ('The barber cleaned the hair clippers.','理发师清洁了理发推子。'),('The museum has a model of a tea clipper.','博物馆有一艘运茶快速帆船的模型。'),sources=['https://en.wiktionary.org/wiki/clipper#English','https://www.etymonline.com/word/clipper'])
R('B4116','夹紧与剪切两条同形来源，扩到片段、工具与船名','CLIP：夹住东西与剪下一段要分线理解','clip → clipping、clipper；clipboard 用夹持义；clipper 帆船看快速移动相关命名。',
 '把两条最基本的动作区分开，回形针、剪报、视频片段、夹板的关系就清楚了。',
 'clyppan 抱紧 → 夹持 clip；klippa 剪 → 剪切 clip；-ing 过程或结果，-er 人或器具。',
 [['基础与夹持用品','clip · clipboard'],['剪下物与器具、船名','clipping · clipper']],
 'clip 的片段义不等于夹子；clippers 工具常用复数；船名词源有不确定处。',
 'She put the clipping on the clipboard and secured it with a clip.\n\n她把剪报放在夹板上，用夹子固定。','clip clipboard clipping clipper')
if __name__=='__main__':save('continuation_20261030_kg',ROOTS,WORDS)
