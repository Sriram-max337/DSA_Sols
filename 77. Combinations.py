class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        lst = [i+1 for i in range(n)]
        combinations_lst = []
        prep_lst = []

        def combinations(num,rem_lst,prep_lst):
            nonlocal combinations_lst
            if len(prep_lst) == k:
                combinations_lst.append(prep_lst)
                return

            for i,num in enumerate(rem_lst[:len(rem_lst)-(k-len(prep_lst))+1]):
                prep_lst_copy = prep_lst + [num]
                combinations(num,rem_lst[i+1:],prep_lst_copy)

        combinations(lst[0],lst,prep_lst)
        return combinations_lst