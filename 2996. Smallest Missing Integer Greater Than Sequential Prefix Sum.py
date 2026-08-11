nums = [1,2,3,2,5]
nums = [3,4,5,1,12,14,13]

ps = 0
for i in range(1,len(nums)):
    if nums[i] == nums[i-1] + 1:
        ps +=1 
    else:
        break

ps += nums[0]
m = max(nums)

HS = set(nums)

x = 0
for ele in HS:
    if ps + x in HS:
        x+=1

print(x)
