class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sw_sum = 0
        for i in range(len(nums)):
            if sw_sum < 0:
                sw_sum = 0
            sw_sum+=nums[i]

            max_sum = max(max_sum, sw_sum)

        return max_sum