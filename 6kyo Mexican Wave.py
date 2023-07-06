people = input()
t = 0
arr = []
for i in range(len(people)):
	if(people!=" "):
		f = people[i+t]
		f.title()
		s = people[i+t:] + f.upper + people[:i+t+1]
		arr.append(s)
	else:
		t += 1
print(arr)

#https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
