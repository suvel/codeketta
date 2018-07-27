from itertools import permutations
l = list(permutations(str(input())))
k=0
for i in range(len(l)):
	if "donhi"==str(''.join(l[i])):
		k=1
		break
if(k==1):
	print("yes")
else:
	print("no")
