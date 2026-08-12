from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:   
        HM = {}
        max_len = 0
        for num in nums:
            if num not in HM:
                HM[num] = 0
        i = 0
        for j in range(len(nums)):
            HM[nums[j]] sssss+= 1
            while HM[nums[j]] > k:
                HM[nums[i]] -= 1
                i+=1
            max_len = max(max_len, j - i + 1)

        return max_len