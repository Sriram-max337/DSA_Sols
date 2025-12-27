from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = Counter(s1)
        freq = Counter()
        
        x=0
        for s in range(len(s2)):
            freq[s2[s]]+=1

            if s-x+1 > len(s1):
                freq[s2[x]]-=1
                if freq[s2[x]]==0:
                    del freq[s2[x]]
                x+=1

            if freq_s1 == freq:
                return True

        return False
    
Sol = Solution()
print(Sol.checkInclusion("ab","eidboaoo"))