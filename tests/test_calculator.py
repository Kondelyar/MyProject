import pytest
from src.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(10, 5) == 15

def test_divide_error():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)