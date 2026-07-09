class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ice = 0
        ice_count = 0
        for i in range(len(costs)):
            if ice + costs[i] <= coins:
                ice+=costs[i]
                ice_count+=1
        return ice_count