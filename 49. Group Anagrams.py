from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]

lst = defaultdict(list)

for s in strs:
    lst["".join(sorted(s))].append(s)

print(list(lst.values()))