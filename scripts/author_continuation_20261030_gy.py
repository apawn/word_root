"""Sphere and photo: scientific layers, fields, light and photographic work."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['希腊 sphaira → 拉丁 sphaera → sphere 等','球、球体'],['科学和比喻构词 -sphere','球形包围层、相关作用范围；并非都严格正圆']]
W('ionosphere','英 /aɪˈɒnəsfɪə/；美 /aɪˈɑːnəsfɪr/','电离层',
 '高空有些气体粒子受能量作用变成带电状态；按这种电离特征圈出一片区域，就叫电离层，和无线电传播关系很大。',
 'iono- 离子、电离 + -sphere 层、区域。ion 来自希腊行进相关命名材料，现代这里指带电粒子；不按 iron 铁去猜。',S+[['iono- + -sphere → ionosphere','以显著电离特征界定的大气区域']],
 'the Earth’s ionosphere 地球电离层，changes in the ionosphere 电离层变化，study the ionosphere 研究电离层。按电离情况分区，可和按温度划分的大气层重叠。',
 'the Earth’s ionosphere；changes in the ionosphere。',
 'ionosphere 是大气中按电离特征讨论的区域，magnetosphere 按磁场影响范围说；两词不能只当高空的一层又一层硬壳。',
 ('The study examines how the ionosphere affects radio signals.','研究考察电离层怎样影响无线电信号。'),('Conditions in the ionosphere change between day and night.','电离层的情况会在昼夜间变化。'),sources=['https://en.wiktionary.org/wiki/ionosphere#English','https://www.spaceweather.gov/phenomena/ionosphere'])
W('magnetosphere','英 /mæɡˈniːtəsfɪə/；美 /mæɡˈniːtəˌsfɪr/','磁层、磁场占主导的空间区域',
 '地球周围有一片空间，粒子运动强烈受地球磁场影响；它会被太阳风压扁、拖出尾部，名字里有 sphere 却不要求整齐圆球。',
 'magneto- 磁 + -sphere 范围、区域。magnet 材料历史关联磁石名称，构词中的 o 是常见连接元音，不单独表一种物质。',S+[['magneto- + -sphere → magnetosphere','以天体自身磁场占主导来界定的区域']],
 'the Earth’s magnetosphere 地球磁层，the shape of the magnetosphere 磁层形状，solar wind and the magnetosphere 太阳风与磁层。',
 'the Earth’s magnetosphere；the shape of the magnetosphere。',
 'magnetosphere 是磁场作用相关范围，atmosphere 是气体包围层；空间有关系，但不等于同一个东西换名字。',
 ('The solar wind changes the shape of the magnetosphere.','太阳风会改变磁层的形状。'),('The satellite measured particles in the Earth’s magnetosphere.','卫星测量了地球磁层中的粒子。'),sources=['https://en.wiktionary.org/wiki/magnetosphere#English','https://science.nasa.gov/heliophysics/focus-areas/magnetosphere-ionosphere/'])
W('photosphere','英 /ˈfəʊtəsfɪə/；美 /ˈfoʊtəˌsfɪr/','光球层；球形全景照片〔另一用法〕',
 '天文学里是恒星向我们放出可见光、看起来像表面的那层；全景摄影里则可说把四周场景包成球面的一张照片。前半段分别选光和照片。',
 '天文词是 photo- 光 + -sphere 层；全景照片用法又能把 photo 当 photograph 的短形式，配 sphere 球面。不是所有 photo- 都必须译照片。',S+[['photo- 光 + -sphere → photosphere','恒星的可见光表面层'],['摄影用法 photo + sphere','呈球面视野的全景照片']],
 'the solar photosphere 太阳光球层，sunspots on the photosphere 光球层上的太阳黑子；a 360-degree photosphere 球形全景照片。太阳没有地面那样的固体表面。',
 'the solar photosphere；sunspots on the photosphere；a 360-degree photosphere。',
 'photosphere 光球层，photograph 照片；照片用法看软件、摄影上下文，天文中的表面也不等于岩石外壳。',
 ('Sunspots appear on the solar photosphere.','太阳黑子出现在太阳光球层上。'),('The virtual tour opens with a photosphere of the courtyard.','虚拟导览首先打开庭院的球形全景照片。'),sources=['https://en.wiktionary.org/wiki/photosphere#English','https://solarscience.msfc.nasa.gov/surface.shtml'])
R('A2085','球体到包围层、作用范围、活动领域','-SPHERE：像包围成球的层，也能是某种作用范围','atmosphere 气体；ionosphere 电离；magnetosphere 磁场；photosphere 光；blogosphere 网络活动领域。',
 '球的画面帮助你抓包围、范围，别强求每个术语都是几何正球。不同科学词按气体、温度、电离、磁场等不同尺度命名，不只是顺序堆壳。',
 'sphaira → sphaera/sphere → -sphere；atmo-/strato-/tropo-/iono-/litho-/magneto-/photo- + -sphere；blogosphere 活动领域比喻。',
 [['大气相关区域','atmosphere · troposphere · stratosphere · ionosphere'],['其他实体、作用区域','lithosphere · magnetosphere · photosphere'],['网络领域比喻','blogosphere']],
 'ionosphere/magnetosphere 电离与磁场尺度不同；photosphere 不是固体壳；-sphere 可只是作用范围。',
 'The course compares the atmosphere, ionosphere and magnetosphere without treating them as identical kinds of layers.\n\n课程对比大气、电离层和磁层，并说明它们不是按同一种标准划分的层。','atmosphere troposphere stratosphere ionosphere lithosphere magnetosphere photosphere blogosphere')
P=[['希腊 phōs、词干 phōt-','光'],['科学 photo- 与 photography 等','光的作用；光成像 → 摄影、照片相关材料']]
W('photojournalism','英 /ˌfəʊtəʊˈdʒɜːnəlɪzəm/；美 /ˌfoʊtoʊˈdʒɜːrnəlɪzəm/','摄影新闻、新闻摄影',
 '用一张或一组照片讲清新闻发生了什么；不只是拍得好看，还要承担新闻记录、叙事的作用。',
 'photo- 摄影、照片 + journalism 新闻工作。这里 photo 是由光成像发展来的摄影义，不是光线本身正在写稿。',P+[['photo- + journalism → photojournalism','以摄影图像为主要方式的新闻工作']],
 'documentary photojournalism 纪实新闻摄影，a photojournalism project 新闻摄影项目，study photojournalism 学习新闻摄影。',
 'study photojournalism；a photojournalism project。',
 'photojournalism 是领域、工作，photojournalist 是从业者；portrait photography 人像摄影不必都是新闻报道。',
 ('She studied photojournalism before joining the newspaper.','她进报社前学的是新闻摄影。'),('The exhibition explores photojournalism during major social changes.','展览探讨重大社会变迁中的新闻摄影。'))
W('photojournalist','英 /ˌfəʊtəʊˈdʒɜːnəlɪst/；美 /ˌfoʊtoʊˈdʒɜːrnəlɪst/','摄影记者',
 '不只是拿相机的人，而是用照片报道新闻、记录现场的记者；photo 说明主要表达方式。',
 'photo- 摄影 + journalist 记者；后者与 journal 记录、刊物 + -ist 人物材料相关。可和 photojournalism 作为人、行业一对来记，不必强断定二者在英语中的出现顺序。',P+[['photo- + journalist → photojournalist','以摄影方式报道新闻的记者']],
 'a freelance photojournalist 自由摄影记者，a newspaper photojournalist 报社摄影记者，work as a photojournalist 当摄影记者。',
 'a freelance photojournalist；a newspaper photojournalist。',
 'photojournalist 包含新闻工作身份，photographer 更宽是摄影者；游客拍现场照片不自动因此成为职业摄影记者。',
 ('A photojournalist documented the evacuation.','一位摄影记者记录了撤离过程。'),('The newspaper sent a photojournalist to the ceremony.','报社派摄影记者去报道仪式。'))
W('photorealistic','英 /ˌfəʊtəʊˌrɪəˈlɪstɪk/；美 /ˌfoʊtoʊˌriːəˈlɪstɪk/','照片般逼真的、照相写实的',
 '明明是绘画、三维渲染，却让人一眼像在看照片；说的是视觉效果，不保证画面里的事件真实发生过。',
 'photo- 照片 + realistic 逼真的。realistic 自己和 real 真实、-istic 相关形容词形式对应；不能因为逼真就判定它是证据照片。',P+[['photo- + realistic → photorealistic','像照片一样逼真的视觉表现']],
 'a photorealistic image 照片般逼真的图像，photorealistic rendering 逼真渲染，a photorealistic painting 照相写实画。',
 'a photorealistic image；photorealistic rendering；a photorealistic painting。',
 'photorealistic 看着像照片，photographic 与摄影相关；真实照片和逼真合成图不是只靠这个形容词就能分真伪。',
 ('The game uses photorealistic landscapes.','游戏使用照片般逼真的风景画面。'),('Her photorealistic painting was mistaken for a photograph.','她的写实画被人误认成了照片。'))
R('A1976','光；由光成像延伸为摄影、照片','PHOTO-：科学先读光，影像语境常读摄影、照片','photograph → photographic；photosynthesis → photosynthetic；photojournalism/photojournalist 行业与人物；photorealistic 照片般逼真。',
 'photons、光合作用里不是照片，摄影记者里也不只是物理光线。先看构词场景，前半段的光与照片两层关系就能分清。',
 'phōs/phōt- → photo-；接 graph、synthesis、voltaic、genic 等科学材料；photo- 接 journalism/journalist/realistic；photosphere 在两种领域可作不同解释。',
 [['光成像与摄影','photograph · photographic · photocopy · photogenic'],['新闻摄影行业和人物','photojournalism · photojournalist'],['视觉逼真','photorealistic'],['光的作用和感受','photon · photosynthesis · photosynthetic · photovoltaic · photoelectric · photoelectron · photosensitive · photoreceptor · photochemical · photoresist'],['光的测量与层','photometry · photometric · photosphere']],
 'photo- 不总是照片；photojournalism/photojournalist 行业与人；photorealistic 不保证事件真实；photosphere 先看天文还是全景摄影。',
 'The photojournalist studied light but did not mistake photorealistic art for documentary evidence.\n\n摄影记者研究光线，也会区分照片般逼真的艺术画面和纪实证据。','photograph photographic photocopy photogenic photojournalism photojournalist photorealistic photon photosynthesis photosynthetic photovoltaic photoelectric photoelectron photosensitive photoreceptor photochemical photoresist photometry photometric photosphere')
if __name__=='__main__':save('continuation_20261030_gy',ROOTS,WORDS)
