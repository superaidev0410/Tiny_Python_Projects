"""
Purpose: test hello program
"""

from hello import say_hello


def test_hello():
    """
    test hello
    """

    hello_msg = say_hello('Tom')
    assert hello_msg == 'Hello, Tom!'
