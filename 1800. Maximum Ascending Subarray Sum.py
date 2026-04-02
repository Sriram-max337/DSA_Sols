class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        win_sum = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                win_sum+=nums[i]
            else:
                max_sum = max(max_sum, win_sum)
                win_sum = nums[i]

        max_sum = max(win_sum,max_sum)

        return max_sum