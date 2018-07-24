N,K=input().split()
N=int(N)
K=int(K)
A=[]
A=input().split()
B=list()
for i in range(N):
	B.append(int(A[i]))
while(K>1):
	M=max(B)
	B.pop(B.index(M))
	K=K-1
print(max(B))	
