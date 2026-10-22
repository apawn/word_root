# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_nomen_a import W as A
from author_batch200_root_nomen_b import W as B
from author_batch200_root_nomen_c import W as C
from author_batch200_root_nomen_d import W as D
W=A+B+C+D
r=next(r for r in json.loads(Path('.cache/batch200/root.json').read_text())['roots'] if r['id']=='C0821')
kept=[w['word'] for w in W]+['nomenclature','interdenominational']
exclude={w:'较冷门的专业词、古称或低收益派生词，本轮暂略' for w in set(r['family'])|set(r['words']) if w not in kept}
ROOT=dict(id='C0821',meaning='名字、命名；由名字延伸的名声',core='NOMEN = NAME',image='把名字写进候选名单，是 nominate；给一类东西贴上名称，是 denomination；名字传得很远，形成 renown。标签与真实情况对不上，就可能是 misnomer。',intro='拉丁 nomen 的属格是 nominis，所以词形中会见到 nomen- 和 nomin-。本组从叫名字出发，分成提出人选、语法名称、给类别命名，以及名声好坏几条路。noun 虽短，也经法语接回拉丁 nomen。',forms='拉丁 nominare 是命名。nominate、nomination、nominator 各有借入形式，不能全部画成英语 nominate 的后代。nominal 可指名义上的或名词的；renown 经法语已看不出 nomin- 的全貌。英语 name 与拉丁 nomen 是更远层次的亲缘词，不是英语直接借了拉丁 nomen。',branches=[['提出名字作为人选','nominate, nomination, nominee, nominator, nominated, nominating'],['语言中的名称与名词','noun, pronoun, nominative, nominalization, nomenclature'],['挂名或象征性标示','nominal, nominally'],['用名称区分类别或单位','denomination, denominational, nondenominational, interdenominational, denominate, denominator'],['名字传开的声誉与失去体面','renown, renowned, ignominy, ignominious'],['名称不准确','misnomer']],contrasts='nominee 是被提名者，nominator 是提名人。nominally 不等于 normally。denomination 可以是面额或教派，denominator 是分母。nom-/nomen- 的命名一支不要与希腊 nomos“规则、分配”的另一组混写。',practice='The renowned scientist received a nomination, but being a nominee did not guarantee an award.\n\n这位享有声誉的科学家获得了提名，但被提名并不保证获奖。',words=kept,exclude=exclude)
if __name__=='__main__':
 for name,data in [('roots_nomen',[ROOT]),('words_nomen',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
