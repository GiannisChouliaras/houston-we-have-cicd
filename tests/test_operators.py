import pytest
from operators import add, subtract, multiply, divide


def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 7) == -7


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(8, 2) == 4
    with pytest.raises(ValueError):
        divide(8, 0)
