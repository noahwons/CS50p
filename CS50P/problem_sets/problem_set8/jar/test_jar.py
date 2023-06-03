from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar(1)
        jar.deposit(4)



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.cookies == 10
    jar.deposit(1)
    assert jar.cookies == 11
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.cookies == 5
    jar.withdraw(2)
    assert jar.cookies == 3