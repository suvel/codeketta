N=int(input())
A=[]
A=input().split()
count=0
for i in range(len(A)):
	for j in range(i+1,len(A)):
		for k in range(j+1,len(A)):
			if(int(A[i])>int(A[j])>int(A[k])):
				count=count+1
print(count)
