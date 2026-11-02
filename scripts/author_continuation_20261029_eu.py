"""Code: collected rules, encoded information and a biological unit."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['拉丁 caudex、codex 木板书、书册 → 古法语 code','成册法规、法典'],['英语 code','成套规则 → 符号编码体系；计算机指令']]
def H(f,m):return C+[[f,m]]
W('code','英 /kəʊd/；美 /koʊd/','代码；编码；准则、法规；编程、编码',
 '一条路是把规则收成一套，另一条是用约定的符号表达信息；计算机代码也是按规则写给机器执行的指令。',
 '经法语来自拉丁 codex，早期木板书、书册，后有法典义。规则系统与符号体系逐渐扩展，不能把现代程序语言说成古罗马人在写软件。',C,
 'a code of conduct 行为准则，a secret code 秘密编码，source code 源代码；code a program 编写程序。',
 'a code of conduct；source code；a secret code；write code。',
 'code 不一定秘密，公开邮编也是 code；code 规则、编码体系不等于每次都是 password 密码。',
 ('The club has a strict code of conduct.','俱乐部有严格行为准则。'),('She writes code for a weather application.','她为一款天气应用编写代码。'),sources=['https://www.etymonline.com/word/code','https://en.wiktionary.org/wiki/code#English'])
W('coding','英 /ˈkəʊdɪŋ/；美 /ˈkoʊdɪŋ/','编程；编码、按类别标记',
 '把信息写进代码、符号或分类体系；不只计算机里敲程序这一种。',
 'code 去 e + -ing，形成动作名词与动词形式。研究里 coding responses 可指给回答分类标记。',H('code + -ing → coding','编码动作 → 编程、分类编码'),
 'learn coding 学编程，colour coding 颜色编码，coding interview responses 给访谈回答编码分类。',
 'learn coding；colour coding；coding skills。',
 'coding 可能编程，也可能研究分类；一个采访研究的 coder 不一定在写应用软件。',
 ('The school offers an introduction to coding.','学校开设编程入门课。'),('The researchers used colour coding to organize the files.','研究人员用颜色编码整理文件。'))
W('coder','英 /ˈkəʊdə/；美 /ˈkoʊdər/','程序员；编码人员、器具',
 '执行写代码或编码分类的主体；具体角色取决于代码是哪种。',
 'code 去末尾 e，加完整表人或器物后缀 -er，得 coder。-er 可指人，也可指编码器物。',H('code + -er → coder','执行编码的主体'),
 'a skilled coder 熟练程序员，a medical coder 医疗记录编码员；后者处理分类代码，不因此变医生。',
 'a skilled coder；a software coder；an independent coder。',
 'coder 角色比软件工程全部职责更具体，但日常两类职称有重合；medical coder 不等于提供治疗的人。',
 ('The team hired another coder to work on the app.','团队又雇了一名程序员开发应用。'),('Two coders classified the interview responses independently.','两名编码人员独立给访谈回答分类。'))
W('encode','英 /ɪnˈkəʊd/；美 /ɪnˈkoʊd/','编码；把信息转成特定形式',
 '按一套规则把原信息换一种表示法，方便储存、传送或处理。',
 'en- 使进入 + code，把信息放入编码形式。现代技术、信息表达领域都常见。',H('en- + code → encode','置入编码形式 → 编码'),
 'encode text as UTF-8 把文本按 UTF-8 编码，encode a video 编码视频。',
 'encode data；encode text；encode a video。',
 'encode 编码不等于 encrypt 加密；编码规则可以完全公开，不必有秘密密钥。',
 ('The system encodes the text as UTF-8.','系统把文本编码为 UTF-8。'),('The message encodes information in a series of symbols.','消息用一串符号编码信息。'))
W('decode','英 /ˌdiːˈkəʊd/，亦 /dɪˈkəʊd/；美 /diːˈkoʊd/','解码；理解隐藏、复杂的含义',
 '按编码规则把符号读回信息；也可比喻弄懂别人含糊难懂的话。',
 'de- 解除、反向 + code，形成与编码方向相反的动词。不是 delete 删除数据的缩写。',H('de- + code → decode','把编码读回信息 → 解码、理解'),
 'decode a signal 解码信号，decode a message 解读消息，decode someone’s remarks 弄懂话意。',
 'decode a signal；decode a message；decode the meaning。',
 'decode 读回编码，与 decrypt 解密相关但不完全同义；没有加密的文件也需正确解码。',
 ('The software decoded the signal successfully.','软件成功解码了信号。'),('I tried to decode the meaning behind his vague reply.','我试着弄懂他含糊答复背后的意思。'))
W('recode','英 /ˌriːˈkəʊd/；美 /ˌriːˈkoʊd/','重新编码；改变分类代码',
 '已有编码、分类或程序，再按新的规则做一次；不一定从零重写整套软件。',
 're- 重新 + code，可用在数据编码、研究分类和程序修改。具体改变范围由对象决定。',H('re- + code → recode','重新编码、分类'),
 'recode a variable 重新编码变量，recode the data 重新编码数据。',
 'recode a variable；recode the data；recode a category。',
 'recode 改编码、分类，decode 解码；把类别1改为类别0是 recode，不一定是把秘密信息读出来。',
 ('The researchers recoded the responses into three categories.','研究人员把回答重新编码为三类。'),('We had to recode the variable before the analysis.','分析前，我们得重新编码这个变量。'))
W('codebase','英 /ˈkəʊdbeɪs/；美 /ˈkoʊdbeɪs/','代码库；一套项目代码',
 '不是某一行程序，而是支持某个项目、系统的那一整套代码。',
 'code + base 基础、集合体。现代软件名词，不一定与一个 Git 仓库边界完全一致。',H('code + base → codebase','项目的代码基础集合 → 代码库'),
 'a large codebase 大型代码库，maintain a codebase 维护代码库，a shared codebase 共享代码基础。',
 'a large codebase；maintain a codebase；a shared codebase。',
 'codebase 一套代码，database 数据库主要存数据；repository 仓库是管理容器，边界不必与 codebase 完全相同。',
 ('The team is gradually cleaning up the old codebase.','团队正逐步整理旧代码库。'),('Both applications use the same codebase.','两个应用使用同一套代码基础。'))
W('codify','英 /ˈkəʊdɪfaɪ/；美 /ˈkɑːdɪfaɪ/','编纂成法规、规则；把做法系统化',
 '原本散着的规定、惯例整理成一套明确条文，让人能查、能统一照做。',
 'code 的规则集义 + -ify 使成，词干表现 cod-，不是 cod 鳕鱼 + 一个无关尾巴。',H('code + -ify → codify','形成成套规则 → 编纂、系统化'),
 'codify the rules 编纂规则，codify existing practices 把现有做法明确成文；不一定是编电脑程序。',
 'codify the rules；codify a practice；codify standards。',
 'codify 系统整理为规则，code 写程序或编码；把公司惯例写成手册通常 codify，不必说写软件。',
 ('The policy codifies practices already used by the team.','政策把团队已有做法明确成文。'),('The committee worked to codify the rules.','委员会着手把规则系统编纂成文。'))
W('codon','英 /ˈkəʊdɒn/；美 /ˈkoʊdɑːn/','密码子',
 '遗传信息中三个核苷酸组成的一组，像按三个字符分组读取的代码单位；对应氨基酸或终止信号。',
 '生物学现代词由 code + -on 构成单位名，不是 con- 加 don。另有从希腊钟形词来的冷门同形义，与遗传密码子分开。',H('code + -on → codon','遗传编码单位 → 密码子'),
 'a stop codon 终止密码子，an RNA codon RNA 密码子；本页记词与概念，不从单个密码子预测个人健康。',
 'a stop codon；a start codon；an RNA codon。',
 'codon 一组三个核苷酸，不等于一个 gene 基因；多个密码子可以编码同一种氨基酸，也存在终止信号。',
 ('The diagram groups the RNA sequence into codons.','图把 RNA 序列分成一组组密码子。'),('A stop codon signals the end of protein synthesis.','终止密码子发出蛋白质合成结束的信号。'),sources=['https://www.genome.gov/genetics-glossary/Codon','https://en.wiktionary.org/wiki/codon#English'])
R('B3409','规则、符号编码与计算机代码','CODE：按规则表达信息，也可收集成规则体系','先看 code、coding、coder，再配对 encode 与 decode；recode、codebase 继续扩展，codify 走成文规则，codon 走遗传编码。',
 'code 经法语接拉丁书册、法典词，符号系统与计算机指令是后来扩展。生物 codon 为现代 code+-on，冷门希腊钟形同形词不混讲。',
 'code → coding、coder；en-、de-、re- → encode、decode、recode；code + base → codebase；-ify → codify；-on → codon。',
 [['基本词、活动与主体','code · coding · coder'],['编码、解码与重编码','encode · decode · recode'],['代码集合与成文规则','codebase · codify'],['遗传与已有代码复合','codon · codeword · codename · postcode · passcode']],
 'encode 不等于 encrypt；codify 不必写软件；codebase 不是 database；codon 是三核苷酸单位，不是整个基因。',
 'The coder decoded the data before adding it to the codebase.\n\n程序员先解码数据，再把它加入代码库。',
 'code coding coder encode decode recode codebase codify codon codeword codename postcode passcode')
if __name__=='__main__':save('continuation_20261029_eu',ROOTS,WORDS)
