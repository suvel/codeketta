def chek(s):
    if(s==s[::-1]):
        return 1
    else:
        return 0
def ck(A):
	s=list()
	for i in range (len(A)):
		s.append(A[i])
	for i in range (len(A)):
		sr= ''.join(s)
		if(chek(sr)==1):
			pass
		else:
			s.pop()

	return (len(A)-len(s))  

	
A=str(input())
if (ck(A)<ck(A[::-1])):
	print(ck(A))
else:
	print(ck(A[::-1]))
	
	
