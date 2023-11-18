from fuel import gauge, convert
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"