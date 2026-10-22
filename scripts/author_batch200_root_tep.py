# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
W=[E('tepid','/ˈtepɪd/','微温的；不冷不热的；不热心的','水只有一点温度，态度也只有一点热度。','来自拉丁 tepidus 微温的，源于 tepere 略微发热；英语先用于温度，后来扩展到感情和反应。',[['拉丁 tepere → tepidus','微温 → 微温的'],['英语 tepid','不冷不热的；比喻缺少热情的']],'tepid water 是温温的水；a tepid response 是反应平淡、没什么热情。说 tepid support 不是完全反对，而是支持得很勉强、力度不足。这个比喻和中文“不冷不热”很接近。','tepid water；a tepid response；tepid support；tepid applause。','warm welcome 是热情欢迎；tepid welcome 就显得敷衍或不够积极。lukewarm 与 tepid 的温度义、态度义都很接近。',('By the time he returned, his tea was tepid.','等他回来时，茶已经只有一点温度了。'),('The proposal received only a tepid response from the committee.','委员会对这项提案的反应相当冷淡。'),sources=['https://www.etymonline.com/word/tepid','https://en.wiktionary.org/wiki/tepid#English'])]
ROOT=dict(id='C1490',meaning='微温；不冷不热',core='TEP = LUKEWARM',image='用手碰水，既不烫也不冷；用同样的温度比喻，人的支持也可以没什么热度。',intro='拉丁 tepere 表示略微温暖，tepidus 是微温的。英语 tepid 把温度上的不够热，转成态度上的不热情。',forms='tepere → tepidus → 英语 tepid。物理温度与情绪热度是同一个词的两种常见应用。',branches=[['温度与态度','tepid']],contrasts='tepid 不等于冰冷。tepid support 仍可能是支持，只是程度弱；说 tepid water 也不是说水很凉。',practice='The room was full, but the applause was tepid.\n\n房间里坐满了人，掌声却不太热烈。',words=['tepid'],exclude={w:'低频名词或专业旧词，本轮略过。' for w in ['tepidarium','subtepid','tepefaction','tepidity','tepor']})
if __name__=='__main__':
 for name,data in [('roots_tep',[ROOT]),('words_tep',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
