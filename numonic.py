import argparse

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--translate', action='store_true')
    parser.add_argument('words', metavar='word', type=str, nargs='+')
    args = parser.parse_args()

    if args.translate:
        number = ''.join(args.words)
        wordfile = '/usr/share/dict/american-english'
        with open(wordfile) as words:
            for group in get_groups(number, words, 3):
                print('='*10)
                for word in group:
                    print(word)
    else:
        print(word_to_number(''.join(args.words)))
