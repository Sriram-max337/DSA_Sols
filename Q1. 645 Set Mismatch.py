nums = [1,5,3,2,2,7,6,4,8,9]
hs = set(range(1,len(nums)+1))
ans = []
nums.sort()
miss = None

for i in range(1,len(nums)):
    if nums[i]==nums[i-1]:
        ans.append(nums[i])

miss_set = hs - set(nums)

for num in miss_set:
    miss = num
    ans.append(miss)

print(ans)
