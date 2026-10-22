# -*- coding: utf-8 -*-
"""C0668 leuc/leuk: white cells and distinct medical terms."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('leukemia','/luːˈkiːmiə/','白血病；英式常写 leukaemia','名称里的“白”指向白细胞。真正要理解的是造血组织发生癌变、异常血细胞大量产生，不是人的血液真的变成白色。','英语仿照或借用十九世纪德语 Leukämie；德语名用希腊 leukos“白”与 haima“血”构成。现代可以识别 leuk- + -emia“血液状况”，但完整病名先在近代医学中形成。',[['希腊 leukos + haima','白色 + 血'],['十九世纪德语 Leukämie → 英语 leukemia／leukaemia','以白细胞异常增多的观察命名白血病']],'leukemia 是一类起于骨髓等造血组织的癌症名称，还分不同类型。“白血病”这个译名保留了同一个历史画面，但读文章时不能把所有白细胞异常都叫 leukemia。它也不是靠“血看起来是什么颜色”来定义的。','acute leukemia；chronic leukemia；leukemia research；a type of leukemia。leukaemia 是常见英式拼写，意义与读音相同。','leukocyte 是白细胞这一正常细胞类别；leukemia 是癌症类别。leukopenia 则说白细胞数量过低，不能与 leukemia 当成同义词。',('The charity funds research into several types of leukemia.','这家慈善机构资助对白血病多个类型的研究。'),('The British report spells the word “leukaemia.”','这份英国报告把这个词拼作 leukaemia。'),sources=['https://www.etymonline.com/word/leukemia','https://www.oxfordlearnersdictionaries.com/definition/english/leukaemia','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/leukemia','https://www.cancer.gov/about-cancer/understanding/what-is-cancer']),
E('leukopenia','英 /ˌluːkəʊˈpiːnɪə/；美 /ˌluːkoʊˈpiːniə/，也读 /ˌluːkəˈpiːniə/','白细胞减少；亦拼 leucopenia','把后半段 -penia 想成“不够、缺少”：血液里循环的白细胞数比正常范围低。它首先描述一种计数状态。','近代拉丁医学名称，由 leuko-“白”与希腊 penia“贫乏、缺少”组成，再进入英语。leuko- 在这里借“白”指白细胞；不是所有白色物质都变少。',[['希腊 leukos + penia','白色 + 缺少、贫乏'],['近代拉丁 leukopenia → 英语 leukopenia／leucopenia','用于血液白细胞数偏低的医学名称']],'看检查报告时，leukopenia 说的是“数量低于正常”，词本身没有告诉你唯一原因，也不等于某一种癌症。这里保留这个词，是为了能读懂医学文章里的基本表述；不要把它和白血病仅凭前半截混在一起。','develop leukopenia；a report of leukopenia；leukopenia and other blood abnormalities。leucopenia 是同义拼写。','leukopenia 是白细胞减少，neutropenia 专指其中的中性粒细胞减少。前者范围更宽；它们也不同于 anemia 所说的贫血。',('The report describes leukopenia as a low white blood cell count.','报告把 leukopenia 解释为白细胞计数偏低。'),('The glossary lists leucopenia as an alternative spelling of leukopenia.','词汇表把 leucopenia 列为 leukopenia 的另一种拼写。'),sources=['https://www.cancer.gov/publications/dictionaries/cancer-terms/def/neutropenia','https://www.merriam-webster.com/dictionary/leukopenia','https://www.collinsdictionary.com/dictionary/english/leucopenia','https://www.collinsdictionary.com/dictionary/english/leukopenia','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/leukopenia']),
]
SH=['leukocyte','leucocyte']
EX={w:'专业细分病理或生物结构术语，按当前常用阅读范围暂略。' for w in ['aleukocytosis','leucism','leucophore','leucoplast','leukocytopenia','aleukemia']}
EX['leucopenia']='同义拼写已在 leukopenia 独立精讲中完整说明，不重复建词条。'
ROOT=dict(id='C0668',meaning='白色、明亮',core='leukos 是希腊语的“白”。现代医学把它用于白细胞相关名称，再用后面的构件说明在讲细胞、数量还是疾病。',image='leukos 白 → leukocyte 白细胞；leukos + haima 血 → Leukämie → leukemia；leuko- + penia 缺少 → leukopenia。',intro='只认出 leuk- 还不够：leukocyte 是细胞，leukopenia 是白细胞减少，leukemia 是白血病。后半个词决定你究竟在读什么。',forms='leuc- 与 leuk- 反映拉丁化 c 和希腊 k 的不同写法；leuco-／leuko- 是组合形式。leukemia 又有英式 leukaemia；拼写变体不等于病种改变。',branches=[['白细胞本身','leukocyte, leucocyte'],['数量状态与疾病名称','leukopenia, leukemia']],contrasts='“白”是命名线索，不是凭肉眼颜色就能判断的标准。白细胞、白细胞减少和白血病属于不同层次的概念，不能因为同根就视为同义。',practice='先问结尾：-cyte 指细胞，-penia 指缺少，-emia 与血液状况有关。再回到完整词的实际含义，尤其把 leukemia 当作独立病名记。',words=[e['word'] for e in W]+SH,exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id'])
 assert {w for w in r['family'] if '-' not in w}<=set(ROOT['words'])|set(EX)
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_155.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('leuc:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
