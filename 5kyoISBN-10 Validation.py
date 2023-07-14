def valid_ISBN10(isbn):
    s = 0
    arr = list(isbn)
    if (len(isbn) != 10):
        return False
    else:
        if isbn.isdigit():
            for i in range(len(arr)):
                s += int(arr[int(i)])*(int(i)+1)
            if(s%11==0):
                return True
            else:
                return False
        else:
            if isbn[:-1].isdigit() and isbn[-1] == 'X':
                for i in range(len(arr)-1):
                    s += int(arr[int(i)])*(int(i)+1)
                if((s+100)%11==0):
                    return True
                else:
                    return False
            else:
                return False
