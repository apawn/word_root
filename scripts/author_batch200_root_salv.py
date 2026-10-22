# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_salv_a import W as A
from author_batch200_root_salv_b import W as B
from author_batch200_root_salv_c import W as C
from author_batch200_root_salv_d import W as D
W=A+B+C+D;kept=[x['word'] for x in W]
ROOT=dict(id='C1252',meaning='保全；使安全；救回',core='SALV = KEEP SAFE',image='先想一个完整、安然无恙的人或物。救人是保住生命，存文件是保住成果，省钱是把钱留住；抢救残骸则是在损失后保住剩余价值。',intro='拉丁 salvus 表示安然无恙，salvare 是使安全、救回。经法语可见 save、safe，保留较明显拉丁词形的则有 salvation、salvage。同族 salus、salutis 的健康与问候支线，产生 salute、salutation、salutary。',forms='salv-、sav-、saf- 是历史借入后可见的形式，不应当作现代英语任意换字母规则。salut- 属相关的 salus 词干；salve 的常见药膏义另源，单独作辨析。',branches=[['保住与安全状态','save, safe, safety, safely, unsafe'],['保护安排与保管','safeguard, safekeeping'],['省下、攒下','saving, savings, saver'],['救助者与救生活动','savior, saviour, lifesaver, lifesaving'],['损失后的挽回','salvage, salvageable, unsalvageable'],['救赎与脱离困境','salvation'],['祝安好到致敬、有益','salute, salutation, salutary'],['同形异源辨析','salve']],contrasts='save 是动作，safe 是状态，safety 是状态名词。salvage 暗示已有损失后尽量挽回；salvation 常更庄重或带宗教含义。salutary 是有益，不等于愉快；salve 常用义不能凭拼写硬归同源。',practice='The files were safely stored, so the team could salvage the project after the computer failed.\n\n文件已经妥善保存，所以电脑故障后，团队仍能挽回这个项目。',words=kept,exclude={'sally':'常见突围、出击义来自法语 saillir、拉丁 salire 跳；本轮按 sali- 页学习，不把专名 Salvation Army 的口语简称混入此词根。'})
if __name__=='__main__':
 for name,data in [('roots_salv',[ROOT]),('words_salv',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 meta=[dict(word=w['word'],pos='noun' if w['word']=='savings' else 'adj',ipa=w['ipa'],gloss='Money kept rather than spent; amounts saved.' if w['word']=='savings' else 'Unable to be recovered or rescued after damage or failure.',meaning_zh=w['meaning'],etymology_text=w['split'],sources=w['sources']) for w in W if w['word'] in {'savings','unsalvageable'}]
 Path('.cache/batch200/root_salv_supplement_request.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
