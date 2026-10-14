from src.addition import add

# test 실행 python3 -m test.test_add

try:
    def test_add_int():
        assert add(1, 2) == 3
        assert add(100, 1) == 101
        print("test_add_int 성공")
    test_add_int()

    def test_add_nagative():
        assert add(1, -3) == -2
        assert add(-5, 100) == 95
        assert add(-1, -2) == -3
        print("test_add_nagative 성공")
    test_add_nagative()
    


except AssertionError:
    print("테스트 실패")
