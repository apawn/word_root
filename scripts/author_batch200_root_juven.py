# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
B=[['拉丁 juvenis','年轻的；年轻人']]
W=[
E('juvie','/ˈdʒuːvi/','少年拘留所；少年犯等〔美式非正式用语，依语境〕','影视里说 someone is in juvie，通常是在说这个少年被关进少年拘留设施。','juvenile 的口语缩短形式，加上 -ie；不是从英语 June“六月”来的。',B+[['拉丁 juvenilis → 英语 juvenile','少年、未成年的'],['juvenile → juvie','口语缩短，常用于少年司法相关语境']],'in juvie 是在少年拘留所；a juvie 在某些语境可指涉案少年。这个词带口语色彩，范围由上下文决定，不是给所有儿童或青少年的通称。','be in juvie；get out of juvie；a juvie detention center。','juvenile 可正常形容未成年动物或年轻人；juvie 的常见口语义更窄，通常牵涉少年拘留或犯罪情节。正式机构名称不一定用它。',('In the film, he spends several months in juvie.','电影里，他在少年拘留所待了几个月。'),('The character is trying to rebuild his life after getting out of juvie.','这个角色从少年拘留所出来后，正努力重新开始生活。'),sources=['https://en.wiktionary.org/wiki/juvie']),
E('rejuvenating','/rɪˈdʒuːvəneɪtɪŋ/','使恢复活力的；让人精神焕发的','像给耗尽的电池重新充电，人或事物又有了清新、有劲的感觉。','rejuvenate + -ing；rejuvenate 以 re- 再、重新与拉丁 juvenis 年轻为基础，表示让青春或活力回来。',B+[['re- + juven- + -ate → rejuvenate','使重新年轻；恢复活力'],['rejuvenate + -ing → rejuvenating','有恢复活力效果的']],'a rejuvenating break 是让人恢复精神的休息；a rejuvenating walk 是走完让人觉得神清气爽的散步。它常表达体验，并不一定声称身体年龄真的变小。','a rejuvenating break；a rejuvenating experience；a rejuvenating walk。','rejuvenating 说带来活力的效果；rejuvenated 说已经恢复活力的状态。广告中的 rejuvenating 也只是描述词，不能直接当成具体效果证明。',('A quiet weekend by the sea was deeply rejuvenating.','在海边安静地过一个周末，让人重新恢复了精神。'),('She found the morning walk surprisingly rejuvenating.','她觉得早晨散步格外提神，出乎自己的意料。'),sources=['https://en.wiktionary.org/wiki/rejuvenating','https://en.wiktionary.org/wiki/rejuvenate'])
]
ROOT=dict(id='C0629',meaning='年轻；青春',core='JUVEN = YOUNG',image='一株年轻植物充满生机；把这种生机带回疲惫的人或老旧事物，就是 rejuvenate 的“重新有活力”。',intro='来自拉丁 juvenis“年轻的、年轻人”。juvenile 既可以客观说年幼、未成年，也可以批评行为幼稚；rejuvenate 把年轻扩展成精力、活力和新气象。junior 也是相关的比较级来源词，已有独立精讲。',forms='juvenile 接拉丁 juvenilis；juvie 是它的口语缩短形式。rejuvenate 有 re- 重新与 juven- 年轻的组合，rejuvenation 表过程或效果，rejuvenating 表能使人恢复活力的。',branches=[['年幼、未成年','juvenile, juvie'],['重新焕发活力','rejuvenate, rejuvenation, rejuvenating']],contrasts='juvenile 不等于任何场景下都幼稚；说 juvenile birds 只是幼鸟。juvie 的少年拘留语境较窄。rejuvenate 可以用于城市、产业或设计，不只说人的年龄。',practice='The quiet holiday was rejuvenating, and she returned to work with fresh energy.\n\n这次安静的假期让她恢复了活力，回到工作时精神焕发。',words=[x['word'] for x in W]+['juvenile','rejuvenate','rejuvenation'],exclude={})
if __name__=='__main__':
 for name,data in [('roots_juven',[ROOT]),('words_juven',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
