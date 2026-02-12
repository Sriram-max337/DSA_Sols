class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat)==1:
            return mat[0][0]
        n = len(mat)
        diag1 = 0
        diag2 = 0

        for i in range(n):
            diag1 += mat[i][i]
            diag2 += mat[i][n-1-i]

        if len(mat) > 2 and n%2!=0:
            diag2-=mat[n//2][n//2]

        return diag1 + diag2