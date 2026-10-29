class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []
        combi_lst = []
        HM = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        def recursion(rem_str, combi_str):
            nonlocal combi_lst
            if rem_str == "":
                combi_lst.append(combi_str)
                return
            digit = rem_str[0]
            for char_i in HM[digit]:
                recursion(rem_str[1:], combi_str + char_i)
        recursion(digits, "")
        return combi_lst