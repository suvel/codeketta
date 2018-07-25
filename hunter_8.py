N=int(input())
A=[]
A=input().split()
for i in range(N):
	for j in range(i+1,N):
		for k in range(j+1,N):
			if(int(A[i])+int(A[j])==int(A[k])):
				print(str(A[i])+""+str(A[j])+""+str(A[k]))
				
