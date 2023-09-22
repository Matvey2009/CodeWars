def solution(number):
    if number >= 0:
        s = 0
        for i in range(number):
            if i%3==0 or i%5==0:
                s+=i
        return s
    else:
        return 0
