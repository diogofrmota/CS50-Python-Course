from bank import get_value

def test_get_value():
    assert get_value("Hello") == 0
    assert get_value(" Hello ") == 0
    assert get_value("Hello, Newman") == 0
    assert get_value("how you doing?") == 20
    assert get_value("What's happening?") == 100
    assert get_value("What's up?") == 100
    assert get_value("HELLO") == 0
    assert get_value("") == 100
    assert get_value(" H") == 20
    assert get_value("h") == 20
    assert get_value("hELLO") == 0
    assert get_value("  HELLO  ") == 0
