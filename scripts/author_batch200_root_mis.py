# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_mis_a import WA
from author_batch200_root_mis_b import WB
from author_batch200_root_mis_c import WC
from author_batch200_root_mis_d import WD
from author_batch200_root_mis_e import WE
from author_batch200_root_mis_f import WF
W=WA+WB+WC+WD+WE+WF
SHARED='misuse misinformation misconception mismanagement misdirection misalignment misplace misprint misperception misdirect misconstrue misophonia'.split()
ROOT=dict(id='C0748',meaning='同形要分源：错误、不当；另一条希腊来源表示厌恶',core='MIS = WRONG；MISO = HATRED（不同来源）',image='两块拼写相似的路牌，通向不同地方：misread 是读错了；misogyny 是厌恶女性。misadventure 还保留古法语“坏、不顺”的另一条历史。',intro='这一页把相似拼写放在一起辨清，不把它们冒充同一个古代词根。① 古英语已有的日耳曼 mis- 表示错误、不当，如 mislead、misread。② 古法语 mes- 也表示坏、不顺，常联系拉丁 minus 的罗曼语发展，并与日耳曼形式发生混合，misadventure 属于这条借入路线。③ 希腊 misos、misein 表示厌恶，形成 miso-／mis-，见 misogyny、misanthrope。原表把它们全放到希腊“厌恶”下面，这里明确纠正。',forms='mis- 可以接英语或借来的词基：mistreat 的 treat 来自法语，不等于整个前缀也来自法语；misdiagnosis 的 diagnosis 来自希腊，也不能把 mis- 解释成“厌恶”。misspell 与 misshapen 的双 s 是前后成分相接。misread 的过去式拼写不变但读 /red/；mislead 的过去式是 misled。',branches=[['误认、误解与误导：日耳曼前缀为主','mistake, mistaken, misunderstand, mislead, misread, misinterpret, misrepresent'],['行为、匹配和结果不对','misconduct, mismatch, misbehave, mistreat, misfit, misfire'],['不幸与意外：要分别看借入路线','misfortune, mishap, misadventure, miscarriage'],['希腊“厌恶”的独立来源','misogyny, misandry, misanthropy, misophonia']],contrasts='misunderstand 是理解者弄错；misrepresent 是呈现出来的内容失真；mislead 是把别人带向错误认识。misfortune 是不幸，并不自动归责于当事人。希腊 miso- 与这些常用“错误”词的前缀不同源。',practice='I misread the date, misunderstood the instructions, and mistakenly blamed the software. A short conversation cleared up the misunderstanding.\n\n我看错了日期，误解了说明，还错怪了软件。一次简短的交谈澄清了误会。',words=[w['word'] for w in W]+SHARED,exclude={'mistry':'来自南亚语言的工匠称呼，不是这几条 mis- 来源的后代。',**{w:'按用户要求暂缓非常低频或专门的派生词。' for w in ['misocainea','misogamist','misogamy','misoneism','misotheism']}})
if __name__=='__main__':
 assert len(W)==53 and len({w['word'] for w in W})==53,(len(W),len({w['word'] for w in W}))
 t=Path('.cache/batch200/drafts/root')
 for suffix,ws in [('a',WA),('b',WB),('c',WC),('d',WD),('e',WE),('f',WF)]: (t/('words_mis_'+suffix+'.json')).write_text(json.dumps(ws,ensure_ascii=False,indent=2))
 (t/'roots_mis.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2))
 rows=[]
 for w in W:
  if w['word'] in ['misbehaviour','misdemeanour']:rows.append(dict(word=w['word'],pos='noun',ipa=w['ipa'],gloss='British spelling of '+{'misbehaviour':'misbehavior','misdemeanour':'misdemeanor'}[w['word']]+'.',meaning_zh=w['meaning'],etymology_text='Spelling with -our corresponding to the form in -or; mis- has negative or pejorative meaning here, not Greek hatred.',sources=w['sources']))
 Path('.cache/batch200/root_mis_supplement_request.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
 print(len(W),'words',sum(len(w['examples']) for w in W),'examples',len(ROOT['words']),'references')
