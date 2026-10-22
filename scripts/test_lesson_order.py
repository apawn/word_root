"""Reading-order regressions: preserve families without inventing genealogy."""
import unittest

from lesson_order import make_relations, order_family


def arrange(names, splits=None, lexicon=None):
    authored = {w: {'split': (splits or {}).get(w, '')} for w in names}
    relations = make_relations(authored, lexicon or {})
    return order_family(names, relations)


class ReadingOrderTests(unittest.TestCase):
    def assert_grouped(self, names, expected_members):
        ordered, groups, _ = arrange(names)
        self.assertEqual(set(ordered), set(names))
        self.assertEqual(len(ordered), len(names))
        self.assertTrue(any(set(group) == set(expected_members) for group in groups))
        return ordered

    def test_frequency_does_not_separate_differ_extensions(self):
        order = self.assert_grouped(
            ['different', 'offer', 'conference', 'difference', 'reference',
             'differently', 'differ', 'differentiate', 'differentiation'],
            ['differ', 'different', 'difference', 'differently',
             'differentiate', 'differentiation'])
        self.assertLess(order.index('differ'), order.index('different'))
        self.assertLess(order.index('different'), order.index('difference'))
        self.assertLess(order.index('differentiate'), order.index('differentiation'))

    def test_nested_extensions_remain_contiguous(self):
        order, groups, parents = arrange(
            ['profitable', 'unprofitable', 'profitability', 'profitably', 'profit',
             'offer', 'offering'])
        profit_group = next(group for group in groups if 'profit' in group)
        self.assertEqual(profit_group[0], 'profit')
        self.assertEqual(order[order.index('profit'):order.index('profit')+len(profit_group)], profit_group)
        self.assertLess(order.index('profit'), order.index('profitable'))
        self.assertLess(order.index('profitable'), order.index('profitability'))
        for child, row in parents.items():
            self.assertLess(order.index(row['base']), order.index(child))

    def test_simple_word_starts_its_family_even_when_less_frequent(self):
        order = self.assert_grouped(['conference', 'conferencing', 'confer', 'offer'],
                                   ['confer', 'conference', 'conferencing'])
        self.assertLess(order.index('confer'), order.index('conference'))

    def test_negative_and_spelling_changes(self):
        self.assert_grouped(['fertility', 'infertility', 'fertile', 'fertilize',
                             'fertilizer', 'fertilization', 'infertile', 'offer'],
                            ['fertile', 'fertility', 'fertilize', 'fertilizer',
                             'fertilization', 'infertile', 'infertility'])

    def test_irregular_forms(self):
        order = self.assert_grouped(['mistakenly', 'mistake', 'taken', 'take',
                                    'mistaken', 'undertake', 'undertaking'],
                                   ['mistakenly', 'mistake', 'taken', 'take',
                                    'mistaken', 'undertake', 'undertaking'])
        self.assertLess(order.index('take'), order.index('taken'))
        self.assertLess(order.index('mistake'), order.index('mistaken'))

    def test_not_just_a_matching_string(self):
        _, groups, _ = arrange(['state', 'station', 'statistic', 'statist',
                               'specie', 'species', 'special', 'specially',
                               'crisis', 'critic', 'copy', 'copious'])
        for a, b in [('state', 'station'), ('statist', 'statistic'),
                     ('specie', 'special'), ('specie', 'species'),
                     ('crisis', 'critic'), ('copy', 'copious')]:
            self.assertFalse(any(a in group and b in group for group in groups), (a,b))

    def test_foreign_operands_cannot_be_read_as_english_bases(self):
        lex = {'special': [{'etymology_templates': [
            {'name': 'suffix', 'args': {'1': 'en', 'lang1': 'la', '2': 'species', '3': 'al'}}]}]}
        _, _, parents = arrange(['species', 'special'], lexicon=lex)
        self.assertNotIn('special', parents)

    def test_cycles_in_dictionary_analyses_are_resolved(self):
        lex = {a: [{'etymology_templates': [{'name': 'affix',
                'args': {'1': 'en', '2': b, '3': '-y'}}]}]
               for a,b in [('choice','choose'),('choose','choice')]}
        ordered, _, parents = arrange(['choice', 'choose'], lexicon=lex)
        self.assertEqual(set(ordered), {'choice', 'choose'})
        self.assertEqual(len(parents), 1)

    def test_repeat_generation_has_same_order(self):
        original = ['offering', 'conference', 'offer', 'confer', 'different', 'differ']
        first, _, _ = arrange(original)
        second, _, _ = arrange(first)
        self.assertEqual(first, second)

    def test_shorter_form_is_not_attached_to_an_abstract_expansion(self):
        _, _, parents = arrange(['archaic', 'archaism', 'mechanic', 'mechanism'])
        self.assertNotEqual(parents.get('archaic', {}).get('base'), 'archaism')
        self.assertNotEqual(parents.get('mechanic', {}).get('base'), 'mechanism')


if __name__ == '__main__':
    unittest.main()
