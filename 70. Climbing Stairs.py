class Solution:
    def climbStairs(self, n: int) -> int:
        HM = {}

        def calc_steps(x):
            if x < 0:
                return 0
            if x == 0:
                return 1
            
            if x not in HM:
                HM[x] = calc_steps(x - 1) + calc_steps(x - 2)
            
            return HM[x]

        return calc_steps(n)