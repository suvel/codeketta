N=input().split()
N_S=len(N)
for i in range(N_S-1):
	print(N[i][::-1],end=" ")
print(N[N_S-1][::-1],end="")	
