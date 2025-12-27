class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split(" ")
        if len(pattern) != len(lst):
            return False

        map = {}

        for i in range(len(pattern)):
            if pattern[i] not in map:
                if lst[i] in map.values():
                    return False
                map[pattern[i]] = lst[i]
            elif map[pattern[i]] != lst[i]:
                return False

        return True