from working import convert
import pytest


def test_ValueError():
    with pytest.raises(ValueError):
        convert("30:00 AM to 30 PM")
        convert("9:00 PM to 5:30 AM")
        convert("300 AM to 30 PM")
        convert("9:00 PM 10 AM")
        convert("9:60 AM to 5:60 PM")
        convert("9 AM - 5 PM")
        convert("09:00 AM - 17:00 PM")
        convert("9:00 PM10 AM")
        convert('9:100 AM to 5:00 PM')
        convert("9 AM 5 PM")
        convert("9 AM 5 PM")


def test_range():
    with pytest.raises(ValueError):
        convert("13:20 AM to 15:10 PM")
        convert("14:80 PM to 11:50 AM")
        convert("13:30 PM to 11:50 AM")
        convert("15:30 PM to 23:30 AM")
        convert("64:30 AM to 9:30 PM")


def test_omits():
    with pytest.raises(ValueError):
        convert("11:00 AM 5:10 PM")
        convert("4:30 5:10")
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    with pytest.raises(ValueError):
        convert("13 AM to 6 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    assert convert("9:59 AM to 12:59 PM") == "09:59 to 12:59"


def test_with_colon():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("4:00 AM to 10:00 PM") == "04:00 to 22:00"


def test_without_colon():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
