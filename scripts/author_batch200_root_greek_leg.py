# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_greek_leg_a import WA
from author_batch200_root_greek_leg_b import WB
from author_batch200_root_greek_leg_c import WC
from author_batch200_root_greek_leg_d import WD
W=WA+WB+WC+WD
SHARED=['logic','dialogue','apologize','apology','apologetic','unapologetic','apologist']
ROOT=dict(id='C0658',meaning='说、话语、词语；把意思表达出来',core='LEG / LEX / LOG = SAY / WORD',image='脑中的意思，要靠词语说出来：词汇像可用的材料，交谈让不同声音来回回应，论证把理由组织起来。某些医学新词也借这些希腊语材料，描述阅读或表达中的困难。',intro='这一组接希腊 legein／lego“说”，以及 lexis“说法、词语”、logos“话语、说明、理由”等词。更早的印欧词族也包含收集、挑选的意义，但不要把“挑出词语排成句子”当成已被证明的历史现场。可以把它当记忆画面，具体词的进入路线仍逐一说明。',forms='lex- 与 log- 在希腊语词族内部相连，但不能看到相同字母就自动判同源。lexicon 是词书，lexical 是词汇的；dialect 从交谈、说话方式发展到方言；apology 词族从辩护发展出道歉义。近代 -lect 常从 dialect 等词中抽出，构成 idiolect、sociolect。拉丁 legere“读、收集”另有专页，不能把本页全部写成拉丁借词。',branches=[['词汇与词典','lexicon, lexis, lexical, lexically, lexeme, lexicalize, lexicalization, lexicography, lexicographer, lexicographic, lexicographical, lexicographically, lexicology, lexicologist, lexigram'],['群体与个人的说话方式','dialect, dialectal, dialectally, dialectology, dialectologist, idiolect, idiolectal, sociolect, sociolectal, ethnolect'],['对话、论证与预备讨论','dialogue, dialogic, dialogical, dialogism, dialectic, dialectical, dialectically, logic, logos, logion, prolegomenon, prolegomena'],['从辩护到歉意','apologia, apology, apologize, apologetic, apologetically, unapologetic, unapologetically, apologist'],['阅读、情绪与言语表达','dyslexia, dyslexic, dyslectic, dyslexically, alexia, alexithymia, alexithymic, dyslogia']],contrasts='dialect 方言不只是 accent 口音；dialectal 方言的与 dialectical 辩证的也不同。apologia 仍常指辩护，apology 日常常指道歉。lexicography 围绕词典，lexicology 围绕词汇系统。dyslexia、alexia、alexithymia 不是泛指“说不好话”的三个近义词。',practice='The lexicographer compared regional dialects while revising the dictionary. In the introduction, she explained that a dialect includes vocabulary and grammar, not just pronunciation.\n\n词典编纂者在修订词典时比较了不同地区的方言。她在引言里解释：方言包括词汇和语法，不只是发音。',words=[x['word'] for x in W]+SHARED)
if __name__=='__main__':
 assert len(W)==46 and len({x['word'] for x in W})==46
 for name,data in [('roots_greek_leg',[ROOT]),('words_greek_leg_a',WA),('words_greek_leg_b',WB),('words_greek_leg_c',WC),('words_greek_leg_d',WD)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),'individually authored words',sum(len(x['examples']) for x in W),'examples')
