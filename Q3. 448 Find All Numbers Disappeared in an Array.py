nums = [1,1]
hs = set(nums)
arr = list(range(1, len(nums)+1))
ans = []

for num in arr:
    if num not in hs:
        ans.append(num)

print(hs)
print(arr)
print(ans)



