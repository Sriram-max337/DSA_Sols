class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_lst = s.strip().split(" ")
        last_str = str_lst[len(str_lst)-1]
        return len(last_str)