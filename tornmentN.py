
def check():
	faz2=2
	count=0
	if(3<=val<=100000 and not(val & (val-1))):
		print("0")
	else:
		while(faz2<val):
			faz2=faz2*2
			count+=1
		print(count-1)
		
	

val=int(input())
if(3<=val<=100000):
	check()
else:
	print("enter value between 3-100000")
