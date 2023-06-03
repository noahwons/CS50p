from twttr import shorten
import pytest

def test_str():
    assert shorten("hello") == "hll"
    assert shorten("noah") == "nh"
    assert shorten("NOAH") == "NH"

def test_int():
    assert shorten("1") == "1"
    assert shorten("0") == "0"
    assert shorten("-1") == "-1"

def test_punctuation():
    assert shorten("hello, noah") == "hll, nh"

def test_valueerror():
    with pytest.raises(TypeError):
        shorten(1)
