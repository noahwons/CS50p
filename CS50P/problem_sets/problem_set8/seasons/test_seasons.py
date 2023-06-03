import pytest
from datetime import date
from seasons import is_valid, days_to_words

def test_Value_Error():
    with pytest.raises(ValueError):
        is_valid("11111-111-111")
        is_valid("111-111-111")
        is_valid("1990-300-300")
