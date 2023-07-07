def wave(people):
    t = 0
    arr = []
    for e, i in enumerate(people):
        if(i!=" "):
            arr.append(people[:e] + people[e].upper() + people[e+1:])
        else:
            t += 1
    return arr
