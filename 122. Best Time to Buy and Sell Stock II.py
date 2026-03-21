class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot_profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                tot_profit+= prices[i+1] - prices[i]

        return tot_profit