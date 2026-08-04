class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        small, big = min(nums), max(nums)
        ans = []

        for num in range(small, big+1):
            if num not in nums_set:
                ans.append(num)

        return ans