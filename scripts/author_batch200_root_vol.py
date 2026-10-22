# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_vol_a import W as A
from author_batch200_root_vol_b import W as B
from author_batch200_root_vol_c import W as C
W=A+B+C;kept=[w['word'] for w in W]+['benevolent','benevolence']
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C1656')
EX={w:'较冷门的哲学或宗教词、低收益派生，本轮暂略' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C1656',meaning='愿意、希望、意志；愉悦一支的远源另有不确定性',core='VOL / VOLUNT = WILL, WISH',image='别人还没强迫，你先举手说“我愿意”，就是 voluntary 与 volunteer 的核心。benevolent 是盼别人好，malevolent 是盼别人倒霉。',intro='拉丁 velle 表愿意，volo 是“我愿意”，volens 是愿意的，voluntas 是意愿。词形变化看起来不小，却围绕同一件事：人的愿望与选择。voluptuous 直接来自“愉悦”的另一支，它与 velle 的远层联系只宜保留为可能关系。',forms='volunt- 出现在 voluntary、volunteer；volit- 出现在 volition、volitional；-volent 出现在 benevolent、malevolent。voluntary 与 involuntary 各有拉丁借入形式，不全是现代英语现拼。这里不是 volare“飞”或 volvere“卷、转”的词族。',branches=[['主动举手与志愿服务','volunteer, volunteering, volunteered, volunteerism'],['出于或不出于自己意愿','voluntary, voluntarily, involuntary, involuntarily'],['意志与选择过程','volition, volitional'],['对人的善意与恶意','benevolent, benevolence, malevolent, malevolence'],['愉悦支线：远源关系未完全确定','voluptuous']],contrasts='voluntary 说自愿，voluntarily 说自愿地行动。involuntary 不一定等于 unconscious；人可能清醒地经历非自愿的调动。malevolent 的 male- 是坏，不是男性。voluptuous 不等于 voluminous。',practice='She volunteered of her own volition, while her colleague joined only because attendance was compulsory.\n\n她出于自己的意愿主动报名，而同事参加只是因为必须出席。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_vol',[ROOT]),('words_vol',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
