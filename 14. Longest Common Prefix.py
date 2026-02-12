class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return
        elif len(strs)==1:
            return strs[0]
        
        res=""
        for i in range(len(strs[0])):
            ch=strs[0][i]
            for str in strs:
                if i>=len(str) or str[i]!=ch:
                    return res
            res+=ch
        return res
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return "".join(c[0] for c in zip(*strs) if len(set(c))==1)