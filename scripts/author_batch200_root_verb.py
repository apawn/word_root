# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_verb_a import W as A
from author_batch200_root_verb_b import W as B
W=A+B
ROOT=dict(id='C1620',meaning='词；话语',core='VERB = WORD',image='想象把想法装进一个个词：用语言表达是 verbalize，逐字保留是 verbatim，词语塞得太多就可能 verbose。',intro='来自拉丁 verbum“词、话语”，在拉丁语中也用于语法上的动词。现代英语 verb 主要缩小为动词这一词类，但 verbal、verbose、proverb 仍保留更广的“词语”意象。别把整族都解释成动作。',forms='verbal 语言的、口头的；verbally 口头或用语言地；verbatim 逐字地。verbose 与 verbosity 分别经拉丁形容词和拉丁／法语名词路线进入，不能把后者画成较晚英语 verbose 的历史后代。adverb 的名称虽来自“加在动词上”，现代也可修饰形容词等。',branches=[['语法词类和功能','verb, adverb, adverbial'],['用词语表达','verbal, verbally, verbalize, verbalise, verbalization, nonverbal'],['措辞保留或过多','verbatim, verbose, verbosity'],['流传的话','proverb, proverbial']],contrasts='verbal 不总等于 oral；verbatim 是逐字原样，verbally 是表达方式。adverb 是词类，adverbial 是功能。verbose 在写作评价里常带啰嗦意味，在软件输出里可能只是表示细节更多。',practice='Please verbalize your idea clearly without repeating the entire report verbatim or becoming too verbose.\n\n请清楚说出你的想法，不必逐字重复整份报告，也别讲得太啰嗦。',words=[x['word'] for x in W]+['nonverbal'],exclude={})
if __name__=='__main__':
 for name,data in [('roots_verb',[ROOT]),('words_verb',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
