matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

m = len(matrix)
n = len(matrix[0])

ans = []

for i in range(len(matrix)):
    print(f"row {i+1} : {matrix[i]}")
    print(f"col {i+1} : {[matrix[0][0], matrix[1][i], matrix[2][i]]}")
    print()

    