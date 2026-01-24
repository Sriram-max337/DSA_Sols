class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==[]:
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