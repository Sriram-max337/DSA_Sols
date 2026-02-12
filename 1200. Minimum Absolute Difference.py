class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        abs_min = arr[1]-arr[0]

        for i in range(1,len(arr)):
            diff = arr[i]-arr[i-1]
            if diff < abs_min:
                abs_min=diff

        for i in range(1,len(arr)):
            if arr[i]-arr[i-1] == abs_min:
                res.append([arr[i-1],arr[i]])

        return res


