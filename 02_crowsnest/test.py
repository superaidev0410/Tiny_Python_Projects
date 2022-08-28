"""
Purpose: test crowsnest program
"""

from crowsnest import report


def test_consonant():
    """
    test consonant
    """

    msg = report('narwhal')
    assert msg == 'Ahoy, Captain, a narwhal off the larboard bow!'


def test_vowel():
    """
    test vowel
    """

    msg = report('octopus')
    assert msg == 'Ahoy, Captain, an octopus off the larboard bow!'
