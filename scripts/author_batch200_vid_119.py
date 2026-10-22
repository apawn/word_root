# -*- coding: utf-8 -*-
"""C0385 erot: desire in ordinary criticism and descriptive vocabulary."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
def S(w):return 'https://www.etymonline.com/word/'+w
def O(w):return 'https://www.oxfordlearnersdictionaries.com/definition/english/'+w
EROS=['希腊 erōs，词干 erōt-','爱欲，尤其指带性欲的爱']
EROT=[EROS,['希腊 erōtikos → 法语 érotique','与爱欲有关的'],['英语 erotic','表现或唤起性欲的']]
W=[
E('erotic','英 /ɪˈrɒtɪk/；美 /ɪˈrɑːtɪk/','性爱的；情色的；能唤起性欲的','作品里的吸引力如果明确带有性欲意味，就可以用 erotic；不一定要直接描写性行为。','经法语 érotique 借入，来自希腊 erōtikos，与 erōs、词干 erōt-“爱欲”相接。现代可辨认 erot- + -ic，但完整词在法语和希腊语中已有历史。',EROT,'评论里 erotic art、erotic tension 分别说作品的情色成分、人物之间带性意味的张力。这个词指出的是欲望的性质，不自动评价作品是否高雅，也不等于所有爱情题材。','erotic art；erotic imagery；erotic tension；an erotic theme。','romantic 重点可以是恋爱、温柔和理想化的情感；erotic 明确带有性欲成分。两者能够同时出现，但不能完全互换。',('The exhibition explores erotic themes in classical sculpture.','这场展览探讨古典雕塑中的性爱主题。'),('The critic found erotic tension beneath the characters’ polite conversation.','评论者在人物礼貌的交谈之下读出了带有性意味的张力。'),sources=[S('erotic'),O('erotic')]),
E('eroticism','英 /ɪˈrɒtɪsɪzəm/；美 /ɪˈrɑːtɪsɪzəm/','情色意味；性爱欲望的表现','把作品中那层带有性欲的气氛单独拿出来讨论，就是在讨论它的 eroticism。','英语 erotic + -ism 构成抽象名词。这里 -ism 不必译成“主义”，它把情色的性质、表现变成可讨论的概念；加后缀后字母 c 读 /s/。',EROT+[['英语 erotic + -ism → eroticism','作品、表达中的情色性质与欲望表现']],'它常作为不可数名词，谈的是一幅画、一首诗或一部电影怎样表现欲望。subtle eroticism 是含蓄的情色意味，不一定是露骨内容。','the eroticism of a painting；subtle eroticism；an exploration of eroticism。','erotic 是形容词，用来修饰作品；eroticism 是那种性质的名词。后缀 -ism 在这里不意味着某个有纲领的思想派别。',('Her essay examines the subtle eroticism of the poems.','她的文章分析了这些诗中含蓄的情色意味。'),('The director used lighting to suggest eroticism without explicit scenes.','导演通过灯光暗示情色意味，没有采用露骨场景。'),sources=[S('eroticism'),O('eroticism')]),
E('erotically','英 /ɪˈrɒtɪkli/；美 /ɪˈrɑːtɪkli/','带有性欲意味地；从情色角度','它不是给对象起一个新名称，而是告诉你：某种表现、描写或理解带有性欲的意味。','英语 erotic 形成的副词，现代常分析为 erotic + -ally；也能联系较早的形容词 erotical。远源沿 erotic 回到法语 érotique、希腊 erōtikos。',EROT+[['英语 erotically','把情色性质用于说明表现方式或感受']],'erotically charged 常见于艺术评论：场景充满性吸引的张力。charged 在这里是“充满某种强烈情绪”，不是字面充电。','erotically charged；erotically suggestive；interpret something erotically。','erotically 修饰形容词或动词；erotic 修饰名词。比较 an erotic scene 与 an erotically charged scene，后者强调气氛里积聚的张力。',('The reviewer described the scene as erotically charged.','影评人形容这个场景充满了性吸引的张力。'),('Some readers interpret the imagery erotically, while others focus on its religious meaning.','有些读者从情色角度理解这些意象，另一些则关注其宗教含义。'),sources=[S('erotic'),O('erotically'),'https://en.wiktionary.org/wiki/erotically#English']),
E('homoerotic','英 /ˌhəʊməʊəˈrɒtɪk/；美 /ˌhoʊmoʊəˈrɑːtɪk/','表现同性之间爱欲的；带有同性情色意味的','关注的是同一性别人物之间的欲望或吸引如何被表现出来，常见于文学、电影和艺术评论。','近代术语由 homo- 与 erotic 组合；这里 homo- 表示同性，远接希腊 homos“相同”。英语早期记录见于精神分析作品的翻译，不能当作古希腊已存在的整个英语词。',[['两组希腊构件：homos；erōs／erōtikos','相同；爱欲、与爱欲有关的'],['近代 homo- + erotic → homoerotic','把同性关系与爱欲表现结合起来'],['英语 homoerotic','描述同性之间的欲望、意象或潜在意味']],'homoerotic subtext 是作品没有直说、却可被读出的同性爱欲意味。这种评论在分析作品的内容与效果，不能仅凭作品有这种意味，就断定作者本人的性取向。','homoerotic imagery；homoerotic themes；a homoerotic subtext。','homo- 在这里不是拉丁 homo“人”。homoerotic 常描述欲望的表现；gay、lesbian 等词还能用于人的身份，使用重点不同。',('The seminar examined homoerotic imagery in Renaissance painting.','研讨课分析了文艺复兴绘画中的同性爱欲意象。'),('The critic argued that the film contained a homoerotic subtext.','评论者认为这部电影包含同性爱欲的潜在意味。'),sources=[S('homoerotic'),O('homoerotic'),'https://en.wiktionary.org/wiki/homoerotic#English']),
]
EX={w:'较冷门的精神医学或态度分类术语，本轮按通用阅读优先暂略。' for w in 'erotomania erotophilia erotophobia'.split()}
SH={'erogenous'}
ROOT=dict(id='C0385',meaning='爱欲；带性意味的爱',core='erot- 抓住的是爱欲中的身体吸引和性欲成分。它能帮助理解艺术评论中的 erotic，也能用于描述相关的身体敏感性。',image='erōs 爱欲 → erōtikos → erotic；erotic + -ism → eroticism；homo-同性 + erotic → homoerotic。',intro='先把“爱”分细一点：温柔的关心、浪漫的恋爱和带性欲的吸引会重叠，却不是同一个意思。这组词主要抓第三层，文学与艺术文章里很常见。',forms='希腊 ἔρως erōs 的属格 erōtos 显出 erot- 词干；erotic 经法语 érotique 借入。erogenous 使用较短的 ero- 与 -genous“产生”组合，不是从英语 erosion“侵蚀”派生。',branches=[['作品与表达中的爱欲','erotic, eroticism, erotically'],['同性关系中的爱欲意味','homoerotic'],['身体敏感性的描述','erogenous']],contrasts='erotic 可以描述作品的气氛或主题，erogenous 常用于身体的敏感区域。eroticism 的 -ism 表示性质和表现，不必硬译成“主义”。词形相近的 erosion 来自另一条“啃蚀”词源。',practice='The critic discussed the painting’s eroticism. 评论者讨论了这幅画的情色意味：erotic 给出性质，eroticism 把性质变成讨论对象。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w and w not in EX]
 assert set(ROOT['words'])=={e['word'] for e in W}|SH
 assert {e['word'] for e in W}<=set(m['owned_words'])
 assert all(len(e['examples'])>=2 and len(e['history'])>=2 for e in W)
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_119.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('erot:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
