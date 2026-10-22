# coding: utf-8
import json
from pathlib import Path
ROOT=dict(id='C0477',meaning='老年；变老',core='GER / GERONT = OLD AGE',image='把变老这件事放到不同镜头下：医疗镜头关注健康照护，更宽的镜头还研究心理、生活和社会。',intro='希腊 geras 表示老年，geron、词干 geront- 表示老人。英语借用这些材料，组成 geriatrics 老年医学和 gerontology 老年学。它们的范围相关，却并不相同。',forms='geriatrics 的 -iatrics 对应医疗学科；gerontology 的 -logy 对应研究。它们是近代使用希腊材料形成的术语，不是古希腊人已经使用的现代学科名称。',branches=[['老年医疗与照护','geriatric, geriatrics'],['更广的衰老与老年生活研究','gerontology']],contrasts='geriatrics 侧重老年人的医疗；gerontology 还包括生物、心理、社会等研究。geriatric 作日常称人用语时可能显得冒犯，医疗搭配中的用法则很常见。',practice='Geriatrics focuses on medical care; gerontology studies ageing more broadly.\n\n老年医学侧重医疗照护；老年学研究的范围更广。',words=['geriatric','geriatrics','gerontology'],exclude={w:'低频或细分专门词，本轮不展开' for w in ['progeria','erigeron','gerontocracy','gerascophobia','gerontophile','gerontophilia','gerontophobia','progeroid']})
if __name__=='__main__':
 Path('.cache/batch200/drafts/root/roots_ger.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2));print('root only; reuse 3 words')
