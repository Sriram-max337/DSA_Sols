class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Map = set(nums)
        max_len=0
        if len(Map)==1:
            return 1

        for num in Map:
            if num-1 not in Map and num+1 in Map:
                curr_len = 1
                start = num

                while start+1 in Map:
                    start = start+1
                    curr_len+=1

                max_len = max(curr_len,max_len)

        return max_len