# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
W=[
E('siesta','/siˈestə/','午睡；午间休息','一天走到最热的中段，先停下来歇一会儿。','借自西班牙语 siesta，来自拉丁 sexta hora 第六个小时：按从日出起算的日间时刻，第六小时约在中午。',[['拉丁 sexta hora','从日出起算的第六小时，约为中午'],['西班牙语 siesta → 英语 siesta','午间休息或午睡']],'take a siesta 是午休、睡个午觉。名称里的六来自古代计时方式，不是说午睡要睡六小时，也不是现代钟表的下午六点。这个词常带西班牙语地区或炎热午间生活的联想，但英语也能用于其他地方。','take a siesta；an afternoon siesta；close for a siesta。','nap 是任何时间的小睡；siesta 更专指午间或午后休息。可以把 nap 当上位概念，siesta 当带时间和文化色彩的一种。',('After lunch, they took a short siesta.','午饭后，他们睡了一会儿午觉。'),('The village grew quiet during the afternoon siesta.','午后休息时，村子安静了下来。'),sources=['https://www.etymonline.com/word/siesta','https://en.wiktionary.org/wiki/siesta#English']),
]
ROOT=dict(id='C1333',meaning='六；第六；六分之一',core='SEXT = SIX / SIXTH',image='六既能数人数，也能分圆周，还能标记从日出起算的时刻。',intro='拉丁 sex 是六，sextus 是第六，sextans 是六分之一。英语 sextet、sextant 和 siesta 分别保留了人数、分数和时刻的不同联系。',forms='sex／sextus → 音乐词 sextet；sextans → sextant；sexta hora → 西班牙语 siesta → 英语 siesta。sextet 的音乐表达与意大利语词形也有历史联系。',branches=[['六人或六件乐器','sextet'],['六分之一圆弧','sextant'],['第六小时的休息','siesta']],contrasts='这里的 sex 是拉丁数字六，不是英语的性。siesta 的六也不表示睡眠时长，而是古代一天中的时刻。',practice='After a short siesta, the sailors practised using a sextant.\n\n短暂午休后，水手们练习使用六分仪。',words=[x['word'] for x in W]+['sextet','sextant'],exclude={w:'较冷门的诗律、历法、数学或专门术语，本轮略过。' for w in ['sext','sextile','sestina','sestet','bissextile','sextillion','sixte','semisextile','sextain','sextan','sextans','sextary','sextic','bissextus']})
if __name__=='__main__':
 for name,data in [('roots_sext',[ROOT]),('words_sext',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
