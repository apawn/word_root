# -*- coding: utf-8 -*-
"""C0356 dys: difficulty and impaired functioning, with existing shared lessons."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
def S(w):return 'https://www.etymonline.com/word/'+w
def O(w):return 'https://www.oxfordlearnersdictionaries.com/definition/english/'+w
W=[
E('dysentery','英 /ˈdɪsəntri/；美 /ˈdɪsənteri/','痢疾','先想到肠道感染造成的带血腹泻，而不是把所有拉肚子都叫这个词。','经古法语 disentere 或直接经中世纪拉丁 dysenteria 进入中古英语 dissenterie；远源是希腊 dys-“不正常、难受”与 entera“肠”组成的病名。不是英语把 dys 和一个独立单词 entery 拼起来。',[['希腊 dys- + entera → dysenteria','不正常、难受 + 肠 → 肠道疾病的名称'],['中世纪拉丁 dysenteria；古法语 disentere','病名流传到拉丁语和法语'],['中古英语 dissenterie → dysentery','痢疾']],'它常出现在历史、旅行卫生和公共卫生报道中。词根能帮助你看出“问题在肠道”，但今天这个词有明确的疾病含义，不能只凭肚子不舒服就把它当通用名称。','an outbreak of dysentery；cases of dysentery；contract dysentery。通常作不可数名词。','diarrhoea／diarrhea 是腹泻这个症状；dysentery 是伴有带血腹泻的肠道感染病名。两者有联系，使用范围却不同。',('The diary records an outbreak of dysentery in the camp.','那本日记记载了营地里的一次痢疾暴发。'),('Several patients were admitted to the hospital with dysentery.','几位痢疾患者住进了医院。'),sources=[S('dysentery'),O('dysentery'),'https://www.nhs.uk/conditions/dysentery/']),
E('dystrophy','英美 /ˈdɪstrəfi/','营养不良性病变；常见于 muscular dystrophy“肌营养不良症”','原来的命名把组织正常生长、维持的过程看成出了问题；现代最常遇到的是肌肉逐渐无力的那组疾病。','经近代拉丁 dystrophia／distrophia 借入，采用希腊 dys-“不良、失常”与 trophē“滋养”。现代可以分析为 dys- + -trophy，但不是把奖杯 trophy 放到前缀后面。',[['希腊 dys- + trophē','失常 + 滋养、维持生长'],['近代拉丁 dystrophia／distrophia','以这些希腊构件组成的医学名称'],['英语 dystrophy','用于组织病变；常见搭配 muscular dystrophy']],'muscular dystrophy 指一组与基因变化有关、导致肌肉逐渐无力的疾病。“营养不良”是沿用下来的中文病名，不能据此理解成单纯吃得少或缺营养。阅读时把整个病名作为一个单位理解。','muscular dystrophy；research into muscular dystrophy；a form of muscular dystrophy。','malnutrition 通常说摄入、吸收等方面造成的营养不足或失衡；muscular dystrophy 是特定疾病类别，不能用前者替换。trophy“奖杯”也不属于这里的滋养构件。',('The charity funds research into muscular dystrophy.','这家慈善机构资助肌营养不良症研究。'),('Her memoir describes living with muscular dystrophy.','她的回忆录讲述了患有肌营养不良症时的生活。'),sources=[S('dystrophy'),O('dystrophy'),'https://www.nichd.nih.gov/health/topics/musculardys/conditioninfo/causes']),
]
EX={w:'较专门的病理、生理或语言障碍术语；按通用阅读优先暂略。' for w in 'dysplasia dysphagia dyspepsia dyskinesia dysphasia'.split()}
SH={'dysfunction','dysfunctional','dyslexia','dyslexic','dystopia','dystopian','dysregulation','dyspnea','dysmorphic'}
ROOT=dict(id='C0356',meaning='失常；困难；不良',core='dys- 像给后面的过程加上“进行得不顺、出了问题”：function 是运作，dysfunction 就是运作失常。具体出了什么问题，要看它后面的构件。',image='dys- 不顺、失常 → dysfunction 运作失常；dyslexia 阅读困难；dystopia 糟糕的社会设想。',intro='这个希腊前缀常出现在医学和心理学词汇，也扩展到制度、家庭、社会等话题。它不总是简单表示“没有”，也不是给一个人作道德评价。先抓住后半部分，再理解困难发生在哪里。',forms='希腊 δυσ-，转写 dys-，通常读 /dɪs/。有些词是古代词整体借入，如 dysentery；有些是近代用希腊构件新造，有些直接接英语词，如 dysfunction。读音相似的拉丁前缀 dis- 有另外的历史。',branches=[['运行与调节失常','dysfunction, dysfunctional, dysregulation'],['阅读处理中的困难','dyslexia, dyslexic'],['令人不安的社会设想','dystopia, dystopian'],['身体问题的名称','dysentery, dystrophy, dyspnea, dysmorphic']],contrasts='dys- 的共同作用是标出困难或失常，具体词义仍由完整单词决定。dyslexia 不等于智力低下，dystrophy 也不能望文生义成单纯吃得不好；词源能帮助记忆，但不能代替现代含义。',practice='The novel depicts a dysfunctional society. 小说描绘了一个运作失常的社会：把 function“运作”找出来，dys- 的作用就容易看懂。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w and w not in EX];ROOT['words']+=sorted(SH-set(ROOT['words']))
 assert set(ROOT['words'])=={e['word'] for e in W}|SH
 assert {e['word'] for e in W}<=set(m['owned_words'])
 assert all(len(e['examples'])>=2 and len(e['history'])>=2 for e in W)
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_118.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('dys:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
