from collections import Counter

word = "aaAbcBC"
HM = Counter(word)
check = set()
count = 0

for i in HM:
    if i not in check:
        if i.islower() and i.upper() in HM:
            count += 1
            check.add(i)
    elif i not in check:
        if i.isupper() and i.lower() in HM:
            count += 1
            check.add(i)

print(count)
    
