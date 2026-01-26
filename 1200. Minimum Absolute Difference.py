arr = [40,11,26,27,-20]
arr.sort()#[1,2,3,4]
res = []
abs_min = arr[1]-arr[0]

for i in range(1,len(arr)):
    diff = arr[i]-arr[i-1]
    if diff < abs_min:
        abs_min=diff

print(abs_min)

for i in range(1,len(arr)):
    if arr[i]-arr[i-1] == abs_min:
        res.append([arr[i-1],arr[i]])

print(res)

