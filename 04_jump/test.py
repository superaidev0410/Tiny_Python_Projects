"""
Purpose: test jump
"""

from jump import encode


def test_encode():
    """
    test encode function
    """

    msg = encode('Call 1-800-329-8044 today!')
    assert msg == 'Call 9-255-781-2566 today!'
