class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        c = 0

        for i in range(32):
            c = 0
            for num in nums:
                c += (num >> i) & 1

            if c % 3 != 0:
                res |= (1 << i)

        if res >= (1 << 31):
            res -= (1 << 32)

        return res