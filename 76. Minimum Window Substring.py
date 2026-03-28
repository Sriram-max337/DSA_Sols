from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sub_str = ""
        ct = Counter(t)

        min_len = float("inf")
        if len(s) < len(t):
            print(sub_str)
        elif len(s) == len(t):
            print(s)

        i = 0
        count = 0
        count_needed = len(ct)
        win_counts = {}

        for j in range(len(s)):
            if s[j] not in win_counts:
                win_counts[s[j]] = 1
                if s[j] in ct and win_counts[s[j]] == ct[s[j]]:
                    count+=1
            elif s[j] in ct:
                win_counts[s[j]]+=1
                if win_counts[s[j]] == ct[s[j]]:
                    count+=1
            else:
                win_counts[s[j]]+=1

            while count == count_needed:
                if s[i] in ct:
                    win_counts[s[i]]-=1
                    if win_counts[s[i]] < ct[s[i]]:
                        count-=1
                else:
                    win_counts[s[i]]-=1

                if min_len > j-i+1:
                    min_len = j-i+1
                    sub_str = s[i:j+1]

                i+=1

        return sub_str