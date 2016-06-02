import unittest
from numonic import word_to_number, get_all_matching_words


class NumonicTestCase(unittest.TestCase):
    def test_ignore_vowels_and_y(self):
        word = 'aeiouy'
        self.assertEqual(word_to_number(word), '')

    def test_ignore_letters_with_diacritics(self):
        word = 'ąćęłńóśźż'
        self.assertEqual(word_to_number(word), '')

    def test_ignore_case(self):
        word = 'bB'
        self.assertEqual(len(word_to_number(word)), 2)
        self.assertEqual(len(set(word_to_number(word))), 1)

    def test_default_mapping(self):
        word_list = [
            'hello', 'hakka', 'shirt', 'other', 'ghoul', 'jelly', 'jello',
            'jellx', 'foobar', 'pumba', 'timon', 'there', 'badly', 'coded'
        ]
        self.assertEqual(
            set(get_all_matching_words(344, word_list)),
            {'hello', 'hakka', 'jelly', 'jello'}
        )


if __name__ == '__main__':
    unittest.main()
