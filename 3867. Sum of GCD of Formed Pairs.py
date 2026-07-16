import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        current_max = nums[0]

        for num in nums:
            current_max = max(current_max, num)
            prefixGcd.append(math.gcd(current_max, num))

        prefixGcd.sort()

        if len(prefixGcd)%2!=0:
            prefixGcd.remove(prefixGcd[len(prefixGcd)//2])

        gcd_sum = 0
        l = 0
        r = len(prefixGcd)-1

        while l < r:
            gcd_sum += math.gcd(prefixGcd[l], prefixGcd[r])
            l+=1
            r-=1

        return gcd_sum