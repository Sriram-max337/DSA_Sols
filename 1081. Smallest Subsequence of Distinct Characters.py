#Direct String version

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
    
#Stack version
class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = []
        HS = set()
        HM = {}

        for i in range(len(s)):
            HM[s[i]] = i

        for i in range(len(s)):
            if s[i] in HS:
                continue
            else:
                while lst and lst[-1] > s[i] and HM[lst[-1]] > i:
                    shit = lst.pop()
                    HS.remove(shit)

                lst.append(s[i])
                HS.add(s[i])

        return "".join(lst)