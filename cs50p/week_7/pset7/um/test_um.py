import pytest


from um import count


def main():
    test_char_plus_um()
    test_um_alphanumeric()
    test_words_wth_um()
    test_wrg_input()
    test_case_insensitive()


def test_char_plus_um():
    assert count("um...") == 1
    assert count("um---") == 1
    assert count("um***") == 1


def test_um_alphanumeric():
    assert count("um1") == 0
    assert count("0um") == 0


def test_words_wth_um():
    assert count("yum") == 0
    assert count("yummy") == 0


def test_wrg_input():
    assert count("cat") == 0
    assert count("dog") == 0
    assert count("duck") == 0


def test_case_insensitive():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1


if __name__ == "__main__":
    main()
