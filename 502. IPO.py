import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        lst = [(capital[i],profits[i]) for i in range(len(capital))]
        lst.sort()

        heap = []
        n = 0
        i = 0
        while n < k:
            while i < len(lst) and w >= lst[i][0]:
                heapq.heappush(heap, -lst[i][1])
                i += 1
            if heap:
                w += (-heapq.heappop(heap))
            n+=1

        return w