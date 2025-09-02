def missing_no(nums):
    n = len(nums)
    hashset = set()

    for num in nums:
        hashset.add(num)

    for i in range(n+1):
        if i not in hashset:
            print(i)
            return i
            
        
missing_no([3,0,1])