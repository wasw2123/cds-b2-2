import unittest
from src.quotient import quotient
from src.remainder import remainder


class TestDivisionConsistency(unittest.TestCase):
    """몫(quotient)과 나머지(remainder)가 나눗셈 정리를 만족하는지 검증합니다.

    모든 정수 a와 0이 아닌 정수 b에 대해 다음이 성립해야 합니다.
    - quotient(a, b) * b + remainder(a, b) == a
    - abs(remainder(a, b)) < abs(b)
    """

    CASES = [
        (7, 2),
        (-7, 2),
        (7, -2),
        (-7, -2),
        (10, 5),
        (0, 3),
        (3, 5),
        (-1, 3),
    ]

    def test_division_identity(self):
        for a, b in self.CASES:
            with self.subTest(a=a, b=b):
                self.assertEqual(quotient(a, b) * b + remainder(a, b), a)

    def test_remainder_smaller_than_divisor(self):
        for a, b in self.CASES:
            with self.subTest(a=a, b=b):
                self.assertLess(abs(remainder(a, b)), abs(b))

    def test_remainder_sign_follows_divisor(self):
        for a, b in self.CASES:
            with self.subTest(a=a, b=b):
                r = remainder(a, b)
                if r != 0:
                    self.assertEqual(r > 0, b > 0)


if __name__ == "__main__":
    unittest.main()
