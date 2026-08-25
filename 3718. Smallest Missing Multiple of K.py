class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        HS = {num for num in nums if num > 0 and num % k == 0}

        if not HS:
            return k
        
        for i in range(k, max(HS)+1, k):
            if i not in HS:
                return i

        return max(HS) + k