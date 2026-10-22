# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
B=[['古希腊 horman；horme','推动、激起；冲动、推动力'],['现代科学造词 hormone','引发生理反应的化学信号']]
W=[
E('hormone','英 /ˈhɔːməʊn/；美 /ˈhɔːrmoʊn/','激素；荷尔蒙','像体内传递消息的小信使：到达能识别它的细胞，就影响那里的活动。','现代术语由 Starling 于1905年引入，取希腊 horman 推动、激起相关形式；意思是促使某种活动发生的东西。',B,'hormone levels 是激素水平；growth hormone 是生长激素。人体激素参与多种调节，不只是青春期、性吸引或情绪；同一个“推动”活动的词源，也不表示所有激素都只会加速。','hormone levels；growth hormone；a hormone signal；produce hormones。','hormone 是信号物质，enzyme 是催化反应的酶，二者不能互换。激素能促进或抑制具体活动，词源只帮助记忆，并非完整机制说明。',('The lesson explains how hormones carry signals through the body.','这节课解释了激素如何在体内传递信号。'),('The study measured changes in hormone levels over time.','这项研究测量了激素水平随时间的变化。'),sources=['https://www.etymonline.com/word/hormone','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/hormone']),
E('hormonal','英 /hɔːˈməʊnəl/；美 /hɔːrˈmoʊnəl/','激素的；与激素有关的','说某个变化或过程和体内的化学信使有关，还没有单靠这个词交代全部原因。','hormone + -al，词尾 e 去掉；把激素这个名词变成表示关系的形容词。',B+[['hormone + -al → hormonal','与激素有关的']],'hormonal changes 是激素相关变化；hormonal regulation 是激素调节。口语里说某个人 is hormonal 有时暗指情绪受激素影响，但会显得武断或轻视，不能当作对人的认真解释。','hormonal changes；hormonal regulation；hormonal signals。','hormonal 是关系形容词，不等于所有情绪波动都由激素造成。准确理解时要看具体讨论的是哪种信号、哪种变化。',('The textbook describes hormonal regulation of growth.','课本介绍了激素对生长的调节。'),('Researchers compared hormonal changes in the two groups.','研究人员比较了两组的激素变化。'),sources=['https://en.wiktionary.org/wiki/hormonal','https://www.etymonline.com/word/hormone'])
]
ROOT=dict(id='C0569',meaning='推动；激起活动',core='HORM = SET IN MOTION',image='像一条通知传到对应部门，接收方开始改变活动；激素的名字抓住了这种推动反应的作用。',intro='来自希腊 horman“推动、激起”及相关名词 horme。现代英语最值得先掌握的是 hormone 与 hormonal。它们从促发活动的古典意象进入科学命名，不必把所有冷门哲学、生理学派生一起背下来。',forms='hormone 是现代科学造词，并非古希腊人已使用的现代生理学术语；hormonal 是英语加 -al。荷尔蒙是 hormone 的音译，激素是常用中文名称。',branches=[['化学信号物质','hormone'],['与激素相关','hormonal']],contrasts='激素不是专指性激素，也不等于酶。推动这一词源不能推出所有激素都只会使活动更快；现代概念要靠具体作用理解。',practice='The lesson links hormonal signals with changes in cell activity.\n\n这节课把激素信号与细胞活动的变化联系起来讲解。',words=[x['word'] for x in W],exclude={w:'较专业或低频的术语，本轮先掌握 hormone 及常用派生。' for w in ['horme','hormephobia','hormesis','hormetic','hormic']})
if __name__=='__main__':
 for name,data in [('roots_horm',[ROOT]),('words_horm',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
