class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perm_lst = []
        permutations_lst = []

        def permutation(no,perm_lst,rem_lst):
            nonlocal permutations_lst
            if len(perm_lst) == len(nums):
                permutations_lst.append(perm_lst)
                return

            for i, no in enumerate(rem_lst):
                perm_lst_copy = perm_lst + [no]
                permutation(no,perm_lst_copy,rem_lst[:i] + rem_lst[i+1:])

        permutation(nums[0],perm_lst,nums)
        return permutations_lst   