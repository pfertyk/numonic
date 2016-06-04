import argparse
from itertools import zip_longest

letter_to_number = {
    'b': 1,
    'c': 1,
    'd': 2,
    'f': 2,
    'g': 3,
    'h': 3,
    'j': 3,
    'k': 4,
    'l': 4,
    'm': 5,
    'n': 5,
    'p': 6,
    'q': 6,
    'r': 7,
    's': 7,
    't': 8,
    'v': 8,
    'w': 9,
    'x': 9,
    'z': 0
}


def word_to_number(word):
    digits = []
    for letter in word.lower():
        if letter in letter_to_number:
            digits.append(letter_to_number[letter])
    return ''.join(str(digit) for digit in digits)


def get_all_matching_words(number, words):
    for word in words:
        if word_to_number(word) == number:
            yield word.strip()


def get_groups(number, words, min_matches=1):
    matching_groups = []
    words = list(words)
    while number:
        end = len(number)
        while True:
            matching_words = get_all_matching_words(number[:end], words)
            matching_words = list(matching_words)
            if len(matching_words) >= min_matches:
                matching_groups.append(matching_words)
                number = number[end:]
                break
            else:
                end -= 1

    return matching_groups


def print_groups(groups):
    row_parts = ['|']
    border_parts = ['+']
    for group in groups:
        max_word_len = max(len(word) for word in group)
        row_parts.append(' {{:{}}} |'.format(max_word_len))
        border_parts.extend(['-'*(max_word_len+2), '+'])
    row = ''.join(row_parts)
    border = ''.join(border_parts)
    print(border)
    for words in zip_longest(*groups, fillvalue=''):
        print(row.format(*words))
    print(border)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--decode', action='store_true')
    parser.add_argument('-m', '--min-matches', type=int, default=1)
    parser.add_argument('words', metavar='word', type=str, nargs='+')
    args = parser.parse_args()

    if args.decode:
        print(word_to_number(''.join(args.words)))
    else:
        number = ''.join(args.words)
        min_matches = args.min_matches
        wordfile = '/usr/share/dict/american-english'
        with open(wordfile) as words:
            groups = get_groups(number, words, min_matches)
            print_groups(groups)
