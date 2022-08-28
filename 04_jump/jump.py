"""
Purpose: exchange numbers in string
"""

import argparse


def parse_args():
    """
    parse command-line arguments

    @returns: command-line arguments
    """

    parser = argparse.ArgumentParser(description='exchange digits in string')
    parser.add_argument('text', help='text to encode', metavar='text')
    return parser.parse_args()


def encode(text):
    """
    encode text

    @param text: text to encode

    @returns: encoded text
    """

    jump_table = {'0':'5', '1':'9', '2':'8', '3':'7', '4':'6',
                  '5':'0', '6':'4', '7':'3', '8':'2', '9':'1'}
    res = ''
    for char in text:
        if char in jump_table:
            res += jump_table[char]
        else:
            res += char
    return res


def main():
    """
    main function
    """

    args = parse_args()
    print(encode(args.text))


if __name__ == '__main__':
    main()
