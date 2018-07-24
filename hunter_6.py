N=int(input())
A=[]
A=input().split()
dif=N
for i in range(N):
	for j in range(i+1,N):
		if(A[i]==A[j] and (j-i)<dif):
			dif=j-i
			g=int(A[i])
			
print(g)
