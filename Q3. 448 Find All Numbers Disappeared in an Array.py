class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hs = set(nums)
        arr = list(range(1,len(nums)+1))
        ans = []
        
        for num in arr:
            if num not in hs:
                ans.append(num)

        return ans