def top_3_words(text):
    for c in text:
        if not (c.isalpha() or c=="'"):
            text = text.replace(c,' ')
    words,counts,out = [],[],[]
    for word in list(filter(None,text.lower().split())):
        if all([not c.isalpha() for c in word]):
            continue
        if word in words:
            counts[words.index(word)] += 1
        else:
            words.append(word); counts.append(0)
    while len(words)>0 and len(out)<3:
        out.append(words.pop(counts.index(max(counts))).lower())
        counts.remove(max(counts))
    return out





#text = input()
#from collections import Counter
#import heapq
#text = text.lower()
#arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#arrk =["'", " "]
#for i in range(len(text)):
#	if text[i] not in arr and text[i] not in arrk:
#		text = text.replace(text[i], " ")
#text = list(text.split(" "))
#i = 0
#while i != len(text):
#	if text[i] == "":
#		text.pop(i)
#		i -=1
#	i += 1
#for i in range(len(text)):
#	t = 0
#	for j in text[i]:
#		if j in arr:
#			t = 1
#			break
#	if t == 0:
#		text.pop(i)
#ctext = Counter(text)
#ctext_keys = list(ctext.keys())
#ctext_values = list(ctext.values())
#print(ctext_keys[0], ctext_keys[1],ctext_keys[2])
#print(ctext_values)
#s = list()
#if len(ctext) >= 3:
#	s.append(ctext_keys[ ctext_values.index( heapq.nlargest(3, ctext_values)[0])])
#	s.append(ctext_keys[ ctext_values.index( heapq.nlargest(3, ctext_values)[1])])
#	s.append(ctext_keys[ ctext_values.index( heapq.nlargest(3, ctext_values)[2])])
#elif len(ctext) == 2:
#	s.append(ctext_keys[ ctext_values.index( heapq.nlargest(3, ctext_values)[0])])
#	s.append(ctext_keys[ ctext_values.index( heapq.nlargest(3, ctext_values)[1])])
#elif len(ctext) == 1:
#	s.append(ctext_keys[ ctext_values.index( heapq.nlargest(3, ctext_values)[0])])
#print(ctext_keys[ ctext_values.index( heapq.nlargest(2, ctext_values)[1])])
#print(s)
