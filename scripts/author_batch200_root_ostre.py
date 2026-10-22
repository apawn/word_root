# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
W=[E('oyster','英 /ˈɔɪstə/；美 /ˈɔɪstər/','牡蛎；蚝','两片粗糙硬壳包住柔软的身体，常作为海鲜出现在餐桌上。','经古法语 oistre 等形式及拉丁 ostrea，追到希腊 ostreon 牡蛎；它与表示硬壳、骨头的古老词族有关。',[['希腊 ostreon → 拉丁 ostrea','牡蛎，一种有硬壳的动物'],['古法语 oistre → 英语 oyster','牡蛎、蚝']],'oyster 是牡蛎，也就是菜单上常说的蚝。the world is your oyster 是固定说法，意思是眼前有很多机会，可以去闯、去选择。可以借开壳取物的画面帮助记忆，但不要把它改编成每只牡蛎里都有珍珠的生物知识。','oyster sauce 蚝油；oyster farming 牡蛎养殖；the world is your oyster 世界充满等你把握的机会。','oyster 是一种具体动物，shellfish 是范围更广的有壳水生动物统称。oyster 也不是所有贝壳的名称。',('The chef added a spoonful of oyster sauce to the vegetables.','厨师往蔬菜里加了一勺蚝油。'),('With those skills and a willingness to travel, the world is your oyster.','有了那些技能，又愿意到各地走走，你面前有许多机会。'),sources=['https://www.etymonline.com/word/oyster','https://www.oxfordlearnersdictionaries.com/definition/english/oyster','https://downloads.bbc.co.uk/learningenglish/shakespeare/bbc_shakespeare_the_worlds_mine_oyster.pdf'])]
ROOT=dict(id='C0931',meaning='牡蛎；有硬壳的海产动物',core='OSTRE = OYSTER',image='两片硬壳扣在一起，包住里面柔软的身体。',intro='希腊 ostreon、拉丁 ostrea 都指牡蛎。经过法语进入英语后，词形变成 oyster。它不是一个能在现代英语里随意拼装大量日常词的前缀，先记住这条具体来源和常见搭配就够用。',forms='ostre- 到 oyster 的变化经过历史借词过程；不能按今天的字母把 oyster 拆成 oy + ster。与骨头、硬壳的词有远源联系，不等于 oyster 是由英语 bone 造出来的。',branches=[['餐桌与日常比喻','oyster']],contrasts='oyster 是牡蛎，shell 是壳，shellfish 是更广的动物类别。the world is your oyster 是机会很多的比喻，并非在谈食物。',practice='The world is your oyster: many opportunities are open to you.\n\n世界充满机会：你有很多可能的路可以走。',words=['oyster'],exclude={'ostreophagist':'食牡蛎者的冷门称呼，日常学习先略过'})
if __name__=='__main__':
 for name,data in [('roots_ostre',[ROOT]),('words_ostre',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
