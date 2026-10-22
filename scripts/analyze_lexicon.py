import json,re,collections,pathlib
D=collections.defaultdict(list)
for line in open('.cache/lexicon.jsonl'):
 try:d=json.loads(line)
 except:continue
 D[d['word']].append(d)
print('Words',len(D),'entries',sum(map(len,D.values())))
T=collections.Counter(t['name'] for ds in D.values() for d in ds for t in d['etymology_templates']);print('templates',T.most_common(35))
for w in ['happy','unhappy','happiness','receive','reception','biology','bio-','-ness','hand','coffee','write','fraternity','spectator']:
 ds=D.get(w,[]); print('\nWORD',w)
 for d in ds[:1]:
  print('etym',d['etymology_text'][:600]);print('templates',json.dumps(d['etymology_templates'],ensure_ascii=False)[:2000]);print('derived',d['derived'][:15])
print('Affix entries',sum(any(d['pos'] in ['prefix','suffix','interfix','infix'] for d in ds) for ds in D.values()))
