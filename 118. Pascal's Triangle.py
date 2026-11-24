# numRows = 5

# pt = []

# for i in range(1,numRows+1):
#     pt.append([])
#     for j in range(i):
#         if j == 0 or j == i-1:
#             pt[i-1].append(1)
#         else:
#             pt[i-1].append(pt[i-2][j-1] + pt[i-2][j])
#     print(pt[i-1])


# PT = [
#         [1],
#        [1,1],
#       [1,2,1],
#      [1,3,3,1],
#     [1,4,6,4,1]
# ]

# #0 and n-1 == 1

#                   1
#               1       1
#           1       2       1
#       1       3       3       1
#   1       4       6       4       1

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pt = [[] for row in range(numRows)]
        HM = {}

        def pascal_triangle(row, col):
            if (row,col) in HM:
                return HM[(row,col)]

            if col == 0 or row == col:
                HM[(row,col)] = 1

            else:
                HM[(row, col)] = pascal_triangle(row-1, col-1) + pascal_triangle(row-1, col)
            
            pt[row].append(HM[(row,col)])
            return HM[(row,col)]

        
        for num in range(numRows):
            pascal_triangle(numRows - 1, num)

        pascal_triangle(0,0)
        return pt




    
