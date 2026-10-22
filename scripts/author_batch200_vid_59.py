# -*- coding: utf-8 -*-
"""C1373 soror: two useful family and university words."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
def K(w):return 'https://en.wiktionary.org/wiki/'+w
def S(w):return 'https://www.etymonline.com/word/'+w
def M(w):return 'https://www.merriam-webster.com/dictionary/'+w
W=[
E('cousin','/ˈkʌzən/','堂兄弟姐妹；表兄弟姐妹；较远的亲戚；相近的事物','沿着家谱往上一代，再走到父母的兄弟姐妹家：他们的孩子就是最常见的 cousin。英语用一个词涵盖中文许多不同称呼。','经古法语 cosin、cosine 等，来自拉丁 consobrinus，含 con- 与 sobrinus。后者属于“姐妹、母系亲属”的词族，与 soror 有历史联系；不是现代英语 co- + sin。',[['拉丁 soror 及相关亲属词族','姐妹；sobrinus 接姐妹、母系亲属关系'],['拉丁 consobrinus','原来较具体的母方表亲称谓，后来扩展'],['古法语 cosin／cosine → 中古英语 cosin 等','亲属、表亲等'],['现代英语 cousin','通常指叔伯姑舅姨的孩子，也泛指较远亲戚或相似事物']],'cousin 本身不区分男女、长幼、堂表。first cousin 通常就是叔伯姑舅姨的孩子；distant cousin 是远房亲戚。复数 cousins 读 /ˈkʌzənz/。比喻中 close cousins 可说彼此相关的语言、技术或物种。','a first cousin；a distant cousin；my younger cousin；close cousins。','sibling 是亲兄弟姐妹，cousin 是旁系亲属。中文要译“表哥”还是“堂妹”，必须结合家族关系与年龄，单看 cousin 得不出来。',('My cousin is visiting us with her two children.','我的一位堂表姐妹要带两个孩子来做客。'),('The two programming languages are close cousins, but their syntax differs.','这两种编程语言关系很近，不过语法有所不同。'),('I grew up playing with my cousins every summer.','小时候，我每年夏天都和堂表兄弟姐妹一起玩。'),sources=[S('cousin'),K('cousin'),M('cousin')]),
E('sorority','英 /səˈrɒrəti/；美 /səˈrɔːrəti/','女生联谊会；女性社团、姐妹会','把没有血缘关系的成员看作“姐妹”，形成一个有身份认同和共同活动的团体。大学语境里常指北美校园的女生联谊组织。','来自中世纪或文艺复兴时期拉丁 sororitas“姐妹关系、姐妹团体”，词基是 soror“姐妹”。现代能认出 -ity 的名词形式，但它不是英语 sister 加后缀形成的。',[['拉丁 soror','姐妹'],['后期拉丁 sororitas','姐妹关系、姐妹团体'],['英语 sorority','女性团体；后来常指大学女生联谊会']],'join a sorority 是加入女生联谊会；a sorority house 是相关团体的会所或居住处。常见组织以希腊字母命名，但不等于希腊语课程，也不是所有女生宿舍都叫 sorority。','join a sorority；a sorority member；a sorority house；sorority events。','fraternity 在校园常指男生联谊组织，也有更广或混合成员用法；sorority 强调女性团体。sisterhood 更常表达姐妹情谊或女性团结。',('She joined a sorority during her second year at university.','她在大学二年级时加入了女生联谊会。'),('The sorority organized a book donation drive for local schools.','这个女生社团为当地学校组织了一次图书捐赠活动。'),sources=[S('sorority'),K('sorority'),M('sorority')]),
]
EXCLUDE={'cousins':'常规复数已在 cousin 正文给出读音和用例，不单独重复精讲；情报机构俚称等低频专义暂略。','sororal':'按用户要求暂略低频书面形容词，优先 cousin 与 sorority。','sororate':'按用户要求暂略专门婚姻人类学术语。','sororicide':'按用户要求暂略罕见杀姐妹及其行为者术语。'}
ROOT=dict(id='C1373',meaning='姐妹；姐妹相关的亲属与团体',core='拉丁 soror 是姐妹。一个方向沿家谱发展为表亲称谓 cousin，另一个方向把团体成员比作姐妹，形成 sorority。',image='姐妹及母系亲属关系 → consobrinus → cousin；姐妹关系、姐妹团体 → sororitas → sorority。',intro='这个词根在普通英语里不需要背很多生僻组合。掌握 cousin 如何把中文许多亲属称呼合在一起，以及 sorority 的校园文化用法，就已经很有价值。',forms='soror- 在 sorority 中还看得见；cousin 则经拉丁亲属词、法语和中古英语变化，外形差得很远。英语 sister 属日耳曼支线，与拉丁 soror 有更远的共同来源，不是从 soror 借来的。',branches=[['真实家族关系','cousin'],['把成员看作姐妹的团体','sorority']],contrasts='cousin 不编码男女、长幼与堂表；sorority 指团体，不等于一般女生宿舍。把 sister 与 soror 当同源亲戚可以，把英语 sister 画成拉丁 soror 的后代则不对。',practice='My cousin joined a sorority at university. 我的一位堂表姐妹在大学加入了女生联谊会。cousin 说明家族关系，sorority 说明社团身份。',words=[],exclude=EXCLUDE)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w and w not in EXCLUDE]
 assert set(ROOT['words'])&set(m['owned_words'])=={e['word'] for e in W}
 assert all(len(e['examples'])>=2 and len(e['history'])>=2 for e in W)
 OUT.mkdir(parents=True,exist_ok=True)
 (OUT/'roots_batch200_vid_59.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2));(OUT/'words_batch200_vid_59.json').write_text(json.dumps(W,ensure_ascii=False,indent=2))
 print('soror:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
