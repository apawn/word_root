# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_kine_a import W as A
from author_batch200_root_kine_b import W as B
from author_batch200_root_kine_c import W as C
W=A+B+C;kept=[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0634')
EX={w:'本轮暂略更专门的药理、细胞和运动障碍术语' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0634',meaning='运动；使动起来',core='KINE / CINE = MOVE',image='静止照片一张张连续放映，画面仿佛动起来：这就是从“运动”理解 cinema 的入口。再看奔跑的人、滚动的球，kinetic 的运动义就容易抓住。',intro='希腊 kinein 是使运动，kinema 是运动，kinesis 也是运动名词。电影词族经法语 cinématographe、cinéma 进入英语，cine- 在英语里通常读 /sɪn/；科学词常保留 k 开头形式。',forms='kinet- 出现在 kinetic，kinemat- 出现在 kinematics 和 cinematography，kinesi- 出现在 kinesiology。不同形式来自相关希腊词干，不是把一个英语单词随意换几个字母。',branches=[['活动影像和影院','cinema, cinematic, cinematography, cinematographer, cineplex, cinemagoer'],['科学描述运动与变化','kinetic, kinetics, kinematics'],['人体运动和感觉','kinesiology, kinesthetic'],['幻想中的遥控物体','telekinesis, telekinetic']],contrasts='cinematography 是电影摄影，cinematographer 是从事它的人。kinematics 描述运动，kinetics 在不同学科里研究运动原因或变化速率。telekinesis 属于所谓意念移物的概念，不是普通无线遥控。',practice='The film’s cinematic style and kinetic action made it popular with young cinemagoers.\n\n影片的电影化风格和富有动感的动作场面让它受到年轻观众欢迎。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_kine',[ROOT]),('words_kine',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
