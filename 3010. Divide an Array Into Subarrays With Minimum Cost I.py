class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        start = nums[0]
        lst = sorted(nums[1:])
        return start + lst[0] + lst[1]