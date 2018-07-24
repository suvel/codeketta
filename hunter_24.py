N,K=input().split()
N,K=int(N),int(K)
A=[]
A=input().split()
for i in range(N):
	for j in range(i+1,N):
		if(K==(i+j)):
			print("YES")
			exit()
		
			
print("NO")
