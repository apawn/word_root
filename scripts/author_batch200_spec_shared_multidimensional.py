# -*- coding: utf-8 -*-
"""Shared multidimensional record: multi and mensur families."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1]
W=[E('multidimensional','英 /ˌmʌltidaɪˈmenʃənəl/、/ˌmʌltidɪˈmenʃənəl/；美也读 /ˌmʌltaɪdɪˈmenʃənəl/','多维的；涉及多个方面的','同一件事要沿几条不同的轴去看，不能只用一个数字或一个角度说清。','英语 multi- “多” + dimensional “维度的”；dimensional 来自 dimension，远接拉丁 dīmēnsiō“测量”。不是把 modern dimension 中的 di- 当成“二”再加上“多”。',[['拉丁 dīmētīrī → dīmēnsiō → 英语 dimension','测量 → 测量、大小；后来表示维度、方面'],['并列构词来源：拉丁 multus → 英语 multi-','多，多个'],['英语 multi- + dimensional → multidimensional','具有多个维度；需要从多个方面考虑']],'数学和数据分析中，每个维度可对应一个独立坐标或变量；不必想象成看得见的房间方向。说 poverty is multidimensional，是说贫困还涉及教育、健康、居住等方面，不能只看收入。多维也不自动等于“至少四维”，具体维数由语境说明。','multidimensional data；a multidimensional problem；a multidimensional character。','multifaceted 也说多方面，常像观察物体的不同侧面；multidimensional 更容易让人想到几个可独立变化的轴。两者在日常评论里可接近，数学中不能随意互换。',('The survey treats quality of life as a multidimensional concept.','这项调查把生活质量看作涉及多个方面的概念。'),('Each row is a point in a multidimensional space, with one coordinate for each measurement.','每一行都是多维空间中的一个点，每项测量对应一个坐标。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/multidimensional','https://www.etymonline.com/word/dimension','https://en.wiktionary.org/wiki/multidimensional#English'])]
p=BASE/'.cache/batch200/drafts/rewrite_spec/words_batch200_spec_shared_multidimensional.json'
p.write_text(json.dumps(W,ensure_ascii=False,indent=2))
print('multidimensional: 1 word / 2 examples')
