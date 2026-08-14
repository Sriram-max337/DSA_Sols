from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:   
        HM = {}
        left = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] not in HM:
                HM[nums[right]] = 1
            else:
                HM[nums[right]] += 1

            while HM[nums[right]] > k:
                HM[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len