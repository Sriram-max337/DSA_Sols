intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals.sort(key=lambda x:x[1])

count = 0#0
prev_last = float("-inf")#4

for first,last in intervals:#1,3
    if first < prev_last:# 1<3
        count+=1
    else:
        prev_last = last 
    
print(count)