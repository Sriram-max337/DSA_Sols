class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        k = 2
        HM = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            if s[right] not in HM:
                HM[s[right]] = 1
            else:
                HM[s[right]] += 1

            while HM[s[right]] > k:
                HM[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len