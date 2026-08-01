import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = {}
        for i in range(len(points)):
            dis[i] = math.sqrt((points[i][0]**2)+(points[i][1]**2))
        dis = dict(sorted(dis.items(), key=lambda item: item[1]))
        lst = []
        for i in dis.keys():
            lst.append(points[i])

        return lst[:k]

import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for i in range(len(points)):
            heapq.heappush(heap, (-math.sqrt((points[i][0]**2)+(points[i][1]**2)),points[i]))
            if len(heap) > k:
                heapq.heappop(heap)

        dis_lst = [x[1] for x in heap]
        return dis_lst