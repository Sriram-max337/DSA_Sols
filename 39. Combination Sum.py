class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        combi_sum_lst = []

        def combisum(rem_lst,target_sum,combi_lst):
            if target_sum == target:
                combi_sum_lst.append(combi_lst)
                return
            elif target_sum > target:
                return

            for i,no in enumerate(rem_lst):
                combi_lst_copy = combi_lst + [no]
                combisum(rem_lst[i:],target_sum + no ,combi_lst_copy)

        combisum(candidates, 0, [])
        return combi_sum_lst