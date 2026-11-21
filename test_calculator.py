import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(1000000, 20000000), 21000000)
    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(6, 4), 2)
        self.assertEqual(subtract(-6, -4), -2)
        self.assertEqual(subtract(3.14159, 0.14159), 3)
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 1), 0)
        self.assertEqual(logarithm(3.14159, 3.14159), 1)
        self.assertEqual(logarithm(10,100), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0,0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()