from twttr import shorten

def main():
    test_letters()
    test_numbers()
    test_punct()
    test_capital()

def test_letters():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""


def test_numbers():
    assert shorten("1") == "1"
    assert shorten("-1") == "-1"


def test_punct():
    assert shorten("!@#$") == "!@#$"


def test_capital():
    assert shorten("CAAPTE") == "CPT"


if __name__ == "__main__":
    main()
