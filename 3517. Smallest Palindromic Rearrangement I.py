from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        HM = dict(Counter(s))
        sorted_map = dict(sorted(HM.items(), key=lambda x:x[0]))
        p = ""
        for char in sorted_map.keys():
            p += char * (sorted_map[char]//2)
        shit = ""
        for char in sorted_map.keys():
            if HM[char]%2!=0:
                shit = char
        if len(s) == 1:
            return s
        if len(s)%2==0:
            return p+p[::-1]
        else:
            return p + shit + p[::-1]
