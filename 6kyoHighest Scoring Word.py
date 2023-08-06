def high(x):
    m = t = 0
    arr1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    arr2 = list(x.split(" "))
    arr3 = list()
    for i in range(len(arr2)):
        t=0
        for j in range(len(arr2[i])):
            t += arr1.index(arr2[i][j])+1
            ti = arr2[i]
        if t>m:
            m=t
            n = ti
    return n
