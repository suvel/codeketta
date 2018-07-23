N=int(input())
A=[]
A=input().split()
B=list()
if(1<=N and N<=100000):
	for i in range(N):
		count=1
		for j in range(i+1,N):
			if(A[i]==A[j]):
				count=count+1
		#print("A[i]:",end=" "),print(A[i]),	print("count:",end=" "),print(count),print("B:",end=" "),print(B)
		if(count>1 and int(A[i]) not in B):
			B.append(int(A[i]))
if(len(B)==0):
	print("unique")
else:
	B.sort()		
	print(*B)			
			
		
