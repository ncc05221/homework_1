f = open("C:/059.fasta", "r")
str1 = f.read()
f.close()

list1 = str1.split('>') [1:]
list2 = list(s.split('\n', 1) for s in list1)

for l in list2:
	l[1] = l[1].replace('\n', '')

dic1 = {}
for l in list2:
	length = len(l[1])

numA = l[1].count('A')
numT = l[1].count('T')
numG = l[1].count('G')
numC = l[1].count('C')

print(numA)
print(numT)
print(numG)
print(numC)
