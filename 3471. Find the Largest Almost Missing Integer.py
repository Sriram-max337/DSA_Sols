class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        fele = nums[0]
        lele = nums[-1]
        
        if k == 1:
            lst = []
            for num, cou in c.items():
                if cou == 1:
                    lst.append(num)
            return max(lst) if lst else -1

        if 1 < k < len(nums):
            if c[fele] > 1 and c[lele]==1:
                return lele
            elif c[lele] > 1 and c[fele]==1:
                return fele
            elif c[fele] == 1 and c[lele] == 1:
                return max(fele, lele)
            return -1

        if k == len(nums):
            return max(nums)