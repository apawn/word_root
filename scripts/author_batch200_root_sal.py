# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_sal_a import W as A
from author_batch200_root_sal_b import W as B
from author_batch200_root_sal_c import W as C
from author_batch200_root_sal_d import W as D
W=A+B+C+D;kept=[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C1247')
EX={w:'本轮暂略更专门或低频的盐相关术语' for w in set(r['family'])|set(r['words']) if w not in kept}
ROOT=dict(id='C1247',meaning='盐；加盐；调味',core='SAL = SALT',image='先想一小撮盐：撒进水里形成盐水，拌进菜里成为调味。调味品能让食物有滋味，人说话也能带一点辛辣劲。',intro='拉丁 sal 表示盐，属格 salis；salsus 是加过盐的。它留下 saline 一类盐分词，也经法语、意大利语、西班牙语进入许多食物名称。salary 与盐词族有关系，但“士兵直接拿盐领工资”的故事不能当作定论。',forms='sal-、salin-、sals- 保留盐的痕迹；sauce 经法语后拼写变化较大。salt 则承自古英语 sealt，与拉丁 sal 有更早的同源关系，不是从法语或拉丁语借来的词。sassy、sass 是 sauce 的口语和比喻支线。',branches=[['薪酬与盐的历史联系','salary, salaried'],['盐分多少与去盐','saline, salinity, salinization, desalination, desalinate'],['餐桌上的调味与食物','salad, sauce, salsa, salami, sausage'],['从酱汁容器到厨房器具','saucer, saucepan'],['话里带辣味','saucy, sassy, sass'],['英语本族的盐词','salt, salty, salted, unsalted, saltwater']],contrasts='salinity 是盐分状态，salinization 是积累过程，desalination 是去盐过程。salted 说加过盐，salty 说尝起来咸；salary 与盐的远源联系不能代替其现代薪酬含义。',practice='The cook used unsalted butter, tasted the sauce, and added a pinch of salt.\n\n厨师用了无盐黄油，尝了尝酱汁，然后加了一小撮盐。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_sal',[ROOT]),('words_sal',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 missing={'salinization','desalinate'}
 meta=[dict(word=w['word'],pos='noun' if w['word']=='salinization' else 'verb',ipa=w['ipa'],gloss='The accumulation of salts in soil or water.' if w['word']=='salinization' else 'To remove dissolved salts from water.',meaning_zh=w['meaning'],etymology_text=w['split'],sources=w['sources']) for w in W if w['word'] in missing]
 Path('.cache/batch200/root_sal_supplement_request.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
