def check(num):
	if num > 1 or num==2:
		for i in range(2,num):
			if (num % i) == 0:
				return 0
				
			else:
				return 1
		return 1

	else:
		return 0

i,j=input().split()
i=int(i)
j=int(j)
count=0
for j in range(i,j+1):
	H=bin(j)[2:]
	H=H.replace('0','')
	l=len(H)
	#print(l)
	#aprint(check(l))
	if(check(l)==1):
		count=count+1
	else:
		pass
print(count)	
	
