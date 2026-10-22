# -*- coding: utf-8 -*-
"""C1156 pter: a wing, in aircraft and familiar fossil terminology."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('pterosaur','美 /ˈterəˌsɔːr/','翼龙','史前天空里会主动飞行的一类爬行动物，翅膀的翼膜主要靠特别延长的第四指撑起。','来自近代拉丁分类名称 Pterosauria，以希腊 pteron“翼”+ sauros“蜥蜴、爬行动物”构成。现代可拆 ptero- + -saur；这是近代命名，不是古希腊人对化石已有的英语分类。',[['希腊 pteron + sauros','翼 + 蜥蜴、爬行动物'],['近代拉丁 Pterosauria','翼龙类的分类名称'],['英语 pterosaur','这一已灭绝类群的成员']],'pterosaur 是一个大类的名称，不是一种长相固定的动物。不同翼龙在大小、牙齿和食性上有差别；它们能主动飞行，也会在地面活动，不能把名字里的“翼”理解成只能待在空中。','a pterosaur fossil；a pterosaur skeleton；pterosaur wings；different species of pterosaur。','pterodactyl 在口语中也会泛指翼龙，严格属名 Pterodactylus 则只是其中一属。翼龙与恐龙是近亲的不同类群；鸟类才处在恐龙的演化支系内。',('The display compares the wing of a pterosaur with that of a bird.','展板比较了翼龙的翅膀与鸟翼的结构。'),('The fossil helped researchers reconstruct the proportions of this pterosaur.','这块化石帮助研究人员复原了这种翼龙的身体比例。'),sources=['https://www.merriam-webster.com/dictionary/pterosaur','https://en.wiktionary.org/wiki/pterosaur','https://www.nhm.ac.uk/discover/the-truth-about-pterosaurs.html'])]
EX={
'pterostigma':'昆虫翅痣专业解剖词，本轮暂略。','apterous':'昆虫无翅状态等专业形容词，本轮暂略。','apterygote':'无翅昆虫分类名，本轮暂略。','brachypterous':'昆虫短翅形态专业词，本轮暂略。','brachyptery':'短翅性专业术语，本轮暂略。','chiropterologist':'蝙蝠研究专家的较冷称谓，本轮暂略。','exopterygote':'外翅昆虫分类词，本轮暂略。','hemipterous':'半翅目相关专业形容词，本轮暂略。','heteropterous':'异翅类相关专业形容词，本轮暂略。','homopterous':'旧昆虫分类相关形容词，本轮暂略。','peripteros':'古典建筑周柱式专门名词，本轮暂略。','pteron':'建筑柱廊等专业名词，本轮暂略；希腊原词在词根说明保留。','pteropod':'翼足类动物专业词，本轮暂略。','pterygote':'有翅昆虫专业分类词，本轮暂略。','tetrapterous':'四翅形态专业词，本轮暂略。','archaeopteryx':'始祖鸟专门化石名称，本轮优先保留翼龙通称。','Chiroptera':'蝙蝠的拉丁分类目名，本轮暂略。','Endopterygota':'昆虫类群拉丁分类名称，本轮暂略。','Neoptera':'昆虫类群拉丁分类名称，本轮暂略。'}
ROOT=dict(id='C1156',meaning='翼、羽毛',core='希腊 pteron 是翼、羽毛。记忆时先看伸展开来支撑飞行的部分：动物可以有翼，机器也可以借“翼”来命名。',image='旋转与翼 → helicopter；翼与手指 → pterodactyl；翼与爬行动物 → pterosaur。',intro='这一根最熟悉的词藏在 helicopter 后半段。它原本是 helico- 加 pter；后来英语才把 copter 当成可单独使用的部分。动物名里的 ptero- 则更容易看出翼的意思。',forms='pter-／ptero- 来自 pteron；词首 pt- 在英语 pterosaur、pterodactyl 中通常不读 p，单词从 /t/ 音开始。helicopter 中的 p 则读出来。',branches=[['机器的旋转之翼','helicopter'],['史前动物的翼','pterosaur, pterodactyl']],contrasts='helicopter 的历史切分不是 heli + copter。pterosaur 是翼龙这一类，Pterodactylus 是其中一属；“会飞”不足以把某个史前动物归成恐龙。',practice='A helicopter uses rotating wings; a pterosaur had wings supported by long fingers. 机器和动物的结构不同，pter- 都把注意力引向翼。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w and w not in EX]
 assert {e['word'] for e in W}<=set(ROOT['words'])
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_102.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('pter:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
