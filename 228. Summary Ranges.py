class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        map = set(nums)
        res = []
        for num in nums:
            #start = None
            if num-1 not in map and num+1 in map:
                start=num
            elif num+1 not in map and num-1 in map:
                end=num
                res.append(str(start)+"->"+str(end))
            elif num-1 not in map and num+1 not in map:
                res.append(str(num))
        return res