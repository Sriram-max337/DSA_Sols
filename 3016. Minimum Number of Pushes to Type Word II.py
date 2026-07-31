from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        ans = 0
        sorted_c = sorted(c.values(), reverse=True)
        i = 0
        for x in sorted_c:
            ans += x * (i//8 + 1)
            i+=1

        return ans