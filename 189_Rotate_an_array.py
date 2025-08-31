#Our logic Optimised - List Slicing
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k] 

#Core logic, general ways -> Array Reversal
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    if k > len(nums):
        k = k%len(nums)

    def reverse(l,r):
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1

    reverse(0,len(nums)-1)
    reverse(0,k-1)
    reverse(k,len(nums)-1)
