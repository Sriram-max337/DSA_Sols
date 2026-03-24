class Solution:
    def trap(self, height: List[int]) -> int:
        max_right = 0
        max_left = 0
        area = 0
        l,r = 0,len(height)-1

        while l < r:
            if height[l] <= height[r]:
                max_left = max(max_left, height[l])
                area += max_left - height[l]
                l+=1
            else:
                max_right = max(max_right, height[r])
                area += max_right - height[r]
                r-=1

        return area