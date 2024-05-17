import pytest

from numb3rs import validate

def main():
    test_rangen()
    test_alpha()
    test_input()
    test_length()


def test_rangen():
    assert validate("256.256.256.256") == False
    assert validate("512.512.512.512") == False
    assert validate("255.255.255.255") == True


def test_alpha():
    assert validate("cat") == False
    assert validate("dog") == False
    assert validate("hello") == False


def test_input():
    assert validate("127.0.0.1") == True
    assert validate("234.2.3.28") == True


def test_lenght():
    assert validate("0.0.0.0") == True
    assert validate("10.10.10.10") == True
    assert validate("100.100.100.100") == True
    assert validate("1000.1000.1000.1000") == False


if __name__ == "__main__":
    main()
