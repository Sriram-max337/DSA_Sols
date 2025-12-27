#our logic -> bit unoptimised
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit1_lst = []
        for num in digits:
            digit1_lst.append(str(num))

        digit1 = "".join(digit1_lst)
        digit2 = str(int(digit1)+1)
        lst2 = list(digit2)

        digit2_lst = []
        for num in digit2:
            digit2_lst.append(int(num))
        return digit2_lst