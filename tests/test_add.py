import unittest

from src.addition import add


class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(100, 1), 101)

    def test_negative_numbers(self):
        self.assertEqual(add(1, -3), -2)
        self.assertEqual(add(-5, 100), 95)
        self.assertEqual(add(-1, -2), -3)

    def test_addition_with_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
