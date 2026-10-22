# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_fend_a import WA
from author_batch200_root_fend_b import WB
REUSE={'offend','offender','offense'}
W=[x for x in WA+WB if x['word'] not in REUSE]
SHARED=['defend','defender','defended','offence','offensive','offended','offend','offender','offense']
ROOT=dict(id='C0413',meaning='击打、推撞；把攻击挡开',core='FEND / FENS = STRIKE / WARD OFF',image='先想象一次冲撞。把它往外挡，是 defend 的保护；向着别人撞过去，是 offend 的冒犯。挡住攻击的东西，可以变成防线，也可以变成一道 fence。',intro='拉丁语中的 -fendere 表示击打、推撞，主要保存在复合词里。de- 加上它形成 defendere“挡开、保护”；ob- 加上它形成 offendere“撞上、冲撞”，再延伸到伤害、触犯和冒犯。英语经过法语及拉丁语借词吸收了这两条词族，不是先有现代 fend，再随意加前缀造出全部单词。',forms='fend- 与 fens- 的交替联系到拉丁词干变化，defend／defense、offend／offense 因而能连起来。英语 fend 是 defend 的缩短，fence 是 defens／defence 的缩短。看到词形短，不代表它历史上一定更早。英美常见拼写差别是 defence／defense、offence／offense；defensive、offensive 通常都写 s。',branches=[['保护与自理','defend, defender, defended, fend'],['防御与辩护','defense, defence, defensive, defensively, defensible, indefensible, defenseless, defenceless'],['触犯与冒犯','offend, offender, offended, offense, offence, offensive, offensively, inoffensive'],['防护物与击剑','fence, fencer, fencing, fender']],contrasts='defensible 评价一个理由能否站住，defensive 描述一个人的防卫姿态。offense 在体育中还指进攻，不能处处译成冒犯。fend for oneself 是自己照顾自己，fend off 是挡开。fence 和 fender 都沿着防护发展，但一个常指围栏，另一个指具体防护部件。',practice='She gave a defensible explanation without becoming defensive. Later, she helped repair the fence that protected the garden.\n\n她给出了有理有据的解释，没有摆出戒备的姿态。后来，她帮忙修好了保护花园的围栏。',words=[x['word'] for x in W]+SHARED)
if __name__=='__main__':
 assert len(W)==15 and len({x['word'] for x in W})==15
 for name,data in [('roots_fend',[ROOT]),('words_fend_a',[x for x in WA if x['word'] not in REUSE]),('words_fend_b',WB)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),'authored words',sum(len(x['examples']) for x in W),'examples')
