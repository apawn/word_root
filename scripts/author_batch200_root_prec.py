# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_prec_a import W as A
from author_batch200_root_prec_b import W as B
W=A+B
ROOT=dict(id='C1116',meaning='请求、祈求；依靠恩惠与表示反对',core='PREC = ASK / PRAY',image='向别人开口求一件事。求来的东西可能全靠别人愿意，所以没保障；祈求一件坏事离开，则能转向反对它。这两次转折连接了祈祷、不稳定和不赞成。',intro='拉丁 prex 的属格 precis 显出 prec-，动词 precari 是祈求。经法语变化的一支成为 pray、prayer；precarius“求得、依赖恩惠的”变成 precarious“不稳固”；deprecari“祈求免于”走向 deprecate“不赞成”，又进入软件的弃用术语。',forms='prec- 不是 pre-“在前”的后面多一个 c。pray 经法语变音，词根外形已不明显。祈祷义 prayer 是法语名词路线；deprecation 也有独立名词借入史。deprecated 与 depreciated 要看清中间是否多一个 i。',branches=[['祈求与祷文','pray, prayer'],['依靠恩惠到缺乏保障','precarious, precariously, precariousness'],['祈求免于到不赞成、弃用','deprecate, deprecation, deprecated, deprecating']],contrasts='prayer 常见义是祈祷本身，不能每次拆成 pray + -er“祈祷的人”。precarious 常见义来自祈求而不是“预先”。deprecation 是弃用或不赞成，depreciation 则是价值下降。',practice='The old function is deprecated, but it has not yet been removed.\n\n旧函数已不建议使用，但还没有被移除。',words=[w['word'] for w in W],exclude={'imprecation':'较冷门的正式或文学诅咒用语，本轮按优先级暂略'})
if __name__=='__main__':
 for name,data in [('roots_prec',[ROOT]),('words_prec',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
