from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HM = dict(Counter(nums))
        heap = []

        for num, freq in HM.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [x[1] for x in heap]