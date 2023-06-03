from bank import value
import pytest

def test_upper_lower():
    assert value("HELLO NOAH") == 0
    assert value("HUNGRY") == 20
    assert value("CAT") == 100

def test_str():
    assert value("hello Noah") == 0
    assert value("hungry") == 20
    assert value("cat") == 100

def test_empty_string():
    assert value("") == 100
