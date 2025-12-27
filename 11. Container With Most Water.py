#Classic Brute Force
class Solution:
    def maxArea(self, height: List[int]) -> int:
        Max = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                if min(height[i],height[j])*(j-i) > Max:
                    Max = min(height[i],height[j])*(j-i)
        return Max
        
#Optimised -> 2Pointers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        Max = 0

        while i < j:
            if min(height[i],height[j])*(j-i) > Max:
                Max = min(height[i],height[j])*(j-i)
            if height[i] > height[j]:
                j-=1
            else:
                i+=1

        return Max
    
