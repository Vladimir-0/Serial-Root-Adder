from math import sqrt


def sqrt_sum(amount: int) -> int:
    """
    Adds up roots rounded down to numbers from 1 to amount inclusive.
    :param amount: The amount of numbers to add.
    :return: The root sum.
    """
    return sum(int(sqrt(i)) for i in range(1, amount + 1))
