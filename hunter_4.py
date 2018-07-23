N=int(input())
A=[]
A=input().split()
B=list()
if(1<=N and N<=100000):
	for i in range(N):
		count=1
		for j in range(i+1,N):
			if(A[i]==A[j]):
			#	print("A[i]"),print(A[i])
				B.append(int(A[i]))
		if(int(A[i]) not in B):
			print(A[i])
	
