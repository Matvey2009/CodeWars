#def next_bigger(n):
n = int(input())
stn = str(n)
arr = list()
for i in stn:
	arr.append(int(i))
arr.sort()
arr.reverse()
if (arr[0] == 0):
	arr[0], arr[1] == arr[1], arr[0]
if (arr[0] == 0):
	arr[0], arr[2] == arr[2], arr[0]
if (arr[0] == 0):
	arr[0], arr[3] == arr[3], arr[0]
k = ""
for i in arr:
	k += str(i)
if(int(k) == n):
	#return -1
	print(-1)
else:
	print(int(k))
	#return int(k)
