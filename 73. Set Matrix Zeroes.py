class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        m = len(matrix[0])
        n = len(matrix)
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)

        for i in range(n):
            for j in range(m):
                if i in row:
                    matrix[i][j]=0
                if j in col:
                    matrix[i][j]=0