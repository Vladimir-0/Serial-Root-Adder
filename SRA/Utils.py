from math import sqrt


def sqrt_sum(amount: int) -> int:
    return sum(int(sqrt(i)) for i in range(0, amount))
