text = input()
from collections import Counter 
text = text.lower()
arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
arrk =["'", " "]
for i in range(len(text)):
	if text[i] not in arr and text[i] not in arrk:
		text = text.replace(text[i], " ")
text = list(text.split(" "))
i = 0
while i != len(text):
	if text[i] == "":
		text.pop(i)
		i -=1
	i += 1
for i in range(len(text)):
	t = 0
	for j in text[i]:
		if j in arr:
			t = 1
			break
	if t == 0:
		text.pop(i)
ctext = Counter(text)
ctext_keys = list(ctext.keys())
ctext_values = list(ctext.values())
print(ctext_keys, ctext_values)

