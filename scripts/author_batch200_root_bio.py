# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_bio_a import WA
from author_batch200_root_bio_b import WB
from author_batch200_root_bio_c import WC
from author_batch200_root_bio_d import WD
from author_batch200_root_bio_e import WE
from author_batch200_root_bio_f import WF
from author_batch200_root_bio_g import WG
from author_batch200_root_bio_h import WH
from author_batch200_root_bio_i import WI
from author_batch200_root_bio_j import WJ
PARTS=dict(a=WA,b=WB,c=WC,d=WD,e=WE,f=WF,g=WG,h=WH,i=WI,j=WJ)
ALL_W=sum(PARTS.values(),[])
RARE=set('biographic biozone biochron biocoenosis ectosymbiosis symbiology symbiogenesis biopoiesis biotype biologism biomorph biomorphism biosemiotic aerobiology anhydrobiosis anoxybiosis biostasis chemobiosis cryobiosis cryptobiosis enterobiasis osmobiosis biosynthetically'.split())
REUSE={'biocentrism','biogenesis'}
W=[x for x in ALL_W if x['word'] not in RARE|REUSE]
SHARED=['biological','biology','autobiography','biodiversity','biotechnology','biologist','microbiology','autobiographical','biodegradable','biosynthesis','neurobiology','biologic','biomechanics','bioscience','biosecurity','bioenergy','biosynthetic','symbiont','astrobiology','biologically','biocentrism','biogenesis']
ROOT=dict(id='C0122',meaning='生命；生活；生物过程',core='BIO = LIFE',image='先想到一个活着的生命：它有一段经历，会生长、与别的生命相处，也会改变周围环境。bio- 可以把镜头拉近到细胞，也能拉远到整个地球。',intro='核心来自希腊 bios“生命、生活、生计”。古代它可以谈一个人的生活方式或一生，近代科学又用 bio- 指各种生命与生物过程。因此 biography 是写一个人的一生，biology 是研究生命，biodegradation 是生物参与分解。大量现代词是科学家用古典材料新造的，不是古希腊就已有今天的技术或学科。',forms='bio- 常出现在词首，-biotic、-biosis 等形式也在同一生命词族中。前面的限定成分会改变观察角度：micro- 小，aero- 空气，exo- 外部，sym- 共同。a- 在 abiotic 中是否定“生物的”；bi- 表示“二”的另一词根与本组不同。读新词时先抓住生命这一中心，再看它在谈过程、物质、关系、学科还是一种理念。',branches=[['一个人的一生','biography, biographical, biographic, biographer, biographically, biopic, autobiography, autobiographical'],['研究生命的不同角度','biology, biological, biologically, biologic, biologist, bioscience, biochemistry, biochemical, biochemist, biochem, microbiology, microbiologist, neurobiology, biophysics, biophysical, biophysicist, biomechanics, biomechanical, bioinformatics, biostatistics, biostatistician, biostatistical'],['生命与身体、医学','biomedical, biomedicine, biopsy, antibiotic, probiotic, prebiotic, bioavailability, bioactive, biotin, biopharmaceutical, biomarker, biofeedback, enterobiasis'],['生命在环境里组成什么','biosphere, biome, biota, biomass, biodiversity, biotic, abiotic, biotope, biocoenosis, biogeography, biogeochemical, biozone, biochron, biotype'],['共同生活与长期整合','symbiosis, symbiotic, symbiotically, symbiont, endosymbiont, endosymbiosis, ectosymbiosis, symbiology, symbiogenesis, microbiome, microbiota'],['借生命过程做事','biotechnology, biotech, biotechnological, bioengineering, bioreactor, biosensor, biometric, biometrics, bionics, bionic, biomolecule, biomolecular, biopolymer, biocompatible, biocompatibility, biofilm, biosynthesis, biosynthetic, biosynthetically'],['环境中的材料、能源与风险','biodegradable, biodegradation, biodegrade, bioenergy, biofuel, biodiesel, biogas, biohazard, biohazardous, biosafety, biosecurity, bioterrorism, biocide, biocidal, bioaccumulate, bioaccumulation, bioremediation'],['起源、现象与生命观念','biogenesis, abiogenesis, biopoiesis, biogenic, bioluminescence, bioluminescent, biorhythm, astrobiology, exobiology, aerobiology, bioethics, biophilia, biocentrism, biologism, biomorph, biomorphism, biosemiotic, biodynamic, macrobiotic'],['生命活动暂时慢下来','biostasis, cryptobiosis, anhydrobiosis, anoxybiosis, cryobiosis, chemobiosis, osmobiosis']],contrasts='bio- 只说明与生命有关，不自动表示健康、天然、安全或环保。biota 是生物成员，biotope 是生活环境；biodegradable 说明可被生物分解，仍要看条件和时间；bioluminescence 是生物化学发光，与荧光不同。biophilia、biocentrism 等还涉及假说或价值立场，不能把词根拆出来的字面意思当成科学证明。',practice='The biologist studied a pond’s biota and collected samples for biochemical analysis. Her biography later described how this small project led to a lifelong interest in biodiversity.\n\n这位生物学家研究一个池塘里的生物，并采样进行生物化学分析。后来，她的传记写到：这个小项目怎样使她一生都关注生物多样性。',words=[x['word'] for x in W]+SHARED)
ROOT['exclude']={w:'按用户最新要求，极少用于通用阅读的专门术语或罕用变体先略过；原稿已单独保存。' for w in sorted(RARE)}
ROOT['branches']=[[title,', '.join(w for w in words.split(', ') if w not in RARE)] for title,words in ROOT['branches'] if any(w not in RARE for w in words.split(', '))]
if __name__=='__main__':
 plan=json.loads(Path('.cache/batch200/bio_sections.json').read_text())
 assert len(ALL_W)==110 and len({x['word'] for x in ALL_W})==110
 for k,rows in PARTS.items():
  assert {x['word'] for x in rows}==set(plan[k]),k
  Path('.cache/batch200/drafts/root/words_bio_'+k+'.json').write_text(json.dumps([x for x in rows if x['word'] not in RARE|REUSE],ensure_ascii=False,indent=2))
 Path('.cache/batch200/deferred').mkdir(exist_ok=True)
 Path('.cache/batch200/deferred/root_bio_rare.json').write_text(json.dumps([x for x in ALL_W if x['word'] in RARE],ensure_ascii=False,indent=2))
 Path('.cache/batch200/drafts/root/roots_bio.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2))
 print(len(W),'individually authored words',sum(len(x['examples']) for x in W),'examples',len(ROOT['words']),'root references')
