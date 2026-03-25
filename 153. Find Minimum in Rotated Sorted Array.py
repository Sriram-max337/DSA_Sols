nums = [3,4,5,1,2]

low = 0
high = len(nums)-1
min_ele = float("inf")

while low <= high:
    mid = (low + high)//2
    min_ele = min(min_ele, nums[mid])
    
    if nums[mid] > nums[high]:
        low = mid + 1
    else:
        
        high = mid - 1

print(min_ele)

