"""The palm family, lids, chins and knuckles."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0238':dict(words=['lid','eyelid'],label='远层同源比较：lid 是覆盖物',note='lid 接古英语 hlid，更远通常联系倾斜、靠下来的印欧语材料，与拉丁 clinare 仅作远层比较；lid 并非拉丁词直接借入。eyelid 则是 eye + lid。'),
 'B2752':dict(words=['eye','lid','eyelid'],label='eye + lid → eyelid：眼睛的盖',note='lid 补足 eyelid 的底词说明，基本是可开合的覆盖物；由物体盖子的日常画面理解眼睑名称。'),
 'A1776':dict(words=['chin','chins','knuckle','knuckles'],label='身体部位单数 → 复数：chin／chins，knuckle／knuckles',note='两个来源不同的身体名词，只按现代复数规则作本组对照；knuckles 还可能是动词第三人称单数。'),
}
R('C0949','手掌；棕榈；隐在手掌中的动作',
 'PALM：摊开的掌面，以及向外展开的叶片',
 '把手掌摊开，再看棕榈向外展开的叶片，能记住 palm 的两个常见名词义。手里藏住小物件，又能理解动词 palm。',
 '来源词是拉丁 palma，既说手掌也说棕榈；手掌义经法语 paume 等形式进入英语，树名还承接古英语从拉丁借入的形式。通常以展开的手、叶形联系解释树名。',
 'palm 是完整英语词，l 在常见标准读法中不发音。复数 palms 加 s，读 /z/；名词和动词形式相同，靠句法与上下文区分。',
 [['手与动作','palm palms'],['植物名称','palm palms']],
 'palm 可说手掌、棕榈，也可说把东西藏在掌中。palm off 常说把不好的东西冒充好的或强塞给别人，是另一固定搭配。',
 'He held the seed in his palm beneath a palm tree.\n\n他站在一棵棕榈树下，把种子托在掌心。',
 'palm palms')
W('palm','/pɑːm/','手掌、掌心；棕榈；把……藏在掌中；把劣物冒充、塞给别人〔palm off〕',
 '掌心是一块摊开的面；棕榈的叶片也向外展开。魔术师把硬币藏在掌心，还会用到动词 palm。',
 '手掌义经古法语 paume、palme 接拉丁 palma；树名经古英语及法语等路线，也接 palma。棕榈名称通常以叶片形似展开的手解释；动词从手掌名转用。',
 [['拉丁 palma → 英语不同借入路径','手掌；叶片如展开手指的棕榈'],['palm 名词 → 动词','掌心 → 把东西隐在掌中、操弄；palm off 欺骗性转交']],
 'the palm of your hand 手掌；a palm tree 棕榈树；palm oil 棕榈油；palm a coin 把硬币藏入掌中；palm something off as genuine 把东西冒充真品。',
 'hold something in your palm；palm it off on someone。','常见读音 l 不发音，读 /pɑːm/。手掌义和树名的近源借入路线不同，记忆时可共用展开的画面，但不是英语临时把手掌改成树。',
 ('She held the tiny shell in the palm of her hand.','她把小贝壳托在掌心。'),('A row of palm trees lined the road.','一排棕榈树立在路边。'),('The magician palmed the coin without anyone noticing.','魔术师把硬币藏进掌中，谁都没察觉。'),sources=['https://www.etymonline.com/word/palm','https://en.wiktionary.org/wiki/palm#English'])
W('palms','/pɑːmz/','手掌、棕榈〔复数〕；把……藏在掌中等〔palm 的第三人称单数〕',
 '两只摊开的手，可以说 palms；海边多棵棕榈也可以说 palms。是手还是树，通常看动作和地点就知道。',
 'palm + -s；l 仍不发音，词末 /m/ 后读 /z/。现代既是名词复数，也可能是动词在 he、she 等主语后的形式。',
 [['palm','手掌、棕榈；也可作动词'],['palm + -s → palms','多个手掌或棕榈；单数主语的动作']],
 'open palms 张开的手掌；sweaty palms 出汗的手心；palms facing up 手心朝上；tall palms 高大的棕榈树。',
 'rub your palms together；palms beside the beach。','his palms 是他的手掌；He palms the coin 是他把硬币藏进掌中。palm oil 中 palm 用单数作修饰语，不写 palms oil。',
 ('He held out his hands with his palms facing up.','他伸出双手，掌心朝上。'),('Tall palms stood behind the small beach house.','海边小屋后面立着高大的棕榈树。'),sources=['https://www.etymonline.com/word/palm','https://en.wiktionary.org/wiki/palms#English'])
W('lid','/lɪd/','盖、盖子；眼睑〔常见于相应搭配〕',
 '容器上面有一块能掀开、拿走的盖，是 lid。盖在眼球外面、能开合的眼睑，也保留了这个盖的画面。',
 '承接古英语 hlid 覆盖物、开口等词，现代开头的 h 消失。更远通常联系倾斜、靠合的日耳曼及印欧语材料；eyelid 是 eye 眼睛 + lid 盖。',
 [['古英语 hlid → lid','可开合、覆盖的物体'],['lid 及 eye + lid → eyelid','容器盖；眼睛的盖，即眼睑']],
 'a lid on a jar 罐盖；lift the lid 掀开盖子；put a lid on the pan 给锅盖上盖子；keep a lid on costs 控制费用。',
 'a loose lid；a tight lid。','cover 范围更广，书封、罩子、覆盖物都可能是 cover；lid 常是容器上可开合的一块盖。keep a lid on 以盖住锅的画面比喻控制、压住。',
 ('Put the lid back on the jar.','把罐子的盖子盖回去。'),('We need to keep a lid on unnecessary costs.','我们需要控制不必要的费用。'),sources=['https://www.etymonline.com/word/lid','https://en.wiktionary.org/wiki/lid#English'])
W('chin','/tʃɪn/','下巴',
 '嘴巴下方、脸最下端向前突出的那一块，是 chin。低头丧气时下巴垂着，鼓励人抬起头来，就有 keep your chin up。',
 '来自古英语 cin、cinn，下接日耳曼语同族，更远联系颌、下巴、脸颊词族。现代 chin 指嘴下方的外部下巴，不是整个承托牙齿的颌骨。',
 [['古英语 cin、cinn → chin','下巴；更早同族也有颌、脸颊的范围'],['具体部位 → 姿态比喻','keep your chin up 以抬头的姿态鼓励别灰心']],
 'rest your chin on your hand 把下巴搁在手上；a pointed chin 尖下巴；keep your chin up 别灰心、打起精神；take it on the chin 挨打击、承受不利结果。',
 'raise your chin；a chin strap。','chin 是脸最下端外表部位，jaw 常说颌骨及其轮廓。keep your chin up 通常是鼓励语，要按打起精神理解。',
 ('She rested her chin on her hand and listened.','她用手托着下巴听。'),('Keep your chin up; we can try again tomorrow.','别灰心，我们明天还能再试。'),sources=['https://www.etymonline.com/word/chin','https://en.wiktionary.org/wiki/chin#English'])
W('chins','/tʃɪnz/','下巴〔复数〕',
 '说好几个人各自的下巴，或者双下巴这样的轮廓时，会用 chins。英语也常用集合场景里的复数描述大家同一个动作。',
 'chin + 复数 -s，/n/ 后读 /z/。承接古英语下巴名，现代不改变词干，只标出不止一个。',
 [['古英语下巴词 → chin','嘴下方的外部部位'],['chin + -s → chins','多个下巴或复数场景中的对应部位']],
 'their chins 他们各自的下巴；double chins 双下巴〔复数谈论〕；keep their chins up 大家打起精神。',
 'lift their chins；rest their chins on their hands。','Their chins rested on their hands 是每个人托着自己的下巴，不必理解为每个人长着多个下巴。所有格与复数常按整组人的数量配合。',
 ('The children rested their chins on their hands.','孩子们都用手托着下巴。'),('They lifted their chins to look at the top shelf.','他们抬起下巴，望向最上层架子。'),sources=['https://www.etymonline.com/word/chin','https://en.wiktionary.org/wiki/chins#English'])
W('knuckle','/ˈnʌkəl/','指关节；突出的关节；认真干起来〔knuckle down〕；屈服〔knuckle under〕',
 '手指弯起来，关节处鼓出一个个小骨节，就是常说的 knuckle。开头虽然写 kn，常见现代发音只读 /n/。',
 '中古英语 knokel 等，属于日耳曼语小骨头、关节词，较早有表示小的形式材料，底词骨头已不以这个简单形式保留在现代英语中。不能把今天不存在的 knuck 当常用独立单词。',
 [['日耳曼语骨头词的指小形式 → knokel → knuckle','小骨头、突出的关节 → 常说指关节'],['knuckle 名词 → 动词及固定搭配','knuckle down 认真做；knuckle under 屈服']],
 'a finger knuckle 手指关节；knuckle down to work 认真工作；knuckle under to pressure 在压力下屈服。',
 'a swollen knuckle；knuckle down to studying。','knuckle down 的认真用功义通常联系弹珠游戏预备动作的扩展；knuckle under 是屈服。后面的小词变了，整组意思也变了。',
 ('He bent his finger slowly at the knuckle.','他在指关节处慢慢弯曲手指。'),('It is time to knuckle down and finish the report.','该认真干起来，把报告完成了。'),sources=['https://www.etymonline.com/word/knuckle','https://en.wiktionary.org/wiki/knuckle#English'])
W('knuckles','/ˈnʌkəlz/','指关节〔复数〕；knuckle 的第三人称单数〔常见于搭配〕',
 '握拳时，手背前端一排突出的骨节常叫 knuckles。主语是 he、she 等时，knuckles down 又可能说某人认真干起来。',
 'knuckle + -s：名词复数或动词第三人称单数，末尾 /l/ 后读 /z/，开头 k 仍不发音。较早小骨头的词义凝固成现代关节名。',
 [['knuckle 小骨节、关节','常指手指上突出的关节'],['knuckle + -s → knuckles','多个关节；也可作单数主语的动词形式']],
 'scraped knuckles 擦破的指关节；white knuckles 握紧后发白的指关节；knock with your knuckles 用指关节敲；She knuckles down 她开始认真干。',
 'tap with your knuckles；his knuckles turned white。','rap someone on the knuckles 字面是打指关节，也能比喻责备、处罚。句中 She knuckles down 的 knuckles 是动词，不是复数部位名。',
 ('She knocked on the door with her knuckles.','她用指关节敲了敲门。'),('When a deadline approaches, he knuckles down and works steadily.','临近截止日期时，他就会认真投入，踏实地干。'),sources=['https://www.etymonline.com/word/knuckle','https://en.wiktionary.org/wiki/knuckles#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vp',ROOTS,WORDS)
 extend_lessons()
