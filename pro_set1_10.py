N=int(input())
if(1<=N and N<=100000):
	a=[]
	a=input().split()
	sum=0
	for j in range(N):
		for i in range(0,j):
			sum=sum+int(a[i])
			
	print(sum)
	
