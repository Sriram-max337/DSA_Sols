s = "1111"
count_even = 0
count_odd = 0

for i in range(len(s)):
    if i % 2 == 0:
        if s[i]!="0":
            count_even+=1
        elif s[i]!="1":
            count_odd+=1
    else:
        if s[i]!="1":
            count_even+=1
        elif s[i]!="0":
            count_odd+=1


print(min(count_odd,count_even))