class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        HM = {}
        for i in range(len(s)):
            HM[s[i]] = i

        for i in range(len(s)):
            if s[i] in ans:
                continue 
            else:
                while ans!="" and ans[-1] > s[i] and HM[ans[-1]] > i:
                    ans = ans[:-1]
                ans+=s[i]
        return ans