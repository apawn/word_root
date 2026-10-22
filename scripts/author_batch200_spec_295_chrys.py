# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0217';TAG='295_chrys';SHARED=['chrysanthemum'];EXCLUDE_REASON='按当前阅读范围暂略少见宝石名、特殊材料艺术术语及罕见恐惧症名称。'
W=[E('chrysalis','/ˈkrɪsəlɪs/','蝶蛹；化蝶前的蛹期','看上去静静悬着，里面却正发生从幼虫到蝴蝶的改变。','英语借自拉丁 chrysalis／chrysallis，接希腊 khrysallis。通常联系 khrysos“金”，与某些蛹的金属光泽或金色斑点相应；古词内部构形也有不同分析，不把每一段都硬拆成确定后缀。',[['希腊 khrysallis〔蛹〕','通常联系 khrysos“金”，具体旧构形并非完全确定'],['拉丁 chrysallis／chrysalis → 英语 chrysalis','蝴蝶的蛹及这个发育阶段']],'chrysalis 指蝴蝶本身所处的蛹阶段或蛹体，不是额外包在外面的丝袋。可以想成暂时不飞不爬的“改造阶段”，但它仍是活着的昆虫；也并非所有蝶蛹都呈金色。','a butterfly chrysalis；emerge from a chrysalis；a chrysalis attached to a twig。','pupa 是更广的“蛹”；chrysalis 通常专指蝶蛹；cocoon 是保护蛹的丝质茧壳。蛹和包住它的茧不是同一层东西。',('A green chrysalis hung beneath the twig.','一只绿色蝶蛹悬在细枝下方。'),('The children watched a butterfly emerge from its chrysalis.','孩子们看着一只蝴蝶从蛹中羽化出来。'),sources=['https://www.etymonline.com/word/chrysalis','https://en.wiktionary.org/wiki/chrysalis#English','https://www.floridamuseum.ufl.edu/discover-butterflies/faq/'])]
ROOT=dict(meaning='金；金色',core='chrys- 的基本颜色画面是黄金的亮色。',image='花瓣的金黄、蝶蛹上的金色斑点，都曾让命名者想到黄金。',intro='希腊 khrysos 表示黄金。chrysanthemum 的旧名是“金花”；chrysalis 通常也联系金色，但古词具体结构仍有不同分析。名称保留旧观察，现代所有个体不必都是金色。',forms='chrys-、chryso- 是常见形式；chrysanthemum 的后半接花的名称，chrysalis 是整个古词经拉丁传入。',branches=[['植物名称','chrysanthemum'],['蝶的发育阶段','chrysalis']],contrasts='白菊、紫菊同样可叫 chrysanthemum；蝶蛹也不都发金光。不能用词源颜色替代现代定义。',practice='分别用 chrysanthemum 和 chrysalis 描写花园里的植物与昆虫，并说明为什么两者都可能让古人想到金色。',sources=['https://www.etymonline.com/word/chrysalis','https://www.etymonline.com/word/chrysanthemum'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
