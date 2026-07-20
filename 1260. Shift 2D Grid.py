class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        mat_lst = []

        for i in range(m):
            for j in range(n):
                mat_lst.append(grid[i][j])

        k = k % len(mat_lst)

        mat_lst = mat_lst[-k:] + mat_lst[:-k]
        shifted_mat = []

        x = 0
        for i in range(m):
            shifted_mat.append([])
            for j in range(n):
                shifted_mat[i].append(mat_lst[x])
                x+=1

        return shifted_mat