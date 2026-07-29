import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [i*-1 for i in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            ele1 = -(heapq.heappop(heap))
            ele2 = -(heapq.heappop(heap))
            if ele1 > ele2:
                ele = ele1 - ele2
            else:
                ele = ele2 - ele1
            heapq.heappush(heap, -ele)

        return -heap[0] if heap else 0