from collections import Counter
nums = [1,2,3,1]

map = Counter(nums)

for i in map.keys():
    if map[i] > 1:
        print(True)
        