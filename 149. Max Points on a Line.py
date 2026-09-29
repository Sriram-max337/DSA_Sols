class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        no_of_points = 0
        HM = {}
        if len(points) == 1:
            return 1
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if i!=j:
                    numer = points[j][1]-points[i][1]
                    denom = points[j][0]-points[i][0]
                    if denom!=0:
                        slope = numer/denom
                        inter = points[i][1] - slope * points[i][0]
                    else:
                        slope = float("inf")
                        inter = points[i][0]

                    HM[tuple(points[j]),tuple(points[i])] = (slope, inter)


        slope_counts = {}

        for point_pair, line in HM.items():
            if line not in slope_counts:
                slope_counts[line] = set()

            slope_counts[line].add(point_pair[0])
            slope_counts[line].add(point_pair[1])

        #print(slope_counts)

        max_no_of_points = 0
        for points_set in slope_counts.values():
            max_no_of_points = max(max_no_of_points, len(points_set))

        return max_no_of_points