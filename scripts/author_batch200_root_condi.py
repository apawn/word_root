# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
W=[E('condiment','英 /ˈkɒndɪmənt/；美 /ˈkɑːndəmənt/','调味品；佐餐调料','饭菜已经有了，再添一点让它更有味道的东西。','拉丁 condire 腌制、调味 → condimentum 调味料，经古法语 condiment 进入英语。不要因拼写相近就拆成 condition 条件。',[['拉丁 condire → condimentum','腌制、调味 → 调味品'],['古法语 condiment → 英语 condiment','给食物添味的材料或酱料']],'餐桌上的芥末酱、番茄酱、酱油等都可称 condiments。这个词按用途归类，不限定一定是粉末，也不限定一定很辣。复数很常见，例如调料架、餐厅里的调味品区。','a selection of condiments；table condiments；a condiment tray。','spice 多指植物来源的香辛料；condiment 强调给食物调味的用途，范围可包含酱料。ingredient 则是所有配料的更宽泛称呼。',('Mustard and ketchup are common condiments for burgers.','芥末酱和番茄酱是汉堡常用的调味品。'),('The waiter placed a tray of condiments on the table.','服务员把一盘调味品放到桌上。'),sources=['https://www.etymonline.com/word/condiment','https://en.wiktionary.org/wiki/condiment#English'])]
ROOT=dict(id='C0249',meaning='调味；腌制保存',core='CONDI = SEASON / PRESERVE',image='往食物里添盐、香料或酱汁，让味道更好；历史上调味与保存也有联系。',intro='拉丁 condire 表示调味、腌制，condimentum 则指用于调味的东西。现代最实用的后代是 condiment。',forms='condire → condimentum → 古法语 condiment → 英语 condiment。现代学习时可联系 -ment 的名词形式，但英语借入的是已经形成的词。',branches=[['调味的东西','condiment']],contrasts='condiment、condition、condemn 不能只看开头相似就归成一组。这里抓住的是调味，不是条件，也不是谴责。',practice='Different diners choose different condiments for the same dish.\n\n面对同一道菜，不同食客会选不同调味品。',words=['condiment'],exclude={})
if __name__=='__main__':
 for name,data in [('roots_condi',[ROOT]),('words_condi',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
