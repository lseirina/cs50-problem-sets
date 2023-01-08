
"""
from fuel import convert, gauge

import pytest
def main():

    test_fruction()   
    test_valueerror()
    test_zerodivision()

def test_fruction():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("1/100") == 1 and gauge(1) == "E"
        
def test_valueerror():
    with pytest.raises(ValueError):
        convert("cat/dog") 

def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert(1/0)
"""

from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75

def test_erros():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    gauge(99) == "F"
    gauge(1) == "E"
    gauge(25) == "25%"