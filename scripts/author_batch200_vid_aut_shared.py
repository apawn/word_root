# -*- coding: utf-8 -*-
"""Early shared aut- lesson needed by cracy; root page follows later."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('autocracy','英 /ɔːˈtɒkrəsi/；美 /ɔːˈtɑːkrəsi/','独裁统治；专制制度；专制国家','重大决定集中在一个统治者手里，缺少能有效限制他的权力；这就是现代 autocracy 最典型的画面。','希腊 autos 自己 + kratos 权力，形成 autokratēs 及抽象名词 autokrateia；有直接希腊借入及经法语 autocratie 的分析。早义曾涉及自主、自我控制，现代政治义还受 autocrat 等相关称谓影响，不只是把 auto- 译成自动。',[['希腊 autos 自己 + kratos 权力 → autokratēs','自行支配、拥有单独权力的'],['希腊 autokrateia；另有法语 autocratie 中介分析 → 英语 autocracy','早有自主权、自我控制等义'],['受 autocrat 等统治者称谓影响的现代政治义','权力高度集中、缺乏有效制约的专制统治']],'既可指统治方式，也可用 an autocracy 指实行这种统治的国家。工作场景里偶尔用来批评一个组织由某人一言堂，但这属于比喻，不能把每次个人作决定都叫独裁制度。','absolute autocracy；an autocracy；the transition from autocracy。','autonomy 是自治、自主；autocracy 现代通常指专制。monarchy 说明有君主，是否专制还要看实际权力安排。',('The chapter compares autocracy with constitutional government.','这一章比较专制统治与宪政政府。'),('They described the organisation as a small autocracy in which one person made every decision.','他们把这个组织形容成一个小型独裁体制，所有决定都由一个人作出。'),sources=['https://www.etymonline.com/word/autocracy','https://www.merriam-webster.com/dictionary/autocracy','https://www.oxfordlearnersdictionaries.com/definition/english/autocracy'])]
if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'words_batch200_vid_aut_shared.json').write_text(json.dumps(W,ensure_ascii=False,indent=2))
    print('autocracy:',len(W),'word;',sum(len(e['examples']) for e in W),'examples')
