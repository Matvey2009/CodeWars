def beeramid(bonus, price):
    col = bonus / price
    but = i = 0
    if bonus < price:
        return 0
    while but <= col:
        i += 1
        but += i**2
    return i-1
