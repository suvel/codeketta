N=int(input())
str=[]
st=input().split()
count=0
for i in range(N):
	sum=0
	
	for j in range(i+1,N):
		if(st[i]>=st[j]):
			pass
		else:
			
			for k in range(j+1,N):
				if(st[j]>=st[k]):
					pass
				else:
					sum=int(st[i])*100+int(st[j])*10+int(st[k])
					count=count+1
					sum=0
					
print(count)				
