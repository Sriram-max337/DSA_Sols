# O(m log n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            low = 0
            high = len(matrix[i])-1

            while low <= high:
                mid = (low+high)//2
                if target == matrix[i][mid]:
                    return True
                elif target < matrix[i][mid]:
                    high = mid - 1
                else:
                    low = mid + 1

        return False
    
# O(log m*n)    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n-1
        while low <= high:
            mid = (low+high)//2
            row = mid//n
            col = mid%n
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                high = mid - 1
            else:
                low = mid + 1

        return False