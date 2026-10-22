# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
W=[E('tapestry','/ˈtæpəstri/','挂毯；织锦；交织而成的整体','很多条不同颜色的线交织在一起，远看才显出一幅完整的画。','经古法语 tapisserie、tapis 等织物词传入，沿拉丁语形式追溯到希腊 tapes、词干 tapet- 厚织物、毯子。更远来源有争议，不把某一种推测当定论。',[['希腊 tapes、tapet- → 希腊、拉丁相关织物形式','厚织物；毯子'],['古法语 tapis → tapisserie → 英语 tapestry','毯、厚织物 → 带图案的装饰织物'],['英语比喻义','许多人物、经历或文化交织成的整体']],'a tapestry 常是织出图案、用来装饰的挂毯。a rich tapestry of memories 则把记忆比作不同色线：每段单看很小，织在一起成为丰富的人生画面。这个比喻强调多样而相互交织，不只是东西很多。','a woven tapestry；a wall tapestry；a rich tapestry of cultures；the tapestry of life。','工艺上 tapestry 主要是织出来的图案，embroidery 是在现成布料上绣图案。日常名称有时较宽，不能只凭名字判断制作技术。',('A large tapestry depicting a forest hung above the staircase.','楼梯上方挂着一幅描绘森林的大挂毯。'),('The memoir weaves family stories into a rich tapestry of city life.','这本回忆录把家庭故事编织成一幅丰富的城市生活图景。'),sources=['https://www.etymonline.com/word/tapestry','https://www.vam.ac.uk/articles/what-is-tapestry'])]
ROOT=dict(id='C1470',meaning='厚织物；毯子',core='TAPET = HEAVY FABRIC / CARPET',image='一根根线织成图案，许多故事也能交织成整体。',intro='希腊 tapes 的变格词干是 tapet-，表示厚织物、毯子。这条来源经过拉丁语和法语，留下今天很有画面感的 tapestry。',forms='tapestry 经法语 tapisserie 借入；英语中间的 t 不应硬解释成一个额外词根。希腊词更远的来源有不同解释，本页从可靠的织物词开始理解。',branches=[['实物挂毯与交织的比喻','tapestry']],contrasts='tapestry 不是 tape 胶带加词尾。它的比喻义强调多种材料共同组成整体，不是任意拼凑。',practice='Many small stories form the tapestry of a community.\n\n许多小故事交织成一个社区的生活图景。',words=['tapestry'],exclude={'tapis':'低频借词，本轮略过','tapetum':'解剖学细分术语，本轮略过'})
if __name__=='__main__':
 for name,data in [('roots_tapet',[ROOT]),('words_tapet',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
