print("enter the number to be reversed-")
try:
	i=int(input())
	print(i)
	if(i>=0):
		um=0
		while (i>0):
			um=um*10+(i%10)
			i=i/10
		print(um)			
	else:
		print("enter a positive integer")
	
except ValueError:
	print("enter a  integer")
     
