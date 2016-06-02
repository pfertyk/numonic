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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--translate', action='store_true')
    parser.add_argument('words', metavar='word', type=str, nargs='+')
    args = parser.parse_args()

    if args.translate:
        number = args.words[0]
        wordfile = '/usr/share/dict/american-english'
        with open(wordfile) as file:
            for word in file:
                w = word.strip()
                if w.isalpha() and word_to_number(w) == number:
                    print(word.strip())
    else:
        print(word_to_number(''.join(args.words)))
