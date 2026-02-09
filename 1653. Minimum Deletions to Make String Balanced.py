class Solution:
    def minimumDeletions(self, s: str) -> int:
        if len(s)==1:
            return 0
        prefix_b = [0]*(len(s)+1)
        for i in range(len(s)):
            prefix_b[i+1] = prefix_b[i] + (s[i]=="b")

        suffix_a = [0]*(len(s)+1)
        for j in range(len(s)-1,-1,-1):
            suffix_a[j] = suffix_a[j+1] + (s[j]=="a")

        min_dels = float("inf")

        for k in range(len(s)+1):
            min_dels = min(min_dels, prefix_b[k]+suffix_a[k])

        return min_dels