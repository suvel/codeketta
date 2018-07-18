value,j,k=raw_input().split()
value=int(value)
j=int(j)
k=int(k)
sum=0
if value%2==0:
	value=value/2;
	while(sum!=value):
		sum=sum+j
		if(sum<value):
			sum=sum+k
		
		if(sum==value):
			print("yes")
			break
		if(sum>value):
			print("no")
			break
		
		print("sum--"+str(sum))	
else:
	print("no")
	
