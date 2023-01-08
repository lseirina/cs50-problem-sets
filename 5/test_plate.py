"""
from plate import is_valid

def main():
    test_is_valid()
    test_is_valid_num()
    test_is_valid_punctuation()

def test_is_valid():
    assert is_valid("HELLO") == True
    assert is_valid("hello") == False
    assert is_valid("HELLLOO") == False
def test_is_valid_num():   
    assert is_valid("3HELLO") == False
    assert is_valid("HELLO09") == False
    assert is_valid("CS50") == True

def test_is_valid_punctuation():
    assert is_valid("Hel,./") == False

if __name__ == "__main__":
    main()
    """


"""

from plate import is_valid
def main():
    test_len()
    test_upper()
    test_punctuation()
    test_digit()
    test_zero_is_not_the_first()

def test_len():
    assert is_valid("HELLO WORLD") == False
    assert is_valid("H") == False

def test_upper():
    assert is_valid("hello") == False

def test_punctuation():
    assert is_valid("HELLO,.") == False

def test_digit():
    assert is_valid("HEL89O") == False

def test_zero_is_not_the_first():
    assert is_valid("CS05") == False

if __name__ == "__main__":
    main()
    
"""
from plate import is_valid
import pytest

def main():
    test_max_min()
    test_begin_with_letters()
    test_zero()
    test_punctuation()

def test_max_min():
    assert is_valid("H") == False
    assert is_valid("HELLOTHERE") == False
    assert is_valid("HE") == True
    assert is_valid("HELLOO") == True

def test_begin_with_letters():
    assert is_valid("HE") == True
    assert is_valid("11") == False
    assert is_valid("1H") == False
    assert is_valid("H") == False

def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_numbers_placement():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_punctuation():
    assert is_valid("HE LL") == False
    assert is_valid("HE,LLO") == False
    assert is_valid("HE!LLO") == False

if __name__ in "__main__":
    main()