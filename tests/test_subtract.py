from src.subtract import subtract


def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(3, 10) == -7
    assert subtract(5, 5) == 0


if __name__ == "__main__":
    test_subtract()
    print("모든 테스트 통과!")

    