from working import convert
import pytest

def test_valueerror():
    with pytest.raises(ValueError):
        convert("9 AM - 11 PM")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9 AM 10 PM")
    with pytest.raises(ValueError):
        convert("9:70 AM to 8:63 PM")

def test_am_hours():
    assert convert("9 AM to 10 AM") == "09:00 to 10:00"
    assert convert("9:00 AM to 10:30 AM") == "09:00 to 10:30"

def test_pm_hours():
    assert convert("9:45 PM to 10:45 PM") == "21:45 to 22:45"
    assert convert("10:30 AM to 1:35 PM") == "10:30 to 13:35"

def test_hour_conversion():
    assert convert("1:00 PM to 9:00 PM") == "13:00 to 21:00"
    assert convert("2:00 PM to 8:00 PM") == "14:00 to 20:00"

def test_minute_conversion():
    assert convert("1:27 PM to 10:26 PM") == "13:27 to 22:26"
    assert convert("5:52 AM to 8:36 PM") == "05:52 to 20:36"