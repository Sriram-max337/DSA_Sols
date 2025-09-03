#Oour logic, unoptimised -> O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i

#Optimised -> O(1) Hashing
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set()

        for num in nums:
            hashset.add(num)

        for i in range(len(nums)+1):
            if i not in hashset:
                return i
