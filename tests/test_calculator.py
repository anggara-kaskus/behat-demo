import unittest
from classes.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 5), 5)
        self.assertEqual(Calculator.subtract(-1, 1), -2)
        self.assertEqual(Calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 7), 21)
        self.assertEqual(Calculator.multiply(-1, 1), -1)
        self.assertEqual(Calculator.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
        self.assertEqual(Calculator.divide(-1, 1), -1)
        self.assertEqual(Calculator.divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

    def test_power(self):
        self.assertEqual(Calculator.power(2, 3), 8)
        self.assertEqual(Calculator.power(5, 0), 1)
        self.assertEqual(Calculator.power(-2, 2), 4)
        self.assertEqual(Calculator.power(2, -2), 0.25)

if __name__ == '__main__':
    unittest.main()
