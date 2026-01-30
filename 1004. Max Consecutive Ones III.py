class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        count0 = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i]==0:
                count0+=1
            while count0 > k:

                if nums[start]==0:
                    count0-=1
                start+=1

            max_len = max(max_len, i-start+1)

        return max_len


        
        
    

