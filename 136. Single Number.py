class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for no in nums:
            res ^= no

        return res