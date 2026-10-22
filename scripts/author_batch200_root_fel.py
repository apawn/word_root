# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
W=[E('feline','/ˈfiːlaɪn/','猫的；猫科的；像猫的；猫科动物','它可以直指猫，也可以抓住像猫一样的轻盈、敏捷或神态。','来自晚期拉丁 felinus 猫的，前身为拉丁 feles、felis 猫。更远来源不确定。-ine 在这类词中形成相关的形容词。',[['拉丁 feles、felis → felinus','猫 → 猫的'],['英语 feline','猫或猫科相关的；像猫的；也可作名词']],'feline behaviour 说猫的行为，feline grace 则说像猫一样轻盈的姿态。名词 a feline 可以指猫科动物，不只家猫。不过日常说自己养了一只猫，用 cat 最自然。','feline behaviour；feline grace；a feline companion；large felines。','feline 对应猫，canine 对应狗，equine 对应马。这些是相关的形容词，并不是给动物换一个更高级的名字。',('The researcher studies feline behaviour.','这位研究者研究猫的行为。'),('The dancer moved with feline grace.','这位舞者动作轻盈，像猫一样优雅。'),sources=['https://www.etymonline.com/word/feline','https://en.wiktionary.org/wiki/feline#English'])]
ROOT=dict(id='C0408',meaning='猫',core='FEL = CAT',image='猫轻轻落地，再无声地走开：feline 可以说这只动物，也可以借它的姿态形容动作。',intro='拉丁 feles、felis 指猫，felinus 是猫的。英语 feline 保留了动物分类和比喻姿态两种常见用法。',forms='feles、felis → felinus → feline。这里的 fel- 与 felicitous 里的幸运、贴切那条词源线不同。',branches=[['猫及像猫的特征','feline']],contrasts='说家猫用 cat 最直接；说猫相关的研究、特征，或像猫一样的动作，feline 很有用。',practice='The cat stretched with effortless feline grace.\n\n猫轻松地伸展开身体，姿态十分优雅。',words=['feline'],exclude={'Felinae':'猫亚科分类专名，暂不扩展。'})
ROOT['branches']=[[x[0],'；'.join(x[1:])] for x in ROOT['branches']]
if __name__=='__main__':
 for name,data in [('roots_fel',[ROOT]),('words_fel',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
