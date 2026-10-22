# coding: utf-8
import json
from pathlib import Path
ROOT=dict(id='C0993',meaning='五；五个组成的',core='PENT / PENTA = FIVE',image='先伸出五根手指，再问词的后半数的是什么：角、线、音级，还是比赛项目。',intro='希腊 pente 是五。这个成分出现在不同领域时数字很稳定，变化的是被数的东西：pentagon 数角，pentagram 用五条线组成星形，pentatonic 数每八度的音级，pentathlon 数比赛项目。',forms='常见组合形式为 pent-、penta-。不要把所有 pent 开头都归到“五”：例如 pent up 中的 pent 是 pen 围住的过去分词；它的意思是被关住、被压住，属于另一条词源。',branches=[['五个角的图形','pentagon、pentagonal'],['五线星形','pentagram'],['五个音级','pentatonic'],['五项比赛','pentathlon']],contrasts='五边形 pentagon 不等于五芒星 pentagram；五声音阶 pentatonic 不等于一首曲子只能弹五下。数词给出数量，后半成分和实际语境才说明数的是什么。',practice='She drew a pentagon while listening to a melody based on a pentatonic scale.\n\n她一边听着五声音阶写成的旋律，一边画了一个五边形。',words=['pentagon','pentagonal','pentagram','pentatonic','pentathlon'],exclude={w:'较冷门的专科术语，先掌握五边形、五线星、五声音阶与五项赛' for w in ['penton','pentode','pentad','pentapolis','diapente','pentalpha','pentatope','pentachoric']})
if __name__=='__main__':
 Path('.cache/batch200/drafts/root/roots_pent.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2))
 print('1 root; 5 shared words')
