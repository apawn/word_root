# -*- coding: utf-8 -*-
"""C0412 femor: the thigh and thighbone."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('femur','英 /ˈfiːmə/；美 /ˈfiːmər/','股骨；大腿骨','摸清位置就很好记：从髋到膝之间，大腿内部那根长骨就是 femur，不是整条腿，也不是骨盆。','直接借入拉丁 femur“大腿、股部”，在英语解剖学里常专指股骨。拉丁属格 femoris 展示 femor- 词干；不要把它与表示女性的 femin- 混为一谈。',[['拉丁 femur，属格 femoris','大腿、股部；词干 femor-'],['英语解剖词 femur','大腿里的股骨']],'现代医学、人体模型和古生物化石说明中都能遇到。人的股骨上端参与髋关节，下端参与膝关节。日常说 thigh bone 更直白，femur 是同一块骨头较正式的名称。','a fractured femur；the head of the femur；the left femur；复数 femurs，也可 femora /ˈfemərə/。','thigh 是大腿整个区域，femur 是其中的骨；pelvis 是骨盆，tibia 是小腿胫骨，位置都不同。',('The model shows the femur between the hip and the knee.','模型展示了髋部与膝部之间的股骨。'),('The fossil collection includes a large animal’s femur.','这批化石藏品包括一根大型动物的股骨。'),sources=['https://www.etymonline.com/word/femur','https://www.oxfordlearnersdictionaries.com/definition/english/femur','https://my.clevelandclinic.org/health/body/22503-femur']),
E('femoral','/ˈfemərəl/','大腿的；股部的；股骨的','它可以把范围指向“大腿这个区域”，也可以具体指“股骨这根骨头”。看后面的名词，才知道说的是血管、神经还是骨。','来自拉丁型形容词 femoralis，接 femur 的词干 femor- 与 -alis。英语现代可用 femur + -al 来帮助理解，但 femor- 的拼写来自拉丁词干，形容词也有独立的借入历史。',[['拉丁 femur／femor-','大腿；词干 femor-'],['中世纪拉丁 femoralis → 英语 femoral','与大腿、股部有关；也指股骨的']],'femoral artery 是股动脉，名称说明它与大腿区域有关，不是说它是一块骨。femoral head 是股骨头，则真正在谈股骨的一部分。读懂“部位形容词 + 结构名词”的组合，医学词就不必逐个死背成毫无联系的名词。','femoral artery；femoral vein；femoral nerve；femoral head；femoral fracture。注意 femur 的首音节 /fiː/ 到 femoral 变为 /fe/。','femoral 指大腿或股骨相关，femur 专指股骨。它没有“女性的”意思，不能与 female、feminine 按开头拼写归为一族。',('The anatomy chart labels the femoral artery in the thigh.','解剖图标出了大腿部位的股动脉。'),('The report describes a fracture of the femoral neck.','报告描述了一处股骨颈骨折。'),sources=['https://www.etymonline.com/word/femoral','https://www.oxfordlearnersdictionaries.com/definition/english/femoral','https://www.merriam-webster.com/dictionary/femoral','https://my.clevelandclinic.org/health/body/21645-femoral-artery']),
]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']=='C0412')
ROOT=dict(id='C0412',meaning='大腿、股部',core='femor- 来自拉丁 femur 的词干，原来指大腿区域。英语 femur 常专指股骨，femoral 仍可广泛修饰股部的骨、血管与神经。',image='拉丁 femur／femor- 大腿 → 英语 femur 股骨；femoralis → femoral 股部的、股骨的。',intro='先确定髋到膝之间的大腿位置，再区分整片区域与其中一根骨。这个小区别足以避免大多数误读。',forms='拉丁主格 femur、属格 femoris 展示 femur／femor- 的变化。英语 femoral 的短元音与 femur 的长元音不同；现代“词根 + -al”分析不取代它的拉丁借词历史。',branches=[['骨头与部位形容词','femur, femoral']],contrasts='femur 是骨，femoral artery 是股部的动脉，不是骨内动脉的专名。femor- 与 femin- 的女性义不属于同一条来源。',practice='读 femoral 后，立刻找它修饰的结构：head 是骨的部分，artery 是血管，nerve 是神经。',words=[e['word'] for e in W],exclude={})
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_175.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('femor:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
