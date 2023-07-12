def prime(n):
    arr = []
    if n == 2:
        arr = [2]
        return arr
    for i in range(2, n+1):
        test = 0
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                test = 1
                break
        if test == 0:
            arr.append(i)
    return arr
