from numb3rs import validate


def test_Invalid():
    assert validate("How are youd doing today? ") == False
    assert validate('125-125-243-234') == False
    assert validate('123.234.34.-6') == False
    assert validate('174.23.34.256') == False


def test_CS50():
    assert validate('255.255.255.255') == True
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False


def test_Valid():
    assert validate('123.123.123.123') == True
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True
    assert validate('145.0.4.64') == True
