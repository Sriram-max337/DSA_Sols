class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        lst = []

        for i in range(len(nums)):
            x = -nums[i]
            if i!=0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l < r:
            
                psum = nums[l] + nums[r]
                if psum == x:
                    lst.append([-x,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r+1] == nums[r]:
                        r-=1

                elif psum < x:
                    l+=1
                else:
                    r-=1

        return lst
    
    