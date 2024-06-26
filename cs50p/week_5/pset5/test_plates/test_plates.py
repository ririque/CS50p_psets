from plates import is_valid


def test_length():
    assert is_valid("AAA222") == True
    assert is_valid("AAAA222") == False
    assert is_valid("H") == False


def test_start():
    assert is_valid("HH") == True
    assert is_valid("11") == False
    assert is_valid("0") == False


def test_mid_plate():
    assert is_valid('CS50P') == False
    assert is_valid('CSP50') == True
    assert is_valid('CS05') == False


def test_punct():
    assert is_valid("PI3.!4") == False
