class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        no = -1
        for i in range(len(nums)):
            no_sum = 0
            no_str = str(nums[i])
            for j in range(len(no_str)):
                no_sum += int(no_str[j])

            if no_sum == i:
                no = i
                break

        return no