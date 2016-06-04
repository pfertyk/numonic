import unittest
from numonic import word_to_number, get_all_matching_words, get_groups


class NumonicTestCase(unittest.TestCase):
    def test_ignore_vowels_and_y(self):
        word = 'aeiouy'
        self.assertEqual(word_to_number(word), '')

    def test_ignore_letters_with_diacritics(self):
        word = 'ąćęłńóśźż'
        self.assertEqual(word_to_number(word), '')

    def test_ignore_case(self):
        number = word_to_number('bB')
        self.assertEqual(len(number), 2)
        self.assertEqual(len(set(number)), 1)

    def test_default_mapping(self):
        words = [
            'hello', 'hakka', 'shirt', 'other', 'ghoul', 'jelly', 'jello',
            'jellx', 'foobar', 'pumba', 'timon', 'there', 'badly', 'coded'
        ]
        self.assertEqual(
            set(get_all_matching_words('344', words)),
            {'hello', 'hakka', 'jelly', 'jello'}
        )

    def test_split_into_groups(self):
        words = [
            'hello', 'world', 'foobar', 'yep', 'Poe', 'queue', 'pay', 'lion',
            'keen', 'Alan', 'badge', 'bodega'
        ]
        groups = get_groups('123456', words)
        self.assertEqual(len(groups), 3)
        self.assertEqual(set(groups[0]), {'badge', 'bodega'})
        self.assertEqual(set(groups[1]), {'Alan', 'keen', 'lion'})
        self.assertEqual(set(groups[2]), {'yep', 'queue', 'Poe', 'pay'})

    def test_number_starting_with_zero(self):
        words = ['zacd', 'zzabf', 'abd']
        self.assertEqual(set(get_all_matching_words('012', words)), {'zacd'})


if __name__ == '__main__':
    unittest.main()
