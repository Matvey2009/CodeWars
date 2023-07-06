def move_zeros(lst):
    for i in range(len(lst)):
        if(lst[i]==0):
            lst.pop(i)
            lst.append(0)
    for i in range(len(lst)):
        if(lst[i]==0):
            lst.pop(i)
            lst.append(0)
    for i in range(len(lst)):
        if(lst[i]==0):
            lst.pop(i)
            lst.append(0)
    for i in range(len(lst)):
        if(lst[i]==0):
            lst.pop(i)
            lst.append(0)
    return lst
