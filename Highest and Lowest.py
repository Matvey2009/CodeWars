def high_and_low(numbers):
    numbers = numbers.split(" ")
    maxi = -99999
    mini = 99999
    for i in numbers:
        if int(i) > int(maxi):
            maxi = i
        if int(i) < int(mini):
            mini = i
    return maxi + " " + mini
