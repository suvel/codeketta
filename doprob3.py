def delin(i,j):
	val=ord(i[j])-64
	return val
def up(a,b,j):
	if ord(a[j])>ord(b[j]):
		
		val=(ord(a[j])-ord(b[j]))
	else:
	#	print(ord(b[j])),print(ord(a[j]))
		val=(ord(b[j])-ord(a[j]))
		
	return val	

#--------------------------------------------------------------
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
		delete=delete+delin(a.upper(),char)
		a = a.replace(a[char],"")
		
	la=len(a)	
for i in range(0,lb):
	#print(str(la)+"b"+str(i))
	if i>=la:
		#print(b[i])
		insert=insert+delin(b.upper(),i)
	
	else:
		#print("a"+str(i))
		if b[i]!=a[i]:
			update=update+up(a.upper(),b.upper(),i)
		
print(delete+update+insert)


