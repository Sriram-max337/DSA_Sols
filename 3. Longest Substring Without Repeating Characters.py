class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        start = 0
        max_len = 0

        for i in range(len(s)):
            while s[i] in hs:
                hs.remove(s[start])
                start+=1

            hs.add(s[i])
            str_len = i - start + 1
            max_len = max(max_len, str_len)

        return max_len