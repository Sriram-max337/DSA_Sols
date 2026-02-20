nums = [1,1,0,1,1,1]

max_ones = 0
count = 0

for i in range(len(nums)):
    if nums[i]==0:
        count = 0

    elif nums[i]==1:
        count+=1
        max_ones = max(count,max_ones)

print(max_ones)

    

