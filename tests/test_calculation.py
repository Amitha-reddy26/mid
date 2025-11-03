from app.calculation import Calculation

def test_repr():
    c = Calculation("add", 3, 3, 6)
    assert repr(c) == "add(3, 3) = 6"