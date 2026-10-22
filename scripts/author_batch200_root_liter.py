# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_liter_a import WA
from author_batch200_root_liter_b import WB
from author_batch200_root_liter_c import WC
from author_batch200_root_liter_d import WD
W=WA+WB+WC+WD
ROOT=dict(id='C0682',meaning='字母、文字；由文字连接到读写与学问',core='LITER / LETTER = LETTERS / WRITING',image='先想纸上的一个字母：字母排成词句，组成书信；人学会读写，进入书本和文学的世界。再把目光贴回每个字，就有“按字面理解”；把字涂到看不见，又能帮助记住“抹除”这条支线。',intro='源头是拉丁 littera，也写 litera，指字母；相关复数用法还可指书信、文字作品与学问。它更早的来源未能确定，不把希腊语或伊特鲁里亚语的假说写成已证实事实。英语一边保留较明显的 liter-，一边经古法语变成日常的 letter。',forms='liter- 常见于 literature、literal、literate；letter 是经法语传入的形式。literal、literary、literate 分别抓住“字面”“文学”“读写能力”。alliteration 的 al- 接 ad-，有同化；obliterate 通常联系 ob- 与 littera，但拉丁早期词义和“遗忘”的影响需要保留分寸。',branches=[['字母、书信与印刷','letter, letterhead, letterbox, lettering, newsletter, letterpress'],['文学与文字修养','literature, literary, nonliterary, literariness, literati, literator, lettered, unlettered'],['会不会读写','literate, literacy, illiterate, illiteracy, illiterately, preliterate, nonliterate'],['跨语言和媒介的能力','biliterate, biliteracy, multiliteracy, transliteracy'],['按字面理解','literal, literally, nonliteral, literalism, literalist, literalistic, literalize, literalization, literality'],['开头声音的呼应','alliteration, alliterate, alliterative, alliteratively'],['抹到无法辨认','obliterate, obliteration, obliterated, obliterating'],['记录、转写与字母数量','literation, literatim, transliterate, transliteration, uniliteral, biliteral, triliteral, quadriliteral, multiliteral']],contrasts='literary 不是 literal，也不是 literate；三者分别是文学、字面和读写素养。illiteracy 的英语历史早于 literacy，alliteration 也早于 alliterate，不能只按现代拼写反推先后。transliteration 转换书写系统，transliteracy 谈跨媒介交流。iterate“重复”、lateral“侧面的”与这一字母词族不是同一个来源。',practice='The newsletter reviews a literary festival and a new literacy programme. Its alliterative title is memorable, but one joke confused readers who took it literally.\n\n这份通讯回顾了一场文学节和一项新的读写教育计划。它押头韵的标题很容易记住，但其中一个笑话让按字面理解的读者感到困惑。',words=[x['word'] for x in W]+['transliterate','transliteration'])
if __name__=='__main__':
 assert len(W)==49 and len({x['word'] for x in W})==49
 for name,data in [('roots_liter',[ROOT]),('words_liter_a',WA),('words_liter_b',WB),('words_liter_c',WC),('words_liter_d',WD)]:
  Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),'individually authored words',sum(len(x['examples']) for x in W),'examples')
