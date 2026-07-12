class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        lst = sorted(arr)
        HM = {}
        res = []
        x = 1
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                HM[lst[i]] = x
                x+=1
            elif lst[i]==lst[i+1]:
                HM[lst[i]] = x
        if lst:
            HM[lst[-1]] = x

        for i in range(len(arr)):
            res.append(HM[arr[i]])
        return res