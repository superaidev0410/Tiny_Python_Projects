"""
Purpose: Report an obstacle
"""

import argparse


def parse_args():
    """
    parse command-line arguments

    @returns: command-line arguments
    """

    parser = argparse.ArgumentParser(description='Report an obstacle')
    parser.add_argument('obstacle', help='name of obstacle')
    return parser.parse_args()


def report(obstacle):
    """
    message to report an obstacle

    @param obstacle: name of obstacle

    @returns: report message
    """

    word = 'an' if obstacle[0].lower() in 'aeiou' else 'a'
    return f'Ahoy, Captain, {word} {obstacle} off the larboard bow!'


def main():
    """
    main function
    """

    args = parse_args()
    print(report(args.obstacle))


if __name__ == '__main__':
    main()
