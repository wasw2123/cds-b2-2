def remainder(a: int, b: int) -> int:
    """두 정수를 나눈 나머지를 반환합니다.

    Args:
        a (int): 나누어지는 수.
        b (int): 나누는 수.

    Returns:
        int: a를 b로 나눈 나머지 (a % b). 결과의 부호는 b의 부호를 따릅니다.
            예: remainder(-7, 2) == 1, remainder(7, -2) == -1

    Raises:
        ZeroDivisionError: b가 0인 경우.
    """
    return a % b
