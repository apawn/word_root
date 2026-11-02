"""Medicine/medical and access: common vocabulary before specialist extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
ME=[['拉丁 medērī、medicus','治疗；医生、医治相关的'],['拉丁 medicīna → 古法语 medecine → 英语 medicine','医术、治疗手段 → 医学、药物']]
W('medicine','/ˈmedɪsɪn/；也常读 /ˈmedsɪn/','药、药物；医学',
 '杯子里要喝的是药，大学里要学的是医学；一个词把治病所用之物和这门学问连起来。',
 '经法语接拉丁 medicīna 医术、治疗手段，与 medicus 医生相关。medicine 不是现代 medic + 一个随意表示药水的 -ine。',ME,
 'take medicine 服药，study medicine 学医学，a medicine for coughs 具体一种药。泛指药常不可数，多种药可说 medicines。',
 'take medicine；study medicine；modern medicine；a medicine cabinet。',
 'medicine 可药物也可学科；medical 是相关形容词。take your medicine 还可比喻接受应承担的后果，需看上下文。',
 ('She hopes to study medicine at university.','她希望在大学学医。'),('The medicine comes with written instructions.','这种药附有书面说明。'))
W('medic','/ˈmedɪk/','医护人员；急救人员；医生〔口语〕',
 '在现场提供医疗救助的人，报道里常见于急救、军队等场景；具体资格看语境。',
 '接拉丁 medicus 医生、医治的相关形式。现代常作人物名词；不是 medicine 的末尾随便切掉几个字母后得到唯一职业名称。',ME[:1]+[['拉丁 medicus → 英语 medic','医生或提供医疗救助的人']],
 'an army medic 军队医护人员，a team of medics 一组医护人员，medics at the scene 现场急救人员。',
 'an army medic；a team of medics；medics at the scene。',
 'medic 是较宽称呼，doctor、paramedic、nurse 的角色不完全相同；不能只凭 medic 推断具体执照或专业。',
 ('Medics arrived at the scene within minutes.','医护人员几分钟内就赶到现场。'),('He served as an army medic.','他曾担任军队医护人员。'))
W('medicinal','/məˈdɪsɪnəl/','药用的；具有治疗用途的',
 '重点在某种东西被当作药来用，或具有药用性质，而不是泛指整个医疗行业。',
 '接拉丁 medicīnālis，与 medicīna 同族；表面可对应 medicine + -al，但历史不是从现代英语临时造出。重音在第二音节。',ME[:1]+[['拉丁 medicīna → medicīnālis → 英语 medicinal','治疗手段、药物 → 药用性质的']],
 'medicinal plants 药用植物，medicinal use 药用，medicinal properties 药用性质；这些是用途描述词。',
 'medicinal plants；medicinal use；medicinal properties。',
 'medical equipment 医疗设备通常不说 medicinal equipment；medicinal 强调药用或治疗性质，medical 泛指医疗医学相关。',
 ('The garden has a section devoted to medicinal plants.','花园有一个专门种药用植物的区域。'),('The book traces the historical medicinal use of the plant.','书中追溯了这种植物历史上的药用情况。'))
W('medical','/ˈmedɪkl/','医疗的；医学的；体检〔名词用法〕',
 '只要与看病、医学、健康检查这套专业活动有关，常用 medical 来修饰。',
 '借法语 médical，上接晚期或中世纪拉丁 medicālis，再接 medicus 医生。与 medicine 同族，但不是 medicine 简单换词尾。',ME[:1]+[['拉丁 medicālis → 法语 médical → medical','医生、医治相关 → 医疗、医学相关']],
 'medical care 医疗照护，medical school 医学院，medical records 医疗记录；have a medical 英式可说做体检。',
 'medical care；medical school；medical records；a medical examination。',
 'medical 医疗相关，medicinal 药用；a medical student 是医学生，medicine student 不是通常的标准搭配。',
 ('She is training at a medical school.','她在医学院接受培养。'),('Please bring your medical records to the appointment.','请带上医疗记录来赴约。'),sources=['https://www.etymonline.com/word/medical','https://en.wiktionary.org/wiki/medical#English'])
W('medically','/ˈmedɪkli/；也可展开读 /ˈmedɪkəli/','从医学上；因医疗原因；用医疗方式',
 '限定判断角度：从医学来说如何，或者这件事是出于医疗方面的需要。',
 'medical + -ly，形容词转副词；弱读时中间音节可压缩，-cally 这一段不是每个字母都单独读。',ME[:1]+[['medical + -ly → medically','按医学判断、在医疗上']],
 'medically trained 受过医疗训练的，medically necessary 医疗上必要的，medically qualified 具医疗专业资格的。',
 'medically trained；medically necessary；medically qualified。',
 'medically 限定医疗层面，legally、financially 等会改成别的判断角度；不要把一个角度的结论当所有角度都成立。',
 ('A medically trained volunteer was present.','现场有一位受过医疗训练的志愿者。'),('The form asks whether the absence was medically necessary.','表格询问缺席是否出于医疗上的必要。'))
W('telemedicine','英 /ˌtelɪˈmedɪsɪn/；美 /ˌteləˈmedɪsɪn/','远程医疗',
 '医护与患者不在同一地点，通过电话、视频或其他通信方式交换医疗信息、提供服务。',
 'tele- 远距离 + medicine 医疗，现代科技复合词。tele- 来自希腊表示远的构词材料，不仅指电视。',ME+[['tele- + medicine → telemedicine','借远距离通信进行的医疗服务或信息交换']],
 'a telemedicine appointment 远程医疗预约，telemedicine services 远程医疗服务。具体包含咨询、监测等哪类服务需看场景。',
 'telemedicine services；a telemedicine appointment；access to telemedicine。',
 'telemedicine 是医疗活动的远程形式；普通搜索健康网页不自动等于正在接受一项远程医疗服务。',
 ('The clinic offers telemedicine appointments.','诊所提供远程医疗预约。'),('Telemedicine allowed the doctor and patient to speak from different towns.','远程医疗让医生与患者可以身处不同城镇交谈。'))
R('B2462','药物、医学与远程、生物医学','MEDICINE：药物与医术；相关形容词分药用、医疗','medicine 先抓药物和学科，medic 讲人；medicinal、medical 分清，再接远程医疗等共享词。',
 '经法语接拉丁医治词族，medicine、medicinal、medical 各有不同借入形式，不能画成一个现代词随便换尾巴。',
 'medicus → medicīna → medicine；medicīnālis → medicinal；medicālis → medical → medically；tele-/bio- + medicine。',
 [['药物、医护与性质','medicine · medic · medicinal · medical · medically'],['远程与交叉领域','telemedicine · biomedicine · biomedical']],
 'medicine 药或学科，medic 人，medicinal 药用，medical 医学相关；telemedicine 的 tele- 表距离。',
 'The medical school offers a course on telemedicine.\n\n医学院开设远程医疗课程。',
 'medicine medic medicinal medical medically telemedicine biomedicine biomedical')
R('B3908','医疗相关与医学判断角度','MEDICAL：与医治有关；MEDICALLY：从医疗角度','把 medicine、medic、medicinal 同族相邻复习；medical → medically，再接 biomedical。',
 'medical 经法语接拉丁医生相关形容词，并非现代 medicine 的任意变形。副词 medically 是 medical + -ly。',
 '拉丁 medicus 同族 → medicine／medic／medicinal／medical；medical + -ly；bio- + medical。',
 [['同族基础与形容词','medicine · medic · medicinal · medical'],['副词与交叉领域','medically · biomedical']],
 'medical 与 medicinal 侧重不同；medically 只限定医疗角度；medic 不保证具体职业资格。',
 'The medically trained guide explained the history of medicinal plants.\n\n受过医疗训练的向导讲解了药用植物的历史。',
 'medicine medic medicinal medical medically biomedical')
AC=[['拉丁 ad- + cēdere → accēdere；accessus','朝向 + 走 → 接近；接近、入口'],['晚期拉丁 accessibilis → 法语 accessible → 英语 accessible','能够接近、进入 → 易用、易理解']]
W('accessible','/əkˈsesəbl/','可到达、可使用的；无障碍的；易理解的',
 '路能走到，设施用得上，文章读得懂：共同点是原本隔着的障碍少了。',
 '经法语及晚期拉丁 accessibilis，接 accessus 接近、入口；现代可对应 access + -ible。形容词有自己的借入历史。',AC,
 'accessible by bus 公交可达，accessible to everyone 人人可用，an accessible explanation 通俗解释；无障碍设施强调相关使用者确实能用。',
 'accessible to；accessible by bus；an accessible explanation；an accessible entrance。',
 'available 有供应、可获得，accessible 能接近、能使用；有一份文件不一定所有人都能打开或读懂。',
 ('The museum is accessible by public transport.','博物馆乘公共交通可以到达。'),('She gives an accessible explanation of a difficult idea.','她把一个难懂的想法解释得通俗易懂。'),sources=['https://www.etymonline.com/word/accessible','https://en.wiktionary.org/wiki/accessible#English'])
W('inaccessible','/ˌɪnəkˈsesəbl/','难以到达的；无法使用的；难懂的',
 '入口被隔断、资料打不开，或文章太晦涩，让人进不去。',
 '经法语接晚期拉丁 inaccessibilis；现代可分析 in- 不 + accessible，in- 在这里否定，不是表示里面。',AC+[['拉丁 in- + accessibilis → 法语、英语 inaccessible','不能接近、使用或理解']],
 'an inaccessible island 难抵达的岛，inaccessible data 无法访问的数据，inaccessible writing 晦涩文字。',
 'inaccessible to；inaccessible data；an inaccessible location。',
 'inaccessible 不一定不存在；文件可能完好，但你没有权限或连接不上。inaccessible 与 unacceptable 不可接受也要分。',
 ('The village became inaccessible after the bridge collapsed.','桥塌后村庄变得无法到达。'),('The report was inaccessible to readers without a subscription.','未订阅的读者无法访问报告。'))
W('accessibility','/əkˌsesəˈbɪləti/','可达性；易用、易理解程度；无障碍性',
 '把能不能到、用起来有没有障碍作为一个整体问题：入口、文字、操作都可能影响它。',
 'accessible + -ity，-ible 对应 -ibility，形成性质名词；受到法语、晚期拉丁相应名词形式影响。重音移到 -bil-。',AC+[['accessible + -ity → accessibility','可接近、可使用、可理解的程度及设计性质']],
 'website accessibility 网站无障碍，improve accessibility 提高可达性和易用性，accessibility features 无障碍功能；具体对象决定评估内容。',
 'improve accessibility；website accessibility；accessibility features。',
 'access 是进入或使用的机会、动作，accessibility 说这种进入、使用有多可行；无障碍性不只是否装了坡道。',
 ('The redesign improved the website’s accessibility.','改版提高了网站的无障碍性。'),('The survey asks residents about the accessibility of local services.','问卷询问居民使用当地服务是否方便、有无障碍。'))
R('B2528','进入、使用与减少理解障碍','ACCESS：能进去；ACCESSIBLE：能接近、用得上','access 已精讲，紧接 accessible → inaccessible、accessibility。',
 '拉丁接近词形成名词与关系形容词，经法语进入英语；现代扩展到设施、信息、文字理解。',
 'access → 相关借入形容词 accessible；in- + accessible；accessible + -ity → accessibility。',
 [['基本进入与可用性质','access · accessible'],['否定与性质名词','inaccessible · accessibility']],
 'available 有供应不保证 accessible 能用；inaccessible 不等于不存在；accessibility 不只坡道。',
 'Better accessibility makes the service accessible to more people.\n\n改善无障碍性让更多人能使用这项服务。',
 'access accessible inaccessible accessibility')
if __name__=='__main__':save('continuation_20261030_x',ROOTS,WORDS)
