from bank import value

def test_hellos():
    assert value("Hello, amigo") == 0
    assert value("hello, amigo") == 0


def test_hs():
    assert value("Hey, may I help you?") == 20
    assert value("How can I help today?") == 20


def test_no_h():
    assert value("What's popping?") == 100
    assert value("In what way I assist you") == 100



