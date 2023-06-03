from fuel import gauge
from fuel import convert
import pytest

def test_convert_number():
    assert convert("3/4") == 75.0
    assert convert("1/4") == 25.0
    assert convert("0/4") == 0.0
    with pytest.raises(ValueError):
        assert convert("cat/cat")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_guage():
    assert gauge(99.0) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"