def remainder(a: int, b: int) -> int:
    """두 정수를 나눈 나머지를 반환합니다.

    Args:
        a (int): 나누어지는 수. Dividend.
        b (int): 나누는 수. Divisor.

    Returns:
        int: Dividend를 Divisor로 나눈 나머지 (Dividend % Divisor). 결과의 부호는 Divisor의 부호를 따릅니다.
            예: remainder(-7, 2) == 1, remainder(7, -2) == -1

    Raises:
        ZeroDivisionError: Divisor가 0인 경우.
    """

    dividend = a
    divisor = b

    return dividend % divisor
