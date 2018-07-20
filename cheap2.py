a,b=input().split()
a=str(a)
b=str(b)
la=len(a)
lb=len(b)
delete=0
update=0
insert=0
if la>lb:
	for char in range(la-1,la-lb,-1):
		delete=delete+1
		a = a.replace(a[char],"")
		
	la=len(a)	
for i in range(0,lb):
	#print(str(la)+"b"+str(i))
	if i>=la:
		#print(b[i])
		insert=insert+1
	
	else:
		#print("a"+str(i))
		if b[i]!=a[i]:
			update=update+1
		
print(delete+update+insert)

