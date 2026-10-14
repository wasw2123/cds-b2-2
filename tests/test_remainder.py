import unittest
from src.remainder import remainder


class TestRemainder(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(remainder(7, 2), 1)
        self.assertEqual(remainder(10, 3), 1)

    def test_exact_division(self):
        self.assertEqual(remainder(10, 5), 0)
        self.assertEqual(remainder(0, 5), 0)

    def test_dividend_smaller_than_divisor(self):
        self.assertEqual(remainder(3, 5), 3)

    def test_negative_numbers(self):
        self.assertEqual(remainder(-7, 2), 1)
        self.assertEqual(remainder(7, -2), -1)
        self.assertEqual(remainder(-7, -2), -1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            remainder(5, 0)


if __name__ == "__main__":
    unittest.main()
