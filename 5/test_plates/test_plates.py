from plates import is_valid


def test_startwith_two_charakters():
    assert is_valid("aLoT12") == True
    assert is_valid("a1234") == False
    assert is_valid("AEI352") == True


def test_maximum_minimim_charatkers():
    assert is_valid("A") == False
    assert is_valid("Hello, Newman") == False
    assert is_valid("abc1234") == False
    assert is_valid("ABC123") == True


def test_numbers_no_middle():
    assert is_valid("AB1C12") == False
    assert is_valid("L2k123") == False
    assert is_valid("a1S1") == False
    assert is_valid("aA12") == True


def test_no_marks():
    assert is_valid("AB 123") == False
    assert is_valid("jw4.2") == False
    assert is_valid("Kai123") == True
    assert is_valid("Kai, 1") == False

def test_zero_start():
    assert is_valid("abc012") == False
    assert is_valid("id0123") == False
    assert is_valid("id1234") == True