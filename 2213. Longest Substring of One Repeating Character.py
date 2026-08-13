class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        lengths = []
        for i in range(len(queryIndices)):
            s = s[:queryIndices[i]] + queryCharacters[i] + s[queryIndices[i]+1:]
            c = 1
            max_len = 1
            for j in range(1,len(s)):
                if s[j] == s[j-1]:
                    c += 1
                else:
                    max_len = max(c, max_len)
                    c = 1
            max_len = max(c, max_len)
            lengths.append(max_len)

        return lengths