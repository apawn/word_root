# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0203';TAG='316_cerat';SHARED=[];EXCLUDE_REASON='暂略冷门分类学与细分术语，保留角质蛋白和常见恐龙名称。'
W=[E('keratin','/ˈkerətɪn/；美也读 /ˈkerətən/','角蛋白','构成头发、指甲等组织的重要蛋白质。','借德语 Keratin；取希腊 kéras〔角〕的词干 kerat-，加德语物质名称词尾 -in。现代可以认出 kerat-＋-in，但英语词本身是借入的。',[['希腊 kéras，词干 kerat-','角'],['德语 Keratin','以角的材料命名蛋白质'],['英语 keratin','角蛋白']],'先想动物角外面的坚韧材料，再联系自己的头发和指甲，就容易记住。keratin 是一组结构蛋白的名称，不是说头发就是一支缩小的角，也不专指某种护发产品。','keratin proteins；keratin in hair；a keratin treatment〔美容项目名称〕。','keratin 是材料名称；hair、nails 则是含有这种材料的具体组织。',('Hair and nails contain keratin.','头发和指甲含有角蛋白。'),('The lesson describes how keratin helps support epithelial cells.','这节课介绍角蛋白如何帮助支撑上皮细胞。'),sources=['https://www.merriam-webster.com/dictionary/keratin','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/keratin']),
E('triceratops','英 /traɪˈserətɒps/；美 /traɪˈserətɑːps/','三角龙','脸部带有三只角的那种著名恐龙。','来自新拉丁属名 Triceratops：tri-〔三〕＋希腊 kerat-〔角〕＋ ōps〔脸〕。属名首字母大写，日常把它当动物普通名称时常小写。',[['希腊三、角、脸的材料','tri-；kerat-；ōps 并列'],['新拉丁属名 Triceratops','三角之脸'],['英语 triceratops','三角龙的普通名称']],'两眼上方各有一只长角，鼻部还有一只较小的角，名字直接抓住这个醒目的外形。末尾 -ops 是“脸”的材料，不是英语复数 -s；一只也叫 a triceratops。','a triceratops skull；a model triceratops；复数 triceratops 或 triceratopses。','tri- 数的是三只角，不是三颗头；三角龙是植食性恐龙，角多不等于肉食。',('The child counted the three horns on the triceratops model.','孩子数了数三角龙模型上的三只角。'),('A large triceratops skull stood near the museum entrance.','博物馆入口附近陈列着一个大型三角龙头骨。'),sources=['https://www.merriam-webster.com/dictionary/triceratops','https://www.nhm.ac.uk/discover/dino-directory/triceratops.html'])]
ROOT=dict(meaning='角；角质',core='cerat-／kerat- 的本来画面是一只动物的角。',image='一条线看角的形状，另一条线看构成角质组织的材料。',intro='希腊 kéras 的词干是 kerat-。英语借科学词时，常见 kerat- 与 cerat- 两种拼写；triceratops 保留角的外形，keratin 转向相关蛋白质。',forms='kerat- 如 keratin；cerat- 如 triceratops。拼写的 c 与 k 是借词形式差异，不表示两个互相派生的英语词根。',branches=[['角的材料','keratin'],['角的外形','triceratops']],contrasts='不要把 keratin 简单理解成“角本身”；它是蛋白质，头发和指甲也含有。',practice='把 triceratops 拆成“三＋角＋脸”，再用自己的头发和指甲记住 keratin。',sources=['https://www.merriam-webster.com/dictionary/keratin','https://www.merriam-webster.com/dictionary/triceratops'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
