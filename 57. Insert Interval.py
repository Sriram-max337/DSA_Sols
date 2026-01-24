class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lst = intervals+[newInterval]
        lst.sort(key=lambda x:x[0])

        res = []

        ls = lst[0][0]
        le = lst[0][1]
        for i in range(1,len(lst)):
            s = lst[i][0]
            e = lst[i][1]
            if s<=le:
                le = max(le,e)
            else:
                res.append([ls,le])
                ls = s
                le = e

        res.append([ls,le])
        return res
