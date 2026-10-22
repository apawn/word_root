# -*- coding: utf-8 -*-
"""C1338 sider: stellar reference, not side + real."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('sidereal','英 /saɪˈdɪəriəl/；美 /saɪˈdɪriəl/','恒星的；以恒星为参照的','想象用远处星星的位置来判断地球转了一圈，而不是用太阳再次到达天空中相同位置来判断。这种“拿恒星作参照”的意思，就是 sidereal 在天文计时中的关键。','接拉丁 sidereus“星的”，来自 sidus，属格 sideris“星、星群”。英语有拉丁词干加 -al 的分析，也有经法语 sidéral 传入的路线；不是英语 side 加 real。',[['拉丁 sidus／sideris → sidereus','星、星群 → 星的'],['拉丁词干加 -al；亦有经法语 sidéral 的借入路线','形成恒星相关的形容词'],['英语 sidereal','恒星的；用于以恒星为参照的时间与运动']],'sidereal day 指恒星日，长度约为日常时钟的 23 小时 56 分钟。它比平均太阳日短约四分钟，是因为地球在自转的同时也绕太阳运动。先记住“参照对象换了”，就比死背两个时长更好理解。','sidereal time；a sidereal day；a sidereal year。它是形容词，通常和时间、周期或天文相关名词搭配。','solar 以太阳为关联对象；sidereal 强调恒星参照。sidereal 不等于夜晚的，也不表示只有晚上才能定义这种时间。',('The display compares a sidereal day with a solar day.','展板比较了恒星日与太阳日。'),('The observatory uses sidereal time to help track the positions of stars.','天文台利用恒星时帮助追踪恒星的位置。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/sidereal','https://www.merriam-webster.com/dictionary/sidereal','https://www.etymonline.com/word/sidereal','https://aa.usno.navy.mil/faq/GAST','https://ssd.jpl.nasa.gov/astro_par.html'])]
ROOT=dict(id='C1338',meaning='星；星群',core='拉丁 sidus 的相关形式是 sideris，词干 sider- 表示星或星群。sidereal 由此表示“恒星的”，在计时中尤其强调拿恒星作参照。',image='sidus／sideris 星、星群 → sidereus 星的 → sidereal 恒星的、以恒星为参照的。',intro='这一组最直观的切入口是恒星日与太阳日：地球仍是同一颗地球，只是判断它转到哪里时采用的参照不同。',forms='sider- 是 sidus 的屈折词干，不是英语 side。sidereal 接拉丁 sidereus，英语形成与法语借入路线均有词源分析。',branches=[['恒星参照的天文用语','sidereal']],contrasts='sidereal 与 solar 的区别主要在参照对象，不是白天与黑夜的区别。拼成 sider- 也不能自动把所有相似词都归入“星”这一支。',practice='用“恒星作参照”和“太阳作参照”分别解释 sidereal day 与 solar day。',words=['sidereal'],exclude={})
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_246.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('sider: 1 new; 2 examples')
