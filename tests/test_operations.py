import pytest

from calculator.operations import add, div, mul, sub


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_sub():
    assert sub(5, 2) == 3
    assert sub(0, 5) == -5


def test_mul():
    assert mul(3, 4) == 12
    assert mul(-2, 5) == -10


def test_div():
    assert div(10, 2) == 5
    assert div(1, 4) == 0.25


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
def test_chained_operations_via_python_api():
    assert mul(add(2, 3), 4) == 20
    assert div(sub(10, 4), 2) == 3
