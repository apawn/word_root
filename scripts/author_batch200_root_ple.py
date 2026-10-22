# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
W=[E('plethora','/ˈpleθərə/','大量；过多；过剩','东西一下子涌来，满满当当，甚至多到难以挑选或处理。','经晚期拉丁 plethora 来自希腊 plethore 充满，关联 plethein 变满。英语早期是旧医学中的充盈术语，后来泛指数量过多或很多。',[['希腊 plethein → plethore','充满 → 满、饱和'],['晚期拉丁 plethora → 英语 plethora','旧医学的过度充盈 → 大量、过剩']],'a plethora of options 是一大堆选择，常带多得有些过头的感觉。现代也有人只用来强调丰富，并不一定批评；看后文是说眼花缭乱还是机会很多。它偏书面，日常说 many 或 lots of 往往更直接。','a plethora of choices；a plethora of information；a plethora of explanations。','plethora 常比 abundance 更容易让人想到过量，但现代用法并非每次都含负面评价。不能只按旧词源强迫所有句子译成病态过剩。',('A plethora of settings made the simple app surprisingly hard to use.','过多的设置让这个简单应用反而变得很难用。'),('The festival offered a plethora of workshops for visitors to explore.','这个节日提供了丰富的工作坊，供游客体验。'),sources=['https://www.etymonline.com/word/plethora','https://www.merriam-webster.com/dictionary/plethora'])]
ROOT=dict(id='C1062',meaning='充满；数量多',core='PLE / PLETH = BE FULL',image='一个容器被装得满满的，满到溢出；后来任何数量多得惊人的事物都能借这个画面。',intro='希腊 plethein 表示充满，plethore 表示满、饱和。日常阅读最值得抓住的是 a plethora of，表示大量，有时暗含多得过头。',forms='plethora 是整体借入的词，不是英语 plenty 缩短后加词尾。它的医学旧义解释了从充盈走向过多的路径，但现代用法已广得多。',branches=[['大量或过剩','plethora']],contrasts='大量不总是好，也不总是坏。a plethora of options 后面若说 difficult to choose，就突出过多；若说 something for everyone，则可能赞赏丰富。',practice='A plethora of choices can be exciting or overwhelming.\n\n选择很多，既可能令人兴奋，也可能让人应接不暇。',words=['plethora'],exclude={w:'低频或细分专门词，本轮略过' for w in ['pleroma','plethysmograph','plethoric','plethodontid','plethysm','plethysmometry']})
if __name__=='__main__':
 for name,data in [('roots_ple',[ROOT]),('words_ple',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
