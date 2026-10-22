# -*- coding: utf-8 -*-
"""C1666 xi: a borrowed letter name."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('xi','/zaɪ/，也读 /ksaɪ/、/saɪ/','希腊字母 ξ／Ξ 的名称','看见公式里的 ξ，想知道怎么把这个符号念出来，xi 就是它的英文名称。它是希腊字母表第十四个字母。','整体借入希腊字母名称 xei／xi；不是英语 x 加后缀 -i。字母在希腊语中表示的声音，与英语说出这个字母名称的读音，是两回事。',[['希腊 xei／xi〔ξεῖ／ξῖ〕','字母 Ξ、ξ 的名称'],['英语 xi','借用希腊字母名，念读或指称这个符号']],'大写 Ξ 像三道横线，小写 ξ 则是一条弯曲的笔画。在数学、物理等文本里，它可以被作者指定为某个量的符号；xi 本身并不自带“随机变量”或某种固定物理量的意思。','the letter xi；lowercase xi；the symbol xi。复数可写 xis。本条列英语常见读音，不是现代希腊语的唯一读法。','xi 是 ξ，chi 是 χ，二者是不同字母。不要把中文人名或地名拼音 Xi 的读法套到希腊字母名上。',('The lecturer called the symbol xi and wrote ξ on the board.','讲师把这个符号念作 xi，并在黑板上写下 ξ。'),('In this formula, xi represents an unknown quantity.','在这个公式中，xi 代表一个未知量。'),sources=['https://www.merriam-webster.com/dictionary/xi','https://www.oxfordlearnersdictionaries.com/definition/english/xi'])]
ROOT=dict(id='C1666',meaning='希腊字母 xi',core='这是字母名，重点是把 xi 与 Ξ、ξ 对上。它不像“抓住、走、写”那样提供可自由延伸的动作意义。',image='希腊 Ξ／ξ 的名称 → 英语 xi → 读出公式或字母表中的这个符号。',intro='学习它，主要是为了看懂符号说明、听懂课堂或科学讨论。不要强拆出一串不存在的英语构词意义。',forms='xei、xi 是希腊字母名称的转写形式；英语采用 xi。',branches=[['字母名称','xi']],contrasts='xi 对应 ξ；chi 对应 χ。英语字母名读音与希腊语中的字母音值要分开。',practice='看到 ξ 时能说出 xi，再查看当前文章如何定义这个符号。',words=['xi'],exclude={})
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_236.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('xi: 1 new; 2 examples')
