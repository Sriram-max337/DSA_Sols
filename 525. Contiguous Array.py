class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        n = len(nums)
        win_count = 0
        running_sum = 0
        k = 0
        HM = {0:-1}

        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum not in HM:
                HM[running_sum] = i
            else:
                win_count = max(win_count, i-HM[running_sum])

        return win_count