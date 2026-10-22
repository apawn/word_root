# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_pasc_a import W as A
from author_batch200_root_pasc_b import W as B
W=A+B;kept=[x['word'] for x in W];r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0964')
EX={w:'本轮暂略较低频的牧养职位、农业专词、古语或艺术专词' for w in set(r['family'])|set(r['words']) if w not in kept}
ROOT=dict(id='C0964',meaning='喂养；放牧；进食',core='PASC / PAST = FEED',image='牧人把羊带到有草的地方：草地是 pasture，照看羊群的人是 pastor 的古老形象。喂养身体延伸到吃一餐，照料羊群又比喻关怀人群。',intro='拉丁 pascere 表示喂养、放牧，过去分词 pastus 留下 past-。核心词族可分食物与照料两路；原表中的 pastel 则主要来自 pasta 糊状物，本页保留为容易混淆的辨析。',forms='pasc- 与 past- 来自同一拉丁动词的不同词形，pasto 是意大利食物、一餐。antipasto 的 anti- 在这里表示餐前。pester 的牧人绳索远源通常以重建形式说明，不当作完整实录。',branches=[['照顾羊群与人群','pastor, pastoral'],['放牧用地','pasture'],['一餐与餐前菜','repast, antipasto'],['拴住、纠缠到烦扰','pester'],['相似拼写与另源辨析','pastel, pastille']],contrasts='pastoral 田园的或关怀性的，pastel 粉彩、浅色，pastille 小片糖或含片。antipasto 不等于反意面；pester 不应拆为 pest 加表示人的 -er。',practice='The pastoral scene showed sheep grazing in a pasture, painted in soft pastel colors.\n\n这幅田园画表现了羊群在牧草地吃草的情景，采用柔和的浅色调。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_pasc',[ROOT]),('words_pasc',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
