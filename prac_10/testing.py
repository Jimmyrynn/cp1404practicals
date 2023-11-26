"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # 1.
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # 2.
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Error"
    test_car = Car()
    assert test_car.fuel == 20, "Error"


run_tests()

# 3.
doctest.testmod()


# 5.
def phrase_to_sentence(phrase):
    sentence = phrase.capitalize()
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


print(phrase_to_sentence('hello'))
print(phrase_to_sentence('It is an ex parrot.'))
print(phrase_to_sentence('james is really really cool.'))
