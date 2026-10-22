# -*- coding: utf-8 -*-
"""C1214 rept: crawling, modern animal names, and figurative language."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('reptile','/ˈreptaɪl/；美式也读 /ˈreptl/','爬行动物','想蜥蜴贴近地面爬行的样子：rept- 的历史动作是“爬”。现代 reptile 已成为分类名称，不是所有会爬的东西都算。','经古法语 reptile，也可直接接晚期拉丁 reptile；后者是 reptilis“爬行的”的中性名词用法，接拉丁 repere“爬”的 rept- 词干。不是 re-“再”加英语 tile“瓷砖”。',[['拉丁 repere → rept- → reptilis','爬行 → 爬行的'],['晚期拉丁 reptile → 古法语 reptile／英语 reptile','爬行的动物'],['近代动物分类逐渐收窄常用范围','日常通常指蛇、蜥蜴、龟、鳄等爬行动物']],'现代常用 reptile 指蛇、蜥蜴、龟、鳄等；蚂蚁会爬，青蛙也能贴地移动，却不是这个日常分类里的 reptiles。较早的自然史写法范围可能更宽，所以读古书时要留意年代。拿 reptile 骂人则是贬低对方卑劣、阴险，并非真的在分类。','a reptile species；a reptile enclosure；reptiles and amphibians。复数 reptiles。','amphibian 指两栖动物，reptile 指爬行动物。二者的分界不能只看是否会游泳；鳄鱼在水中活动也仍被称为 reptile。',('A tortoise is a reptile even though it carries a large shell.','乌龟虽然背着大大的壳，也属于爬行动物。'),('The museum has separate displays about reptiles and amphibians.','博物馆分别设置了爬行动物和两栖动物展区。'),sources=['https://www.etymonline.com/word/reptile','https://www.oxfordlearnersdictionaries.com/definition/english/reptile','https://www.amnh.org/exhibitions/permanent/reptiles-amphibians']),
E('reptilian','/repˈtɪliən/','爬行动物的；像爬行动物的；冷酷阴险的〔比喻〕','把 reptile 变成形容词：可以客观谈爬行动物的特征，也可以形容一个虚构角色的眼神或动作像蛇蜥，让人觉得冷冷的。','英语 reptile + -ian，去掉末尾不发音的 e 后构成形容词。十九世纪先用于爬行动物相关特征，随后出现冷酷、阴险等文学比喻。',[['拉丁 repere → reptilis → 英语 reptile','爬行 → 爬行动物'],['英语 reptile + -ian → reptilian','属于或像爬行动物的'],['后起比喻 reptilian','用人的想象描写冷酷、阴险等气质']],'reptilian skin 可以是爬行动物的皮肤，也可能是道具模仿出来的鳞状质感。a reptilian stare 则是作者把人的眼神比作想象中的蛇蜥眼神；这是文学效果，不是科学上判定爬行动物“道德冷酷”。','reptilian features；reptilian skin；a reptilian creature；a reptilian stare。重音在 -til-，不同于 reptile 的首音节重音。','reptile 常指一只动物；reptilian 常形容属性或相似外观。figurative reptilian 的“冷酷”是修辞，不能拿来等同于动物学的体温调节方式。',('The costume gave the creature a reptilian appearance.','这套戏服让那个生物看起来像爬行动物。'),('The novelist describes the villain’s silent, reptilian stare.','小说家描写了反派那种沉默而冷酷阴森的凝视。'),sources=['https://www.etymonline.com/word/reptilian','https://www.oxfordlearnersdictionaries.com/definition/english/reptilian']),
]
ROOT=dict(id='C1214',meaning='爬行、匍匐',core='repere 的动作是贴近地面爬行。rept- 是其历史词干形式，先产生“爬行的”，再用来称呼一类动物。',image='repere 爬 → reptilis 爬行的 → reptile 爬行动物 → reptilian 爬行动物的、像爬行动物的。',intro='词根给你动作画面，现代动物分类给你具体范围。把这两层分开，就不会因为虫子也会爬而叫它 reptile。',forms='拉丁 repere 与 rept- 是相关动词、词干形式。reptile 经过拉丁语及法语借入；reptilian 则是英语在已有词上加后缀形成。',branches=[['动物名称与属性','reptile, reptilian']],contrasts='reptile 中的 re- 不是可以单拆的“再”。文学里 reptilian 的阴冷感是比喻，也不能拿来替代生物分类或科学结论。',practice='先看一只贴地爬行的蜥蜴记 reptile；再给虚构生物加上鳞状皮肤记 reptilian。一个是名词对象，一个常用来描述特征。',words=[e['word'] for e in W],exclude={})
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id'])
 assert set(ROOT['words'])=={w for w in r['family'] if '-' not in w}
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_161.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('rept:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
