"""
Purpose: Bring foods for picnic
"""

import argparse


def parse_args():
    """
    parse command-line arguments

    @returns: command-line arguments
    """

    parser = argparse.ArgumentParser(description='Bring foods for picnic')
    parser.add_argument('foods', help='foods to bring', nargs='+')
    parser.add_argument('-s', '--sorted', help="sort foods", action='store_true')
    return parser.parse_args()


def bring(foods, is_sort=False):
    """
    message to bring foods for picnic

    @param foods: foods to bring
    
    @returns: message
    """

    if is_sort:
        foods.sort()
    
    cnt = len(foods)
    if cnt == 1:
        return f"You are bringing {foods[0]}"
    elif cnt == 2:
        return f"You are bringing {foods[0]} and {foods[1]}"
    else:
        return 'You are bringing ' + ', '.join(foods[:-1]) + f', and {foods[-1]}.'


def main():
    """
    main function
    """

    args = parse_args()
    print(bring(args.foods, args.sorted))


if __name__ == '__main__':
    main()
