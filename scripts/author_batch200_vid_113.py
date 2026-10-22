# -*- coding: utf-8 -*-
"""C0491 glutin: glue, gluten and sticky rice."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
def S(w):return 'https://www.etymonline.com/word/'+w
def O(w):return 'https://www.oxfordlearnersdictionaries.com/definition/english/'+w
def K(w):return 'https://en.wiktionary.org/wiki/'+w
N='https://www.niddk.nih.gov/health-information/digestive-diseases/celiac-disease/eating-diet-nutrition'
W=[
E('glue','英、美 /ɡluː/','胶水；胶；用胶粘住；把事物连在一起的力量','两块原本分开的东西，中间添一点能黏住的材料，就不容易分开了。','名词经古法语 glu，接晚期拉丁 glus／glutem，远处来自拉丁 gluten“胶”。动词也有古法语 gluer／gluier 的借入路线，不能只把英语名词转动词当完整历史。',[['拉丁 gluten；晚期拉丁 glus／glutem','胶、黏合物'],['古法语 glu 名词；gluer／gluier 动词','胶；用胶粘住'],['中古英语 glew／glue → glue','现代名词和动词；进一步有关系、注意力的比喻义']],'名词 glue 通常不可数，说 some glue 或 a tube of glue。glue a photo to a page 是用胶粘照片；be glued to a screen 则像目光被粘住，表示一直盯着看。','a tube of glue；glue two pieces together；glue something to a surface；be glued to the screen。','stick 可以泛指粘住，也可指插、放等动作；glue 通常明确用胶。the glue that holds a team together 比喻维系团队的因素，并非把人困住。',('She glued the photograph to the first page of the album.','她把照片粘在相册第一页。'),('We need a little more glue before we can finish the model.','还需要一点胶水，我们才能做完这个模型。'),('Everyone was glued to the screen during the final minutes.','最后几分钟，所有人都目不转睛地盯着屏幕。'),sources=[S('glue'),O('glue_1'),O('glue_2'),K('glue')]),
E('gluten','英、美 /ˈɡluːtən/','面筋蛋白；麸质','想到面团中那部分能形成黏弹结构的蛋白，而不是把面粉里的淀粉也一并算进去。','经法语 gluten 或直接借拉丁 gluten“胶、黏合物”。英语早期用来称黏性物质、某些动物组织蛋白，后来逐渐成为谷物相关蛋白的名称；不是英语 glue 加 -ten。',[['拉丁 gluten','胶、黏合物'],['法语 gluten／拉丁直接借入 → 英语 gluten','早期指黏性物质及某些组织成分'],['谷物与食品用法','面筋蛋白；食品语境涉及小麦、大麦、黑麦等的相关蛋白']],'在烘焙中会讨论 flour 的 gluten 含量和面团性质；在食品标签中会讨论某种产品是否含 gluten。它是蛋白相关概念，不是糖、淀粉的另一个名字，也不是所有谷物都含有。','contain gluten；gluten content；wheat gluten；gluten intolerance。','glutinous 主要说黏，不等于 contains gluten。纯糯米本身不含这里所说的 gluten；具体做成的食品是否含有，还要看加入了什么。',('The baker compared the gluten content of two types of flour.','面包师比较了两种面粉的面筋蛋白含量。'),('The label states that the sauce contains gluten.','标签注明这种酱料含有麸质。'),sources=[S('gluten'),O('gluten'),N]),
E('glutinous','英、美 /ˈɡluːtənəs/','黏的；胶黏的；糯的','不是干爽地散开，而是黏在一起，有点像胶把各部分拉住。','来自古法语 glutineux 或拉丁 glutinosus，由拉丁 gluten“胶”的 glutin- 词干形成。它的黏性义早于现代食品蛋白 gluten 的常见用法，不能直接解释成“含麸质的”。',[['拉丁 gluten；词干 glutin-','胶、黏合物'],['拉丁 glutinosus；古法语 glutineux','像胶一样黏的'],['英语 glutinous','胶黏的；常见于 glutinous rice 糯米']],'菜单和食谱中的 glutinous rice 就是糯米，名字说的是黏糯质地。也可以说 a glutinous mixture，形容黏稠、黏结的混合物；不一定含小麦蛋白。','glutinous rice；glutinous rice flour；a glutinous mixture；a glutinous texture。','sticky 是更普通的“黏”；glutinous 较正式，常见于食物质地。gluttonous 则是“贪吃的”，多了一个 t，却走吞吃那条词源。',('These small cakes are made with glutinous rice flour.','这些小糕点是用糯米粉做的。'),('As the mixture cooled, it became thick and glutinous.','混合物冷却后变得浓稠而黏。'),sources=[S('glutinous'),O('glutinous'),'https://gluten.org/faq/is-it-safe-to-include-glutinous-rice-in-a-gluten-free-diet-what-exactly-is-it/',N]),
]
EX={w:'冷门物理、语言学、生化术语或罕用派生词，本轮暂略。' for w in ['gluon','agglutination','agglutinative','agglutinate','agglutinant','glutelin','glutinosity','nonagglutinative']}
SHARED=['superglue']
ROOT=dict(id='C0491',meaning='胶；黏合、黏住',core='拉丁 gluten 原本就是胶。沿法语变化走成短短的 glue，保留古典形式则有 gluten、glutinous；共同画面是东西黏在一起，现代意思却要分开。',image='拉丁 gluten 胶 → 法语 glu → glue；拉丁 gluten → gluten 食品蛋白；glutinosus → glutinous 黏的。',intro='这一根在手工、烘焙、食品标签里都实用。最容易踩的坑是把“黏”和“含面筋蛋白”混为一谈：糯米之所以叫 glutinous rice，是因为黏糯，不是因为里面有小麦麸质。',forms='glutin- 是拉丁 gluten 的词干形式。glue 经晚期拉丁和古法语变化，名词、动词各有借入路线；glutinous 也有独立的古法语、拉丁形容词来源。现代词义不能全靠字母相似推出。',branches=[['把物体或关系黏在一起','glue, superglue'],['食品成分与黏糯质地','gluten, glutinous']],contrasts='glue 是胶或粘贴动作，gluten 是食品语境中的蛋白名称，glutinous 描述黏。glutinous rice 不是“含 gluten 的米”；gluttonous 贪吃也不是此根。',practice='Glutinous rice is sticky, but its name does not mean that it contains gluten. 糯米很黏，名字中的黏性却不能拿来判断麸质成分。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=list(dict.fromkeys([w for w in r['family'] if '-' not in w and w not in EX]+SHARED))
 assert {e['word'] for e in W}<=set(ROOT['words']) and {e['word'] for e in W}<=set(m['owned_words'])
 assert len(W)==len({e['word'] for e in W}) and all(len(e['examples'])>=2 and len(e['history'])>=2 for e in W)
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_113.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('glutin:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
