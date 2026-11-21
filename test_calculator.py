# https://github.com/calevzak/lab10-CZ-MH.git
# Partner 1: Calev Zak
# Partner 2: Mitchel Horkheimer
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
#Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(1000000, 20000000), 21000000)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(6, 4), 2)
        self.assertEqual(subtract(-6, -4), -2)
        self.assertAlmostEqual(subtract(3.14159, 0.14159), 3)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 1), 0)
        self.assertAlmostEqual(logarithm(3.14159, 3.14159), 1)
        self.assertAlmostEqual(logarithm(10, 100), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 0)

#Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(13, 0), 0)
        self.assertEqual(mul(-4, -10), 40)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(-3, 15), -5)
        self.assertEqual(div(9, 27), 3)
        self.assertEqual(div(-25, -125), 5)
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,-4),5)
        self.assertAlmostEqual(hypotenuse(5,7),8.60232526)
        self.assertEqual(hypotenuse(20,21),29)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        with self.assertRaises(ValueError):
            square_root(-49)
        # Test basic function
        self.assertEqual(square_root(49), 7)
        self.assertEqual(square_root(144), 12)
        self.assertEqual(square_root(4), 2)

# Do not touch this
if __name__ == "__main__":
    unittest.main()