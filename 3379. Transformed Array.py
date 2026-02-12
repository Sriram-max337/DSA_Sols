nums = [-1,4,-1]
res = []

for i in range(len(nums)):
    if nums[i]==0:
       res.append(nums[i])

    else:
      res.append(nums[(i+nums[i])%len(nums)])

    
    
print(res)
                      

