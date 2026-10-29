n = 4
k = 2

lst = [i+1 for i in range(n)]
combinations_lst = []
prep_lst = []

def combinations(no,rem_lst,prep_lst):
    nonlocal combinations_lst
    if len(prep_lst) == k:
        combinations_lst.append(prep_lst)
        return
    
    #prep_lst.append(rem_lst[0])
    rem_lst = rem_lst[1:]

    for num in rem_lst:
        prep_lst.append(num)
        combinations(num,rem_lst,prep_lst)

combinations(lst[0],lst[1:],prep_lst=[lst[0]])

prep_lst = [1]
prep_lst += [2]

print(prep_lst)

def combinations(no,rem_lst,prep_lst):
    nonlocal combinations_lst
    if len(prep_lst_copy) == k:
        combinations_lst.append(prep_lst_copy)
        return
    
    rem_lst = rem_lst[1:]
    for i,num in enumerate(rem_lst):
        prep_lst_copy = prep_lst + [num]
        combinations(num,rem_lst[i+1:],prep_lst_copy)

combinations(lst[0],lst[1:],prep_lst=[lst[0]])
return combinations_lst