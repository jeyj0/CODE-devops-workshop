from unittest import TestCase
from calculator.logic import Calculator


class CalculatorTests(TestCase):
    def test_mul_with_5_and_10(self):
        calculator = Calculator()
        assert calculator.mul(5, 10) == 50

    def test_div(self):
        pass
