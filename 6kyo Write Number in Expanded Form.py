def expanded_form(num):
    snum = str(num)
    arr = list()
    t = ""
    for i in range(len(snum)):
        if snum[i] != '0':
            arr.append(snum[i]+(abs(i-len(snum)+1)*'0'))
    for i in range(len(arr)):
        t += " + " + arr[i]
    return t[3:]
