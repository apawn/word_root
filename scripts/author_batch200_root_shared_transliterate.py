# -*- coding: utf-8 -*-
import json
from pathlib import Path
from lesson_authoring import entry as E
W=[E('transliterate','/trænzˈlɪtəreɪt/','转写；用另一套文字表示','把一个名字从一种文字搬到另一种文字里，名字所指的东西并没有换。','trans-“跨到另一边” + 拉丁 littera / litera“字母” + -ate；按拉丁材料构成的英语词。',[['拉丁 trans + littera','跨越 + 字母、文字'],['英语 transliterate','把文字按规则转成另一套书写系统']],'把俄文 Москва 转写成 Moskva，处理的是字母和书写方式；把普通名词换成另一种语言中意思对应的词，则是在翻译。不同转写方案可能不同；转写也不必完全等同于按耳朵听到的发音拼写。','transliterate a name；transliterate into Latin letters。','translate 着重传达意思；transliterate 着重转换文字系统。两者可以出现在同一份译稿里，但不是同一操作。',('The catalogue transliterates the authors’ names into Latin letters.','这份目录把作者姓名转写成拉丁字母。'),('We transliterated the place name rather than translating its meaning.','我们对这个地名作了转写，没有翻译它的字面意思。'),sources=['https://www.etymonline.com/word/transliterate','https://ahdictionary.com/word/search.html?q=transliterate'])]
if __name__=='__main__':
 Path('.cache/batch200/drafts/root/words_shared_transliterate.json').write_text(json.dumps(W,ensure_ascii=False,indent=2))
 print('1 individually authored shared word')
