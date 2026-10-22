# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
W=[E('psychoanalytic','英 /ˌsaɪkəʊˌænəˈlɪtɪk/；美 /ˌsaɪkoʊˌænəˈlɪtɪk/','精神分析的','把说出口的感受与未被意识到的冲突联系起来理解，属于精神分析的那套思路。','现代可拆 psycho-“心理、精神” + analytic“分析的”，也与 psychoanalysis 的形容词形式对应。analytic 的远源是希腊 ana- + lýein“解开”；“解开心结”是理解联想，不是希腊人已发明现代精神分析。',[['两组希腊材料：psykhḗ；ana- + lýein → analytikós','心灵；解开、分析'],['中世纪拉丁 analyticus → 英语 analytic；psycho- 作心理组合形式','分析的；心理的'],['精神分析术语背景下：psycho- + analytic → psychoanalytic','与精神分析理论、方法相关的']],'a psychoanalytic interpretation 常关注无意识、冲突和早期经历等概念，也用于文学评论。它是特定分析传统，不是“凡是认真分析人的心理都算”。对人物作这样的解读，也不等于完成临床诊断。','a psychoanalytic approach；psychoanalytic theory；a psychoanalytic interpretation。','psychological 范围更广，凡与心理有关都可能用；psychoanalytic 限定精神分析这一理论或方法方向。',('The critic offers a psychoanalytic interpretation of the character’s recurring dreams.','评论者从精神分析角度解读人物反复出现的梦。'),('The course compares psychoanalytic theory with other approaches to the mind.','课程把精神分析理论与其他研究心灵的方法作比较。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/psychoanalytic','https://www.etymonline.com/word/psychoanalytic','https://www.etymonline.com/word/analytic','https://en.wiktionary.org/wiki/psychoanalytic#English'])]
(OUT/'words_batch200_spec_shared_psychoanalytic.json').write_text(json.dumps(W,ensure_ascii=False,indent=2)+'\n')
print('psychoanalytic',len(W),'word',sum(len(x['examples']) for x in W),'examples')
