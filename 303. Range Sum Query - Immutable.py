class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.ps_nums = [0] * (n+1)
        for i in range(1,n+1):
            self.ps_nums[i] = self.ps_nums[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        sum_range = self.ps_nums[right]-self.ps_nums[left]
        return sum_range


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)