nums = [2,5,4,3]

seen = set()
hm = {}

for i in range(len(nums)):
    if nums[i] not in seen:
        seen.add(nums[i])

    
