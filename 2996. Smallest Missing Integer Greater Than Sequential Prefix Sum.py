class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ps = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                ps += nums[i]
            else:
                break

        ps += nums[0]
        HS = set(nums)
        while ps in HS:
            ps += 1
        return ps