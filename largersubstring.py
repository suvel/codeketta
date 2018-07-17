i=str(input())
inew=""
large_str=""
for j in range (0,len(i)):

	if(inew==""):
		inew=inew+i[j]
	elif i[j] in inew:
		if(len(inew)>len(large_str)):
			large_str=inew
		inew="";
		
	elif j==len(i)-1:
		large_str=inew
	else:
		inew=inew+i[j]
print(len(large_str))		
