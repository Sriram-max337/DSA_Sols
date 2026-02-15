mat = [[1,2],[3,4]]
r = 1
c = 4
m = len(mat)
n = len(mat[0])
eles = []

for i in range(len(mat)):
    eles.append(*mat[i])

print(eles)