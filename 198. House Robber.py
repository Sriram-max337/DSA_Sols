class Solution:
    def rob(self, nums: list[int]) -> int:
        HM = {}
        n = len(nums)
        if n == 1:
            return nums[-1]

        def rob(x):
            if x == 0:
                return nums[0]

            if x == 1:
                return max(nums[0], nums[1])

            if x not in HM:
                HM[x] = max(nums[x] + rob(x-2), rob(x-1))

            return HM[x]

        tot_money = rob(n-1)

        return tot_money