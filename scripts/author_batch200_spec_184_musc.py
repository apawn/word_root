# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
W=[E('mosquito','英 /məˈskiːtəʊ/，也读 /mɒˈskiːtəʊ/；美 /məˈskiːtoʊ/','蚊子','耳边嗡嗡飞、常让人想到叮咬的那种小昆虫。','借自西班牙语、葡萄牙语 mosquito，是 mosca“蝇”的小称形式，往前接拉丁 musca。原来是“小蝇”般的称呼，不是英语 moss、quit 或 toe 拼起来的。',[['拉丁 musca → 西班牙语、葡萄牙语 mosca','蝇'],['mosca 的小称 mosquito → 英语 mosquito','小蝇般的昆虫 → 蚊子']],'a mosquito bite 是蚊子叮的包；a mosquito net 是蚊帐。复数 mosquitoes 和 mosquitos 都使用。记住“小飞虫”这个来历就够了，不需要把每一段拼写都拆成英语词。','mosquito bites；a mosquito net；mosquitoes buzzing；mosquito repellent。','fly 是更泛的蝇类日常名称，mosquito 明确指蚊子。它和 muscle“肌肉”虽有相近字母，不能按 musc- 一概归成同一来源。',('A mosquito kept buzzing beside my ear.','一只蚊子一直在我耳边嗡嗡飞。'),('We slept under a mosquito net during the trip.','旅行期间，我们睡在蚊帐里。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/mosquito','https://en.wiktionary.org/wiki/mosquito'])]
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']=='C0775');c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']=='C0775');keep={'mosquito'};excluded={w:'按用户要求暂略：专门药理学或形态学术语；musciform 另有拉丁 muscus“苔藓”的同形来源，不与 musca 混为一条。'for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT=[dict(id='C0775',meaning='蝇、小飞虫',core='这里的 musc- 接拉丁 musca“蝇”，最值得掌握的后代是 mosquito。',image='mosca 后面接小称，像说“一只小飞虫”，进入英语后成了熟悉的蚊子。',intro='这页用一个日常高频词把词源讲明白：mosquito 经西班牙语、葡萄牙语的小称形式进入英语。原词根的专业药理学长尾暂略，先把这个常用词掌握扎实。',forms='拉丁 musca → 西班牙语、葡萄牙语 mosca → 小称 mosquito。英语里已经是完整借词，不需要按现代英语逐段硬拆。',branches=[['日常昆虫','mosquito']],contrasts='musca“蝇”、muscus“苔藓”以及 muscle 的来源不能仅按字母相似合并。小称解释的是名称来历，不是现代严格的动物分类。',practice='用 mosquito bite 和 mosquito net 各说一句日常生活中的话。',words=['mosquito'],exclude=excluded,sources=['https://www.oxfordlearnersdictionaries.com/definition/english/mosquito'])]
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT[0]['words'])-set(excluded)
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',ROOT),('words',W)]: (OUT/f'{k}_batch200_spec_184_musc.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C0775',len(W),'new',len(ROOT[0]['words']),'retained')
