import unittest
from src.quotient import quotient


class TestQuotient(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(quotient(7, 2), 3)
        self.assertEqual(quotient(10, 5), 2)

    def test_zero_dividend(self):
        self.assertEqual(quotient(0, 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(quotient(-7, 2), -4)
        self.assertEqual(quotient(7, -2), -4)
        self.assertEqual(quotient(-7, -2), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            quotient(5, 0)


if __name__ == "__main__":
    unittest.main()
