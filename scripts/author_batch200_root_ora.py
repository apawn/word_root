# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_ora_a import W as A
from author_batch200_root_ora_b import W as B
from author_batch200_root_ora_c import W as C
W=A+B+C;kept=[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0910')
EX={w:'本轮暂略较低频的祈祷或长篇演说术语' for w in set(r['family'])|set(r['words']) if w not in kept}
ROOT=dict(id='C0910',meaning='正式说话；恳求；祈祷',core='ORA = SPEAK / PLEAD',image='面对人群开口，是演说；朝神明开口，是祈求；面对别人反复请求却说不动，就碰上 inexorable。',intro='拉丁 orare 的可靠核心是公开讲话、恳求、祈祷。它与 os／oris“嘴”的联系是重要词源分析，但更远源也存在不同解释；以下演化从明确的拉丁节点展开。',forms='orat- 出现在拉丁演讲者、讲话行为等派生形式中；ad-orare 是朝某个对象祈求、敬拜。in-exorabilis 是无法被恳求说动。不同名词和形容词多有各自拉丁或法语借入链，不能全部画成英语 orate 的后代。',branches=[['面向人群说话','orator, oration, oratory, oratorical, orate'],['从敬拜到喜欢','adore, adoration, adorable, adorably, adoring'],['怎么求也改变不了','inexorable, inexorably'],['神谕与祈祷场所的音乐','oracle, oratorio']],contrasts='orator 是演说者，oration 是演说，oratory 是演讲艺术，另有祈祷堂义。adoring 是爱的一方，adorable 是惹人喜欢的对象。inexorable 不是无法解释，而是难以说动、阻止。',practice='The orator spoke with skill, but even his finest oratory could not stop the inexorable change.\n\n演说家讲得很有技巧，但再出色的雄辩也挡不住不可逆转的变化。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_ora',[ROOT]),('words_ora',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
