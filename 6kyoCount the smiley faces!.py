arr = list(input().split())
print(arr)
s = 0
for i in arr:
	print(len(i))
	if len(i) >= 2 and (i[0] == ":" or i[0] == ";"):
		if (i[1] == "D" or i[1] == ")") and len(i)==2:
			s+=1
		elif len(i) == 3 and (i[1] == "-" or i[1] == '~'):
			if i[2] == "D" or i[2] == ')':
				s += 1
			else:
				continue
		else:
			continue
	else:
		continue
print(s)
