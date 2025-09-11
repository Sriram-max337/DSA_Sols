#Direct One Liner
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])

#Algorithmic -> Two Pointers  
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j = 0,len(nums)-1
        squares_lst = []
        
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                squares_lst.append(nums[j]**2)
                j-=1
            else:
                squares_lst.append(nums[i]**2)
                i+=1
        
        return squares_lst[::-1]
