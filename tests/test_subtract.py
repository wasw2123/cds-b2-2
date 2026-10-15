import unittest
from src.subtract import subtract


class TestSubtract(unittest.TestCase):
    def test_positive_result(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(20, 5), 15)
        self.assertEqual(subtract(100, 40), 60)

    def test_negative_result(self):
        self.assertEqual(subtract(3, 10), -7)
        self.assertEqual(subtract(5, 20), -15)
        self.assertEqual(subtract(10, 100), -90)

    def test_zero_result(self):
        self.assertEqual(subtract(5, 5), 0)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-10, -10), 0)

    def test_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-10, 5), -15)
        self.assertEqual(subtract(10, -5), 15)


if __name__ == "__main__":
    unittest.main()
