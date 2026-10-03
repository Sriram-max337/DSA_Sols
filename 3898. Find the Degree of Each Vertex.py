class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])

        s = 0
        for i in range(m):
            for j in range(n):
                s += matrix[i][j]
            ans.append(s)
            s = 0

        return ans