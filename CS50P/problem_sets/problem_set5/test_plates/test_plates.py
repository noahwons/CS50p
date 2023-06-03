# TODO: Implement functioning first two chars ara alphabetical test
from plates import is_valid

def test_four_digits():
    assert is_valid("CS50") == True
    assert is_valid("C50S") == False

def test_six_plus_digits():
    assert is_valid("CS55CS") == False
    assert is_valid("CS55555") == False

def test_first_two_chars():
    assert is_valid("CS50") == True
    assert is_valid("..50") == False
    assert is_valid("1250") == False

def test_alpha():
    assert is_valid("66666A") == False
    assert is_valid("55555A") == False
    assert is_valid("66666") == False

def test_punctuation():
    assert is_valid("CS.50") == False
    assert is_valid("CS50?") == False

def test_zero_placement():
    assert is_valid("CS05") == False
