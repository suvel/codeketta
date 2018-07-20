N=int(input())
if(1<=N and N<=100000):
	a=[]
	a=input().split()
	sum=0
	for j in range(N):
		for i in range(0,j):
			if(a[0]!=a[j] and a[j]>a[i]):
				sum=sum+int(a[i])
			else:
				sum=sum+0;
	print(sum)
	
