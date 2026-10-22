# -*- coding: utf-8 -*-
"""C0012 acr: a tip, a high point, and the leading edge of a line."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('acrostic','英 /əˈkrɒstɪk/；美 /əˈkrɔːstɪk/','藏头诗；用各行特定字母拼出词语的文字','横着读是几行文字，竖着读每行开头，又藏着另一个词。这就是常见的 acrostic。','源头是希腊 akrostikhis，由 akro-“端头”与 stikhos“行、诗行”组成，经拉丁 acrostichis 和法语 acrostiche 等路线进入英语。末尾本来含有表示诗行的 -stich，后来受英语 -ic 词尾影响变成 acrostic，不能机械拆成 acro + 普通形容词后缀 -ic。',[['希腊 akro- + stikhos → akrostikhis','端头 + 诗行 → 从各行端头读出文字'],['拉丁 acrostichis；法语 acrostiche','相应的藏头诗名称'],['英语 acrostic','词尾受 -ic 形式影响；也可作修饰诗或谜题的词']],'最容易理解的做法，是三行依次以 C、A、T 开头，竖着读就得到 CAT。通常藏的是首字母，也有选取每行其他位置的形式。它不要求每行都很短，也不一定押韵，关键是行与行之间还藏了一条读法。','an acrostic poem；write an acrostic；an acrostic puzzle。名词可数，复数 acrostics。','acronym 用多个词的开头字母组成缩略名称；acrostic 把信息藏进多行文字的位置里。二者都关注“开头”，但组织方式不同。',('The children wrote an acrostic using the letters of their school’s name.','孩子们用学校名称中的字母写了一首藏头诗。'),('Read the first letter of each line to find the message hidden in the acrostic.','读出每行的首字母，就能找到这篇藏头文字里的隐藏信息。'),sources=['https://www.etymonline.com/word/acrostic','https://www.oxfordlearnersdictionaries.com/definition/english/acrostic','https://en.wiktionary.org/wiki/acrostic'])]
SH={'acronym','acrobat','acrobatic','acrobatics','acropolis','acrophobia'}
EX={w:'较冷门的专门医学、解剖学或建筑术语，本轮按通用阅读优先暂略。' for w in ['acromegaly','acromion','acrochordon','acrotomophilia','acromegalia','acroterion']}
ROOT=dict(id='C0012',meaning='高处、顶端；端头、尖端',core='想象一个东西最外面的端头：可以是山顶和城市的高处，也可以是脚尖或一行文字的开头。acro- 并不总要译成“高”。',image='希腊 akros／akron 顶端、端头 → acropolis 高处的城；acrobat 踮脚、高处表演者；acronym 取词头的名称；acrostic 取行头的文字。',intro='这一组最有用的联系，是把“高点”和“开头”看成不同场景中的端部。走到高处是 acro-，取一行文字的头部也可以是 acro-；后面接什么，决定它具体指哪种端头。',forms='希腊 akros 是处在最外端、最高处的，akron 是端部、顶点，组合形式常作 acro-。acrobat 经法语及希腊拉丁化形式借入；acronym 是近代名称；acrostic 的后半部接诗行 stikhos。',branches=[['身体技巧与表演','acrobat, acrobatic, acrobatics'],['高处与恐高','acropolis, acrophobia'],['文字的开头','acronym, acrostic']],contrasts='acrobat 不只指走钢丝的人，现代还包括多种杂技技巧。acrophobia 是恐高症相关名称，不宜把每次站高处小心都当成病理恐惧。acronym 与 acrostic 都取开头，但一个造缩略名称，一个把字藏进各行。',practice='An acrostic hides a word at the beginnings of its lines. 藏头文字在各行的开头藏着一个词：这里 acro- 对应的是行的端头，不是文字写在高山上。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w and w not in EX];ROOT['words']+=sorted(SH-set(ROOT['words']))
 assert set(ROOT['words'])=={e['word'] for e in W}|SH
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_133.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('acr:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
