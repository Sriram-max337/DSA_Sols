class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        for i in range(len(s)):
            mid = i
            l = i
            r = i

            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > max_len:
                        max_len = max(max_len, len(s[l:r+1]))
                        res = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break

            mid = i
            l = i
            r = i+1

            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > max_len:
                        max_len = max(max_len, len(s[l:r+1]))
                        res = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break

        return res