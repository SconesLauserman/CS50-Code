from seasons import get
import pytest

def test_CS50():
    assert get('2022-06-30') == 'Five hundred twenty-five thousand, six hundred minutes'
    assert get('2021-06-30') == 'One million, fifty-one thousand, two hundred minutes'


def test_Invalid():
    with pytest.raises(SystemExit):
        get('cat')
        get('January 1, 1999')
        get('243-12-05')
        get('1999-2-12')
