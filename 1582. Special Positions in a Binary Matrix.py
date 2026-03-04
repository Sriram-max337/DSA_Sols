class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        special = 0
        r = []
        c = []

        for i in range(m):
            r.append(mat[i].count(1))

        for j in range(n):
            count = 0
            for i in range(m):
                if mat[i][j] == 1:
                    count+=1
            c.append(count)

        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and r[i]==1 and c[j]==1:
                    special+=1

        return special