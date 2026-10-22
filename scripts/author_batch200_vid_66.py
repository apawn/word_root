# -*- coding: utf-8 -*-
"""C0606 infra: beneath a structure or below a reference frequency."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('infrared','英、美 /ˌɪnfrəˈred/','红外线；红外的','把可见光按频率排开，越过红光的低频一侧，就来到眼睛通常看不见的红外区域。它不是“更深的红色”，而是红光之外的一段电磁波。','英语 infra-“低于” + red，19 世纪形成；infra- 来自拉丁 infra“在下面”。这里可以按低于红光的频率理解，不能误记成波长更短：红外波长比红光更长。',[['拉丁 infra','在下面、低于'],['英语 infra- + red → infrared','在可见光红端之外、频率更低的一侧'],['现代 infrared','红外辐射；探测或使用红外线的']],'红外线可用于遥控器、天文观测和热成像等。热成像利用特定红外波段反映物体的热辐射；不能反过来把一切红外图像都当作温度照片，也不能把“红外”直接等同于全部热量。','infrared radiation；an infrared camera；infrared imaging；an infrared signal。','ultraviolet 在可见光紫端之外，频率更高；infrared 在红端之外，频率更低。infrasonic 则是声音的低频范围，属于另一种波。',('The remote control sends an infrared signal to the television.','遥控器向电视发送红外信号。'),('The astronomers compared visible and infrared images of the same region.','天文学家比较了同一区域的可见光图像与红外图像。'),sources=['https://www.etymonline.com/word/infra-red','https://www.oxfordlearnersdictionaries.com/definition/english/infrared','https://science.nasa.gov/ems/07_infraredwaves/','https://www.grc.nasa.gov/WWW/k-12/Aero2000/studweb/glossary/infrared.html'])]
ROOT=dict(id='C0606',meaning='在下面；低于',core='infra- 是“在下面、低于”。下面可以是支撑上层活动的基础，也可以是低于某条频率界限。先问清楚它在和什么比较。',image='支撑生活和工作的底层系统 → infrastructure；低于红光频率 → infrared；低于通常人耳频率下限 → infrasound／infrasonic。',intro='从基础设施和红外遥控器出发，这个前缀就不抽象了。基础设施的“底层”常是功能比喻，不等于全部埋在地下；红外、次声的“低”则指频率。',forms='拉丁 infra 本身是副词、介词，后来作为前缀参与近现代构词。infrastructure 经法语借入，infrared 在英语中由 infra- 与 red 组合，infrasound／infrasonic 属近现代科学命名。',branches=[['支撑系统的基础','infrastructure, infrastructural'],['可见光红端之外','infrared'],['通常听觉下限之外','infrasound, infrasonic']],contrasts='infra- 不等于 intra-“在内部”。infrared 的频率更低、波长更长；infrasonic 不是速度低于声速。infrastructure 可以包括地上的桥梁、通信系统等。',practice='Infrastructure supports everyday life. Infrared lies below visible red in frequency. 两句中的“下面”分别是功能上的底层、频率上的低端。',words=['infrastructure','infrastructural','infrared','infrasound','infrasonic'],exclude={})
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());already={'infrasound','infrasonic'}
 assert (set(ROOT['words'])&set(m['owned_words']))-already=={e['word'] for e in W}
 assert all(len(e['examples'])>=2 and len(e['history'])>=2 for e in W)
 OUT.mkdir(parents=True,exist_ok=True)
 (OUT/'roots_batch200_vid_66.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2));(OUT/'words_batch200_vid_66.json').write_text(json.dumps(W,ensure_ascii=False,indent=2))
 print('infra:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
