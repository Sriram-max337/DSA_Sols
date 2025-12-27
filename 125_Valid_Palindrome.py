#Brute Force-our logic
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_lst = []
        for i in s.lower().strip().replace(" ",""):
            if i >= 'a' and i<='z'or i >='0' and i<='9':
                str_lst.append(i)

        #print(str_lst)
        str1 = "".join(str_lst)
        #print(str1)
        rev_str_lst = reversed(list(str_lst))
        str2 = "".join(rev_str_lst)
    
        return str1 == str2
    
#Semi Optimised , cleanest Sol
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # More concise filtering using list comprehension and str.isalnum()
        cleaned = ''.join(char for char in s.lower() if char.isalnum())
        return cleaned == cleaned[::-1]
    
#Classic Sol, Optimised 2Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1

        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower()!=s[r].lower():
                return False
                break
            else:
                l+=1
                r-=1
        return True