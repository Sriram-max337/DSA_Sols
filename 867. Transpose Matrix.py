matrix = [[1,2,3],[4,5,6]]
ans = []

for i in range(len(matrix[0])):
    ans.append([])
    for j in range(len(matrix)):
        ans[i].append(matrix[j][i])

print(ans)


