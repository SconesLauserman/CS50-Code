from bank import value


def test_start_h():
    assert value("Hi, what is youre name?") == 20
    assert value("how are you donig?") == 20
    assert value("hey, hows you're day going?") == 20


def test_start_hello():
    assert value("Hello, newman") == 0
    assert value("Hello") == 0
    assert value("Hello my friend") == 0


def test_else():
    assert value("so nice to meet you!") == 100
    assert value("Ive heard a lot about you") == 100
    assert value("well hello there") == 100
