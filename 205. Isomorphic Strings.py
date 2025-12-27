class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        map = {}
        for i in range(len(s)):
            if s[i] not in map:
                if t[i] in map.values():
                    return False
                map[s[i]]=t[i]

            elif map[s[i]]!=t[i]:
                return False

        return True



