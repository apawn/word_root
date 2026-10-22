# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0714';TAG='252_meg';SHARED=['megaphone','megalomania','megalomaniac','megalopolis'];EXCLUDE_REASON='按用户当前范围暂略：专门病名、较旧计量名称或古典人名。'
M=[['希腊 mégas／megal-','大、巨大的'],['近代计量前缀 mega-','规定表示一百万倍']]
W=[E('megabyte','/ˈmeɡəbaɪt/','兆字节','用来量数据大小；先分清它数的是字节。','mega- 百万 + byte 字节。mega- 接希腊“大”的词族，但在现代计量名称中已有固定倍数，不只是泛泛地说“很大的字节”。',M+[['现代英语 mega- + byte → megabyte','数据容量单位，符号 MB']],'按十进制标准，1 MB 是1,000,000字节。旧用法和某些软件也把2的20次方字节叫 megabyte；精确区分时，后者写 mebibyte，符号 MiB。看文件大小，不能把 MB 的 B 与 bit 的小写 b 混掉。','a file of five megabytes；several megabytes of data；MB。用英文全称时，复数加 s。','megabyte 数字节；megabit 数比特。一个 byte 通常是8个 bit，所以同一个数字的 MB 和 Mb 不是同样的数据量。',('The compressed image is less than one megabyte.','压缩后的图片不到一兆字节。'),('The specification distinguishes megabytes from mebibytes.','规格说明区分了兆字节与二进制的 mebibyte。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/megabyte','https://physics.nist.gov/cuu/Units/binary.html']),
E('megawatt','英 /ˈmeɡəwɒt/；美 /ˈmeɡəwɑːt/','兆瓦','描述设备以多快的速率产生或使用能量。','mega- 百万 + watt 瓦特，后者是纪念 James Watt 的功率单位名。mega- 来自希腊“大”，这里精确表示一百万，不是可随意理解的夸张说法。',M+[['现代单位 watt 与 mega- 结合 → megawatt','一百万瓦的功率，符号 MW']],'1 MW 等于1,000,000 W。它常出现在电站、风机、用电负荷的报道里，表示功率。若要表达一段时间累计产生多少能量，还需要 megawatt-hour 等能量单位。','megawatts of power；a capacity of ten megawatts；MW。单位符号不加复数 s。','megawatt 是功率，megawatt-hour 是能量；可以把前者想成“流得多快”，后者想成“一段时间流了多少”。',('The generator has a rated output of two megawatts.','这台发电机的额定输出功率为两兆瓦。'),('The chart reports power in megawatts rather than total energy used.','图表以兆瓦报告功率，而不是累计用掉的能量。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/megawatt','https://www.nist.gov/pml/owm/metric-si-prefixes'])]
ROOT=dict(meaning='大；巨大',core='mega-/megal- 原来表示大，普通词里保留大小意象，单位词里则固定为一百万倍。',image='megaphone 把声音放大；megalopolis 是大城市区域；megawatt 中的 mega- 是精确倍数。',intro='先区分普通命名与计量规则。“大”可以是形象，也可以被标准化为数字；不能把所有带 mega- 的词都解释成一百万。',forms='希腊 mégas 在词形变化中有 megal-；英语常见 mega-、megalo-。单位前缀 mega- 的符号是大写 M。',branches=[['声音、城市与心理描述','megaphone、megalopolis、megalomania、megalomaniac'],['常用计量词','megabyte、megawatt']],contrasts='megalomania 中没有一百万这个算术含义；megabyte、megawatt 则需要按单位规则读。',practice='解释为什么 megaphone 不能译成“百万声音”，但 megawatt 可以准确换算成一百万瓦。',sources=['https://www.nist.gov/pml/owm/metric-si-prefixes','https://physics.nist.gov/cuu/Units/binary.html'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
