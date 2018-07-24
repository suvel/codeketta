A=str(input())
B=str(input())
i=['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for j in range(len(A)):
	#print(A[j]),print(B[j])
	Q=i.index(A[j])+i.index(B[j])
	if(Q>26):
		print(i[Q-26],end='')
	else:
		print(i[Q],end='')
