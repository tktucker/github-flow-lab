import pytest

from calculator.operations import add, div, mod, mul, sub


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

def test_mod():
    assert mod(10, 3) == 1

def test_mod_by_zero():
    with pytest.raises(ZeroDivisionError):
        mod(1, 0)
