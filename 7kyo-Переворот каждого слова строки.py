text = input()
s = ""
n = text.split(" ")
for i in n:
	s += " " + i[::-1]
#return s[1:]
print(s[1:])
