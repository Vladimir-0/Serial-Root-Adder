from math import sqrt


class Utils:
    @staticmethod
    def sqrt_sum(amount: int) -> int:
        return sum(int(sqrt(i)) for i in range(0, amount))
