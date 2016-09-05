"""
Purpose: test howler
"""

import os
from howler import convert


def test_text2text():
    """
    test converting text to text
    """

    output = convert('How dare you steal that car!', 'stdout')
    assert output == 'HOW DARE YOU STEAL THAT CAR!'


def test_text2file():
    """
    test converting text to file
    """

    # test function runs successfuly
    output = convert('How dare you steal that car!', 'out_test1.txt')
    assert output == 'success'

    # test file exists
    assert os.path.exists('out_test1.txt') is True

    # teset file content
    with open('out_test1.txt', 'r', encoding='utf8') as output_file:
        assert output_file.read() == 'HOW DARE YOU STEAL THAT CAR!'


def test_file2text():
    """
    test converting file to text
    """

    # test input file exists
    assert os.path.exists('in.txt') is True

    with open('in.txt', 'r', encoding='utf8') as input_file:
        input_text = input_file.read()

    # test function runs successfuly
    output = convert(input_text, 'stdout')
    assert output == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'


def test_file2file():
    """
    test converting file to file
    """

    # test input file exists
    assert os.path.exists('in.txt') is True

    with open('in.txt', 'r', encoding='utf8') as input_file:
        input_text = input_file.read()

    # test function runs successfuly
    output = convert(input_text, 'out_test2.txt')
    assert output == 'success'

    # test file exists
    assert os.path.exists('out_test2.txt') is True

    # teset file content
    with open('out_test1.txt', 'r', encoding='utf8') as output_file:
        assert output_file.read() == 'HOW DARE YOU STEAL THAT CAR!'
