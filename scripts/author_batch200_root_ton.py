# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_ton_a import W as A
from author_batch200_root_ton_b import W as B
from author_batch200_root_ton_c import W as C
W=A+B+C
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C1486');keep={w['word'] for w in W};EX={w:'医学、语言学或音乐中的低优先级专业词，本轮暂略' for w in r['family'] if w not in keep and '-' not in w}
ROOT=dict(id='C1486',meaning='拉伸、张紧；音调及相关比喻',core='TEN / TON = STRETCH / TONE',image='拉紧琴弦，声音就发生变化；这是理解拉伸到音调的一座桥。语气、单调、音乐结构继续沿声音支线走，斜边和肌肉僵直则各自回到拉伸、紧绷的源头。',intro='希腊 teinein 是拉伸，tonos 原有张紧、琴弦张力等意思，发展出音调。tone 讲声音特性、语气和色调，tune 常讲曲调与调准。这里把实用音乐、沟通和数学词汇讲清，密集的专门医学派生暂不扩写。',forms='tone 经拉丁 tonus 与法语 ton 一路借入；tune 是早期同族变体，元音变化原因不宜编造。mono- 加音调成分表示单一，penta- 表五。hypotenuse 直接走 teinein 的伸展支线；tetanus 走紧绷、僵直支线。',branches=[['声音、曲调与调整','tone, tune, tuning, tuner, tunable, tuneful, toned, ringtone'],['整体调子与隐含意味','tonal, tonality, overtone, undertone'],['单调感与单调性质','monotone, monotonous, monotony, monotonic'],['音乐里的结构','tonic, pentatonic, diatonic'],['拉伸与紧绷的其他支线','hypotenuse, tetanus']],contrasts='tone 是声音特性或语气，tune 是曲调或调准。monotonous 多指乏味，monotonic 是技术中的单调性质。overtone 和 undertone 都能表示言外之意，不能按 over 与 under 强行做绝对区分。',practice='A cheerful tune helped break the monotony of the repetitive task.\n\n一段欢快的曲调帮助打破了重复工作的单调。',words=[w['word'] for w in W],exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_ton',[ROOT]),('words_ton',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
