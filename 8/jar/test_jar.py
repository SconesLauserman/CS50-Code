from jar import Jar

def test_init():
    jar = Jar(15)
    assert jar._cookie == 0
    assert jar._capacity == 15


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(13)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(8)
    assert jar.size == 13


def test_withdraw():
    jar = Jar(8)
    jar.deposit(7)
    jar.withdraw(3)
    jar.withdraw(1)
    assert jar._cookie == 3
    jar.withdraw(3)