#Semi Brute force -> O(n*K)
nums = [1,12,-5,-6,50,3]
n=len(nums)
k = 4
l=0
current_sum = sum(nums[l:k])
max_sum = current_sum
for r in range(k,n):
    current_sum += nums[r]
    current_sum -= nums[l]
    l+=1
    max_sum = max(max_sum, current_sum)

print(max_sum/k)

#Clean Sliding window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        l=0
        current_sum = sum(nums[l:k])
        max_sum = current_sum
        for r in range(k,n):
            current_sum += nums[r]
            current_sum -= nums[l]
            l+=1
            max_sum = max(max_sum, current_sum)
        return max_sum/k