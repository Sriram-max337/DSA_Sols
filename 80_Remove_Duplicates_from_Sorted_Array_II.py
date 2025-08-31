nums = [1,1,1,2,2,3]
#we need to keep only 2 occurences of every ele

k=0
for num in nums:
    if num!=nums[k-2]:
        nums[k]=num
        k+=1

print(k)