"""Path and frame: routes, guides, enclosing/supporting structure and perspective."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
P=[['古英语 pæþ → 中古英语 path、peth → path','路、足迹踩出的通道；更远来源有争议'],['英语 path','小路、行进轨迹；行动途径、文件位置等']]
def PH(f,m):return P+[[f,m]]
W('path','英 /pɑːθ/；美 /pæθ/','小路、路径；轨迹；做事途径；文件路径',
 '从这里到那里，脚或物体走过一条线；做事怎样一步步到目标，也可借这条路来理解。',
 '接古英语 pæþ，经中古英语延续。更远是否从伊朗语等借入仍有争议，不能把重建的通过词根说成已确证。现代数字文件路径借定位路线来命名。',P,
 'a narrow path 小路，the path of a storm 风暴路径，a path to success 通向成功的途径，a file path 文件位置路径。',
 'follow a path；a path through；a path to；a file path。',
 'path 常步行小路、路线，road 常道路，way 更广也可方法；path 不一定铺了供汽车行驶的路面。',
 ('A narrow path led through the woods.','一条小路穿过树林。'),('The guide explained a possible path to solving the problem.','指南说明了解决问题的一种可行途径。'))
W('pathfinder','英 /ˈpɑːθfaɪndə/；美 /ˈpæθfaɪndər/','探路者、开拓者',
 '别人还不知道该怎么走，他先找出一条能过的路；也能比喻开辟新方法的人。',
 'path 路 + finder〔find + -er〕，构成人物名。军事或探险等领域可能有专门角色，但基本画面仍是先找路。',PH('path + finder → pathfinder','找到通路的人；方法开拓者'),
 'a skilled pathfinder 熟练探路者，a scientific pathfinder 科学开拓者，act as a pathfinder 充当探路者。',
 'a skilled pathfinder；a scientific pathfinder；act as a pathfinder。',
 'pathfinder 开辟、找到路者，follower 跟随者；大写 Pathfinder 还可专名，不能凭词就推定具体产品。',
 ('The pathfinder checked the route before the group moved on.','探路者先检查路线，队伍才继续前进。'),('The researcher became a pathfinder in the new field.','那位研究者成了新领域的开拓者。'))
W('towpath','英 /ˈtəʊpɑːθ/；美 /ˈtoʊpæθ/','纤道、运河岸牵船路',
 '过去人或马在岸上沿路走，用绳子牵着船前进；这条岸路就是 towpath。今天有些成了散步、骑行道。',
 'tow 拖、牵引 + path 小路，按牵船用途命名。不是 toe 脚趾 + path。',PH('tow + path → towpath','沿水道岸边供牵船用的路'),
 'a canal towpath 运河纤道，walk along the towpath 沿纤道走，a restored towpath 修复的纤道。',
 'a canal towpath；along the towpath；a restored towpath。',
 'towpath 特定历史用途岸路，footpath 步行小路更泛；不靠它今天是否还有马来决定名称。',
 ('We walked along the canal towpath.','我们沿运河纤道散步。'),('The old towpath is now popular with cyclists.','旧纤道现在很受骑行者欢迎。'))
R('B2783','通路、轨迹；方法与探路、牵船用途','PATH：从此处到彼处的一条路线','path → pathway、footpath；pathfinder 人物、towpath 岸路；warpath 已有比喻精讲复用。',
 '近源古英语明确，更远借入说有争议。小路、风暴路线和做事途径按路线画面联系，不见 path 就当供人走的铺装路。',
 'path + way/finder；foot/tow/war + path；finder 为 find + -er。',
 [['路线与步行通道','path · pathway · footpath'],['开路人物和用途','pathfinder · towpath · warpath']],
 'path/road/way 范围不同；towpath 历史牵船用途；pathfinder 人物，file path 可数字位置。',
 'The pathfinder followed the towpath beside the canal.\n\n探路者沿运河旁的纤道前进。','path pathway footpath pathfinder towpath warpath')
F=[['古英语 framian、fremman 等 → 中古英语 framen、frame','促进、做成 → 准备、构造；旧名词来源还有相关形式交汇'],['英语 frame','支撑骨架、外框；安排表达方式；构陷等']]
def FH(f,m):return F+[[f,m]]
W('frame','/freɪm/','框、骨架；画面帧；组织、表述；装框；构陷',
 '给画围个框，让它按某个边界呈现；给问题选一套说法，也像把它放进特定框架。',
 '动词接古英语促进、做成等相关形，中古英语有准备、构造义；名词结构、外框与这些动词及相关借词形交汇，更早细节有不同分析。构陷义与安排、编造情节的旧用法相关，不是把人真的镶进相框。',F,
 'a picture frame 相框，a bicycle frame 自行车车架，frame a question 组织问题的表述，frame someone for a crime 栽赃某人，a video frame 视频一帧。',
 'a picture frame；frame a question；frame someone for；a video frame。',
 'frame 外框、支撑结构，framework 框架系统更重整体组织；a frame of mind 心态，不是脑中有实物相框。',
 ('She put the photograph in a wooden frame.','她把照片放进木相框。'),('The way we frame the question can change the discussion.','我们怎样表述问题，会改变讨论方向。'),
 sources=['https://en.wiktionary.org/wiki/frame#English','https://www.etymonline.com/word/frame'])
W('framer','英 /ˈfreɪmə/；美 /ˈfreɪmər/','装框者；构建、制定者',
 '可以是为画做框的人，也可以是为规则、协议搭出整体结构的人。',
 'frame + -er，形成执行装框、构建、拟定的人物名。词尾 e 与后缀衔接。',FH('frame + -er → framer','装框、构建或制定的人'),
 'a picture framer 画框制作、装裱者，the framers of a constitution 宪法制定者，the framers of an agreement 协议制定者。',
 'a picture framer；the framers of；a skilled framer。',
 'framer 人物，frame 框、结构或动作；立法、制度背景的 framer 不是职业装裱师的字面意思。',
 ('The picture framer measured the print carefully.','装裱师仔细量了画作尺寸。'),('The framers of the agreement tried to avoid ambiguous wording.','协议制定者尽量避免含糊措辞。'))
W('frameless','/ˈfreɪmləs/','无框的',
 '没有平时看得见的外框，画、玻璃门、眼镜等看起来更像边缘直接露出来。',
 'frame + -less，保留词尾 e，写 frameless。否定外框不保证完全没有其他支撑、固定部件。',FH('frame + -less → frameless','没有通常外框的'),
 'frameless glasses 无框眼镜，a frameless mirror 无框镜子，a frameless glass door 无框玻璃门。',
 'frameless glasses；a frameless mirror；a frameless glass door。',
 'frameless 无框、borderless 无边界或边框，具体领域可重叠；无框眼镜仍可有鼻梁和镜腿支撑。',
 ('She chose a frameless mirror for the hallway.','她给走廊选了一面无框镜。'),('The shop has a frameless glass door.','店里装着一扇无框玻璃门。'))
W('reframe','/ˌriːˈfreɪm/','重新装框；换一种框架、角度表述',
 '换相框是字面；同一件事换个提问、评价角度，则是重新框定问题。事实未必变，呈现方式变了。',
 're- 重新 + frame，既可重新装框，也可重新组织、解释。不是把事情换个好听说法就证明问题已经解决。',FH('re- + frame → reframe','重新装框；重新组织理解、表达的框架'),
 'reframe a picture 给画换框，reframe the question 换个角度提问，reframe a problem 重新界定问题。',
 'reframe the question；reframe the problem；reframe a picture。',
 'reframe 改组织视角，rewrite 改文字内容，二者可能同时发生但不必相同；换框架不自动改变事实。',
 ('The museum reframed the painting before the exhibition.','展览前，博物馆给画换了框。'),('She reframed the discussion around what users actually needed.','她把讨论重新围绕用户真正需要什么来展开。'))
R('B3837','外框、支撑结构；按框架构造和表述','FRAME：把东西组织在一套边界、骨架之中','frame → framer、frameless、reframe；framework、mainframe、airframe、doorframe 按组织系统、计算机、机体、门框复习。',
 '词源较早做成、促进的动词与结构名词有交汇，近义变化不编成唯一故事。表述与构陷义看实际对象；reframe 不等于改变事实。',
 'frame + -er/-less；re- + frame；frame + work；main/air/door + frame。',
 [['基本框与人物、性质、再框定','frame · framer · frameless · reframe'],['结构系统与各类骨架','framework · mainframe · airframe · doorframe']],
 'framer 人物；frameless 无外框非完全无支撑；reframe 与 rewrite 不完全相同；frame someone 构陷不按装相框直译。',
 'The framer suggested a simpler frame for the picture.\n\n装裱师建议给画配一个更简洁的框。','frame framer frameless reframe framework mainframe airframe doorframe')
if __name__=='__main__':save('continuation_20261030_cy',ROOTS,WORDS)
