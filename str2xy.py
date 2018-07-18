R=raw_input()
j=len(R)
C=0
C1=0
P=0

for i in range(j):
	C=0
	for k in range(0,j):
		if(R[i]==R[k]):
			C=C+1
	if(C1==0):
		C1=C
		P=R[i]
	if(C1<C):
		C1=C
		P=R[i]
print(P)
