import unittest
from src.multiplier import multiplier


class TestMultiplier(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiplier(2, 3), 6)
        self.assertEqual(multiplier(10, 5), 50)

    def test_multiplication_with_zero(self):
        self.assertEqual(multiplier(0, 5), 0)
        self.assertEqual(multiplier(5, 0), 0)
        self.assertEqual(multiplier(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiplier(-2, 3), -6)
        self.assertEqual(multiplier(2, -3), -6)
        self.assertEqual(multiplier(-4, -5), 20)

    def test_multiplication_with_one(self):
        self.assertEqual(multiplier(1, 42), 42)
        self.assertEqual(multiplier(42, 1), 42)


if __name__ == "__main__":
    unittest.main()
