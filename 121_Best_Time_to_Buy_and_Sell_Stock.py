#Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits_lst = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] - prices[i] > 0:
                    profits_lst.append(prices[j] - prices[i])

        if profits_lst == []:
            return 0
        else:
            return max(profits_lst)
        
#Optimised
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_val:
                min_val = price

            profit = price - min_val

            if profit > max_profit:
                max_profit = profit

        return max_profit