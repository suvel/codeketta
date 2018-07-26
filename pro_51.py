def check(i):
	if i>0:
		return 1
	if i<0:
		return -1
N=int(input())
A=[]
A=input().split()
count=0
charge=0
l=list()
for i in range(N):
	count=0
	charge=0
	if(charge==0):
		charge=check(int(A[i]))
		#print(charge)
		count=count+1
	for h in range(i+1,N):
		if(check(int(A[h]))!=charge):
			count=count+1
			charge=check(int(A[h]))
		else:
			break
	l.append(count)
print(*l)	
		
			
