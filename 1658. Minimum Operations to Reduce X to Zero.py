class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        l,r = 0,0
        tot_sum = sum(nums)
        win_sum = 0
        res = float('inf')

        for r in range(len(nums)):
            win_sum += nums[r]
            while l <= r:
                if win_sum > tot_sum - x:
                    win_sum -= nums[l]
                    l+=1
                else:
                    break
            if win_sum == tot_sum - x:
                res = min(res, len(nums) - (r - l + 1))

        return res if res != float('inf') else -1