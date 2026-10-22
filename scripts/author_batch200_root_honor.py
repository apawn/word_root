# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_honor_a import W as A
from author_batch200_root_honor_b import W as B
from author_batch200_root_honor_c import W as C
W=A+B+C
ROOT=dict(id='C0566',meaning='尊敬；荣誉；值得尊敬的品格',core='HONOR = RESPECT / ESTEEM',image='想象别人郑重地向一个人致敬：可以给他荣誉，也可以因为他守诺、诚实而敬重他。荣誉和诚实就在“值得尊敬”这里接上。',intro='来自拉丁 honos，后来也用 honor，属格 honoris。古法语把它带入英语，形成 honor/honour。honest 则沿拉丁 honestus“值得尊敬的”这条支线，逐渐突出“不欺骗、坦诚”。更远来源未定，从可靠的拉丁节点记起即可。',forms='honor 美式、honour 英式；honored/honoured、honorable/honourable 等随之变化。h 都不发音。honest 不是 honor 加最高级 -est；honesty 和 dishonesty 有各自的拉丁—法语名词借入链。',branches=[['给予和接受尊敬','honor, honour, honored, honoree'],['品格与称号','honorable, honorably, honorary, honorific, honorarium'],['损害名誉','dishonor, dishonorable, dishonorably'],['从正直到诚实','honest, honesty, honestly, dishonest, dishonesty, dishonestly']],contrasts='honorable 是正直、值得尊敬；honorary 是为表彰而授予；honorific 是表示敬意的称谓。honor a promise 是履行承诺。honest 不保证判断正确，dishonest 也不能只由一次无心错误推断。',practice='The honorary member gave an honest answer and said she felt honored by the invitation.\n\n这位名誉会员作了坦诚的回答，并表示受邀让她感到荣幸。',words=[x['word'] for x in W],exclude={'honorand':'较少见受荣誉者称谓，常用 honoree 已讲'})
if __name__=='__main__':
 for name,data in [('roots_honor',[ROOT]),('words_honor',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
