# -*- coding: utf-8 -*-
"""C1429 stom: common stomach words and the useful mouth/opening concept."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
def S(w):return 'https://www.etymonline.com/word/'+w
def K(w):return 'https://en.wiktionary.org/wiki/'+w
def O(w):return 'https://www.oxfordlearnersdictionaries.com/definition/english/'+w
ST=[['希腊 stoma“口、开口” → stomakhos','原指咽喉、食道等开口通道；后也指胃'],['拉丁 stomachus → 古法语 estomac／stomaque','咽喉、胃；也发展出欲望、情绪等相关用法'],['中古英语 stomak／stomake → stomach','胃；日常也指肚子，后来动词常指忍受']]
W=[
E('stomach','英、美 /ˈstʌmək/','胃；肚子；〔动词〕忍受、接受','食物进入胃，胃容纳并处理食物；“这事我实在咽不下去”又能帮助理解 can’t stomach 的忍受不了。','经古法语 estomac／stomaque、拉丁 stomachus，接希腊 stomakhos，远接 stoma“口、开口”。最早的名称涉及咽喉、食道和内部开口，后用于胃；这是名称指向的变化，不是器官变成另一个器官。',ST,'胃是具体消化器官，但日常 I was hit in the stomach 常说被打到肚子。I can’t stomach his excuses 则说受不了他的借口。ch 读 /k/，不要读成 /tʃ/。','an empty stomach；an upset stomach；butterflies in my stomach；can’t stomach something。','belly、tummy 常指肚子；stomach 在准确解剖语境指胃。can’t stomach 是难以接受，和实际能否消化食物不一定有关。',('My stomach rumbled while I was waiting for lunch.','等午饭时，我的肚子咕咕叫。'),('He lay on his stomach to look under the sofa.','他趴着查看沙发底下。'),('I can’t stomach the way he treats his colleagues.','我受不了他对待同事的方式。'),sources=[S('stomach'),K('stomach'),O('stomach_1'),O('stomach_2')]),
E('stomachache','英、美 /ˈstʌməkeɪk/','肚子痛；胃痛','肚子这一带痛，日常先用一个宽泛的词说出来，并没有凭这个词确定具体哪个器官或什么原因。','英语 stomach + ache“持续的疼痛”；也常分写 stomach ache。合成发生在英语里，前半来自希腊、拉丁和法语路线，ache 则是英语本族的疼痛词。',ST+[['英语 stomach + ache → stomachache','肚子或胃附近的疼痛；也写 stomach ache']],'have a stomachache 是肚子痛；complain of stomachache 是诉说肚子痛。日常的 stomach 范围可能宽于医学上的胃，因此不应把这个表达直接当作某种具体诊断。','have a stomachache；get a stomachache；a mild stomachache。','headache 是头痛，stomachache 是肚子痛；两者都用 ache。stomachache 说明疼痛位置的大概范围，不说明病因。',('She went home early because she had a stomachache.','她因为肚子痛而提前回家。'),('The child described the discomfort as a stomachache.','孩子把那种不舒服描述为肚子痛。'),sources=[K('stomachache'),O('stomach-ache'),S('stomach')]),
E('stoma','英 /ˈstəʊmə/；美 /ˈstoʊmə/','气孔；身体的开口；外科造口','核心就像一个让物质进出的“小口”。植物上可以是叶片气孔，医疗文章里则常指手术形成的开口。','经近代拉丁 stoma，直接采用希腊 stoma“口、开口”。它与 stomach 共用更早的希腊来源，但英语 stoma 不是把 stomach 后几个字母删掉得到的。',[['希腊 stoma，复数 stomata','口；出入口'],['近代拉丁 stoma → 英语 stoma','生物体上的开口'],['植物学与医学用法','植物气孔；手术形成的造口等']],'植物的 stomata 是气体和水蒸气进出的孔，周围保卫细胞调节开合。医疗语境中的 abdominal stoma 是腹部造口，可为排泄提供出口；stoma 是开口本身，不是外面的收集袋。复数可用 stomata，也有 stomas。','leaf stomata；a stoma nurse；stoma care；an abdominal stoma。','植物气孔与外科造口是不同结构，联系在于“开口”。stomach 是胃，stoma 不是胃的另一种拼法。',('Under the microscope, the students could see stomata on the leaf surface.','在显微镜下，学生们能看到叶片表面的气孔。'),('The booklet explains what a stoma is in plain language.','这本小册子用通俗语言解释了什么是造口。'),sources=[S('stoma'),K('stoma'),O('stoma'),'https://openstax.org/books/biology/pages/30-4-leaves','https://www.nhs.uk/tests-and-treatments/colostomy/what-is-a-colostomy/']),
]
SHARED=[]
EX={w:'主要是专科手术、胚胎分类或罕用口腔术语，按用户常用阅读优先要求暂略。' for w in ['anastomosis','anastomotic','deuterostome','monostomous','ozostomia','pentastomid','protostome','stomatalgia','stomatic','stomatoplasty']}
ROOT=dict(id='C1429',meaning='口；开口、通道入口',core='希腊 stoma 的本意是口，也泛指开口。用一个能让东西进出的口来理解这个根，比把它一律背成“胃”准确。',image='口、开口 → 咽喉和食道的名称 stomakhos → stomach 胃；直接采用开口名称 → stoma 植物气孔或医学造口。',intro='日常最值得掌握的是 stomach，包括胃、肚子和“忍受”的动词用法。stoma 则帮助读懂植物科普和基础医疗说明。',forms='stoma 的希腊屈折形式带 stomat-，所以复数是 stomata。stomach 经过拉丁和法语，有自己的较早借入路线；stoma 是后来采用近代拉丁的学术词，两者不是现代英语彼此删字母派生。',branches=[['胃、肚子与忍受','stomach, stomachache'],['进出的开口','stoma']],contrasts='stomach 指胃，日常也泛指肚子；stoma 指开口。stomachache 不是具体病名。can’t stomach something 常说无法接受某事，与真正吃东西无关。',practice='I can’t stomach that excuse. 这个借口我实在接受不了：用“咽不下去”记住 stomach 的动词用法。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=list(dict.fromkeys([w for w in r['family'] if '-' not in w and w not in EX]+SHARED))
 assert set(ROOT['words'])==set(SHARED)|{e['word'] for e in W}
 assert {e['word'] for e in W}<=set(m['owned_words'])
 assert len(W)==len({e['word'] for e in W}) and all(len(e['examples'])>=2 and len(e['history'])>=2 for e in W)
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_76.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('stom:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
