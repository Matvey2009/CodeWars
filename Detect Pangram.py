def is_pangram(s):
    s = list(set(s.lower()))
    t = 0
    arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(len(arr)):
        for j in range(len(s)):
            if arr[i] == s[j]:
                t += 1
                break
    if t == 26:
        return True
    else:
        return False
