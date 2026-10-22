# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_pol_a import W as A
from author_batch200_root_pol_b import W as B
W=A+B
ROOT=dict(id='C1087',meaning='轴；极；极点',core='POL = AXIS / POLE',image='想象一个转动的地球，轴线通向两端。由轴端可以理解极地、两极属性，也能联想到相距很远的两种立场；物理术语再按各自定义理解。',intro='来自希腊 polos，意为轴、枢轴等，经拉丁 polus 进入后来的欧洲语言。pole 的极点义属于这一支；pole 的木杆义另来自拉丁 palus 的日耳曼借词。polar 经拉丁或法语形式进入英语，polarize 则最初是近代法语光学术语。',forms='pol- 在 polar、polarity 中显现；di- + pole 得 dipole，bi-/uni-/multi- + polar 分别表示两极、单极、多极。polarise/polarisation 与 polarize/polarization 是常见拼写差异。',branches=[['极点及相关属性','pole, polar, polarity'],['一极、两极、多极及环极','unipolar, bipolar, multipolar, dipole, circumpolar'],['形成分化或物理偏振、极化','polarize, polarise, polarization, polarisation'],['状态与引发作用','polarized, polarised, polarizing, polarising']],contrasts='polar 不是 police 或 politics 的缩写，后两者主要接城市 polis 一支。偏振、材料电极化、社会两极分化是不同领域的概念，不用一个字面拆分替代专业定义。',practice='A polarizing speech can leave an already divided audience even more polarized.\n\n一场容易引起对立的演讲，可能使本来就有分歧的听众更加两极分化。',words=[x['word'] for x in W]+['pole','bipolar','unipolar','multipolar'],exclude={})
if __name__=='__main__':
 for name,data in [('roots_pol',[ROOT]),('words_pol',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
