# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_andr_a import W as A
from author_batch200_root_andr_b import W as B
W=A+B
words=[w['word'] for w in W]+['misandry']
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0053')
EX={w:'较冷门的专业派生、旧词或专名，本轮按学习优先级暂略' for w in r['family'] if w not in words and '-' not in w}
ROOT=dict(id='C0053',meaning='男子、男性、丈夫；部分词中泛指人的形态',core='ANDR = MAN / MALE',image='抓住对象是谁：andr- 通常落在男性或丈夫。接形状成为人形机器人；接女性成分谈兼具特征；接多个、憎恨或中心，则分别说明数量、态度和观察视角。',intro='希腊 anēr 的属格 andros 显出 andr-。常见连接形式是 andro-。android 在现代是人形机器人，androgen 是雄激素，androgynous 的 gyn 则是女性，不能把这几个相似词混成一类。',forms='andr-、andro-、-andry 是常见形式。-oid 表形似，-gen 与产生或促生有关，gyn- 表女性。philander 经过文学人物名转成普通词，不能仅按爱加男人来猜今天的意思。',branches=[['人的外形','android'],['激素及其作用','androgen, androgenic'],['男性与女性特征的组合','androgynous, androgyny'],['从文学情人名到拈花惹草','philander, philanderer'],['社会关系、态度与视角','polyandry, misandry, androcentric']],contrasts='android 是人形机器人，androgen 是雄激素，androgyny 是兼具男女特征或中性风格。androcentric 以男性为中心，anthropocentric 以人类为中心。相似的词头必须连同后半段一起读。',practice='The article discusses androgynous fashion; the biology chapter discusses androgenic effects.\n\n这篇文章讨论中性风格的时装；生物学章节讨论雄激素样作用。',words=words,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_andr',[ROOT]),('words_andr',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
