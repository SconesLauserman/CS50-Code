from twttr import shorten


def test_case():
    assert shorten("tWttR") == "tWttR"
    assert shorten("THiS iS Text") == "THS S Txt"
    assert shorten("aEiOUueAoI123") == "123"
    assert shorten("..123aehello") == "..123hll"
