"""Preserve existing word-family links while prepending verified simple forms.

Input: one JSON mapping on stdin. Intended for authored continuation batches.
"""
import ast,json,sys
from pathlib import Path
from explanatory import load_lessons
from lesson_order import RELATED

def update(groups):
 _,words=load_lessons()
 assert all(k in words and all(v in words for v in values) for k,values in groups.items()),'All grouping entries must already be authored'
 assert all(k not in values for k,values in groups.items()),'No self links'
 path=Path(__file__).with_name('lesson_order.py');source=path.read_text();tree=ast.parse(source)
 node=next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(q,ast.Name) and q.id=='RELATED' for q in n.targets))
 lines=source.splitlines(keepends=True);offsets=[0]
 for line in lines:offsets.append(offsets[-1]+len(line))
 def pos(line,col):return offsets[line-1]+len(lines[line-1].encode()[:col].decode())
 edits=[];seen=set()
 for key,value in zip(node.keys,node.values):
  name=ast.literal_eval(key)
  if name in groups:
   seen.add(name);edits.append((pos(value.lineno,value.col_offset),pos(value.end_lineno,value.end_col_offset),repr(list(dict.fromkeys(groups[name]+RELATED[name])))))
 for start,end,replacement in sorted(edits,reverse=True):source=source[:start]+replacement+source[end:]
 for name in sorted(groups.keys()-seen):source=source.replace('RELATED = {','RELATED = {\n    '+f'{name!r}: {groups[name]!r},',1)
 path.write_text(source)
 print('Updated',len(groups),'family links')
if __name__=='__main__':update(json.load(sys.stdin))
