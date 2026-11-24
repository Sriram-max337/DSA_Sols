class Solution:
    def fib(self, n: int) -> int:
        HM = {}

        def fibonacci(x):
            if x == 0:
                return 0

            if x == 1:
                return 1

            if x not in HM:
                HM[x] = fibonacci(x - 1) + fibonacci(x - 2)

            return HM[x]

        return fibonacci(n)