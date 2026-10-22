# -*- coding: utf-8 -*-
"""Join manually authored gen/gon sections and declare the root lesson."""
import json
from pathlib import Path
from author_batch200_root_greekgen_a import W as WA
from author_batch200_root_greekgen_b import W as WB
from author_batch200_root_greekgen_c import W as WC
W=WA+WB+WC
ROOT=dict(id='C0474',meaning='出生、产生；世代、种类；现代基因支线',core='GEN / GON = COME INTO BEING',image='先想一件东西从无到有，再追问：由什么产生、从哪里产生、属于哪一支。这能接起 genesis 的起源、hydrogen 的生成水、endogenous 的内部产生，以及 gene 的遗传信息。',intro='希腊 gígnesthai 是产生、出生，génos 是出身或种类，génesis 是产生过程；gonḗ 走生殖、后代一支。它与拉丁 gignere、genus 的词族有更远同源关系，但不是所有英语词都先经过拉丁语。gene 是近代科学新词；许多含 gen 的词比它早，讲的是产生或种类，并不讲基因。',forms='gen- / gon- 的元音变化来自相关希腊词形。-gen 可指引起某物的因子，-genesis 是形成过程，-genic / -genous 常作形容词。gene 通常读 /dʒiːn/，genetic 读 /dʒəˈnetɪk/；gonad 的 g 则读 /ɡ/。表示角的希腊 gōnía 是另一词根，不能把 polygon 直接接到出生这一支。',branches=[['从起源到家族谱系','genesis, genealogy, genealogical, genealogist, Eugene, epigone'],['遗传信息与整套基因组','gene, genetic, genetically, genetics, geneticist, genome, genomic, genomics, genotype, monogenic, polygenic, pseudogene, oncogene, genet'],['同类与不同类','homogeneous, heterogeneous, homogeneity, heterogeneity, homogenize, inhomogeneous, homogenesis, homogenetic, polygenous'],['引起什么、生成什么','hydrogen, hydrogenate, hydrogenation, dehydrogenase, hydroxyl, antigen, antigenic, pathogen, allergen, allergenic, carcinogen, carcinogenic, mutagen, mutagenic, mutagenesis'],['内外来源及发育','endogenous, exogenous, autogenous, biogenesis, epigenesis, epigenetic, epigenetics, epigenome, phylogenetic, cytogenetic, anagenesis, autogenesis, endogen, progenesis'],['生殖与相关历史词','gonad, gonadal, hypogonadism, spermatogenesis, oogenesis, gametogenesis, erogenous, genophobia, eugenics, eugenic, dysgenic, genocide'],['地下、地表与生成不足','epigene, hypogene, hypogenic, hypogenous, hypogenesis, paragenesis']],contrasts='genetic 不一定只指现代基因，旧义还能指共同起源。homogeneous 是组成均一，genetically identical 才是遗传上相同。antigen 是免疫识别的目标，pathogen 是致病因子。hypogene 是地质的地下形成，hypogenesis 是发育不足。genet 的麝猫义另源，不可用基因硬拆。',practice='The researchers compared the genomes of two plants and traced the genesis of a new variety. They found a heterogeneous population with several genotypes.\n\n研究人员比较了两种植物的基因组，并追溯一个新品种的形成过程。他们发现这个群体内部并不一致，包含几种基因型。',words=[w['word'] for w in W]+['genocide','genealogy','allergen'])
if __name__=='__main__':
 assert len(W)==len({w['word'] for w in W})==73
 Path('.cache/batch200/drafts/root/roots_greekgen.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2))
 for suffix,words in [('a',WA),('b',WB),('c',WC)]:Path('.cache/batch200/drafts/root/words_greekgen_'+suffix+'.json').write_text(json.dumps(words,ensure_ascii=False,indent=2))
 print('1 root,',len(W),'individually authored words,',sum(len(w['examples']) for w in W),'examples')
