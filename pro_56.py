N,K=input().split()
N,K=int(N),int(K)
A=[]
A=input().split()
MT=0
count=0
for i in range(N):
	MT=MT+(86400-int(A[i]))
	if(MT>=K):
		count=count+1
		print(count) 
		exit()
	if(MT<K):
		count=count+1
		
print(count) 
