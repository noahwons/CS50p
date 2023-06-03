import pytest
from numb3rs import validate

def test_whitespace():
    assert validate("127.0.0.1") == True
    assert validate("127.127. 127.0") == False

def test_letters():
    assert validate("cat") == False
    assert validate("255.cat.cat.255") == False

def test_validation():
    assert validate("275.255.255.0") == False
    assert validate("-1,-1,-1,-1") == False

def test_length():
    assert validate("10.10.10.10.10") == False
    assert validate("1.1.1.1.1.1.1.1.1.1") == False
    assert validate("1.1") == False
    assert validate("1.1.1.1") == True

def test_byte():
    assert validate("127.275.275.275") == False
    assert validate("275.275.275.127") == False