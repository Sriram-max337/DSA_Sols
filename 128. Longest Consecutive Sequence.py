# #Method 1
# nums = [100,4,200,1,3,2]
# nums.sort()
# Map = []

# for i in range(len(nums)):
#     if nums[i]-nums[i-1]==1:
#         Map.append(nums[i-1])

# print(len(Map)+1)

# #Method 2
# nums = [100,4,200,1,3,2]
# Map = [min(nums)]
# nums.remove(min(nums))

# j=0
# for i in range(len(nums)):
#     if min(nums)-Map[j]==1:
#         print(f"min(nums) : {min(nums)}, Map[j] : {Map[j]}, j : {j}")
#         Map.append(min(nums))
#         nums.remove(min(nums))
#         j+=1

# print(len(Map))

# nums = [100,4,200,1,3,2]
# Map = []

# for i in range(len(nums)):
#     if nums[i]+1 in nums and nums[i] not in Map:
#         Map.append(nums[i])

# print(len(Map)+1)

nums = [100,1]
s = set(nums)
max_len=0
start = 0
curr_len = 1

for i in range(len(nums)):
    if nums[i]-1 not in s and nums[i]+1 in s:
        start = nums[i]
    
        while start+1 in s:
            start = start+1
            curr_len+=1

        max_len = max(curr_len,max_len)

print(max_len)



    


    



        


