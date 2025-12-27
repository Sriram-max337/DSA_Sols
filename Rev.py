# #125-Valid Palindrome
# s = "A man, a plan, a canal: Panama"

# l,r = 0,len(s)-1
# while l<r:
#     if not s[l].isalnum():
#         l+=1
#     elif not s[r].isalnum():
#         r-=1
#     elif s[l].lower()!=s[r].lower():
#         print(False)
#         break
#     else:
#         l+=1
#         r-=1
# print(True)


# #167. Two Sum II - Input Array Is Sorted
# numbers,target = [2,7,11,15],9

# l,r = 0,len(numbers)-1

# while l<r:
#     if numbers[l] + numbers[r] == target:
#         print(f"l:{l+1}, r:{r+1}")
#         break
#     elif numbers[l] + numbers[r] < target:
#         l+=1
#     elif numbers[l] + numbers[r] > target:
#         r-=1

# #26. Remove Duplicates from Sorted Array
# nums = [1,1,2]
# k=1
# for i in range(1,len(nums)):#i=1,i=2
#     if nums[i]!=nums[i-1]:#1==1,2!=1
#         nums[i] = nums[k]#
#         k+=1
# print(k)

#80. Remove Duplicates from Sorted Array II
nums = [1,1,1,2,2,3]
k=0

for num in nums:
    if k<2 or num != nums[k-2]:
        num = nums[k]
        k+=1

print(k)



