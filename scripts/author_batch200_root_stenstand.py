# coding: utf-8
import json
from pathlib import Path
ROOT=dict(id='C1414',meaning='站立；原有立场；离开原来的立场',core='ST / STA = STAND',image='原来站在一个群体或信仰里，后来从那个位置走开。',intro='本页沿目录中的 sten- 入口补看站立这一词族。apostasy、apostate 的实际历史要追到希腊 histēmi 站立、使站立及 aphistēmi 离开；不能把它们机械拆出一个现代英语 sten。',forms='apo- 离开 + histēmi 站立 → aphistēmi 离开、脱离；再分别形成 apostasía 和 apostátēs，经拉丁语等路线成为 apostasy、apostate。两者是不同的历史名词分支。',branches=[['脱离信仰或立场','apostasy；apostate']],contrasts='apostasy 是放弃、背离原信仰或立场的行为；apostate 是这样做的人。这个词族还要与表示狭窄的 sten- 分开，两者并非一个意思。',practice='The novel follows an apostate and examines the consequences of apostasy.\n\n小说追踪一位弃教者的经历，并探讨弃教带来的后果。',words=['apostasy','apostate'],exclude={})
if __name__=='__main__':
 Path('.cache/batch200/drafts/root/roots_stenstand.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2));print('1 shared root')
