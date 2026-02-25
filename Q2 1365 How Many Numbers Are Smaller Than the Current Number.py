class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hs = {}
        res = []
        sor_nums  = sorted(nums)

        for i in range(len(sor_nums)):
            if sor_nums[i] not in hs:
                hs[sor_nums[i]] = i

        for i in range(len(nums)):
            res.append(hs[nums[i]])

        return res