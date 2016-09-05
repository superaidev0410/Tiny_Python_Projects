"""
Purpose: Making all the letters uppercase.
"""

import argparse
import os


def parse_args():
    """
    parse command-line arguments
    """

    parser = argparse.ArgumentParser(description='Making all the letters uppercase')
    parser.add_argument('-o', '--output', default='stdout', help='name of output file')
    parser.add_argument('input', help='input text or file')
    return parser.parse_args()


def convert(input_data, output):
    """
    Convert all the letters uppercase

    @param input_data: input text or file
    @param output: ouput text or file

    @returns: output text or 'success' in case of output is file
    """

    # get input text
    text = input_data
    if os.path.isfile(input_data):
        with open(input_data, 'r', encoding='utf8') as input_file:
            text = input_file.read()

    text = text.upper()

    # output text
    if output == 'stdout':
        return text
    with open(output, 'w', encoding='utf8') as output_file:
        output_file.write(text)
    return 'success'


def main():
    """
    main function
    """

    args = parse_args()
    print(convert(args.input, args.output))


if __name__ == '__main__':
    main()
