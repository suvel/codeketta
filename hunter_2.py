N=int(input())
A=[]
A=input().split()
B=list()
if(1<=N and N<=100000):
	for i in range(N):
		B.append(int(A[i]))
while(B):
	print(max(B),end="")
	if(max(B)==0):
		break
	else:
		
		B.pop(B.index(max(B)))
		
