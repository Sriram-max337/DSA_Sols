class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1]) 
        min_arrows = 1
        posi = points[0][1]

        for i in range(1,len(points)):
            if posi < points[i][0]:
                min_arrows+=1
                posi = points[i][1]

        return min_arrows