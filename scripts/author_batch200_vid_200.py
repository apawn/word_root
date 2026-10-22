# -*- coding: utf-8 -*-
"""C0223 cirr: a colour-based name, not a diagnosis from colour alone."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('cirrhosis','英 /səˈrəʊsɪs/；美 /səˈroʊsɪs/','肝硬化','肝脏里的正常组织被大量瘢痕组织替代，内部结构和工作能力受到破坏。先抓住这种持续损伤、瘢痕化的画面，再看名称的颜色来源。','19 世纪形成的现代拉丁医学名称，采用希腊 kirros／kirrhos“黄褐色、橙黄色”与 -osis 状态词尾，因一些患病肝脏的外观颜色而命名，再借入英语。它不是由表示卷曲的拉丁 cirrus 构成。',[['希腊 kirros／kirrhos','黄褐色、橙黄色'],['现代拉丁 cirrhosis','借某些患病肝脏的颜色形成医学名称'],['英语 cirrhosis','现代主要指肝脏广泛瘢痕化和结构破坏']],'词源只讲名字怎么来的，现代含义不只是“肝变黄”。多种长期肝脏损伤都可能导致肝硬化，不能看到 cirrhosis 就自动断定一个人的饮酒情况。它与一般肝炎或肝癌也不是同一个名称。','cirrhosis of the liver；liver cirrhosis；a diagnosis of cirrhosis。','hepatitis 是肝炎，cirrhosis 是肝硬化；liver cancer 是肝癌。它们可以有关联，但不能互相当作译词。',('The article explains how scar tissue changes the liver in cirrhosis.','文章解释了肝硬化中的瘢痕组织怎样改变肝脏。'),('The report lists cirrhosis among the patient’s diagnosed conditions.','报告把肝硬化列在这名患者已确诊的疾病中。'),sources=['https://www.etymonline.com/word/cirrhosis','https://www.oxfordlearnersdictionaries.com/definition/english/cirrhosis','https://www.merriam-webster.com/dictionary/cirrhosis','https://www.niddk.nih.gov/health-information/liver-disease/cirrhosis/definition-facts'])]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());names=[x['word'] for x in W]
ROOT=dict(id='C0223',meaning='黄褐色、橙黄色',core='本根接希腊表示黄褐色的词。cirrhosis 用颜色给病变命名，但现代理解应看肝脏的瘢痕和结构变化。',image='希腊黄褐色词 → 现代拉丁 cirrhosis → 英语肝硬化名称。',intro='这一页只保留日常医学阅读中常见的 cirrhosis。把命名时看见的颜色与现代疾病定义分开，就不容易被字面带偏。',forms='cirrhosis 是近代医学拉丁构词后进入英语，-osis 表状态。cirrh- 的拼写不能据此并到 cirrus“卷曲、卷云”一系。',branches=[['由颜色命名的医学词','cirrhosis']],contrasts='词源是颜色，现代概念是肝脏瘢痕化；不等于黄疸、一般肝炎或肝癌，也不能单凭病名推断病因。',practice='用一句话说清现代含义，再用另一句说明命名来源；不要把“黄褐色”本身当成完整定义。',words=names,exclude={})
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_200.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('cirr:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
