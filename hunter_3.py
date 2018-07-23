N=int(input())
A=[]
A=input().split()
B=list()
if(1<=N and N<=100000):
	for i in range(N):
		if(i==int(A[i])):
			B.append(int(A[i]))
if(len(B)==0):
	print("-1")
else:
	B.sort()
	print(*B)
		
