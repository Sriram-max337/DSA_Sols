def bal_arr(nums=[1,6,2,9],k=3):
    nums.sort()
    if len(nums)==1:
        return 0
    elif len(nums)==2:
        if nums[1]<=k*nums[0]:
            return 0
    
    j=0
    max_len=0
    for i in range(len(nums)):
        while j < len(nums) and nums[j]<=k*nums[i]:
            max_len = max(max_len, j-i+1)
            j+=1

    return len(nums)-max_len

        

print(bal_arr())

