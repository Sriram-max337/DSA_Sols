class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        j = 0
        max_len = 0

        for i in range(n):
            if j < i:
                j = i

            while j < n and nums[j] <= k * nums[i]:
                max_len = max(max_len, j - i + 1)
                j += 1

        return n - max_len