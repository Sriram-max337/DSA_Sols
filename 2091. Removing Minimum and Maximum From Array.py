class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=2 :
            return n

        min_ele = min(nums)
        max_ele = max(nums)

        min_ele_index = nums.index(min_ele)
        max_ele_index = nums.index(max_ele)

        si = min(min_ele_index, max_ele_index)
        ei = max(min_ele_index,max_ele_index)

        from_front = ei + 1 
        from_back = n - si
        from_both = (si + 1) + (n - ei)

        return min(from_front, from_back, from_both)