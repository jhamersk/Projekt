def test_addition():
    assert 2 + 2 == 4


def test_subtraction():
    assert 5 - 3 == 2
    assert 0 - 1 == -1


def test_multiplication():
    assert 3 * 4 == 12
    assert 0 * 10 == 0


def test_division():
    assert 10 / 2 == 5


def test_modulo():
    assert 10 % 3 == 1
    assert 8 % 2 == 0


def add(a, b):
    return a + b


def test_add_function():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
