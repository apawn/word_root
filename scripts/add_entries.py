import concurrent.futures,json,pathlib,requests,urllib.parse
P=pathlib.Path('.cache'); extra={
'C0129':['boreal'],'C0209':['chelonian'],'C0321':['dexiotropic'],'C0364':['Egyptology','Egyptian'],'C0410':['fellatio'],'C0439':['fennel'],'C0533':['hemerophile'],'C0789':['myzopod'],'C0827':['notogaean'],'C0885':['onager'],'C0995':['penteconter'],'C1029':['phrynoderma'],'C1048':['piriform'],'C1079':['plurimal'],'C1150':['psithurism'],'C1223':['rhigophobia'],'C1229':['rhynchocephalian','rhynchophore'],'C1299':['segetal'],'C1500':['tetartohedral'],'C1531':['trabecula'],'C1538':['trecentenary','trecentennial'],'C1540':['tredecillion'],'C1665':['xesis'],'C1676':['ziziphus']}
words=sorted({w for v in extra.values() for w in v})
def get(w):
 u='https://kaikki.org/dictionary/English/meaning/'+urllib.parse.quote(w[0])+'/'+urllib.parse.quote(w[:2])+'/'+urllib.parse.quote(w)+'.jsonl'
 try:
  r=requests.get(u,timeout=30)
  if r.status_code!=200:return w,[]
  ds=[json.loads(line) for line in r.text.splitlines()]
  return w,ds
 except:return w,[]
all_data=[];good={}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for w,ds in pool.map(get,words):
  ds=[d for d in ds if d.get('lang_code')=='en']
  print(w,len(ds),flush=True)
  if ds:all_data.extend(ds);good[w]=1
(P/'supplemental-raw.json').write_text(json.dumps(all_data,ensure_ascii=False))
(P/'extra-seeds.json').write_text(json.dumps({k:[w for w in v if w in good] for k,v in extra.items()},ensure_ascii=False))
with (P/'supplemental-lexicon.jsonl').open('w') as f:
 for d in all_data:
  senses=[s for s in d.get('senses',[]) if 'form_of' not in s and 'alt_of' not in s and s.get('glosses')]
  if not senses:continue
  for s in senses:s['examples']=[e for e in s.get('examples',[]) if e.get('type')=='example']
  f.write(json.dumps(dict(word=d['word'],pos=d['pos'],senses=senses,etymology_number=d.get('etymology_number'),etymology_text=d.get('etymology_text',''),etymology_templates=d.get('etymology_templates',[]),etymology_links=d.get('etymology_links',[]),sounds=[s for s in d.get('sounds',[]) if 'ipa'in s],translations=[t for t in d.get('translations',[]) if t.get('code') in ['cmn','zh']],derived=[]),ensure_ascii=False)+'\n')
