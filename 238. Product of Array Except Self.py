#Our Logic -> Brute Force -> O(n^2) time, O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_lst = []
        def prod(i):
            prod1,prod2=1,1
            for num in nums[:i]:
                prod1*=num

            for num in nums[i+1:]:
                prod2*=num

            return prod1*prod2

        for i in range(len(nums)):
            prod_lst.append(prod(i))
        
        return prod_lst
    
#Semi Optimised -> O(n) time, O(n) extra space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1] * n
        suffix_prod = [1] * n
        prod_lst = []
        
        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]

        for j in range(n-2, -1, -1):
            suffix_prod[j] = suffix_prod[j+1] * nums[j+1]

        for i in range(n):
            prod_lst.append(prefix_prod[i] * suffix_prod[i])

        return prod_lst   
    
#Optimised -> O(n) time, O(1) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [1]*n
        for i in range(1, n):
            prod[i] = prod[i-1] * nums[i-1]

        suffix=1
        for i in range(n-1, -1, -1):
            prod[i]*=suffix
            suffix*=nums[i]

        return prod     