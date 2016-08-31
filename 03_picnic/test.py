"""
Purpose: test picnic
"""

from picnic import bring


def test_one():
    """
    test bring one food
    """

    msg = bring(['salad'])
    assert msg == 'You are bringing salad.'


def test_two():
    """
    test bring two foods
    """

    msg = bring(['salad', 'chips'])
    assert msg == 'You are bringing salad and chips.'


def test_three():
    """
    test bring three foods
    """

    msg = bring(['salad', 'chips', 'bread'])
    assert msg == 'You are bringing salad, chips, and bread.'


def test_sort():
    """
    test sorting
    """

    msg = bring(['salad', 'chips', 'bread'], True)
    assert msg == 'You are bringing bread, chips, and salad.'
