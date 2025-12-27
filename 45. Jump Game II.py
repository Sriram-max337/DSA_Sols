nums = [2,3,1,1,4]
       #0,1,2,3,4

MaxReach=0
jumps=0
CurrentEnd=0

for i in range(len(nums)-1):
    MaxReach = max(MaxReach,i+nums[i])
    if CurrentEnd==i:
        jumps+=1
        CurrentEnd=MaxReach
print(jumps) 
