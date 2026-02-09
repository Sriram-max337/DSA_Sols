# nums = [1,2,1]
# ans = []

# for i in range(len(nums)):
#     ans.append(nums[i])

# for j in range(len(nums)):
#     ans.append(nums[j])

# print(ans)

# a = [1, 2, 3]
# b = a
# a += [4, 5]

# print(b)

# def func(x, l=[]):
#     l.append(x)
#     return l

# print(func(1))
# print(func(2))
# print(func(3))


a = [1,2,3]
b = a[:]
print(b)

print(a==a[:])
