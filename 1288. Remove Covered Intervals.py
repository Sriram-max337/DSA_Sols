class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x:(x[0], -x[1]))

        res = len(intervals)
        max_end = 0

        for i in range(n):
            if intervals[i][1] > max_end:
                max_end = intervals[i][1]
            else:
                res-=1

        return res