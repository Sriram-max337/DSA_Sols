class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        si = 0

        if sum(gas) < sum(cost):
            return -1
        else:
            for i in range(len(gas)):
                tank+=gas[i]
                tank-=cost[i]
                if tank < 0:
                    tank = 0
                    si = i+1
            return si
        