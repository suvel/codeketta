N=int(input())
A={}
value=3
note=1
for i in range(0,N):
	if(value==1):
		A[i+1]=value
		value=2*A[note]
		note=i+2
	else:
		A[i+1]=value
		value=value-1
print(A[N])
	
	
