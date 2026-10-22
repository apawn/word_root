# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
W=[E('trinity','英、美 /ˈtrɪnəti/','三位一体；密切相连的三个成员或要素','三个相互联系的成员被放在一起理解；宗教用法有特定含义。','借古法语 trinite，经后期拉丁 trinitas，接拉丁 trinus“三重的”、trini“每组三个”，与 tres“三”相关。英语可看到 trin- 与 -ity 的对应，但它是完整借词，不是在现代英语中由 three 直接拼出来的。',[['拉丁 tres；trini / trinus','三；每组三个、三重的'],['后期拉丁 trinitas → 古法语 trinite','三重性；用于三位一体教义'],['中古英语 trinite → 英语 trinity','三位一体；后来也说相连的三个成员或要素']],'大写的 the Trinity 通常说基督教中的圣父、圣子、圣灵三个位格而同为一位上帝；不要把这个教义改说成“三个神”。普通小写 a trinity of ... 是较正式或带修辞色彩的说法，突出三个东西紧密相关，如品质、价格、服务被看成共同决定体验的三要素。','the Trinity；the Holy Trinity；a trinity of ideas；a trinity of essential elements。','trio 是更普通的三人组、三件套，尤其常用于音乐；trinity 常突出三个成员的联系，也容易带宗教联想。日常数出三个苹果，直接说 three apples 即可。',('The guide explained the painting’s symbols of the Trinity.','导游解释了画中象征三位一体的符号。'),('The designer described light, space and colour as a trinity of essential elements.','设计师把光线、空间和色彩称为相互配合的三大基本要素。'),sources=['https://www.etymonline.com/word/trinity','https://www.merriam-webster.com/dictionary/trinity','https://www.oxfordlearnersdictionaries.com/definition/english/trinity'])]
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']=='C1554');keep={w['word']for w in W};excluded={w:'按用户要求暂略占星、三元系统或文学中的少用说法，保留通用文化阅读词。'for w in set(r['family'])-keep}
ROOT=[dict(id='C1554',meaning='每组三个；三重的',core='trin-：三个相连、成组来看。',image='把三个相关成员圈在同一组里；宗教中的三位一体需按教义理解。',intro='拉丁 trini 表示每组三个，trinus 表示三重的，与 tres“三”相关。trinity 经法语进入英语，宗教义常大写；一般文章也会借它强调三个要素构成紧密的一组。',forms='trin- 与更熟悉的 tri-“三”有历史联系；trinity 的 -ity 对应名词形式，但整词经拉丁、法语借入。',branches=[['宗教概念与三者组合','trinity']],contrasts='宗教的 the Trinity 不是三个神；普通的 a trinity of ... 是较正式的三者组合，不是所有三个东西都需要这样说。',practice='分别写出 the Trinity 和 a trinity of ...，说明大小写、冠词和使用场景的区别。',words=[w for w in r['family']if w in keep],exclude=excluded,sources=['https://www.etymonline.com/word/trinity','https://www.merriam-webster.com/dictionary/trinity'])]
assert keep==set(r['family'])-set(excluded)
assert all(w['word']in m['owned_words']for w in W)
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history']),w['word']
for k,d in [('roots',ROOT),('words',W)]: (OUT/f'{k}_batch200_spec_153_trin.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C1554',len(W),'new',sum(len(w['examples'])for w in W),'examples')
