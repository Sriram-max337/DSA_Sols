class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        flat_mat = []
        upd_mat = []
        if m*n != r*c:
            return mat

        for i in range(m*n):
            a = i//n
            b = i%n
            flat_mat.append(mat[a][b])

        for i in range(r):
            upd_mat.append([])
            for j in range(c):
                upd_mat[i].append(flat_mat[i*c+j])

        return upd_mat

