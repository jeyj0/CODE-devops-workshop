# encoding=utf-8


class ValueTooLowException(Exception):
    pass


class ValueTooHighException(Exception):
    pass


class Calculator(object):
    def __init__(self, min_value=-1000, max_value=1000):
        self.min_value = min_value
        self.max_value = max_value

    def checkValueValidities(self, a, b):
        if (a > self.max_value or a < self.min_value 
            or b > self.max_value or b < self.min_value):
            raise ValueError("Too big or too small value passed.")

    def mul(self, a, b):
        self.checkValueValidities(a, b)
        return a * b

    def div(self, a, b):
        self.checkValueValidities(a, b)
        return a / b
