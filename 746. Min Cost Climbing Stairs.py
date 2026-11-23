class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        HM = {}
        stair_len = len(cost)
        stair_cost = 0

        def calc_min_cost(i):
            if i == 0:
                return cost[0]

            if i == 1:
                return cost[1]

            if i not in HM:
                HM[i] = cost[i] + min(calc_min_cost(i-1), calc_min_cost(i-2))

            return HM[i]

        stair_cost = min(calc_min_cost(stair_len-1), calc_min_cost(stair_len-2))
        return stair_cost