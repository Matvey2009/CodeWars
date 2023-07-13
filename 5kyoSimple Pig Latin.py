def pig_it(text):
    arr = text.split(" ")
    l = ""
    for i in range(len(arr)):
        if (arr[i] == "?" or arr[i] == "!"):
            continue
        temp = arr[i][:1]
        arr[i] += temp
        arr[i] = arr[i][1:]
        arr[i] += "ay"

    for i in range(len(arr)):
        l += " " + arr[i]
    return l[1:]
