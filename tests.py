import unittest
from numonic import word_to_number


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


if __name__ == '__main__':
    unittest.main()
