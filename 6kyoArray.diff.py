def array_diff(a, b):
    k=0
    while k!=len(a):
        if a[k] in b:
            a.pop(k)
            k-=1
        k+=1
    return a
