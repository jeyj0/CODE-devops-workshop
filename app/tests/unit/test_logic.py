from unittest import TestCase
from calculator.logic import Calculator
import pytest

class CalculatorTests(TestCase):
    def test_mul_with_5_and_10(self):
        calculator = Calculator()
        assert calculator.mul(5, 10) == 50

    def test_mul_with_two_positive_numbers(self):
        calculator = Calculator()
        assert calculator.mul(3, 7) == 21

    def test_mul_with_two_negative_numbers(self):
        calculator = Calculator()
        assert calculator.mul(-8, -4) == 32

    def test_mul_with_one_positive_and_one_negative_number(self):
        calculator = Calculator()
        assert calculator.mul(6, -3) == -18

    def test_mul_raises_ValueError_if_a_too_high(self):
        calculator = Calculator()
        with pytest.raises(ValueError):
            calculator.mul(1001, 2)

    def test_mul_raises_ValueError_if_a_too_low(self):
        calculator = Calculator()
        with pytest.raises(ValueError):
            calculator.mul(-1001, 2)

    def test_mul_raises_ValueError_if_b_too_high(self):
        calculator = Calculator()
        with pytest.raises(ValueError):
            calculator.mul(2, 1001)

    def test_mul_raises_ValueError_if_b_too_low(self):
        calculator = Calculator()
        with pytest.raises(ValueError):
            calculator.mul(2, -1001)

    def test_div(self):
        pass
