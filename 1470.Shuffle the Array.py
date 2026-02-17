nums = [2,5,1,3,4,7]
n = 3

upd_nums = []

p1 = 0
p2 = n

while p2 < len(nums):
    upd_nums.append(nums[p1])
    upd_nums.append(nums[p2])
    p1+=1
    p2+=1

print(upd_nums)
