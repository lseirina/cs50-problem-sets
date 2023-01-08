"""

from bank import value

def test_value():
    assert value("hello") == "$0"
    assert value("hi") == "$20"
    assert value("Good morning") == "$100"


def test_value_lower_():
    assert value("HELLO") == "$0"

"""




from bank import value

def test_str():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100