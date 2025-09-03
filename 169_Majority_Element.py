#Booyer Moore Voting Algo
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidaite = None
        count = 0
        for num in nums:
            if count == 0:
                candidaite = num
                count=1
            elif num == candidaite:
                count+=1
            else:
                count-=1

        return candidaite
        
#Optimised -> Using Hashing (Collections module -> Counter)
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count, key=count.get)
        

