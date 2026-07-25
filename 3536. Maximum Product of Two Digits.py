class Solution:
    def maxProduct(self, n: int) -> int:
        lst = [int(i) for i in str(n)]
        lst.sort()
        return lst[-2] * lst[-1]