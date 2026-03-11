class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        shit = []
        for i in range(len(prices)):
            while shit and prices[i] <= prices[shit[-1]]:
                prices[shit[-1]] -= prices[i]
                shit.pop()
            shit.append(i)

        return prices