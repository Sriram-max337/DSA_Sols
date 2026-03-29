class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        win_count = 0 
        HM = {0:1}
        running_sum = 0

        for i in range(n):
            running_sum += nums[i]
            if running_sum - k in HM:
                win_count += HM[running_sum - k]

            HM[running_sum] = HM.get(running_sum, 0) + 1

        return win_count