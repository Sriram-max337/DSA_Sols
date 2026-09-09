class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10**3:
            return 0
        elif n < 10**6:
            return n*1 - 1000 + 1
        elif n < 10**9:
            return n * 2 - 10**6 - 10**3 + 2
        elif n < 10**12:
            return n * 3 - 10**9 - 10**6 - 10**3 + 3
        elif n < 10**15:
            return n * 4 - 10**12 - 10**9 - 10**6 - 10**3 + 4
        elif n == 10**15:
            return 3998998998999005