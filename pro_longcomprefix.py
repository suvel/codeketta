N=int(input())
if(1<=N):
	A=[]
	for i in range (N):
		A.append(input())
	length=0
	tempN=N
	while(tempN>0):
		tempN=tempN-1
		if(length==0 or length>len(A[tempN])):
			length=len(A[tempN])
	temp=""		
	if(length<=100000):
		f=False
		for p in range(0,length):
			
			if(f==True):
				break
			
			#print("p"),print(p)
			tempN=N
			temp=""
			count=0
			while(tempN>0):
				tempN=tempN-1
				st=A[tempN]
				#print(str(tempN)+" "+st[p])
				if(temp=="" or temp==st[p]):
					temp=st[p]
					count=count+1
				else:
					f=True
					break
				if(count==N):
					print(st[p],end="")	
	
			
