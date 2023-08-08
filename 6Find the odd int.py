def find_it(seq):
    from collections import Counter
    arr = Counter(seq)
    k = 0
    for i in seq:
        if arr[int(i)] % 2 != 0:
            return seq[k]
            break
        k += 1
