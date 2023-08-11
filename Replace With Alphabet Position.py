def alphabet_position(text):
    text = text.lower()
    arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    m=''
    for i in text:
        if i in arr:
            m += " " + str(arr.index(i)+1)
    return m[1:]
