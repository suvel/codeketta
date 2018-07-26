def chQ(Q):
	if(len(Q)<0):
		return 0
	else:
		return len(Q)-1 
	
S=str(input())
Q=str(input())
l_Q=len(Q)
L=[]
R=[]
L,R=S.split('|')
while(l_Q):
	l_Q=chQ(Q)
	#print(l_Q)
	if(len(L)!=len(R) and l_Q>=0):
		while(len(L)!=len(R) and l_Q>=0):
			if(len(L)>len(R)):
				R=R+Q[l_Q]
			else:
				L=Q[l_Q]+L
			l_Q=l_Q-1
	elif(l_Q>0 and l_Q%2==0):
		l_Q=l_Q
		L=Q[l_Q]+L
		
		l_Q=l_Q
		R=R+Q[l_Q]
	else:
		print("Impossible")
		break
	
	if(len(L)==len(R) and l_Q==0):
		print(L,end="")
		print("|",end="")
		print(R)
		break
	
	
	
