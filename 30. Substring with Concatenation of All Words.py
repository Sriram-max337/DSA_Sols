import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        c = collections.Counter(words)
        l = len(words[0])
        perm_len = l*len(words)

        for i in range(l):
            for j in range(i, len(s)-perm_len+1,l):
                win = s[j:j+perm_len]
                win_words = [win[k:k+l] for k in range(0,perm_len,l)]
                if c==collections.Counter(win_words):
                    ans.append(j)

        return ans