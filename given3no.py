
value=int(input())
j=int(input())
k=int(input())
sum=0
if value%2==0:
	while(sum<=value):
	
		if(sum==value):
			print("yes")
			break
		elif(sum>value):
			print("no")
			break
		else:
			sum=sum+k
		sum=sum+j	
else:
	print("no")
	
