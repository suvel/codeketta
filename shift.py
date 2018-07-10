def rightrot (K,N,arryn):
	
	for u in range (0,K):
		temp=arryn[N-1]
		for  g in range (N-1,0,-1):
				arryn[g]=arryn[g-1]
				
		arryn[0]=temp
		
	           
	return arryn
			
N=input()
K=input()
arryn=[]
j=raw_input()
arryn=j.split(' ',N-1)
arryn=rightrot(K,N,arryn)
iny=map(int,arryn)
for i in range(0,N):
	print(iny[i]),
	
	
