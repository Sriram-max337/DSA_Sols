class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_score = float("inf")
        if len(nums)==1:
            return 0

        for i in range(len(nums)-k+1):
            win = nums[i:i+k]
            diff = win[-1]-win[0]
            if diff < min_score:
                min_score = diff

        return min_score