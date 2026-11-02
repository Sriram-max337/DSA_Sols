class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parentheses_lst = []
        def parentheses(par_str, open_count, close_count):
            nonlocal parentheses_lst
            if close_count == n:
                parentheses_lst.append(par_str)
                return

            if open_count < n:
                parentheses(par_str + "(", open_count + 1, close_count)

            if close_count < open_count:
                parentheses(par_str + ")", open_count, close_count + 1)

        parentheses("", 0, 0)
        return parentheses_lst