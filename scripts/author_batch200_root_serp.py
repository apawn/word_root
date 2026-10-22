# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
B=[['拉丁 serpere → serpens，词干 serpent-','爬行 → 爬行之物、蛇']]
W=[
E('serpent','英 /ˈsɜːpənt/；美 /ˈsɜːrpənt/','蛇；文学或宗教语境中的蛇','这个名称把蛇看成在地上爬行、滑动的东西。','来自古法语 serpent，源于拉丁 serpens；后者本是 serpere 爬行的现在分词，名词化后指蛇。英语 -ent 在这里保留了拉丁分词形态的痕迹。',B+[['古法语 serpent → 英语 serpent','蛇的名称进入英语']],'日常看到草丛里有蛇，多半说 snake。serpent 更常出现在神话、宗教、文学或有象征意味的图案里，容易让人想到盘绕的蛇形。它不是某个固定的大型蛇品种，也不自动表示有毒。','a serpent in a myth；a coiled serpent；a serpent symbol。','snake 是常用名称，serpent 语气更书面、富于意象。不能把 serpent 统一翻译成巨蟒，具体大小和种类要看上下文。',('A serpent is carved around the handle of the cup.','杯子的把手上雕着一条盘绕的蛇。'),('The story describes a serpent guarding the hidden garden.','故事描写了一条守护隐秘花园的蛇。'),sources=['https://www.etymonline.com/word/serpent','https://www.oxfordlearnersdictionaries.com/definition/english/serpent']),
E('serpentine','英 /ˈsɜːpəntaɪn/；美 /ˈsɜːrpəntaɪn/','像蛇一样弯曲的；蜿蜒的；错综曲折的','想象蛇身一弯接一弯：道路、河流，甚至故事线也能这样绕来绕去。','经法语 serpentin，最终关联拉丁 serpentinus 蛇的、像蛇的；现代可看成 serpent + -ine。较晚的蜿蜒义把蛇的形状和运动方式移到别的事物上。',B+[['拉丁 serpentinus → 法语 serpentin → 英语 serpentine','蛇的、像蛇的'],['形状与比喻延伸','路线蜿蜒；情节或过程曲折']],'a serpentine road 强调连续弯曲的形状；a serpentine plot 把故事看成有很多转折、难以一下看清的路线。这种形容比 winding 更有画面，也更书面。不需要对象真的像一条完整的蛇。','a serpentine road；a serpentine path；a serpentine plot。','serpentine 通常强调像蛇一样曲折，steep 讲坡度陡，narrow 讲宽度窄。一条路可以三种特点都有，但这些形容词各说不同的事。',('A serpentine road climbed through the wooded hills.','一条蜿蜒的道路穿过林木覆盖的山丘，向上延伸。'),('The novel’s serpentine plot kept us guessing until the last chapter.','小说曲折的情节让我们一直猜到最后一章。'),sources=['https://www.etymonline.com/word/serpentine','https://dictionary.cambridge.org/us/dictionary/english/serpentine','https://dictionary.cambridge.org/pronunciation/english/serpentine'])
]
ROOT=dict(id='C1323',meaning='爬行；像蛇一样移动',core='SERP = CREEP / CRAWL',image='一条蛇贴着地面向前滑动，身体弯弯曲曲；同样的形状也能拿来描述道路和故事。',intro='拉丁 serpere 是爬行，serpens 本来可理解为爬行的东西，后来指蛇。英语保留 serpent 作蛇的书面名称，又用 serpentine 把蛇的形状借给路线和情节。',forms='serpent 保留拉丁分词词干 serpent-，serpentine 与拉丁、法语的蛇形形容词相连。现代可以联系 serpent + -ine，但它有历史借入背景。',branches=[['蛇的名称','serpent'],['蛇形路线与曲折情节','serpentine']],contrasts='serpent 与日常 snake 在指动物时大体同义，但语气不同；serpentine 不保证道路很陡或很窄，只突出曲折蜿蜒。',practice='The serpentine path reminded her of a serpent moving through the grass.\n\n那条蜿蜒的小路让她想到一条在草丛中移动的蛇。',words=[x['word'] for x in W],exclude={})
if __name__=='__main__':
 for name,data in [('roots_serp',[ROOT]),('words_serp',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
