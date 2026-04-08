class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        win_sum1 = 0
        min_sum = nums[0]
        win_sum2 = 0

        for i in range(len(nums)):
            if win_sum1 < 0:
                win_sum1 = 0
            win_sum1 += nums[i]
            max_sum = max(max_sum, win_sum1)

        for j in range(len(nums)):
            if win_sum2 > 0:
                win_sum2 = 0
            win_sum2 += nums[j]
            min_sum = min(min_sum, win_sum2)

        cir_sum = max(max_sum, sum(nums)-min_sum)
        if cir_sum == 0:
            return max(nums)
        else:
            return cir_sum