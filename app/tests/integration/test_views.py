from unittest import TestCase
from ..base import TestClient
from calculator.app import app


class ViewTests(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = TestClient(app)

    def test_multiply(self):
        r = self.client.get("/calc/3*10")
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.body, "30")

    def test_multiply_value_error(self):
        r = self.client.get("/calc/1100*3")
        self.assertEquals(r.status_code, 403)
        self.assertEquals(r.body, "Too big or too small value passed.")

    def test_divide(self):
        r = self.client.get("/calc/6/2")
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.body, "3")

    def test_divide_value_error(self):
        r = self.client.get("/calc/5/2000")
        self.assertEquals(r.status_code, 403)
        self.assertEquals(r.body, "Too big or too small value passed.")

    def test_divide_divide_zero_error(self):
        r = self.client.get("/calc/1/0")
        self.assertEquals(r.status_code, 403)
        self.assertEquals(r.body, "integer division or modulo by zero")
