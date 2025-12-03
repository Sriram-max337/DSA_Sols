from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map1 = Counter(ransomNote)
        map2 = Counter(magazine)

        for ch in map1:
            if map1[ch] > map2[ch]:
                return False
        return True

        
sol = Solution()
print(sol.canConstruct("a","b"))