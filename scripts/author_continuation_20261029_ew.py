"""Load: carrying, digital transfer and amounts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
L=[['古英语 lād 行程、运送 → 中古英语 lode、loade','运送 → 搬运的负荷'],['现代 load','货物、负担；装载 → 加载与数据传送']]
def H(f,m):return L+[[f,m]]
W('load','英 /ləʊd/；美 /loʊd/','负荷；一批装载物；装载；加载',
 '放到车上、机器里、系统里让它承担的东西都可想成负载；具体是货、工作还是数据，看对象。',
 '接古英语 lād 行程、运送相关词，中古英语发展出负担、载量义；与 lode 矿脉等形式后来分化。现代计算机加载接把内容装入可用位置的画面。',L,
 'a heavy load 重负载，a load of washing 一批洗衣物，load a truck 给卡车装货，load a page 加载页面；loads of 口语很多。',
 'a heavy load；load a truck；load a page；loads of。',
 'load 装载的量或动作，weight 具体重量不等同；一批资料可 load into memory，不需物理卡车。',
 ('Workers loaded the boxes onto the truck.','工人把箱子装上卡车。'),('The page took several seconds to load.','页面花了几秒钟才加载好。'))
W('loaded','英 /ˈləʊdɪd/；美 /ˈloʊdɪd/','装满、装有的；带偏向的；口语有钱的',
 '基本是东西已经装进去了；问题里塞了预设，便成 loaded question，口语 loaded 还可说富得很。',
 'load + -ed，末尾 /ɪd/ 单独成音节。实物装入与抽象满载预设、资源的比喻在不同搭配中保留。',H('load + -ed → loaded','已装入 → 满载；含预设、偏向；富有'),
 'a loaded truck 满载卡车，a loaded question 带预设或诱导的问题，loaded with detail 充满细节；They are loaded 是他们很有钱。',
 'a loaded truck；a loaded question；loaded with；They are loaded。',
 'loaded question 不是文件已加载的问题；loaded 一词不能自动告诉你装的是什么。',
 ('The van was loaded with furniture.','货车里装满了家具。'),('The interviewer asked a loaded question about who was to blame.','采访者问了一个带着责任预设的问题。'))
W('loader','英 /ˈləʊdə/；美 /ˈloʊdər/','装载工、装载机；加载程序',
 '谁把东西装进去，或者哪个装置、程序负责加载，都能从这个角色理解。',
 'load + -er，执行装载、加载的人或物。现代工程与软件语境分别有装载机、加载程序。',H('load + -er → loader','装入的主体 → 人员、设备、程序'),
 'a front loader 前装载机，a boot loader 引导加载程序；具体是机器还是软件由场景决定。',
 'a front loader；a boot loader；a file loader。',
 'loader 不永远是工人；download 下载动词则描述传送方向，不是装载者。',
 ('The loader moved gravel into the truck.','装载机把碎石装进卡车。'),('The boot loader starts the operating system.','引导加载程序启动操作系统。'))
W('upload','动词英 /ˌʌpˈləʊd/、美 /ˌʌpˈloʊd/；名词常前重音','上传；上传的文件、过程',
 '从自己设备这端，把文件送到服务器或共享系统那端；up 是系统关系，不是往天空发。',
 'up + load，现代计算机方向用语。动词常后重音，名词常前重音；不同说话者读法也可有变化。',H('up + load → upload','向服务器、远端系统传送 → 上传'),
 'upload a photo 上传照片，upload to a website 上传到网站，a failed upload 上传失败。',
 'upload a file；upload a photo；upload to；an upload limit。',
 'upload 与 download 看当前设备、系统关系；同一传送在不同两端可从相反视角描述。',
 ('Please upload the signed form to the portal.','请把签好的表格上传到门户。'),('The video upload failed halfway through.','视频上传到一半失败了。'))
W('download','动词英 /ˌdaʊnˈləʊd/、美 /ˌdaʊnˈloʊd/；名词常 /ˈdaʊnləʊd/ 等','下载；下载物、下载过程',
 '把服务器、网站等处的文件取到当前设备，和 upload 上传方向相对。',
 'down + load，现代数据传送词。down 表传送关系中的接收一端，不说明服务器真在高楼上。',H('down + load → download','从远端取得文件 → 下载'),
 'download a file 下载文件，a free download 免费下载物，download speed 下载速度。',
 'download a file；download from；download speed；a free download。',
 'download 保存取得文件，stream 流式播放通常侧重边传边用；具体软件可能缓存，不按字面定绝对技术边界。',
 ('You can download the guide as a PDF.','你可以把指南下载成 PDF。'),('The download stopped when the connection failed.','连接中断后，下载停止了。'))
W('reload','英 /ˌriːˈləʊd/；美 /ˌriːˈloʊd/','重新装载；重新加载',
 '原来装过、读过，现在再装一次、再读一遍；网页刷新是常见场景。',
 're- 重新 + load，既可实物装载，也可程序、网页再加载。其他装填语境同样按重新装入理解。',H('re- + load → reload','重新装入 → 重装、重新加载'),
 'reload the page 重新加载页面，reload the machine 重新装入机器所需材料。',
 'reload the page；reload the file；reload the machine。',
 'reload 重新加载，restart 重启；重新读一个页面不一定关闭再启动整个程序。',
 ('Try reloading the page if the image does not appear.','图片没出现的话，试试重新加载页面。'),('The operator reloaded the printer with paper.','操作员给打印机重新装上纸。'))
W('unload','英 /ʌnˈləʊd/；美 /ʌnˈloʊd/','卸下；卸货；倾诉负担',
 '原本由车、机器或自己承担，现在把东西卸出来；心里压力也能像货一样卸给别人。',
 'un- 解除、逆转 + load，形成装载的反向动作。现代也可用于数据、程序等释放加载状态。',H('un- + load → unload','解除装载 → 卸货、卸下负担'),
 'unload a truck 给卡车卸货，unload the boxes 卸下箱子，unload your worries 吐露烦恼。',
 'unload a truck；unload the goods；unload worries。',
 'unload 卸下，download 下载不是同义，后者是取得远端数据；unload a truck 卸车不是把车搬走。',
 ('They unloaded the boxes outside the warehouse.','他们在仓库外卸下箱子。'),('She needed someone to unload her worries on.','她需要一个能倾诉烦恼的人。'))
W('offload','英 /ˌɒfˈləʊd/；美 /ˌɔːfˈloʊd/','卸下；转移负担、任务；抛售',
 '把自己承担的东西挪出去，常强调交给别处、别人，或把不想继续持有的东西处理掉。',
 'off- 离开 + load 负载，先有卸货，再有转交工作、处理资产等扩展。',H('off- + load → offload','把负载移离 → 卸下、转移'),
 'offload cargo 卸货，offload work onto someone 把工作甩给别人，offload stock 卖出库存。',
 'offload cargo；offload work onto；offload unwanted stock。',
 'offload 与 unload 卸货时重合，转嫁任务时常带摆脱负担的语气；delegate 委派可更中性。',
 ('The crew offloaded the cargo at the port.','船员在港口卸下货物。'),('He tried to offload his paperwork onto a colleague.','他试着把文书工作甩给同事。'))
W('truckload','/ˈtrʌkləʊd/；美 /ˈtrʌkloʊd/','一卡车的量；大量',
 '把一辆卡车能载的东西当一批，口语也能夸很多，不必逐件数。',
 'truck 卡车 + load 载量。车辆大小不同，一 truckload 并不规定固定吨数。',H('truck + load → truckload','卡车一载的量 → 一卡车、大量'),
 'a truckload of sand 一卡车沙，truckloads of supplies 多车物资。',
 'a truckload of；truckloads of supplies；by the truckload。',
 'truckload 是载量称呼，不等于所有卡车容量相同；the truck 卡车本身与装的货也不同。',
 ('A truckload of gravel arrived before noon.','中午前到了一卡车碎石。'),('Volunteers collected truckloads of supplies.','志愿者募集了好几卡车物资。'))
W('caseload','英 /ˈkeɪsləʊd/；美 /ˈkeɪsloʊd/','经办案件、个案的数量；个案工作量',
 '律师、社工、医护等手上要处理多少个案，把它们合起来就是工作负荷。',
 'case 个案 + load 负担、数量，形成专业工作量名词。不是一个装案件文件的实体箱子。',H('case + load → caseload','所承担个案的量 → 个案工作量'),
 'a heavy caseload 繁重个案量，reduce a caseload 减少经办个案；数量与复杂度均会影响实际负荷。',
 'a heavy caseload；reduce the caseload；manage a caseload。',
 'caseload 个案数量、负荷，workload 工作总量范围更广；两个医生病例数相同也可能复杂度不同。',
 ('The social worker has a heavy caseload.','这位社工经办的个案很多，负担重。'),('The office hired more staff to reduce individual caseloads.','办公室增聘人员，减少每人的个案工作量。'))
W('boatload','英 /ˈbəʊtləʊd/；美 /ˈboʊtloʊd/','一船的量；大量',
 '字面一条船载的东西，口语一大堆则不必真运来一艘船。',
 'boat 船 + load 载量，从实际船运量形成大量的夸张表达。',H('boat + load → boatload','船的一载 → 大量'),
 'a boatload of passengers 一船乘客，a boatload of money 一大笔钱；口语、非正式常见。',
 'a boatload of；boatloads of money；a boatload of work。',
 'boatload 数量比喻不是精确标准单位；a boatload of work 不是工作坐船来。',
 ('The ferry brought a boatload of visitors to the island.','渡船带来了一船游客。'),('The repairs cost a boatload of money.','维修花了一大笔钱。'))
R('B3850','装载、数据传送与负担数量','LOAD：让某物承担内容，再看装入、移出与多少','load、loaded、loader 紧邻，再按上传下载、重装卸下分动作，truckload、caseload、boatload 分量的对象。',
 '历史接行程、运送词，负荷义后来发展；数字 load 借装入可用位置的画面。用户要求先略非常生僻、粗俗扩展，本页不列粗俗量词。',
 'load → loaded、loader；up/down/re-/un-/off- + load；truck/case/boat + load；已有 overload、workload、payload、preload、freeloader 共享。',
 [['基本动作、结果与主体','load · loaded · loader'],['数字传送与重复','upload · download · reload · preload'],['卸下、转移与过载','unload · offload · overload'],['不同负载内容与量','truckload · caseload · boatload · workload · payload · freeloader']],
 'upload 上传与 download 下载相对；unload 卸货不是 download；loaded question 带预设；caseload 个案量不等于全部工作。',
 'The loader unloaded a truckload of gravel.\n\n装载机卸下了一卡车碎石。',
 'load loaded loader upload download reload preload unload offload overload truckload caseload boatload workload payload freeloader')
if __name__=='__main__':save('continuation_20261029_ew',ROOTS,WORDS)
