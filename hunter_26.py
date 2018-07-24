N=int(input())
A=[]
A=input().split()
for i in range(N-1,0,-1):
	print(str(A[i])+"->",end="")
print(str(A[0]))	
