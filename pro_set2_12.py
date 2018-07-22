import sys
N,K=input().split()
N=int(N)
K=int(K)
if(1<=N and K<=100000):
	sys.exit()
else:
	temp=0
	A=[]
	A=input().split()
	if(len(A)==N):
		for i in range (K):
			temp=A[i]
			A[i]=A[i+1]
			A[i+1]=temp
		for i in range(N):
			print(A[i],end="")
	
	
