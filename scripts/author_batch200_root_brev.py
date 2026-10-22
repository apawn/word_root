# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_brev_a import W as A
from author_batch200_root_brev_b import W as B
W=A+B
ROOT=dict(id='C0138',meaning='短；简要说明、缩写和删节',core='BREV = SHORT',image='把一条长绳剪短：时间可以缩短，表达可以精简，长篇作品可以删节；简要文书又连接到交代情况。',intro='拉丁 brevis 表示短。brief 经借入路线改变了音形，brevity 保留更明显的 brev-。abbreviate 与 abridge 都联系到拉丁 abbreviare“使短”，只是前者较接近拉丁形式，后者经历了法语的变化。',forms='brief 可以是形容词、文书名词和说明情况的动词；briefing 由动词形成。debrief 常指任务后的信息回收。abbreviation 与 abbreviate 历史上分别形成或借入，不能用现代拆分倒推出先后。',branches=[['时间和表达简短','brief, briefly, brevity, briefer'],['文书与情况说明','briefcase, briefing, briefed, debrief, debriefing'],['词语缩写与作品删节','abbreviate, abbreviation, abbreviated, abridge, abridged, unabridged']],contrasts='briefing 常交代情况，debriefing 常事后回顾。abbreviation 常是名称的短形式，abridged edition 是内容删节版。briefcase 的 brief 是文件，不是说包很短。',practice='Keep the briefing brief, but leave enough time for a proper debriefing afterwards.\n\n情况说明尽量简短，但也要给事后的认真复盘留够时间。',words=[w['word'] for w in W],exclude={'brevicaudate':'描述短尾的专门形态词，暂略'})
if __name__=='__main__':
 for name,data in [('roots_brev',[ROOT]),('words_brev_a',A),('words_brev_b',B)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 x=next(w for w in W if w['word']=='abridge');Path('.cache/batch200/root_brev_supplement_request.json').write_text(json.dumps([dict(word=x['word'],pos='verb',ipa=x['ipa'],gloss='To shorten a text by omitting parts; to curtail.',meaning_zh=x['meaning'],etymology_text='From Middle English and Old French abregier or abrigier, from Latin abbreviare, from brevis (short). Doublet of abbreviate.',sources=x['sources'])],ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
