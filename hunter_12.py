N=str(input())
N_S=len(N)
A=list()
for i in range(N_S-1,-1,-1):
	A.append(N[i])
print("".join(A))	
	
