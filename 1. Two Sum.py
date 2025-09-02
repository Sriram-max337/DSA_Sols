#Our Logic, Un optimised [O(n)]
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a,b = 0,0
        lst = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    lst.append(i)
                    lst.append(j)

        return lst
    
#Optimised -> Using Hashmaps
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i,num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target-num],i]
            hashmap[num] = i