n = int(input())
arr = {2}
for i in range(n):
	for j in range(2, int(i ** 0.5) + 1):
		if i % j == 0:
			break
		else:
			arr.update(i)
print(arr)

