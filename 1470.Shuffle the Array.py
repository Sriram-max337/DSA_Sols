class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        upd_nums = []
        p1 = 0
        p2 = n
        while p2 < len(nums):
            upd_nums.append(nums[p1])
            upd_nums.append(nums[p2])
            p1+=1
            p2+=1
        return upd_nums