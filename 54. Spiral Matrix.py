class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_mat = []
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows - 1
        right = cols -1
        left = 0

        while top<=bottom and left<=right:
            for i in range(left, right+1):
                spiral_mat.append(matrix[top][i])
            top+=1

            for j in range(top, bottom+1):
                spiral_mat.append(matrix[j][right])
            right-=1

            if top<=bottom:
                for k in range(right, left-1, -1):
                    spiral_mat.append(matrix[bottom][k])
                bottom-=1

            if left<=right:
                for l in range(bottom, top-1, -1):
                    spiral_mat.append(matrix[l][left])
                left+=1

        return spiral_mat