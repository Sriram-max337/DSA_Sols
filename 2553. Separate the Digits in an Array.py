nums = [13,25,83,77]
ans = []

for num in nums:
    for digit in str(num):
        ans.append(int(digit))

print(ans)