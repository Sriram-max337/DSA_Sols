class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sqr_sum = 0
        n = len(nums)

        for i in range(n):
            if n % (i+1) == 0:
                sqr_sum += (nums[i]**2)

        return sqr_sum