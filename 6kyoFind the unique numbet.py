def find_uniq(arr):
    if arr[0] == arr[1]:
        orig = arr[0]
    else:
        orig = arr[2]
    arr = list(set(arr))
    if arr[0] == orig:
         return arr[1]
    else:
         return arr[0]
   
