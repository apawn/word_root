"""Selected ide names, hugs and silicon."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
I=[['法国化学命名 oxide 等的词尾','经德语 -id 等形式扩展为 -ide'],['英语化学 -ide','许多二元化合物及阴离子名；后来也用于其他化学类别']]
W('fluoride','英 /ˈflʊəraɪd/、/ˈflɔːraɪd/；美 /ˈflʊraɪd/','氟化物；氟离子 F⁻',
 'fluorine 是元素氟的名称，改成 fluoride 时，常在说氟形成的阴离子或相应氟化物。像把元素名换成它在化合物中的角色名。',
 'fluor- 取自 fluorine + -ide；离子语境中 F⁻ 是带一个负电荷的氟离子，化合物语境则看整个名称。',I+[['fluor- + -ide → fluoride','氟化物、氟离子']],
 'sodium fluoride 氟化钠，fluoride ions 氟离子，a fluoride compound 氟化物；学习名称，不由词尾推断具体产品用法。',
 'sodium fluoride；fluoride ions。',
 'fluorine 元素氟与 fluoride 氟化物、离子分清；相似开头不等于相同物质。',
 ('The label lists sodium fluoride as an ingredient.','标签把氟化钠列为一种成分。'),('Fluoride ions carry a negative charge.','氟离子带负电荷。'),sources=['https://en.wiktionary.org/wiki/fluoride#English','https://www.affixes.org/-ide.html'])
W('sulfide','/ˈsʌlfaɪd/','硫化物；硫离子相关名称',
 'sulfur 是硫，sulfide 让你看硫与别的成分形成的那类化合物。金属硫化物是最容易入门的一组例子。',
 'sulf- 取自 sulfur + -ide；也见英式 sulphide 拼写。无机硫化物常联系 S²⁻，有机 sulfide 还可指 R—S—R′ 结构，不能只靠词尾认全部细节。',I+[['sulf- + -ide → sulfide','硫化物；有机、无机语境各有结构']],
 'iron sulfide 硫化铁，metal sulfides 金属硫化物；讨论具体化合物时完整名称、化学式才决定组成。',
 'iron sulfide；metal sulfides。',
 'sulfide、sulfite 亚硫酸盐、sulfate 硫酸盐是不同名称；英语词尾的一点变化可能对应结构差别。',
 ('The rock contains several metal sulfides.','这块岩石含有几种金属硫化物。'),('The label identified the sample as iron sulfide.','标签把样品标为硫化铁。'),sources=['https://en.wiktionary.org/wiki/sulfide#English','https://www.affixes.org/-ide.html'])
W('iodide','/ˈaɪədaɪd/','碘化物；碘离子 I⁻',
 'iodine 是碘，iodide 是碘形成的阴离子或相关碘化物。看到 potassium iodide，就先认钾与碘化物这一命名组合。',
 'iod- 取自 iodine + -ide；I⁻ 表一个碘原子获得额外电子后形成的阴离子。盐类、其他化合物还要看完整名称。',I+[['iod- + -ide → iodide','碘化物、碘离子']],
 'potassium iodide 碘化钾，iodide ions 碘离子，detect iodide 检测碘离子。',
 'potassium iodide；iodide ions。',
 'iodide 与 iodine 不是可无条件替换的名称；iodate 碘酸盐又是不同结构类别。',
 ('Potassium iodide contains iodide ions.','碘化钾含有碘离子。'),('The analysis detected iodide in the sample.','分析检测出样品中的碘离子。'),sources=['https://en.wiktionary.org/wiki/iodide#English','https://www.affixes.org/-ide.html'])
A=[['ammonia 氨一族 + -ide 命名形式','形成 amide 名称'],['有机化学常用 amide','羰基碳直接连氮的羧酰胺结构；更广定义另含其他酰胺'],['无机语境的另一类 amide','氨、胺的金属衍生物也采用这个类名']]
W('amide','英 /ˈæmaɪd/；美 /ˈæmaɪd/、/ˈæmɪd/','酰胺；〔另一化学用法〕氨、胺的金属衍生物',
 '在常见有机结构里，先找到 C=O，再看这个碳直接连着氮：这是认羧酰胺的关键。它像一段能把有机部分接起来的结构，肽键也属这一类。',
 '名称由 ammonia 氨一族与 -ide 构成。现代 amide 是化学类别名，常用羧酰胺只是其中重要分支；氨、胺的金属衍生物另有同名用法。',A,
 'an amide group 酰胺基，an amide bond 酰胺键，polyamide 聚酰胺；基础阅读先抓 C(=O)—N 结构，更广定义随化学语境。',
 'an amide group；an amide bond。',
 'amide 酰胺与 amine 胺分清，常见有机酰胺的氮直接接羰基碳；不能把所有带氮有机物都叫 amide。',
 ('The diagram marks the amide bond between the two parts.','图中标出了两部分之间的酰胺键。'),('This polymer contains repeating amide links.','这种聚合物含有反复出现的酰胺连接。'),sources=['https://en.wiktionary.org/wiki/amide#English','https://goldbook.iupac.org/terms/view/A00266'])
R('A1879','化学命名后缀，常见于阴离子、二元化合物及其他类别','-IDE：把元素或基团放进化合物名称，整词和化学式一起看','fluoride、chloride、bromide、iodide；sulfide；amide、peptide 等再看专门结构。',
 '不是背一个化合物的中文就够，而是学会元素名怎样换成相应角色名。后缀用途后来扩展，不能一律解释成同一种电荷、同一种二元结构。',
 '-ide 经法语 oxide 等命名及德语 -id 影响；fluor-、chlor-、brom-、iod- 等取元素词干，其他类别有各自命名历史。',
 [['卤素相关名称','fluoride · chloride · bromide · iodide · halide'],['其他无机及基团名称','sulfide · cyanide'],['有机结构与生物化学类别','amide · peptide · nucleotide']],
 '-ide 不保证所有词都只有两种元素；化学式与具体类别一起看。',
 'The table distinguishes fluoride, iodide and several other compounds ending in -ide.\n\n表中区分了氟化物、碘化物和其他几种以 -ide 结尾的化合物。','fluoride chloride bromide iodide halide sulfide cyanide amide peptide nucleotide')
H=[['早期英语 hugge → hug','双臂搂住、紧贴'],['更早来源有不同分析','可能联系北欧安慰词或蜷缩、聚拢旧词，未完全确定'],['hug + -er → hugger','拥抱者、喜欢拥抱的人']]
W('hug','/hʌɡ/','拥抱；紧抱；贴着、沿着',
 '双臂把人搂近是 hug；车道紧贴海岸线，也像把海岸抱在旁边。共同画面是靠得近、贴得紧。',
 '由早期 hugge 延续，更早来源不完全确定，常有北欧安慰词、蜷缩聚拢词等分析。现代由搂住扩展到紧贴路线、边缘。',H[:2],
 'give someone a hug 抱一抱某人，hug someone tightly 紧抱某人，hug the coast 沿海岸近处走，hug one’s knees 抱膝。',
 'give someone a hug；hug the coast。',
 'hug 常有贴紧的身体画面；沿路 hug the wall 不是墙真的被人双臂圈住，而是走得很靠近。',
 ('She gave her brother a warm hug.','她热情地抱了抱哥哥。'),('The road hugs the coast for several miles.','道路沿海岸近处延伸了好几英里。'))
W('hugger','英 /ˈhʌɡə/；美 /ˈhʌɡər/','拥抱者；喜欢拥抱的人',
 '有人见到亲友就喜欢抱一下，会说 I’m a hugger。-er 把拥抱动作变成这个人的行为特点。',
 'hug + -er，双写 g，形成人物名词；也能指某一次执行拥抱的人。',H[:2]+[['hug + -er → hugger','做拥抱动作、习惯拥抱的人']],
 'a big hugger 很喜欢拥抱的人，not much of a hugger 不太习惯拥抱的人；口语介绍亲近方式时常见。',
 'a big hugger；not much of a hugger。',
 'hugger 不是职业名，-er 也可以表示习惯做某事的人。',
 ('I’m a hugger, and so is my sister.','我喜欢拥抱，我妹妹也一样。'),('He is not much of a hugger, but he gave her a warm welcome.','他不太习惯拥抱，不过还是热情地欢迎了她。'))
R('B4223','双臂搂近，到路线贴近与人物习惯','HUG：靠得近、贴得紧','hug → hugger；拥抱实体与沿线紧贴的比喻一起看。',
 '把身体搂近很好记，路线紧贴某处也能借这个词。人物后缀 -er 则让拥抱变成某人的行为习惯。',
 'hugge → hug，早期来源有不同分析；-er 人物，双写 g。',
 [['贴近动作与拥抱者','hug · hugger']],
 'hug the coast 看路线贴近；hugger 不只职业后缀用法。',
 'The hugger gave her friend a hug before they followed the road hugging the coast.\n\n那位爱拥抱的人抱了抱朋友，然后两人沿贴着海岸的路前行。','hug hugger')
R('B3198','硅元素与相关材料，字母多一点类别就变','SILICON：元素硅；silicone 是另一类材料名','silicon → polysilicon；silicone 与元素名关联但不是同物。',
 '先分清元素与聚合材料，再认 poly- 多这一限定。中文硅、硅酮相近，英语 silicon、silicone 也只差一个字母，读音和类别都需对照。',
 'silicon 由 silica 等材料词族形成元素名；poly- 多 + silicon → polysilicon；silicone 是另一个材料命名。',
 [['硅元素与多晶硅','silicon · polysilicon'],['硅酮聚合材料','silicone']],
 'silicon 与 silicone 不同；polysilicon 通常多晶硅，不按硅酮胶理解。',
 'The text distinguishes silicon chips from silicone seals.\n\n文中区分了硅芯片与硅酮密封件。','silicon polysilicon silicone')
if __name__=='__main__':save('continuation_20261030_mn',ROOTS,WORDS)
