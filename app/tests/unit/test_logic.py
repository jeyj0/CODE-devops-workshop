from unittest import TestCase
from calculator.logic import Calculator
import pytest

class CalculatorTests(TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_mul_with_5_and_10(self):
        assert self.calculator.mul(5, 10) == 50

    def test_mul_with_two_positive_numbers(self):
        assert self.calculator.mul(3, 7) == 21

    def test_mul_with_two_negative_numbers(self):
        assert self.calculator.mul(-8, -4) == 32

    def test_mul_with_one_positive_and_one_negative_number(self):
        assert self.calculator.mul(6, -3) == -18

    def test_mul_raises_ValueError_if_a_too_high(self):
        with pytest.raises(ValueError):
            self.calculator.mul(1001, 2)

    def test_mul_raises_ValueError_if_a_too_low(self):
        with pytest.raises(ValueError):
            self.calculator.mul(-1001, 2)

    def test_mul_raises_ValueError_if_b_too_high(self):
        with pytest.raises(ValueError):
            self.calculator.mul(2, 1001)

    def test_mul_raises_ValueError_if_b_too_low(self):
        with pytest.raises(ValueError):
            self.calculator.mul(2, -1001)

    def test_div_with_two_positive_numbers(self):
        assert self.calculator.div(10, 5) == 2
    
    def test_div_with_two_negative_numbers(self):
        assert self.calculator.div(-20, -5) == 4

    def test_div_with_one_negative_and_one_positive(self):
        assert self.calculator.div(-30, 5) == -6

    def test_div_raises_ValueError_a_too_high(self):
        with pytest.raises(ValueError):
            self.calculator.div(1001, 2)

    def test_div_raises_ValueError_b_too_high(self):
        with pytest.raises(ValueError):
            self.calculator.div(2, 1001)

    def test_div_raises_ValueError_a_too_low(self):
        with pytest.raises(ValueError):
            self.calculator.div(-1001, 2)

    def test_div_raises_ValueError_b_too_low(self):
        with pytest.raises(ValueError):
            self.calculator.div(2, -1001)

    def test_div_raises_divide_by_zero_exception(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.div(2, 0)
