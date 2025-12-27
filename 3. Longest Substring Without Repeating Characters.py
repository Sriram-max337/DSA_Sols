from collections import Counter
s = "abcabcbb"

l=0
min_len = len(s)
map = Counter(s)
freq = Counter()

for r in range(len(s)):
    freq[s[r]]+=1
    if s[r]==s[r-1]:
        pass
    