"""
Purpose: Say hello
"""

import argparse


def parse_args():
    """
    parse command-line arguments

    @returns: arguments
    """

    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument('-n', '--name', metavar='name', help='name to greet', default='World')
    return parser.parse_args()


def say_hello(name):
    """
    make hello message to name

    @param name: name to say hello

    @returns: hello message
    """

    return f'Hello, {name}!'


def main():
    """
    main function
    """

    args = parse_args()
    print(say_hello(args.name))


if __name__ == '__main__':
    main()
