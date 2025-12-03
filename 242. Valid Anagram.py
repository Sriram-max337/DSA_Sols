from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S_map = Counter(s)
        T_map = Counter(t)

        if S_map == T_map:
            return True
        else:
            return False
        