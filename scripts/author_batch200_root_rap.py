# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_rap_a import WA
from author_batch200_root_rap_b import WB
from author_batch200_root_rap_c import WC
W=WA+WB+WC
ROOT=dict(id='C1203',meaning='猛地抓住、夺取、带走',core='RAP / RAPT = SEIZE / CARRY OFF',image='一只手猛地抓住东西，把它带走。这个动作可以真的发生在财物和猎物上，也可以形容急水冲走泥土，或音乐把人的心神整个吸引走。沿各自历史路线，就出现了迅速、掠夺、沟谷和陶醉。',intro='本页接拉丁 rapere“抓住、夺走”，第一人称形式为 rapio，分词为 raptus。后来的法语支线常出现 rav-，复合词里还可出现 rip-、rept-。先抓“攫住并带走”的共同背景，再分清现代各词的具体语气。',forms='rap- 见 rapid、rapacious；rapt- 见 rapt、rapture、raptor；经法语形成的 rav- 见 ravish、ravage、ravine、ravenous。surreptitious 的 surr- 来自 sub- 的同化，-rept- 属 rapere 的复合变化。不要因此把所有含 rept 的词都归入本页，reptile 的爬行词源是另一支。',branches=[['动作迅疾、变化很快','rapid, rapidly, rapidity'],['心神被吸引走','rapt, rapture, rapturous, rapturously, enrapture, enraptured, enrapt'],['强烈食欲与贪婪攫取','ravenous, ravenously, rapacious, rapacity, rapaciously, rapaciousness'],['抓住猎物','raptor, raptorial'],['急水与破坏','ravine, ravage, ravager, rapine'],['避开注意、隐瞒依据','surreptitious, surreptitiously, surreptitiousness, subreption'],['强行带走与心神陶醉的分化','rape, ravish, ravishing, ravishingly, ravishment'],['古旧的攫住心神说法','raptus, arreption, arreptitious']],contrasts='ravenous 不来自鸟名 raven；植物 rape 与性暴力义 rape 不同源。ravage 是严重破坏，ravishing 常是美得令人陶醉。rapacity 与 rapidity 等名词有各自的拉丁、法语借入路线，不能一律画成英语形容词加后缀。rapture 和 rupture 也不是同一词族。',practice='After a rapid walk, the ravenous hikers stopped beside a ravine. Later, they listened with rapt attention as the guide told a story.\n\n快走一段之后，饥肠辘辘的徒步者在沟谷旁停下。后来，向导讲故事时，他们听得全神贯注。',words=[w['word'] for w in W]+['arreption'])
if __name__=='__main__':
 assert len(W)==33
 for name,v in [('roots_rap',[ROOT]),('words_rap_a',WA),('words_rap_b',WB),('words_rap_c',WC)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(v,ensure_ascii=False,indent=2))
 print(len(W),'individually authored words',sum(len(w['examples']) for w in W),'examples')
