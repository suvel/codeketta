a=str(input())
b=str(input())
la=len(a)
lb=len(b)
delete=1
update=1
insert=1
if la>lb:
	for char in range(la-1,la-lb-1,-1):
		
		a = a.replace(a[char],"")
		delete=delete+1
		
for i in range(0,lb):
	if i>=la:
		a=a+b[i]
		insert=insert+1
	if b[i]!=a[i]:
		a[i]=b[i]
		update=update+1
print(delete+update+insert),
print(a)
