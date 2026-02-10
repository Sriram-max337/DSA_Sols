class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix[0])):
            ans.append([])
            for j in range(len(matrix)):
                ans[i].append(matrix[j][i])

        return ans