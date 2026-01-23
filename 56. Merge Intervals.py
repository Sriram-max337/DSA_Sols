class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x:x[0])
    
        ls = intervals[0][0]
        le = intervals[0][1]

        for i in range(1,len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if s<=le:
                le = max(le,e)
            else:
                res.append([ls,le])
                ls = s
                le = e
                
        res.append([ls,le])
    

        return res