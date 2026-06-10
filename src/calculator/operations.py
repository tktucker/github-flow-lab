"""Basic arithmetic operations.

This module is intentionally small. Exercises will have you add operations
(mod, pow), introduce a bug, fix the bug, and create merge conflicts here.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

def sub(a: float, b: float) -> float:
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def mod(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return a % b
