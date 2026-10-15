def quotient(a: int, b: int) -> int:
    """두 정수를 나눈 몫을 반환합니다.

    Args:
        a (int): 나누어지는 수.
        b (int): 나누는 수.

    Returns:
        int: a를 b로 나눈 몫 (a // b). 음수는 내림 기준입니다. 예: quotient(-7, 2) == -4

    Raises:
        ZeroDivisionError: b가 0인 경우.
    """
    return int(a / b)
