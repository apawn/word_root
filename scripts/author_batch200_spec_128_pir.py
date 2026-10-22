# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
P=['希腊语 peira → peiran → peirates','尝试、进攻 → 袭击者、海盗']
PIRATE=[P,['拉丁语 pirata → 法语 pirate','海盗'],['中古英语 pirate → 现代英语 pirate','海盗；后也指盗用作品者，并转作动词']]
PIRACY=[P,['希腊语 peirateia；中古拉丁 piratia','海盗行为'],['英语 piracy','海盗行为；后扩展为盗版活动']]
W=[
E('pirate','英美 /ˈpaɪrət/','海盗；盗版者；盗用、制作盗版','从抢夺船只和财物的人，扩展到未经许可利用别人作品的人或行为。','经法语 pirate 或中古拉丁 pirata 借入，接希腊 peirates“袭击者、海盗”，更前面是尝试、进攻的 peira、peiran。现代英语不宜把 pir- 当成可随意造词的“偷”前缀。',PIRATE,'海上的 pirate 抢夺船只或财物。作品领域把这个名称借给盗用者；作动词时 pirate a film 表示非法复制、传播影片。pirate radio 则是未经许可的广播，未必真的从船上发射。','a pirate ship；pirate attacks；pirate radio；pirate software。','pirate 的人称义与 piracy 的活动义分开。plagiarist 更突出把别人的创作冒充自己的，盗版则不一定掩盖原作者是谁。',('The story follows a pirate searching for a hidden island.','故事讲述一名海盗寻找隐秘岛屿的经历。'),('The report explains how the film was pirated and distributed online.','报告说明了这部影片怎样被盗版并在网上传播。'),sources=['https://www.etymonline.com/word/pirate','https://www.oxfordlearnersdictionaries.com/definition/english/pirate_1']),
E('piracy','英美 /ˈpaɪrəsi/','海盗活动；盗版行为','把抢掠或盗版看成一类活动，而不是某个做这件事的人。','借中古拉丁 piratia，联系希腊 peirateia、peirates。它是已有古典语前史的活动名词；现代可和 pirate 配对记忆，但不是把英语 pirate 随意换成 -cy 才第一次产生。',PIRACY,'讨论航运时 piracy 多指海盗袭击；讨论电影、软件、书籍时则指未经许可复制、传播作品的盗版活动。这个词通常不可数，描述整个现象；具体一次海盗袭击可以说 an act of piracy。','maritime piracy；software piracy；digital piracy；combat piracy；an act of piracy。','piracy 是活动，pirate 是人或动词。作品是免费的不自动等于 piracy，关键看是否有相应许可和权利依据，不能只凭收费与否判断。',('The museum has an exhibition on the history of maritime piracy.','博物馆有一个介绍海盗活动历史的展览。'),('The article discusses the effect of digital piracy on small publishers.','文章讨论了数字盗版对小型出版社的影响。'),sources=['https://www.etymonline.com/word/piracy','https://www.oxfordlearnersdictionaries.com/definition/english/piracy']),
E('antipiracy','英 /ˌæntiˈpaɪrəsi/；美 /ˌæntaɪˈpaɪrəsi/，也读 /ˌæntiˈpaɪrəsi/','反盗版的；反海盗的','形容旨在防止海盗活动或盗版的措施、行动、工具。','英语 anti-“反对、防止” + piracy。它可以写成一个词，也有连字符拼法；这里保留连续拼写这一词条。',PIRACY+[['英语 anti- + piracy → antipiracy','针对海盗或盗版的']],'an antipiracy patrol 是反海盗巡逻，an antipiracy campaign 在出版、影视语境则常是反盗版宣传。先看 piracy 在谈船只还是作品，再给 anti- 加上“防止”。','antipiracy measures；an antipiracy campaign；antipiracy patrols；antipiracy software。','anti- 在这里表示反对、预防，不是 before。antipiracy 也不说明措施一定采用某种特定技术，它只表明目的。',('The publisher launched an antipiracy awareness campaign.','出版社发起了一项反盗版宣传活动。'),('The coast guard expanded its antipiracy patrols.','海岸警卫队扩大了反海盗巡逻。'),sources=['https://dictionary.cambridge.org/dictionary/english/anti-piracy','https://www.dictionary.com/browse/antipiracy','https://en.wiktionary.org/wiki/antipiracy'])
]
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(r for r in m['roots']if r['id']=='C1047');family=r['family'];keep={w['word']for w in W}
excluded={'apeirogon':'希腊 apeiros“无限”+角的几何术语，不是 peirates“海盗”词族；且属冷门术语。','apeirohedron':'希腊 apeiros“无限”+面的几何术语，不是 peirates“海盗”词族；且属冷门术语。','piratic':'按用户范围暂略罕用形容词。','e-piracy':'用户暂略含连字符的组合词。'}
ROOT=[dict(id='C1047',meaning='尝试、进攻；海盗',core='pir-：本组主要记“袭击者、海盗”以及由此发展出的盗版比喻。',image='从海上抢掠的海盗，转到未经许可复制传播作品的行为。',intro='希腊 peirates 表示袭击者、海盗，经拉丁语与法语传下 pirate。piracy 是相关活动名词，anti- 再表示反对、预防。词源更早的“尝试”只是历史基础，现代不能把海盗直接翻成普通尝试者。',forms='pirate 与 piracy 分别有借词历史，不能把 t/c 的变化解释成任意拼写替换。pir- 也不是可以对所有相似单词生效的“抢夺”前缀。',branches=[['做事的人与动作','pirate'],['活动与现象','piracy'],['防止相关活动','antipiracy']],contrasts='盗版 piracy 与冒充原创的 plagiarism 有交集，但不等同。海盗义与作品义是比喻延伸，要从搭配判断当前所指。',practice='分别解释 a pirate、software piracy、antipiracy patrols，并说明词性和语境怎样改变。',words=[w for w in family if w in keep],exclude=excluded,sources=['https://www.etymonline.com/word/pirate','https://www.etymonline.com/word/piracy'])]
assert keep==set(family)-set(excluded)
assert all(w['word']in m['owned_words']for w in W)
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history']),w['word']
for k,d in [('roots',ROOT),('words',W)]: (OUT/f'{k}_batch200_spec_128_pir.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C1047',len(W),'new',sum(len(w['examples'])for w in W),'examples')
