N,Q=input().split()
N,Q=int(N),int(Q)
A=[]
A=input().split()
b=int(input())
sum=0
for i in range(len(A)):
	if(i==Q):
		pass
	else:
		sum=sum+int(A[i])

sum=sum/2		
if(b-(sum)):
	print(int(b-(sum)))
else:
	print("Bon Appetit")
	
